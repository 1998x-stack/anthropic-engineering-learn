"""Phase 3 pipeline: dry run, provenance safety, no-loss and catalog tests."""
import json
import tempfile
import unittest
from pathlib import Path

from ael.pipeline import PipelineError, build_catalog, main, plan, run
from ael.reconcile import render_records
from ael.registry import read_records


class SafePipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.make("anthropic/agents/test.md",
                  "# Test article\n\n> **Published:** 2024-12-19\n\n"
                  "> **Source:** [link](https://www.anthropic.com/research/test)\n")
        self.make("docs/anthropic/agents/test.html", "<html>Original static site</html>")
        self.make("registry/verified-overrides.json", "{}\n")
        self.make("index.json", '{"articles":[]}\n')
        self.registry = self.root / "registry/records.jsonl"
        self.registry.write_text(render_records([{
            "id": "source:anthropic:test", "kind": "source_article",
            "source": "anthropic", "path": "anthropic/agents/test.md",
            "review_status": "unreviewed", "publication_status": "unspecified",
        }]), encoding="utf-8")
        self.source_before = (self.root / "anthropic/agents/test.md").read_bytes()
        self.site_before = (self.root / "docs/anthropic/agents/test.html").read_bytes()

    def make(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_ingest_preview_has_no_side_effects(self):
        self.make("anthropic/agents/new.md", "# A new article\n")
        before = self.registry.read_bytes()
        result = run("ingest", root=self.root)
        self.assertEqual(result["new_paths"], ["anthropic/agents/new.md"])
        self.assertEqual(self.registry.read_bytes(), before)
        self.assertFalse((self.root / "registry/audit-report.json").exists())

    def test_explicit_ingest_write_preserves_old_ids(self):
        self.make("anthropic/agents/new.md", "# New content\n")
        result = run("ingest", root=self.root, write=True)
        self.assertEqual(result["records"], 2)
        rows = read_records(self.registry)
        self.assertEqual({r["id"] for r in rows},
                         {"source:anthropic:test", "source:anthropic:new"})
        self.assertEqual(run("check", root=self.root)["records"], 2)
        self.assertEqual((self.root / "anthropic/agents/test.md").read_bytes(), self.source_before)

    def test_reconcile_dry_run_requires_explicit_write(self):
        before = self.registry.read_bytes()
        dry = run("reconcile", root=self.root)
        self.assertIn("registry/records.jsonl", dry["would_change"])
        self.assertEqual(self.registry.read_bytes(), before)
        actual = run("reconcile", root=self.root, write=True)
        self.assertIn("registry/audit-report.json", actual["written"])
        self.assertEqual(run("check", root=self.root)["published_catalog_entries"], 1)

    def test_missing_source_stops_apply_and_does_not_delete(self):
        (self.root / "anthropic/agents/test.md").unlink()
        before = self.registry.read_bytes()
        with self.assertRaises(PipelineError):
            run("reconcile", root=self.root, write=True)
        with self.assertRaises(PipelineError):
            run("ingest", root=self.root, write=True)
        self.assertEqual(self.registry.read_bytes(), before)

    def test_catalog_is_explicit_generated_output_only(self):
        run("reconcile", root=self.root, write=True)
        dry = run("publish", root=self.root)
        self.assertEqual(dry["entries"], 1)
        self.assertFalse((self.root / "docs/catalog.json").exists())
        written = run("publish", root=self.root, write=True)
        self.assertEqual(written["entries"], 1)
        payload = json.loads((self.root / "docs/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["items"][0]["site_path"], "docs/anthropic/agents/test.html")
        self.assertEqual(run("publish", root=self.root, check=True)["entries"], 1)
        self.assertEqual((self.root / "docs/anthropic/agents/test.html").read_bytes(), self.site_before)
        self.assertEqual((self.root / "anthropic/agents/test.md").read_bytes(), self.source_before)

    def test_detects_content_drift(self):
        run("reconcile", root=self.root, write=True)
        self.make("anthropic/agents/test.md", "# Changed article\n")
        with self.assertRaises(PipelineError):
            run("check", root=self.root)
        with self.assertRaises(PipelineError):
            run("publish", root=self.root, write=True)

    def test_rejects_unsafe_html_location_and_duplicates(self):
        row = read_records(self.registry)[0]
        row["publication_status"] = "published"
        row["site_path"] = "docs/../private.html"
        with self.assertRaises(PipelineError):
            build_catalog(self.root, [row])
        row["site_path"] = "docs/anthropic/agents/test.html"
        with self.assertRaises(PipelineError):
            build_catalog(self.root, [row, dict(row)])

    def test_idempotence_and_plan_read_only(self):
        run("reconcile", root=self.root, write=True)
        state = self.registry.read_bytes()
        self.assertEqual(run("reconcile", root=self.root, write=True)["written"], [])
        dry = plan(self.root)
        self.assertEqual(dry["new_content"], 0)
        self.assertEqual(dry["metadata_changed_files"], [])
        self.assertEqual(self.registry.read_bytes(), state)
        self.assertEqual(run("validate", root=self.root)["valid"], True)

    def test_cli_help_and_read_only(self):
        self.assertEqual(main(["plan"], root=self.root), 0)


if __name__ == "__main__":
    unittest.main()
