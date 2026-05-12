#!/usr/bin/env python3
"""Enhance existing markdown files: clean content, fix frontmatter, rebuild indexes."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# Classification rules
CATEGORIES = {
    "e2b": [
        ("case-studies", ["case-study", "interview", "conversation", "about-building-tools", "about-deployment", "about-e2b"]),
        ("integrations", ["with-", "integration", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "mcp", "docker-e2b"]),
        ("announcements", ["announcement", "launch", "introducing", "release", "funding", "series", "seed", "postmortem"]),
        ("ai-agents", ["agent", "agentic", "autogpt", "computer-use", "multi-agent", "ai-agent", "swe", "sweep", "codium"]),
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
    for cat, patterns in CATEGORIES.get(site, []):
        for p in patterns:
            if p in text:
                return cat
    return "general"

def clean_content(content):
    """Clean up markdown content."""
    lines = content.split('\n')
    
    # Remove lines that are just navigation noise
    noise_patterns = [
        r'^-?$',
        r'^\s*$',
        r'^CASE.*?STUDY.*?LEARN MORE',
        r'^\*\*.*?We raised.*?\*\*',
        r'^\*\*.*?Learn what.*?\*\*',
        r'^\s*Follow @',
        r'^\s*We\'re hiring',
        r'^\s*Hundreds of millions',
        r'^\s*All posts',
        r'^\s*\[Back\]',
        r'^\s*Read time:',
        r'^\s*min read',
        r'^\s*min$',
        r'^\s*By [A-Z]',  # Keep author bylines for now
    ]
    
    cleaned = []
    skip_mode = False
    for line in lines:
        stripped = line.strip()
        
        # Skip very short lines that are likely noise (but keep headings and list items)
        if len(stripped) < 3 and stripped not in ['', '-']:
            continue
        
        # Skip obvious nav/CTA patterns
        if any(re.search(p, stripped, re.IGNORECASE) for p in noise_patterns):
            continue
        
        # Skip lines that are just URL-like without content
        if stripped.startswith('![]()') and len(stripped) < 20:
            continue
        
        # Skip lines that are just asterisks
        if stripped.strip('* ') == '':
            continue
        
        cleaned.append(line)
    
    # Join and clean up excessive newlines
    result = '\n'.join(cleaned)
    result = re.sub(r'\n{3,}', '\n\n', result)
    result = result.strip()
    
    # Find first meaningful content line
    # Remove leading empty image tags and short noise
    while result:
        first_line = result.split('\n')[0].strip()
        if not first_line or first_line.startswith('![]()') or len(first_line) < 5:
            result = '\n'.join(result.split('\n')[1:])
        else:
            break
    
    return result

def build_index(site, url_prefix):
    """Build index for a site."""
    posts_dir = os.path.join(BASE, site, "posts")
    if not os.path.exists(posts_dir):
        return
    
    articles = []
    cat_names = {}
    
    for cat_dir in os.listdir(posts_dir):
        cat_path = os.path.join(posts_dir, cat_dir)
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
    
    with open(os.path.join(posts_dir, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    for site, url_prefix in [
        ("e2b", "https://e2b.dev/blog/"),
        ("browserbase", "https://www.browserbase.com/blog/"),
        ("modal", "https://modal.com/blog/")
    ]:
        posts_dir = os.path.join(BASE, site, "posts")
        if not os.path.exists(posts_dir):
            continue
        
        print("\n=== %s ===" % site)
        articles = []
        reclassified = 0
        cleaned = 0
        
        # Process all files
        for cat_dir in list(os.listdir(posts_dir)):
            cat_path = os.path.join(posts_dir, cat_dir)
            if not os.path.isdir(cat_path):
                continue
            
            for filename in os.listdir(cat_path):
                if not filename.endswith(".md"):
                    continue
                filepath = os.path.join(cat_path, filename)
                
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
                
                slug = filename.replace(".md", "")
                title = title_m.group(1) if title_m else slug
                date = date_m.group(1) if date_m else "Unknown"
                author = author_m.group(1) if author_m else "Unknown"
                url = url_m.group(1) if url_m else url_prefix + slug
                
                # Classify
                new_cat = classify(site, slug, body)
                
                # Clean content
                new_body = clean_content(body)
                
                # Move to correct category if changed
                if new_cat != cat_dir:
                    new_dir = os.path.join(posts_dir, new_cat)
                    os.makedirs(new_dir, exist_ok=True)
                    new_path = os.path.join(new_dir, filename)
                    
                    # Write with updated frontmatter
                    title_esc = title.replace('"', '\\"')
                    author_esc = author.replace('"', '\\"')
                    new_fm = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
                        title_esc, author_esc, date, url, new_cat, site
                    )
                    with open(new_path, "w", encoding="utf-8") as f:
                        f.write(new_fm + new_body)
                    os.remove(filepath)
                    reclassified += 1
                    
                    if len(new_body) < len(body):
                        cleaned += 1
                    
                    articles.append({"slug": slug, "title": title, "date": date, "author": author, "url": url, "category": new_cat})
                else:
                    # Just clean content and ensure frontmatter has site
                    if new_body != body:
                        title_esc = title.replace('"', '\\"')
                        author_esc = author.replace('"', '\\"')
                        new_fm = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
                            title_esc, author_esc, date, url, cat_dir, site
                        )
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(new_fm + new_body)
                        cleaned += 1
                    
                    articles.append({"slug": slug, "title": title, "date": date, "author": author, "url": url, "category": cat_dir})
        
        # Remove empty dirs
        for d in os.listdir(posts_dir):
            dp = os.path.join(posts_dir, d)
            if os.path.isdir(dp) and not os.listdir(dp):
                os.rmdir(dp)
        
        print("  %d articles, %d reclassified, %d cleaned" % (len(articles), reclassified, cleaned))
        
        # Build index
        build_index(site, url_prefix)
        
        # Print distribution
        cat_counts = {}
        for a in articles:
            cat_counts[a["category"]] = cat_counts.get(a["category"], 0) + 1
        for cat, cnt in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
            print("  %-25s %3d" % (cat, cnt))

if __name__ == "__main__":
    main()
