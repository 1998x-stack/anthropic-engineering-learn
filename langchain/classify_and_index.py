#!/usr/bin/env python3
"""Classify LangChain blog posts using precise slug-based rules."""
import os
import re
import shutil

POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")

def classify(slug):
    s = slug.strip("/").lower()
    
    if "newsletter" in s:
        return "newsletters"
    
    # === ANNOUNCEMENTS ===
    if s.startswith("announcing-") or s.startswith("introducing-"):
        if s.startswith("introducing-langserve") or s.startswith("introducing-deploy"):
            return "langsmith-deployment"
        if s.startswith("introducing-airbyte"):
            return "tools-integrations"
        return "announcements"
    # Version releases
    if any(x in s for x in [
        "langchain-v0-1-0", "langchain-v02", "langchain-1-0-alpha",
        "the-new-langchain-architecture", "langchain-vectara",
        "langchain-skills", "langchain-prompt-hub",
        "langchain-templates", "langchain-state-of-ai",
        "goodbye-cves", "documentation-refresh",
        "documentation-refresh-for", "langchain-expression-language",
        "langmem-sdk-launch", "langchain-partners",
        "langchain-and-scrimba", "langchain-expands",
        "state-of-ai-2023", "state-of-ai-2024",
        "series-b", "10m-seed", "seed-round",
        "second-birthday", "first-birthday", "three-years",
        "introducing-interrupt", "join-langchain-at",
        "previewing-interrupt", "interrupt-preview",
        "join-us-for-interrupt", "interrupt-2025-recap",
        "aws-marketplace",
    ]):
        return "announcements"
    
    # === CASE STUDIES ===
    if s.startswith("customers") or s.startswith("customers/"):
        return "case-studies"
    for kw in ["ally-financial-collaborates", "morningstar-intelligence",
               "transforming-mortgage", "llms-accelerate-adyens",
               "how-build-inc-used", "how-captide-is-redefining",
               "how-chaos-labs-built", "how-mendable-leverages",
               "how-moda-builds", "how-minimal-built",
               "how-my-agents-self-heal", "unify-launches-agents",
               "robocorps-code", "credit-genie-insights",
               "customer-bertelsmann"]:
        if s.startswith(kw):
            return "case-studies"
    
    # === LANGSMITH DEPLOYMENT ===
    if any(x in s for x in [
        "introducing-langserve", "introducing-deploy-cli",
        "why-langgraph-platform", "why-agent-infrastructure",
        "why-you-should-outsource", "cognitive-architecture",
        "workspaces-in-langsmith",
        "introducing-langsmith-fleet", "arcade-dev-tools",
        "how-we-deployed", "langgraph-platform-ga",
        "langgraph-cloud", "langsmith-ga",
        "introducing-langsmith-sandboxes",
        "langsmith-is-now-available-in-google",
        "langsmith-incident", "access-control-updates",
        "launching-long-term-memory",
        "langserve-playground", "langsmith-agent-builder",
        "langsmith-cli-skills", "langsmith-alerts",
        "langsmith-homepage-redesign",
        "langsmith-production-logging",
        "langsmith-langchain-oss-eu-ai-act",
        "launching-langgraph-templates",
    ]):
        return "langsmith-deployment"
    
    # === LANGSMITH OBSERVABILITY ===
    if any(x in s for x in [
        "evaluation", "observab", "trace", "monitor",
        "feedback", "insights-agent", "annotation", "polly",
        "spade-", "test-run", "regression", "pairwise",
        "benchmarking", "aligning-llm-as-a-judge",
        "human-judgment", "high-cardinality",
        "how-correct-are", "from-traces", "traces-start",
        "in-the-loop", "self-learning", "auto-eval",
        "auto-evaluator", "openevals", "peering-into-the-soul",
        "how-we-build-evals", "react-agent-benchmarking",
        "extraction-benchmarking", "public-langsmith-benchmarks",
        "reusable-langsmith", "pytest-and-vitest",
        "agent-evaluation-readiness", "agent-observability",
        "easier-evaluations", "debugging-deep-agents",
        "dosu-langsmith", "dataset-schemas",
        "data-annotation-queue", "evaluating-deep",
        "evaluating-skills", "aligning-llm-as-a-judge",
        "testing-fine-tuned", "tracing",
        "using-langsmith-to-support",
        "langsmith-fetch",
    ]):
        if "evaluating-rag" in s or "ragas" in s:
            return "rag-knowledge"
        return "langsmith-observability"
    
    # === DEEP AGENTS ===
    if any(x in s for x in [
        "deep-agent", "deepagents",
        "context-engineering-for-agents",
        "context-management-for-deepagents",
        "using-skills-with-deep-agents",
        "memory-for-agents", "how-agents-can-use-filesystems",
        "new-in-agent-builder", "introducing-agent-builder",
        "agent-builder-generally", "agent-builder-now-in",
        "agent-builder-template", "semantic-search-for-langgraph",
        "how-we-built-agent-builder",
        "how-to-use-memory",
        "execute-code-with-sandboxes",
        "improving-deep-agents",
        "deep-agents-cli", "deep-agents-v0",
        "deep-agents-deploy", "running-subagents",
        "open-deep-research", "the-two-patterns-by-which-agents",
        "the-rise-of-context-engineering",
        "continual-learning",
    ]):
        return "deep-agents"
    
    # === LANGGRAPH CORE ===
    if any(x in s for x in [
        "langgraph",
        "agent-middleware", "agent-frameworks-runtimes",
        "human-in-the-loop", "man-in-the-middle",
        "agent-protocol", "agentic-engineering",
        "assistant-ui", "asssistant-editor",
        "custom-agents", "agent-toolkits",
        "javascript-langgraph", "functional-api",
        "not-another-workflow", "agent-harness",
        "anatomy-of-an-agent", "your-harness-your-memory",
        "harness-engineering", "better-harness",
        "middleware-lets", "runtime-behind",
        "message.state", "standard-message",
        "agentic.frontend", "agent-engineering-a-new",
        "agent-authorization", "two-different.types",
        "what-is-an-agent", "what-is-a-cognitive",
        "ux-for-agents", "command-a-new-tool",
        "custom-authentication-and-access",
        "opengpts", "adding-long-term-memory-to-opengpts",
        "how-to-build-an-agent", "how-we-built-langchains-gtm",
        "how-we-made-our-docs", "our-docs-test-themselves",
    ]):
        return "langgraph-core"
    
    # === RAG & KNOWLEDGE ===
    if any(x in s for x in [
        "chunk", "retrieval", "embed", "vector-store",
        "splitter", "rag", "pinecone", "weaviate",
        "chroma", "milvus", "qdrant", "knowledge-graph",
        "context-compression", "hyde", "parent-document",
        "multi-vector", "semantic-search",
        "conversational-retrieval", "multi-modal-rag",
        "neo4j", "supabase", "timescale", "voyage",
        "xata", "neon",
        "deconstructing-rag", "enhancing-rag",
        "evaluating-rag", "agentic-rag",
        "chat-langchain", "rebuilding-chat-langchain",
        "syncing-data-sources", "semi-structured",
        "graph-based-metadata", "a-chunk-by-any",
        "applying-openai-rag", "beyond-rag",
        "chat-loaders", "chat-models",
        "chat-your-data", "chat-with-your-data",
        "chatopensource", "benchmarking-rag",
        "rag-with-langgraph",
        "construc", "knowledge.graphs",
        "knowledge.base", "document.summary.index",
        "llamaindex", "weblangchain",
        "multi-needle-in-a-haystack",
        "parallel-function-calling",
    ]):
        return "rag-knowledge"
    
    # === TOOLS & INTEGRATIONS ===
    if any(x in s for x in [
        "-x-langchain", "-x-langsmith",
        "integration", "mcp", "connector", "plugin",
        "fireworks", "nvidia", "groq", "anthropic",
        "openai", "mistral", "ollama", "cohere",
        "mongodb", "postgres", "databricks", "snowflake",
        "airbyte", "zapier", "cisco", "auth0",
        "gradio", "streamlit", "demogpt",
        "langsmith-sdk", "tool-calling",
        "code-execution", "code.interpreter",
        "secure-agents", "opentelemetry",
        "cube-x", "composio", "eden-ai",
        "lepton", "multion", "neum",
        "realchar", "rubric-labs", "robocorp",
        "origin-web", "jockey",
        "exa", "unstructured", "langchainhub",
        "langchain-vectara", "langchain-supabase",
        "feature-stores", "summarizing-and-querying",
        "integrating-langchain-with-azure",
        "integrating-chatgpt-with-google",
        "llamafile", "vllm",
        "data-viz-agent",
        "going-beyond-chatbots",
        "json-based-agents",
        "streamlit-llm",
        "fine-tune-your", "fine-tuning-chatgpt",
        "from-foundation",
        "bringing-free-oss",
        "gpt-researcher-x",
        "gpteam", "gptwitter",
        "gradio-llm",
        "langfriend",
        "llms-to-improve",
        "making-data-ingestion",
        "mcp-fad",
        "open-swe",
        "open-source-extraction-service",
        "open-models-have-crossed",
        "openais-bet",
        "the-prompt-landscape",
        "promptim",
        "prompt-selectors",
        "async-api",
        "callbacks",
        "streaming-support",
        "rebuff",
        "recalign",
        "prem-challenge",
        "dataherald",
        "captide",
        "empowering-development",
        "bcg-x-releases",
        "how-coding-agents",
        "js-envs",
        "communication-is-all",
        "code-interpreter-api",
        "choosing-the-right-multi",
        "data-driven-characters",
        "generating-usable-text",
        "agents-round",
        "llms-and-sql",
        "the-hidden-metric",
        "ted-ai-hackathon",
        "student-hacker",
    ]):
        return "tools-integrations"
    
    # === TUTORIALS & GUIDES ===
    if any(x in s for x in [
        "how-to", "tutorial", "guide", "recipe",
        "getting-started", "beginner", "walkthrough",
        "building-chat-langchain", "building-langgraph",
        "building-llm-powered", "building-multi-agent",
        "how-and-when-to-build", "how-do-i-speed",
        "how-we-built-langchains-gtm",
        "mental-health-therapy",
        "incorporating-domain",
        "supercharging-if",
        "using-a-knowledge-graph",
        "generating-useable",
        "exploring-genworlds",
        "exploring-prompt",
        "exploring-uxs",
        "few-shot-prompting",
        "handling-pii-data",
        "implementing-advanced",
        "improving-core-tool",
        "improving-document",
        "in-software-the-code",
        "is-langgraph-used",
        "iterating-towards",
        "making-it-easier",
        "planning-for-agents",
        "planning-agents",
        "plan-and-execute",
        "query-construction",
        "query-transformations",
        "reflection-agents",
        "scipe-",
        "structured-report",
        "structured-tools",
        "tool-calling-with",
        "typescript-support",
        "unifying-ai",
        "unleashing-the-power",
        "use-case-accelerant",
        "ux-for-agents",
        "week-of-7-8",
        "winning-in-ai",
        "automating-web-research",
    ]):
        return "tutorials-guides"
    
    return "general"

