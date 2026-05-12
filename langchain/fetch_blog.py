#!/usr/bin/env python3
"""Fetch LangChain blog articles and save as markdown."""
import os
import re
import sys
import subprocess
import json
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)
URL_FILE = "/tmp/langchain_blog_urls.txt"

def fetch_with_curl(url):
    """Fetch a page using curl."""
    try:
        result = subprocess.run(
            ["curl", "-sL", "-m", "30", "-A",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
             url],
            capture_output=True, text=True, timeout=35
        )
        if result.returncode == 0:
            return result.stdout
    except Exception as e:
        print(f"    ERROR: {e}")
    return None

def extract_article(html, url):
    """Extract article metadata and content from HTML."""
    slug = url.rstrip("/").split("/")[-1]
    
    # Title
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    full_title = title_match.group(1).strip() if title_match else slug
    title = re.sub(r'\s*[-\u2013]\s*LangChain$', '', full_title).strip()
    if not title:
        title = slug
    
    # Date
    date = None
    patterns = [
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'article:published_time"\s+content="([^"]+)"',
        r'<time[^>]*datetime="([^"]+)"',
        r'"dateModified"\s*:\s*"([^"]+)"',
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
        meta = re.findall(r'<meta[^>]*name=["\']author["\'][^>]*content=["\']([^"\']+)["\']', html)
        if not meta:
            meta = re.findall(r'<meta[^>]*content=["\']([^"\']+)["\'][^>]*name=["\']author["\']', html)
        if meta:
            authors = [a.strip() for a in meta[0].split(",")]
    
    if not authors:
        # Try JSON-LD
        jsonld = re.findall(r'"author":\s*\{[^}]*"name":\s*"([^"]+)"', html)
        if jsonld:
            authors = jsonld
    
    author_str = ", ".join(authors) if authors else "Unknown"
    
    # Extract body content
    # Try article tag first
    article_body = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
    if article_body:
        body_html = article_body.group(1)
    else:
        # Try main tag
        main_content = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
        if main_content:
            body_html = main_content.group(1)
        else:
            body_html = html
    
    # Remove scripts and styles
    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
    
    # Basic HTML to markdown
    md = body_html
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n\n# \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n\n## \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n\n### \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n\n#### \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<h5[^>]*>(.*?)</h5>', r'\n\n##### \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*(?:alt="([^"]*)")?[^>]*/?>', r'![\2](\1)', md, flags=re.IGNORECASE)
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<br\s*/?>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'</?[uo]l[^>]*>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'\n\n> \1\n\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<hr[^>]*/?>', '\n\n---\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<[^>]+>', '', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = md.strip()
    
    # Truncate
    if len(md) > 50000:
        md = md[:50000] + "\n\n---\n*Content truncated.*"
    
    return {
        "slug": slug,
        "title": title,
        "date": date or "Unknown",
        "author": author_str,
        "url": url,
        "content": md,
    }

def save_article(article):
    filename = article["slug"] + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
        return False
    
    title_esc = article["title"].replace('"', '\\"')
    author_esc = article["author"].replace('"', '\\"')
    
    frontmatter = '---\ntitle: "%s"\nauthor: "%s"\ndate: "%s"\nurl: "%s"\n---\n\n' % (
        title_esc, author_esc, article["date"], article["url"]
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter + article["content"])
    return True

def load_existing_article(filepath, slug):
    """Load metadata from existing file."""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
        title_m = re.search(r'title:\s*"([^"]*)"', content)
        date_m = re.search(r'date:\s*"([^"]*)"', content)
        author_m = re.search(r'author:\s*"([^"]*)"', content)
        url_m = re.search(r'url:\s*"([^"]*)"', content)
        return {
            "slug": slug,
            "title": title_m.group(1) if title_m else slug,
            "date": date_m.group(1) if date_m else "Unknown",
            "author": author_m.group(1) if author_m else "Unknown",
            "url": url_m.group(1) if url_m else "https://www.langchain.com/blog/" + slug,
            "content": "",
        }
    except:
        return None

def build_index(articles):
    sorted_articles = sorted(articles, key=lambda x: x["date"], reverse=True)
    
    years = {}
    for a in sorted_articles:
        year = a["date"][:4] if len(a["date"]) >= 4 else "Unknown"
        if year not in years:
            years[year] = []
        years[year].append(a)
    
    lines = [
        "# LangChain Blog Index",
        "",
        "> Source: https://www.langchain.com/blog",
        "> Archived: " + datetime.now().strftime("%Y-%m-%d"),
        "> Total: %d articles" % len(articles),
        "",
    ]
    
    for year in sorted(years.keys(), reverse=True):
        lines.append("## %s" % year)
        lines.append("")
        lines.append("| Date | Title | File |")
        lines.append("| --- | --- | --- |")
        
        for a in years[year]:
            filename = a["slug"] + ".md"
            date_display = a["date"] if a["date"] != "Unknown" else ""
            title_display = a["title"].replace("|", "\\|")
            lines.append("| %s | [%s](%s) | [%s](./%s) |" % (
                date_display, title_display, a["url"], filename, filename
            ))
        lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("## Stats")
    lines.append("")
    lines.append("- **Total articles:** %d" % len(articles))
    if sorted_articles:
        lines.append("- **Date range:** %s to %s" % (sorted_articles[-1]["date"], sorted_articles[0]["date"]))
    lines.append("")
    
    return "\n".join(lines)

def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    with open(URL_FILE) as f:
        urls = [line.strip() for line in f if line.strip()]
    
    if end is None:
        end = len(urls)
    
    batch_urls = urls[start:end]
    print("Processing batch %d-%d: %d URLs" % (start, end, len(batch_urls)))
    
    articles = []
    
    for i, url in enumerate(batch_urls):
        slug = url.rstrip("/").split("/")[-1]
        filepath = os.path.join(OUTPUT_DIR, slug + ".md")
        
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            art = load_existing_article(filepath, slug)
            if art:
                articles.append(art)
            print("  [%3d/%d] SKIP  %s" % (i+1, len(batch_urls), slug))
            continue
        
        html = fetch_with_curl(url)
        if html is None:
            print("  [%3d/%d] FAIL  %s" % (i+1, len(batch_urls), slug))
            continue
        
        article = extract_article(html, url)
        saved = save_article(article)
        articles.append(article)
        print("  [%3d/%d] %s  %s (%d chars)" % (
            i+1, len(batch_urls),
            "SAVED" if saved else "SKIP ",
            slug, len(article["content"])
        ))
    
    # Load any other existing articles for index
    existing_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".md") and f != "index.md"]
    existing_slugs = set(a["slug"] for a in articles)
    
    for ef in existing_files:
        slug = ef.replace(".md", "")
        if slug in existing_slugs:
            continue
        filepath = os.path.join(OUTPUT_DIR, ef)
        art = load_existing_article(filepath, slug)
        if art:
            articles.append(art)
    
    # Build index
    index_content = build_index(articles)
    with open(os.path.join(OUTPUT_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print("\nDone! %d articles indexed." % len(articles))

if __name__ == "__main__":
    main()
