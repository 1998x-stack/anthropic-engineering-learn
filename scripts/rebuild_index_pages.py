#!/usr/bin/env python3
"""
Rebuild categorized index.html pages for all blog sources.

Reads markdown directory structure for category mappings,
parses existing HTML for article metadata, and generates
categorized index pages following the Anthropic template.
"""

import os
import re
from pathlib import Path
from html import escape
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# ─── Category definitions per source ────────────────────────────────────────
# Each category: (slug, display_name, emoji, gradient_colors, description)

CATEGORY_DEFS = {
    "langchain": [
        ("curated",               "Curated Picks",          "⭐", ("#10b981", "#059669"), "Hand-selected essential reads on agent harnesses, observability, and memory"),
        ("deep-agents",           "Deep Agents",            "🤖", ("#6366f1", "#8b5cf6"), "Deep agent architectures, context management, and continual learning"),
        ("langgraph-core",        "LangGraph Core",         "🔗", ("#06b6d4", "#0ea5e9"), "LangGraph framework, state machines, functional API, and platform"),
        ("langsmith-observability","LangSmith Observability","🔍", ("#f59e0b", "#d97706"), "Tracing, evals, debugging, and monitoring with LangSmith"),
        ("langsmith-deployment",  "LangSmith Deployment",   "🚀", ("#8b5cf6", "#7c3aed"), "Deploying agents to production with LangGraph Platform"),
        ("rag-knowledge",         "RAG & Knowledge",        "📚", ("#ec4899", "#db2777"), "Retrieval-augmented generation, embeddings, and knowledge management"),
        ("tools-integrations",    "Tools & Integrations",   "🔌", ("#14b8a6", "#0d9488"), "Third-party integrations, MCP, tool calling, and connectors"),
        ("case-studies",          "Case Studies",           "📊", ("#f97316", "#ea580c"), "Real-world production deployments and customer stories"),
        ("announcements",         "Announcements",          "📢", ("#0ea5e9", "#0284c7"), "Product launches, partnerships, and company updates"),
        ("tutorials-guides",      "Tutorials & Guides",     "📖", ("#10b981", "#047857"), "Step-by-step guides and how-to articles"),
        ("general",               "General",                "📝", ("#64748b", "#475569"), "General posts, retrospectives, and ecosystem overviews"),
        ("newsletters",           "Newsletters",            "📬", ("#a855f7", "#9333ea"), "Weekly and monthly roundups"),
    ],
    "llamaindex": [
        ("llamaindex-core",      "LlamaIndex Core",        "🏗️", ("#f59e0b", "#d97706"), "Framework fundamentals — agents, workflows, indexing, and query engines"),
        ("document-processing",  "Document Processing",    "📄", ("#6366f1", "#8b5cf6"), "LlamaParse, OCR, PDF extraction, and document AI"),
        ("rag",                  "RAG",                    "📚", ("#10b981", "#059669"), "Retrieval-augmented generation patterns and pipelines"),
        ("tools-integrations",   "Tools & Integrations",   "🔌", ("#ec4899", "#db2777"), "Third-party connectors, vector stores, and LLM integrations"),
        ("general",              "General",                "📝", ("#64748b", "#475569"), "Community updates, ecosystem overviews, and miscellaneous"),
        ("llamacloud",           "LlamaCloud",             "☁️", ("#0ea5e9", "#0284c7"), "Managed cloud services, hosted parsing, and enterprise RAG"),
        ("benchmarks-evals",     "Benchmarks & Evals",     "🧪", ("#f97316", "#ea580c"), "Evaluation frameworks, benchmark results, and dataset comparisons"),
        ("case-studies",         "Case Studies",           "📊", ("#14b8a6", "#0d9488"), "Production deployments and customer stories"),
        ("newsletters",          "Newsletters",            "📬", ("#a855f7", "#9333ea"), "Roundups and digests"),
    ],
    "modal": [
        ("inference",           "Inference & GPUs",        "⚡", ("#8b5cf6", "#7c3aed"), "GPU inference optimization, model serving, vLLM, and performance engineering"),
        ("sandboxes",           "Sandboxes",               "📦", ("#06b6d4", "#0ea5e9"), "Code sandboxes, directory snapshots, and isolated execution"),
        ("training-finetuning", "Training & Fine-tuning",  "🎯", ("#f59e0b", "#d97706"), "Model training, RL workflows, and fine-tuning on Modal"),
        ("tutorials",           "Tutorials",               "📖", ("#10b981", "#059669"), "Step-by-step guides and example applications"),
        ("general",             "General",                 "📝", ("#64748b", "#475569"), "Company news, partnerships, and general updates"),
        ("engineering",         "Engineering",             "🔧", ("#ec4899", "#db2777"), "Internal engineering deep-dives and infrastructure"),
        ("announcements",       "Announcements",           "📢", ("#0ea5e9", "#0284c7"), "Product launches and major milestones"),
    ],
    "e2b": [
        ("integrations",           "Integrations",              "🔌", ("#6366f1", "#8b5cf6"), "Framework integrations — LangChain, OpenAI, Groq, CrewAI, and more"),
        ("case-studies",           "Case Studies",              "📊", ("#f97316", "#ea580c"), "How teams use E2B in production — interviews and deep dives"),
        ("announcements",          "Announcements",             "📢", ("#0ea5e9", "#0284c7"), "Product launches, funding, and company milestones"),
        ("ai-agents",              "AI Agents",                 "🤖", ("#10b981", "#059669"), "Agent frameworks, code interpreters, and execution environments"),
        ("tutorials",              "Tutorials",                 "📖", ("#14b8a6", "#0d9488"), "Step-by-step guides for building with E2B"),
        ("sandbox-code-execution", "Sandbox & Code Execution",  "📦", ("#8b5cf6", "#7c3aed"), "Core sandbox technology, Firecracker, and runtime internals"),
    ],
    "browserbase": [
        ("tutorials",      "Tutorials",          "📖", ("#f97316", "#ea580c"), "Guides on web scraping, proxies, and headless browsers"),
        ("stagehand",       "Stagehand SDK",      "🎭", ("#6366f1", "#8b5cf6"), "The AI web agent SDK — features and updates"),
        ("general",         "General",            "📝", ("#64748b", "#475569"), "Infrastructure, security, and company updates"),
        ("announcements",   "Announcements",      "📢", ("#0ea5e9", "#0284c7"), "Product launches and milestones"),
    ],
    "browser-use": [
        ("benchmarks-research",      "Benchmarks & Research",      "🧪", ("#6366f1", "#8b5cf6"), "Browser agent benchmarks, model comparisons, and evaluation systems"),
        ("architecture-engineering",  "Architecture & Engineering", "🏗️", ("#06b6d4", "#0ea5e9"), "Agent frameworks, harness design, performance, and infrastructure"),
        ("security-trust",           "Security & Trust",           "🔒", ("#f59e0b", "#d97706"), "Bot detection, authentication, CAPTCHAs, and agent security"),
        ("product-company",          "Product & Company",          "📢", ("#10b981", "#059669"), "Funding, product launches, and milestones"),
        ("case-studies",             "Case Studies",               "📊", ("#f97316", "#ea580c"), "Partner integrations and real-world deployments"),
        ("guides-tutorials",         "Guides & Tutorials",         "📖", ("#ec4899", "#db2777"), "Practical guides for web automation and agent development"),
    ],
    "openai": [
        ("agents-codex",    "Agents & Codex",     "🤖", ("#0ea5e9", "#0284c7"), "Codex harness engineering, Responses API, data agents, and orchestration"),
        ("infrastructure",  "Infrastructure",     "🔧", ("#f59e0b", "#d97706"), "Scaling systems — rate limits, voice AI, and supercomputer networking"),
    ],
}

