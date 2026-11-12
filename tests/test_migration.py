"""Phase 4: research-note migration and compatibility/link regression tests."""
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from ael.migration import compatibility_stub, read_moves, validate_moves
from ael.registry import classify, inventory, read_records, validate
from ael.reconcile import enrich


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.old = "langchain/curated/01-test-harness.md"
        self.new = "content/research/article-notes/langchain/01-test-harness.md"
        body = "# A test research note\n\n**来源:** [LangChain Blog](https://www.langchain.com/blog/original)\n"
        self.write(self.new, body)
        digest = hashlib.sha256(body.encode()).hexdigest()
        self.move = {"id": "note:langchain:01-test-harness",
                     "from": self.old, "to": self.new, "sha256": digest}
        self.write(self.old, compatibility_stub(self.move))
        self.write("registry/migrations.json", json.dumps({"schema_version": 1, "moves": [self.move]}))
        self.write("langchain/posts/deep-agents/original.md", '---\ntitle: "Original"\nauthor: "A"\n'
                   'date: "2026-03-10"\nurl: "https://www.langchain.com/blog/original"\n---\n# Original\n')
        self.write("docs/langchain/01-test-harness.html", "<html><body>Existing page</body></html>")
        self.rows = [
            {"id": self.move["id"], "kind": "article_note", "source": "langchain",
             "path": self.new, "source_sha256": digest,
             "publication_status": "published", "review_status": "unreviewed"},
            {"id": "source:langchain:original", "kind": "source_article",
             "source": "langchain", "path": "langchain/posts/deep-agents/original.md",
             "publication_status": "not_published", "review_status": "unreviewed"},
        ]
        self.write("registry/records.jsonl", "".join(json.dumps(x) + "\n" for x in self.rows))

    def write(self, path, content):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_manifest_keeps_old_github_url_and_original_bytes(self):
        self.assertEqual(read_moves(self.root), [self.move])
        self.assertEqual(validate_moves(self.root, self.rows), [])
        self.assertEqual((self.root / self.old).read_text(), compatibility_stub(self.move))
        self.assertEqual(hashlib.sha256((self.root / self.new).read_bytes()).hexdigest(), self.move["sha256"])

    def test_migrated_content_registered_once_with_stable_id(self):
        found = inventory(self.root)
        ids = [x["id"] for x in found]
        self.assertEqual(len(ids), 2)
        self.assertIn(self.move["id"], ids)
        self.assertEqual(next(x for x in found if x["id"] == self.move["id"])["path"], self.new)
        self.assertEqual(classify(self.new)["id"], self.move["id"])
        self.assertEqual(validate(self.root, self.root / "registry/records.jsonl"), [])

    def test_reconcile_keeps_research_and_static_published_page(self):
        records, audit = enrich(self.root, self.rows)
        moved = next(x for x in records if x["id"] == self.move["id"])
        self.assertEqual(moved["site_path"], "docs/langchain/01-test-harness.html")
        self.assertEqual(moved["publication_status"], "published")
        self.assertIn("source:langchain:original", moved["related_ids"])
        self.assertEqual(moved["source_sha256"], self.move["sha256"])

    def test_breaking_compatibility_link_fails_validation(self):
        self.write(self.old, "# Oops: no redirect\n")
        errors = validate(self.root, self.root / "registry/records.jsonl")
        self.assertTrue(any("compatibility link" in e for e in errors))

    def test_modifying_original_content_is_blocked(self):
        self.write(self.new, "# Accidentally edited\n")
        self.assertTrue(any("bytes were not preserved" in s for s in validate_moves(self.root, self.rows)))

    def test_manifest_rejects_path_traversal_and_duplicate_mapping(self):
        bad = dict(self.move, to="content/research/article-notes/../../escape.md")
        self.write("registry/migrations.json", json.dumps({"schema_version": 1, "moves": [bad]}))
        self.assertTrue(any("unsafe" in e for e in validate_moves(self.root, self.rows)))
        self.write("registry/migrations.json", json.dumps({"schema_version": 1, "moves": [self.move, self.move]}))
        self.assertTrue(any("duplicate" in e for e in validate_moves(self.root, self.rows)))

    def test_migration_remains_compatible_with_original_doc_links(self):
        link = (self.root / self.old).read_text(encoding="utf-8")
        self.assertIn("查看完整研究笔记", link)
        self.assertIn("../../content/research/article-notes/", link)

    def test_missing_migrated_file_is_detected(self):
        (self.root / self.new).unlink()
        self.assertTrue(any("migrated note missing" in e for e in validate_moves(self.root, self.rows)))


if __name__ == "__main__":
    unittest.main()
