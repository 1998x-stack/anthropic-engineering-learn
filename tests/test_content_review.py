"""SHA-bound, event-sourced content approval, rejection and revocation."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from ael.review import ReviewError, approved_content_decisions
from ael.reconcile import enrich


class ContentReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / "anthropic/agents/example.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text("# Example\n\nOriginal content.\n", encoding="utf-8")
        self.row = {"id": "source:anthropic:example", "kind": "source_article",
                    "source": "anthropic", "path": "anthropic/agents/example.md",
                    "review_status": "unreviewed", "publication_status": "not_published"}
        (self.root / "registry").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def event(self, action="approve", event_id="event-1"):
        return {"event_id": event_id, "id": self.row["id"], "action": action,
                "evidence_sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
                "reviewer": "editor@example.org", "reviewed_at": "2026-11-12",
                "rationale": "Checked the complete article against primary-source evidence.",
                "evidence_urls": ["https://www.anthropic.com/engineering/example"]}

    def write_events(self, events):
        (self.root / "registry/content-review-decisions.json").write_text(
            json.dumps({"schema_version": 1, "events": events}), encoding="utf-8")

    def test_manual_verified_flag_is_not_trusted(self):
        output, _ = enrich(self.root, [dict(self.row, review_status="verified")])
        self.assertEqual(output[0]["review_status"], "unreviewed")

    def test_approval_and_rejection_have_current_hash_evidence(self):
        self.write_events([self.event()])
        self.assertEqual(approved_content_decisions(self.root, [self.row])[self.row["id"]],
                         "verified")
        output, _ = enrich(self.root, [self.row])
        self.assertEqual(output[0]["review_status"], "verified")
        self.write_events([self.event("reject")])
        output, _ = enrich(self.root, [self.row])
        self.assertEqual(output[0]["review_status"], "rejected")

    def test_revocation_keeps_history_and_withdraws_approval(self):
        self.write_events([self.event(), self.event("revoke", "event-2")])
        output, _ = enrich(self.root, [self.row])
        self.assertEqual(output[0]["review_status"], "unreviewed")
        ledger = json.loads((self.root / "registry/content-review-decisions.json").read_text())
        self.assertEqual(len(ledger["events"]), 2)

    def test_file_change_blocks_stale_approval(self):
        self.write_events([self.event()])
        self.path.write_text("# Example\n\nMaterially changed content.\n", encoding="utf-8")
        with self.assertRaises(ReviewError):
            enrich(self.root, [self.row])

    def test_invalid_evidence_and_duplicate_events_rejected(self):
        event = self.event()
        event["evidence_urls"] = []
        self.write_events([event])
        with self.assertRaises(ReviewError):
            approved_content_decisions(self.root, [self.row])
        event["evidence_urls"] = ["https://www.anthropic.com/engineering/example"]
        self.write_events([event, event])
        with self.assertRaises(ReviewError):
            approved_content_decisions(self.root, [self.row])
        event["id"] = "source:anthropic:unknown"
        self.write_events([event])
        with self.assertRaises(ReviewError):
            approved_content_decisions(self.root, [self.row])


if __name__ == "__main__":
    unittest.main()
