---
title: "Introducing: B200s and H200s on Modal"
author: "Unknown"
date: "2025-05-30"
url: "https://modal.com/blog/introducing-b200-h200"
category: "inference"
site: "modal"
---

# Introducing: B200s and H200s on Modal

  It [never](https://x.com/modal/status/1592915154207133699) [gets](/blog/introducing-l40s) [old](/blog/introducing-h100): we are pleased to announce that the most powerful GPUs on the market are now available on Modal.

No “contact sales” button or asking for quota. B200s and H200s are accessible to anyone with a Modal account. It’s a one-liner to add them to any Modal Function.

B200s are priced at $6.25/hour, and H200s are priced at $4.54/hour.

## What are the specs of the B200 and H200 GPUs?

Comparing the B200s and H200s with H100s, we can see how much more powerful these new GPUs are.

 [B200](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)[H200](https://nvdam.widen.net/s/nb5zzzsjdf/hpc-datasheet-sc23-h200-datasheet-3002446)[H100](https://resources.nvidia.com/en-us-hopper-architecture/nvidia-tensor-core-gpu-datasheet) [Streaming Multiprocessor Architecture](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)BlackwellHopperHopper[GPU RAM](https://modal.com/gpu-glossary/device-hardware/gpu-ram)180 GB141 GB80 GBGPU RAM ↔ [Streaming Multiprocessor](https://modal.com/gpu-glossary/device-hardware/streaming-multiprocessor) Memory Bandwidth8 TB/s4.8 TB/s3.5 TB/sFP4 [Tensor Core](https://modal.com/gpu-glossary/device-hardware/tensor-core) Arithmetic Bandwidth9 PFLOP/sn/an/aFP8 Tensor Core Arithmetic Bandwidth5 PFLOP/s2 PFLOP/s2 PFLOP/s

## How do I interpret B200 and H200 GPU specs?

Both B200s and H200s have more on-device memory than their predecessors. B200s have 180GB of HBM3e on-device memory (aka VRAM)—2.25x the storage of an H100. That leaves more space for the weights and caches of large Mixture-of-Experts (MoE) models like DeepSeek-R1, Qwen 3, and LLaMA 4. Some of these models are so large they can’t be deployed on a single node, even with 8 H100s, but they fit comfortably on 8 H200s or 8 B200s.

Note also that B200s have 8 TB/s of memory bandwidth to the Hopper GPUs’ ~4 TB/s. That means you can get bits into and out of their more capacious memory and into the compute units at twice the rate. Memory-bound workloads like chatbot inference will typically see a >2x latency decrease moving from H100s to B200s—without any changes to inference code, just infrastructure.

The new Blackwell architecture also introduces native support for 4-bit floating point operations in the Tensor Cores, resulting in a ~4x speedup over the native 8-bit floating point matrix math supported by Hopper GPUs. This simultaneously reduces contention for memory bandwidth (great for memory-bound workloads) and capacity while increasing arithmetic bandwidth (great for compute-bound workloads).

## What are the performance gains for B200s over H200s and H100s?

Many workloads will see an immediate speedup between 2x and 4x when migrated from H100s to B200s. But the full performance benefits of B200s in particular will take some time to realize. For example, the popular open source LLM serving engine vLLM just stabilized support for Blackwell GPUs in [version 0.9](https://github.com/vllm-project/vllm/releases/tag/v0.9.0), released on Tuesday. And achieving the peak performance promised by the hardware will take even more work.

Despite that, we’ve already seen big gains in our early testing for some workload types!

Below is one popular workload where our benchmarking showed significant gains for latency and throughput on B200s vs H200s. We used the latest version of vLLM to run the DeepSeek V3 Large Mixture-of-Experts Language Model in its native 8-bit precision to process 1000 tokens (about one page of text) as input and generate 128 tokens (e.g. a summary paragraph) as output. This model is too large to run on an 8xH100, but we benchmarked it on an 8xH200 and an 8xB200 on Modal.

- At 1 request per second, the median time-to-first-token is 2.5x faster on the B200s vs H200s.
 - At a median time-to-first-token of 1 second, queries-per-second is 1.7x higher on the B200s vs H200s.

![](https://modal-cdn.com/blog/images/benchmarks-h200-b200.webp)

You can run vLLM on Modal B200s with [this code sample](/docs/examples/gpt_oss_inference).

As open-source engines release new optimizations, we expect to see further performance gains—and we’ll be here to [explain](/docs/examples/trtllm_latency) how you can make use of them on Modal!

## Why Modal for B200s and H200s?

Modal is the easiest way to deploy code to GPUs with no reservations or commitments. Our custom infrastructure allows us to spin up GPU containers running your code in less than a second. We help you efficiently autoscale your workloads to hundreds of GPUs, and you only ever pay for what you use.

Modal also comes with $30/month in free compute, so you can try B200s or H200s for free right now! [Sign up](/signup) today to get started.