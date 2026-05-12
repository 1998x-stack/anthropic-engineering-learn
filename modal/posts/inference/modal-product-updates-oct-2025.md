---
title: "Product Updates: Updates to Volumes, JS and Go SDKs, and more"
author: "Unknown"
date: "2025-10-31"
url: "https://modal.com/blog/modal-product-updates-oct-2025"
category: "inference"
site: "modal"
---

# Product Updates: Updates to Volumes, JS and Go SDKs, and more

## 🗃️ Volumes v2 now in Beta

 **Volumes v2** is now in open beta and available for all Modal apps. We’ve updated the filesystem to support higher throughput, improved random-access performance, and true high-concurrency writes from hundreds of containers at once.

There’s also no longer a limit on the number of files you can store, making Volumes ideal for managing large datasets, model checkpoints, and training artifacts.

Check out the [Volumes v2 docs](/docs/guide/volumes#volumes-v2) for more.

## 💡Modal SDKs for Javascript and Go are now in Beta

![](https://modal-cdn.com/blog/images/oct2025update_js.gif)

The **Modal SDKs for JavaScript/TypeScript and Go** are now in beta with v0.5. This release brings a unified Client object for interacting with Modal resources, support for Sandboxes, Functions, Images, and Volumes, and extended docs and examples.

[Read the docs](/docs/guide/sdk-javascript-go#modal-sdks-for-javascript-and-go) for more.

## 👩‍💻 Client Updates

Run `pip install --upgrade modal` to get the latest client updates. Here are some highlights from the changelog:

- Introduced [**App tags**](/docs/reference/changelog#120-2025-10-09) for adding key-value metadata to your Apps for better organization and cost tracking
 - Added [**Sandbox Connect Tokens**](/docs/guide/sandbox-networking) for making secure HTTP and WebSocket connections to Sandboxes using authenticated requests

## ⚡️ Reverse engineering Flash Attention 4

![](https://modal-cdn.com/blog/images/oct2025update_fa4.png)

Nvidia’s new **Flash Attention 4** kernel delivers up to 20% faster Transformer attention on **Blackwell GPUs.** Since there’s no paper yet, we dug into the source to explain how it works, from async pipelines to clever math tricks for exponentials and softmax.

Read the full breakdown [here](/blog/reverse-engineer-flash-attention-4).

## 🪩 Modal Vibe: Build an AI coding platform that scales

![](https://modal-cdn.com/blog/images/oct2025update_modalvibe.png)

**Modal Vibe** is a new, open-source demo that shows how to build an AI coding platform that can scale. It lets users prompt an LLM to generate sandboxed web apps that each run inside a **Modal Sandbox** and connect to a React UI through **Modal Tunnels**. The system can scale from zero to thousands of running apps in just minutes.

[Read the blog post](/blog/modal-vibe) for performance results and architecture details, or explore the [repo](https://github.com/modal-labs/modal-vibe) to learn more.

## 🌎 How Meta, Cognition, and Restate are building with Modal Sandboxes

Across research and production, teams are using Modal Sandboxes to securely run code at scale, from world-model research to fast, agentic coding systems.

- The team at Meta FAIR used Sandboxes as part of their reinforcement learning setup for the recently-released Code World Model (CWM), a 32B-parameter open-weights LLM for code generation research. [Read the paper →](https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/)
 - Cognition launched its Fast Context subagent this month with a playground built on Modal Sandboxes, enabling instant, containerized comparisons between SWE-grep, Claude Code, and others — designed to feel local in the browser. [Read more →](https://cognition.ai/blog/swe-grep)
 - In their latest guide, the team at Restate shows how to build a durable, serverless coding agent using Sandboxes for execution, Restate for orchestration, and GPT-5 as the LLM. [Read the guide →](https://www.restate.dev/blog/durable-coding-agent-with-restate-and-modal)

## Upcoming Events

Modal is on the move! Meet the team, grab some swag, and talk shop about AI infra, research, and everything in between.

- **💥 [AI Engineer Code Summit](https://www.ai.engineer/code) (Nov 19-21, NYC)**
 - **☁️ [AWS re:Invent](https://reinvent.awsevents.com/) (Dec 1-5, Las Vegas)**
 - **🧠 [NeurIPS 2025](https://neurips.cc/) (Dec 2-7, San Diego)**

👉 [Check out our event calendar](https://luma.com/calendar/manage/cal-lYa2810srHvkQRC) to RSVP or book a 1:1 with the Modal team at any of these events.