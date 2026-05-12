---
title: "How sync. uses Modal to lipsync 100 hours of video a day"
author: "Unknown"
date: "2025-04-18"
url: "https://modal.com/blog/sync-labs-case-study"
category: "inference"
site: "modal"
---

# How sync. uses Modal to lipsync 100 hours of video a day

  “With Modal, we went from a research project to a revenue-generating business almost overnight. Leveraging Modal allowed us to focus on what we do best – training state of the art video generation models – without worrying about MLops and infrastructure.” — Prady Modukuru, CEO

## About sync.

 sync. is a research lab training foundational models to understand and manipulate humans in video. They released a state-of-the-art lipsyncing model that lets you reanimate the speech of any human in live-action, animated, or AI generated video. They are the original team behind wav2lip, and are used by thousands of developers, marketing teams, and creatives around the world.

Check out how their latest zero-shot lipsyncing model preserves the original speaking style of Nicolas Cage even when he’s translated into other languages.

> [](https://twitter.com/_/status/1901780574936957055)

But they didn’t start here. Check out the viral demo that brought them to the forefront of AI video: Lex Fridman and Mark Zuckerberg talking about Elon Musk in Hindi.

> [](https://twitter.com/_/status/1680645510103977987)

## The Challenge: Graduating from Google Colab

The viral tweet above was powered by a Google Colab notebook. This was great for a prototype and to get research out quickly, but impossible to scale into a business.

Like many, they started with AWS Lambda and quickly ran into headaches with their deployment process, autoscaling policies, and lack of GPU support. At this time, they were only a team of five and wanted to focus on training new models and iterating on product, not MLops infrastructure.

Then they checked out AI-as-an-API providers like Replicate. While Replicate was great for serving off-the-shelf models, the sync. team quickly became frustrated deploying their custom model via Replicate’s Cog framework. Every code update required a redeploy and rebuild of the container, which took **10-15 minutes**. Successful startups need to be able to iterate in seconds, not tens of minutes.

## Finding Modal: The Right Fit for AI-Driven Video Editing

Through connections at Founders Inc and Y Combinator, sync. discovered Modal’s startup credits program and was successfully awarded $25K in credits. Unlike other solutions, Modal just worked. No need to log in to a separate platform to write code; sync. could easily decorate their existing code, run `modal serve` to see code changes live, and deploy worry-free knowing that Modal would handle autoscaling.

This fast iterative loop meant sync. could deploy up to **95 times a day** testing many small iterations and updates while managing a production workload. In one year, they were able to ship 10 major model variants to production and 1000 iterations in between.

## Deep dive: lipsyncing over 100 hours of video a day

Let’s look at a specific example of how Sync Labs uses parallel execution on Modal to lipsync over 100 hours of video a day.

Short videos are processed in a single batch. Longer videos are broken down systematically:

- Splice the video into n scenes
 - For n scenes, run face detection and translation across n T4 GPU containers
 - Pass each scene to proprietary LipSync GenAI model on more powerful A100s
 - Stitch dubbed scenes back together

![](https://modal-cdn.com/cdnbot/sync-diagramva5adbna_2b2d3f05.webp)

This is a great example of how Modal’s simple [parallel execution model](/docs/guide/scale) can efficiently process what would have been hours-long, compute-intensive workloads.

## What’s next for sync. and Modal?

sync. wants to put the power of a VFX studio in everyone’s pocket. Translation and lipsyncing is just the beginning of AI-enabled editing; the team is hard at work on emotion editing, pose adjustment, and even changing physical characteristics of the subject.

It’s incredible how much a small team can accomplish these days. sync. can focus entirely on R&amp;D and let Modal handle the platform. This is the kind of modern startup organization that Modal was built to support; people at the cutting edge of AI research who want to ship code fast.