def main():
    # Flatten first
    for d in os.listdir(POSTS_DIR):
        dp = os.path.join(POSTS_DIR, d)
        if os.path.isdir(dp):
            for f in os.listdir(dp):
                fp = os.path.join(dp, f)
                if f.endswith(".md"):
                    dest = os.path.join(POSTS_DIR, f)
                    if fp != dest:
                        shutil.move(fp, dest)
            os.rmdir(dp)
    
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith(".md") and f != "index.md"]
    print("Found %d article files" % len(files))
    
    articles = []
    moved = 0
    
    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        try:
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            continue
        
        title_m = re.search(r'title:\s*"([^"]*)"', content)
        date_m = re.search(r'date:\s*"([^"]*)"', content)
        author_m = re.search(r'author:\s*"([^"]*)"', content)
        url_m = re.search(r'url:\s*"([^"]*)"', content)
        
        slug = filename.replace(".md", "")
        title = title_m.group(1) if title_m else slug
        date = date_m.group(1) if date_m else "Unknown"
        author = author_m.group(1) if author_m else "Unknown"
        url = url_m.group(1) if url_m else "https://www.langchain.com/blog/" + slug
        
        category = classify(slug)
        
        cat_dir = os.path.join(POSTS_DIR, category)
        os.makedirs(cat_dir, exist_ok=True)
        
        dest_path = os.path.join(cat_dir, filename)
        
        if filepath != dest_path:
            shutil.move(filepath, dest_path)
            moved += 1
        
        articles.append({
            "slug": slug, "title": title, "date": date,
            "author": author, "url": url, "category": category,
        })
    
    print("Moved %d files" % moved)
    build_index(articles)

