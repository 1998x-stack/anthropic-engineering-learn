---
title: "Introducing Notebooks"
author: "ekzhang1"
date: "2025-09-09"
url: "https://modal.com/blog/notebooks"
category: "inference"
site: "modal"
---

# Introducing Notebooks

In most cloud notebooks, kernels take minutes to start, environments aren’t preserved, idle sessions waste money, and you’re stuck on oversized GPU instances. Modal Notebooks removes these points of friction, so you can focus on cutting-edge work.

After a limited beta last month, Notebooks are now generally available to all Modal customers.

## A better way to iterate on code and research

 “Modal Notebooks have been incredible for sharing ML research across Suno. Engineers and designers can start playing with cutting-edge models within minutes after training runs are completed.” — Victor Tao, ML Research Engineer [

](https://suno.com/) Today, tens of millions of end-users interact with applications built on Modal, from AI-generated music at [Suno](https://suno.com/), to payments at [Ramp](https://ramp.com/), to consumer apps like [Lovable](https://lovable.dev/) and [Substack](https://substack.com/).

Notebooks represent a new way to develop with Modal. They are designed for research and experimentation—not just writing code, but *rapidly developing and refining ideas* with your team. We believe this process is an important part of AI development and deserves equally good tooling as full-scale production workflows.

Features include:

- **Fast time-to-first-cell.** Cold-start to ready in *less than 5 seconds*, on arbitrary container images and hardware ranging up to 256 vCPUs and 8 H100/B200 GPUs. Switch GPU type just as easily.
 - **No zombie boxes.** Kernels auto-idle and resume, so you only pay for when they’re running (configurable if you need control).
 - **One environment.** Access the same Volumes (distributed storage), Secrets, and deployed Functions as the rest of your Modal Apps.

Modal has already redefined how teams run and scale jobs in production. Notebooks aim to bring our core developer experience principles to the exploratory side of AI work.

## What you can do

### Start instantly. Scale on demand.

Run from as little as **0.125 CPUs** up to **8 Nvidia A100/H100/B200 GPUs**.

*With CPU, you can also burst above configured resource usage and only pay for active compute cycles.*

Bring a **custom image** or work from a curated AI base image.

*Modal’s content-addressed FUSE filesystem caches packages and loads them on demand, so kernels boot quickly even with large images.*

Automatic idle-shutdown with fast resume (manual control is also available).

### Work together in real time

- Multiple cursors, live presence, and seamless collaborative editing.

### Use your Modal stack, directly

Attach **Volumes** (persistent storage) and **Secrets** from the UI; browse files inline or upload them via drag-and-drop. Volumes can store terabytes of data with relaxed consistency and are multi-writer accessible from around the world.

![](https://modal-cdn.com/nb-assets-sept-8/filesystem-viewer.png)

**Call Modal Functions** from any cell without extra authentication.

Reuse the **same images and runtime primitives** you already deploy in production.

### Modern dev experience (LSP + AI)

- **Pyright** language server for completions, types, and diagnostics.
 - **AI completions** when you’re exploring what to try next.
 - Rich HTML outputs for plots/media in libraries like Altair, Seaborn, Plotly, and py3Dmol.

## Industry usage of Notebooks

During our short beta in August, **over 5,000 accounts** adopted Notebooks in their daily workflows, running **200,000 code cells** with instant startup and real-time collaboration. Early adopters included leading AI research and product startups—teams that need to move quickly from training to production.

Here’s what some of them had to say:

 “Testing different GPUs on the fly has massively accelerated our workflow for profiling models. Tasks that used to take days now take minutes.” — Simran Makariye, ML Engineer [

](https://sync.so/) “Other platforms like Colab didn't have the capacity we needed. We love how Modal Notebooks lets us scale up any amount of GPUs and compute.” — Arda Göreci, Co-founder &amp; CTO [](https://ligo.bio/) “Honestly, one of the best experiences I’ve had for casual and exploratory coding. The ability to live-swap hardware specs—including top-tier GPUs, and even multiple ones—is next-level. Super smooth and really fun to use.” — Stefano Giomo  “We used to spend hours just setting up access and dealing with surprise costs. With Modal Notebooks, I set up a research environment for our intern and could give feedback on his experiment in real time.” — Alice Yu, Co-Founder &amp; CEO @ OncoCardia  And while today marks general availability, we’re already thinking ahead. Upcoming features include:

- **Memory snapshots** to suspend and later resume execution, while preserving variables and files.
 - **One-click export** of notebook code into Modal Apps.
 - **Scheduled runs and edit history** for better reproducibility.

## Try it today, with $30 free credits

For the Modal team, Notebooks have become our default surface for experiments and collaborative work. Our hope is that their speed, usability, and compute flexibility enable researchers to work together and bring simpler, better products into the world.

Check out some of our featured examples:

 [

 Whisper Audio Analysis Transcribe audio with OpenAI's Whisper, and visualize how it attends to different parts of the input via attention weights over time.](/notebooks/modal-labs/_/nb-Ld85WlrVtJTiLWpB5l469e)[ Run Claude Code in a Modal Sandbox Build your own coding agent that can run securely in a Modal Sandbox and analyze a custom GitHub repository.](/notebooks/modal-labs/_/nb-30WInxiigR3Wc8kQ3jU7Hr)[ Exploring Qwen3 on vLLM Run a fine-tuned open source code generation model. Compare code quality, analyze token patterns, and experiment with different prompts.](/notebooks/modal-labs/_/nb-KCjgUBAf1S99LafrrONNZ7)[ Parse Documents with dots.ocr Extract and analyze text from images and PDFs, using the state-of-the-art OCR model based on LLM foundations.](/notebooks/modal-labs/_/nb-8wvXoGoAcba8sRF8VkVg18)[ UMAP Embeddings Visualization Visualize high-dimensional embeddings in 2D/3D space. Explore semantic similarity, cluster data, and understand vector representations.](/notebooks/modal-labs/_/nb-qAEQwvMr1LSvedsywD28od) [See the docs](https://modal.com/docs/guide/notebooks) for more, or [send us feedback on Slack](https://modal.com/slack).