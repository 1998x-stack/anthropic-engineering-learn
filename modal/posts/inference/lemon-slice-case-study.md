---
title: "How Lemon Slice built real-time generative video with Modal and Daily"
author: "Unknown"
date: "2025-04-24"
url: "https://modal.com/blog/lemon-slice-case-study"
category: "inference"
site: "modal"
---

# How Lemon Slice built real-time generative video with Modal and Daily

  Video generation has been all the rage, and [Lemon Slice](https://lemonslice.com/) is on a mission to build the most expressive character generation models in the world. Lemon Slice has used Modal from the very beginning, and we’re excited to support their latest product: real-time video conversations with AI characters. Real-time is hard to accomplish, but with Modal and Daily’s low-latency primitives, it takes only seconds to get from user input to avatar response.

## Prologue: scalable inference for a 1B parameter video model

Lemon Slice’s first [viral product](https://news.ycombinator.com/item?id=41467704) was a site where you could generate a video of a character speaking by inputting an image of the character plus text or audio.

![](https://modal-cdn.com/lemon-slice-product.gif)  See [https://lemonslice.com/gallery](https://lemonslice.com/gallery) for full quality examples with audio

From the get-go they knew they wanted to set up their production inference pipeline on Modal. The founders, who came from ML research backgrounds, had previously built out custom infrastructure on AWS and GCP. This was not something they were eager to repeat—from configuring instances to working across compute regions to building out scaling logic, it was going to be a big distraction from shipping new AI products to market.

![](https://modal-cdn.com/cdnbot/tmpfse31kxs_ebd718cf.webp)  Without Modal, the Lemon Slice team would have to set up and manage multiple infra services.

With Modal, they were able to scale to 10,000 requests per hour just by writing two Modal Functions in Python: one that was a REST endpoint for user input and another that ran inference on their video model. This solution:

- allowed them to avoid setting up an ECS cluster, job queue system, and load balancer.
 - autoscaled efficiently, as Modal would spin GPU containers up and down for video inference based on request volume.
 - came with performance optimizations like [memory snapshotting](/docs/guide/memory-snapshots) built in, cutting down container initialization time.

![](https://modal-cdn.com/cdnbot/tmp_ukux39z_f81a710f.webp)  With Modal, the Lemon Slice team writes Python functions and Modal manages the infrastructure components.

Modal’s autoscaling also sped up their model eval process. Every few hours when a new model checkpoint was created, 50+ sample videos could be generated in parallel, providing a quick slate of outputs for the team to assess.

 “Modal allowed us to go from an idea on Monday to something live on Tuesday. From 70% of an engineer’s time spent in infrastructure to like, less than 10%, that’s a huge delta.” — Lina Colucci, CEO and Co-founder, Lemon Slice

## Now let’s make it real-time

Lemon Slice’s newest product, [Lemon Slice Live](https://lemonslice.com/live), lets users video chat with AI characters. The real-time component to the user interaction adds a new level of complexity. To tackle this, their architecture, from user input (audio) to AI output (video plus audio), is latency-optimized throughout:

- When a user starts a video session, two Modal Functions are invoked. One starts a Pipecat server while the other loads up the video model for inference on a GPU. Modal autoscales the containers for these Functions based on how many user sessions are live.
 - When the user speaks, data starts flowing through the Pipecat pipeline. [Pipecat](https://www.pipecat.ai/) is an open-source orchestration framework that enables real-time, multi-modal AI services by chunking and processing data continuously.
 - The Pipecat pipeline calls Deepgram to turn user speech into text, Grok to get the LLM conversational response, ElevenLabs to convert that to speech, and finally the model running on the other Modal container to generate video.
 - To minimize latency between the Pipecat container and video inference container, the two containers a) communicate directly via our [Tunnel](/docs/guide/tunnels) feature, which uses TCP ports and b) are co-located using our [region selection](/docs/guide/region-selection) feature.
 - The video inference container sends frames to [Daily](https://www.daily.co/), a global WebRTC infrastructure platform, which streams the final video and audio back to the user.

![](https://modal-cdn.com/cdnbot/tmpejx9y_k5_a57c8cf9.webp)

By combining the low latency features of Modal, Pipecat, and Daily, Lemon Slice has delivered a best-in-class character video generation product with an end-to-end video response latency of 3-6 seconds.