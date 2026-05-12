#!/usr/bin/env python3
"""Fetch blog articles from multiple sources and classify them."""
import os
import re
import shutil
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, "posts")
META_DIR = os.path.join(BASE_DIR, "meta")
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

# Classification rules per site
CATEGORIES = {
    "e2b": {
        "sandbox-code-execution": ["sandbox", "code-interpreter", "code-execution", "codebuddy", "execution", "compute"],
        "ai-agents": ["agent", "agentic", "llm-agent", "ai-agent", "multi-agent", "autogpt", "computer-use"],
        "integrations": ["integration", "with-", "x-e2b", "langchain", "openai", "anthropic", "groq", "ollama", "v0", "replit", "cursor"],
        "tutorials": ["how-to", "tutorial", "build", "building", "creating", "guide", "step-by-step"],
        "announcements": ["announcement", "launch", "introducing", "release", "v1", "ga", "funding", "series", "seed"],
        "benchmarks-evals": ["benchmark", "eval", "comparison", "test"],
        "case-studies": ["case-study", "interview", "conversation", "about-", "ceo", "founder"],
    },
    "browserbase": {
        "stagehand": ["stagehand", "act-extract-observe", "web-agent"],
        "tutorials": ["tutorial", "how-to", "building", "guide"],
        "announcements": ["launch", "introducing", "announcement", "ga", "general-availability"],
        "benchmarks": ["benchmark", "eval"],
        "case-studies": ["case-study", "amplitude", "customer"],
        "engineering": ["engineering", "director", "platform", "internal"],
    },
    "modal": {
        "inference": ["inference", "llm", "transformer", "gpu", "vllm", "tensorrt", "triton", "serve", "deploy"],
        "training-finetuning": ["train", "finetune", "fine-tune", "lora", "sft", "checkpoint"],
        "sandboxes": ["sandbox", "firecracker", "microvm", "micro-vm", "cold-start"],
        "case-studies": ["case-study", "joining-modal", "zencastr", "tidbyt"],
        "engineering": ["cuda", "pytorch", "compil", "benchmark", "performance", "optim"],
        "announcements": ["announcing", "launch", "introducing", "release"],
        "serverless": ["serverless", "batch", "queue", "task", "cron", "schedule"],
        "tutorials": ["tutorial", "guide", "how-to", "building"],
        "community": ["community", "meetup", "video", "podcast"],
    },
}

def classify(site, slug, content=""):
    """Classify an article based on site, slug, and content."""
    text = (slug + " " + content[:2000]).lower().replace("-", " ").replace("_", " ")
    cats = CATEGORIES.get(site, {})
    for cat, patterns in cats.items():
        for p in patterns:
            if p in text:
                return cat
    return "general"