def build_index(articles):
    articles.sort(key=lambda x: x["date"], reverse=True)
    
    cat_years = {}
    for a in articles:
        cat = a["category"]
        date = a["date"]
        year = date[:4] if len(date) >= 4 else "Unknown"
        if cat not in cat_years:
            cat_years[cat] = {}
        if year not in cat_years[cat]:
            cat_years[cat][year] = []
        cat_years[cat][year].append(a)
    
    cat_names = {
        "langgraph-core": "LangGraph Core",
        "langsmith-observability": "LangSmith Observability & Evals",
        "langsmith-deployment": "LangSmith Deployment & Platform",
        "rag-knowledge": "RAG & Knowledge",
        "deep-agents": "Deep Agents",
        "case-studies": "Case Studies",
        "tools-integrations": "Tools & Integrations",
        "tutorials-guides": "Tutorials & Guides",
        "newsletters": "Newsletters",
        "announcements": "Announcements",
        "general": "General",
    }
    
    lines = [
        "# LangChain Blog Index",
        "",
        "> Source: https://www.langchain.com/blog",
        "> Archived: 2026-05-11",
        "> Total: %d articles" % len(articles),
        "",
        "## File Structure",
        "",
        "```",
        "external/blog/langchain/posts/",
        "├── langgraph-core/              # LangGraph framework: architecture, graphs, state, middleware",
        "├── langsmith-observability/     # LangSmith: tracing, evals, monitoring, benchmarks",
        "├── langsmith-deployment/        # LangSmith: deployment, LangServe, LangGraph Cloud/Platform",
        "├── rag-knowledge/               # RAG: retrieval, chunking, embeddings, vector stores",
        "├── deep-agents/                 # Deep Agents: agent builder, context engineering, memory",
        "├── case-studies/                # Customer stories and real-world implementations",
        "├── tools-integrations/          # Tools, SDKs, 3rd-party integrations",
        "├── tutorials-guides/            # How-tos, tutorials, recipes, building guides",
        "├── newsletters/                 # Weekly/monthly newsletters",
        "├── announcements/               # Product launches, releases, funding, events",
        "├── general/                     # Uncategorized",
        "└── index.md                     # This file",
        "```",
        "",
        "## Category Summary", "",
        "| Category | Articles |", "| --- | --- |",
    ]
    
    cat_counts = {}
    for a in articles:
        cat = a["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        name = cat_names.get(cat, cat)
        lines.append("| [%s](#%s) | %d |" % (name, cat.replace(" ", "-"), cat_counts[cat]))
    lines.append("")
    
    for cat in sorted(cat_years.keys()):
        cat_name = cat_names.get(cat, cat)
        lines.append("")
        lines.append("## %s" % cat_name)
        lines.append("")
        for year in sorted(cat_years[cat].keys(), reverse=True):
            lines.append("### %s" % year)
            lines.append("")
            lines.append("| Date | Title | File |")
            lines.append("| --- | --- | --- |")
            for a in sorted(cat_years[cat][year], key=lambda x: x["date"], reverse=True):
                date_display = a["date"]
                title_display = a["title"].replace("|", "\\|")
                filename = a["slug"] + ".md"
                lines.append("| %s | [%s](%s) | [%s](./%s/%s) |" % (
                    date_display, title_display, a["url"], filename, cat, filename
                ))
            lines.append("")
    
    lines.append("---\n\n## Stats\n")
    lines.append("- **Total articles:** %d" % len(articles))
    dates = [a["date"] for a in articles if a["date"] != "Unknown"]
    if dates:
        dates.sort()
        lines.append("- **Date range:** %s → %s" % (dates[0], dates[-1]))
    lines.append("- **Categories:** %d" % len(cat_counts))
    lines.append("")
    
    with open(os.path.join(POSTS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("Index: %d articles across %d categories" % (len(articles), len(cat_counts)))
    print("\nDirectory:")
    for cat in sorted(os.listdir(POSTS_DIR)):
        cp = os.path.join(POSTS_DIR, cat)
        if os.path.isdir(cp):
            cnt = len([f for f in os.listdir(cp) if f.endswith(".md")])
            print("  %-35s %3d articles" % (cat_names.get(cat, cat), cnt))
    total = sum(len([f for f in os.listdir(os.path.join(POSTS_DIR, d)) if f.endswith(".md")]) for d in os.listdir(POSTS_DIR) if os.path.isdir(os.path.join(POSTS_DIR, d)))
    print("  %-35s %3d articles" % ("TOTAL", total))

if __name__ == "__main__":
    main()
