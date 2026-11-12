"""Reviewed, link-preserving Source/Research migrations.

The manifest records deliberate changes in a stable ID's primary path.
Compatibility Markdown stubs preserve legacy GitHub links. No automatic moves
or deletes: this module plans/checks *reviewed* migrations, never writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]


def read_moves(root: Path = ROOT) -> list[dict]:
    path = root / "registry" / "migrations.json"
    if not path.exists():
        return []
    doc = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict) or doc.get("schema_version") != 1 or not isinstance(doc.get("moves"), list):
        raise ValueError("registry/migrations.json: expected {schema_version: 1, moves: []}")
    return doc["moves"]


def safe_relative(raw: str) -> bool:
    if not isinstance(raw, str) or not raw or "\\" in raw:
        return False
    parts = PurePosixPath(raw).parts
    return bool(parts) and not PurePosixPath(raw).is_absolute() and ".." not in parts and "." not in parts and raw == PurePosixPath(raw).as_posix()


def compatibility_stub(move: dict) -> str:
    """An intentionally visible Markdown link; GitHub cannot HTTP-redirect a file."""
    old = PurePosixPath(move["from"])
    new = PurePosixPath(move["to"])
    relative = os.path.relpath(str(new), str(old.parent)).replace("\\", "/")
    relative = quote(relative, safe="/._-")
    return (
        "# 研究笔记已迁移 / Research note moved\n\n"
        "原始研究笔记已移动至新的 Research 目录。本文内容未删除。\n\n"
        f"**[查看完整研究笔记 / Read the full note]({relative})**\n\n"
        f"<!-- ael:compatibility-link id={move['id']} -->\n"
    )


def validate_moves(root: Path, rows: list[dict]) -> list[str]:
    """Validate stable IDs, byte integrity and old-path compatibility links."""
    errors: list[str] = []
    try:
        moves = read_moves(root)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        return [str(exc)]
    by_id = {r.get("id"): r for r in rows}
    seen_ids, seen_sources, seen_targets = set(), set(), set()

    for i, move in enumerate(moves, 1):
        label = f"migration {i}"
        if not isinstance(move, dict) or set(move) != {"id", "from", "to", "sha256"}:
            errors.append(f"{label}: expected id/from/to/sha256 only")
            continue
        ident, old, new, digest = (move[field] for field in ("id", "from", "to", "sha256"))
        if not isinstance(ident, str) or not ident.startswith("note:"):
            errors.append(f"{label}: only note IDs can move in this phase")
            continue
        if not safe_relative(old) or not safe_relative(new):
            errors.append(f"{label}: unsafe or noncanonical path")
            continue
        if not old.endswith(".md") or not new.endswith(".md") or not new.startswith("content/research/article-notes/"):
            errors.append(f"{label}: unsupported migration path")
            continue
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            errors.append(f"{label}: expected SHA-256 lowercase hex digest")
            continue
        if ident in seen_ids or old in seen_sources or new in seen_targets:
            errors.append(f"{label}: duplicate migrated identity or file path")
        seen_ids.add(ident)
        seen_sources.add(old)
        seen_targets.add(new)
        row = by_id.get(ident)
        if row is None or row.get("path") != new or row.get("kind") != "article_note":
            errors.append(f"{label}: registry must point stable note ID {ident} to {new}")
        if row and row.get("source_sha256") != digest:
            errors.append(f"{label}: registry content hash changed from original")
        target = root / new
        if not target.is_file():
            errors.append(f"{label}: migrated note missing: {new}")
        elif hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            errors.append(f"{label}: original Markdown bytes were not preserved: {new}")
        old_path = root / old
        if not old_path.is_file():
            errors.append(f"{label}: old GitHub link no longer resolves: {old}")
        elif old_path.read_text(encoding="utf-8") != compatibility_stub(move):
            errors.append(f"{label}: compatibility link does not point to original content: {old}")
        rel = os.path.relpath(new, str(PurePosixPath(old).parent))
        if (old_path.parent / rel).resolve() != target.resolve():
            errors.append(f"{label}: compatibility target escapes its destination")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("plan", "check"))
    args = parser.parse_args()
    from .registry import read_records
    rows = read_records(ROOT / "registry" / "records.jsonl")
    moves = read_moves(ROOT)
    errors = validate_moves(ROOT, rows)
    result = {
        "migrations": len(moves),
        "moved_ids": [m.get("id") for m in moves],
        "legacy_links_kept": sum((ROOT / m.get("from", "")).is_file() for m in moves),
        "errors": errors,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if args.command == "check" and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