def fetch_page(url):
    try:
        r = subprocess.run(
            ["curl", "-sL", "-m", "30",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        if r.returncode == 0 and len(r.stdout) > 100:
            return r.stdout
    except:
        pass
    return None

def extract_article(html, site, slug):
    """Extract article metadata and content from HTML."""
    if site == "e2b":
        url = "https://e2b.dev/blog/" + slug
        base = "https://e2b.dev"
    elif site == "browserbase":
        url = "https://www.browserbase.com/blog/" + slug
        base = "https://www.browserbase.com"
    else:
        url = "https://modal.com/blog/" + slug
        base = "https://modal.com"
    
    # Title
    title_m = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    full_title = title_m.group(1).strip() if title_m else slug
    # Remove site suffix
    for suffix in [" - E2B", " | E2B", " | Browserbase", " | Modal", " - Modal"]:
        full_title = full_title.replace(suffix, "").strip()
    title = full_title if full_title else slug
    
    # Date
    date = None
    for p in [r'"datePublished"\s*:\s*"([^"]+)"', r'article:published_time"\s+content="([^"]+)"',
              r'<time[^>]*datetime="([^"]+)"', r'"dateModified"\s*:\s*"([^"]+)"']:
        m = re.search(p, html)
        if m:
            date = m.group(1)[:10]
            break
    
    # Author
    authors = []
    sm = re.search(r'"author"\s*:\s*\[(.*?)\]', html, re.DOTALL)
    if sm:
        authors = re.findall(r'"name"\s*:\s*"([^"]+)"', sm.group(1))
    if not authors:
        jsonld = re.findall(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"([^"]+)"', html)
        if jsonld:
            authors = jsonld
    if not authors:
        meta = re.findall(r'<meta[^>]*name=["\']author["\'][^>]*content=["\']([^"\']+)["\']', html)
        if not meta:
            meta = re.findall(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*name=["\']author["\']', html)
        if meta:
            authors = [a.strip() for a in meta[0].split(",")]
    author_str = ", ".join(authors) if authors else "Unknown"
    
    # Extract body
    article_body = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_body:
        body_html = article_body.group(1)
    else:
        main_content = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
        body_html = main_content.group(1) if main_content else html
    
    # Remove scripts/styles
    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
    
    # HTML to markdown
    md = body_html
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
    ]:
        md = re.sub(pat, repl, md, flags=re.DOTALL | re.IGNORECASE)
    
    md = re.sub(r'<[^>]+>', '', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = md.strip()
    
    if len(md) > 50000:
        md = md[:50000] + "\n\n---\n*Content truncated.*"
    
    return {
        "slug": slug,
        "title": title,
        "date": date or "Unknown",
        "author": author_str,
        "url": url,
        "category": classify(site, slug, md),
        "content": md,
        "site": site,
    }

def save_article(article):
    cat_dir = os.path.join(POSTS_DIR, article["site"], article["category"])
    os.makedirs(cat_dir, exist_ok=True)
    
    filename = article["slug"] + ".md"
    filepath = os.path.join(cat_dir, filename)
    
    if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
        return False
    
    title_esc = article["title"].replace('"', '\\"')
    author_esc = article["author"].replace('"', '\\"')
    cat_esc = article["category"].replace('"', '\\"')
    
    frontmatter = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\nsite: "%s"\n---\n\n' % (
        title_esc, author_esc, article["date"], article["url"], cat_esc, article["site"]
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + article["content"])
    
    # Save metadata
    meta_path = os.path.join(META_DIR, article["site"], article["slug"] + ".json")
    os.makedirs(os.path.dirname(meta_path), exist_ok=True)
    desc = ""
    desc_m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', "")
    meta_content = '{"title":"%s","author":"%s","date":"%s","url":"%s","category":"%s","site":"%s"}' % (
        title_esc, author_esc, article["date"], article["url"], cat_esc, article["site"]
    )
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(meta_content)
    
    return True

def main():
    site = sys.argv[1]  # e2b, browserbase, modal
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    slug_file = os.path.join(BASE_DIR, "..", "..", "..", "tmp", "%s_slugs.txt" % site)
    if not os.path.exists(slug_file):
        print("Slug file not found: %s" % slug_file)
        sys.exit(1)
    
    with open(slug_file) as f:
        slugs = [s.strip() for s in f if s.strip()]
    
    if end is None:
        end = len(slugs)
    
    batch = slugs[start:end]
    print("Processing %s batch %d-%d: %d URLs" % (site, start, end, len(batch)))
    
    saved = 0
    skipped = 0
    failed = 0
    
    for i, slug in enumerate(batch):
        filename = slug + ".md"
        # Find in any category dir
        found = False
        for d in os.listdir(os.path.join(POSTS_DIR, site)) if os.path.exists(os.path.join(POSTS_DIR, site)) else []:
            fp = os.path.join(POSTS_DIR, site, d, filename)
            if os.path.exists(fp) and os.path.getsize(fp) > 100:
                found = True
                break
        
        if found:
            skipped += 1
            print("  [%3d/%d] SKIP  %s" % (i+1, len(batch), slug))
            continue
        
        if site == "e2b":
            url = "https://e2b.dev/blog/" + slug
        elif site == "browserbase":
            url = "https://www.browserbase.com/blog/" + slug
        else:
            url = "https://modal.com/blog/" + slug
        
        html = fetch_page(url)
        if html is None or '<title>404' in html or 'Page not found' in html[:500]:
            failed += 1
            print("  [%3d/%d] FAIL  %s" % (i+1, len(batch), slug))
            continue
        
        article = extract_article(html, site, slug)
        was_saved = save_article(article)
        if was_saved:
            saved += 1
        else:
            skipped += 1
        
        print("  [%3d/%d] %s  %s (%s) [%d chars]" % (
            i+1, len(batch),
            "SAVED" if was_saved else "SKIP ",
            slug, article["category"], len(article["content"])
        ))
    
    print("\nBatch %s %d-%d: %d saved, %d skipped, %d failed" % (site, start, end, saved, skipped, failed))

if __name__ == "__main__":
    main()