# ─── Manual category assignments for flat sources ───────────────────────────

BROWSER_USE_CATEGORIES = {
    "ai-browser-agent-benchmark":     "benchmarks-research",
    "online-mind2web-benchmark":      "benchmarks-research",
    "our-browser-agent-evaluation-system": "benchmarks-research",
    "sota-technical-report":          "benchmarks-research",
    "stealth-benchmark":              "benchmarks-research",
    "what-model-to-use":              "benchmarks-research",
    "bitter-lesson-agent-frameworks": "architecture-engineering",
    "bitter-lesson-agent-harnesses":  "architecture-engineering",
    "playwright-to-cdp":              "architecture-engineering",
    "speed-matters":                  "architecture-engineering",
    "llm-gateway":                    "architecture-engineering",
    "browser-infra":                  "architecture-engineering",
    "two-ways-to-sandbox-agents":     "architecture-engineering",
    "everything-i-got-wrong":         "architecture-engineering",
    "bot-detection":                  "security-trust",
    "prove-you-are-a-robot":          "security-trust",
    "web-agent-authentication":       "security-trust",
    "seed-round":                     "product-company",
    "free-tier-announcement":         "product-company",
    "bux-launch-blog":                "product-company",
    "one-year-of-progress":           "product-company",
    "frigade":                        "case-studies",
    "new-generation":                 "case-studies",
    "parallel":                       "case-studies",
    "how-to-win-hackathons":          "guides-tutorials",
    "web-scraping-guide-2026":        "guides-tutorials",
    "agent-freedom":                  "guides-tutorials",
    "web-agents-that-actually-learn": "guides-tutorials",
}

