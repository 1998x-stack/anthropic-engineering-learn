"""Phase 7: static full-text shard reproducibility and no-source-write tests."""
import json
import tempfile
import unittest
from pathlib import Path

from ael.fulltext import FullTextError, build_outputs, run, CHUNK_SIZE


class FullTextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.original = "# Deep agent article\n\nHere is the opening.\n\n" + (
            "This section describes baseline models and tool calls.\n" * 9
        ) + "终章：跨会话记忆压缩机制的独特术语。\n"
        self.write("anthropic/agents/example.md", self.original)
        self.records = [{
            "id": "source:anthropic:example", "kind": "source_article", "source": "anthropic",
            "path": "anthropic/agents/example.md", "review_status": "unreviewed",
            "publication_status": "not_published",
        }]
        self.write("registry/records.jsonl", json.dumps(self.records[0], ensure_ascii=False) + "\n")
        self.write("registry/migrations.json", '{"schema_version":1,"moves": []}')

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def test_entire_body_is_preserved_and_index_is_reproducible(self):
        output, manifest = build_outputs(self.root, self.records)
        self.assertEqual(manifest["count"], 1)
        self.assertEqual(manifest["markdown_body_count"], 1)
        self.assertEqual(manifest["pdf_metadata_only_count"], 0)
        shard_path = self.root / "docs/explore/data/anthropic-000.json"
        record = json.loads(output[shard_path])["items"][0]
        self.assertIn("终章：跨会话记忆压缩机制的独特术语。", record["text"])
        self.assertIn("Here is the opening", record["text"])
        result = run(root=self.root, write=True)
        self.assertEqual(result["records"], 1)
        self.assertEqual(run(root=self.root, check=True)["changed"], [])
        self.assertEqual((self.root / "anthropic/agents/example.md").read_text(), self.original)
        self.assertFalse(run(root=self.root, write=True)["changed"])

    def test_detects_drift_without_modifying_source(self):
        run(root=self.root, write=True)
        self.write("docs/explore/data/anthropic-000.json", '{"tampered":true}')
        with self.assertRaises(FullTextError):
            run(root=self.root, check=True)
        self.assertEqual((self.root / "anthropic/agents/example.md").read_text(), self.original)
        run(root=self.root, write=True)
        self.assertEqual(run(root=self.root, check=True)["changed"], [])

    def test_shards_are_small_deterministic_groups(self):
        records = []
        for i in range(CHUNK_SIZE * 2 + 1):
            path = f"anthropic/agents/topic-{i:03d}.md"
            self.write(path, f"# Topic {i}\n\nunique phrase {i}\n")
            records.append(dict(id=f"source:anthropic:topic-{i:03d}",
                                source="anthropic", kind="source_article", path=path))
        result, manifest = build_outputs(self.root, records)
        self.assertEqual([x["count"] for x in manifest["shards"]], [32, 32, 1])
        self.assertEqual(len(result), 4)
        self.assertEqual(manifest["count"], CHUNK_SIZE * 2 + 1)

    def test_pdf_is_metadata_only_and_path_traversal_is_rejected(self):
        path = self.root / "papers/sample.pdf"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"%PDF-1.4 demo")
        pdf = {"id": "paper:sample", "kind": "paper", "source": "papers",
               "path": "papers/sample.pdf", "title": "Research paper"}
        outputs, manifest = build_outputs(self.root, [pdf])
        item = json.loads(outputs[self.root / "docs/explore/data/papers-000.json"])["items"][0]
        self.assertEqual(item["text"], "Research paper\n")
        self.assertTrue(item["metadata_only"])
        self.assertEqual(manifest["pdf_metadata_only_count"], 1)
        with self.assertRaises(FullTextError):
            build_outputs(self.root, [dict(pdf, path="../../etc/passwd")])


if __name__ == "__main__":
    unittest.main()
