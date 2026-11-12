# Phase 4: Source / Research separation (pilot)

**Decision:** original publisher content stays under the existing source directories during this pilot. Only two existing, original-language-independent *research notes* are moved into \`content/research/article-notes/<source>/\`. The site remains served from \`docs/\`.

## Invariants

1. \`registry/records.jsonl\` remains the single authority for content identity. A move changes \`path\` but **never** \`id\`.
2. \`registry/migrations.json\` records \`id\`, old path, new path and the pre-move SHA-256 of the full Markdown file. CI verifies that the moved file matches those bytes exactly.
3. The old Markdown path becomes a visible **compatibility link** to the new file. It is not a real HTTP 301; existing GitHub links continue to open a page that links to the full content. The old file is excluded from the content inventory to prevent double counting.
4. Previously published HTML pages and existing source documents remain byte-for-byte unchanged. Website routing is not rewritten.
5. Validation checks missing or modified compatibility links, invalid paths, duplicate migrated IDs, modified content, and missing published HTML.
6. CI will never bulk-delete source content or silently reinterpret a moved document as a new article.
7. Existing \`_meta/\`, \`index.json\`, source Markdown and PDFs remain in their historical locations. Moving all sources or regenerating HTML is explicitly out of scope.

## Pilot moves

- \`note:anthropic:building-effective-agents:interrogation\` → \`content/research/article-notes/anthropic/\`
- \`note:langchain:01-the-anatomy-of-an-agent-harness\` → \`content/research/article-notes/langchain/\`

These demonstrate separate original source and interpretation layers with distinct types and preserved links.

## Check

\`\`\`bash
PYTHONPATH=src python -m ael.migration check
PYTHONPATH=src python -m ael check
PYTHONPATH=src python -m unittest discover -s tests -v
\`\`\`

Future migration batches must add a manifest entry (with original SHA-256), move the entire file byte-for-byte, leave a corresponding compatibility link and reconcile the Registry and audit report in the **same PR**. No automatic mass migration will run against \`main\`.
