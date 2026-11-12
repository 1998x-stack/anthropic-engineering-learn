"""Phase 7 evidence queue and SHA-bound editorial decisions."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from ael.review import ReviewError, approved_topic_decisions, build_queue


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.note = self.root / "notes/note.md"
        self.note.parent.mkdir(parents=True)
        self.note.write_text("# Agent Memory\n\nFull evidence text.\n", encoding="utf-8")
        self.sha = hashlib.sha256(self.note.read_bytes()).hexdigest()
        self.rows = [
            {"id": "note:langchain:note", "kind": "article_note", "source": "langchain",
             "title": "Agent Memory", "path": "notes/note.md", "source_sha256": self.sha,
             "publication_status": "not_published", "review_status": "unreviewed"},
        ]

    def tearDown(self):
        self.tmp.cleanup()

    def test_queue_tracks_missing_source_and_does_not_guess(self):
        audit = {
            "unlinked_notes": ["note:langchain:note"],
            "note_reference_links": [{"id": "note:langchain:note",
                                      "status": "no_explicit_citation"}],
        }
        result = build_queue(self.rows, audit)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["unlinked"], 1)
        item = result["items"][0]
        self.assertEqual(item["source_sha256"], self.sha)
        self.assertNotIn("related_ids", item)
        self.assertNotIn("explicit_reference_url", item)

    def test_review_decision_is_sha_bound_to_actual_document(self):
        path = self.root / "registry/review-decisions.json"
        path.parent.mkdir()
        entry = {"id": self.rows[0]["id"], "topics": ["agent-memory"],
                 "evidence_sha256": self.sha, "reviewer": "maintainer@example.org",
                 "reviewed_at": "2026-11-12",
                 "rationale": "The research note explicitly discusses persistent memory."}
        path.write_text(json.dumps({"schema_version": 1,
                                     "topic_decisions": [entry]}), encoding="utf-8")
        decisions = approved_topic_decisions(self.root, self.rows, {"agent-memory"})
        self.assertEqual(decisions[entry["id"]]["topics"], ["agent-memory"])
        self.note.write_text("# New content", encoding="utf-8")
        with self.assertRaises(ReviewError):
            approved_topic_decisions(self.root,
                [dict(self.rows[0], source_sha256=hashlib.sha256(self.note.read_bytes()).hexdigest())],
                {"agent-memory"})

    def test_invalid_reviewer_topic_and_missing_evidence_rejected(self):
        path = self.root / "registry/review-decisions.json"
        path.parent.mkdir()
        e = {"id": "note:langchain:note", "topics": ["unknown-topic"],
             "evidence_sha256": self.sha, "reviewer": "x", "reviewed_at": "2026-11-12",
             "rationale": "This rationale is long enough to describe why."}
        path.write_text(json.dumps({"schema_version": 1,
                                     "topic_decisions": [e]}), encoding="utf-8")
        with self.assertRaises(ReviewError):
            approved_topic_decisions(self.root, self.rows, {"agent-memory"})
        e["topics"] = ["agent-memory"]
        with self.assertRaises(ReviewError):
            approved_topic_decisions(self.root, self.rows, {"agent-memory"})


if __name__ == "__main__":
    unittest.main()
