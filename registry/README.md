# Registry — authoritative metadata and provenance (Phase 3)

**Authority:** `registry/records.jsonl` holds stable identities, file paths, source metadata, local-site publication status and links. Legacy `_meta/`, `index.json` and article frontmatter are **read-only inputs** during this phase. They are not removed. The audit is `registry/audit-report.json`.

## Verification is field-level, not assumed

- Data extracted from Markdown, old JSON or the old index is **provisional**. It is not automatically certified as the original publisher's truth.
- Existing official URL/date overrides live in `registry/verified-overrides.json`. Some `evidence_url` entries still point to an Anthropic index page rather than the exact article; treat those as **insufficient article-level evidence pending review**. Their values override old local metadata, but they do not imply a full editorial approval.
- Source-precedence for provisional data: article frontmatter → article header → corresponding `_meta/` JSON → Anthropic `index.json` → Markdown H1 (title only). Verified overrides take precedence over all of these.
- Every chosen field can be traced to `metadata_provenance`. Conflicting candidates are reported, **not erased**; unsupported/unknown dates and authors are omitted.
- Research notes have **their own title**; they do not inherit the original author's byline, publication date or canonical source URL. A link to an original source is represented in `related_ids`.
- `source_sha256` fingerprints the current file and is useful for detecting accidental content changes. It is not a publisher-authentication proof.
- `publication_status=published` here means **a matching static HTML asset is present under `docs/`**, which is the GitHub Pages input. It does not guarantee public deployment or that editorial review passed. `not_published` means no matching HTML was found; `archived` is respected.
- Duplicated canonical URLs, unmatched legacy metadata, unlinked research notes and unmapped HTML appear in `audit-report.json`. These are an **audit queue**, not an excuse to delete historical content.
- The registry is the only authoritative index for **new workflows**; do not hand-edit generated metadata. Make editorial changes in `verified-overrides.json` or source files and regenerate.

## Commands

Use the unified [pipeline CLI](../scripts/README.md); the old per-module commands remain available for compatibility. Python 3.11+, standard library only:

