---
title: "Product Updates: L40Ss, proxy auth tokens, and Sandbox disk snapshotting"
author: "app"
date: "2025-01-21"
url: "https://modal.com/blog/modal-product-updates-jan-2025"
category: "inference"
site: "modal"
---

# Product Updates: L40Ss, proxy auth tokens, and Sandbox disk snapshotting

## 🚀 Introducing L40S GPUs

 NVIDIA L40S GPUs are [now available](/blog/introducing-l40s) on Modal at $1.95/hr! With 48GB of DDR6 RAM and impressive CUDA and Tensor Core performance, the L40S offers significant advantages over our popular A10 GPUs:

- 2x more memory for running larger models and longer contexts
 - Up to 40% faster for memory-bound tasks
 - Over 100% speedup for compute-bound jobs using 16bit Tensor Cores

Try it now by adding this decorator to your function: `@app.function(gpu="L40S")`

![](https://modal-cdn.com/l40s-benchmark.svg)

## 🔒 Proxy Auth Tokens

Modal now supports [Proxy Auth tokens](/docs/guide/webhook-proxy-auth) for authenticating access to web endpoints! This means you can gate access to web endpoints and prevent unwanted usage from incurring charges.

## 📷 File System API and Disk Snapshotting for Sandboxes

The new [Filesystem API](/docs/guide/sandbox-files) makes it seamless to read and write files in your Sandbox, and is especially good for getting files in and out of a Sandbox interactively.

We are also introducing [disk](/docs/guide/sandbox-snapshots) capabilities for Sandboxes, expanding on our existing function snapshotting feature. This enables you to:

- Create snapshots of your Sandbox’s entire state
 - Branch off from any snapshot to create new Sandbox instances
 - Eliminate cold-start times by restoring from snapshots

## 👩‍💻 Client Updates

Run `pip install --upgrade modal` to get the latest updates. Here are some of the highlights:

- **Images:** When using `Image.from_dockerfile()` or `image.dockerfile_commands()`, the system will now automatically look for and use a `.dockerignore` file.
 - **Images:**`FilePatternMatcher` has a [new constructor](/docs/reference/modal.FilePatternMatcher#from_file) `from_file` which allows you to read file matching patterns from a file instead of having to pass them in directly.
 - **Volumes:** Modal Volumes can now be [renamed](/docs/reference/cli/volume#modal-volume-rename) via the CLI (`modal volume rename`) or SDK (`modal.Volume.rename`).
 - **Sandboxes**: Sandboxes now support `fsnotify-like` file watching and accept larger write payloads up to 1 GiB
 - **Environment:** The`App.run` context manager has a new `environment_name` [parameter](/docs/reference/modal.App#run).
 - **VSCode:** You can now point `modal launch vscode` at an arbitrary Dockerhub base image:

`modal launch vscode --image=nvidia/cuda:12.4.0-devel-ubuntu22.04`

## 🔐 SOC 2 Type 2 Certification

We’re pleased to announce [the completion of our SOC 2 Type 2 certification](/blog/soc2type2). If you would like to see the report or have more questions, please email [security@modal.com](mailto:security@modal.com).

## 📚 GPU Glossary

![](https://modal-cdn.com/cdnbot/gpu-glossary-streaming-multiprocessor48kg_mtn_a0e1fe04.webp)

We work a lot with GPUs, and if you do too you probably know how hard it can be to find the information you need in the public documentation. So we put together a handy [GPU Glossary](https://modal.com/gpu-glossary) that collects together quick explanations and high-quality resources for everything from Tensor Cores and Warp Schedulers to Compute Capabilities and the CUDA Toolkit.

## 🧬 New computational bio, OCR, and image diffusion resources

![](https://modal-cdn.com/cdnbot/e3m3-predicted-structureihuxe_c3_90f6339f.webp)

- **ESM3**: recent model from Evolutionary Scale that can not only predict protein structures from sequences but also generate new proteins. [Protein folding dashboard example on Modal](/docs/examples/esm3).
 - **GOT:** a 580M parameter OCR model that can better handle a variety of content formats. [Example on Modal](/docs/examples/doc_ocr_jobs).
 - ICYMI, we hosted a webinar recently covering best practices on productionizing diffusion models. [Here’s the video](https://www.youtube.com/watch?v=iiuFht5VhGg).

## 🍭 Fun Tidbits

- We’ve been hosting exclusive dinners for biotech founders and engineers! Reach out if you’d like to join our next one.