---
title: "Product updates: Modal Notebooks, sandbox idle timeouts, and more"
author: "app"
date: "2025-09-19"
url: "https://modal.com/blog/modal-product-update-sep-2025"
category: "sandboxes"
site: "modal"
---

# Product updates: Modal Notebooks, sandbox idle timeouts, and more

## 📓 Modal Notebooks

 ![](https://modal-cdn.com/notebooks.gif)

To get started, open [modal.com/notebooks](https://modal.com/notebooks) or read more [here](https://modal.com/blog/notebooks).

## ⌛ Sandbox Idle Timeouts

You asked, we listened. Users are now able to provide an optional `idle_timeout` parameter to `modal.Sandbox.create()`. When provided, Sandboxes will terminate after a specified number of seconds of idleness.

More details in our docs [here](https://modal.com/docs/guide/sandbox#idle-timeouts)!

## 👩‍💻 Client updates

Run `pip install --upgrade modal` to get the latest client updates. Here are some highlights from the [changelog](https://modal.com/docs/reference/changelog):

Added a `startup_timeout` parameter to the  `@app.function()`  and  `@app.cls()`  decorators. When used, this configures the timeout applied to each container’s startup period separately from the input `timeout` ([1.1.4](https://modal.com/docs/reference/changelog#114-2025-09-03))

![](https://modal-cdn.com/blog/images/codesnippet.webp)

Introduced a new API pattern for imperative management of Modal resource types (`modal.Volume`, `modal.Secret`, `modal.Dict`, and `modal.Queue`) ([1.1.2](https://modal.com/docs/reference/changelog#112-2025-08-14))

## ❤️ Customer spotlight: Zencastr

![](https://modal-cdn.com/cdnbot/zencastrn3sp9dci_3f74463d.webp)

## 🏎️ GPU Performance Glossary

![](https://modal-cdn.com/cdnbot/gpuperformanceglossarytw46908y_d5f5fab0.webp)

For GPUs and their applications, performance is the product. That’s why we extended our popular “CUDA docs for humans”, the GPU Glossary, with a [new section on performance](https://modal.com/gpu-glossary/perf). We cover everything from [warp divergence at the assembler level](https://modal.com/gpu-glossary/perf/warp-divergence) to [memory-bound LLM inference napkin math](https://modal.com/gpu-glossary/perf/memory-bound) to [the roofline model from quantitative computer architecture](https://modal.com/gpu-glossary/perf/roofline-model).

Read it [here](https://modal.com/gpu-glossary/perf).

## 🦥 Finetune an LLM with Unsloth

[Unsloth](https://unsloth.ai/) provides optimized methods for LLM finetuning with LoRA and quantization, leading to 2x faster training with 70% less memory usage. Learn how to use Unsloth to finetune a version of Qwen3-14B with the FineTome-100k dataset on Modal using only a single GPU! Check it out [here](https://modal.com/docs/examples/unsloth_finetune)!

## 🗣️ Finetune an ASR model with Whisper

In this example, we demonstrate how to fine-tune OpenAI’s [Whisper](https://huggingface.co/openai/whisper-tiny.en) model to improve transcription accuracy. Learn how to fine-tune and deploy the model on Modal [here](https://modal.com/docs/examples/fine_tune_asr)!

## 📅 Upcoming events

![](https://modal-cdn.com/blog/images/biotech.webp)

Seats are limited: [RSVP here](https://luma.com/1xfz2u2o)

![](https://modal-cdn.com/cdnbot/vapiconssjxprls_f1ba7bc0.webp)

- We’re headed to [Vapicon](https://luma.com/vapicon2025) in SF on Thursday, October 2! Catch Modal co-founder Erik Bernhardsson on the *Voice AI Infrastructure: How to Scale and Achieve 99.999?* panel at 3:10pm. Snag 20% off your ticket with code “BERNHARDSSON20”
 - We are also hosting an intimate, invite-only Voice AI dinner after the conference with Daily and Rime. Register [here](https://luma.com/ckh9cabs).

### 🍭 Other fun tidbits

- Interested in the secret sauce that makes Modal so fast? One of our investors, Amplify, did a deep dive of Modal in a recent [blog post](https://www.amplifypartners.com/blog-posts/how-modal-built-a-data-cloud-from-the-ground-up) and [interview](https://www.youtube.com/watch?v=pLBxrY8RX6w).