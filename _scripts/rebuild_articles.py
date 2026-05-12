#!/usr/bin/env python3
"""Fetch blog articles, extract metadata, classify, save as clean markdown."""
import os
import re
import subprocess
import sys
from datetime import datetime

URL_FILE = sys.argv[1]  # Path to slugs file
SITE = sys.argv[2]  # e2b, browserbase, modal
BATCH_START = int(sys.argv[3]) if len(sys.argv) > 3 else 0
BATCH_END = int(sys.argv[4]) if len(sys.argv) > 4 else None

# Site config
SITES = {
    "e2b": {"prefix": "https://e2b.dev/blog/", "base": "e2b/posts"},
    "browserbase": {"prefix": "https://www.browserbase.com/blog/", "base": "browserbase/posts"},
    "modal": {"prefix": "https://modal.com/blog/", "base": "modal/posts"},
}

# Classification
CATEGORIES = {
    "e2b": [
        ("case-studies", ["case-study", "interview", "conversation", "about-", "ceo", "founder"]),
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

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def fetch(url):
    try:
        r = subprocess.run(
            ["curl", "-sL", "-m", "30",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        return r.stdout if r.returncode == 0 and len(r.stdout) > 500 else None
    except:
        return None

def extract(html, slug, site):
    url = SITES[site]["prefix"] + slug
    
    # Title
    tm = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = tm.group(1).strip() if tm else slug
    for sfx in [" - E2B", " | E2B", " | Browserbase", " | Modal", " - Modal"]:
        title = title.replace(sfx, "").strip()
    
    # Date - try structured first
    date = None
    for p in [r'"datePublished"\s*:\s*"([^"]+)"', r'article:published_time"\s+content="([^"]+)"',
              r'<time[^>]*datetime="([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"']:
        m = re.search(p, html)
        if m:
            date = m.group(1)[:10]
            break
    # Try text dates
    if not date:
        m = re.search(r'((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4})', html)
        if m:
            try:
                date = datetime.strptime(m.group(1).replace(",", ""), "%B %d %Y").strftime("%Y-%m-%d")
            except:
                pass
    
    # Author
    author = None
    sm = re.search(r'"author"\s*:\s*\[(.*?)\]', html, re.DOTALL)
    if sm:
        names = re.findall(r'"name"\s*:\s*"([^"]+)"', sm.group(1))
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
    # Try "By Name" patterns
    if not author:
        m = re.search(r'By\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)', html)
        if m:
            author = m.group(1)
    
    # Body
    am = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    body = am.group(1) if am else html
    mm = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if mm and not am:
        body = mm.group(1)
    
    # Clean
    body = re.sub(r'<nav[^>]*>.*?</nav>', '', body, flags=re.DOTALL|re.I)
    body = re.sub(r'<footer[^>]*>.*?</footer>', '', body, flags=re.DOTALL|re.I)
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<aside[^>]*>.*?</aside>', '', body, flags=re.DOTALL|re.I)
    
    # HTML→MD
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
        md = re.sub(pat, repl, md, flags=re.DOTALL|re.I)
    
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = md.strip()
    
    # Remove leading noise
    lines = md.split('\n')
    start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if len(s) > 20 and not any(x in s.lower() for x in ['case study', 'learn more →', 'we raised', 'all posts', 'follow @', "we're hiring", 'hundreds of millions']):
            start = i
            break
    md = '\n'.join(lines[start:])
    
    if len(md) > 50000:
        md = md[:50000] + "\n\n---\n*Content truncated.*"
    
    # Classify
    text = (slug + " " + md[:1000]).lower().replace("-", " ")
    category = "general"
    for cat, patterns in CATEGORIES.get(site, []):
        for p in patterns:
            if p in text:
                category = cat
                break
        if category != "general":
            break
    
    return {
        "slug": slug, "title": title, "date": date or "Unknown",
        "author": author or "Unknown", "url": url, "category": category,
        "content": md,
    }

def save(article):
    base = os.path.join(BASE_DIR, SITES[article["site"]]["base"])
    cat_dir = os.path.join(base, article["category"])
    os.makedirs(cat_dir, exist_ok=True)
    
    filepath = os.path.join(cat_dir, article["slug"] + ".md")
    
    te = article["title"].replace('"', '\\"')
    ae = article["author"].replace('"', '\\"')
    fm = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
        te, ae, article["date"], article["url"], article["category"], article["site"]
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fm + article["content"])
    return True

def main():
    with open(URL_FILE) as f:
        slugs = [s.strip() for s in f if s.strip()]
    
    if BATCH_END is None:
        end = len(slugs)
    else:
        end = BATCH_END
    
    batch = slugs[BATCH_START:end]
    print("Processing %s batch %d-%d: %d URLs" % (SITE, BATCH_START, end, len(batch)))
    
    saved = 0
    failed = 0
    for i, slug in enumerate(batch):
        url = SITES[SITE]["prefix"] + slug
        html = fetch(url)
        if not html:
            failed += 1
            print("  [%3d/%d] FAIL  %s" % (i+1, len(batch), slug))
            continue
        
        article = extract(html, slug, SITE)
        article["site"] = SITE
        save(article)
        saved += 1
        print("  [%3d/%d] SAVE  %s (%s, %s, %d chars)" % (
            i+1, len(batch), slug, article["date"], article["category"], len(article["content"])))
    
    print("\nDone: %d saved, %d failed" % (saved, failed))

if __name__ == "__main__":
    main()
