# Knowledge Explorer — Phase 7

The Knowledge Explorer is a dependency-free static search interface for the **entire Registry**. Deployed by GitHub Pages at `/explore/`, preserving all old published HTML routes.

## Search: complete Markdown text

- `docs/catalog.json` remains a **metadata** index with all Registry records, heuristic topics and explicit links. Its backwards-compatible `count`/`items` fields still contain only published HTML.
- `docs/explore/data/manifest.json` and approximately 36 source-specific `.json` shards are **generated only during Pages builds**, never committed. Run `PYTHONPATH=src python -m ael fulltext --write` locally to create them.
- Every registered `.md` is indexed using its **full locally stored Markdown text**, not a truncated excerpt. The 5 `.pdf` entries are **metadata-only** (no OCR or PDF extraction); they are included in the index for consistent ID coverage.
- The browser initially loads the small metadata catalog. On the first nonempty full-text query, it lazily fetches shards with bounded concurrency, then reranks results by title/metadata/body. Users can choose metadata-only mode for faster, lighter searches.
- Keyword matching is simple case-insensitive Unicode NFKC **literal substring search** with AND semantics across whitespace-separated terms. There is no semantic vector retrieval, phrase stemming, BM25 index, PDF body search, or search server.
- Full-text shards contain snippets of third-party articles already held in this repository. They are generated from local files only; no remote crawling, embeddings or LLM summaries.
- JSON rendering uses DOM `textContent`, not `innerHTML`, to prevent executing Markdown or source text as code.

## Provenance review and topic policy

- [Source review queue](../../registry/review-queue.json) lists unresolved original-source links plus already linked notes whose historical URL differs. It is regenerated with `PYTHONPATH=src python -m ael review --write`, checked with `... review --check`.
- Currently the queue has **67 unlinked notes + 4 URL mismatch cases**. The queue does **not** create speculative source IDs; a noted external URL is not evidence that the matching Markdown has already been ingested.
- [Topic reviews](../../registry/review-decisions.json) start empty. A human editor may add explicit decisions with stable Registry ID, selected topic slugs, document SHA-256, reviewer, date and at least a 20-character evidence rationale. The system rejects missing/stale evidence or undefined topics. Only those reviewed entries override [heuristic topics](../../registry/topics.json).
- The existing `review_status` field is **not** automatically promoted to `verified`. Topic-level review and whole-document editorial review are separate concepts.
- [External experiment repos](../../registry/projects.json) are links to existing GitHub projects, not substantiated claims of reproducibility.

## Local commands

```bash
PYTHONPATH=src python -m ael check
PYTHONPATH=src python -m ael review --check
PYTHONPATH=src python -m ael publish --write
PYTHONPATH=src python -m ael fulltext --write
PYTHONPATH=src python -m ael fulltext --check
PYTHONPATH=src python -m unittest discover -s tests -v
node --test tests/test_search_engine.cjs
```

Use a local HTTP static server rooted at `docs/` to test the frontend, because browsers may block `fetch` for `file:` URLs. The fulltext writer may remove **only stale generated shard JSON files** inside `docs/explore/data/`. It does not write Markdown, PDF, legacy HTML or Registry data.

## Next evidence work

Review 20 external citations for import suitability, verify the four historical alias mappings, and identify original URLs for 47 notes without a citation; some more notes may later be added to the queue. Link a research note to a captured source only after inspecting the actual publisher evidence.