"""A deterministic knowledge index for the static search portal.

No external crawling, embeddings, inferred identity joins or original text edits.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


class KnowledgeError(ValueError):
    pass


def load_taxonomy(root: Path) -> dict:
    path = root / "registry" / "topics.json"
    if not path.is_file():
        return {"schema_version": 1, "topics": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("topics"), list):
        raise KnowledgeError("Invalid registry/topics.json")
    seen = set()
    for topic in data["topics"]:
        if not isinstance(topic, dict) or not re.fullmatch(r"[a-z][a-z0-9-]*", str(topic.get("id", ""))):
            raise KnowledgeError("Topic must have a stable slug ID")
        if topic["id"] in seen or not topic.get("label_zh") or not topic.get("label_en"):
            raise KnowledgeError("Duplicate topic ID or missing bilingual label")
        seen.add(topic["id"])
        if not isinstance(topic.get("patterns"), list) or not topic["patterns"]:
            raise KnowledgeError(f"{topic['id']}: patterns must be nonempty")
        for p in topic["patterns"]:
            if not isinstance(p, str):
                raise KnowledgeError(f"{topic['id']}: invalid regex pattern")
            try:
                re.compile(p, flags=re.IGNORECASE)
            except re.error as exc:
                raise KnowledgeError(f"{topic['id']}: bad regex {exc}") from exc
    return data


def load_projects(root: Path, ids: set[str]) -> list[dict]:
    path = root / "registry" / "projects.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("projects"), list):
        raise KnowledgeError("Invalid registry/projects.json")
    projects, seen = [], set()
    for p in data["projects"]:
        if not isinstance(p, dict):
            raise KnowledgeError("Project must be an object")
        ident = p.get("id")
        if not isinstance(ident, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", ident) or ident in seen:
            raise KnowledgeError("Invalid or duplicate project ID")
        seen.add(ident)
        url = p.get("url")
        parts = urlsplit(url) if isinstance(url, str) else None
        if (not parts or parts.scheme != "https" or parts.netloc != "github.com" or
                not re.fullmatch(r"/1998x-stack/[A-Za-z0-9._-]+/?", parts.path) or
                parts.query or parts.fragment or parts.username or parts.password):
            raise KnowledgeError(f"{ident}: URL must be the approved GitHub repository")
        links = p.get("related_ids")
        if (not isinstance(links, list) or not links or
                any(not isinstance(x, str) or x not in ids for x in links) or len(set(links)) != len(links)):
            raise KnowledgeError(f"{ident}: dangling/duplicate IDs")
        if p.get("status") != "repository_link_only":
            raise KnowledgeError(f"{ident}: experiment results were not verified")
        if not isinstance(p.get("title"), str) or not p["title"]:
            raise KnowledgeError(f"{ident}: missing project title")
        projects.append({key: p[key] for key in ("id", "title", "url", "description", "status", "related_ids")})
    return sorted(projects, key=lambda item: item["id"])


def assign_topics(row: dict, taxonomy: dict) -> list[str]:
    """Keyword suggestions based solely on title, stable ID and current path."""
    haystack = " ".join((str(row.get("title", "")), str(row.get("id", "")).replace(":", " "),
                         str(row.get("path", "")).replace("/", " ")))
    found = [t["id"] for t in taxonomy["topics"]
             if any(re.search(p, haystack, re.IGNORECASE) for p in t["patterns"])]
    if len(found) > 1 and "agent-patterns" in found:
        found.remove("agent-patterns")
    return found[:4]


def short_summary(root: Path, row: dict, limit: int = 210) -> str:
    """Short local Markdown preview. Nothing is downloaded or executed."""
    path = root / row["path"]
    if path.suffix.lower() != ".md":
        return ""
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("---\n"):
        end = raw.find("\n---", 4)
        if end >= 0:
            raw = raw[end + 4:]
    in_code = False
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith((chr(96) * 3, "~~~")):
            in_code = not in_code
            continue
        if in_code or not line or line.startswith(("#", "|", "<", "![", "---", "- ", "* ")):
            continue
        if re.match(r"^(?:>\s*)?(?:\*\*)?(?:Source|Published|Author|Title|来源|作者|日期|原文|分析对象)\s*[:：]", line, re.I):
            continue
        line = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"[\x60*_>]", "", line).strip()
        if len(line) >= 36:
            return line[:limit].rstrip()
    return ""


def audited_status_map(root: Path, rows: list[dict], audit: dict | None = None) -> dict[str, str]:
    note_ids = {r["id"] for r in rows if r.get("kind") == "article_note"}
    if audit is None:
        path = root / "registry" / "audit-report.json"
        if path.exists():
            audit = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(audit, dict) and isinstance(audit.get("note_reference_links"), list):
        links = audit["note_reference_links"]
        statuses = {r.get("id"): r.get("status") for r in links if isinstance(r, dict)}
        if set(statuses) == note_ids and len(links) == len(note_ids):
            return statuses
    def fallback(r: dict) -> str:
        linked = any(x.startswith(("source:", "paper:")) for x in r.get("related_ids", []))
        if linked:
            return "linked_by_id_url_mismatch" if r.get("source_reference_url") else "matched"
        return "external_only" if r.get("source_reference_url") else "no_explicit_citation"
    return {r["id"]: fallback(r) for r in rows if r.get("kind") == "article_note"}


def build_index(root: Path, rows: list[dict], audit: dict | None = None) -> dict:
    from .migration import read_moves

    taxonomy = load_taxonomy(root)
    id_index = {r["id"]: r for r in rows}
    if len(id_index) != len(rows):
        raise KnowledgeError("Duplicate Registry IDs")
    projects = load_projects(root, set(id_index))
    old_paths = {m["id"]: m["from"] for m in read_moves(root)}
    project_by_id = {ident: [] for ident in id_index}
    for project in projects:
        for ident in project["related_ids"]:
            project_by_id[ident].append(project["id"])
    statuses = audited_status_map(root, rows, audit)
    records, topic_counts = [], Counter()
    for row in sorted(rows, key=lambda x: x["id"]):
        topics = assign_topics(row, taxonomy)
        topic_counts.update(topics)
        item = {
            "id": row["id"], "kind": row["kind"], "source": row["source"],
            "title": row.get("title") or Path(row["path"]).stem,
            "content_path": row["path"], "review_status": row["review_status"],
            "publication_status": row["publication_status"],
            "topics": topics, "topic_basis": taxonomy.get("assignment_policy", "keyword_rules_v1"),
        }
        summary = short_summary(root, row)
        if summary:
            item["summary"] = summary
        for field in ("site_path", "published_at", "author", "canonical_url",
                      "source_reference_url", "related_ids"):
            if row.get(field):
                item[field] = row[field]
        if row["id"] in old_paths:
            item["legacy_markdown_path"] = old_paths[row["id"]]
        if project_by_id[row["id"]]:
            item["related_projects"] = sorted(project_by_id[row["id"]])
        if row["kind"] == "article_note":
            item["reference_status"] = statuses[row["id"]]
        records.append(item)
    published = [r for r in records if r["publication_status"] == "published"]
    return {
        "schema_version": 2,
        "count": len(published), "items": published,
        "records": records,
        "topics": [{key: t[key] for key in ("id", "label_zh", "label_en", "description")}
                   for t in taxonomy["topics"]],
        "projects": projects,
        "statistics": {
            "total": len(records), "published_html": len(published),
            "source_articles": sum(r["kind"] == "source_article" for r in records),
            "research_notes": sum(r["kind"] == "article_note" for r in records),
            "papers": sum(r["kind"] == "paper" for r in records),
            "notes_without_local_source": sum(
                r["kind"] == "article_note" and not any(x.startswith(("source:", "paper:"))
                for x in r.get("related_ids", [])) for r in records),
            "untagged": sum(not r["topics"] for r in records),
            "topic_counts": dict(sorted(topic_counts.items())),
        },
    }
