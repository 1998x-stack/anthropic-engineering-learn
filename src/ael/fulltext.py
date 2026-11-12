"""Deterministic full-Markdown text shards for the static Knowledge Explorer.

All 1,119 Registry identities are represented; 5 PDF records carry metadata
only (no PDF text extraction). No network access, vector embeddings or external
dependencies. The only writable location is docs/explore/data/.
"""
from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

from .registry import ROOT, read_records, validate


class FullTextError(ValueError):
    pass


CHUNK_SIZE = 32
SHARD_NAME = re.compile(r"^[a-z][a-z0-9-]*-[0-9]{3,}\.json$")


def render(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def build_outputs(root: Path, records: list[dict]) -> tuple[dict[Path, str], dict]:
    root = root.resolve()
    outdir = root / "docs" / "explore" / "data"
    by_source: dict[str, list[dict]] = {}
    markdown, pdf = 0, 0
    by_id = set()
    for row in sorted(records, key=lambda r: r["id"]):
        ident = row["id"]
        if ident in by_id:
            raise FullTextError(f"duplicate stable ID: {ident}")
        by_id.add(ident)
        relative = Path(row["path"])
        source_path = (root / relative).resolve()
        if relative.is_absolute() or not source_path.is_relative_to(root) or not source_path.is_file():
            raise FullTextError(f"unsafe or missing content path: {row['path']}")
        suffix = source_path.suffix.lower()
        if suffix == ".md":
            content = source_path.read_text(encoding="utf-8-sig")
            markdown += 1
        elif suffix == ".pdf":
            content = ""
            pdf += 1
        else:
            raise FullTextError(f"unsupported source extension: {row['path']}")
        text = (row.get("title") or source_path.stem) + "\n" + content
        by_source.setdefault(row["source"], []).append({
            "id": ident, "text": text, "metadata_only": suffix == ".pdf",
        })
    outputs: dict[Path, str] = {}
    shards = []
    total_bytes = 0
    for source, items in sorted(by_source.items()):
        for idx, pos in enumerate(range(0, len(items), CHUNK_SIZE)):
            name = f"{source}-{idx:03d}.json"
            content = render({"schema_version": 1, "source": source, "items": items[pos:pos + CHUNK_SIZE]})
            encoded = content.encode("utf-8")
            outputs[outdir / name] = content
            shards.append({
                "file": name, "source": source, "count": len(items[pos:pos + CHUNK_SIZE]),
                "bytes": len(encoded), "sha256": hashlib.sha256(encoded).hexdigest(),
            })
            total_bytes += len(encoded)
    manifest = {
        "schema_version": 1,
        "index_kind": "full_local_markdown",
        "count": len(records),
        "markdown_body_count": markdown,
        "pdf_metadata_only_count": pdf,
        "total_bytes": total_bytes,
        "shards": shards,
        "source_counts": dict(sorted(Counter(r["source"] for r in records).items())),
    }
    outputs[outdir / "manifest.json"] = render(manifest)
    return outputs, manifest


def inspect(root: Path, outputs: dict[Path, str]) -> list[str]:
    directory = root / "docs" / "explore" / "data"
    expected = set(outputs)
    drift = [str(p.relative_to(root)) for p, body in outputs.items()
             if not p.is_file() or p.read_text(encoding="utf-8") != body]
    if directory.exists():
        for item in directory.iterdir():
            if item.is_file() and (SHARD_NAME.fullmatch(item.name) or item.name == "manifest.json"):
                if item not in expected:
                    drift.append(str(item.relative_to(root)) + " (obsolete)")
    return sorted(drift)


def write_outputs(root: Path, outputs: dict[Path, str]) -> list[str]:
    """Write *only* generated JSON inside the dedicated search directory."""
    root = root.resolve()
    directory = root / "docs" / "explore" / "data"
    if any(p.parent != directory or
           not (SHARD_NAME.fullmatch(p.name) or p.name == "manifest.json")
           for p in outputs):
        raise FullTextError("unsafe generated destination")
    directory.mkdir(parents=True, exist_ok=True)
    changed = []
    # Shards go first; manifest becomes visible only after the build succeeds.
    for target, body in sorted(outputs.items(), key=lambda x: x[0].name == "manifest.json"):
        if target.exists() and target.read_text(encoding="utf-8") == body:
            continue
        temp_name = None
        try:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=directory,
                                             prefix=".index-", suffix=".tmp", delete=False) as f:
                temp_name = f.name
                f.write(body)
                f.flush()
                os.fsync(f.fileno())
            os.replace(temp_name, target)
            changed.append(str(target.relative_to(root)))
        finally:
            if temp_name:
                Path(temp_name).unlink(missing_ok=True)
    expected = set(outputs)
    for p in sorted(directory.iterdir()):
        if p.is_file() and SHARD_NAME.fullmatch(p.name) and p not in expected:
            p.unlink()  # delete *only* stale generated search shards, never source assets
            changed.append(str(p.relative_to(root)) + " (obsolete)")
    return changed


def run(root: Path = ROOT, write: bool = False, check: bool = False) -> dict:
    if write and check:
        raise FullTextError("--write and --check are mutually exclusive")
    root = root.resolve()
    records_file = root / "registry" / "records.jsonl"
    errors = validate(root, records_file)
    if errors:
        raise FullTextError("Registry validation failed: " + "; ".join(errors[:5]))
    outputs, manifest = build_outputs(root, read_records(records_file))
    drift = inspect(root, outputs)
    if check and drift:
        raise FullTextError("Full-text index drift: " + ", ".join(drift[:12]))
    if write:
        changed = write_outputs(root, outputs)
        drift = inspect(root, outputs)
        if drift:
            raise FullTextError("Index still has drift after write: " + ", ".join(drift[:10]))
    else:
        changed = []
    return {
        "records": manifest["count"], "markdown_bodies": manifest["markdown_body_count"],
        "pdf_metadata_only": manifest["pdf_metadata_only_count"],
        "shards": len(manifest["shards"]), "bytes": manifest["total_bytes"],
        "changed": changed if write else drift, "dry_run": not write,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="explicitly write generated search shards")
    parser.add_argument("--check", action="store_true", help="fail on any generated index drift")
    args = parser.parse_args(argv)
    try:
        result = run(write=args.write, check=args.check)
    except FullTextError as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
