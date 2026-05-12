---
title: "Product Updates: Directory Snapshots, GLM-5, Billing updates and more"
author: "Unknown"
date: "2026-03-04"
url: "https://modal.com/blog/product-updates-directory-snapshots-glm-5-billing-updates-and-more"
category: "inference"
site: "modal"
---

# Product Updates: Directory Snapshots, GLM-5, Billing updates and more

## 📁 Introducing Directory Snapshots for Modal Sandboxes

Until now, snapshotting a Sandbox meant capturing the entire filesystem as one unit. Directory Snapshots let you snapshot a specific directory and mount it into a new Sandbox later, independently of the base image. This makes it easy to separate system dependencies from application code, pre-warm Sandbox pools, and speed up initialization times.

[Read the full post](https://modal.com/blog/directory-snapshots-resumable-project-state-for-sandboxes) to learn more.

## 🤖 Try GLM-5, free on Modal

[Z.ai](http://Z.ai) recently shipped GLM-5, a frontier open-weights model built for long-horizon agents matching the performance of the latest proprietary models. We partnered with [Z.ai](http://Z.ai) to release a free public endpoint through the end of April so everyone can try the model. It’s great for coding agents, and compatible with OpenCode, Claude Code, OpenClaw, and the Vercel AI SDK.

[Try it free](https://modal.com/glm-5-endpoint) today, or [read the blog](https://modal.com/blog/try-glm-5) for examples on how to integrate with coding agents.

> [](https://twitter.com/_/status/2022050582832590850)

## 💲Better billing visibility: Refreshed UI and new billing API

The `modal billing report` CLI and `modal.billing.workspace_billing_report` API are now generally available for all Team and Enterprise plan workspaces, making it easier to track and report on Modal usage programmatically. We've also rolled out a refreshed billing UI for all workspaces.

[Read the docs](https://modal.com/docs/guide/billing#generating-billing-reports) to learn more, or check out [your new billing page!](https://modal.com/settings/usage)

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/blog/images/New_billing_ui.gif)

## 💻 SDK Updates

Run `uv pip install --upgrade modal` to get the latest client updates. Here are some highlights from the changelog:

- The Modal CLI now has a `modal changelog` command that prints release notes, offering a flexible query interface like `modal changelog --since=2025-12-01` or `modal changelog --newer`. Use this feature to teach your coding agents about new Modal features or other changes to the SDK.
- We’ve added more ways to move from your code to the associated object in the modal dashboard. Modal objects now have a `.get_dashboard_url()` method, and we’ve added new `modal dashboard`, `modal app dashboard` and `modal volume dashboard` CLI commands to make it easier to open any App or Volume directly.
- `modal.Sandbox` objects now have a `.detach()` method that you can call to trigger resource cleanup, which can be useful for long-lived clients managing many Sandboxes

## 📹 Inside Modal Sandboxes

Sandboxes are becoming the default infrastructure for coding agents. In our recent webinar, we look at how teams are running coding agents at scale. We cover common patterns for scaling Sandboxes, security and networking tradeoffs, and the scaffolding decisions that matter most when moving from prototype to production.

## 🔬 AI research that accelerates AI research

Researchers are increasingly using AI to accelerate AI research itself, and Modal is helping make that work possible. We spoke with labs at Stanford doing some of the most exciting work in this space — from TTT-Discover, which used Modal's consistent GPU environment to train a model that out-wrote human engineers at a GPUMODE kernel contest, to RL-4-MLE, which is using Modal Sandboxes to automate the full ML research lifecycle across hundreds of concurrent rollouts.

[Read the blog](https://modal.com/blog/accelerating-ai-research-case-study) for more.

## **📍 **Find Modal this March

From Nvidia GTC to agent infrastructure convos in NYC, we’ve got a packed month ahead. Here are a few highlights:

- [Intro to Speculative Decoding](https://watch.getcontrast.io/register/modal-high-performance-inference-intro-to-speculative-decoding): March 11 | Virtual
- [Modal @ Nvidia GTC](https://luma.com/cb479eme): March 16-19 | Booth 4020
- [Women in AI/ML](https://luma.com/niwjk62h): March 16 | San Jose
- [Agents after hours](https://luma.com/agents_after_hours): March 17 | Santa Clara
- [raid 8: talks on research, ai, design](https://luma.com/1y7fu01k): March 26 | NYC
- [Scaling up AI Agent Infrastructure](https://luma.com/pxlqabyf): March 30 | NYC

👉 [See everything that’s coming up](https://luma.com/modal-labs)