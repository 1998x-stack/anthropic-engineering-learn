---
title: "Product updates: Logs v2, live container profiling, and region selection on all plans"
author: "Unknown"
date: "2025-02-14"
url: "https://modal.com/blog/modal-product-updates-feb-2025"
category: "tutorials"
site: "modal"
---

# Product updates: Logs v2, live container profiling, and region selection on all plans

## 🪵 Logs refresh

 Our logs dashboard has gotten a refresh! This includes interface improvements like being able to filter on inputs over a time range.

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/logs-v2.gif)

## 🔍 🕵️ Live profiling containers

We’ve added a container profiling feature that allows you to see what code is running in your container in real time. This is intended to help you debug when a container or input is stuck

To access this feature, head over to the **Containers** tab in your function, open a running container, and kick off a **Live Profiling** session.

![](https://modal-public-assets.s3.us-east-1.amazonaws.com/live-profiling-bigger+(1).gif)

## 🐚 Debug shells

Our new [Debug Shells](https://modal.com/docs/guide/developing-debugging#debugging-running-containers) let you run commands inside a running container. They come preinstalled with tools such as `vim`, `ps`, and `strace`. To get started, run:

- `modal container list` to get your container ID
 - `modal shell [container-id]` to launch a debug shell

![](https://modal-cdn.com/cdnbot/debug-shellscmxwm3nn_61867325.webp)

## 🌎 Region selection available on all plans

Our [region selection](https://modal.com/docs/guide/region-selection#region-selection) feature allows you to define which cloud region you’d like your function to run in. It’s helpful for reducing egress fees and complying with data residency requirements, and is now available on all plans! Usage is priced with a multiplier on top of our base prices.

![](https://modal-cdn.com/cdnbot/region-pricing-all-planshadznxlx_3b45432c.webp)

## 👩‍💻 Client updates

Run `pip install --upgrade modal` to get the latest client updates:

- We’ve added [OIDC authentication](https://modal.com/docs/guide/cloud-bucket-mounts#using-oidc-identity-tokens) support for cloud bucket mounts via the new `oidc_auth_role_arn` field in `CloudBucketMount`.
 - Modal functions, methods and entrypoints can now accept [variable-length arguments](https://modal.com/docs/guide/apps#argument-parsing) to skip Modal’s default CLI parsing.

## 🧬 DeepSeek on Modal

Fresh off the DeepSeek launches, we have a [new example](https://modal.com/docs/examples/llama_cpp) on how to run DeepSeek-R1 (in ternary format) on Modal.

## 🖊️ New on our blog

- [Sandboxes in GA](https://modal.com/blog/sandbox-launch) - Sandboxes are the Modal primitive for safely running untrusted code, whether that code comes from LLMs, users, or other third-party sources. They are now generally available!

## 🍭 March 6 developer event with Mistral

![](https://modal-cdn.com/cdnbot/modal-mistral-event6ch33az7_3425a5bd.webp)

We’re hosting an open-source LLM demo night and happy hour with [Mistral](https://mistral.ai/en) on March 6! RSVP [here](https://lu.ma/bk3gbum3). If you use Mistral and Modal and are interested in demoing, fill out [this form](https://form.fillout.com/t/udirWcL1quus).