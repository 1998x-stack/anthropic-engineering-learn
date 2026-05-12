# Engineering Blogs 汇总

AI/Infra 领域工程博客合集，按来源分目录，共 ~1000 篇文章。

> 最后整理：2026-05-12

---

## 目录结构

```
.
├── anthropic/          Anthropic 官方工程博客 (23 篇)
├── langchain/          LangChain 博客 (6 篇精选 + 409 篇全量)
├── openai/             OpenAI 工程博客 (9 篇)
├── llamaindex/         LlamaIndex 博客 (382 篇)
├── modal/              Modal 博客 (69 篇)
├── e2b/                E2B 博客 (61 篇)
├── browser-use/        Browser Use 博客 (29 篇)
├── browserbase/        Browserbase 博客 (10 篇)
├── _meta/              元数据索引 (JSON)
├── _scripts/           抓取与维护脚本
└── docs/               Anthropic 文档站点镜像
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

## 工具

| 目录 | 说明 |
|------|------|
| `_scripts/` | 博客抓取、清理、去重、索引重建脚本 (12 个 Python 脚本) |
| `_meta/` | 各来源的 JSON 元数据索引 |
