---
title: "Product updates: multi-node training clusters, B200 and H200s, and Client 1.0 release"
author: "clustered"
date: "2025-07-11"
url: "https://modal.com/blog/modal-product-updates-jul-2025"
category: "inference"
site: "modal"
---

# Product updates: multi-node training clusters, B200 and H200s, and Client 1.0 release

## 🏋️ Multi-node training clusters in beta

 ![](https://modal-cdn.com/cdnbot/1id9la4d7_3aee338a.webp)

We’ve made multi-node training as easy as multi-GPU training on Modal. By simply adding the `@clustered` decorator, you can instantly tap into dozens of GPUs on multiple hosts, co-scheduled and co-located. And thanks to high-speed RDMA interconnect (3.2 Tbps Infiniband), those GPUs can communicate quickly enough to scale your training runs linearly with node count.

Check out the [guide](https://modal.com/docs/guide/multi-node-training) for more info and examples. **We are actively looking for beta users, please [reach out](https://modal.com/slack) if interested!**

## 🚀 Introducing B200s and H200s on Modal

![](https://modal-cdn.com/cdnbot/2bi0jbx8r_1ec6fa68.webp)

Modal now offers NVIDIA B200 and H200 GPUs serverlessly. Add a one-liner to your Modal function, pay as you go ($6.25/hr for B200, $4.54/hr for H200), and see up to 2-4× faster LLM inference compared to H100s.

See the full announcement [here](https://modal.com/blog/introducing-b200-h200).

## 🗞️ Modal Client 1.0 release

We recently launched [version 1.0 of the Modal client](https://pypi.org/project/modal/), underscoring our commitment to API stability and giving users more clarity and predictability. For instructions on how to migrate to 1.0, check out our [migration guide](https://modal.com/docs/guide/modal-1-0-migration).

For more insight into the design principles underlying the release, read our blog [here](https://modal.com/blog/introducing-client-1-0).

## 👩‍💻 Client updates

Run `pip install --upgrade modal` to get the latest client updates.

- Added a [`modal.Volume.read_only`](https://modal.com/docs/reference/modal.Volume#read_only) method [(1.05)](https://modal.com/docs/reference/changelog#:~:text=Latest-,1.0.5%20(2025%2D06%2D27),-Added%20a%20modal)
 - Added a `--secret` option to `modal shell` for including environment variables defined by named Secret(s) in the shell session [(1.04)](https://modal.com/docs/reference/changelog#:~:text=Added%20a%20%2D%2Dsecret%20option%20to%20modal%20shell%20for%20including%20environment%20variables%20defined%20by%20named%20Secret(s)%20in%20the%20shell%20session)
 - Added support for specifying a timezone on `Cron` schedules [(1.03)](https://modal.com/docs/reference/changelog#:~:text=Added%20support%20for%20specifying%20a%20timezone%20on%20Cron%20schedules%2C%20which%20allows%20you%20to%20run%20a%20Function%20at%20a%20specific%20local%20time%20regardless%20of%20daylight%20savings%3A)
 - Added a `--timestamps` flag to `modal app logs` that prepends a timestamp to each log line [(1.01)](https://modal.com/docs/reference/changelog#:~:text=Added%20a%20%2D%2Dtimestamps%20flag%20to%20modal%20app%20logs%20that%20prepends%20a%20timestamp%20to%20each%20log%20line.)

## 📊 LLM Engineer’s Almanac: SGLang or vLLM?

![](https://modal-cdn.com/cdnbot/3c24nb034_08f150ed.webp)

In case you missed it: AI is actually open now, thanks to the teams releasing open models (LLaMA, ERNIE, DeepSeek) and engines (vLLM, SGLang).

But that just means more questions: which engine should you use? How much will it cost to self-host your RAG chatbot? We ran over a thousand LLM engine performance benchmarks and built an interactive tool to help you answer these questions. Check it out [here](https://modal.com/llm-almanac/summary)!

## 🖼️ FLUX.1 Kontext [dev] on Modal

![](https://modal-cdn.com/cdnbot/4its4wyln_44782a6d.webp)

Black Forest Labs released weights for [FLUX Kontext [dev]](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev). It’s the new state-of-the-art open-weight image generation model, with super precise contextual editing abilities across success renderings. Our [example](https://modal.com/docs/examples/image_to_image) shows you how to run it on B200s.

## 🏎️ Run FLUX.1-dev 3x faster

![](https://modal-cdn.com/cdnbot/5euw8r4qy_40ad1a19.webp)

Speaking of FLUX: check out our blog post on how to make Flux [dev] run 3x faster with multiple optimizations. That means you have the flexibility of self-deployments while still getting the speed and price of API platforms! Read more [here](https://modal.com/blog/flux-3x-faster).

## ❓Learn how Quora uses Modal Sandboxes at scale

Quora uses Modal to power sandboxed code execution for Poe, their chatbot platform. Quora can create up to 1,000 Sandboxes per second with Modal, plus we’ve saved the team >15% engineering time compared to building their own sandbox solution! Read more [here](https://modal.com/blog/quora-case-study).