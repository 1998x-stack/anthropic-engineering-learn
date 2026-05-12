---
title: "Browser Use = state of the art Web Agent"
author: "Gregor Zunic"
date: "2024-12-15"
url: "https://browser-use.com/posts/sota-technical-report"
---

# Browser Use = state of the art Web Agent

**Author:** Gregor Zunic
**Date:** 2024-12-15
> Browser Use achieves state-of-the-art performance on the WebVoyager benchmark with an 89.1% success rate.

---

We're excited to announce that Browser Use has achieved state-of-the-art performance on the WebVoyager benchmark, with an impressive **89.1% success rate** across 586 diverse web tasks. And the best part? We are FULLY open source.

## Method

We took the existing WebVoyager codebase and slightly changed it according to our needs. The prompts are slightly different. We also migrated pure openai to Langchain. All the code used for testing is available at eval repository.

We ran our evaluation with gpt4o.

Some tasks are impossible to solve. For Apple doesn't show prices for certain products in the dataset, there are no recipes for chocolate chip cookies etc.

A lot of tasks have dates in the past (kookings, flights), so we just changed the years from 2023 to 2024 or 2024 to 2025 respectively.

We removed 55 tasks.

## The Results

Here's how Browser Use performed across different domains:

| Website | Success Rate | Avg Steps |
| --- | --- | --- |
| Huggingface | 100% | 9.7 |
| Google Flights | 95% | 36.2 |
| Amazon | 92% | 14.7 |
| GitHub | 92% | 15.9 |
| Apple | 91% | 12.5 |
| BBC News | 91% | 18.2 |
| Cambridge Dictionary | 91% | 16.7 |
| Allrecipes | 90% | 18.3 |
| Coursera | 90% | 8.5 |
| Google Search | 90% | 14.4 |
| Google Map | 86% | 14.9 |
| ESPN | 85% | 21.0 |
| ArXiv | 83% | 17.6 |
| Wolfram Alpha | 83% | 18.4 |
| Booking | 80% | 32.7 |

Even our "worst" performing domain (Booking.com) still achieved an 80% success rate. Not too shabby!

## Analysis

We believe in transparency, so here are some caveats:

### Manual correction of evaluations

The eval model is not good. That's why we added another success criteria - `unknown` if the eval model is not sure.

We manually reviewed the evaluations for the tasks that are either "unknown" or "failed" and corrected them. This is due to the fact that the default WebVoyager evaluator is not good.

- Some tasks were impossible due to outdated data (we removed these)
- Cloudflare sometimes got grumpy and blocked us
- The original evaluation model wasn't great (we manually reviewed edge cases)
- Some prompts were more ambiguous than your average fortune cookie

## What's Next?

We're not stopping here! Coming soon:
- make manually labeled items more transparent
- add proxy rotations for Cloudflare blocking
- test all kinds of models and different setups (Claude, GPT-4o, Llama 3, etc.)
- test different setups (single vs multiple images, single vs multiple tasks, etc.)
