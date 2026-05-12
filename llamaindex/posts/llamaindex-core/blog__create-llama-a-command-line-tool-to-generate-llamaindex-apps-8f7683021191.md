---
title: "Create-Llama CLI: Generate LlamaIndex Apps Fast | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/create-llama-a-command-line-tool-to-generate-llamaindex-apps-8f7683021191"
category: "llamaindex-core"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)



   21



Introducing `[create-llama](https://www.npmjs.com/package/create-llama)`, the easiest way to get started with LlamaIndex!

*Update 2023–11–20: we now have a *[*guide to deploying your create-llama apps*](/shipping-your-retrieval-augmented-generation-app-to-production-with-create-llama-7bbe43b6287d)*!*

Want to use the power of LlamaIndex to load, index and chat with your data using LLMs like GPT-4? It just got a lot easier! We’ve created a simple to use command-line tool that will generate a full-stack app just for you — just bring your own data! To get started, run:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



npx create-llamaThe app will then ask you a series of questions about what kind of app you want. You’ll need to supply your own [OpenAI API key](https://platform.openai.com/api-keys) (or you can customize it to use a different LLM), and make a few decisions.

# How does it get my data?

The generated app has a `data` folder where you can put as many files as you want; the app will automatically index them at build time and after that you can quickly chat with them. If you’re using LlamaIndex.TS as the back-end (see below), you’ll be able to ingest PDF, text, CSV, Markdown, Word and HTML files. If you’re using the Python backend, you can read even more types, including audio and video files!

# Technical details

The front-end it generates is a Next.js application, with your choice of [shadcn/ui](https://ui.shadcn.com/) or vanilla HTML and CSS for styling.

For the back-end, you have 3 options:

- **Next.js**: if you select this option, you’ll have a full stack Next.js application that you can deploy to a host like [Vercel](https://vercel.com/) in just a few clicks. This uses [LlamaIndex.TS](https://ts.llamaindex.ai/), our TypeScript library.
- **Express**: if you want a more traditional Node.js application you can generate an Express backend. This also uses LlamaIndex.TS.
- **Python FastAPI**: if you select this option you’ll get a backend powered by the [llama-index python package](https://pypi.org/project/llama-index/), which you can deploy to a service like [Render](https://render.com/) or [fly.io](https://fly.io/).

There are a couple of other questions you’ll be asked:

- Streaming or non-streaming: if you’re not sure, you’ll probably want a streaming backend.
- `SimpleChatEngine` or `ContextChatEngine` : the ContextChatEngine is the one that uses your data. If you just want to chat with GPT, you can use the `SimpleChatEngine`.

# Go forth and customize!

Once you’ve got your app up and running, you can customize it to your heart’s content! By default, for cost reasons, the app will use GPT-3.5-Turbo. If you’d like to use GPT-4 you can configure that by modifying the file `app/api/chat/llamaindex-stream.ts` (in the Next.js backend) or you can configure it to use a different LLM entirely! LlamaIndex has integrations with dozens of LLMs, both APIs and local.