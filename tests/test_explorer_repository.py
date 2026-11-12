"""Repository regression gate for the Phase 6 search portal."""
import json
import unittest

from ael.pipeline import build_catalog
from ael.registry import ROOT, read_records


class ExplorerRepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = read_records(ROOT / "registry/records.jsonl")
        cls.catalog = build_catalog(ROOT, cls.rows)
        cls.audit = json.loads((ROOT / "registry/audit-report.json").read_text(encoding="utf-8"))

    def test_search_covers_all_registered_ids(self):
        items = self.catalog["records"]
        self.assertEqual(len(items), len(self.rows))
        self.assertEqual({x["id"] for x in items}, {x["id"] for x in self.rows})
        self.assertGreaterEqual(len(items), 1119)
        self.assertEqual(self.catalog["statistics"]["total"], len(items))

    def test_published_html_and_legacy_items_stay_compatible(self):
        published = [x for x in self.catalog["records"] if x["publication_status"] == "published"]
        self.assertEqual(len(published), self.catalog["count"])
        self.assertEqual(len(self.catalog["items"]), self.catalog["count"])
        self.assertGreaterEqual(self.catalog["count"], 523)
        for item in published:
            self.assertTrue((ROOT / item["site_path"]).is_file())

    def test_topics_and_source_links_are_traceable(self):
        topics = {t["id"] for t in self.catalog["topics"]}
        self.assertGreaterEqual(len(topics), 10)
        self.assertGreater(sum(bool(r["topics"]) for r in self.catalog["records"]), 100)
        self.assertTrue(all(set(r["topics"]) <= topics for r in self.catalog["records"]))
        notes = [r for r in self.catalog["records"] if r["kind"] == "article_note"]
        self.assertEqual(len(notes), 123)
        self.assertEqual(sum(not any(x.startswith(("source:", "paper:"))
                             for x in r.get("related_ids", [])) for r in notes),
                         len(self.audit["unlinked_notes"]))
        self.assertEqual({r["id"] for r in notes},
                         {x["id"] for x in self.audit["note_reference_links"]})

    def test_explicit_experiment_projects_are_links_only(self):
        self.assertEqual(len(self.catalog["projects"]), 3)
        ids = {r["id"] for r in self.catalog["records"]}
        for project in self.catalog["projects"]:
            self.assertEqual(project["status"], "repository_link_only")
            self.assertTrue(set(project["related_ids"]) <= ids)
        self.assertTrue(any(r.get("related_projects") for r in self.catalog["records"]))

    def test_site_portal_assets_and_home_entry_exist(self):
        html = (ROOT / "docs/explore/index.html").read_text(encoding="utf-8")
        js = (ROOT / "docs/explore/app.js").read_text(encoding="utf-8")
        css = (ROOT / "docs/explore/style.css").read_text(encoding="utf-8")
        index = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn('src="app.js"', html)
        self.assertIn('href="style.css"', html)
        self.assertIn('fetch("../catalog.json")', js)
        self.assertNotIn(".innerHTML", js)
        self.assertTrue(css)
        self.assertIn('href="explore/"', index)


if __name__ == "__main__":
    unittest.main()
