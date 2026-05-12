#!/usr/bin/env python3
"""Deduplicate blog articles - keep the larger/better version."""
import os
import re
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))

for site in ["e2b", "browserbase", "modal"]:
    posts_dir = os.path.join(BASE, site, "posts")
    if not os.path.exists(posts_dir):
        continue
    
    # Find all files and group by filename
    files_by_name = defaultdict(list)
    for root, dirs, files in os.walk(posts_dir):
        for f in files:
            if f.endswith(".md") and f != "index.md":
                filepath = os.path.join(root, f)
                size = os.path.getsize(filepath)
                files_by_name[f].append((filepath, size))
    
    # Deduplicate
    removed = 0
    for filename, file_list in files_by_name.items():
        if len(file_list) <= 1:
            continue
        # Keep the largest file (best content)
        file_list.sort(key=lambda x: x[1], reverse=True)
        keep_path, keep_size = file_list[0]
        for remove_path, remove_size in file_list[1:]:
            print("  REMOVE (%d bytes): %s (keeping %s with %d bytes)" % (
                remove_size, remove_path, keep_path, keep_size))
            os.remove(remove_path)
            removed += 1
    
    # Remove empty dirs
    for d in os.listdir(posts_dir):
        dp = os.path.join(posts_dir, d)
        if os.path.isdir(dp) and not os.listdir(dp):
            os.rmdir(dp)
    
    # Count remaining
    remaining = sum(1 for root, dirs, files in os.walk(posts_dir) for f in files if f.endswith(".md") and f != "index.md")
    print("%s: removed %d duplicates, %d articles remaining" % (site, removed, remaining))
