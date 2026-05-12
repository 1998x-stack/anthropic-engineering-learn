---
title: "Modal + Datalab: Deploy high-throughput document intelligence in &lt;5 minutes"
author: "Unknown"
date: "2025-10-29"
url: "https://modal.com/blog/datalab-and-modal"
category: "inference"
site: "modal"
---

# Modal + Datalab: Deploy high-throughput document intelligence in &lt;5 minutes

  We’re excited to collaborate with [Datalab](https://www.datalab.to/), creators of [Marker](https://github.com/datalab-to/marker) and [Surya](https://github.com/datalab-to/surya), to make it faster than ever for developers and teams to deploy best-in-class document intelligence models.

Marker is a purpose-built, sub-billion-parameter model trained specifically for document structure. It delivers deterministic, high-fidelity parsing without the hallucination or instability of larger LLMs, and does so at a fraction of the cost. Marker, along with Datalab’s other open-source tools, have earned 48k+ stars on GitHub and are trusted by researchers, startups, and enterprise teams alike.

Modal already powers Datalab’s hosted platform, enabling them to deliver reliable, scalable model serving and roll out new releases quickly:

 “Using Modal for inference is like having an extra infra team—it’s reliable, scalable, and fast—meaning I can get back to training models.” — Vik Paruchuri, Founder @ Datalab

**Now, any builder or team can use Modal to instantly deploy Datalab’s state-of-the-art [Marker](https://github.com/datalab-to/marker) pipeline and [Surya](https://github.com/datalab-to/surya) OCR toolkit.** Datalab’s tools remain free for research, personal use, and startups under $2M funding/revenue, with licensing options for commercial customers.

## Quickstart

Marker is easy to clone and run locally, but you can deploy it on Modal to maximize scalability and throughput. Clone the Marker repository and deploy the Modal example [here](https://github.com/datalab-to/marker), which will provision a GPU container in Modal, install `marker`, and expose its functionality behind a FastAPI endpoint.

That’s it! For a more detailed full-stack example, check out this [Modal example](https://modal.com/docs/examples/doc_ocr_jobs) of building a quick document OCR web app.

![](https://modal-cdn.com/blog/images/receipt-parsing.png)

Modal comes with $30/mo in free compute credits, which is plenty to get started with your OCR tasks.

## How it works

Modal allows you to deploy Marker on GPUs in seconds. Modal also autoscales GPUs for your deployment so you get max throughput on batch jobs with no additional effort.

Here’s what happens behind the scenes:

First, Marker model weights get cached in a [Modal Volume](/docs/guide/volumes), which cuts cold start times. No need to redownload models every time, and Volumes guarantee fast reads no matter where your inference function is running.

Then, when the inference function is called, Modal spins up a container using the environment and hardware requirements [specified in the function decorator](/docs/guide/images). You don’t need to use config files, as everything is defined in-line with application code.

Need to process thousands of PDFs at once? Modal [autoscales instantly](/docs/guide/scale)—up to thousands of GPUs—based on request volume. Our global capacity pools guarantee that you never wait on quota.

## Why Marker?

Marker supports over 90 languages, handles incredibly complex and dense tables, and is state-of-the-art in extracting math from PDFs. Marker can be used for a wide range of tasks like:

- Indexing PDF knowledge bases for RAG
 - Parsing multilingual PDF content for training
 - Extracting key information from unstructured documents

![](https://modal-cdn.com/blog/images/marker-benchmarks.png)  see [here](https://github.com/datalab-to/marker?tab=readme-ov-file#benchmarks) for detailed benchmarks

Marker benchmarks favorably for both accuracy and throughput compared to cloud services like Llamaparse and Mathpix, as well as other open source tools. Accuracy benchmarks above were performed on single PDF pages from Common Crawl and scored using LLM-as-a-judge.

## 10x Marker throughput on Modal

Accuracy alone isn’t enough. Real-world systems demand high throughput and reliability to process millions of documents quickly, consistently, and cost-effectively. Marker was designed with that in mind, and Modal is the fastest way to achieve scale for self-deployments.

On an M4 Mac using Apple MPS (no GPU), you can process around 0.22 pages per second. On Modal, you can increase this to around 2.2 pages per second per container. This **10x gain** comes from using more powerful hardware (e.g. H100 GPU), Flash Attention optimizations, and environment tuning (for settings like `OMP_NUM_THREADS`). Note that in practice, you should experiment with various configurations to find your ideal balance of accuracy, cost, and throughput

If you’re batch processing multiple PDFs, Modal can easily autoscale to hundreds of GPUs, further improving overall throughput.

Need a managed solution for a commercial use case? Datalab’s API platform uses additional inference optimizations to enable a page throughput of around 3-4 pages per second. This is deployed on Modal behind the scenes!

![](https://modal-cdn.com/blog/images/marker-throughput-chart.png)

## Deploy best-in-class document intelligence

We’re excited to be deepening our collaboration with Datalab. Many of our users have already been turning to Modal for best practices on deploying Marker and Surya, and this collaboration now makes that seamless.

Get started today with [this example](/docs/examples/doc_ocr_jobs).