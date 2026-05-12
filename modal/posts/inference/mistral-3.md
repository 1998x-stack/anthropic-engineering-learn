---
title: "Modal + Mistral 3: 10x faster cold starts with GPU snapshotting"
author: "Unknown"
date: "2025-12-02"
url: "https://modal.com/blog/mistral-3"
category: "inference"
site: "modal"
---

# Modal + Mistral 3: 10x faster cold starts with GPU snapshotting

  ![](https://modal-cdn.com/blog/images/mistral-3-vllm-cold-start-ecdf.png)

Today, [Mistral](https://mistral.ai/) launched Mistral 3, a family of open models with frontier-class performance, customization capabilities, and trusted transparency. We’re proud to offer Day 0 support for running these models on Modal.

Modal enables developers to instantly deploy and scale Mistral 3 models without orchestrating compute infrastructure. Beyond a great DevEx and abundant GPU capacity, Modal also offers cutting-edge features like GPU memory snapshotting that can reduce median cold start time for some of these models by almost 10x, from almost two minutes to just ten seconds.

## About Mistral 3

Mistral 3 is the newest frontier open model family from Mistral. It is a suite of multimodal models with strong multilingual support, and it is available in multiple sizes and capabilities for max flexibility.

This blog post focuses on Ministral 3, whose size is well-suited for Modal’s serverless infrastructure. Ministral 3 is the small version of the Mistral 3 family of models and is available in 3B, 8B, and 14B sizes. It performs competitively with the Qwen 3-VL model series [on benchmarks](https://huggingface.co/collections/mistralai/ministral-3-more). This makes Ministral 3 well-suited for companies that are seeking a balance of intelligence and compute efficiency.

## Quickstart

Follow [this sample code in our docs](/docs/examples/ministral3_inference), which uses [vLLM](https://vllm.ai) to serve Ministral 3.

Install Modal, [clone our examples repo](https://github.com/modal-labs/modal-examples), and then run the example:

See the example text for details on deployment with `modal deploy`.

## How it works

The basic example above takes advantage of several key Modal features:

- [Serverless GPUs](/docs/guide/gpu) that automatically scale up and down from 0 based on request volume to the vLLM server.
 - [Volumes](/docs/guide/volumes), Modal’s native, distributed file system, to cache model weights and compilation artifacts from vLLM.
 - [Python-defined infrastructure](/docs/guide/images) to keep environment and hardware requirements cleanly in sync with application code.

Together, these features allow developers to deploy Mistral 3 without being blocked on acquiring GPU quota or managing complex configuration surface areas.

## Now, speed up cold starts by almost 10x

Modal recently launched a new [GPU snapshotting](/docs/guide/memory-snapshots) feature in alpha. This can drastically reduce cold starts for workloads that require heavy initialization work—like spinning up a vLLM server.

We tested this on the 3B version of Ministral 3 and saw an almost 10x reduction in median cold start time, from ~118s to ~12s. Drastically shorter cold starts means you can deploy Ministral 3 in a way that is both cost-efficient and responsive to user demand.

### vLLM + Ministral 3 3B

   Cold start time (with snapshots) Cold start time (baseline)

To use this feature, you must enable Sleep Mode for your vLLM server and set `experimental_options={"enable_gpu_snapshot": True}` in your Modal App. The first time the vLLM server finishes initializing, it will be put to sleep. This shifts most of the contents of GPU memory to CPU memory, which facilitates the snapshotting process. Upon subsequent starts, the vLLM server is restored from this snapshot.

Try it out for yourself by deploying the code sample [here](https://github.com/modal-labs/modal-examples/blob/main/06_gpu_and_ml/llm-serving/ministral3_inference.py).