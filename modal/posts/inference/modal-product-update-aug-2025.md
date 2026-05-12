---
title: "Product updates: GPU memory snapshots, notebooks, service tokens, and more"
author: "Unknown"
date: "2025-08-11"
url: "https://modal.com/blog/modal-product-update-aug-2025"
category: "inference"
site: "modal"
---

# Product updates: GPU memory snapshots, notebooks, service tokens, and more

## 📸 GPU Memory Snapshots (Alpha)

 ![](https://modal-cdn.com/cdnbot/gpu-snapshotuvmsrmbr_370c7551.webp)

We’ve brought the magic of memory snapshots to GPUs on Modal! You can now enjoy 10x faster cold boots for GPU workloads by skipping expensive steps like Torch compilation. If you’re already using memory snapshots, just add the `enable_gpu_snapshot` experimental option to get started.

Check out our [blog post](https://modal.com/blog/gpu-mem-snapshots) for more info.

## 📓 Introducing Modal Notebooks (Beta)

![](https://modal-cdn.com/notebooks.gif)

To get started, open [modal.com/notebooks](https://modal.com/notebooks) in your browser, or [check out our docs](https://modal.com/docs/guide/notebooks).

## 🤖 Service Tokens

![](https://modal-cdn.com/cdnbot/service-userslgl14v49_d1e2c6ba.webp)

Modal workspace managers can now create Service Users that have their own API tokens. This makes it easy to automate deploys of Modal apps without relying on a specific member’s tokens.

More details in our docs [here](https://modal.com/docs/guide/service-users)!

## 🏃 Run Modal Functions from the browser (Beta)

![](https://modal-cdn.com/cdnbot/UI-for-Functionsampu2p7y_025374bd.webp)

Modal now generates a UI for your Function based on its type annotations! Use it for easier testing and debugging, or as a user-friendly way to trigger internal workflows.

*Note: App has to be deployed with `modal` client version 1.1 or later, and all function arguments need to have type annotations specified*

## 🧩 First-class Support for uv

![](https://modal-cdn.com/cdnbot/uv-install0ye1cftd_c71c9e91.webp)

Make your container builds even faster on Modal with [uv](https://github.com/astral-sh/uv). Use `uv_sync` to sync your Modal image with your local project and `uv_pip_install` to install packages lightning fast.

Read more about it in our [changelog](https://modal.com/docs/reference/changelog#110-2025-07-17).

## **👩‍💻 Client updates**

Run `pip install --upgrade modal` to get the latest client updates. Here’s some highlights from the [changelog](https://modal.com/docs/reference/changelog):

- Introduced the concept of “named Sandboxes” for use cases where Sandboxes need to have unique ownership over a resource ([1.1.1](https://modal.com/docs/reference/changelog#111-2025-08-01))
 - Added a `.name` property and `.info()` method to to `modal.Dict` , `modal.Queue` , `modal.Volume` , and `modal.Secret` objects ([1.1.1](https://modal.com/docs/reference/changelog#111-2025-08-01))
 - Introduced support for the `2025.06` [Image Builder Version](https://modal.com/docs/guide/images#image-builder-updates) ([1.1.0](https://modal.com/docs/reference/changelog#110-2025-07-17)). These improvements should greatly reduce the risk of conflicts with user code dependencies. They also allow Modal Sandboxes to easily be used with existing Images or Dockerfiles that are not themselves compatible with the Modal client library.

## 🏎️ **Run OpenAI’s gpt-oss model with vLLM**

![](https://modal-cdn.com/cdnbot/gpt-oss_newz4tlhs5i_8c37cbd7.webp)

With our new gpt-oss example, you can deploy OpenAI’s new open-weight reasoning model on Modal in minutes using vLLM. Check it out [here](https://modal.com/docs/examples/gpt_oss_inference)!

## 🔉 **Transcribe a week of audio in a minute for a dollar**

![](https://modal-cdn.com/cdnbot/audio-blog7pf9gnr1_724887c6.webp)

ICYMI, open speech-to-text models are really good now. Learn how to deploy an audio transcription service that is over 100x faster or 100x cheaper than proprietary APIs in our blog post [here](https://modal.com/blog/fast-cheap-batch-transcription).

## ❤️ Customer spotlights: Lovable, Marimo, Pipecat

 - [Marimo](https://marimo.io/), an open-source Python notebook, [launched](https://x.com/marimo_io/status/1946271211841007970) their cloud-hosted notebook workspace on Modal Sandboxes.
 - [Pipecat](https://github.com/pipecat-ai/pipecat), an open-source real-time voice AI framework, [trained](https://x.com/kwindla/status/1946267669638046010) their new turn detection model on Modal.

## 📅 Recent events

- We recently hosted 100+ builders at a Voice AI event with [Daily](https://www.linkedin.com/company/dailyco/), featuring a panel with researchers at [NVIDIA](https://www.linkedin.com/company/nvidia/) and [Mistral AI](https://www.linkedin.com/company/mistralai/) building state-of-the-art speech models. Missed it? Watch the livestream [here](https://www.youtube.com/watch?v=-YOB_N6SGss)!

![](https://modal-cdn.com/cdnbot/voice-ai-eventdqurq2k1_6c5ae38e.webp)