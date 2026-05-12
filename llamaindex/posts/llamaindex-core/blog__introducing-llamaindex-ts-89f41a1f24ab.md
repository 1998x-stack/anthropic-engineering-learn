---
title: "LlamaIndex.TS: TypeScript Library Guide For LLM Apps | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llamaindex-ts-89f41a1f24ab"
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







We are beyond excited to announce v0.0.1 of [**LlamaIndex.TS**](https://github.com/run-llama/LlamaIndexTS/), a Typescript first library focused on helping you use your private data with large language models.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



## **What is LlamaIndex?**

Our core goal for LlamaIndex is to help developers easily integrate their data with Large Language Models (LLMs). LLMs, like ChatGPT, have been a revolution in the way we think about handling textual input and data, but all of them have the limitation in what data they have access to. In addition to the “knowledge cutoff” (we are nearing the 2 year anniversary for when ChatGPT’s latest data was trained) LLMs can’t access data from your companies, from your personal analyses, or from the data your users generate.

With LlamaIndex.TS, we look to achieve that goal by meeting developers at their (my) language of choice, in this case Typescript. We are committed to making this library the easiest to use, most robust solution out there for using data with LLMs.

## **Backstory**

It was at the Emergency ChatGPT Hackathon hosted by Pete Huang and Rachel Woods that I met Jerry. Having worked in the JS world for the last 8 years, my first question was “why don’t you build this in Javascript?” After he demurred, he very patiently guided me through setting up the Python dev environment. (I think it took us 20 minutes before we figured it all out!) So, when Jerry offered to let me build LlamaIndex.TS I obviously couldn’t turn him down. Can’t wait to see what you build with it!

## **Design**

At a high level, LlamaIndex.TS first takes the file inputs, loads them into a standardized format, and creates an Index (knowledge base).

![](/blog/images/1*fn3F-QZ3Wu9P8ZWfHH6-gQ.jpeg)

We then retrieve the relevant information from the index and use that in our query to the LLM to generate more a grounded response.

![](/blog/images/1*bP7gDSU4l2E9QyBF8nPBMg.jpeg)

Check out [our docs](https://ts.llamaindex.ai/) for a more in depth explanation!

## Playground

We are building an open source playground for LlamaIndex.TS. Please check it out at [https://llama-playground.vercel.app/](https://llama-playground.vercel.app/) PRs are welcome here! [https://github.com/run-llama/ts-playground](https://github.com/run-llama/ts-playground)

## **Main Differences from LlamaIndex Python**

- All function names are 🐪 camel cased.
- The prompt interface is much simpler and uses native javascript template literals.
- We do not ship non-async versions of functions. Please use await or .then callbacks.
- We use interfaces and POJOs in lieu of classes where it makes sense. For example, ChatEngine, a base class in Python is an interface in JS. ServiceContext, a class in Python is an interface/POJO in JS.

## **Runtimes**

Currently, we support NodeJS v18 and up. Lots of plans on this front though. Stay tuned!

## **Contributing**

Only the core features are built out so far, so there is a lot of work that needs to be done on the loader and integration side. If you’re interested in contributing, please send us a message or even better a PR!

[https://github.com/run-llama/LlamaIndexTS](https://github.com/run-llama/LlamaIndexTS)