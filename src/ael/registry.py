"""Inventory and validate existing content without moving source files.

Python 3.11+, standard library only. Run with: PYTHONPATH=src python -m ael.registry ...
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROVIDERS = (
    "anthropic", "openai", "langchain", "llamaindex", "modal",
    "e2b", "browser-use", "browserbase",
)
FIELDS = ("id", "kind", "source", "path", "review_status", "publication_status")
KINDS = {"source_article", "article_note", "paper"}
REVIEW = {"unreviewed", "verified", "rejected"}
PUBLICATION = {"unspecified", "published", "not_published", "archived"}
ID_PATTERN = re.compile(r"^(?:source|note|paper):[a-z0-9][a-z0-9._:-]*$")


def classify(relative_path: str) -> dict | None:
    """Classify one source path. Filenames are a bootstrap, not permanent identity."""
    p = Path(relative_path)
    if p.parts[:3] == ("content", "research", "article-notes"):
        if len(p.parts) != 5 or p.parts[3] not in (*PROVIDERS, "papers") or p.suffix.lower() != ".md":
            return None
        source = p.parts[3]
        slug = p.stem.lower()
        is_interrogation = slug.endswith("(musk-interrogation)")
        if is_interrogation:
            slug = slug.removesuffix("(musk-interrogation)")
        ident = f"note:{source}:{slug}" + (":interrogation" if is_interrogation else "")
        row = {
            "id": ident, "kind": "article_note", "source": source,
            "path": p.as_posix(), "review_status": "unreviewed",
            "publication_status": "unspecified",
        }
        if is_interrogation:
            row["related_ids"] = [f"paper:{slug}" if source == "papers" else f"source:{source}:{slug}"]
        return row
    if len(p.parts) < 2 or p.parts[0] not in (*PROVIDERS, "papers"):
        return None
    name = p.name
    if name.lower() in ("readme.md", "index.md"):
        return None
    if p.parts[0] == "papers":
        if p.suffix.lower() == ".pdf":
            kind = "paper"
        elif name.endswith("(musk-interrogation).md"):
            kind = "article_note"
        else:
            return None
    elif p.suffix.lower() != ".md":
        return None
    else:
        kind = "article_note" if "curated" in p.parts[1:-1] or name.endswith("(musk-interrogation).md") else "source_article"

    provider = p.parts[0]
    slug = p.stem.lower()
    is_interrogation = slug.endswith("(musk-interrogation)")
    if is_interrogation:
        slug = slug.removesuffix("(musk-interrogation)")
    if kind == "paper":
        ident = f"paper:{slug}"
    elif kind == "source_article":
        ident = f"source:{provider}:{slug}"
    else:
        ident = f"note:{provider}:{slug}" + (":interrogation" if is_interrogation else "")

    row = {
        "id": ident,
        "kind": kind,
        "source": provider,
        "path": p.as_posix(),
        "review_status": "unreviewed",
        "publication_status": "unspecified",
    }
    if is_interrogation:
        row["related_ids"] = [f"paper:{slug}" if provider == "papers" else f"source:{provider}:{slug}"]
    return row


def inventory(root: Path = ROOT) -> list[dict]:
    from .migration import read_moves
    aliases = {move["from"] for move in read_moves(root)}
    rows = []
    for provider in (*PROVIDERS, "papers"):
        base = root / provider
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                if relative in aliases:
                    continue
                record = classify(relative)
                if record:
                    rows.append(record)
    notes = root / "content" / "research" / "article-notes"
    if notes.is_dir():
        for path in notes.rglob("*.md"):
            if path.is_file():
                record = classify(path.relative_to(root).as_posix())
                if record:
                    rows.append(record)
    return sorted(rows, key=lambda row: row["id"])


def read_records(registry_path: Path) -> list[dict]:
    if not registry_path.exists():
        return []
    rows = []
    for line_no, raw in enumerate(registry_path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{registry_path}:{line_no}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{registry_path}:{line_no}: expected JSON object")
        rows.append(row)
    return rows


def sync(root: Path, registry_path: Path, write: bool = False) -> tuple[int, int]:
    """Append new files; keep existing records and IDs even if paths disappear."""
    old = read_records(registry_path)
    by_path = {row.get("path"): row for row in old}
    if len(by_path) != len(old):
        raise ValueError("duplicate paths in existing registry; refusing to overwrite")
    discovered = inventory(root)
    new_rows = [row for row in discovered if row["path"] not in by_path]
    seen_ids = {row.get("id") for row in old}
    for row in new_rows:
        if row["id"] in seen_ids:
            raise ValueError(f"ID collision: {row['id']}; resolve explicitly")
        seen_ids.add(row["id"])
    combined = sorted(old + new_rows, key=lambda row: row["id"])
    if write:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in combined)
        registry_path.write_text(payload, encoding="utf-8")
    return len(new_rows), len(combined)


def validate(root: Path, registry_path: Path) -> list[str]:
    errors = []
    try:
        rows = read_records(registry_path)
    except ValueError as exc:
        return [str(exc)]
    if not rows:
        return ["registry is empty"]
    ids, paths = set(), set()
    inventory_by_path = {row["path"]: row for row in inventory(root)}
    for i, row in enumerate(rows, 1):
        label = f"record {i} ({row.get('path', '?')})"
        for field in FIELDS:
            if not isinstance(row.get(field), str) or not row[field]:
                errors.append(f"{label}: missing or invalid {field}")
        if not all(field in row and isinstance(row[field], str) and row[field] for field in FIELDS):
            continue
        if row["id"] in ids:
            errors.append(f"{label}: duplicate id {row['id']}")
        ids.add(row["id"])
        if row["path"] in paths:
            errors.append(f"{label}: duplicate path")
        paths.add(row["path"])
        if not ID_PATTERN.fullmatch(row["id"]):
            errors.append(f"{label}: invalid id format")
        if row["kind"] not in KINDS or row["source"] not in (*PROVIDERS, "papers"):
            errors.append(f"{label}: invalid kind/source")
        if row["review_status"] not in REVIEW or row["publication_status"] not in PUBLICATION:
            errors.append(f"{label}: invalid status")
        expected = inventory_by_path.get(row["path"])
        if expected is None:
            errors.append(f"{label}: file missing or outside managed inventory")
        elif (row["kind"], row["source"]) != (expected["kind"], expected["source"]):
            errors.append(f"{label}: kind/source mismatch")
        url = row.get("canonical_url")
        if url is not None and (not isinstance(url, str) or not re.match(r"^https?://", url)):
            errors.append(f"{label}: invalid canonical_url")
        related = row.get("related_ids", [])
        if not isinstance(related, list) or any(not isinstance(r, str) for r in related):
            errors.append(f"{label}: related_ids must be a string array")
    for row in rows:
        for target in row.get("related_ids", []) if isinstance(row.get("related_ids", []), list) else []:
            if target not in ids:
                errors.append(f"{row.get('id')}: dangling related_ids target {target}")
    for path in sorted(inventory_by_path.keys() - paths):
        errors.append(f"unregistered content: {path}")
    from .migration import validate_moves
    errors.extend(validate_moves(root, rows))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("report", "sync", "validate"))
    parser.add_argument("--write", action="store_true", help="write new rows when syncing; never removes old records")
    args = parser.parse_args()
    registry_path = ROOT / "registry" / "records.jsonl"
    if args.command == "sync":
        new, total = sync(ROOT, registry_path, args.write)
        print(f"{new} new records; {total} total" + (" (written)" if args.write else " (dry run)"))
        return 0
    if args.command == "report":
        rows = read_records(registry_path)
        print(json.dumps({"total": len(rows), "by_kind": dict(Counter(r.get("kind") for r in rows)),
                          "by_source": dict(Counter(r.get("source") for r in rows))}, ensure_ascii=False, indent=2))
        return 0
    errors = validate(ROOT, registry_path)
    for error in errors[:50]:
        print(f"ERROR: {error}")
    if errors:
        print(f"Validation failed with {len(errors)} errors (first 50 shown)")
        return 1
    print(f"OK: {len(read_records(registry_path))} registered content records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
