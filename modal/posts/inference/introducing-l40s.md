---
title: "Introducing: L40S GPUs on Modal"
author: "Unknown"
date: "2024-12-19"
url: "https://modal.com/blog/introducing-l40s"
category: "inference"
site: "modal"
---

# Introducing: L40S GPUs on Modal

  At Modal, we believe that [AI inference has unique infrastructure needs](https://modal.com/blog/the-future-of-ai-needs-more-flexible-gpu-capacity).

The L40S can offer substantial performance benefits over our current most popular inference-focused accelerator, the [NVIDIA A10 GPU](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a10/pdf/a10-datasheet.pdf).

## Run bigger models with the L40S

At 48GB, the L40S has twice the on-device DDR6 random access memory of the A10.

That means you can run larger models on large inputs. For example, [running Flux.1-schnell](https://modal.com/docs/examples/flux) in 16bit precision consumes 24 GB of RAM just for model weights, so it cannot run on a single A10 GPU without a throughput-killing offload to CPU RAM. Trying to do so will trigger a dreaded CUDA OOM:

![](https://modal-cdn.com/cdnbot/tmp0d4e4yb7_a972858f.webp)

But the same workload fits very comfortably in a single L40S!

![](https://modal-cdn.com/cdnbot/tmp2gewl_pt_3056472b.webp)

## Run inference faster with the L40S

The L40S is also faster than the A10, not just beefier.

Users can expect approximately a 40% speedup for memory-bound jobs like small-batch inference and well over a 100% speedup for compute-bound jobs using 16bit [Tensor Cores](https://modal.com/docs/gpu-glossary/device-hardware/tensor-cores). *Without any tuning*, we were able to achieve a 20% speedup in a [basic load test](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/llm-serving/openai_compatible/load_test.py) for a chat-style workload.

![](https://modal-cdn.com/l40s-benchmark.svg)

## A10 vs L40S specs

See the table below for a comparison of the features of the A10 and the L40S, adapted from the manufacturer datasheets. If any of the vocabulary is new to you, click the link to be taken to our new [GPU Glossary](https://modal.com/gpu-glossary) for an explanation.

 [A10](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a10/pdf/a10-datasheet.pdf)[L40S](https://resources.nvidia.com/en-us-l40s/l40s-datasheet-28413?ncid=no-ncid) [Streaming Multiprocessor Architecture](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)AmpereAda Lovelace[Compute Capability](https://modal.com/gpu-glossary/device-software/compute-capability)8.68.9[GPU RAM](https://modal.com/gpu-glossary/device-hardware/gpu-ram)24 GB DDR648 GB DDR6[GPU RAM](https://modal.com/gpu-glossary/device-hardware/gpu-ram) ↔ [Streaming Multiprocessor](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor) Memory Bandwidth600 GB/s864 GB/sFP16/BF16 [Tensor Core](https://modal.com/gpu-glossary/device-hardware/tensor-core) Arithmetic Bandwidth125 TFLOP/s362 TFLOP/sFP8 [Tensor Core](https://modal.com/gpu-glossary/device-hardware/tensor-core) Arithmetic BandwidthN/A733 TFLOP/s

## Get started now

Modal is the easiest way to deploy code to GPUs. Our custom infrastructure allows us to spin up L40S (or other GPU) containers running your code in one second. We help you efficiently autoscale your workloads to hundreds of GPUs, and you only ever pay for what you use.

Modal also comes with $30/month in free compute, so you can try an L40S for free right now. Just [sign up for Modal](https://modal.com/signup) if you haven’t yet, install and authenticate with our [Python SDK](https://modal.com/docs/guide), and then decorate a Python function with `app.function(gpu="L40S")`: