#!/usr/bin/env python3
"""Reclassify E2B articles, fix directory structure, build indexes."""
import os
import re
import shutil

def classify_e2b(slug, content=""):
    text = (slug + " " + content[:500]).lower().replace("-", " ")
    cats = [
        ("case-studies", ["case-study", "interview", "conversation", "about-building-tools", "about-deployment"]),
        ("integrations", ["with-", "integration", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "mcp", "docker-e2b"]),
        ("announcements", ["announcement", "launch", "introducing", "release", "funding", "series", "seed", "postmortem"]),
        ("ai-agents", ["agent", "agentic", "autogpt", "computer-use", "multi-agent", "ai-agent", "swe", "sweep", "codium", "code-review"]),
        ("tutorials", ["how-to", "tutorial", "setup", "get-started", "building", "creating", "guide", "step-by-step"]),
        ("sandbox-code-execution", ["sandbox", "code-interpreter", "code-execution", "compute", "execution", "container", "docker"]),
    ]
    for cat, patterns in cats:
        for p in patterns:
            if p in text:
                return cat
    return "general"

def main():
    # Fix directory structure
    for site in ["e2b", "browserbase", "modal"]:
        old = os.path.join("posts", site, "posts")
        new = os.path.join(site, "posts")
        if os.path.exists(old):
            if os.path.exists(new):
                shutil.rmtree(new)
            os.makedirs(os.path.dirname(new), exist_ok=True)
            shutil.move(old, new)
            old_parent = os.path.dirname(old)
            if os.path.isdir(old_parent) and not os.listdir(old_parent):
                os.rmdir(old_parent)
    
    # Reclassify E2B
    e2b_dir = os.path.join("e2b", "posts")
    articles = []
    for cat_dir in os.listdir(e2b_dir):
        cat_path = os.path.join(e2b_dir, cat_dir)
        if not os.path.isdir(cat_path):
            continue
        for filename in os.listdir(cat_path):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(cat_path, filename)
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            
            slug = filename.replace(".md", "")
            new_cat = classify_e2b(slug, content)
            
            if new_cat != cat_dir:
                new_dir = os.path.join(e2b_dir, new_cat)
                os.makedirs(new_dir, exist_ok=True)
                new_content = re.sub(r'category:\s*"[^"]*"', 'category: "%s"' % new_cat, content)
                with open(os.path.join(new_dir, filename), "w", encoding="utf-8") as f:
                    f.write(new_content)
                os.remove(filepath)
            
            title_m = re.search(r'title:\s*"([^"]*)"', content)
            date_m = re.search(r'date:\s*"([^"]*)"', content)
            url_m = re.search(r'url:\s*"([^"]*)"', content)
            articles.append({
                "slug": slug,
                "title": title_m.group(1) if title_m else slug,
                "date": date_m.group(1) if date_m else "Unknown",
                "url": url_m.group(1) if url_m else "https://e2b.dev/blog/" + slug,
                "category": new_cat,
            })
    
    # Remove empty E2B dirs
    for d in os.listdir(e2b_dir):
        dp = os.path.join(e2b_dir, d)
        if os.path.isdir(dp) and not os.listdir(dp):
            os.rmdir(dp)
    
    e2b_counts = {}
    for a in articles:
        e2b_counts[a["category"]] = e2b_counts.get(a["category"], 0) + 1
    print("E2B: %d articles" % len(articles))
    for cat, cnt in sorted(e2b_counts.items(), key=lambda x: x[1], reverse=True):
        print("  %-25s %3d" % (cat, cnt))
    
    # Build all indexes
    for site, url_prefix in [
        ("e2b", "https://e2b.dev/blog/"),
        ("browserbase", "https://www.browserbase.com/blog/"),
        ("modal", "https://modal.com/blog/")
    ]:
        build_index(site, url_prefix)

def build_index(site, url_prefix):
    base = os.path.join(site, "posts")
    if not os.path.exists(base):
        return
    
    articles = []
    cat_names = {}
    for cat_dir in os.listdir(base):
        cat_path = os.path.join(base, cat_dir)
        if not os.path.isdir(cat_path):
            continue
        cat_names[cat_dir] = cat_dir.replace("-", " ").title()
        for filename in os.listdir(cat_path):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(cat_path, filename)
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            
            slug = filename.replace(".md", "")
            title_m = re.search(r'title:\s*"([^"]*)"', content)
            date_m = re.search(r'date:\s*"([^"]*)"', content)
            author_m = re.search(r'author:\s*"([^"]*)"', content)
            url_m = re.search(r'url:\s*"([^"]*)"', content)
            
            articles.append({
                "slug": slug,
                "title": title_m.group(1) if title_m else slug,
                "date": date_m.group(1) if date_m else "Unknown",
                "author": author_m.group(1) if author_m else "Unknown",
                "url": url_m.group(1) if url_m else url_prefix + slug,
                "category": cat_dir,
            })
    
    if not articles:
        return
    
    articles.sort(key=lambda x: x["date"], reverse=True)
    
    cat_years = {}
    for a in articles:
        cat = a["category"]
        year = a["date"][:4] if len(a["date"]) >= 4 else "Unknown"
        if cat not in cat_years:
            cat_years[cat] = {}
        if year not in cat_years[cat]:
            cat_years[cat][year] = []
        cat_years[cat][year].append(a)
    
    lines = [
        "# %s Blog Index" % site.title(),
        "",
        "> Source: %s" % url_prefix.rstrip("/"),
        "> Archived: 2026-05-11",
        "> Total: %d articles" % len(articles),
        "",
        "## Category Summary",
        "",
        "| Category | Articles |",
        "| --- | --- |",
    ]
    
    cat_counts = {}
    for a in articles:
        cat_counts[a["category"]] = cat_counts.get(a["category"], 0) + 1
    
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        name = cat_names.get(cat, cat)
        lines.append("| [%s](#%s) | %d |" % (name, cat.replace(" ", "-"), cat_counts[cat]))
    lines.append("")
    
    for cat in sorted(cat_years.keys()):
        cat_name = cat_names.get(cat, cat)
        lines.append("## %s" % cat_name)
        lines.append("")
        for year in sorted(cat_years[cat].keys(), reverse=True):
            lines.append("### %s" % year)
            lines.append("")
            lines.append("| Date | Title | File |")
            lines.append("| --- | --- | --- |")
            for a in sorted(cat_years[cat][year], key=lambda x: x["date"], reverse=True):
                lines.append("| %s | [%s](%s) | [%s](./%s/%s) |" % (
                    a["date"], a["title"].replace("|", "\\|"), a["url"],
                    a["slug"] + ".md", cat, a["slug"] + ".md"
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
    
    with open(os.path.join(base, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("\n%s: %d articles across %d categories" % (site, len(articles), len(cat_counts)))
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        print("  %-25s %3d" % (cat_names.get(cat, cat), cat_counts[cat]))

if __name__ == "__main__":
    main()
