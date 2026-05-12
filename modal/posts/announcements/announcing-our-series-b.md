---
title: "Announcing our $87M Series B"
author: "bernhardsson"
date: "2025-09-29"
url: "https://modal.com/blog/announcing-our-series-b"
category: "announcements"
site: "modal"
---

# Announcing our $87M Series B

 ![](https://modal-cdn.com/blog/images/erik-bernhardsson.webp) [Erik Bernhardsson@bernhardsson](https://twitter.com/bernhardsson) CEO and Co-Founder![](https://modal-cdn.com/blog/images/akshat-bubna.webp) [Akshat Bubna@akshat_b](https://twitter.com/akshat_b) CTO and Co-Founder  We’re excited to announce that we have raised more than $80M in a Series B round, led by Lux Capital, with existing investors participating as well. Our post-money valuation is $1.1B. This brings our total money raised to $111M.

## AI-native companies need AI-native infrastructure. We built it.

When electricity was new, it was often retrofitted into existing solutions. A big electric engine replaced a big steam engine. But over time, we learned to take advantage of the new technology. You could replace one big engine with many tiny engines. You could connect all power generation into a big grid.

Compute infrastructure is going through a similar transformation. We all know we are still early in the days of AI – and honestly, even the cloud. A lot of existing infrastructure has not been built for either, and we’re increasingly running up against their limitations – global GPU capacity management, highly variable demand, large models, and many other things.

As developers, we saw a massive opportunity in rethinking infrastructure for these new-age needs. So we spent the last four years building something that:

- can aggregate GPUs and CPUs around the world in seconds so users never have to think about capacity management
 - lets developers iterate quickly, have fun, and get products to market way faster
 - is code-first, with programmable building blocks for storage, compute, and networking
 - is lightning fast, with sub-second container startup times and low-latency routing
 - is usage-based and built on serverless primitives, meaning users only pay for the time they run things

By pooling the world’s compute and managing the capacity at scale, we can drive efficiency and speed. By building for AI workloads directly, we can design better solutions.

Building this wasn’t easy, and we had to go very deep in order to lay the foundation we needed. This included building our own file system, container runtime, scheduler, and much more. But as a result, we now have thousands of customers running complex applications who agree that we offer an unparalleled experience.

## The future of AI is already running on Modal:

Our customers do everything from curing cancer to using AI to craft songs on Modal. Here’s why:

 “Everyone here loves Modal because it helps us move so much faster. We rely on it to handle massive spikes in volume for evals, RL environments, and MCP servers. Whenever a team asks about compute, we tell them to use Modal.” — Aakash Sabharwal, VP of Engineering [

](https://scale.com/) “Modal lets us deploy new ML models in hours rather than weeks. We use it across spam detection, recommendations, audio transcription, and video pipelines, and it’s helped us move faster with far less complexity.” — Mike Cohen, Head of AI &amp; ML Engineering [](https://substack.com/) “We've previously managed to break services like GitHub because of our load, so Modal handling our massive scale so smoothly means a lot. We trust Modal to keep up with our growth, and we're excited to build together in the long term.” — Anton Osika, Founder and CEO [](https://lovable.dev/) This is just a small window into how some of the biggest names in AI use our technology today. Just recently, Meta announced [Code World Models (CWM)](https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/), where they used Modal to spin up thousands of concurrent sandboxed environments for reinforcement learning.

## We’re building products for the entire ML lifecycle

The foundation of Modal that keeps everything running is our container platform and storage layer. We’ve also built robust primitives on top of this foundation that let teams build powerful AI applications.

![](https://modal-cdn.com/blog/images/blog_asset_1.webp)

More recently, we’ve shipped several new products to serve new AI use cases. Our full product suite now includes:

- [Inference](/products/inference): run LLMs, generative media models, or any custom model, on thousands of GPUs
 - [Sandboxes](/products/sandboxes): spin up secure, dynamically-defined environments for your agents to execute code; we run tens of thousands of containers simultaneously for customers like Lovable
 - [Batch](/products/batch): easily launch massive parallel jobs; customers use this for batch transcription, protein folding, weather forecasting, and much more
 - [Training](/products/training): spin up a cluster of nodes interconnected with high-throughput RDMA in seconds
 - [Notebooks](/products/notebooks): collaborate on exploratory data analysis with near-instant GPU cold starts

## **What’s next?**

Our goal is to be the infrastructure provider for every single part of developing and running AI in production. The infrastructure demands of AI are only becoming more complex over time.

Modal empowers developers to get stuff into production as fast as possible. With our deep bench of talent, we’ve made tremendous progress toward that end and are excited to launch many more things over the next few years.

If you’re eager to build with us, [check out our open roles](/careers). If you’re a developer who wants to try Modal, [sign up here.](/signup)