#!/usr/bin/env python3
"""Deduplicate, clean, classify, and rebuild indexes for all blog articles."""
import os
import re
from collections import defaultdict
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

# Classification
CATS = {
    "e2b": [
        ("case-studies", ["case-study", "interview", "conversation", "about-building-tools", "about-deployment", "about-e2b", "about-cognosys", "ceo", "founder"]),
        ("integrations", ["with-", "integration", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "mcp", "docker-e2b"]),
        ("announcements", ["announcement", "launch", "introducing", "release", "funding", "series", "seed", "postmortem"]),
        ("ai-agents", ["agent", "agentic", "autogpt", "computer-use", "multi-agent", "ai-agent", "swe-", "sweep", "codium", "code-review", "reacteval"]),
        ("tutorials", ["how-to", "tutorial", "setup", "get-started", "building", "creating", "guide", "step-by-step"]),
        ("sandbox-code-execution", ["sandbox", "code-interpreter", "code-execution", "compute", "execution", "container", "firecracker"]),
    ],
    "browserbase": [
        ("stagehand", ["stagehand"]),
        ("announcements", ["announcement", "launch", "introducing", "release", "autobrowse", "multi-region"]),
        ("tutorials", ["tutorial", "how-to", "building", "guide", "best-", "1password"]),
        ("case-studies", ["case-study", "amplitude"]),
    ],
    "modal": [
        ("inference", ["inference", "llm", "transformer", "gpu", "vllm", "tensorrt", "triton", "serve", "model", "token"]),
        ("training-finetuning", ["train", "finetune", "fine-tune", "lora", "sft", "checkpoint"]),
        ("sandboxes", ["sandbox", "firecracker", "microvm", "micro-vm", "cold-start"]),
        ("announcements", ["announcing", "series-b", "funding", "joins-modal", "joining-modal"]),
        ("engineering", ["cuda", "pytorch", "compil", "benchmark", "performance", "optim", "profile"]),
        ("tutorials", ["tutorial", "guide", "how-to", "building"]),
        ("case-studies", ["case-study", "zencastr", "tidbyt", "decagon", "runway", "doppel"]),
    ],
}

def classify(site, slug, content=""):
    text = (slug + " " + content[:1000]).lower().replace("-", " ")
    for cat, patterns in CATS.get(site, []):
        for p in patterns:
            if p in text:
                return cat
    return "general"

def clean_content(content):
    """Clean markdown content."""
    lines = content.split('\n')
    cleaned = []
    for line in lines:
        s = line.strip()
        if not s:
            if cleaned and cleaned[-1] != '':
                cleaned.append('')
            continue
        # Skip noise
        if any(x in s.lower() for x in [
            'case study', 'learn more →', 'we raised', 'all posts', 'follow @',
            "we're hiring", 'hundreds of millions', 'we\'re always excited',
            'check open positions', '[back]', '← back', 'share',
            'min read', 'read time:', 'min\n',
        ]):
            continue
        if s.startswith('![]()') or s.startswith('[]('):
            continue
        if re.match(r'^\*+$', s):
            continue
        if len(s) < 15 and not s.startswith('#'):
            if any(x in s for x in ['→', '←', 'home', 'blog', 'docs']):
                continue
        cleaned.append(line)
    
    result = '\n'.join(cleaned)
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip()
    
    # Find first real content
    lines = result.split('\n')
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if len(s) > 15 and not any(x in s.lower() for x in ['case study', 'learn more', 'we raised', 'all posts', 'follow @']):
            start = i
            break
    return '\n'.join(lines[start:]).strip()

def main():
    for site in ["e2b", "browserbase", "modal"]:
        posts_dir = os.path.join(BASE, site, "posts")
        if not os.path.exists(posts_dir):
            continue
        
        print("\n=== %s ===" % site)
        url_prefix = {"e2b": "https://e2b.dev/blog/", "browserbase": "https://www.browserbase.com/blog/", "modal": "https://modal.com/blog/"}[site]
        
        # Step 1: Collect all files and deduplicate by slug
        all_files = {}
        for root, dirs, files in os.walk(posts_dir):
            for f in files:
                if f.endswith(".md") and f != "index.md":
                    slug = f.replace(".md", "")
                    filepath = os.path.join(root, f)
                    size = os.path.getsize(filepath)
                    if slug not in all_files or size > all_files[slug][1]:
                        all_files[slug] = (filepath, size)
                    elif filepath != all_files[slug][0]:
                        print("  Removing duplicate: %s (%d bytes, keeping %d bytes)" % (filepath, size, all_files[slug][1]))
                        os.remove(filepath)
        
        # Step 2: Process each unique file
        articles = []
        reclassified = 0
        cleaned = 0
        
        for slug, (filepath, _) in all_files.items():
            old_cat = os.path.basename(os.path.dirname(filepath))
            
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            
            # Parse frontmatter
            fm = re.match(r'^---\n(.*?)\n---\n\n', content, re.DOTALL)
            if not fm:
                continue
            
            fm_text = fm.group(1)
            body = content[fm.end():]
            
            title_m = re.search(r'title:\s*"([^"]*)"', fm_text)
            date_m = re.search(r'date:\s*"([^"]*)"', fm_text)
            author_m = re.search(r'author:\s*"([^"]*)"', fm_text)
            url_m = re.search(r'url:\s*"([^"]*)"', fm_text)
            
            title = title_m.group(1) if title_m else slug
            date = date_m.group(1) if date_m else "Unknown"
            author = author_m.group(1) if author_m else "Unknown"
            url = url_m.group(1) if url_m else url_prefix + slug
            
            # Clean content
            new_body = clean_content(body)
            
            # Classify
            new_cat = classify(site, slug, new_body)
            
            # Update frontmatter
            te = title.replace('"', '\\"')
            ae = author.replace('"', '\\"')
            new_fm = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
                te, ae, date, url, new_cat, site
            )
            
            new_content = new_fm + new_body
            
            # Move to correct category
            if new_cat != old_cat:
                new_dir = os.path.join(posts_dir, new_cat)
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, slug + ".md")
                with open(new_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                os.remove(filepath)
                reclassified += 1
                old_cat = new_cat
            elif new_body != body:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                cleaned += 1
            
            articles.append({
                "slug": slug, "title": title, "date": date,
                "author": author, "url": url, "category": old_cat,
            })
        
        # Remove empty dirs
        for d in os.listdir(posts_dir):
            dp = os.path.join(posts_dir, d)
            if os.path.isdir(dp) and not os.listdir(dp):
                os.rmdir(dp)
        
        print("  %d unique articles, %d reclassified, %d cleaned" % (len(articles), reclassified, cleaned))
        
        # Step 3: Build index
        build_index(site, articles, posts_dir, url_prefix)

def build_index(site, articles, posts_dir, url_prefix):
    articles.sort(key=lambda x: x["date"], reverse=True)
    
    cat_years = {}
    cat_names = {}
    for a in articles:
        cat = a["category"]
        cat_names[cat] = cat.replace("-", " ").title()
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
    
    unknown_dates = len([a for a in articles if a["date"] == "Unknown"])
    if unknown_dates:
        lines.append("- **Articles with unknown date:** %d" % unknown_dates)
    lines.append("")
    
    with open(os.path.join(posts_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("  Index: %d articles across %d categories" % (len(articles), len(cat_counts)))
    for cat in sorted(cat_counts.keys(), key=lambda x: cat_counts[x], reverse=True):
        print("    %-25s %3d" % (cat_names.get(cat, cat), cat_counts[cat]))

if __name__ == "__main__":
    main()
