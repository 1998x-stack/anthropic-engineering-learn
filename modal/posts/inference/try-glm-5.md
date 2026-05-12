---
title: "Try GLM-5.1, the new frontier of open intelligence, on Modal"
author: "charles_irl"
date: "2026-02-11"
url: "https://modal.com/blog/try-glm-5"
category: "inference"
site: "modal"
---

# Try GLM-5.1, the new frontier of open intelligence, on Modal

 ![](https://modal-cdn.com/charles-frye.jpg) [Charles Frye@charles_irl](https://twitter.com/charles_irl) Member of Technical Staff![](https://modal-cdn.com/blog/images/gongy-modal.webp) [Richard Gong@_gongy](https://twitter.com/_gongy) Member of Technical Staff![]( https://modal-cdn.com/cdnbot/david_wang_headshotgylhrfss_85189999.webp) [David Wang@_dcw02](https://twitter.com/_dcw02) Member of Technical Staff![](https://modal-cdn.com/timothy-feng.jpg) Timothy Feng Member of Technical Staff

#### Update 2026-04-07: Today, [Z.ai released GLM-5.1](https://z.ai/blog/glm-5.1), once again setting the state-of-the-art for open weights intelligence. Our free endpoint has been upgraded to serve this new version.

Today [Z.ai released GLM-5](http://z.ai/blog/glm-5), a frontier open weights foundation language model designed for long-horizon agents and systems engineering.

The Modal Research team partnered with Z.ai ahead of public launch so we could test drive the model on our infrastructure. It’s delightful, smart, and fast. Internally, we’ve added it to our favorite AI frontends: the [Vercel AI SDK](https://github.com/modal-projects/modal-jazz/tree/main/frontends/ai_sdk_react), [Claude Code](https://github.com/modal-projects/modal-jazz/tree/main/frontends/claude), [OpenCode](https://github.com/modal-projects/modal-jazz/tree/main/frontends/opencode), and [OpenClaw](https://github.com/modal-projects/modal-jazz/tree/main/frontends/openclaw).

And now you can too: [try it for free](https://modal.com/glm-5-endpoint)!

## Why does this matter?

In case you missed it, software engineers have officially been automated out of the job; we are all prompt engineers now.

Well, not exactly. But there has been a [vibe shift in vibe coding](https://thundergolfer.com/vibe-coding-vibe-shift) in the last two months, as serious, taste-making senior engineers from [Linus Torvalds](https://github.com/torvalds/AudioNoise) (Linux) to [dhh](https://x.com/dhh/status/2007504187568074843?s=20) (Ruby on Rails) have increasingly embraced coding with agents. Even George Hotz called agentic coding [“decent”](https://x.com/__tinygrad__/status/2000972812731998522?s=20).

The missing piece was model quality. Each new generation of frontier models supports a new and more ambitious application, from [early tab-completion with GPT-3 models](https://github.blog/ai-and-ml/github-copilot/under-the-hood-exploring-the-ai-models-powering-github-copilot) (RIP to `code-davinci-002`) to [copiloting chat assistants with GPT-3.5/Claude 2](https://cursor.com) to [simple app development with GPT-4/Claude 3](https://lovable.dev/). Now, with Claude Opus 4.6 and GPT 5.3 Codex, the frontier supports long-horizon tasks, like the development and improvement of complex systems. If you don’t believe us, just ask your terminally online friend who won’t shut up about Claude Code and ClawdeBot moltbot OpenClaw.

As before, this new application domain was pioneered by proprietary models — models whose weights are not available under an [Open Source Initiative-approved license](https://opensource.org/licenses), like MIT or Apache. But since DeepSeek’s epoch-making launch of DeepSeek-R1, open models have not been far behind. Now, GLM-5 matches the performance of proprietary models released in the last month and is available under the MIT license.

![](https://modal-cdn.com/blog/images/glm-5-benchmark-image.webp)

For details on the above benchmarks and more, see [Z.ai’s blog post](https://z.ai/blog/glm-5).

## How do I run GLM-5?

We’ve written [in depth about the performance profile of LLM inference](https://modal.com/docs/guide/high-performance-llm-inference), but we walk through the core considerations for GLM-5 quickly here. In [eight bit floating point precision](https://www.quant.exposed/), GLM-5 weighs in at about 700 GB. That’s larger than the [HBM](https://modal.com/gpu-glossary/device-hardware/gpu-ram) of any single GPU on the market, so it must be deployed onto multiple GPUs to avoid tanking performance. Like most large models, it uses mixture-of-experts (MoE) sparsity in the matrix multiplications of its MLP blocks to reduce demand on [memory bandwidth](https://modal.com/gpu-glossary/perf/memory-bandwidth). A variant of [DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) controls the punishing quadratic scaling with sequence length of the attention mechanism by quickly filtering out all but a few thousand past tokens with a lightweight, data-dependent filtering layer (”indexer”). We’ve landed on running it with tensor parallelism in the MoE layers (using DeepSeek’s DeepGemm kernels) and data parallelism in the attention layers (using DeepSeek’s FlashMLA kernels).

With high quality open source inference engines like vLLM and SGLang, any engineer with access to the right hardware can host this model themselves and support long-horizon agents and systems engineering tasks with excellent per-user latency. We’ve been running the model internally with interactivities between 30 and 75 tokens per second per user (depending on replica load and speculator hit rate).

At time of writing, getting GLM-5 to run involves a few patches, which we document with reproducible deployment code [here](https://github.com/modal-projects/modal-jazz/blob/main/backend/backend.py). That code deploys GLM-5 with SGLang on a single node of eight B200s on our cloud platform. We expect fast follows to stabilize support and to improve performance, including integrating our work on inference-optimized paths for [Flash Attention 4](https://modal.com/blog/reverse-engineer-flash-attention-4).

## How do I use GLM-5?

To support everyone who wants to take GLM-5 for a spin, we’re releasing an endpoint you can connect to your favorite AI frontend. And it’s free! From now until the end of April. You can generate a credential and get started [here](https://modal.com/glm-5-endpoint).

Usage is limited to a single concurrent request. There are no direct limits on tokens — [requests are what really matter!](https://modal.com/blog/dollars-per-token-considered-harmful) We find this maps nicely onto “personal use” of a coding agent: one or a few active client threads, each possibly spanning many thousands of tokens.

It's the first time we're releasing an endpoint in addition to sample self-deployment code. More to come on this front from the Modal Research team.

Have a production use case in mind? Contact [sales@modal.com](#) to discuss higher rate limits or for guidance on [deploying your own GLM-5 endpoint on Modal](https://github.com/modal-projects/modal-jazz/blob/main/backend/backend.py).

Below, we document how to integrate our GLM-5 endpoint with a variety of frontend frameworks. We’re running an OpenAI API-compatible server, so the integration path will in general go through your framework’s support for that API.

## How do I use GLM-5 with OpenCode?

We really like the [OpenCode](https://opencode.ai/) coding agent framework. It’s easily configurable, widely compatible with other tooling, and highly extensible.

Once you [create a token for the Modal GLM-5 endpoint](https://modal.com/glm-5-endpoint), you just need to add Modal as a `provider` in an `opencode.json` configuration file, like in the sample below. You can find docs [here](https://opencode.ai/docs/providers/#custom-provider).

If you want to scale up your OpenCode agents, try [deploying them onto a Modal Sandbox](https://modal.com/docs/examples/opencode_server). You keep the HTTP API and the easy web and terminal UIs, but you gain ultra-fast autoscaling cloud infrastructure. That’s [why Ramp built their Inspect background coding agent with OpenCode on Modal Sandboxes](https://builders.ramp.com/post/why-we-built-our-background-agent).

## How do I use GLM-5 with OpenClaw?

The hottest agent framework on the block right now is [OpenClaw](https://openclaw.ai/), which promiscuously integrates LLM APIs with tools, knowledge sources, and skills. If you thought `--dangerously-skip-permissions` was spooky, you ain’t seen nothing yet!

OpenClaw supports OpenAI API-compatible providers through the `openai-completions` setting of the `api` key of a model provider defined in `openclaw.json`.

Copy the `modal` key and value from the snippet below, add it to your `openclaw.json`, and then launch an OpenClaw server with your token in the environment under `LLM_BACKEND_API_KEY`. Or just paste this into your OpenClaw UI and ask the agent to figure it out; that’s closer to the spirit.

## How do I use GLM-5 with Claude Code?

Claude Code is not as open as other frontend agent frameworks. It is tightly integrated with Anthropic’s proprietary backend offerings.

However, you can [use a LiteLLM gateway to proxy](https://code.claude.com/docs/en/llm-gateway) between a Claude Code client and an OpenAI API-compatible endpoint like ours. We demonstrate how to deploy a such a proxy on Modal [here](https://github.com/modal-projects/modal-jazz/tree/main/frontends/claude).

## How do I use GLM-5 with the Vercel AI SDK?

The [Vercel AI SDK](https://ai-sdk.dev/) is a key library for JavaScript applications of LLM APIs. For instance, OpenCode supports OpenAI-compatible APIs by [delegating to the Vercel AI SDK](https://ai-sdk.dev/providers/openai-compatible-providers).

After you’ve [created a token for the Modal GLM-5 endpoint](https://modal.com/glm-5-endpoint), you can provide it as an `apiKey` when creating an `OpenAICompatible` provider.

You’ll also need to include the model name when creating a `chatModel`:

Like any good full-stack JavaScript framework, the Vercel AI SDK has two components: a Core library for logic and a UI library for frontends.

You can find a minimal integration of a Modal-hosted LLM with the Vercel AI SDK Core [here](https://github.com/modal-projects/modal-jazz/tree/main/frontends/ai_sdk_cli). We like to use this when fiddling with our LLM backends, since you retain a lot of control and observability while still developing against an interface that’s used in harder-to-debug applications like TUIs.

You can find a more fulsome integration of a Modal-hosted LLM with the AI SDK’s UI elements in [this sample React application](https://github.com/modal-projects/modal-jazz/tree/main/frontends/ai_sdk_react).