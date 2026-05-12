---
title: "Product updates: Price drops, brand refresh, and image-to-video example"
author: "Unknown"
date: "2025-03-17"
url: "https://modal.com/blog/modal-product-updates-mar-2025"
category: "inference"
site: "modal"
---

# Product updates: Price drops, brand refresh, and image-to-video example

## 🔻 We dropped our GPU, CPU, and memory prices by up to 65%

 ![](https://modal-cdn.com/cdnbot/pricing-drop-imagewbgj9bs7_2f5f0510.webp)

p.s. You can also spike up to 50 GPUs concurrently on the Team plan now!

## 📦 Modal SDK now available on `conda-forge`

By popular demand from the scientific computing community, the Modal SDK is now available on `conda-forge` starting with version `0.73.46`. You can install it with:

## 👩‍💻 Client updates

- We’re planning to release version 1.0 of the Modal client soon, and we’re working hard to address pain points and common sources of confusion in the SDK. When you update your client, you’ll likely see some deprecation warnings. We’ve put together a [Migration Guide](https://modal.com/docs/guide/modal-1-0-migration) to highlight the major changes and provide advice about how to update your application code.
 - We took the `_experimental` out of `_experimental_buffer_containers`! Add `buffer_containers=N` to your decorators and we’ll keep an extra “buffer” of containers around while your Functions are running, ready for when more inputs show up. See the [docs](https://modal.com/docs/guide/cold-start#overprovision-resources-with-min_containers-and-buffer_containers) for details.

## 📽️ New image-to-video example

We recently dropped [an example](https://modal.com/docs/examples/image_to_video) of how to run LTX-Video on Modal to animate images.

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/example-image-to-video.gif)

## ⛽️ Blog post: How to maximize GPU utilization

Three types of GPU utilization [you should know](https://modal.com/blog/gpu-utilization-guide) and how to go about measuring them.

![](https://modal-cdn.com/cdnbot/maximize-gpu-utilizationives8jfk_579c96c9.webp)

## 🖊️ More from our blog

- We made our hit [GPU glossary open-source](https://modal.com/blog/open-source-gpu-glossary) - now welcoming community contributions!

## 🍭 Fun tidbits

- You may have also noticed we launched [a shiny new logo](https://live.standards.site/modal) 🤩
 - We launched our first billboard campaign in SF! Anyone who finds and tweets a photo of our billboards gets a little prize.

![](https://modal-cdn.com/cdnbot/modal-billboard0jqgfu3f_d70d901d.webp)