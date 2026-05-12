#!/usr/bin/env python3
"""Generate tasks for subagents to re-fetch all articles properly."""
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))

# Collect all existing article slugs per site
sites_data = {}
for site in ["e2b", "browserbase", "modal"]:
    posts_dir = os.path.join(BASE, site, "posts")
    if not os.path.exists(posts_dir):
        continue
    
    slugs = []
    for root, dirs, files in os.walk(posts_dir):
        for f in files:
            if f.endswith(".md") and f != "index.md":
                slugs.append(f.replace(".md", ""))
    
    sites_data[site] = {
        "slugs": sorted(slugs),
        "prefix": {"e2b": "https://e2b.dev/blog/", "browserbase": "https://www.browserbase.com/blog/", "modal": "https://modal.com/blog/"}[site],
    }
    print("%s: %d articles" % (site, len(slugs)))

# Write task list
task_file = os.path.join(BASE, "refetch_tasks.json")
with open(task_file, "w") as f:
    json.dump(sites_data, f, indent=2)

print("\nTask file written to: %s" % task_file)
print("Total: %d articles to re-fetch" % sum(len(v["slugs"]) for v in sites_data.values()))
