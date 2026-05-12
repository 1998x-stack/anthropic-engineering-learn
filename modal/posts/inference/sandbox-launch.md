---
title: "Modal Sandboxes are generally available"
author: "Unknown"
date: "2025-01-21"
url: "https://modal.com/blog/sandbox-launch"
category: "inference"
site: "modal"
---

# Modal Sandboxes are generally available

  Sandboxes are the Modal primitive for safely running untrusted code, whether that code comes from LLMs, users, or other third-party sources. We’ve been honing Sandboxes in beta for the past year, and today we’re excited to announce they’re generally available!

## Why we built Sandboxes

We built Modal [Functions](https://modal.com/docs/reference/modal.Function) to run code written by you, the user. Your Functions can interact with your Modal workspace - they can mount Secrets, create Volumes, call other Functions, and more. This model works because you know you can trust the code you deploy directly.

But agentic systems need to execute code without human supervision. Your agent may make a destructive mistake, or a malicious user may prompt your agent in a dangerous direction! In either case, you can’t trust an LLM with your resources the same way that you can trust yourself. LLM-generated code should run in an isolated environment where its blast radius is limited.

These concerns extend to your users as well. When executing user-written code, you need to ensure that an attacker can’t damage your environment or extract sensitive data.

We built Sandboxes to solve for these concerns. Sandboxes give you a dynamic environment to run code in an arbitrary language, safely isolated from the rest of your Modal resources.

## Enough talk, let’s see the code

[Sandboxes](https://modal.com/docs/guide/sandboxes) provide a simple `exec` API for executing code:

LLMs may specify dependencies or need to execute code in other languages. Sandboxes let you configure the execution environment at runtime, using the same [Image](https://modal.com/docs/guide/images) API and infrastructure as Functions:

You can even [snapshot your filesystem](https://modal.com/docs/guide/sandbox-snapshots#filesystem-snapshots) for persistence and to fan out search over many Sandboxes:

This is just a taste of the Sandbox feature set. Check out the [Sandbox docs](https://modal.com/docs/guide/sandboxes) for details on how to [forward ports](https://modal.com/docs/guide/sandbox-networking#forwarding-ports), [restrict network access](https://modal.com/docs/guide/sandbox-networking#networking), [access files](https://modal.com/docs/guide/sandbox-files) and more.

## Why use Modal Sandboxes

Sandboxes run on the same underlying infrastructure as Functions, meaning you get all the benefits you’re used to with Modal Functions. This means blazing fast cold starts, access to the latest GPUs, global region selection, and more are all available in Sandboxes. As we make our core platform more powerful and reliable, those improvements will play out in both Functions and Sandboxes.

The tight integration in our platform also means it’s simple to quickly build features that use both Sandboxes and Functions!

## Customer stories

We’re proud of the applications our customers are building across a variety of use cases that require secure and scalable code execution.

### Accelerating agent benchmarks with SWE-bench

[SWE-bench](https://github.com/swe-bench/SWE-bench) is the highest profile benchmark for testing coding agents. It runs LLM-generated code against actual GitHub pull requests to measure model performance at fixing bugs, implementing features, and more.

We’ve upstreamed Modal support into SWE-bench for blazing fast evaluations. By adding a simple `--modal` flag to their run command, researchers can now:

- Run evaluations entirely in the cloud without any infrastructure setup
 - Execute tests in parallel across hundreds of containers
 - **Run the [Verified benchmark](https://openai.com/index/introducing-swe-bench-verified/) (500 tasks) in only 7 minutes**

Modal’s built-in image caching follows the same layered approach as SWE-bench’s existing Docker images, allowing for a simple integration process. These evaluation runs could take hours previously; the Modal integration enables a much tighter feedback loop.

### Secure code execution at Quora

[Quora](https://www.quora.com/) uses Modal Sandboxes to power the code execution in Poe, their AI chat platform. When you ask Poe’s AI-powered bots to write and run code, that code executes safely in Modal Sandboxes. They’re completely isolated, meaning the code is kept separate from both the main Quora infrastructure and any other user’s code.

This integration allows Poe to offer interactive coding features while still maintaining strict security. You can experiment with code that the AI suggests without worrying about damaging the platform or exposing any sensitive data.

![](https://modal-cdn.com/cdnbot/quora_poe_chatc16fpv5o_3be7782a.webp)

We’ve done extensive performance testing to make sure we’re future-proofed at any scale that Quora may burst up to. **We’ve tested Sandbox creation throughput up to 1000 Sandboxes per second** - if you need to rapidly scale out code execution, let us know!

### Large-scale refactors with Codegen

[Codegen](https://codegen.com) is building an AI system for performing large-scale codebase refactors. Their approach involves building a massive in-memory index of the target codebase and giving AI models the ability to execute “codemods” - automated code transformations that implement the desired changes. For example, our own [modal-client](https://github.com/modal-labs/modal-client) repository looks like this in Codegen:

![](https://modal-cdn.com/cdnbot/codegen_visualizationtb2yqp1y_d1a8c5bc.webp)

Modal Sandboxes provide Codegen with two critical capabilities:

- A reliable environment for building and maintaining their in-memory codebase representations
 - A secure execution environment for running AI-generated codemods with strict isolation

This combination of performance and security enables Codegen to confidently apply AI-driven refactoring at scale.

### AI workforce automation with Relevance AI

[Relevance AI](https://relevanceai.com) is building an AI workforce platform that uses agents to automate complex tasks. They leverage Modal Sandboxes in two key ways:

- Providing a secure environment for their AI agents to run dynamically generated code
 - Powering their notebook/builder feature where users can write and execute code in a serverless environment

![](https://modal-cdn.com/cdnbot/relevance_notebookejxosnq0_5458ea4b.webp)

Modal Sandboxes were a perfect fit for Relevance AI because they offer:

- Flexibility to install any package on demand
 - Full customization of runtime commands
 - Fast cold-boot times for responsive execution
 - Support for any programming language their agents need

This combination lets Relevance AI’s agents tackle a wide range of automation tasks while maintaining strict security boundaries between executions.

## Get started today

Modal Sandboxes are available to all users. Whether you’re building an AI coding assistant, running untrusted user code, or just need a secure environment for code execution, Sandboxes provide the tools you need.

To get started:

- Install Modal: `pip install modal`
 - Create an account: `python -m modal setup`
 - Check out our [Sandbox documentation](https://modal.com/docs/guide/sandboxes)

We can’t wait to see what you build!