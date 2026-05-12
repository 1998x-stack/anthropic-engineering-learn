---
title: "Introducing Modal Batch: Process 1 Million Jobs with 1 Line of Code"
author: "Unknown"
date: "2025-05-22"
url: "https://modal.com/blog/batch-processing"
category: "training-finetuning"
site: "modal"
---

# Introducing Modal Batch: Process 1 Million Jobs with 1 Line of Code

 ![](https://modal-cdn.com/blog/images/gongy-modal.webp) Richard Gong Member of Technical Staff  We’re excited to announce the launch of [Modal Batch](/docs/guide/batch-processing)—a new interface backed by a new durable queue system built specifically to make job processing easy, scalable, and fault-tolerant.

Many of our AI customers have batch processing needs. From preprocessing audio clips for training to embedding documents offline, customers need an efficient way to transform millions of data inputs at once. Modal’s ultra-fast container infrastructure makes us particularly well-suited to expand into this use case. Companies like Harvey, Suno, and Achira already use Modal Batch today.

## How it works

Let’s say you need to embed a million video clips.

First, define a Modal Function that performs the embedding. You can specify a custom image or specific hardware for the Function if needed.

Next, call `.spawn_map` on that Function with the set of your million video clips as input. This will instantly launch thousands of containers in the cloud and is guaranteed to run reliably to completion on all your inputs.

That’s it! Watch us spin up 100+ containers to handle 25,000 inputs here:

## Wait, I thought batch processing was already possible on Modal

Not like this. You may have used `.map` or `.spawn` before to process many inputs at once, but we’ve introduced a number of step-change improvements that make Modal much better suited for massive jobs.

- We overhauled our queue system so that it could handle 500x more inputs. You can queue 1 million inputs at once now, up from 2000.
 - We now guarantee inputs will be executed up to 7 days after you launch a batch job, up from 1 day.
 - We introduced a native handler, `.spawn_map`, to spawn batches of inputs. Previously, you had to manage async logic yourself to call `.spawn` concurrently over your inputs.

## Why Modal Batch over alternatives

Setting up batch processing is complex because you’re typically working with a full distributed system to handle payload storage, batch orchestration, cloud resource scaling, monitoring, and more. Modal Batch capitalizes on Modal’s existing strengths so you can stay focused on business logic over infrastructure.

**Enterprise-grade scalability.** Our custom container runtime, filesystem, and scheduler allow us to instantly spin up thousands of containers—including with GPUs, no reservations required—to complete your job.

![](https://modal-cdn.com/blog/images/batch-scheduler.webp)

**Ergonomic UX.** Launching a batch job doesn’t require leaving your IDE. There are no cloud consoles, YAML files, or container orchestration systems to manage.

**Easy debugging.** Modal’s dashboard lets you drill into logs and metrics for individual inputs and containers so you can quickly pinpoint failures. You can also see these metrics in aggregate for each batch job.

![](https://modal-cdn.com/blog/images/batch-error.webp)

**Integrated with the rest of your ML pipeline.** Because Modal is a general-purpose compute platform, you can easily chain together Functions for batch processing, training, or inference with the same Python UX.

## Customer Stories

Our customers have built diverse applications on top of Modal Batch since we launched in beta.

### Speeding up document processing at Harvey

Harvey is an AI platform used by legal teams to accelerate document-based workflows. One key feature is the ability for users to quickly pull relevant insights from knowledge bases of case laws, tax regulations, and legislation. Powering this requires their data team to preprocess, chunk, and embed millions of documents—which is where Modal comes in.

Using Modal Batch, Harvey observed a 10x speed-up in their data processing pipeline, since Modal could quickly fan out their document inputs across 1000 containers. Previously, the team used open-source orchestrators like Argo and Airflow, which meant they had to manage the underlying infrastructure themselves. This resulted in high operating costs and limited scalability.

 “With the old in-house systems, we'd have to tune number of workers, instance size, parallelization strategy, all this stuff, which was very time-consuming and not directly generating business value. Modal magically handled all that.” — Samarth Goel, ML engineer at Harvey

### Scaling audio processing at Suno

Suno is pushing the boundaries of AI-generated music with their state-of-the-art audio models. Their latest 4.5 model can generate up to 8 minutes of high-fidelity audio at 48kHz in stereo. But with great audio quality comes massive data processing needs. Training these models requires preprocessing enormous datasets, running embeddings, and preparing training data—all at a scale that would typically demand a big dedicated GPU cloud and a team to manage.

Modal enables Suno to:

- Launch a batch job on thousands of GPUs on short notice without infrastructure setup
 - Run GPU-accelerated pre-processing models on high bandwidth audio data
 - Maintain simple scripts that “just work” without ongoing maintenance

 “Modal's autoscaling capabilities give us the best of both worlds. We get the power of a massive GPU cloud when we need it, without the complexity of managing spot instances or cloud-specific infrastructure.” — Georg Kucsko, CTO at Suno

### Preparing Scientific Datasets at Achira

Achira is advancing drug discovery by building atomistic foundation simulation models. A key part of their workflows involve processing and validating quantum mechanical datasets for model training. These datasets, while high signal, require additional processing to add crucial metadata which is not always present.

 “Processing external quantum mechanical datasets comes with unique challenges. Jobs can fail in numerous ways—from low-level errors thrown by the underlying analysis packages, to transient issues communicating with our storage server. Modal's retry mechanism and batching primitives have made our data pipeline much more robust.” — Liz Decolvenaere, Quantum Chemical Engineer at Achira

## What’s next?

We’re extending Modal’s batch processing capabilities while maintaining our core principle of a simple *function* interface. Coming soon:

- **Function caching**: Never run the same computation twice.
 - **Improved ergonomics:** Interact with your batch job programmatically—change priority, check progress, and cancel from your Python code.
 - **Support in other languages:** Use our SDKs for JavaScript or other languages to write your batch jobs.

## Get started today

Ready for a dead simple way to throw a thousand containers at your batch job?

- Install Modal: `pip install modal`
 - Create an account: `python -m modal setup`
 - Check out our [batch processing documentation](/docs/guide/batch-processing)