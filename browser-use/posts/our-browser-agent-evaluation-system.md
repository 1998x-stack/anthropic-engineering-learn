---
title: "How we built scalable evaluation infrastructure for AI web agents"
author: "Alexander Yue"
date: "2026-02-23"
url: "https://browser-use.com/posts/our-browser-agent-evaluation-system"
---

# How we built scalable evaluation infrastructure for AI web agents

**Author:** Alexander Yue
**Date:** 2026-02-23

---

Evaluating an agent that browses the real web isn't like evaluating an LLM on text benchmarks. The web is messy, non-deterministic, and constantly changing.

A popup that takes 100ms longer to load can throw off an entire agent trajectory. A random A/B test can break a selector. Because of this, agent traces are inherently chaotic.

We sourced our evaluation tasks from **millions of LLM-labeled user spans** rather than synthetic sites, because synthetic environments completely fail to capture the bizarre reality, complexity, and ugliness of how the actual web is built.

But dealing with real websites means dealing with variance. Single-run deterministic tests are useless here.

It's concerning that many AI agent benchmarks do not include error bars or variance estimations; coming from backgrounds in experimental particle physics, that lack of statistical rigor is alarming.

You need **real statistical rigor**. That means running the exact same task **multiple times**, messing with a ton of agentic settings, ensuring **perfect reproducibility** of those settings, and aggregating the results with **statistical bootstrapping**.

## Building the Evaluation Engine

### 100 Tasks in Under 5 Minutes

We cycled through several third-party evaluation tools before throwing them out to build an engine in-house.

Using [Blacksmith](https://blacksmith.sh) runners on GitHub Actions, we achieve insane scaling, running 100 complex web tasks in parallel in under 5 minutes end-to-end.

Crucially, we built the LLM judge **directly into the agent code itself**, running after the agent returns `done`. This means that the judge can also double as a **real-time validation layer** for the agent during regular use.

### Observability at Scale

Running fast isn't enough; you need absolute observability. We stream every single token, prompt, timing metric, and cost directly into **ClickHouse** via **Laminar**, which efficiently handles the massive amount of LLM messages.

We even record each browser session and save the frames to Laminar. (For the real-time UI state and making dashboards, we rely on **Convex** to keep our engineers in sync with active runs and results.)

## The LLM Judge & The Failure of Clustering

### Why Deterministic Checks Fail

When tasks involve navigating real websites (e.g., "Find the cheapest flight from JFK to LHR and create a Doc with the options"), there is no simple `assert(success == true)`.

It takes complex reasoning and judgment, but human judges are not scalable. Instead, we need an agentic judge.

### The LLM Judge

We iterated through many judge frameworks, aligning them against **200 meticulously hand-labeled traces**. `gemini-2.5-flash` powers our final judge, achieving an **87% alignment** with human labels.

We found that simple prompts and absolute True/False verdicts work best. Complex rubrics lead to indecisive judging.

### The Clustering Trap

Initially, we tried embedding and clustering the failed traces to find common issues. It was a complete failure.

**The Pivot**: We shifted to having Claude Code extract the raw `failure_reason` string from the judge. Claude reads hundreds of these raw reasons, suggests **concrete categories**, drops the small ones, and iteratively subcategorizes the big ones until we have **highly specific, actionable error buckets**.

## The Agentic Self-Improvement Loop

### Slack as the Control Center

Comparing A/B runs manually in custom dashboards was overwhelming. So we rebuilt the whole evaluation process to be **agent-first**, integrated directly into Slack.

### Claude Code Orchestrator

1. A developer pings Claude in Slack with a request to run an eval.
2. Claude triggers the Blacksmith runners via a custom MCP server and Python scripts. The traces stream into Laminar and ClickHouse.
3. When done, Claude is pinged. It queries the raw trace data directly via SQL.
4. Claude executes its generated SQL queries against ClickHouse and performs statistical A/B analysis, then posts a summary back in Slack.
5. The developer can then ping Claude to make changes to the codebase based on that theory.

## Conclusion & Open Source

This pipeline runs automatically on every single PR in our open-source repo to guarantee we don't regress performance.

We have open-sourced one benchmark for LLM providers and researchers at [github.com/browser-use/benchmark](https://github.com/browser-use/benchmark). The judge prompt and settings are in our open-source agent at [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use).

We are moving toward a fully closed loop: an automated infinite self-improvement cycle where the agent evaluates itself, finds its own flaws, writes its own patches, and proves its success statistically.
