# Knowledge Explorer — Phase 6

This folder is a small, dependency-free static search interface for the **entire Registry**, not just its published HTML files. GitHub Pages serves it at `/explore/`.

## Data and evidence policy

- `docs/catalog.json` is derived deterministically by `PYTHONPATH=src python -m ael publish --write`. **It is generated during GitHub Pages builds**, not checked into Git.
- The original `count` and `items` remain the published-HTML-only list (523 mapped pages at Phase 6 baseline).
- New `records` contains every Registry identity (1,119 at baseline). When an HTML page exists the portal links to it; otherwise it links to the stored GitHub file.
- Search matches **titles, metadata, topics and a short local Markdown excerpt**. No full-text index, semantic embeddings, remote crawling or AI-generated summaries are claimed.
- Topics come from [topic rules](../../registry/topics.json), using title, ID and path keyword matching. These are transparent **heuristic suggestions**, not manually reviewed classifications.
- A Research note's `reference_status` comes from the [source link audit](../../registry/audit-report.json). Exact relationships are only those in `related_ids`; external citations are not invented ingested articles.
- Three directly verified repositories are [linked](../../registry/projects.json) as external engineering projects, **not** verified experiments or measured results.
- Existing HTML, PDFs, Markdown sources and backward-compatible old note links are preserved.

## Supported workflow

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m ael check
PYTHONPATH=src python -m ael publish --write
PYTHONPATH=src python -m ael publish --check
```

Open a static file server from `docs/` after generating `catalog.json` to test the UI locally; loading the HTML directly as a `file:` URL can block JSON fetches in browsers.

## Next improvements

Editorial review of currently unlinked notes; manual topic corrections with evidence; optional verified full-text indexing and curated topic pages. Never infer missing original links from title similarity without source evidence.
