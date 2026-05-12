#!/usr/bin/env python3
"""Fetch LlamaIndex blog articles, classify, and save as markdown."""
import os
import re
import sys
import subprocess

URL_FILE = "/tmp/llamaindex_blog_slugs.txt"
BASE = "https://www.llamaindex.ai"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
META_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meta")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)

# Classification rules: (category_dir, regex_patterns)
CATEGORIES = [
    ("document-processing", [
        r'parse', r'llamaparse', r'lliteparse', r'ocr', r'extract',
        r'pdf', r'document', r'recognition', r'parsing', r'invoice',
        r'receipt', r'table', r'chart', r'scan', r'kyc', r'mortgage',
        r'income-verification', r'accounts-payable', r'financial-document',
        r'deep-extraction', r'unstructured-data', r'multilingual',
        r'parsebench', r'agentic-document', r'agentic-ocr',
        r'building-an-ocr', r'pdf-character', r'engineering-insights',
        r'beyond-raw-text',
    ]),
    ("rag", [
        r'rag', r'retrieval', r'rerank', r'query-engine', r'search',
        r'vector-store', r'embedding', r'knowledge-graph',
        r'advanced-rag', r'agentic-rag', r'contextual',
    ]),
    ("llamacloud", [
        r'llamacloud', r'cloud-', r'indexing-pipeline',
    ]),
    ("tools-integrations", [
        r'mcp', r'sdk', r'integrat', r'llamafile', r'nvidia',
        r'vllm', r'copilot', r'ag-ui', r'framework',
        r'tooling', r'weaviate', r'chroma', r'pinecone',
        r'milvus', r'qdrant', r'zep', r'groq', r'voyage',
        r'fireworks', r'llamaindex-cloud',
    ]),
    ("benchmarks-evals", [
        r'benchmark', r'eval', r'leaderboard', r'dataset',
        r'compare', r'gpt-4', r'comparison', r'showdown',
        r'accu', r'performance', r'testing',
    ]),
    ("case-studies", [
        r'case-study', r'customer', r'success', r'story',
        r'how.*built', r'how.*used', r'building.*with',
    ]),
    ("llamaindex-core", [
        r'llamaindex-', r'announcing.*llamaindex', r'v0\.',
        r'0\.10', r'0\.9', r'0\.11', r'0\.12',
        r'release', r'new.*llamaindex', r'llama.*index',
        r'workflows', r'agent', r'llama.*agent',
        r'functional-api', r'agent-search', r'llama.*deploy',
    ]),
    ("tutorials-guides", [
        r'how-to', r'tutorial', r'guide', r'recipe',
        r'start', r'beginner', r'step-by', r'walkthrough',
        r'local', r'private',
    ]),
    ("newsletters", [
        r'newsletter', r'weekly',
    ]),
]

def classify(slug):
    slug_lower = slug.lower().replace('/', '').replace('-', ' ').replace('_', ' ')
    # Check URL slug against patterns
    for category, patterns in CATEGORIES:
        for p in patterns:
            if re.search(p, slug_lower):
                return category
    return "general"

def fetch_page(url):
    try:
        result = subprocess.run(
            ["curl", "-sL", "-m", "30", "-A",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        if result.returncode == 0:
            return result.stdout
    except:
        pass
    return None

def extract_article(html, slug):
    url = BASE + slug
    
    # Title
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    full_title = title_match.group(1).strip() if title_match else slug
    title = re.sub(r'\s*[-\u2013]\s*LlamaIndex$', '', full_title).strip()
    if not title:
        title = slug.split('/')[-1].replace('-', ' ').replace('_', ' ').title()
    
    # Date
    date = None
    patterns = [
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'article:published_time"\s+content="([^"]+)"',
        r'<time[^>]*datetime="([^"]+)"',
        r'"dateModified"\s*:\s*"([^"]+)"',
        r'publishDate["\s:]+(\d{4}-\d{2}-\d{2})',
    ]
    for p in patterns:
        m = re.search(p, html)
        if m:
            date = m.group(1)[:10]
            break
    
    # Author
    authors = []
    schema_match = re.search(r'"author"\s*:\s*\[(.*?)\]', html, re.DOTALL)
    if schema_match:
        names = re.findall(r'"name"\s*:\s*"([^"]+)"', schema_match.group(1))
        if names:
            authors = names
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
    
    # Description/summary from meta
    desc = ""
    desc_m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html)
    if not desc_m:
        desc_m = re.search(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*name=["\']description["\']', html)
    if desc_m:
        desc = desc_m.group(1)
    
    # Extract body
    article_body = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_body:
        body_html = article_body.group(1)
    else:
        main_content = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
        if main_content:
            body_html = main_content.group(1)
        else:
            body_html = html
    
    # Remove scripts and styles
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
        (r'<i[^>]*>(.*?)</i>', r'*\1*'),
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
        "slug": slug.strip("/"),
        "title": title,
        "date": date or "Unknown",
        "author": author_str,
        "url": url,
        "description": desc,
        "category": classify(slug),
        "content": md,
    }

def save_article(article):
    # Create category directory
    cat_dir = os.path.join(OUTPUT_DIR, article["category"])
    os.makedirs(cat_dir, exist_ok=True)
    
    filename = article["slug"].replace("/", "__") + ".md"
    filepath = os.path.join(cat_dir, filename)
    
    if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
        return False
    
    title_esc = article["title"].replace('"', '\\"')
    author_esc = article["author"].replace('"', '\\"')
    
    frontmatter = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\ncategory: "%s"\n---\n\n' % (
        title_esc, author_esc, article["date"], article["url"], article["category"]
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + article["content"])
    
    # Save metadata for index
    meta_path = os.path.join(META_DIR, article["slug"].replace("/", "__") + ".json")
    meta_content = '{"title":"%s","author":"%s","date":"%s","url":"%s","category":"%s","description":"%s"}' % (
        title_esc, author_esc, article["date"], article["url"], article["category"],
        article["description"].replace('"', '\\"')
    )
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(meta_content)
    
    return True

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    with open(URL_FILE) as f:
        slugs = [line.strip() for line in f if line.strip()]
    
    if end is None:
        end = len(slugs)
    
    batch = slugs[start:end]
    print("Processing batch %d-%d: %d URLs" % (start, end, len(batch)))
    
    saved = 0
    skipped = 0
    failed = 0
    
    for i, slug in enumerate(batch):
        meta_file = slug.replace("/", "__") + ".json"
        meta_path = os.path.join(META_DIR, meta_file)
        cat_dir_name = classify(slug)
        filename = slug.replace("/", "__") + ".md"
        filepath = os.path.join(OUTPUT_DIR, cat_dir_name, filename)
        
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            skipped += 1
            print("  [%3d/%d] SKIP  %s" % (i+1, len(batch), slug))
            continue
        
        url = BASE + slug
        html = fetch_page(url)
        if html is None:
            failed += 1
            print("  [%3d/%d] FAIL  %s" % (i+1, len(batch), slug))
            continue
        
        article = extract_article(html, slug)
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
    
    print("\nBatch complete: %d saved, %d skipped, %d failed" % (saved, skipped, failed))

if __name__ == "__main__":
    main()
