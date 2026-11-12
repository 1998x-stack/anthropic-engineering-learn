# Registry — authoritative metadata and provenance (Phase 3)

**Authority:** `registry/records.jsonl` holds stable identities, file paths, source metadata, local-site publication status and links. Legacy `_meta/`, `index.json` and article frontmatter are **read-only inputs** during this phase. They are not removed. The audit is `registry/audit-report.json`.

## Verification is field-level, not assumed

- Data extracted from Markdown, old JSON or the old index is **provisional**. It is not automatically certified as the original publisher's truth.
- A small, human-checked collection of official URLs and dates lives in `registry/verified-overrides.json`. The `evidence_url` points to the actual primary-source page. Its values override old local metadata, but `review_status` remains `unreviewed` until full editorial review.
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

`source_reference_url` on a note means an explicitly cited external original; it does not claim that source has been ingested. `audit-report.json` partitions notes into `matched`, `external_only`, `no_explicit_citation`, and `ambiguous` statuses. Never fabricate a `related_ids` reference when the original is absent.
