---
title: "Up to 5x Faster Sandboxes"
author: "Tereza Tizkova"
date: "2024-02-26"
url: "https://e2b.dev/blog/up-to-5x-faster-sandboxes"
category: "sandbox-code-execution"
site: "e2b"
---

We added support for [Huge Pages](https://www.perplexity.ai/search/what-is-huge-QjvkVL5vQs26enuyxEZj8Q) to our sandboxes.

This new feature makes the start of memory-intensive tasks in sandboxes **up to 5x faster**. For example, reading 0,5 GB of data for the first time after the sandbox starts used to take about **4,9s**. It now takes only **0,76s** thanks to the memory improvements.

Huge pages let you use **2 MiB chunks** of memory instead of **4 KiB chunks**, which are the default. Because there is an overhead each time sandboxes need to ask for more memory, being able to ask for bigger chunks of memory means you can ask fewer times with less total overhead.

Huge pages are enabled by default in all **newly** created custom sandboxes. If you have an existing custom sandbox, you need to rebuild it by calling `e2b build` in the directory with the `e2b.toml` file.

### Getting started

If you want to try the sandboxes, start [here](/docs) and let us know at [hello@e2b.dev](mailto:hello@e2b.dev) if you need any support.