OPENAI_CATEGORIES = {
    "harness-engineering":                          "agents-codex",
    "equip-responses-api-computer-environment":     "agents-codex",
    "inside-our-in-house-data-agent":               "agents-codex",
    "open-source-codex-orchestration-symphony":     "agents-codex",
    "speeding-up-agentic-workflows-with-websockets":"agents-codex",
    "unlocking-the-codex-harness":                  "agents-codex",
    "beyond-rate-limits":                           "infrastructure",
    "delivering-low-latency-voice-ai-at-scale":     "infrastructure",
    "mrc-supercomputer-networking":                 "infrastructure",
}

# ─── Source page configs ────────────────────────────────────────────────────

SOURCE_CONFIGS = {
    "langchain": {
        "title":       "LangChain",
        "page_title":  "LangChain — Engineering Blogs",
        "hero_tag":    "https://www.langchain.com/blog",
        "description": "LangGraph, LangSmith, RAG, deep agents, case studies, and tutorials.",
        "source_url":  "https://www.langchain.com/blog",
        "source_label":"langchain.com/blog",
        "icon_gradient": ("#10b981", "#059669"),
    },
    "llamaindex": {
        "title":       "LlamaIndex",
        "page_title":  "LlamaIndex — Engineering Blogs",
        "hero_tag":    "https://www.llamaindex.ai/blog",
        "description": "RAG pipelines, document processing, LlamaCloud, and framework updates.",
        "source_url":  "https://www.llamaindex.ai/blog",
        "source_label":"llamaindex.ai/blog",
        "icon_gradient": ("#f59e0b", "#d97706"),
    },
    "modal": {
        "title":       "Modal",
        "page_title":  "Modal — Engineering Blogs",
        "hero_tag":    "https://modal.com/blog",
        "description": "Serverless GPU inference, sandboxes, model training and fine-tuning.",
        "source_url":  "https://modal.com/blog",
        "source_label":"modal.com/blog",
        "icon_gradient": ("#8b5cf6", "#7c3aed"),
    },
    "e2b": {
        "title":       "E2B",
        "page_title":  "E2B — Engineering Blogs",
        "hero_tag":    "https://e2b.dev/blog",
        "description": "Cloud sandboxes for AI agents — code execution, integrations, and tutorials.",
        "source_url":  "https://e2b.dev/blog",
        "source_label":"e2b.dev/blog",
        "icon_gradient": ("#ec4899", "#db2777"),
    },
    "browserbase": {
        "title":       "Browserbase",
        "page_title":  "Browserbase — Engineering Blogs",
        "hero_tag":    "https://www.browserbase.com/blog",
        "description": "Cloud browser infrastructure — Stagehand SDK, automation, and tutorials.",
        "source_url":  "https://www.browserbase.com/blog",
        "source_label":"browserbase.com/blog",
        "icon_gradient": ("#f97316", "#ea580c"),
    },
    "browser-use": {
        "title":       "Browser Use",
        "page_title":  "Browser Use — Engineering Blogs",
        "hero_tag":    "https://browser-use.com/posts",
        "description": "Browser agents, web automation, benchmarks, and harness architecture.",
        "source_url":  "https://browser-use.com/posts",
        "source_label":"browser-use.com",
        "icon_gradient": ("#14b8a6", "#0d9488"),
    },
    "openai": {
        "title":       "OpenAI Engineering",
        "page_title":  "OpenAI Engineering — Engineering Blogs",
        "hero_tag":    "https://openai.com/index",
        "description": "OpenAI engineering posts on harness design, voice AI, agent infrastructure, and systems at scale.",
        "source_url":  "https://openai.com/index",
        "source_label":"openai.com/index",
        "icon_gradient": ("#0ea5e9", "#0284c7"),
    },
}


