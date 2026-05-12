---
title: "Stealth Browser Infrastructure"
author: "Gregor Zunic"
date: "2025-09-30"
url: "https://browser-use.com/posts/browser-infra"
---

# Stealth Browser Infrastructure

**Author:** Gregor Zunic
**Date:** 2025-09-30
> Introducing: Stealth and native browser use infrastructure built directly into the library. Want to bypass Cloudflare, or any other anti-bot protection? It's never been easier 👀

---

We're excited to announce **Browser Use Cloud Infrastructure** - a native browser service built directly into the Browser Use library itself.

Our in-house browser infrastructure is built to bypass essentially anything. Whether you're dealing with anti-bot protections, CAPTCHAs, or restrictive environments, Browser Use Cloud handles it seamlessly. Your agents browse like real users—undetectable, unrestricted, and unstoppable.

## One API Key. That's It.

Getting started with cloud browsers used to mean juggling multiple services, configuring CDPs, and managing complex infrastructure. Not anymore.

With Browser Use Cloud, you simply need a `BROWSER_USE_API_KEY` and you're ready to run agents at scale:

```python
from browser_use import Agent, Browser, ChatOpenAI

# Use Browser-Use cloud browser service
browser = Browser(
    use_cloud=True,  # Automatically provisions a cloud browser
)

agent = Agent(
    task="Your task here",
    llm=ChatOpenAI(model='gpt-4.1-mini'),
    browser=browser,
)
```

That's it. The same simple code you'd use locally, now running on scalable cloud infrastructure.
