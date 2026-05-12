#!/usr/bin/env python3
"""
Refetch all blog articles using web_fetch (handles JS rendering).
Run as: python3 refetch_batch.py <site> <start> <end>

This script generates a list of URLs and uses openclaw's web_fetch equivalent.
Since we can't call web_fetch from Python directly, this script outputs URLs
that need to be fetched.

Usage: The subagent should use web_fetch tool for each URL, then save the markdown.
"""
import os
import sys

URLS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls_to_fetch.txt")

SITES = {
    "e2b": "https://e2b.dev/blog/",
    "browserbase": "https://www.browserbase.com/blog/",
    "modal": "https://modal.com/blog/",
}

site = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3]) if len(sys.argv) > 3 else None

# Get slugs from existing files
posts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), site, "posts")
slugs = []
for root, dirs, files in os.walk(posts_dir):
    for f in files:
        if f.endswith(".md") and f != "index.md":
            slugs.append(f.replace(".md", ""))

slugs = sorted(set(slugs))
if end is None:
    end = len(slugs)

batch = slugs[start:end]
prefix = SITES[site]

urls = [prefix + s for s in batch]
with open(URLS_FILE, "w") as f:
    f.write("\n".join(urls))

print("Site: %s, Batch: %d-%d, URLs: %d" % (site, start, end, len(urls)))
for u in urls[:5]:
    print("  %s" % u)
if len(urls) > 5:
    print("  ... and %d more" % (len(urls) - 5))
