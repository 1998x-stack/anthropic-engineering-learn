# Engineering Blogs 汇总

> **Architecture migration (Phase 7):** The reconciled source-of-truth inventory and audit live in [registry/records.jsonl](registry/records.jsonl). Use [scripts/README.md](scripts/README.md) for the supported dry-run-first CLI, and [registry/README.md](registry/README.md) for provenance and audits. All 123 curated/research notes are now consolidated under `content/research/article-notes/` with old Markdown compatibility links; publisher source articles and historical HTML remain in place. The [Knowledge Explorer](https://1998x-stack.github.io/anthropic-engineering-learn/explore/) now provides a Registry-wide search portal.

AI/Infra 领域工程知识合集：Registry 登记 **991 篇来源文章、123 篇研究笔记、5 份 PDF**，按来源保留现有目录。

> Registry 统计基准：2026-11-12（由 records.jsonl 提供）

---

## 目录结构

```
.
├── anthropic/          Anthropic 官方工程博客 (23 篇)
├── langchain/          LangChain 博客 (99 篇精选 + 409 篇来源文章)
├── openai/             OpenAI 工程博客 (9 篇)
├── llamaindex/         LlamaIndex 博客 (382 篇来源文章 + 8 篇精选)
├── modal/              Modal 博客 (69 篇)
├── e2b/                E2B 博客 (61 篇)
├── browser-use/        Browser Use 博客 (29 篇)
├── browserbase/        Browserbase 博客 (10 篇)
├── _meta/              元数据索引 (JSON)
├── _scripts/           历史维护脚本（不再作为官方入口）
├── registry/           权威内容清单与审计结果
├── src/ael/            安全、可校验的统一 CLI
├── scripts/            历史页面生成脚本及迁移说明
└── docs/               GitHub Pages 静态内容与构建时目录
```

---

## Anthropic (`anthropic/`)

Anthropic 官方工程实践文章，按主题分类。

| 分类 | 篇数 | 内容 |
|------|------|------|
| [agents/](anthropic/agents/) | 8 | Building effective agents, context engineering, harness design, managed agents |
| [tools-mcp/](anthropic/tools-mcp/) | 6 | Tool use, MCP, think tool, contextual retrieval, desktop extensions |
| [evals/](anthropic/evals/) | 4 | Agent evals, SWE-bench, eval awareness |
| [reliability/](anthropic/reliability/) | 3 | Postmortems, infrastructure noise |
| [claude-code/](anthropic/claude-code/) | 2 | Auto mode, sandboxing |
| [infrastructure/](anthropic/infrastructure/) | — | 基础设施 |

## LangChain (`langchain/`)

| 子目录 | 内容 |
|--------|------|
| [curated/](langchain/curated/) | 6 篇精选：agent harness, subagents, observability, GTM agent, human judgment, memory |
| [posts/](langchain/posts/) | 409 篇全量，含 11 个分类 (announcements, case-studies, deep-agents, langgraph-core, langsmith, rag, tools, tutorials 等) |

## OpenAI (`openai/`)

9 篇 OpenAI 工程博客：rate limits, voice AI, responses API, harness engineering, data agent 等。

## LlamaIndex (`llamaindex/`)

382 篇，按 10 个分类：benchmarks-evals, case-studies, document-processing, llamacloud, llamaindex-core, newsletters, rag, tools-integrations 等。

## Modal (`modal/`)

69 篇，按 7 个分类：announcements, engineering, general, inference 等。

## E2B (`e2b/`)

61 篇，按 6 个分类：ai-agents, announcements, case-studies, integrations 等。

## Browser Use (`browser-use/`)

29 篇：agent benchmarks, bot detection, browser automation, harness design 等。

## Browserbase (`browserbase/`)

10 篇，按 4 个分类：announcements, general, stagehand, tutorials。

---

## Knowledge Explorer · 跨来源检索

打开 [知识检索门户](https://1998x-stack.github.io/anthropic-engineering-learn/explore/)：可按来源、内容类型、主题、站点发布状态和来源关联状态筛选 **1,119 条 Registry 记录**（阶段 6 基线）。尚未发布 HTML 的条目提供 GitHub Markdown / PDF 跳转，已有 HTML 的条目继续使用原有页面。支持按需加载的完整 Markdown 关键词检索（PDF 仅可检索元数据，非语义向量检索）。主题默认是关键词建议；只有经编辑提供 SHA-256 证据与审阅记录的决策才显示为已审核。

67 篇未建立本地原文关联的笔记已列入 [来源核验队列](registry/review-queue.json)，另有 4 篇需检查历史 URL 差异。尚无充足证据的记录不会自动关联。关联项目仅作为工程仓库链接，不声称实验结果已验证。实现与证据政策见 [docs/explore/README.md](docs/explore/README.md)、[registry/topics.json](registry/topics.json) 与 [registry/projects.json](registry/projects.json)。

## 工具

| 目录 | 说明 |
|------|------|
| `src/ael/` | 正式入口：`PYTHONPATH=src python -m ael plan`，再按需显式 `--write` |
| `_meta/` | 旧 JSON 元数据（只读，暂不删除） |
