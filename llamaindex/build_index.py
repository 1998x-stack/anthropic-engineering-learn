#!/usr/bin/env python3
"""Build index.md from metadata files and create categorized index."""
import os
import json
from datetime import datetime

META_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meta")
POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")

CATEGORY_NAMES = {
    "document-processing": "Document Processing & OCR",
    "rag": "RAG & Retrieval",
    "llamacloud": "LlamaCloud",
    "tools-integrations": "Tools & Integrations",
    "benchmarks-evals": "Benchmarks & Evaluations",
    "case-studies": "Case Studies",
    "llamaindex-core": "LlamaIndex Core",
    "tutorials-guides": "Tutorials & Guides",
    "newsletters": "Newsletters",
    "general": "General",
}

def main():
    articles = []
    
    for filename in os.listdir(META_DIR):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(META_DIR, filename)
        try:
            with open(filepath, encoding="utf-8") as f:
                meta = json.load(f)
            meta["filename"] = filename.replace(".json", "")
            articles.append(meta)
        except:
            pass
    
    # Sort by date (newest first)
    articles.sort(key=lambda x: x.get("date", "Unknown"), reverse=True)
    
    # Group by category, then by year
    cat_years = {}
    for a in articles:
        cat = a.get("category", "general")
        date = a.get("date", "Unknown")
        year = date[:4] if len(date) >= 4 else "Unknown"
        
        if cat not in cat_years:
            cat_years[cat] = {}
        if year not in cat_years[cat]:
            cat_years[cat][year] = []
        cat_years[cat][year].append(a)
    
    lines = [
        "# LlamaIndex Blog Index",
        "",
        "> Source: https://www.llamaindex.ai/blog",
        "> Archived: " + datetime.now().strftime("%Y-%m-%d"),
        "> Total: %d articles" % len(articles),
        "",
        "## File Structure",
        "",
        "```",
        "external/blog/llamaindex/posts/",
        "├── document-processing/    # Document processing, OCR, parsing",
        "├── rag/                    # RAG, retrieval, vector stores",
        "├── llamacloud/             # LlamaCloud features",
        "├── tools-integrations/     # MCP, SDKs, 3rd-party integrations",
        "├── benchmarks-evals/       # Benchmarks, evaluations, comparisons",
        "├── case-studies/           # Customer stories, real-world usage",
        "├── llamaindex-core/        # LlamaIndex framework releases & updates",
        "├── tutorials-guides/       # How-tos, tutorials, recipes",
        "├── newsletters/            # Weekly newsletters",
        "├── general/                # Uncategorized articles",
        "└── index.md                # This file",
        "```",
        "",
    ]
    
    # Category index with counts
    lines.append("## Category Summary")
    lines.append("")
    lines.append("| Category | Articles |")
    lines.append("| --- | --- |")
    
    cat_counts = {}
    for a in articles:
        cat = a.get("category", "general")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        name = CATEGORY_NAMES.get(cat, cat)
        lines.append("| [%s](#%s) | %d |" % (name, cat.replace(" ", "-"), cat_counts[cat]))
    
    lines.append("")
    
    # Full article list by category
    for cat in sorted(cat_years.keys()):
        cat_name = CATEGORY_NAMES.get(cat, cat)
        lines.append("")
        lines.append("## %s" % cat_name)
        lines.append("")
        
        for year in sorted(cat_years[cat].keys(), reverse=True):
            lines.append("### %s" % year)
            lines.append("")
            lines.append("| Date | Title | File |")
            lines.append("| --- | --- | --- |")
            
            for a in sorted(cat_years[cat][year], key=lambda x: x.get("date", ""), reverse=True):
                date_display = a.get("date", "")
                title_display = a.get("title", "").replace("|", "\\|")
                url = a.get("url", "")
                filename = a["filename"] + ".md"
                lines.append("| %s | [%s](%s) | [%s](./%s/%s) |" % (
                    date_display, title_display, url, filename, cat, filename
                ))
            lines.append("")
    
    # Stats
    lines.append("---")
    lines.append("")
    lines.append("## Stats")
    lines.append("")
    lines.append("- **Total articles:** %d" % len(articles))
    dates = [a.get("date", "") for a in articles if a.get("date", "Unknown") != "Unknown"]
    if dates:
        dates.sort()
        lines.append("- **Date range:** %s → %s" % (dates[0], dates[-1]))
    lines.append("- **Categories:** %d" % len(cat_counts))
    lines.append("")
    
    # Write index
    index_path = os.path.join(POSTS_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("Index built: %d articles across %d categories" % (len(articles), len(cat_counts)))
    print("Saved to %s" % index_path)
    
    # Print directory tree
    print("\nDirectory structure:")
    for cat in sorted(os.listdir(POSTS_DIR)):
        cat_path = os.path.join(POSTS_DIR, cat)
        if os.path.isdir(cat_path):
            count = len([f for f in os.listdir(cat_path) if f.endswith(".md")])
            name = CATEGORY_NAMES.get(cat, cat)
            print("  %-20s %3d articles" % (name, count))
    
    total = sum(
        len([f for f in os.listdir(os.path.join(POSTS_DIR, d)) if f.endswith(".md")])
        for d in os.listdir(POSTS_DIR) if os.path.isdir(os.path.join(POSTS_DIR, d))
    )
    print("  %-20s %3d articles" % ("TOTAL", total))

if __name__ == "__main__":
    main()
