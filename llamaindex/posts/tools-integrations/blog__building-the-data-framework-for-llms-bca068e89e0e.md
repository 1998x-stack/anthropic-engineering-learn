---
title: "LLM Data Framework: How to Build With Private Data | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-the-data-framework-for-llms-bca068e89e0e"
category: "tools-integrations"
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



   1



Today is an exciting day for LlamaIndex, and a big milestone in my personal journey with generative AI. I’ve followed generative models for most of my academic/professional career — from [my research on GANs/sensor compression](https://scholar.google.com/citations?user=8JjemawAAAAJ&amp;hl=en) to following [Transformers](https://arxiv.org/abs/1706.03762)/[GPT](https://openai.com/blog/gpt-3-apps) [developments](https://openai.com/blog/chatgpt). It became increasingly clear that as these models got bigger/better, they were evolving from knowledge generators to intelligent engines that could reason/act over new information.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



I formalized some of these key intuitions more concretely:

- LLMs are fantastic reasoning engines, capable of question-answering, summarization, planning, and more. They had the promise of becoming the “neural” compute unit at the core of a new age of AI-enabled software.
- Yet, LLMs inherently have no awareness of your own data.
- No one really knew the best practices for feeding your data into the LLM. Models had limited context windows and were expensive to finetune.

If we could offer a toolkit to help set up the data architecture for LLM apps, then we could enable anyone to build LLM-powered knowledge workers and transform the way that software is written over private data. LLM-enabled software requires new infrastructure tooling over your data and has significant implications for the modern software data stack.

Determined to tackle this challenge, I built GPT Index (which we later rebranded to LlamaIndex), an initial exploratory effort to organize and retrieve information using LLMs. ([first Tweet is here](https://twitter.com/jerryjliu0/status/1590192512639332353?s=20)!)

It happened at the perfect time. Since last November, there has been an explosion in developer interest in building applications on top of LLMs. Most developers were figuring out ways to leverage the reasoning capabilities of LLMs on top of their own private data. Just two months in, I joined forces with Simon Suo, a brilliant AI technologist and my former colleague, and we evolved LlamaIndex from an exploratory project into a comprehensive framework designed to connect a user’s private data with LLMs. It gained recognition within the AI community, captivating the attention of hackers, developers, and industry experts alike. In just six months, the project garnered an impressive following, with [16K Github Stars](https://github.com/jerryjliu/llama_index), [20K Twitter followers](https://twitter.com/llama_index), [200K monthly downloads](https://pypi.org/project/llama-index/), and [6K active Discord users](https://discord.gg/dGcwcsnxhU). Companies like Instabase, Front, and Uber started experimenting with LlamaIndex on top of their data.

Some initial stacks started to emerge — for instance a common paradigm for building QA systems and chatbots was using a simple retrieval mechanism (top-k lookup from a vector database) with an LLM. LlamaIndex became viewed as a [critical](https://medium.com/cowboy-ventures/the-new-infra-stack-for-generative-ai-9db8f294dc3f) [data](https://www.unusual.vc/post/devtools-for-language-models) [orchestration](https://www.madrona.com/foundation-models/) [component](https://foundationcapital.com/foundation-model-ops-powering-the-next-wave-of-generative-ai-apps/) of the emerging LLM software landscape.

Yet, it became clear that there were still significant technical challenges in the space of LLMs and data, and no one had the right answers. Even with the capable toolkit that we’ve developed, we were just starting to scratch the surface on unlocking value from data.

We are thrilled to share that LlamaIndex has secured $8.5 million in seed funding, led by Greylock, to help propel these efforts further. We’re excited to work with Jerry Chen, Saam Motamedi, and Jason Risch on the Greylock team. Joining us in this exciting journey are Jack Altman (CEO of Lattice), Lenny Rachitsky (Lenny’s Newsletter), Mathilde Collin (CEO of Front), Raquel Urtasun (CEO of Waabi), Joey Gonzalez (Berkeley), and many others. Their belief in our vision and the impact of LlamaIndex on the future of AI fuels our passion in solving these data + AI problems.

# **Why LlamaIndex?**

Calling an LLM API is easy. Setting up a software system that can extract insights from your private data is harder.

LlamaIndex is the advanced data framework for your LLM applications. It encompasses essential features allowing you to both manage and query your data.

- **Data Management: **Data ingestion, data parsing/slicing, data storage/indexing.
- **Data Querying: **Data retrieval, response synthesis, multi-step interactions over your data.

LlamaIndex allows you to seamlessly integrate individual or enterprise data, including files, workplace apps, and databases, with LLM applications. We also offer an extensive array of integrations with other storage providers and downstream applications.

- 100+ data loaders
- 13+ vector database providers
- Integrations with observability and experimentation frameworks (e.g. prompt tracking and system tracing)
- Integrations as a [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/datastore/providers/llama_datastore.py) or with [Poe](https://github.com/poe-platform/poe-protocol/tree/main/llama_poe)

The end result is that you can build a variety of amazing knowledge-intensive LLM applications. This ranges from a search engine over your data, to chatbot-style interfaces, to structured analytics helpers, to autonomous knowledge agents.

# **What’s next?**

There are *so *many things that we want to do to more fully realize our vision of unlocking LLM capabilities on top of your data. We’ll broadly break this down into two categories: 1) our continued commitment to the open-source developer community, and 2) solving the data problem at scale for enterprises.

## **Build the best open source data framework and developer community**

At a high-level, we want to continue iterating on our core feature capabilities, improving reliability, and satisfy both the needs of beginner and advanced users.

- **Handle complex queries:** We want to continue advancing the idea of “querying your data”, whether it’s through leveraging agent-style interactions for data retrieval and synthesis or program synthesis/DSL.
- **Multi-modal data management:** The future of foundation models is multimodal, not just contained to LLMs. There are many types of semi-structured data (e.g. semi-structured data like JSONs, yaml files) as well as “complex” unstructured data (audio, images, video) that we’d love to have native support for.
- **Better evaluation of LLM data systems: **Properly evaluating LLM calls is already tricky (how do you best evaluate the quality of a generated output? Some [libraries](https://github.com/openai/evals) for handling this). This becomes even more tricky when you chain LLM calls within an overall data system. We want to invest efforts into this area to provide greater transparency to our users.
- **Optimization of Latency/Cost: **Users are faced with a plethora of choices when it comes to building a data-driven LLM app: the choice of LLM model, embedding model, vector database, etc. They must choose in accordance to a variety of factors, from latency and cost to privacy.
- **Ease of use for both beginner users and advanced users: **Our goal is to make the utilization of LLM capabilities accessible and user-friendly for individuals at all skill levels. We will develop clear tutorials, examples, and tools to simplify the learning curve and convey the value of all of our features.

## **Solving the data problem at scale for Enterprises**

As we’re iterating on the open-source project, we also want to identify the surrounding pain points in being able to build and deploy data-powered LLM apps to production. Our solution to this will build upon the success of our open-source project and be a natural evolution to the enterprise setting.

- **Production-ready data ingestion and management:** We want to handle data updates, data consistency, and scalability to larger volumes of data parsing. We also want to continue expanding on the right storage abstractions for multi-modal data.
- **Scale to Large Data Volumes: **Enterprises will typically have orders of magnitude more data than an individual. We want to invest in hosted infrastructure/deployment solutions around our core package so that you don’t have to.
- **Domain-specific LLM solutions: **We want to offer packaged solutions to enable users to easily build LLM apps in different domains, from healthcare to finance to legal.

If you’re building LLM apps in the enterprise setting, we’d love to chat and learn more about pain points + desired features! Check out our [form here](https://docs.google.com/forms/d/1lzXIE9G07D9eoK7MBUpRuN-PdBYGA7nWVqcIvNtN9mQ/edit#responses).

# **Join the Llama Gang! 🦙**

Join the Llama(Index) gang as we embark on this journey to solve problems at the intersection of LLMs and data. We are not just building tools for ML practitioners/researchers; the emerging LLM + data architecture stacks have implications for *all* of software development. As a result, we are operating at the intersection of incredibly fun and challenging problems from a variety of different fields:

- Foundation Model Development
- Information Retrieval + Recommendation Systems
- Data Systems
- MLOps
- DevOps

Interested in checking out the project?

- Find our project on [Github](https://github.com/jerryjliu/llama_index) and check out our [Docs](https://gpt-index.readthedocs.io/en/latest/)
- Check out our brand new landing page: [https://llamaindex.ai](https://llamaindex.ai)
- Join our [Discord](https://discord.gg/dGcwcsnxhU) or Follow our [Twitter](https://twitter.com/llama_index)

Also, we’re hiring!

- We’re looking for founding engineers — experience in one or more of AI, data systems, and full-stack/front-end is nice to have but not a requirement.
- If you’re interested, [fill out our form here](https://docs.google.com/forms/d/e/1FAIpQLScpSqZvTincCsspY5CyY_9gAGXnQfTS7HQvsgVQccncCJ7x5w/viewform?usp=sf_link).