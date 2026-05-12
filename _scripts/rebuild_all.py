#!/usr/bin/env python3
"""Re-fetch all articles using web_fetch-style approach and rebuild markdowns."""
import os
import re
import subprocess
import json

BASE = os.path.dirname(os.path.abspath(__file__))

def get_all_slugs(site):
    """Get all article slugs for a site."""
    if site == "e2b":
        url = "https://e2b.dev/blog"
        prefix = "https://e2b.dev/blog/"
    elif site == "browserbase":
        url = "https://www.browserbase.com/blog"
        prefix = "https://www.browserbase.com/blog/"
    else:
        url = "https://modal.com/blog"
        prefix = "https://modal.com/blog/"
    
    # Use curl to get page and extract links
    html = fetch_page(url)
    if not html:
        return []
    
    slugs = []
    for m in re.finditer(r'href="(/blog/([a-zA-Z0-9_-]+))"', html):
        slug = m.group(2)
        if slug and len(slug) > 3:
            slugs.append(slug)
    
    return sorted(set(slugs))

def fetch_page(url):
    try:
        r = subprocess.run(
            ["curl", "-sL", "-m", "30",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        return r.stdout if r.returncode == 0 and len(r.stdout) > 100 else None
    except:
        return None

def extract_article(html, site, slug):
    """Extract article from HTML."""
    if site == "e2b":
        url = "https://e2b.dev/blog/" + slug
    elif site == "browserbase":
        url = "https://www.browserbase.com/blog/" + slug
    else:
        url = "https://modal.com/blog/" + slug
    
    # Title
    title_m = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = title_m.group(1).strip() if title_m else slug
    for suffix in [" - E2B", " | E2B", " | Browserbase", " | Modal", " - Modal"]:
        title = title.replace(suffix, "").strip()
    
    # Date
    date = None
    for p in [r'"datePublished"\s*:\s*"([^"]+)"',
              r'article:published_time"\s+content="([^"]+)"',
              r'<time[^>]*datetime="([^"]+)"',
              r'"dateModified"\s*:\s*"([^"]+)"']:
        m = re.search(p, html)
        if m:
            date = m.group(1)[:10]
            break
    if not date:
        m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})', html)
        if m:
            from datetime import datetime
            try:
                date = datetime.strptime(m.group(0), "%B %d, %Y").strftime("%Y-%m-%d")
            except:
                pass
    
    # Author
    author = None
    m = re.search(r'"author"\s*:\s*\[(.*?)\]', html, re.DOTALL)
    if m:
        names = re.findall(r'"name"\s*:\s*"([^"]+)"', m.group(1))
        if names:
            author = ", ".join(names)
    if not author:
        m = re.search(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"([^"]+)"', html)
        if m:
            author = m.group(1)
    if not author:
        m = re.search(r'<meta[^>]*name=["\']author["\'][^>]*content=["\']([^"\']+)["\']', html)
        if not m:
            m = re.search(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*name=["\']author["\']', html)
        if m:
            author = m.group(1).strip()
    # Try bylines in content
    if not author:
        m = re.search(r'By\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)', html)
        if m:
            author = m.group(1)
    
    # Body extraction
    article_m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    body = article_m.group(1) if article_m else html
    
    # Remove noise
    body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<aside[^>]*>.*?</aside>', '', body, flags=re.DOTALL | re.IGNORECASE)
    
    # HTML to markdown
    md = body
    for pat, repl in [
        (r'<h1[^>]*>(.*?)</h1>', r'\n\n# \1\n\n'),
        (r'<h2[^>]*>(.*?)</h2>', r'\n\n## \1\n\n'),
        (r'<h3[^>]*>(.*?)</h3>', r'\n\n### \1\n\n'),
        (r'<h4[^>]*>(.*?)</h4>', r'\n\n#### \1\n\n'),
        (r'<strong[^>]*>(.*?)</strong>', r'**\1**'),
        (r'<b[^>]*>(.*?)</b>', r'**\1**'),
        (r'<em[^>]*>(.*?)</em>', r'*\1*'),
        (r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)'),
        (r'<img[^>]*src="([^"]*)"[^>]*(?:alt="([^"]*)")?[^>]*/?>', r'![\2](\1)'),
        (r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n'),
        (r'<code[^>]*>(.*?)</code>', r'`\1`'),
        (r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n'),
        (r'<br\s*/?>', '\n'),
        (r'<li[^>]*>(.*?)</li>', r'- \1\n'),
        (r'</?[uo]l[^>]*>', '\n'),
        (r'<blockquote[^>]*>(.*?)</blockquote>', r'\n\n> \1\n\n'),
        (r'<hr[^>]*/?>', '\n\n---\n\n'),
        (r'<[^>]+>', ''),
    ]:
        md = re.sub(pat, repl, md, flags=re.DOTALL | re.IGNORECASE)
    
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = md.strip()
    
    # Find actual content start (skip nav noise)
    lines = md.split('\n')
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if len(s) > 30 and not any(x in s.lower() for x in ['case study', 'learn more', 'we raised', 'all posts']):
            start = i
            break
    md = '\n'.join(lines[start:])
    
    if len(md) > 50000:
        md = md[:50000] + "\n\n---\n*Content truncated.*"
    
    return {
        "slug": slug,
        "title": title,
        "date": date or "Unknown",
        "author": author or "Unknown",
        "url": url,
        "content": md,
    }

def classify(site, slug, content=""):
    text = (slug + " " + content[:1000]).lower().replace("-", " ")
    cats = {
        "e2b": [
            ("case-studies", ["case-study", "interview", "conversation", "about-", "ceo", "founder"]),
            ("integrations", ["with-", "integration", "langchain", "openai", "anthropic", "groq", "replit", "cursor", "mcp", "docker-e2b", "v0"]),
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
    }.get(site, [])
    
    for cat, patterns in cats:
        for p in patterns:
            if p in text:
                return cat
    return "general"

def save_article(site, article):
    """Save article and return its category."""
    posts_dir = os.path.join(BASE, site, "posts")
    category = classify(site, article["slug"], article["content"])
    
    cat_dir = os.path.join(posts_dir, category)
    os.makedirs(cat_dir, exist_ok=True)
    
    filepath = os.path.join(cat_dir, article["slug"] + ".md")
    
    title_esc = article["title"].replace('"', '\\"')
    author_esc = article["author"].replace('"', '\\"')
    
    frontmatter = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
        title_esc, author_esc, article["date"], article["url"], category, site
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + article["content"])
    
    return category

def main():
    import sys
    site = sys.argv[1] if len(sys.argv) > 1 else None
    start_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end_idx = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    sites_to_process = [site] if site else ["e2b", "browserbase", "modal"]
    
    for s in sites_to_process:
        slugs = get_all_slugs(s)
        if not slugs:
            print("%s: no slugs found" % s)
            continue
        
        if end_idx is None:
            end_idx = len(slugs)
        
        batch = slugs[start_idx:end_idx]
        print("\n=== %s: processing %d-%d of %d ===" % (s, start_idx, end_idx, len(slugs)))
        
        saved = 0
        failed = 0
        for i, slug in enumerate(batch):
            url = {"e2b": "https://e2b.dev/blog/", "browserbase": "https://www.browserbase.com/blog/", "modal": "https://modal.com/blog/"}[s] + slug
            
            html = fetch_page(url)
            if not html:
                failed += 1
                print("  [%d/%d] FAIL %s" % (i+1, len(batch), slug))
                continue
            
            article = extract_article(html, s, slug)
            cat = save_article(s, article)
            saved += 1
            print("  [%d/%d] SAVE %s (%s, %d chars, %s)" % (
                i+1, len(batch), slug, article["date"], len(article["content"]), cat))
        
        print("  %d saved, %d failed" % (saved, failed))

if __name__ == "__main__":
    main()
