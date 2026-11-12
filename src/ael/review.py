"""Evidence-first editorial queue and explicit topic decision validation.

This does not guess or create relationships from filenames or similar titles.
Only reviewed decisions with a current, matching content SHA are applied.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import tempfile
import os

from .registry import ROOT, read_records


class ReviewError(ValueError):
    pass


def canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def approved_topic_decisions(root: Path, rows: list[dict], topics: set[str]) -> dict[str, dict]:
    path = root / "registry" / "review-decisions.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("topic_decisions"), list):
        raise ReviewError("review-decisions.json must have schema_version=1 and topic_decisions array")
    if set(data) != {"schema_version", "topic_decisions"}:
        raise ReviewError("unexpected keys in review-decisions.json")
    by_id = {r["id"]: r for r in rows}
    accepted = {}
    for entry in data["topic_decisions"]:
        if not isinstance(entry, dict) or set(entry) != {
            "id", "topics", "evidence_sha256", "reviewer", "reviewed_at", "rationale"}:
            raise ReviewError("topic decision missing required evidence metadata")
        ident = entry["id"]
        row = by_id.get(ident)
        if not row or ident in accepted:
            raise ReviewError(f"{ident}: missing or duplicate record")
        assigned = entry["topics"]
        if (not isinstance(assigned, list) or len(assigned) != len(set(assigned)) or
                any(not isinstance(t, str) or t not in topics for t in assigned)):
            raise ReviewError(f"{ident}: unknown or duplicate topics")
        reviewer = entry["reviewer"]
        rationale = entry["rationale"]
        if not isinstance(reviewer, str) or len(reviewer.strip()) < 2:
            raise ReviewError(f"{ident}: reviewer must explicitly identify the editor")
        if not isinstance(rationale, str) or len(rationale.strip()) < 20:
            raise ReviewError(f"{ident}: rationale must describe document evidence")
        try:
            date.fromisoformat(entry["reviewed_at"])
        except (TypeError, ValueError):
            raise ReviewError(f"{ident}: invalid review date") from None
        expected_sha = row.get("source_sha256")
        if not expected_sha:
            expected_sha = hashlib.sha256((root / row["path"]).read_bytes()).hexdigest()
        if entry["evidence_sha256"] != expected_sha:
            raise ReviewError(f"{ident}: evidence content hash does not match current source")
        accepted[ident] = entry
    return accepted



def approved_content_decisions(root: Path, rows: list[dict]) -> dict[str, str]:
    """Resolve append-only editorial events against current content bytes.

    A manual change to Registry review_status is not an approval. Any later
    content modification invalidates the last approval until reviewed again.
    """
    path = root / "registry" / "content-review-decisions.json"
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if (not isinstance(data, dict) or set(data) != {"schema_version", "events"}
            or data["schema_version"] != 1 or not isinstance(data["events"], list)):
        raise ReviewError("content-review-decisions.json requires schema_version=1 and events array")
    records = {row["id"]: row for row in rows}
    seen_events: set[str] = set()
    latest: dict[str, dict] = {}
    for event in data["events"]:
        required = {"event_id", "id", "action", "evidence_sha256",
                    "reviewer", "reviewed_at", "rationale", "evidence_urls"}
        if not isinstance(event, dict) or set(event) != required:
            raise ReviewError("content review event has missing or unsupported fields")
        event_id, ident = event["event_id"], event["id"]
        if (not isinstance(event_id, str) or not event_id.strip()
                or event_id in seen_events or not isinstance(ident, str) or ident not in records):
            raise ReviewError(f"invalid/duplicate event or unknown record: {event_id}")
        seen_events.add(event_id)
        if event["action"] not in {"approve", "reject", "revoke"}:
            raise ReviewError(f"{event_id}: invalid review action")
        if not isinstance(event["reviewer"], str) or len(event["reviewer"].strip()) < 2:
            raise ReviewError(f"{event_id}: reviewer identity required")
        if not isinstance(event["rationale"], str) or len(event["rationale"].strip()) < 20:
            raise ReviewError(f"{event_id}: evidence rationale required")
        try:
            reviewed_at = date.fromisoformat(event["reviewed_at"])
        except (TypeError, ValueError):
            raise ReviewError(f"{event_id}: invalid review date") from None
        urls = event["evidence_urls"]
        if (not isinstance(urls, list) or len(urls) != len(set(map(str, urls)))
                or any(not isinstance(url, str) or not url.startswith("https://") for url in urls)):
            raise ReviewError(f"{event_id}: evidence_urls must be unique HTTPS URLs")
        if event["action"] == "approve" and not urls:
            raise ReviewError(f"{event_id}: approval requires primary-source evidence URLs")
        digest = event["evidence_sha256"]
        if (not isinstance(digest, str) or len(digest) != 64
                or any(char not in "0123456789abcdef" for char in digest)):
            raise ReviewError(f"{event_id}: invalid evidence SHA-256")
        if ident in latest and reviewed_at < date.fromisoformat(latest[ident]["reviewed_at"]):
            raise ReviewError(f"{event_id}: history must be chronological")
        latest[ident] = event

    statuses = {}
    for ident, event in latest.items():
        content_path = (root / records[ident]["path"]).resolve()
        if not content_path.is_relative_to(root.resolve()) or not content_path.is_file():
            raise ReviewError(f"{ident}: missing or unsafe reviewed content")
        current_sha = hashlib.sha256(content_path.read_bytes()).hexdigest()
        if event["evidence_sha256"] != current_sha:
            raise ReviewError(f"{ident}: stale content approval; re-review or revoke explicitly")
        statuses[ident] = {"approve": "verified", "reject": "rejected",
                           "revoke": "unreviewed"}[event["action"]]
    return statuses


def build_queue(rows: list[dict], audit: dict) -> dict:
    links = audit.get("note_reference_links")
    if not isinstance(links, list):
        raise ReviewError("audit missing per-note provenance statuses")
    by_id = {r["id"]: r for r in rows}
    unlinked = set(audit.get("unlinked_notes", []))
    seen = set()
    items = []
    actions = {
        "external_only": "Verify cited original, ingest it if appropriate, then link by exact source evidence",
        "no_explicit_citation": "Find and document the original citation; do not infer from title alone",
        "linked_by_id_url_mismatch": "Verify official URL redirect or archival alias; preserve current stable-ID link",
        "ambiguous": "Disambiguate explicit citation candidates with publisher evidence",
    }
    for link in links:
        if not isinstance(link, dict) or not isinstance(link.get("id"), str):
            raise ReviewError("invalid source audit item")
        ident = link["id"]
        if ident in seen or ident not in by_id:
            raise ReviewError(f"duplicate/unknown source audit ID: {ident}")
        seen.add(ident)
        row = by_id[ident]
        status = link.get("status")
        if ident not in unlinked and status != "linked_by_id_url_mismatch" and status != "ambiguous":
            continue
        if status not in actions:
            raise ReviewError(f"unexpected review status for {ident}: {status}")
        item = {
            "id": ident, "title": row.get("title") or Path(row["path"]).stem,
            "path": row["path"], "source": row["source"],
            "source_sha256": row["source_sha256"],
            "reference_status": status,
            "has_local_source": ident not in unlinked,
            "required_action": actions[status],
        }
        if row.get("source_reference_url"):
            item["explicit_reference_url"] = row["source_reference_url"]
        if row.get("related_ids"):
            item["related_ids"] = row["related_ids"]
        items.append(item)
    if not unlinked.issubset(seen):
        raise ReviewError("audit unlinked notes missing from detailed reference list")
    ordered = sorted(items, key=lambda item: (
        {"linked_by_id_url_mismatch": 0, "ambiguous": 1, "external_only": 2,
         "no_explicit_citation": 3}[item["reference_status"]], item["id"]))
    return {
        "schema_version": 1,
        "total": len(ordered), "unlinked": len(unlinked),
        "needs_url_alias_verification": sum(item["reference_status"] == "linked_by_id_url_mismatch"
                                            for item in ordered),
        "status_counts": dict(sorted(Counter(item["reference_status"] for item in ordered).items())),
        "items": ordered,
        "policy": "Evidence queue only; no source ID guessed from titles or similarity",
    }


def generate(root: Path = ROOT) -> tuple[Path, str, dict]:
    rows = read_records(root / "registry" / "records.jsonl")
    audit = json.loads((root / "registry" / "audit-report.json").read_text(encoding="utf-8"))
    from .knowledge import load_taxonomy
    approved_topic_decisions(root, rows, {t["id"] for t in load_taxonomy(root)["topics"]})
    approved_content_decisions(root, rows)
    queue = build_queue(rows, audit)
    return root / "registry" / "review-queue.json", canonical(queue), queue


def run(root: Path = ROOT, write: bool = False, check: bool = False) -> dict:
    if write and check:
        raise ReviewError("--write and --check cannot be combined")
    root = root.resolve()
    path, expected, queue = generate(root)
    drift = not path.is_file() or path.read_text(encoding="utf-8") != expected
    if check and drift:
        raise ReviewError("review queue has drift; regenerate after changing source evidence")
    if write and drift:
        temp = None
        try:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                             prefix=".review-", suffix=".tmp", delete=False) as f:
                temp = f.name
                f.write(expected)
                f.flush()
                os.fsync(f.fileno())
            os.replace(temp, path)
        finally:
            if temp:
                Path(temp).unlink(missing_ok=True)
    return {"total": queue["total"], "unlinked": queue["unlinked"],
            "url_alias_verification": queue["needs_url_alias_verification"],
            "status_counts": queue["status_counts"],
            "changed": bool(drift and write), "dry_run": not write}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = run(write=args.write, check=args.check)
    except (ReviewError, KeyError, ValueError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
