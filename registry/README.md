# Registry — Phase 1

`records.jsonl` is the **single authoritative inventory** of currently managed content files. Each JSON line represents one source article, research note, or PDF; metadata is intentionally conservative at bootstrap time.

- Stable `id` identifies the content; `path` is only its current location. Renaming a file must update its registered path **without changing its ID**.
- `review_status=unreviewed` means no human provenance check has been performed. It does **not** mean the content was never displayed on the website.
- `publication_status=unspecified` means publication status has not yet been reconciled with `docs/`.
- Never infer `canonical_url` or publication dates from a filename. Missing facts should remain absent until verified.
- `related_ids` is only automatically added for explicitly named `(musk-interrogation)` notes pointing to a matching source/paper; other relationships require explicit review.
- Legacy `_meta/`, top-level `index.json`, existing frontmatter, and HTML are retained as migration inputs, **not** authoritative for new edits.

Commands (Python 3.11+, no runtime dependencies):

```bash
PYTHONPATH=src python -m ael.registry report
PYTHONPATH=src python -m ael.registry validate
PYTHONPATH=src python -m ael.registry sync           # preview new content records
PYTHONPATH=src python -m ael.registry sync --write   # append records for new content
PYTHONPATH=src python -m unittest discover -s tests -v
```

`sync` never deletes or silently renames existing IDs. Move existing files only after updating their registry paths in the same commit. CI checks coverage, referential integrity, and missing paths. `docs/` is untouched in Phase 1.

Next phase: reconcile verified canonical URLs, publication dates, source hashes, and site visibility; defer filesystem moves and static-site regeneration until link-preservation tests exist.
