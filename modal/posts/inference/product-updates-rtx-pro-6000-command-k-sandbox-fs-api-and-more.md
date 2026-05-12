---
title: "Product Updates: RTX Pro 6000 Blackwell, Command K, Sandbox FS API and more"
author: "Unknown"
date: "2026-04-07"
url: "https://modal.com/blog/product-updates-rtx-pro-6000-command-k-sandbox-fs-api-and-more"
category: "inference"
site: "modal"
---

# Product Updates: RTX Pro 6000 Blackwell, Command K, Sandbox FS API and more

## ⚡RTX Pro 6000 Blackwell is now available on Modal

![](https://modal-cdn.com/cdnbot/- (4)s6xce7jf_beda80e0.webp)NVIDIA's RTX Pro 6000 Blackwell is now available on Modal with a single line of code. With 96GB of VRAM and strong fp4/fp8 throughput, it's great for inference workloads, fine-tuning runs, and anything that benefits from large memory headroom.

[Learn more](https://modal.com/docs/guide/gpu#specifying-gpu-type) about specifying your GPU type.

## ⌨️ Command K now in the dashboard

Hit **CMD+K** (or Ctrl+k on Windows) anywhere in the Modal dashboard to open the new Command Palette. This first release includes basic navigation shortcuts and the ability to jump directly to any Modal object page by pasting its Modal ID. You can also jump straight to the object from the CLI by using [`modal dashboard &lt;object-id>`](https://modal.com/docs/reference/cli/dashboard#modal-dashboard).

## 📁 Sandbox Filesystem API now in Beta

We’ve overhauled the sandbox Filesystem API to improve reliability and stability over the prior Alpha version. The FS API is the easiest way to move files in and out of sandboxes. It supports reading files up to 5GB, writing files of any size, streaming in both directions, and syncing data to volumes V2:

[Read the docs →](https://modal.com/docs/guide/sandbox-files#filesystem-api-beta)

## 💻 SDK Updates

Run `uv pip install --upgrade modal` to get the latest. Highlights from the [changelog](https://modal.com/docs/reference/changelog):

### CLI for Modal Logs

We’ve made significant CLI enhancements so that Modal logs can be more accessible to coding agents (and humans!). [`modal app logs`](https://modal.com/docs/reference/cli/app#modal-app-logs) and [`modal container logs`](https://modal.com/docs/reference/cli/container#modal-container-logs) commands now have the ability to fetch historical logs using counting (e.g. `--tail 1000`) or time-based (e.g., `--since 4h`, `--until 2026-03-15`, etc.) configuration. You can also now filter by `--search`, `--source`, `--function`, `--container`, and prefix each line with its origin ID.

### New deployment strategies

You can now use `--strategy recreate` when running [`modal deploy`](https://modal.com/docs/reference/cli/deploy#modal-deploy) (or `app.deploy(strategy="recreate")`) to immediately terminate running containers when a deployment completes, guaranteeing all subsequent inputs hit the new version instead of waiting for a graceful rollover. This is useful for dev workflows and for Apps running at `max_containers`. `modal serve` now uses this strategy automatically during code updates. The default rolling strategy is unchanged.

### More from 1.4.0

- [`modal.Image.from_scratch()`](https://modal.com/docs/reference/modal.Image#from_scratch) — creates a minimal empty image, useful as a lightweight filesystem to mount into a Sandbox
- Sandboxes now accept `include_oidc_identity_token=True` for OIDC-based auth (e.g. AWS federation)
- Finally, we’re introducing a few breaking changes and beginning to enforce some deprecations of pre-1.0 APIs, including the removal of backwards compatibility for the old autoscaler configuration (`keep_warm`, `concurrency_limit`, etc.), removal of vestigial `namespace` parameters, and more.

## 📖 Content Roundup

### Deploy Gemma 4

Learn how to deploy Google's Gemma 4 on Modal. We published a detailed walkthrough for the 26B-A4B variant, a multimodal, reasoning-capable MoE model that punches way above its weight. The example covers the full setup: caching weights with Modal Volumes, configuring vLLM, and wiring up tool use and reasoning parsing for Gemma 4.

[Check out the example ](https://modal.com/docs/examples/vllm_inference#run-openai-compatible-llm-inference-with-gemma-and-vllm)[→](https://modal.com/blog/runway-chooses-modal-to-power-real-time-inference-for-runway-characters)

### Powering real-time inference at Runway

Runway Characters is a real-time video agent API built on GWM-1 that lets developers create expressive conversational characters from a single image with zero fine-tuning. Runway's team went from proof of concept to production on Modal in under 30 days.

[Read the post → ](https://modal.com/blog/runway-chooses-modal-to-power-real-time-inference-for-runway-characters)

### Building the agentic dev stack on Modal

Imbue is building an agentic dev stack on Modal. [Mngr](https://imbue.com/product/mngr/) orchestrates 100s of isolated AI coding agents across Modal sandboxes. Attach to any one live mid-task, auto-shutdown when idle. [Keystone](https://imbue.com/product/keystone/) generates working Dockerfiles for any repo by running Claude Code safely in a Modal sandbox. [Offload](https://imbue.com/product/offload/) fans out test suites across up to 200 Modal sandboxes, seeing 6x speedups on real test suites.

### How Doppel eliminated ML infrastructure tax with Modal

Doppel migrated their ML workflows to Modal and cut build times by up to 10× with image layer caching and persistent volumes for model weights. Their inference workloads now auto-scale to absorb traffic spikes, no manual intervention needed.

[Read the post →](https://modal.com/blog/how-doppel-eliminated-ml-infrastructure-tax-with-modal)

## 📍 Find Modal this April

- [HumanX After Hours](https://luma.com/j0fpyhpe): The Open-Source AI Stack: Apr 7 | San Francisco
- [Voice AI Leaders Dinner with pyannoteAI and Modal](https://luma.com/hy8cea3g): Apr 8 | London
- [Truly Serverless GPUs: A Deep Dive Inside Modal's Fast Cold Starts:](https://watch.getcontrast.io/register/modal-truly-serverless-gpus-a-deep-dive-inside-modal-s-fast-cold-starts) Apr 8 | Virtual
- [AI After Hours — Let's keep HumanX going](https://luma.com/humanxafterhours): Apr 8 | San Francisco
- [AI night at the aquarium](https://luma.com/clb9w0mk): Apr 9 | London
- [Voice AI builders night:](https://luma.com/voice_builders) Apr 16 | San Francisco

👉 [See everything coming up](https://luma.com/modal-labs)