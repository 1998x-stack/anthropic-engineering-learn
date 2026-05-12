---
title: "LlamaIndex Turns 1: Big Milestones And Growth | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-turns-1-f69dcdd45fe3"
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







It’s our birthday! One year ago, Jerry pushed his [first commit](https://github.com/run-llama/llama_index/tree/2e62c6987808797611e9bb7c1ae8c86e72a88727) to GPT Index, the project that would become LlamaIndex. It worked with GPT-3, the state of the art model available at the time. That initial version was very simple, but the problem statement — and the solution — remain the same:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



>

*one fundamental limitation of GPT-3 is the context size […] the ability to feed “knowledge” to GPT-3 is mostly limited to this limited prompt size […] But what if GPT-3 can have access to potentially a much larger database of knowledge[…]?*

Twelve months have passed and there’s been a tsunami of new developments in the world of generative AI and LLMs, but the reason LlamaIndex was invented remains: even the most sophisticated model isn’t trained on **your** data, which can be locked behind an API or in a SQL database, and even the latest GPT-4-Turbo context size of 128,000 tokens isn’t enough to hold even a relatively modest dataset. Retrieval-Augmented Generation (RAG) is here to stay.

# Big numbers

At just 1 year old, LlamaIndex has gotten very big. How big? Here’s some numbers:

- Over [450 contributors](https://github.com/run-llama/llama_index/graphs/contributors) to our open-source library!
- Nearly 3,000 open-source projects [depend on LlamaIndex](https://github.com/run-llama/llama_index/network/dependents)!
- Nearly 4,000 members in our Discord ([come join us!](https://discord.com/invite/eN6D2HQ4aX))
- 47,000 lines of Python in the library! (Don’t worry, it’s still just [0.5MB to download](https://pypi.org/project/llama-index/#files))
- Nearly [900,000 downloads every month](https://pypistats.org/packages/llama-index)!
- RAG deployed among [popular](https://openbb.co/blog/breaking-barriers-with-openbb-and-llamaIndex) [open-source](https://github.com/imartinez/privateGPT) [projects](https://github.com/TransformerOptimus/SuperAGI), as well as in [production](https://www.gunder.com/news/gunderson-dettmer-launches-chatgd-a-homegrown-generative-ai-chat-app-to-its-lawyers/) in [enterprise](https://www.springworks.in/albus/) [settings](https://mqube.com/blog/4-lessons-from-launching-an-llm-chatbot).

# Big thanks

But big numbers aside, the thing we’re proudest of is our community: we have users in (nearly) every country in the world, from single hobby developers to Fortune 500 companies and everyone in between. LlamaIndex’s founder, Jerry Liu, says:

>

*Our community is everything at LlamaIndex. We love seeing the amazing things people are building every day! It’s what gets us up in the morning and keeps us motivated to keep pushing the boundaries of what developers can do with GenAI. And we’re especially grateful to the developers who give back by pushing PRs, issues and bug reports. They’re what makes the open source world go round.*

# Big milestones

What’s happened in a year? Well, everything! But here’s some highlights:

- November 2022: Launched [GPT Tree Index](https://twitter.com/jerryjliu0/status/1590192512639332353?lang=en), a way of organizing information into a tree. Based on the initial interest/traction, we expanded this into a List Index and Keyword Index. Then ChatGPT launched in November
- December 2022: Some big feature releases: support for [indexing embeddings + vector stores](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing.html#what-is-an-embedding), and initial data loaders for Notion, Slack, and Google Drive
- January 2023: LlamaIndex hits Github trending for the first time!
- February 2023: We launched [LlamaHub](https://x.com/jerryjliu0/status/1622981509849444354?s=20) with Jesse Zhang, containing an initial repository of data loaders for users to access. We ran a sweepstakes with OctoML and got 50+ data loader submissions!
- March 2023: [ChatGPT API launched](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) and then [Plugins](https://openai.com/blog/chatgpt-plugins). We scrambled to support the new API + [Plugin](https://gpt-index.readthedocs.io/en/v0.6.3/how_to/integrations/chatgpt_plugins.html) integrations.
- April 2023: We incorporated!
- May 2023: At the end of April, we launched [0.6.0](https://betterprogramming.pub/llamaindex-0-6-0-a-new-query-interface-over-your-data-331996d47e89), where we completely rewrote the entire framework from the ground-up for greater modularity and composability for different levels of abstraction.
- June 2023: We announced that we raised $8.5M in funding!
- July 2023: We launched [Data Agents](/data-agents-eed797d7972f) + Agent Tools on LlamaHub. We also launched a [Typescript package](https://x.com/jerryjliu0/status/1683560483071328256?s=20)
- August 2023: We integrated with [OpenAI fine-tuning and launched a variety of LLM and embedding fine-tuning abstractions](https://x.com/jerryjliu0/status/1694370574808887496?s=20).
- September 2023: We [launched](https://twitter.com/llama_index/status/1699116440056651976) [secinsights.ai](http://secinsights.ai) — a production-ready full-stack application
- October 2023: We launched [LlamaIndex Chat](https://twitter.com/jerryjliu0/status/1719022164203196824) — a full-stack Typescript template.
- November 2023: Went [fully multi-modal](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal.html) with the release of GPT-4-vision!

# Big plans

With all that growth and all those features, what’s next for us? Stay tuned!