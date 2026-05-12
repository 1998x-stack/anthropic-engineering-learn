---
title: "Dogfooding Modal: What we learned at our internal hackathon"
author: "Unknown"
date: "2024-12-09"
url: "https://modal.com/blog/modal-hackathon"
category: "training-finetuning"
site: "modal"
---

# Dogfooding Modal: What we learned at our internal hackathon

  This fall, we went to Ericeira, Portugal for our company offsite.

 ![](https://modal-cdn.com/cdnbot/tmp1pjn1jfr_043d4557.webp) ![](https://modal-cdn.com/cdnbot/offsite-erik5mo8pq3g_faca6511.webp)

One of the highlights was an internal hackathon. The 30 of us split into 13 different teams and hacked on projects across AI agents, real time translation, and music. The only constraint was that the project had to use Modal in some way.

## Browserman

The Browserman team built a multi-modal AI agent app that, given a task, navigates the internet and uses purely visual information to complete the task. For example, when asked to “reorder my favorite order from Domino’s”, Browserman is able to autonomously find the Domino’s website and click through ads and buttons to satisfy the request:

Browserman was built with [Llama-3.2-90B-Vision-Instruct-FP8](https://huggingface.co/neuralmagic/Llama-3.2-90B-Vision-Instruct-FP8-dynamic), [vLLM](https://blog.vllm.ai/2023/06/20/vllm.html), Playwright, and [Modal’s distributed Queues](/docs/guide/queues). We were about to pivot the company before it got scooped by Anthropic’s [Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use) which was released one week after our hackathon :).

## Glodal

The Glodal team built a beautiful real-time app visualizing how a Modal client request traverses the globe to our us-east control plane and to our workers distributed across the US, Europe, and Asia. Controlling [region selection](/docs/guide/region-selection) of workers is one of our most popular features.

The Glodal team also implemented a prototype of a **distributed control plane** and demonstrated how it can drive down latency by 100x. In the visualization below, compare the path of a Modal client request from a single us-east control plane (red) to a distributed control plane (green):

![](https://modal-cdn.com/cdnbot/glodal-screenshotsnrasei5_616fd778.webp)

This example simulates an eu-west client kicking off a Modal job requesting eu-west containers. On our existing single us-east control plane setup:

- The eu-west client sends a transatlantic request to Modal’s us-east control plane
 - The Modal control plane sends another transatlantic request to kick off workers in eu-west

Using Glodal’s distributed control plane, all communication stays within the continent, driving down overall latency from 268ms to 3ms. This project helped validate the benefits we would get from a distributed control plane, and we’re now working on building that into the platform.

Here’s a full video showing even more examples of how a Modal request traverses the globe:

## Waluigi

Before Modal, Erik Bernhardsson and Elias Frieder built [Luigi](https://github.com/spotify/luigi), one of the first modern workflow orchestrators that changed how we manage complex batch processing pipelines. The idea for the Waluigi team was simple: support Modal as a worker type for a Luigi workflow.

Below is a visualization of a Luigi DAG running several Modal tasks in parallel:

![](https://modal-cdn.com/cdnbot/hackathon_2sa26_2_4c2e5643.webp)

The combination of a workflow scheduler like Luigi with Modal’s cloud functions is a very powerful batch processing system that supports:

- autoscaling to maximize parallelism in DAG execution
 - configuring each DAG job type with its own hardware requirements, including GPUs
 - orchestrating dependencies, work distribution, and partial retries

## pytest-modal

The pytest-modal team built a pytest plugin that parallelizes test suites on Modal. Each test runs in its own container, taking advantage of Modal’s ability to fan out batch jobs and handle bursty workloads. They were able to shorten test suite runtime from minutes to seconds:

## Conclusion

At the end of the hackathon presentations, everyone left feeling incredibly impressed by the quality and creativity of what their teammates were able to accomplish in such a short amount of time.

![](https://modal-cdn.com/cdnbot/erik-slacksfd_2jee_e82e7776.webp)

It was a great reminder of what excited us all about Modal in the first place: its ability to turbo charge developer productivity across diverse use cases in AI, arts, and the overall software lifecycle.

![](https://modal-cdn.com/hackathon2024/team.gif)

 The Modal team over time