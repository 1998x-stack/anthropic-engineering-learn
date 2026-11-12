"""Phase 6 knowledge index: deterministic facets, audit and safety."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from ael.knowledge import KnowledgeError, build_index, load_projects, load_taxonomy


class KnowledgeIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write("registry/topics.json", json.dumps({"schema_version": 1, "assignment_policy": "rule:v1",
            "topics": [
                {"id": "agent-memory", "label_zh": "记忆", "label_en": "Memory", "description": "Memory",
                 "patterns": [r"\bmemory\b", "记忆"]},
                {"id": "agent-patterns", "label_zh": "Agent 架构", "label_en": "Agents", "description": "Architecture",
                 "patterns": [r"\bagent\b"]},
            ]}))
        self.write("registry/projects.json", json.dumps({"schema_version": 1, "projects": [{
            "id": "pi-memory", "title": "Pi Memory",
            "url": "https://github.com/1998x-stack/pi-memory",
            "description": "Repository link only",
            "status": "repository_link_only",
            "related_ids": ["note:langchain:memory-note"],
        }]}))
        self.write("content/research/article-notes/langchain/memory-note.md",
                   "# Memory note\n\n**来源:** [LangChain](https://www.langchain.com/blog/memory)\n\n"
                   "这篇研究笔记探讨智能体跨会话记忆的可扩展运行模式以及稳定的知识保存方法。\n")
        self.write("langchain/posts/agents/memory.md",
                   "# Agent memory\n\nAgent memory in LangChain applications can help workloads over long tasks.\n")
        self.write("docs/langchain/memory.html", "<html>Existing HTML</html>")
        self.rows = [
            {"id": "source:langchain:memory", "kind": "source_article", "source": "langchain",
             "title": "Agent memory", "path": "langchain/posts/agents/memory.md",
             "publication_status": "not_published", "review_status": "unreviewed"},
            {"id": "note:langchain:memory-note", "kind": "article_note", "source": "langchain",
             "title": "Agent Memory 笔记", "path": "content/research/article-notes/langchain/memory-note.md",
             "publication_status": "published", "site_path": "docs/langchain/memory.html",
             "review_status": "unreviewed", "related_ids": ["source:langchain:memory"],
             "source_reference_url": "https://www.langchain.com/blog/memory"},
        ]

    def tearDown(self):
        self.temp.cleanup()

    def write(self, path, content):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def test_published_backward_compatibility_and_full_registry(self):
        data = build_index(self.root, self.rows, {"note_reference_links": [
            {"id": "note:langchain:memory-note", "status": "matched"}]})
        self.assertEqual(data["count"], 1)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["statistics"]["total"], 2)
        self.assertEqual(len(data["records"]), 2)
        self.assertEqual(data["statistics"]["notes_without_local_source"], 0)
        note = next(x for x in data["records"] if x["kind"] == "article_note")
        self.assertIn("agent-memory", note["topics"])
        self.assertNotIn("agent-patterns", note["topics"])
        self.assertEqual(note["reference_status"], "matched")
        self.assertEqual(note["related_projects"], ["pi-memory"])
        self.assertIn("这篇研究笔记", note["summary"])

    def test_rejects_bad_project_target_and_unsafe_external_link(self):
        path = self.root / "registry/projects.json"
        obj = json.loads(path.read_text(encoding="utf-8"))
        obj["projects"][0]["related_ids"] = ["note:langchain:missing"]
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaises(KnowledgeError):
            build_index(self.root, self.rows)
        obj["projects"][0]["related_ids"] = ["note:langchain:memory-note"]
        obj["projects"][0]["url"] = "https://github.com/1998x-stack.evil.com/pi-memory"
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaises(KnowledgeError):
            load_projects(self.root, {x["id"] for x in self.rows})

    def test_rejects_bad_taxonomy_regex(self):
        path = self.root / "registry/topics.json"
        obj = json.loads(path.read_text(encoding="utf-8"))
        obj["topics"][0]["patterns"] = ["["]
        path.write_text(json.dumps(obj), encoding="utf-8")
        with self.assertRaises(KnowledgeError):
            load_taxonomy(self.root)

    def test_deterministic_order_and_audit_status(self):
        audit = {"note_reference_links": [{"id": "note:langchain:memory-note", "status": "matched"}]}
        first = build_index(self.root, self.rows, audit)
        second = build_index(self.root, list(reversed(self.rows)), audit)
        self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))

    def test_missing_local_source_not_guessed_from_note_title(self):
        note = dict(self.rows[1], related_ids=[])
        data = build_index(self.root, [self.rows[0], note], {"note_reference_links": [
            {"id": note["id"], "status": "external_only"}]})
        item = next(x for x in data["records"] if x["kind"] == "article_note")
        self.assertEqual(item["reference_status"], "external_only")
        self.assertFalse(item.get("related_ids"))
        self.assertEqual(data["statistics"]["notes_without_local_source"], 1)

    def test_portal_escapes_untrusted_catalog_text(self):
        code = (Path(__file__).resolve().parents[1] / "docs/explore/app.js").read_text(encoding="utf-8")
        self.assertIn("textContent", code)
        self.assertNotIn(".innerHTML", code)
        self.assertIn('fetch("../catalog.json")', code)


if __name__ == "__main__":
    unittest.main()
