---
title: "Browser Agent Benchmark: Comparing LLM Models for Web Automation"
author: "Alexander Yue"
date: "2026-01-31"
url: "https://browser-use.com/posts/ai-browser-agent-benchmark"
---

# Browser Agent Benchmark: Comparing LLM Models for Web Automation

**Author:** Alexander Yue
**Date:** 2026-01-31
> We benchmark every major LLM on 100 hard browser tasks. Browser Use Cloud scores 78%, 16 points ahead of the best open-source model.

---

## 100 hard browser tasks, one leaderboard

To truly understand our agent performance, we built a suite of internal tools for evaluating our agent in a standardized and repeatable way so we can compare versions and models and continuously improve. We take evaluations seriously. As of now, we have over 600,000 tasks run in testing.

This is our first open source benchmark. BU Bench V1: 100 hand-selected tasks that are hard but possible, drawn from five established sources.

| Source | Tasks | Description |
| --- | --- | --- |
| Custom | 20 | Page interaction challenges (iframes, drag-and-drop, complex forms) |
| WebBench | 20 | Web browsing tasks |
| Mind2Web 2 | 20 | Multi-step web navigation |
| GAIA | 20 | General AI assistant tasks (web-based) |
| BrowseComp | 20 | Browser comprehension tasks |

Every task was run many times with different LLMs, agent settings, and frameworks. Too-easy tasks were removed. Tasks majority-voted impossible and never completed were removed. What's left is hard and verified completable.

The task set is encrypted to prevent LLM training contamination.

## The judge

Real websites can't be judged deterministically. We use an LLM judge (`gemini-2.5-flash`) with a simple true/false verdict. Rubric-based scoring sounds better in theory, but in practice LLMs give middling scores to both successes and failures. Binary verdicts are more reliable.

We hand-labeled 200 traces and measured alignment. The judge agrees with human judgments 87% of the time, differing only on partial successes and technicalities.

To ensure consistency across models, the same judge LLM, prompt, and inputs are used for every evaluation.

## Results

| Model | Type | Score |
| --- | --- | --- |
| Browser Use Cloud (bu-ultra) | Cloud | 78.0% |
| OSS + BU LLM (ChatBrowserUse-2) | OSS + Cloud LLM | 63.3% |
| claude-opus-4-6 | Open Source | 62.0% |
| gemini-3-1-pro | Open Source | 59.3% |
| claude-sonnet-4-6 | Open Source | 59.0% |
| gpt-5 | Open Source | 52.4% |
| gpt-5-mini | Open Source | 37.0% |
| gemini-2.5-flash | Open Source | 35.2% |

**Browser Use Cloud leads at 78%**, 16 points ahead of the best open-source model. Each model was evaluated multiple times and results include error bars (standard error).

The throughput plot tells the rest of the story. Browser Use Cloud (bu-ultra) is both the most accurate **and** the fastest at ~14 tasks per hour. GPT-5 is the slowest at ~6 tasks per hour.

## Why Cloud scores higher

Browser Use Cloud is not just a model. It combines a purpose-built agent with our own browser infrastructure: stealth proxies, CAPTCHA solving, persistent filesystem, and optimized tool orchestration. The 16-point gap over the best open-source model comes from this full-stack optimization, not just a better LLM.

For users who need custom tools or self-hosting, the open-source library with ChatBrowserUse-2 (63.3%) still outperforms every standalone open-source model.
