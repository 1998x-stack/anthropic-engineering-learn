"""Repository-level regression tests for the complete Research migration."""
from __future__ import annotations

import json
import unittest

from ael.migration import read_moves, validate_moves
from ael.pipeline import build_catalog
from ael.registry import ROOT, inventory, read_records


class RepositoryResearchIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = read_records(ROOT / "registry" / "records.jsonl")
        cls.moves = read_moves(ROOT)
        cls.notes = [r for r in cls.rows if r["kind"] == "article_note"]
        cls.by_id = {r["id"]: r for r in cls.rows}

    def test_all_research_notes_have_canonical_paths(self):
        self.assertGreaterEqual(len(self.notes), 123)
        self.assertTrue(all(r["path"].startswith("content/research/article-notes/")
                            for r in self.notes))
        inventory_notes = [r for r in inventory(ROOT) if r["kind"] == "article_note"]
        self.assertEqual({r["id"] for r in inventory_notes}, {r["id"] for r in self.notes})
        self.assertEqual(len(inventory_notes), len(self.notes))

    def test_original_migrations_preserve_links_and_hashes(self):
        self.assertGreaterEqual(len(self.moves), 123)
        self.assertEqual(validate_moves(ROOT, self.rows), [])
        self.assertEqual(len({m["id"] for m in self.moves}), len(self.moves))
        for move in self.moves:
            self.assertEqual(self.by_id[move["id"]]["path"], move["to"])
            self.assertEqual(self.by_id[move["id"]]["source_sha256"], move["sha256"])

    def test_audit_partitions_every_research_citation(self):
        audit = json.loads((ROOT / "registry" / "audit-report.json").read_text(encoding="utf-8"))
        refs = audit["note_reference_links"]
        self.assertEqual({r["id"] for r in refs}, {r["id"] for r in self.notes})
        self.assertEqual(len(refs), len(self.notes))
        self.assertEqual(sum(audit["note_reference_status"].values()), len(self.notes))
        self.assertEqual(set(audit["unlinked_notes"]),
                         {r["id"] for r in self.notes if not r.get("related_ids")})

    def test_site_manifest_exposes_old_and_new_paths(self):
        catalog = build_catalog(ROOT, self.rows)
        by_id = {r["id"]: r for r in catalog["items"]}
        for move in self.moves:
            row = self.by_id[move["id"]]
            if row.get("publication_status") != "published":
                continue
            item = by_id[move["id"]]
            self.assertEqual(item["content_path"], move["to"])
            self.assertEqual(item["legacy_markdown_path"], move["from"])
            self.assertTrue((ROOT / item["site_path"]).is_file())


if __name__ == "__main__":
    unittest.main()
