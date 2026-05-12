---
title: "The Fastest Web Agent in the World"
author: "Gregor Zunic"
date: "2025-10-08"
url: "https://browser-use.com/posts/llm-gateway"
---

# The Fastest Web Agent in the World

**Author:** Gregor Zunic
**Date:** 2025-10-08
> We built a special LLM gateway that reduces the latency by 6x while keeping the same performance. The agents can now take 20 steps per minute. How many can a human do?

---

**Browser Use 0.8.0** introduces `ChatBrowserUse` gateway which reduces the latency like crazy (6x faster than computer use models) while keeping the same performance.

Our agents can now take **20 steps per minute**. How many can a human do?

BU 1.0 achieves the same accuracy (~65%) as other state-of-the-art computer use models (Claude Sonnet 4, Claude Sonnet 4.5, Gemini 2.5 Computer Use, OpenAI Computer-Using Model) while being **4x faster**.

The latency shown is pure LLM inference time—just the time the model takes to decide what to do next. Our latency is ~68 seconds per trajectory compared to ~225-330 seconds for other models.

## One API Key. That's It.

All you need is `BROWSER_USE_API_KEY`, which automatically takes care of everything.

```python
"""
1. Get your API key from https://cloud.browser-use.com/dashboard/api
2. Set environment variable: export BROWSER_USE_API_KEY="your-key"
"""
import asyncio
from browser_use import Agent
from browser_use.llm import ChatBrowserUse

async def main():
    agent = Agent(
        task='Find the number of stars of the following repos: browser-use, playwright, stagehand, react, nextjs',
        llm=ChatBrowserUse(),
    )
    await agent.run()
```

That's it. One environment variable and you're running at 2x speed.

## Pricing

| Token Type | Price per 1M tokens |
| --- | --- |
| Input tokens | $0.50 |
| Output tokens | $3.00 |
| Cached tokens | $0.10 |
