---
title: "What LLM model should I use for Browser Use? The Definitive Browser AI Benchmark"
author: "Alexander Yue"
date: "2026-02-19"
url: "https://browser-use.com/posts/what-model-to-use"
---

# What LLM model should I use for Browser Use? The Definitive Browser AI Benchmark

**Author:** Alexander Yue
**Date:** 2026-02-19
> A statistically rigorous benchmark comparing the speed, cost, and accuracy of top frontier models for browser automation.

---

One question dominates every conversation we have with developers: *"Which model should I plug into Browser Use?"*

A single test run means nothing on the chaotic, ever-changing real web. We run our benchmark multiple times per model and aggregate with statistical bootstrapping for real error bars. Our evaluation system has run over 600,000 tasks, validated by an LLM judge achieving 87% agreement with human labels.

## The results

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

"Open Source" means running the open-source Browser Use library with that LLM. "OSS + Cloud LLM" means the open-source library with our ChatBrowserUse-2 model. "Cloud" is the fully managed Browser Use Cloud agent.

100 hand-selected tasks from five sources (Custom, WebBench, Mind2Web 2, GAIA, BrowseComp). Each task is hard but verified completable.

## The model breakdown

### Browser Use Cloud (`bu-ultra`) -- 78.0%

The clear winner. Not just the highest accuracy but also the fastest at ~14 tasks per hour. Each step is slower than a raw frontier LLM call, but bu-ultra completes tasks in far fewer steps, so total wall-clock time is lower.

This isn't just a better model. It's a purpose-built agent with stealth browser infrastructure, CAPTCHA solving, persistent filesystem, and optimized tool orchestration. The 16-point gap over the best frontier model comes from full-stack optimization.

**Verdict**: Best performance, highest throughput, zero setup. Use this.

### ChatBrowserUse-2 (OSS + Cloud LLM) -- 63.3%

Our model specifically optimized for browser automation, running on the open-source library. It outperforms every standalone frontier model while being faster and cheaper per task.

**Verdict**: Best option if you need custom tools or self-hosting but still want top-tier accuracy.

### Claude -- 62.0% (opus), 59.0% (sonnet)

Claude models are the strongest standalone frontier option. Claude-opus-4-6 leads all non-Browser Use models at 62%. When the agent needs to execute custom JavaScript or extract complex structured data, Claude is unparalleled.

Claude-sonnet-4-6 at 59% is close behind opus at roughly half the cost, making it the best value among Anthropic models.

**Verdict**: Best standalone frontier model. Use Claude when your workflow relies on custom code execution.

### Gemini -- 59.3% (3-1-pro), 35.2% (2.5-flash)

Gemini-3-1-pro scores 59.3%, neck and neck with Claude Sonnet. Strong vision, low latency, and massive context windows that handle enormous DOMs without issue.

Gemini-2.5-flash at 35.2% is the fastest cheap option but accuracy drops hard. You get what you pay for.

**Verdict**: Gemini-3-1-pro is a strong alternative to Claude. Flash is only for cost-sensitive, low-stakes tasks.

### OpenAI -- 52.4% (gpt-5), 37.0% (gpt-5-mini)

GPT-5 scores 52.4% and is the slowest model on the benchmark at ~6 tasks per hour. GPT-5-mini at 37% doesn't make up for the speed gap.

Recent OpenAI models have not kept pace with Claude and Gemini on browser automation tasks.

**Verdict**: Falling behind competitors. Use Claude or Gemini instead.

## Recommendations

- **Want the best agent?** Use Browser Use Cloud (`bu-ultra`). 78% accuracy, fastest throughput, no setup.
- **Need custom tools or self-hosting?** Use the open-source library with `ChatBrowserUse-2`. 63.3%, still beats every frontier model.
- **Prefer a standalone frontier LLM?** Claude-opus-4-6 (62%) or gemini-3-1-pro (59.3%).
- **On a budget?** Claude-sonnet-4-6 (59%) gives near-opus accuracy at lower cost.
