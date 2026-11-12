# Research notes — Phase 5 consolidation

All **123** curated and analytical notes use the stable canonical path `content/research/article-notes/<source>/<filename>.md`. The 991 original source articles and 5 PDF papers stay in their historical paths.

- Each moved note reuses the original Git blob: **no substantive Markdown content is rewritten**.
- Every old Markdown location remains a short compatibility note linking to canonical content; it is not an HTTP redirect.
- [Migration manifest](../../registry/migrations.json) records old/new path, stable ID and the original SHA-256. CI checks every alias and every file hash.
- Existing published HTML stays where it was. `docs/catalog.json` adds canonical `content_path`, `legacy_markdown_path` and `source_reference_url` fields as applicable.
- Note citations are parsed only when explicitly labeled as original/source. No title/slug guessing: unmatched captured originals are `external_only`; existing ID links with historical URL differences are `linked_by_id_url_mismatch`; notes without citations are `no_explicit_citation`.
- `registry/audit-report.json` records all coverage gaps and source-reference link status; `review_status` is never auto-upgraded to verified.

Run `PYTHONPATH=src python -m ael.migration check`, `PYTHONPATH=src python -m ael check`, and the full unit-test suite before merging.
