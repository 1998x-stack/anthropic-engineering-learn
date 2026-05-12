#!/usr/bin/env python3
"""Reorganize and reclassify E2B/Browserbase/Modal articles, build indexes."""
import os
import re
import shutil

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")

# E2B classification
E2B_CATS = {
    "sandbox-code-execution": ["sandbox", "code-interpreter", "code-execution", "docker-e2b", "compute", "execution"],
    "ai-agents": ["agent", "agentic", "autogpt", "computer-use", "multi-agent", "ai-agent"],
    "integrations": ["with-", "integration", "x-e2b", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "v0", "mcp"],
    "tutorials": ["how-to", "tutorial", "build", "building", "creating", "guide", "step-by-step", "setup"],
    "announcements": ["announcement", "launch", "introducing", "release", "funding", "series", "seed", "postmortem"],
    "case-studies": ["case-study", "interview", "conversation", "about-", "ceo", "founder", "crivent", "sully"],
}

def classify_e2b(slug, content=""):
    text = (slug + " " + content[:1000]).lower().replace("-", " ")
    for cat, patterns in E2B_CATS.items():
        for p in patterns:
            if p in text:
                return cat
    return "general"

def main():
    sites = {
        "e2b": {
            "base": os.path.join(BASE, "e2b"),
            "url_prefix": "https://e2b.dev/blog/",
            "cat_names": {
                "sandbox-code-execution": "Sandbox & Code Execution",
                "ai-agents": "AI Agents",
                "integrations": "Integrations",
                "tutorials": "Tutorials",
                "announcements": "Announcements",
                "case-studies": "Case Studies & Interviews",
                "general": "General",
            },
            "classify": classify_e2b,
        },
        "browserbase": {
            "base": os.path.join(BASE, "browserbase"),
            "url_prefix": "https://www.browserbase.com/blog/",
            "cat_names": {
                "stagehand": "Stagehand",
                "tutorials": "Tutorials",
                "announcements": "Announcements",
                "engineering": "Engineering",
                "case-studies": "Case Studies",
                "general": "General",
            },
        },
        "modal": {
            "base": os.path.join(BASE, "modal"),
            "url_prefix": "https://modal.com/blog/",
            "cat_names": {
                "inference": "Inference",
                "training-finetuning": "Training & Fine-tuning",
                "sandboxes": "Sandboxes",
                "engineering": "Engineering",
                "announcements": "Announcements",
                "tutorials": "Tutorials",
                "case-studies": "Case Studies",
                "general": "General",
            },
        },
    }

    for site_name, site_info in sites.items():
        old_base = os.path.join(BASE, site_name)  # e.g. external/blog/posts/e2b
        new_base = site_info["base"]  # e.g. external/blog/e2b
        cat_names = site_info["cat_names"]
        
        if not os.path.exists(old_base):
            print("%s: old dir not found, skipping" % site_name)
            continue
        
        articles = []
        moved_count = 0
        
        # Get all .md files from old category dirs
        old_cats = [d for d in os.listdir(old_base) if os.path.isdir(os.path.join(old_base, d))]
        for old_cat in old_cats:
            old_cat_dir = os.path.join(old_base, old_cat)
            for filename in os.listdir(old_cat_dir):
                if not filename.endswith(".md"):
                    continue
                old_path = os.path.join(old_cat_dir, filename)
                
                # Read content
                try:
                    with open(old_path, encoding="utf-8") as f:
                        content = f.read()
                except:
                    continue
                
                # Extract metadata
                title_m = re.search(r'title:\s*"([^"]*)"', content)
                date_m = re.search(r'date:\s*"([^"]*)"', content)
                author_m = re.search(r'author:\s*"([^"]*)"', content)
                url_m = re.search(r'url:\s*"([^"]*)"', content)
                
                slug = filename.replace(".md", "")
                title = title_m.group(1) if title_m else slug
                date = date_m.group(1) if date_m else "Unknown"
                author = author_m.group(1) if author_m else "Unknown"
                url = url_m.group(1) if url_m else site_info["url_prefix"] + slug
                
                # Reclassify E2B
                if site_name == "e2b":
                    category = classify_e2b(slug, content)
                else:
                    category = old_cat  # Keep existing
                
                # Create new category dir
                new_cat_dir = os.path.join(new_base, "posts", category)
                os.makedirs(new_cat_dir, exist_ok=True)
                
                # Update content with new category
                if site_name == "e2b":
                    new_content = re.sub(r'category:\s*"[^"]*"', 'category: "%s"' % category, content)
                    new_content = re.sub(r'site:\s*"[^"]*"', 'site: "%s"' % site_name, new_content)
                else:
                    new_content = content
                
                new_path = os.path.join(new_cat_dir, filename)
                with open(new_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                moved_count += 1
                articles.append({
                    "slug": slug, "title": title, "date": date,
                    "author": author, "url": url, "category": category,
                })
        
        # Clean up old dirs
        for old_cat in old_cats:
            old_cat_dir = os.path.join(old_base, old_cat)
            if os.path.isdir(old_cat_dir):
                shutil.rmtree(old_cat_dir)
        
        print("%s: %d articles reorganized" % (site_name, moved_count))
        
        # Build index
        build_index(site_name, articles, new_base, cat_names)
    
    # Clean up old empty dirs
    if os.path.exists(os.path.join(BASE, "e2b")) and not os.listdir(os.path.join(BASE, "e2b")):
        os.rmdir(os.path.join(BASE, "e2b"))
    if os.path.exists(os.path.join(BASE, "browserbase")) and not os.listdir(os.path.join(BASE, "browserbase")):
        os.rmdir(os.path.join(BASE, "browserbase"))
    if os.path.exists(os.path.join(BASE, "modal")) and not os.listdir(os.path.join(BASE, "modal")):
        os.rmdir(os.path.join(BASE, "modal"))

def build_index(site_name, articles, base, cat_names):
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
    
    # File structure
    file_tree_lines = []
    for cat in sorted(cat_names.keys()):
        file_tree_lines.append("├── %s/" % cat)
    
    lines = [
        "# %s Blog Index" % site_name.title(),
        "",
        "> Source: https://%s.com/blog" % (site_name if site_name != "browserbase" else "www.browserbase.com"),
        "> Archived: 2026-05-11",
        "> Total: %d articles" % len(articles),
        "",
        "## File Structure",
        "",
        "```",
        "external/blog/%s/posts/" % site_name,
    ]
    for i, line in enumerate(file_tree_lines):
        prefix = "└── " if i == len(file_tree_lines) - 1 else "├── "
        lines.append("%s%s" % (prefix, line.replace("├── ", "")))
    lines.append("└── index.md")
    lines.append("```")
    lines.append("")
    
    # Category summary
    lines.append("## Category Summary")
    lines.append("")
    lines.append("| Category | Articles |")
    lines.append("| --- | --- |")
    
    cat_counts = {}
    for a in articles:
        cat = a["category"]
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        name = cat_names.get(cat, cat)
        lines.append("| [%s](#%s) | %d |" % (name, cat.replace(" ", "-"), cat_counts[cat]))
    lines.append("")
    
    # Articles by category
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
    
    # Stats
    lines.append("---\n\n## Stats\n")
    lines.append("- **Total articles:** %d" % len(articles))
    dates = [a["date"] for a in articles if a["date"] != "Unknown"]
    if dates:
        dates.sort()
        lines.append("- **Date range:** %s → %s" % (dates[0], dates[-1]))
    lines.append("- **Categories:** %d" % len(cat_counts))
    lines.append("")
    
    index_path = os.path.join(base, "posts", "index.md")
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("  Index: %d articles across %d categories" % (len(articles), len(cat_counts)))
    print("  Saved to %s" % index_path)
    
    # Print directory structure
    posts_dir = os.path.join(base, "posts")
    print("  Directory:")
    for cat in sorted(os.listdir(posts_dir)):
        cp = os.path.join(posts_dir, cat)
        if os.path.isdir(cp):
            cnt = len([f for f in os.listdir(cp) if f.endswith(".md")])
            print("    %-30s %3d articles" % (cat_names.get(cat, cat), cnt))

if __name__ == "__main__":
    main()