def build_category_map(source: str) -> dict[str, str]:
    """Build {html_filename_stem: category_slug} mapping."""
    if source == "browser-use":
        return dict(BROWSER_USE_CATEGORIES)
    if source == "openai":
        return dict(OPENAI_CATEGORIES)

    cat_map = {}
    if source == "langchain":
        curated_dir = ROOT / "langchain" / "curated"
        if curated_dir.exists():
            for f in curated_dir.glob("*.md"):
                cat_map[f.stem] = "curated"
        posts_dir = ROOT / "langchain" / "posts"
    elif source == "llamaindex":
        posts_dir = ROOT / "llamaindex" / "posts"
    else:
        posts_dir = ROOT / source / "posts"

    if posts_dir.exists():
        for cat_dir in posts_dir.iterdir():
            if cat_dir.is_dir():
                cat_slug = cat_dir.name
                for f in cat_dir.glob("*.md"):
                    cat_map[f.stem] = cat_slug

    return cat_map


def parse_existing_html(source: str) -> list[dict]:
    """Parse existing index.html to extract article metadata."""
    index_path = DOCS / source / "index.html"
    if not index_path.exists():
        return []

    html = index_path.read_text(encoding="utf-8")
    articles = []

    card_pattern = re.compile(
        r'<a\s+href="([^"]+)"\s+class="card\s+card-done">'
        r'.*?<h3>(.*?)</h3>'
        r'.*?<span\s+class="card-date">(.*?)</span>'
        r'.*?</a>',
        re.DOTALL
    )

    for m in card_pattern.finditer(html):
        href = m.group(1)
        title = m.group(2).strip()
        date = m.group(3).strip()
        stem = href.replace(".html", "")

        title = re.sub(r'<[^>]+>', '', title)
        title = title.replace("&amp;", "&").replace("&#x27;", "'").replace("&#39;", "'").replace("&lt;", "<").replace("&gt;", ">")

        articles.append({
            "href": href,
            "stem": stem,
            "title": title,
            "date": date,
        })

    # Also check for TODO cards (no href)
    todo_pattern = re.compile(
        r'<div\s+class="card\s+card-todo">'
        r'.*?<h3>(.*?)</h3>'
        r'.*?</div>\s*</div>',
        re.DOTALL
    )
    for m in todo_pattern.finditer(html):
        title = m.group(1).strip()
        title = re.sub(r'<[^>]+>', '', title)

    return articles


def sort_key(article: dict) -> str:
    """Sort by date descending. Unknown dates go last."""
    d = article["date"]
    if d == "Unknown" or not d:
        return "0000-00-00"
    return d


