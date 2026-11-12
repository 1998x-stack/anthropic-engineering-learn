import tempfile
import unittest
from pathlib import Path
from ael.registry import classify, read_records, sync, validate


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.registry = self.root / "registry" / "records.jsonl"
        for relative in (
            "anthropic/agents/building-effective-agents.md",
            "anthropic/agents/building-effective-agents(musk-interrogation).md",
            "langchain/curated/01-the-anatomy-of-an-agent-harness.md",
            "papers/Meta-Harness.pdf",
        ):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"fixture")

    def tearDown(self):
        self.temp.cleanup()

    def test_classifies_source_note_and_paper(self):
        self.assertEqual(classify("anthropic/agents/building-effective-agents.md")["kind"], "source_article")
        self.assertEqual(classify("papers/Meta-Harness.pdf")["id"], "paper:meta-harness")
        self.assertEqual(classify("langchain/curated/README.md"), None)

    def test_sync_is_idempotent_and_preserves_existing_records(self):
        self.assertEqual(sync(self.root, self.registry, write=True), (4, 4))
        self.assertEqual(sync(self.root, self.registry, write=True), (0, 4))
        rows = read_records(self.registry)
        self.assertEqual(len(rows), 4)
        self.assertEqual(validate(self.root, self.registry), [])
        note = next(r for r in rows if r["id"].endswith(":interrogation"))
        self.assertEqual(note["related_ids"], ["source:anthropic:building-effective-agents"])

    def test_validation_detects_missing_content(self):
        sync(self.root, self.registry, write=True)
        (self.root / "papers/Meta-Harness.pdf").unlink()
        self.assertTrue(any("file missing" in e for e in validate(self.root, self.registry)))


if __name__ == "__main__":
    unittest.main()
