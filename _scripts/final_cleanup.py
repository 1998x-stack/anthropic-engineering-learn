#!/usr/bin/env python3
"""Clean, reclassify, and rebuild indexes for all blog articles."""
import os
import re
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

# Classification rules
CATS = {
    "e2b": [
        ("case-studies", ["case-study", "interview", "conversation", "about-building-tools", "about-deployment", "about-e2b", "about-cognosys"]),
        ("integrations", ["with-", "integration", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "mcp", "docker-e2b"]),
        ("announcements", ["announcement", "launch", "introducing", "release", "funding", "series", "seed", "postmortem"]),
        ("ai-agents", ["agent", "agentic", "autogpt", "computer-use", "multi-agent", "ai-agent", "swe-", "sweep", "codium", "code-review"]),
        ("tutorials", ["how-to", "tutorial", "setup", "get-started", "building", "creating", "guide", "step-by-step"]),
        ("sandbox-code-execution", ["sandbox", "code-interpreter", "code-execution", "compute", "execution", "container"]),
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
    """Clean markdown content, remove nav noise."""
    lines = content.split('\n')
    cleaned = []
    
    for line in lines:
        s = line.strip()
        # Skip obvious noise
        if not s:
            if cleaned and cleaned[-1] != '':
                cleaned.append('')
            continue
        if s in ['-', '*']:
            continue
        if any(x in s.lower() for x in [
            'case study', 'learn more →', 'we raised', 'all posts', 'follow @',
            "we're hiring", 'hundreds of millions', 'we\'re always excited',
            'check open positions', '[back]', '← back', 'share',
            'min read', 'read time:', '•', 'min\n',
        ]):
            continue
        # Skip lines that are just empty links or images
        if s.startswith('![]()') or s.startswith('[]('):
            continue
        if re.match(r'^\*+$', s):
            continue
        # Skip very short non-heading lines that look like nav
        if len(s) < 15 and not s.startswith('#'):
            # Check if it's a nav item
            if any(x in s for x in ['→', '←', 'home', 'blog', 'docs']):
                continue
        cleaned.append(line)
    
    # Join and clean
    result = '\n'.join(cleaned)
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip()
    
    # Find first real content
    lines = result.split('\n')
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if len(s) > 15:
            # Skip if it looks like nav
            if not any(x in s.lower() for x in ['case study', 'learn more', 'we raised', 'all posts', 'follow @']):
                start = i
                break
    result = '\n'.join(lines[start:])
    
    return result.strip()

def try_extract_date_from_content(content):
    """Try to extract date from content text."""
    # Look for patterns like "January 15, 2025" or "Jan 15, 2025"
    m = re.search(r'((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4})', content[:2000])
    if m:
        try:
            return datetime.strptime(m.group(1).replace(",", ""), "%B %d %Y").strftime("%Y-%m-%d")
        except:
            pass
    m = re.search(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},?\s+\d{4})', content[:2000])
    if m:
        try:
            return datetime.strptime(m.group(1).replace(",", ""), "%b %d %Y").strftime("%Y-%m-%d")
        except:
            pass
    # Try ISO date
    m = re.search(r'(\d{4}-\d{2}-\d{2})', content[:2000])
    if m:
        return m.group(1)
    return None

def try_extract_author_from_content(content):
    """Try to extract author from content."""
    # "By Name" patterns
    m = re.search(r'By\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)', content[:3000])
    if m:
        return m.group(1)
    # Twitter handles
    m = re.search(r'@([a-zA-Z0-9_]+)', content[:3000])
    if m:
        return m.group(1)
    return None

def main():
    for site in ["e2b", "browserbase", "modal"]:
        posts_dir = os.path.join(BASE, site, "posts")
        url_prefix = {
            "e2b": "https://e2b.dev/blog/",
            "browserbase": "https://www.browserbase.com/blog/",
            "modal": "https://modal.com/blog/",
        }[site]
        
        if not os.path.exists(posts_dir):
            continue
        
        print("\n=== %s ===" % site)
        articles = []
        reclassified = 0
        cleaned = 0
        
        # Collect all files
        files_to_process = []
        for root, dirs, files in os.walk(posts_dir):
            for f in files:
                if f.endswith(".md") and f != "index.md":
                    files_to_process.append(os.path.join(root, f))
        
        for filepath in files_to_process:
            filename = os.path.basename(filepath)
            slug = filename.replace(".md", "")
            old_cat = os.path.basename(os.path.dirname(filepath))
            
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            
            # Parse frontmatter
            fm = re.match(r'^---\n(.*?)\n---\n\n', content, re.DOTALL)
            if not fm:
                continue
            
            fm_text = fm.group(1)
            body = content[fm.end():]
            
            # Extract metadata
            title_m = re.search(r'title:\s*"([^"]*)"', fm_text)
            date_m = re.search(r'date:\s*"([^"]*)"', fm_text)
            author_m = re.search(r'author:\s*"([^"]*)"', fm_text)
            url_m = re.search(r'url:\s*"([^"]*)"', fm_text)
            
            title = title_m.group(1) if title_m else slug
            date = date_m.group(1) if date_m else "Unknown"
            author = author_m.group(1) if author_m else "Unknown"
            url = url_m.group(1) if url_m else url_prefix + slug
            
            # Try to extract date from content if unknown
            if date == "Unknown":
                extracted_date = try_extract_date_from_content(body)
                if extracted_date:
                    date = extracted_date
            
            # Try to extract author from content if unknown
            if author == "Unknown":
                extracted_author = try_extract_author_from_content(body)
                if extracted_author:
                    author = extracted_author
            
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
            
            # Move to correct category if changed
            if new_cat != old_cat:
                new_dir = os.path.join(posts_dir, new_cat)
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, filename)
                with open(new_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                os.remove(filepath)
                reclassified += 1
                old_cat = new_cat
            
            if new_body != body:
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
        
        print("  %d articles, %d reclassified, %d cleaned" % (len(articles), reclassified, cleaned))
        
        # Build index
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
    
    print("  Index saved")

if __name__ == "__main__":
    main()
