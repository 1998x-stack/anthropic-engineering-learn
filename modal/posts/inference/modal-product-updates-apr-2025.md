---
title: "Product updates: Running batch jobs with 1M inputs, ephemeral apps, and a new TensorRT-LLM example"
author: "Unknown"
date: "2025-04-17"
url: "https://modal.com/blog/modal-product-updates-apr-2025"
category: "inference"
site: "modal"
---

# Product updates: Running batch jobs with 1M inputs, ephemeral apps, and a new TensorRT-LLM example

## 🍩 Run async jobs with 1M inputs

 ![](https://modal-cdn.com/cdnbot/async-batchpw6jrz3o_3cc440c6.webp)

Running large-scale async jobs on Modal just got a whole lot easier:

- You can now queue up to **1 million inputs** per Modal Function (previously 2k).
 - We’ve also raised the `.spawn()` rate limit so you can submit inputs more quickly.
 - `FunctionCall` results now stick around for **7 days**, giving you more flexibility to retrieve them when you’re ready.

Want to try job processing on Modal? [Check out the guide
→](https://modal.com/docs/guide/job-queue)

## 👩‍💻 Client updates

Run `pip install --upgrade modal` to get the latest client updates.

- Modal Client v1.0 is on the way! Expect cleaner APIs and some deprecation warnings — check out our [Migration Guide](/docs/guide/modal-1-0-migration) to prep your code.
 - You can now launch [ephemeral apps](/docs/guide/apps#ephemeral-apps) from within containers using `with app.run():`. Avoid putting this in global scope to prevent recursion.
 - Use `context_dir` to make relative `COPY` commands in [Dockerfiles](/docs/reference/modal.Image#from_dockerfile) work more
reliably.
 - Use `Image.cmd(...)` to [define default entrypoint args](/docs/reference/modal.Image#cmd) for your Docker images.
 - You can [now see Git commit info for apps](/docs/reference/cli/app#modal-app-history), both in the CLI via `modal app history`, and in the dashboard.

![](https://modal-cdn.com/cdnbot/app-historyje7pox6y_7a049cc5.webp)

## 🖊️New super fast LLM inference example with TensorRT-LLM

Check out our [new
example](https://modal.com/docs/examples/trtllm_latency#serve-an-interactive-language-model-app-with-latency-optimized-tensorrt-llm-llama-3-8b) showing how to serve large language models with ultra-low (less than 400 ms) latency
using [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) on Modal. Perfect
for real-time applications.

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/example-trtllm-latency-ezgif.com-video-to-gif-converter+(2).gif)

## 📽️ Video walkthroughs

Want to see Modal in action? We dropped two new walkthroughs:

- **Deploy DeepSeek models on Modal** — A step-by-step guide to spinning up DeepSeek in production. [Watch the video →](https://www.youtube.com/watch?v=HrFAlcAZ0Mk)
 - **Serve OpenAI-compatible APIs with vLLM** — Learn how to deploy and scale a blazing-fast vLLM service on Modal. [Watch the video →](https://www.youtube.com/watch?v=gh-JizAs-jY)

## 🚀 Customer launches

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/sculptor-social-ar+(2).gif)

- [Imbue](https://imbue.com/) launched [Sculptor](https://imbue.com/product/sculptor/), the first coding agent environment that helps you catch issues, write tests, and improve your code, built on Modal Sandboxes.
 - [Phonic](https://phonic.co/) launched their new voice AI platform, with Modal
enabling low-latency inference and massively parallel job processing.
 - [Firebender](https://firebender.com/blog/kotlin-bench) launched [Kotlin-bench](https://github.com/Kotlin/kotlinx-benchmark), the first benchmark evaluating AI models on real-world Kotlin &amp; Android tasks, using Modal’s `.map()` for large-scale parallelization.

## 🍭 Fun tidbits

- We were named the #2 most promising early-stage company on the [2025 Enterprise Tech 30 list by Wing VC and Eric Newcomer](https://www.enterprisetech30.com/).

![](https://modal-cdn.com/cdnbot/enterprise-listx_wud907_76896579.webp)

- We had some amazing demos at our open-source LLM demo night (hosted jointly with Mistral), from blazing fast speech-to-speech to domain-specific agent evals.

![](https://modal-cdn.com/cdnbot/modal-mistral4v0mlwkf_eab78885.webp)

- We launched our first billboard campaign in SF! Anyone who finds and tweets a photo of our billboards gets a little prize.

![](https://modal-cdn.com/cdnbot/billboard-imagemxfu0ae6_a7e0a4a2.webp)