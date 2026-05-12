#!/usr/bin/env python3
"""
Subagent script: re-fetch blog articles using web_fetch, clean content, save.
Run with: python3 refetch_articles.py <site> <urls_file>
"""
import os
import re
import json
import sys
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))

# Use openclaw's web_fetch via CLI if available, or fallback to curl
def web_fetch(url, max_chars=80000):
    """Use openclaw web_fetch if available, else curl."""
    # Try openclaw CLI first
    try:
        r = subprocess.run(
            ["openclaw", "web-fetch", url, "--max-chars", str(max_chars)],
            capture_output=True, text=True, timeout=60
        )
        if r.returncode == 0:
            result = json.loads(r.stdout)
            return result.get("text", "")
    except:
        pass
    
    # Fallback to curl
    try:
        r = subprocess.run(
            ["curl", "-sL", "-m", "30",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        return r.stdout if r.returncode == 0 else None
    except:
        return None

def extract_and_save(url, site):
    """Extract article from HTML, save as markdown."""
    html = web_fetch(url)
    if not html:
        return False, "fetch_failed"
    
    slug = url.rstrip("/").split("/")[-1]
    
    # Title
    tm = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = tm.group(1).strip() if tm else slug
    for sfx in [" - E2B", " | E2B", " | Browserbase", " | Modal", " - Modal"]:
        title = title.replace(sfx, "").strip()
    
    # Date
    date = None
    for p in [r'"datePublished"\s*:\s*"([^"]+)"', r'article:published_time"\s+content="([^"]+)"',
              r'<time[^>]*datetime="([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"']:
        m = re.search(p, html)
        if m:
            date = m.group(1)[:10]
            break
    if not date:
        from datetime import datetime
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
    categories = {
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
    
    category = "general"
    for cat, patterns in categories.get(site, []):
        for p in patterns:
            if p in text:
                category = cat
                break
        if category != "general":
            break
    
    # Save
    posts_dir = os.path.join(BASE, site, "posts")
    cat_dir = os.path.join(posts_dir, category)
    os.makedirs(cat_dir, exist_ok=True)
    
    filepath = os.path.join(cat_dir, slug + ".md")
    te = title.replace('"', '\\"')
    ae = (author or "Unknown").replace('"', '\\"')
    fm = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
        te, ae, date or "Unknown", url, category, site
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(fm + md)
    
    return True, category

def main():
    site = sys.argv[1]
    urls_file = sys.argv[2]
    
    with open(urls_file) as f:
        urls = [u.strip() for u in f if u.strip()]
    
    print("Re-fetching %d %s articles" % (len(urls), site))
    
    saved = 0
    failed = 0
    for i, url in enumerate(urls):
        ok, result = extract_and_save(url, site)
        if ok:
            saved += 1
            print("  [%d/%d] OK  %s (%s)" % (i+1, len(urls), url.split("/")[-1], result))
        else:
            failed += 1
            print("  [%d/%d] FAIL %s (%s)" % (i+1, len(urls), url.split("/")[-1], result))
    
    print("\nDone: %d saved, %d failed" % (saved, failed))

if __name__ == "__main__":
    main()