```bash
PYTHONPATH=src python -m ael.reconcile report
PYTHONPATH=src python -m ael.reconcile apply  # deterministically regenerate records + audit
PYTHONPATH=src python -m ael.reconcile check  # fail on drift or broken references
PYTHONPATH=src python -m ael.registry validate
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Migration invariants

1. No original Markdown, old metadata, PDF or HTML gets deleted or rewritten by the reconciler.
2. Stable IDs and existing explicit relationships are preserved, including when filenames later change.
3. The audit records source conflicts and coverage gaps instead of guessing missing facts.
4. No automatic upgrade to `review_status=verified`.
5. The website is **not regenerated** in this phase; static-site link preservation belongs to a later migration.

## Phase 3 update

Use `PYTHONPATH=src python -m ael plan` for a zero-write preview, `PYTHONPATH=src python -m ael check` to enforce reproducibility, and `PYTHONPATH=src python -m ael publish --write` to create the static JSON catalog in a Pages build. The historical crawlers are not called by the pipeline. Original files and HTML pages remain read-only.

## Phase 4: path migrations

A stable note ID can point to a new `content/research/article-notes/<source>/` path. `registry/migrations.json` records old path, new path and original SHA-256. Legacy Markdown paths become compatibility links, excluded from inventory. The moved content is byte-for-byte identical and existing HTML is not rewritten. Use `PYTHONPATH=src python -m ael.migration check` to enforce these invariants. The Registry remains the authority for new paths; the migration manifest is a historical alias map, not a second content index.

## Phase 5 — complete Research consolidation

All 123 registered research notes now live under `content/research/article-notes/`; their 123 legacy Markdown paths are compatibility aliases (not HTTP redirects). `migrations.json` is the identity/path evidence ledger.

`source_reference_url` on a note means an explicitly cited external original; it does not claim that source has been ingested. `audit-report.json` partitions notes into `matched`, `external_only`, `linked_by_id_url_mismatch`, `no_explicit_citation`, and `ambiguous` statuses. Never fabricate a `related_ids` reference when the original is absent.

## Phase 6 — topics, source links, and search index

The search portal at `docs/explore/` consumes the build-time `docs/catalog.json` (schema v2). The prior `count` / `items` still represent only mapped HTML; `records` now covers the full Registry. The search covers titles, metadata and short local excerpts, **not full text or vector embeddings**.

`registry/topics.json` defines transparent title/ID/path keyword heuristics. These are suggestions rather than human-verified topic decisions. `registry/projects.json` contains manually linked, GitHub-confirmed external repositories in `repository_link_only` status; no experimental conclusions are asserted. The page exposes unresolved source associations from the existing citation audit without inventing sources.

## Phase 7 — human-reviewed topics and source-link review queue

The `registry/review-queue.json` is a deterministic, evidence-first checklist derived from `records.jsonl` plus `audit-report.json`. It includes 67 unlinked notes plus four linked records with historical URL mismatches, rather than guessing links.

`registry/review-decisions.json` is the **explicit topic review ledger**. Each decision requires a stable record ID, reviewed topic IDs, current document SHA-256, reviewer identity, review date and evidence rationale. It does not alter `review_status` or automatically create missing `related_ids`. As of this phase the ledger is empty: no human topic approvals are being claimed.

The Explorer's full Markdown index is generated into `docs/explore/data/` with `PYTHONPATH=src python -m ael fulltext --write`; content is neither moved nor edited. PDF records are included by title only. Verify with `... fulltext --check`. No semantic search claims.


## Phase 8 — evidence-gated document review

Whole-document review is separate from topic tagging. The append-only
`registry/content-review-decisions.json` file contains manual review **events**
and initially has no approvals. Do not mark a document verified by editing the
generated Registry directly.

Each event requires a unique event ID, stable Registry ID, action
(approve / reject / revoke), SHA-256 of the reviewed content, reviewer,
ISO review date, substantive rationale and a list of HTTPS evidence URLs.
An approval must include at least one evidence URL. The last event for an
ID determines its status: approve = verified, reject = rejected, revoke =
unreviewed. Earlier events remain in the ledger as an audit history.

The last event's SHA must match **current file bytes**; any material edit blocks
CI until a human re-reviews or revokes. An unledgered verified flag in the
Registry is reset to unreviewed during reconciliation. Topic decisions in
`review-decisions.json` do not confer full-document approval.

Review new events with `PYTHONPATH=src python -m ael review --check`, then
run `PYTHONPATH=src python -m ael reconcile --write` to regenerate the
Registry, and `PYTHONPATH=src python -m ael check` before merging.

## Historical HTML aliases

Some older static HTML pages use a filename that differs from the migrated Research Note slug. `registry/site-aliases.json` is a small, explicit exception list; it is **not** an inferred title-to-ID join. Each alias must point to an existing HTML file in the corresponding publisher directory and record the precise expected page title, matching the current Research Note heading, plus a rationale. Reconciliation rejects missing pages, duplicate mappings, unsafe paths and title mismatches. The original URL remains valid, and the Registry may safely mark that note as having a published HTML asset without changing Markdown or HTML bytes.

## Phase 8.1 — official publication-date evidence

On 2026-11-12, all 23 Anthropic dated overrides were checked against their
specific publisher article pages. The 18 generic blog-homepage evidence links
were replaced with article URLs under `/research/<slug>`, the observed
redirect destinations of the historical `/engineering/<slug>` addresses.
Historical canonical URLs remain unchanged to preserve source-note joins.

`registry/official-date-checks.json` is a point-in-time observational snapshot:
ID, publisher evidence URL, observed publication date, and inspection date.
It does not prove that CI has fetched the live article or that a human editor
has approved the full document. CI rejects missing/duplicate observations,
conflicting dates or evidence URLs, unrelated-article evidence and homepages.
Changing a date requires a fresh official-source inspection and snapshot update.
