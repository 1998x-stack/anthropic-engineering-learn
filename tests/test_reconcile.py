"""Phase 2: metadata reconciliation and non-destructive migration tests."""
import json
import tempfile
import unittest
from pathlib import Path
from ael.reconcile import enrich, clean_date, clean_url, frontmatter, render_records


class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.make("anthropic/agents/example.md",
                  "# Example article\n\n> **Published:** 2025-01-06\n\n> **Source:** "
                  "[https://www.anthropic.com/engineering/example](https://www.anthropic.com/engineering/example)\n")
        self.make("anthropic/agents/example(musk-interrogation).md", "# Example note\n")
        self.make("langchain/posts/deep-agents/original.md",
                  '---\ntitle: "Original title"\nauthor: "Original Author"\n'
                  'date: "2026-02-10"\nurl: "https://www.langchain.com/blog/original"\n---\n# Original title\n')
        self.make("langchain/curated/01-study.md",
                  "# Study note\n\n**来源:** [LangChain Blog](https://www.langchain.com/blog/original)\n")
        self.make("docs/langchain/original.html", "<html></html>")
        self.make("docs/langchain/01-study.html", "<html></html>")
        self.make("_meta/langchain/original.json", json.dumps({
            "title": "Different title", "date": "Unknown",
            "url": "https://www.langchain.com/blog/original"}))
        self.make("index.json", json.dumps({"articles": [{
            "file": "agents/example.md", "title": "Example from index",
            "date": "2025-01-06", "url": "https://www.anthropic.com/engineering/example"
        }]}))
        self.make("registry/verified-overrides.json", json.dumps({
            "source:anthropic:example": {
                "published_at": "2024-12-19",
                "canonical_url": "https://www.anthropic.com/research/example",
                "evidence_url": "https://www.anthropic.com/research/example"
            }
        }))
        self.rows = [
            self.row("source:anthropic:example", "source_article", "anthropic/agents/example.md", "anthropic"),
            self.row("note:anthropic:example:interrogation", "article_note", "anthropic/agents/example(musk-interrogation).md", "anthropic", ["source:anthropic:example"]),
            self.row("source:langchain:original", "source_article", "langchain/posts/deep-agents/original.md", "langchain"),
            self.row("note:langchain:01-study", "article_note", "langchain/curated/01-study.md", "langchain"),
        ]

    def make(self, name, content):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def row(self, id_, kind, path, source, related=None):
        row = dict(id=id_, kind=kind, source=source, path=path,
                   review_status="unreviewed", publication_status="unspecified")
        if related:
            row["related_ids"] = related
        return row

    def tearDown(self):
        self.tmp.cleanup()

    def test_metadata_precedence_and_conflicts(self):
        enriched, report = enrich(self.root, self.rows)
        byid = {r["id"]: r for r in enriched}
        a = byid["source:anthropic:example"]
        self.assertEqual(a["published_at"], "2024-12-19")
        self.assertEqual(a["canonical_url"], "https://www.anthropic.com/research/example")
        self.assertEqual(a["review_status"], "unreviewed")
        self.assertEqual(a["metadata_provenance"]["published_at"],
                         "registry/verified-overrides.json#source:anthropic:example")
        self.assertEqual(a["publication_status"], "not_published")
        self.assertGreaterEqual(len(report["field_conflicts"]), 2)
        self.assertEqual(report["legacy_metadata"]["matched"], 1)
        self.assertEqual(len(report["duplicate_source_urls"]), 0)

    def test_links_and_publication_do_not_inherit_authorship(self):
        enriched, report = enrich(self.root, self.rows)
        byid = {r["id"]: r for r in enriched}
        self.assertIn("source:langchain:original", byid["note:langchain:01-study"]["related_ids"])
        self.assertNotIn("author", byid["note:langchain:01-study"])
        self.assertEqual(byid["source:langchain:original"]["author"], "Original Author")
        self.assertEqual(byid["source:langchain:original"]["site_path"], "docs/langchain/original.html")
        self.assertEqual(byid["source:langchain:original"]["publication_status"], "published")
        self.assertEqual(byid["note:langchain:01-study"]["publication_status"], "published")
        self.assertEqual(report["note_source_url_matched"], 1)

    def test_idempotence_and_no_loss(self):
        first, report = enrich(self.root, self.rows)
        second, report2 = enrich(self.root, first)
        self.assertEqual(render_records(first), render_records(second))
        self.assertEqual(report, report2)
        self.assertEqual({r["id"] for r in first}, {r["id"] for r in self.rows})

    def test_note_citation_kept_when_original_is_missing(self):
        self.make("langchain/curated/02-external-only.md",
                  "# External note\n\n**来源:** [Blog](https://blog.langchain.dev/external-only/)\n")
        extended = self.rows + [self.row("note:langchain:02-external-only",
                                         "article_note", "langchain/curated/02-external-only.md",
                                         "langchain")]
        enriched, audit = enrich(self.root, extended)
        row = next(r for r in enriched if r["id"] == "note:langchain:02-external-only")
        self.assertEqual(row["source_reference_url"], "https://blog.langchain.dev/external-only")
        self.assertFalse(row.get("related_ids"))
        self.assertIn("note:langchain:02-external-only", audit["unlinked_notes"])
        self.assertEqual(audit["note_reference_status"]["external_only"], 1)
        self.assertTrue(any(x["id"] == row["id"] and x["status"] == "external_only"
                            for x in audit["note_reference_links"]))

    def test_preexisting_note_link_is_not_mistaken_for_external_only(self):
        self.make("anthropic/agents/example(musk-interrogation).md",
                  "# Example note\n\n> **分析对象**: "
                  "[Article](https://www.anthropic.com/engineering/example)\n")
        enriched, report = enrich(self.root, self.rows)
        note_id = "note:anthropic:example:interrogation"
        note = next(row for row in enriched if row["id"] == note_id)
        self.assertIn("source:anthropic:example", note["related_ids"])
        status = next(row["status"] for row in report["note_reference_links"]
                      if row["id"] == note_id)
        self.assertEqual(status, "linked_by_id_url_mismatch")

    def test_missing_citation_is_not_guessed_from_title(self):
        self.make("langchain/curated/03-original.md", "# Original\\n(no explicit source)\\n")
        added = self.row("note:langchain:03-original", "article_note",
                         "langchain/curated/03-original.md", "langchain")
        records, audit = enrich(self.root, self.rows + [added])
        row = next(x for x in records if x["id"] == added["id"])
        self.assertNotIn("source_reference_url", row)
        self.assertNotIn("related_ids", row)
        self.assertIn("note:langchain:03-original", audit["unlinked_notes"])


    def test_reconcile_revokes_stale_source_metadata_and_provenance(self):
        first, _ = enrich(self.root, self.rows)
        original = next(x for x in first if x["id"] == "source:langchain:original")
        self.assertEqual(original["author"], "Original Author")
        self.assertEqual(original["published_at"], "2026-02-10")
        self.assertIn("canonical_url", original)

        # Simulate removal of all authoritative metadata candidates.
        (self.root / "_meta/langchain/original.json").unlink()
        self.make("langchain/posts/deep-agents/original.md", "# Revised title\n")
        second, _ = enrich(self.root, first)
        refreshed = next(x for x in second if x["id"] == original["id"])
        self.assertEqual(refreshed["title"], "Revised title")
        for key in ("author", "published_at", "canonical_url"):
            self.assertNotIn(key, refreshed)
            self.assertNotIn(key, refreshed.get("metadata_provenance", {}))
        self.assertEqual(refreshed["review_status"], original["review_status"])

        # Reconciliation is idempotent even after a field was withdrawn.
        third, _ = enrich(self.root, second)
        self.assertEqual(render_records(second), render_records(third))

    def test_reconcile_does_not_keep_removed_note_title_or_citation(self):
        self.make("langchain/curated/01-study.md",
                  "# Evidence note\n\n**来源:** [Original](https://www.langchain.com/blog/original)\n")
        first, _ = enrich(self.root, self.rows)
        note = next(x for x in first if x["id"] == "note:langchain:01-study")
        self.assertIn("title", note)
        self.assertIn("source_reference_url", note)

        self.make("langchain/curated/01-study.md", "This note has no title or explicit citation.\n")
        second, _ = enrich(self.root, first)
        updated = next(x for x in second if x["id"] == note["id"])
        self.assertNotIn("title", updated)
        self.assertNotIn("source_reference_url", updated)
        self.assertNotIn("metadata_provenance", updated)

    def test_paper_editorial_metadata_is_not_cleared(self):
        # This isolated fixture contains no Anthropic records.
        (self.root / "registry/verified-overrides.json").write_text("{}", encoding="utf-8")
        self.make("papers/sample.pdf", "%PDF-1.4\n")
        paper = self.row("paper:sample", "paper", "papers/sample.pdf", "papers")
        paper["title"] = "Curated paper title"
        paper["author"] = "Editorial author"
        refreshed, _ = enrich(self.root, [paper])
        self.assertEqual(refreshed[0]["title"], "Curated paper title")
        self.assertEqual(refreshed[0]["author"], "Editorial author")

    def test_article_evidence_must_point_to_matching_article(self):
        from ael.reconcile import read_overrides
        path = self.root / "registry/verified-overrides.json"
        for bad in ("https://www.anthropic.com/engineering",
                    "https://www.anthropic.com/research/someone-elses-article",
                    "https://www.anthropic.com/research/example?tracking=1",
                    "https://evil.example/research/example"):
            path.write_text(json.dumps({
                "source:anthropic:example": {"published_at": "2024-12-19",
                                               "evidence_url": bad}}), encoding="utf-8")
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                read_overrides(self.root)

    def test_official_date_checks_enforce_coverage_and_observed_date(self):
        from ael.reconcile import read_overrides
        path = self.root / "registry/verified-overrides.json"
        date_log = self.root / "registry/official-date-checks.json"
        identity = "source:anthropic:example"
        original = json.loads(path.read_text(encoding="utf-8"))[identity]
        valid = {"id": identity, "evidence_url": original["evidence_url"],
                 "observed_published_at": original["published_at"],
                 "checked_at": "2026-11-12"}
        doc = {"schema_version": 1, "method": "official_publisher_page_observation",
               "checked_articles": [valid]}
        date_log.write_text(json.dumps(doc), encoding="utf-8")
        self.assertEqual(read_overrides(self.root)[identity], original)
        doc["checked_articles"][0]["observed_published_at"] = "2025-01-01"
        date_log.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaises(ValueError):
            read_overrides(self.root)
        doc["checked_articles"] = []
        date_log.write_text(json.dumps(doc), encoding="utf-8")
        with self.assertRaises(ValueError):
            read_overrides(self.root)

    def test_reject_unknown_and_invalid(self):
        self.assertIsNone(clean_date("Unknown"))
        self.assertIsNone(clean_date("2026-99-99"))
        self.assertIsNone(clean_url("https://evil.example/phishing", "anthropic"))
        self.assertEqual(clean_url("https://www.anthropic.com/research/example?x=1", "anthropic"),
                         "https://www.anthropic.com/research/example")
        self.assertEqual(frontmatter('---\ntitle: "A title"\n---\nbody')['title'], '"A title"')


if __name__ == "__main__":
    unittest.main()
