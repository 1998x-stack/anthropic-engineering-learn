---
title: "Speed Matters: How Browser Use Achieves the Fastest Agent Execution"
author: "Gregor Zunic"
date: "2025-10-09"
url: "https://browser-use.com/posts/speed-matters"
---

# Speed Matters: How Browser Use Achieves the Fastest Agent Execution

**Author:** Gregor Zunic
**Date:** 2025-10-09
> Matching state-of-the-art accuracy is table stakes. We built BU 1.0 to be the fastest browser agent while maintaining the same performance.

---

BU 1.0 achieves **65.7% accuracy** on OnlineMind2Web — matching Gemini 2.5 Computer Use and outperforming all the other models. We recently released our LLM gateway that makes this possible.

But accuracy is table stakes. People want their agents to work at least as fast as humans.

## Evaluation Challenges

Before diving into performance, a quick note on methodology: Standard screenshot-based evaluation pipelines like OnlineMind2Web's judge don't work for Browser Use. Why? Because BU 1.0 extracts the DOM into a text-based representation that the LLM can interact with. The agent can read content and interact with elements that aren't directly visible in screenshots.

Screenshot-based judges miss this entirely. So we adapted the judge to consider both the screenshot *and* the DOM state at each step. This gives a fair comparison to vision-based models while accurately capturing what DOM-based agents can actually do.

## The Speed Advantage

In OnlineMind2Web, BU 1.0 agent completes tasks in **68 seconds on average**. For context:
- Gemini 2.5 Computer Use: 225s
- Claude Sonnet 4.5: 285s
- Claude Sonnet 4: 295s
- OpenAI Computer-Using Model: 330s

We're significantly faster than other state-of-the-art models - taking on average 3 seconds per step with our strongest model.

## How We Built the Fastest Agent

### 1. Making Use of the KV Cache

Unlike coding agents where state is "previous state + agent's changes," browser agents face a fundamental challenge: the browser state changes independently and must be re-observed at each step.

We solved this by placing agent history before the browser state in our prompt structure. This lets us cache the entire conversation history while presenting fresh browser state to the agent. The result? Significant latency and cost reduction through KV cache hits without sacrificing state accuracy.

### 2. Screenshots Only When Needed

Most web navigation doesn't require vision. BU 1.0 navigates primarily using the DOM, only capturing screenshots when visual context is actually necessary.

The cost? Our experiments both with custom and closed-source multimodal models show that each screenshot adds **~0.8 seconds** to LLM inference latency as the image encoder processes it. By making screenshots optional, we eliminate this overhead for the majority of steps and allow the model to view the page when needed.

### 3. Smart Text Extraction

Computer use models typically extract information by reading screenshots. This is expensive and limited—you can only see what fits on screen.

BU 1.0 has an `extract` tool that queries page's markdown directly from the DOM. When a page contains 20,000+ tokens of text, the agent doesn't dump everything into its context. Instead, it asks: "What's the price of this product?" or "When was this PR opened?" The `extract` tool runs a separate LLM call against the page markdown, retrieves only the relevant information, and returns it to the agent.

### 4. Minimize Output Tokens

We measured token costs on our infrastructure with custom LLMs we trained for Browser Use:
- 1,000 input tokens: **29.1ms**
- 10 output tokens: **62.6ms**

Output tokens cost **~215x more time** than input tokens per unit time.

To minimize output token usage, we designed our action space to be extremely concise. Action names and parameters are terse enough that most actions can be expressed in **10-15 tokens**. Less output = faster execution.

Speed matters. BU 1.0 delivers SOTA accuracy at a fraction of the latency.