def generate_index_html(source: str) -> str:
    """Generate categorized index.html for a source."""
    config = SOURCE_CONFIGS[source]
    cat_defs = CATEGORY_DEFS[source]
    cat_map = build_category_map(source)
    articles = parse_existing_html(source)

    # Group articles by category
    by_cat: dict[str, list[dict]] = defaultdict(list)
    uncategorized = []
    for art in articles:
        cat = cat_map.get(art["stem"])
        if cat:
            by_cat[cat].append(art)
        else:
            uncategorized.append(art)

    # Sort each category by date descending
    for cat_slug in by_cat:
        by_cat[cat_slug].sort(key=sort_key, reverse=True)
    uncategorized.sort(key=sort_key, reverse=True)

    total_articles = len(articles)
    total_done = total_articles  # all are card-done
    num_cats = len([c for c in cat_defs if by_cat.get(c[0])])
    if uncategorized:
        num_cats += 1

    # Build HTML
    sections = []
    for cat_slug, display_name, emoji, (c1, c2), desc in cat_defs:
        arts = by_cat.get(cat_slug, [])
        if not arts:
            continue

        cards_html = []
        for art in arts:
            t = escape(art["title"])
            cards_html.append(
                f'      <a href="{art["href"]}" class="card card-done">'
                f'<div class="card-status"><span class="badge-done">✓</span></div>'
                f'<div class="card-body"><h3>{t}</h3>'
                f'<div class="card-meta"><span class="card-date">{art["date"]}</span></div>'
                f'</div></a>'
            )

        section = f"""
  <!-- ====== {display_name.upper()} ====== -->
  <section class="category">
    <div class="category-header">
      <div class="category-icon" style="background:linear-gradient(135deg,{c1},{c2})">{emoji}</div>
      <div>
        <h2>{escape(display_name)}</h2>
        <p>{escape(desc)}</p>
      </div>
      <span class="category-count">{len(arts)}</span>
    </div>
    <div class="cards">
{chr(10).join(cards_html)}
    </div>
  </section>"""
        sections.append(section)

    # Uncategorized section
    if uncategorized:
        cards_html = []
        for art in uncategorized:
            t = escape(art["title"])
            cards_html.append(
                f'      <a href="{art["href"]}" class="card card-done">'
                f'<div class="card-status"><span class="badge-done">✓</span></div>'
                f'<div class="card-body"><h3>{t}</h3>'
                f'<div class="card-meta"><span class="card-date">{art["date"]}</span></div>'
                f'</div></a>'
            )
        section = f"""
  <!-- ====== UNCATEGORIZED ====== -->
  <section class="category">
    <div class="category-header">
      <div class="category-icon" style="background:linear-gradient(135deg,#94a3b8,#64748b)">📄</div>
      <div>
        <h2>Other</h2>
        <p>Articles not yet categorized</p>
      </div>
      <span class="category-count">{len(uncategorized)}</span>
    </div>
    <div class="cards">
{chr(10).join(cards_html)}
    </div>
  </section>"""
        sections.append(section)

    g1, g2 = config["icon_gradient"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(config["page_title"])}</title>
  <link rel="stylesheet" href="../assets/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    .category-count {{
      font-size: 13px;
      font-weight: 700;
      background: #f1f5f9;
      color: var(--text-secondary);
      padding: 4px 12px;
      border-radius: 999px;
      margin-left: auto;
      flex-shrink: 0;
    }}
  </style>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href=".." class="nav-brand">
      <span class="nav-logo">⚡</span>
      <span>Engineering Blogs Hub</span>
    </a>
    <a href=".." style="font-size:13px;color:var(--text-secondary)">← Back to Hub</a>
  </div>
</nav>

<header class="hero">
  <div class="hero-inner">
    <div class="hero-tag">{escape(config["hero_tag"])}</div>
    <h1>{escape(config["title"])}</h1>
    <p>{escape(config["description"])}</p>
    <div class="hero-stats">
      <div class="stat"><span class="stat-num">{total_articles}</span><span class="stat-label">Articles</span></div>
      <div class="stat"><span class="stat-num done">{total_done}</span><span class="stat-label">Deep-Dives</span></div>
      <div class="stat"><span class="stat-num">{num_cats}</span><span class="stat-label">Categories</span></div>
    </div>
  </div>
</header>

<main class="container">
{"".join(sections)}

</main>

<footer class="footer">
  <p>Source: <a href="{config["source_url"]}" target="_blank">{escape(config["source_label"])}</a> · <a href="..">← Back to Hub</a></p>
</footer>

</body>
</html>
"""


def main():
    for source in SOURCE_CONFIGS:
        print(f"Building {source}...")
        html = generate_index_html(source)
        out_path = DOCS / source / "index.html"
        out_path.write_text(html, encoding="utf-8")

        # Report stats
        cat_map = build_category_map(source)
        articles = parse_existing_html(source)
        categorized = sum(1 for a in articles if a["stem"] in cat_map)
        print(f"  → {len(articles)} articles, {categorized} categorized, "
              f"{len(articles) - categorized} uncategorized")

    print("\nDone!")


if __name__ == "__main__":
    main()
