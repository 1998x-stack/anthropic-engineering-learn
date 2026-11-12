"""Historical HTML path aliases require explicit title evidence."""
import json
import tempfile
import unittest
from pathlib import Path

from ael.reconcile import enrich


class HistoricalSiteAliasTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.note = self.root / "anthropic/agents/example(musk-interrogation).md"
        self.note.parent.mkdir(parents=True)
        self.note.write_text("# Example note\n\nA reviewed heading.\n", encoding="utf-8")
        self.html = self.root / "docs/anthropic/agents/legacy.html"
        self.html.parent.mkdir(parents=True)
        self.html.write_text("<html><head><title>Example note</title></head></html>", encoding="utf-8")
        self.row = {"id": "note:anthropic:example:interrogation", "kind": "article_note",
                    "source": "anthropic", "path": "anthropic/agents/example(musk-interrogation).md",
                    "review_status": "unreviewed", "publication_status": "not_published"}
        (self.root / "registry").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def alias(self, path="docs/anthropic/agents/legacy.html"):
        return {"id": self.row["id"], "site_path": path,
                "html_title": "Example note",
                "rationale": "The original HTML title exactly matches the migrated note heading."}

    def write_aliases(self, entries):
        (self.root / "registry/site-aliases.json").write_text(
            json.dumps({"schema_version": 1, "aliases": entries}), encoding="utf-8")

    def test_verified_legacy_html_is_indexed(self):
        self.write_aliases([self.alias()])
        rows, audit = enrich(self.root, [self.row])
        self.assertEqual(rows[0]["publication_status"], "published")
        self.assertEqual(rows[0]["site_path"], "docs/anthropic/agents/legacy.html")
        self.assertEqual(audit["unmapped_site_html"], [])

    def test_title_mismatch_and_path_traversal_are_rejected(self):
        self.write_aliases([self.alias()])
        self.html.write_text("<html><title>Different article</title></html>", encoding="utf-8")
        with self.assertRaises(ValueError):
            enrich(self.root, [self.row])
        self.html.write_text("<html><title>Example note</title></html>", encoding="utf-8")
        self.write_aliases([self.alias("docs/anthropic/../legacy.html")])
        with self.assertRaises(ValueError):
            enrich(self.root, [self.row])


if __name__ == "__main__":
    unittest.main()
