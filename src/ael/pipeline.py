"""Safe local content pipeline: discover, normalize, validate, reconcile, publish.

This replaces *entrypoints*, not historical crawler implementations. No network
access is performed and no legacy Markdown/HTML or _meta files are modified.
Python 3.11+, standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile

from .reconcile import enrich, render_records
from .registry import ROOT, inventory, read_records, validate


class PipelineError(RuntimeError):
    """Reject operations that might create inconsistent or destructive state."""


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def registry_paths(root: Path) -> tuple[Path, Path]:
    return root / "registry" / "records.jsonl", root / "registry" / "audit-report.json"


def discover(root: Path) -> dict:
    """Compare filesystem inventory to Registry without modifying anything."""
    registry_path, _ = registry_paths(root)
    existing = read_records(registry_path)
    observed = inventory(root)
    by_path = {r["path"]: r for r in existing}
    if len(by_path) != len(existing):
        raise PipelineError("Duplicate registered paths; manual resolution required")
    ids = {r["id"] for r in existing}
    if len(ids) != len(existing):
        raise PipelineError("Duplicate registered IDs; manual resolution required")

    new = [r for r in observed if r["path"] not in by_path]
    stale = [r["path"] for r in existing if r["path"] not in {o["path"] for o in observed}]
    collisions = [r["id"] for r in new if r["id"] in ids]
    return {
        "existing": len(existing), "discovered": len(observed),
        "new_paths": sorted(r["path"] for r in new),
        "stale_paths": sorted(stale), "id_collisions": sorted(collisions),
        "new_records": new, "existing_records": existing,
    }


def plan(root: Path) -> dict:
    """Prepare a dry-run plan; source files remain byte-for-byte unchanged."""
    state = discover(root)
    records = state["existing_records"]
    if state["stale_paths"] or state["id_collisions"]:
        raise PipelineError("Stale paths or identifier collisions; fix manually before reconciliation")
    merged = records + state["new_records"]
    transformed, audit = enrich(root, merged)
    catalog = build_catalog(root, transformed, audit)
    registry_path, report_path = registry_paths(root)
    proposed = {registry_path: render_records(transformed),
                report_path: canonical_json(audit)}
    changed = [p.relative_to(root).as_posix() for p, text in proposed.items()
               if not p.exists() or p.read_text(encoding="utf-8") != text]
    return {
        "registered": len(records),
        "discovered": state["discovered"],
        "new_content": len(state["new_records"]),
        "stale_content": len(state["stale_paths"]),
        "id_collisions": len(state["id_collisions"]),
        "metadata_changed_files": sorted(changed),
        "valid_source_urls": audit["with_source_url"],
        "dated_sources": audit["with_source_date"],
        "metadata_conflicts": len(audit["field_conflicts"]),
        "manual_review_needed": len(audit["manual_review_needed"]),
        "published_catalog_entries": catalog["count"],
    }


def prepare(root: Path, include_new: bool = False) -> tuple[list[dict], dict]:
    state = discover(root)
    if state["stale_paths"]:
        raise PipelineError("Missing registered paths (no automatic deletes or moves): " +
                            ", ".join(state["stale_paths"][:10]))
    if state["id_collisions"]:
        raise PipelineError("Stable ID collisions require manual resolution: " +
                            ", ".join(state["id_collisions"][:10]))
    if state["new_records"] and not include_new:
        raise PipelineError(f"{len(state['new_records'])} new file(s) must be ingested first")
    rows = state["existing_records"] + (state["new_records"] if include_new else [])
    enriched, audit = enrich(root, rows)
    if len(enriched) != len(rows):
        raise PipelineError("Reconciliation changed record cardinality")
    if {r["id"] for r in enriched} != {r["id"] for r in rows}:
        raise PipelineError("Reconciliation unexpectedly changed stable IDs")
    return enriched, audit


def safe_write(root: Path, changes: dict[Path, str]) -> list[str]:
    """Allowlist-only, atomic-per-file writes with best-effort rollback.

    A crash between replacements can leave partial generated outputs; running
    'check' detects such drift. No source asset is ever an allowed target.
    """
    allowed = {*registry_paths(root), root / "docs" / "catalog.json"}
    if not changes or set(changes) - allowed:
        raise PipelineError("Refusing to write outside known generated outputs")
    snapshots = {p: p.read_bytes() if p.is_file() else None for p in changes}
    updates = [(p, text) for p, text in changes.items()
               if snapshots[p] != text.encode("utf-8")]
    staged: dict[Path, Path] = {}
    completed: list[Path] = []
    try:
        for target, content in updates:
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                             dir=target.parent, prefix=".ael-",
                                             suffix=".tmp", delete=False) as f:
                tmp = Path(f.name)
                staged[target] = tmp
                f.write(content)
                f.flush()
                os.fsync(f.fileno())
        for target, _ in updates:
            os.replace(staged.pop(target), target)
            completed.append(target)
    except Exception:
        for target in reversed(completed):
            before = snapshots[target]
            if before is None:
                target.unlink(missing_ok=True)
            else:
                # Rollback is intentionally best effort: never touches source assets.
                target.write_bytes(before)
        raise
    finally:
        for tmp in staged.values():
            tmp.unlink(missing_ok=True)
    return [target.relative_to(root).as_posix() for target, _ in updates]


def generated_outputs(root: Path, rows: list[dict], audit: dict) -> dict[Path, str]:
    registry_path, report_path = registry_paths(root)
    return {registry_path: render_records(rows), report_path: canonical_json(audit)}


def build_catalog(root: Path, records: list[dict], audit: dict | None = None) -> dict:
    """Full searchable Registry index, retaining the published 'items' contract."""
    from .knowledge import KnowledgeError, build_index

    try:
        result = build_index(root, records, audit)
    except KnowledgeError as exc:
        raise PipelineError(str(exc)) from exc
    page_paths, ids = set(), set()
    for item in result["items"]:
        page = item.get("site_path")
        if not isinstance(page, str):
            raise PipelineError(f"{item['id']}: published entry missing site_path")
        rel = Path(page)
        if (rel.is_absolute() or ".." in rel.parts or len(rel.parts) < 3
                or rel.parts[0] != "docs" or rel.suffix != ".html"):
            raise PipelineError(f"{item['id']}: unsafe site_path: {page}")
        if not (root / rel).is_file():
            raise PipelineError(f"{item['id']}: missing published HTML: {page}")
        if page in page_paths or item["id"] in ids:
            raise PipelineError(f"Duplicate site path or ID: {item['id']}")
        page_paths.add(page)
        ids.add(item["id"])
    return result


def verify(root: Path, check_catalog: bool = True) -> dict:
    registry_path, _ = registry_paths(root)
    errors = validate(root, registry_path)
    if errors:
        raise PipelineError("Registry invalid: " + "; ".join(errors[:8]))
    rows, audit = prepare(root, include_new=False)
    drift = [p.relative_to(root).as_posix()
             for p, expected in generated_outputs(root, rows, audit).items()
             if not p.is_file() or p.read_text(encoding="utf-8") != expected]
    if drift:
        raise PipelineError("Generated metadata drift: " + ", ".join(drift))
    catalog = build_catalog(root, rows, audit)
    existing_catalog = root / "docs" / "catalog.json"
    if check_catalog and existing_catalog.exists() and existing_catalog.read_text(encoding="utf-8") != canonical_json(catalog):
        raise PipelineError("Generated site catalog drift: docs/catalog.json")
    return {"records": len(rows), "published_catalog_entries": catalog["count"],
            "metadata_conflicts": len(audit["field_conflicts"]),
            "unmapped_html": len(audit["unmapped_site_html"])}


def run(command: str, root: Path = ROOT, write: bool = False, check: bool = False) -> dict:
    root = root.resolve()
    if command == "plan":
        return plan(root)
    if command == "ingest":
        if not write:
            state = discover(root)
            return {"discovered": state["discovered"], "registered": state["existing"],
                    "new_paths": state["new_paths"], "stale_paths": state["stale_paths"],
                    "id_collisions": state["id_collisions"], "dry_run": True}
        rows, audit = prepare(root, include_new=True)
        updated = safe_write(root, generated_outputs(root, rows, audit))
        return {"records": len(rows), "written": updated}
    if command == "normalize":
        rows, audit = prepare(root, include_new=False)
        return {"records": len(rows), "source_urls": audit["with_source_url"],
                "valid_dates": audit["with_source_date"],
                "field_conflicts": len(audit["field_conflicts"]),
                "unlinked_notes": len(audit["unlinked_notes"]),
                "dry_run": True}
    if command == "validate":
        errors = validate(root, registry_paths(root)[0])
        if errors:
            raise PipelineError("Registry invalid: " + "; ".join(errors[:8]))
        return {"valid": True, "records": len(read_records(registry_paths(root)[0]))}
    if command == "reconcile":
        rows, audit = prepare(root, include_new=False)
        updated = generated_outputs(root, rows, audit)
        if write:
            return {"records": len(rows), "written": safe_write(root, updated)}
        return {"records": len(rows), "would_change": [
            p.relative_to(root).as_posix() for p, content in updated.items()
            if not p.is_file() or p.read_text(encoding="utf-8") != content],
            "dry_run": True}
    if command == "publish":
        if not write:
            # Validate structural and content integrity before building manifest.
            rows, audit = prepare(root, include_new=False)
        else:
            verify(root, check_catalog=False)
            rows = read_records(registry_paths(root)[0])
            audit = json.loads((root / "registry" / "audit-report.json").read_text(encoding="utf-8"))
        catalog = canonical_json(build_catalog(root, rows, audit))
        destination = root / "docs" / "catalog.json"
        if check:
            if not destination.is_file() or destination.read_text(encoding="utf-8") != catalog:
                raise PipelineError("docs/catalog.json missing or out of date")
            return {"catalog_valid": True, "entries": json.loads(catalog)["count"]}
        if write:
            return {"entries": json.loads(catalog)["count"],
                    "written": safe_write(root, {destination: catalog})}
        return {"entries": json.loads(catalog)["count"], "output": "docs/catalog.json",
                "dry_run": True}
    if command == "fulltext":
        from .fulltext import run as fulltext_run
        return fulltext_run(root=root, write=write, check=check)
    if command == "review":
        from .review import run as review_run
        return review_run(root=root, write=write, check=check)
    if command == "check":
        return verify(root)
    raise PipelineError(f"Unknown pipeline stage: {command}")


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    for command in ("plan", "ingest", "normalize", "validate", "reconcile", "publish", "fulltext", "review", "check"):
        sub = subs.add_parser(command)
        if command in ("ingest", "reconcile", "publish", "fulltext", "review"):
            sub.add_argument("--write", action="store_true", help="explicitly write allowlisted generated files")
        if command in ("publish", "fulltext", "review"):
            sub.add_argument("--check", action="store_true", help="require an up-to-date generated catalog")
    args = parser.parse_args(argv)
    if getattr(args, "check", False) and getattr(args, "write", False):
        parser.error("--write and --check cannot be used together")
    try:
        data = run(args.command, root=root,
                   write=getattr(args, "write", False),
                   check=getattr(args, "check", False))
    except (PipelineError, ValueError, FileNotFoundError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(canonical_json(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
