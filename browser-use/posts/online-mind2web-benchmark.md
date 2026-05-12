---
title: "How we built the best browser agent with Auto-Research"
author: "Magnus Müller"
date: "2026-03-25"
url: "https://browser-use.com/posts/online-mind2web-benchmark"
---

# How we built the best browser agent with Auto-Research

**Author:** Magnus Müller
**Date:** 2026-03-25
> 97% on Online-Mind2Web benchmark. The highest score ever.

---

## The Benchmark

Online-Mind2Web is the most widely reported browser agent benchmark. 300 tasks across 136 real websites - shopping, finance, travel, government, and more. Every web agent is tested on it.

| Difficulty | Tasks | Example |
| --- | --- | --- |
| Easy | 83 | "Open the reviews of a recipe with beef sirloin" - allrecipes.com |
| Medium | 143 | "Find full-time legal jobs in San Diego County, min $4,000+/month" - ca.gov |
| Hard | 74 | "Find the cheapest hotel + flight + car package from New York to San Francisco, for two adults and a six-year-old child, with free breakfast and spa" - booking.com |
| Total | 300 | |

## How Auto-Research for browser agents works

We give Claude Code a CLI to our eval platform and a prompt to run in a loop.

No orchestration code. Each Claude Code session gets a goal and runs 20 cycles on its own.

With this eval infra we run them in parallel and get a search tree over the space of possible best agents.

We don't care about low performers. We only care about getting the best agent. So we tell the coding agent to make big bets and avoid small changes, since small tweaks get lost in run-to-run variance.

## The debugging CLI for deep dives

One trace can be millions of tokens. That's why we designed the CLI in 3 hierarchical levels to let the agent find root causes as fast as possible.

TSV over JSON saves 40% of tokens for our data structure. Small format choices can make or break agentic debugging.

## The biggest improvement

Claude Code updated our browser agent harness into a coding agent. Instead of only tools like click and type, it added Python to parse HTML and extract data. This aligns much better with the LLM's training distribution and makes edge cases and data extraction dramatically easier.

The rest: fixing hundreds of edge cases with the loop.

**What we added:** The stealthiest browser infrastructure and every day new tasks our power users ask us to fix. Online-Mind2Web improved as a side effect.

## The Leaderboard

| Agent | Score | Is Data Public? |
| --- | --- | --- |
| Browser Use Cloud (bu-max) | 97% | ✓ |
| GPT-5.4 Native Computer Use | 93% | ✗ |
| UI-TARS-2 | 88% | ✗ |
| ABP + Claude Opus 4.6 | 86% | ✓ |
| OpenAGI Lux | 84% | ✗ |
| TinyFish | 81% | ✓ |
| Navigator (Yutori) | 79% | ✗ |
| ChatGPT Atlas Agent Mode | 71% | ✗ |
| Google Gemini CUA | 69% | ✓ |
| Stagehand (Gemini 2.5 CU) | 65% | ✓ |
| OpenAI Operator | 61% | ✓ |
| Claude Sonnet 4.0 CU | 61% | ✗ |
| Stagehand (Sonnet 4.5) | 55% | ✓ |

*OpenAI reported their score without publishing the judge, harness, or task-level results, so independent verification isn't possible.

## The judge matters

The original judge is screenshot-based. But browser agents now write code, call APIs and extract thousands of items. For traditional judges, that's hallucination. If your agentic capabilities increase, you need an agentic judge.

We built an agentic judge on the Claude Agent SDK. We aligned it with human judges, which was key to making the auto-research loop work.

## Are we overfitting?

The natural tendency of the auto-research loop is to overfit on single tasks. You need to prompt the research system hard to generalize. Most of my time merging cycles is rejecting task-specific solutions that overfit.

We use train/validation splits. The loop only sees training data. We then run on old datasets it has never seen and see score improvements across the board.

## No tasks removed

Many companies remove tasks they consider impossible before reporting their score. We use all 300 tasks. Our few failures come from unavailable sites, ambiguous prompts, or websites that changed since the benchmark was created.

## Rerunning our results is easy

Clone github.com/browser-use/online-mind2web, set your Browser Use API key, and run.

We also uploaded prompts, results, and judgments.

## We need harder benchmarks

We're building a benchmark with everything users actually care about. Currently benchmarks ignore tasks like: "Extract 1000 products with subpages and compare them across platforms" because it was unimaginable that a single browser agent could do this.
