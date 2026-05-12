# HTML Generation TODO

> Generated: 2026-05-12
> Design system: see [gotchas.md](gotchas.md)

## Priority Order

### Batch 1: Anthropic (3 remaining) — DONE
- [x] `anthropic/tools-mcp/claude-think-tool.html`
- [x] `anthropic/tools-mcp/contextual-retrieval.html`
- [x] `anthropic/tools-mcp/desktop-extensions.html`

### Batch 2: OpenAI (9 articles)
- [ ] `openai/posts/*.html` (9 articles — harness engineering, voice AI, etc.)

### Batch 3: Browser Use (28 articles)
- [ ] `browser-use/posts/*.html` (28 articles)

### Batch 4: Browserbase (10 articles)
- [ ] `browserbase/posts/*.html` (10 articles)

### Batch 5: E2B (61 articles)
- [ ] `e2b/posts/*.html` (61 articles, 6 categories)

### Batch 6: Modal (69 articles)
- [ ] `modal/posts/*.html` (69 articles, 7 categories)

### Batch 7: LangChain (415 articles)
- [ ] `langchain/posts/*.html` (415 articles, 11 categories)

### Batch 8: LlamaIndex (382 articles)
- [ ] `llamaindex/posts/*.html` (382 articles, 10 categories)

## Design Rules (from gotchas.md)

1. Deep-dive pages use **inline `<style>`**, not shared CSS
2. Each page: Hero (gradient + stats) → TOC → Sections (h2+emoji+lead) → Footer
3. At least 3 visualizations per page (charts/timeline/compare/flow)
4. Fonts: Noto Sans SC + Inter + JetBrains Mono (Google Fonts)
5. Responsive: 768px breakpoint
6. Nav: brand → hub (`../../`), back → source index (`../`)
7. After each batch: `git add + commit + push` to deploy

## Completion Status

| Source | Total | Done | Remaining |
|--------|-------|------|-----------|
| Anthropic | 23 | 23 | 0 |
| OpenAI | 9 | 0 | 9 |
| Browser Use | 28 | 0 | 28 |
| Browserbase | 10 | 0 | 10 |
| E2B | 61 | 0 | 61 |
| Modal | 69 | 0 | 69 |
| LangChain | 415 | 0 | 415 |
| LlamaIndex | 382 | 0 | 382 |
| **Total** | **997** | **23** | **974** |
