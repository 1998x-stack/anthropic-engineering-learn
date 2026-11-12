"""Non-destructive provenance reconciliation for the content registry.

This reads legacy metadata, frontmatter, article headers, and built HTML.
It never edits legacy sources. Repository-derived metadata is provisional;
officially verified exceptions live in registry/verified-overrides.json.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit

from .registry import ROOT, read_records, validate

COMPUTED_FIELDS = ("title", "author", "canonical_url", "published_at")
UNKNOWN = {"", "unknown", "n/a", "none", "null", "not found", "untitled", "undefined"}
EXPECTED_HOSTS = {
    "anthropic": ("anthropic.com",),
    "openai": ("openai.com",),
    "langchain": ("langchain.com",),
    "llamaindex": ("llamaindex.ai",),
    "modal": ("modal.com",),
    "e2b": ("e2b.dev",),
    "browser-use": ("browser-use.com",),
    "browserbase": ("browserbase.com",),
}
FIELD_MAP = {"date": "published_at", "url": "canonical_url",
             "title": "title", "author": "author"}


def clean(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    value = value.strip().strip('"').strip("'").strip()
    return value if value and value.lower() not in UNKNOWN else None


def clean_date(value: object) -> str | None:
    value = clean(value)
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10]).isoformat() if re.fullmatch(r"\d{4}-\d{2}-\d{2}.*", value) else None
    except ValueError:
        return None


def clean_url(value: object, source: str) -> str | None:
    value = clean(value)
    if not value:
        return None
    try:
        split = urlsplit(value)
        host = (split.hostname or "").lower()
        if split.scheme != "https" or not split.netloc or split.username or split.password:
            return None
        if not any(host == h or host.endswith("." + h) for h in EXPECTED_HOSTS.get(source, ())):
            return None
        return urlunsplit(("https", host, split.path.rstrip("/") or "/", "", ""))
    except ValueError:
        return None


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        matched = re.match(r"^([A-Za-z][\w-]*):\s*(.*?)\s*$", line)
        if matched:
            data[matched.group(1).lower()] = matched.group(2)
    return data


def first_heading(text: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", text[:6000], re.MULTILINE)
    return clean(match.group(1)) if match else None


def quoted_header(text: str) -> dict[str, str]:
    section = text[:1800]
    values = {}
    for field, regex in (
        ("published_at", r"^>\s*\*\*Published:\*\*\s*(\d{4}-\d{2}-\d{2})"),
        ("canonical_url", r"^>\s*\*\*Source:\*\*\s*\[[^\]]+\]\((https://[^)]+)\)"),
    ):
        m = re.search(regex, section, re.MULTILINE)
        if m:
            values[field] = m.group(1)
    return values


def legacy_indexes(root: Path) -> dict[str, dict]:
    path = root / "index.json"
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {"anthropic/" + item["file"].lstrip("/"): item
            for item in data.get("articles", []) if isinstance(item, dict) and item.get("file")}


def legacy_meta_path(root: Path, row: dict) -> Path | None:
    if row["kind"] != "source_article":
        return None
    path = root / "_meta" / row["source"] / (Path(row["path"]).stem + ".json")
    return path if path.is_file() else None


def published_path(root: Path, row: dict) -> str | None:
    stem = Path(row["path"]).stem
    source = row["source"]
    candidates = [Path("docs") / source / (stem + ".html")]
    if source == "anthropic":
        parts = Path(row["path"]).parts
        if len(parts) > 2:
            candidates.insert(0, Path("docs") / source / parts[1] / (stem + ".html"))
    return next((p.as_posix() for p in candidates if (root / p).is_file()), None)


def read_overrides(root: Path) -> dict[str, dict]:
    path = root / "registry" / "verified-overrides.json"
    if not path.exists():
        return {}
    values = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(values, dict):
        raise ValueError("verified-overrides.json must be a JSON object")
    for ident, entry in values.items():
        if not isinstance(entry, dict) or not entry.get("evidence_url"):
            raise ValueError(f"{ident}: override requires evidence_url")
        if not isinstance(entry["evidence_url"], str) or not entry["evidence_url"].startswith("https://"):
            raise ValueError(f"{ident}: invalid evidence_url")
        if any(k not in ("canonical_url", "published_at", "title", "author", "evidence_url") for k in entry):
            raise ValueError(f"{ident}: unsupported override field")
    return values


def enrich(root: Path, records: list[dict]) -> tuple[list[dict], dict]:
    """Apply deterministic, explicit source precedence; audit all disagreements."""
    legacy = legacy_indexes(root)
    overrides = read_overrides(root)
    ids = {r["id"] for r in records}
    if overrides.keys() - ids:
        raise ValueError("unknown override IDs: " + ", ".join(sorted(overrides.keys() - ids)))
    used_meta = set()
    conflicts = []
    invalid = []
    output = []
    source_urls: dict[str, list[str]] = defaultdict(list)
    note_urls: dict[str, str] = {}

    for row in records:
        rec = dict(row)
        path = root / row["path"]
        if not path.is_file():
            raise FileNotFoundError(row["path"])
        rec["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        html = published_path(root, row)
        if rec.get("publication_status") != "archived":
            rec["publication_status"] = "published" if html else "not_published"
        if html:
            rec["site_path"] = html
        else:
            rec.pop("site_path", None)

        data = path.read_text(encoding="utf-8") if path.suffix == ".md" else ""
        fm = frontmatter(data) if data else {}
        candidates: dict[str, list[tuple[int, str, str]]] = defaultdict(list)

        def put(field: str, value: object, origin: str, priority: int) -> None:
            cleaned = clean_date(value) if field == "published_at" else (
                clean_url(value, row["source"]) if field == "canonical_url"
                else clean(value))
            if cleaned is not None:
                candidates[field].append((priority, origin, cleaned))
            elif clean(value) and field in ("canonical_url", "published_at"):
                invalid.append({"id": row["id"], "field": field, "origin": origin, "raw": str(value)[:180]})

        if row["kind"] == "source_article":
            for key, field in FIELD_MAP.items():
                put(field, fm.get(key), row["path"] + "#frontmatter", 10)
            h = quoted_header(data)
            for field, value in h.items():
                put(field, value, row["path"] + "#header", 15)
            index = legacy.get(row["path"])
            if index:
                for key, field in FIELD_MAP.items():
                    put(field, index.get(key), "index.json#" + row["path"], 30)
            metadata_path = legacy_meta_path(root, row)
            if metadata_path:
                rel = metadata_path.relative_to(root).as_posix()
                used_meta.add(rel)
                try:
                    obj = json.loads(metadata_path.read_text(encoding="utf-8"))
                    if isinstance(obj, dict):
                        for key, field in FIELD_MAP.items():
                            put(field, obj.get(key), rel, 20)
                    else:
                        invalid.append({"id": row["id"], "field": "meta_file", "origin": rel, "raw": "not a JSON object"})
                except (OSError, ValueError) as exc:
                    invalid.append({"id": row["id"], "field": "meta_file", "origin": rel, "raw": str(exc)[:180]})
            put("title", first_heading(data), row["path"] + "#heading", 40)
            verified = overrides.get(row["id"])
            if verified:
                for field in COMPUTED_FIELDS:
                    if field in verified:
                        put(field, verified[field], "registry/verified-overrides.json#" + row["id"], 0)
        elif row["kind"] == "article_note":
            put("title", first_heading(data), row["path"] + "#heading", 10)
            # A note cites its subject: it does not inherit the source's author/date.
            head = data[:1200]
            m = re.search(r"\*\*来源[:：]\*\*.*?\((https://[^)]+)\)", head)
            if not m:
                m = re.search(r"^>\s*\*\*分析对象\*\*[:：]?\s*\[[^\]]+\]\((https://[^)]+)\)", head, re.MULTILINE)
            if m and row["source"] != "papers":
                url = clean_url(m.group(1), row["source"])
                if url:
                    note_urls[row["id"]] = url

        evidence = dict(rec.get("metadata_provenance", {}))
        for field in COMPUTED_FIELDS:
            ranked = sorted(candidates.get(field, ()), key=lambda item: (item[0], item[1]))
            if not ranked:
                continue
            _, origin, chosen = ranked[0]
            rec[field] = chosen
            evidence[field] = origin
            distinct = sorted({value for _, _, value in ranked})
            if len(distinct) > 1:
                conflicts.append({"id": row["id"], "field": field, "chosen": chosen,
                                  "candidates": [{"value": v, "origin": o} for _, o, v in ranked]})
        if evidence:
            rec["metadata_provenance"] = evidence
        if row["kind"] == "source_article" and rec.get("canonical_url"):
            source_urls[rec["canonical_url"]].append(row["id"])
        output.append(rec)

    duplicates = [{"url": url, "ids": sorted(members)} for url, members in sorted(source_urls.items())
                  if len(members) > 1]
    target_by_url = {url: members[0] for url, members in source_urls.items() if len(members) == 1}
    linked = 0
    for rec in output:
        if rec["kind"] != "article_note":
            continue
        target = target_by_url.get(note_urls.get(rec["id"], ""))
        if target and target != rec["id"]:
            related = list(rec.get("related_ids", []))
            if target not in related:
                related.append(target)
            rec["related_ids"] = sorted(set(related))
            linked += 1

    legacy_files = {(p.relative_to(root)).as_posix() for p in (root / "_meta").rglob("*.json")} if (root / "_meta").exists() else set()
    site_files = {(p.relative_to(root)).as_posix() for p in (root / "docs").rglob("*.html")} if (root / "docs").exists() else set()
    site_files = {x for x in site_files if not x.endswith("/index.html")}
    indexed_site_files = {r["site_path"] for r in output if r.get("site_path")}
    unlinked_notes = sorted(r["id"] for r in output if r["kind"] == "article_note" and not r.get("related_ids"))
    missing_urls = sorted(r["id"] for r in output if r["kind"] == "source_article" and not r.get("canonical_url"))
    missing_dates = sorted(r["id"] for r in output if r["kind"] == "source_article" and not r.get("published_at"))
    missing_authors = sorted(r["id"] for r in output if r["kind"] == "source_article" and not r.get("author"))
    source_hashes = len([r for r in output if r.get("source_sha256")])
    report = {
        "schema_version": 1,
        "total_records": len(output),
        "by_kind": dict(sorted(Counter(r["kind"] for r in output).items())),
        "by_source": dict(sorted(Counter(r["source"] for r in output).items())),
        "source_hashes": source_hashes,
        "with_source_url": sum(bool(r.get("canonical_url")) for r in output if r["kind"] == "source_article"),
        "with_source_date": sum(bool(r.get("published_at")) for r in output if r["kind"] == "source_article"),
        "with_source_author": sum(bool(r.get("author")) for r in output if r["kind"] == "source_article"),
        "reviewed_records": sum(r["review_status"] == "verified" for r in output),
        "officially_verified_field_records": sum(any(str(origin).startswith("registry/verified-overrides.json#") for origin in r.get("metadata_provenance", {}).values()) for r in output),
        "site_html_present": sum(bool(r.get("site_path")) for r in output),
        "publication_status": dict(sorted(Counter(r["publication_status"] for r in output).items())),
        "legacy_metadata": {
            "total_files": len(legacy_files),
            "matched": len(used_meta),
            "unmatched": sorted(legacy_files - used_meta),
            "anthropic_index_matched": sum(r["path"] in legacy for r in output if r["kind"] == "source_article"),
        },
        "missing_source_url": missing_urls,
        "missing_source_date": missing_dates,
        "missing_source_author": missing_authors,
        "unlinked_notes": unlinked_notes,
        "note_source_url_matched": linked,
        "unmapped_site_html": sorted(site_files - indexed_site_files),
        "duplicate_source_urls": duplicates,
        "field_conflicts": sorted(conflicts, key=lambda c: (c["id"], c["field"])),
        "invalid_candidates": sorted(invalid, key=lambda c: (c["id"], c["field"], c["origin"])),
        "manual_review_needed": sorted(set(missing_urls + missing_dates + missing_authors + unlinked_notes +
                                           [c["id"] for c in conflicts] + [c["id"] for c in invalid] +
                                           [ident for d in duplicates for ident in d["ids"]])),
    }
    return sorted(output, key=lambda r: r["id"]), report


def render_records(rows: list[dict]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("apply", "check", "report"))
    args = parser.parse_args()
    registry_path = ROOT / "registry" / "records.jsonl"
    report_path = ROOT / "registry" / "audit-report.json"
    records, report = enrich(ROOT, read_records(registry_path))
    if args.command == "report":
        overview = {k: v for k, v in report.items()
                    if isinstance(v, (int, dict)) and k != "legacy_metadata"}
        overview["legacy_metadata_matched"] = report["legacy_metadata"]["matched"]
        overview["field_conflicts"] = len(report["field_conflicts"])
        overview["unlinked_notes"] = len(report["unlinked_notes"])
        overview["manual_review_needed"] = len(report["manual_review_needed"])
        print(json.dumps(overview, indent=2, ensure_ascii=False))
        return 0
    contents = {
        registry_path: render_records(records),
        report_path: json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
    }
    if args.command == "check":
        changed = [p for p, content in contents.items()
                   if not p.is_file() or p.read_text(encoding="utf-8") != content]
        if changed:
            print("Metadata drift detected: " + ", ".join(str(p.relative_to(ROOT)) for p in changed))
            return 1
        errors = validate(ROOT, registry_path)
        if errors:
            print("Registry validation errors: " + "; ".join(errors[:10]))
            return 1
        print(f"OK: {len(records)} records; {report['site_html_present']} site pages; "
              f"{len(report['field_conflicts'])} provisional field disagreements")
        return 0
    for p, content in contents.items():
        p.write_text(content, encoding="utf-8")
    errors = validate(ROOT, registry_path)
    if errors:
        print("Registry validation errors: " + "; ".join(errors[:10]))
        return 1
    print(f"Wrote {len(records)} records and metadata audit report")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
