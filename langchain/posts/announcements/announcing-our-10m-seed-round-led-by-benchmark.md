---
title: "Announcing our $10M seed round led by Benchmark"
author: "LangChain Accounts"
date: "2023-04-04"
url: "https://www.langchain.com/blog/announcing-our-10m-seed-round-led-by-benchmark"
---

Company Announcements

# Announcing our $10M seed round led by Benchmark

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 4, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)It was only six months ago that we released the first version of LangChain, but it seems like several years. When we launched, generative AI was starting to go mainstream: stable diffusion had[ just been released](https://stability.ai/blog/stable-diffusion-public-release?ref=blog.langchain.com) and was captivating people’s imagination and fueling an explosion in developer activity, Jasper [announced a funding round](https://www.prnewswire.com/news-releases/jasper-announces-125m-series-a-funding-round-bringing-total-valuation-to-1-5b-and-launches-new-browser-extension-301651733.html?ref=blog.langchain.com), and investors released the first [Gen AI market maps](https://www.sequoiacap.com/article/generative-ai-a-creative-new-world/?ref=blog.langchain.com).

Alongside this boon in content creation, people started to realize that the true power of this technology was not using a language model in isolation, but using the language model as part of a new, more intelligent system. Developers were discussing how to connect language models to their own proprietary documents, APIs, and structured data. Research papers like [Self-Ask with Search](https://twitter.com/OfirPress/status/1577302733383925762?s=20&amp;ref=blog.langchain.com) and[ ReAct](https://blog.langchain.com/content/files/abs/2210.xml) were published, demonstrating the power of these approaches.

Amongst these early tremors of a tectonic shift in computing, we released the first version of the LangChain Python package on October 24th, 2022. In the very first [tweet thread](https://twitter.com/hwchase17/status/1584925380976091137?s=20&amp;ref=blog.langchain.com), Harrison said:

- “a python package aimed at helping build LLM applications through composability”
- “The real power comes when you are able to combine [LLMs] with other things.”
- “LangChain aims to help with that by creating… a comprehensive collection of pieces you would ever want to combine… a flexible interface for combining pieces into a single comprehensive ‘chain’”

## **Why Raise Funding?**

This all started as an open-source side project, without any intention of building a company. It began by noticing common patterns in how people were approaching problems, and attempting to create abstractions that made it easier. These first simple abstractions struck a chord and the project took off, thanks largely to your community support and contributions. LangChain now has over 20K stars on GitHub, 10K active Discord members, over 30K followers on Twitter, and - most importantly - over 350 contributors.

It became clear that the combination of LangChain + LLMs blows open the frontier of amazing products and applications to be built. And, it also is clear that far more work and tooling are needed to make these applications work well (particularly in production). You’re asking us every day for more (400+ GitHub issues, 100 open PRs) and we want to help!

With that in mind, we are excited to publicly announce that we have raised $10 million in seed funding. Benchmark led the round and we’re thrilled to have their counsel as they’ve been the first lead investors in some of the iconic open source software we all use including Docker, Confluent, Elastic, Clickhouse and more. With this capital we are going to invest aggressively to keep up with the ground breaking work the community is doing building intelligent apps. Our goal is simple: empower developers to build useful applications powered by language models.

So what can you expect from us?

## **LangChain Today**

LangChain is a framework for developing applications powered by language models, offered as both a [Python](https://github.com/hwchase17/langchain?ref=blog.langchain.com) and a [TypeScript](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com) package. We believe that the most powerful and differentiated language model applications will:

- Be data-aware: connect a language model to other sources of data
- Be agentic: allow a language model to interact with its environment

The LangChain framework is designed with the above objective principles in mind. We believe that the two main value props it provides are:

### **Components**

LangChain offers a modular set of abstractions and components that provide everything developers need to build applications using language models. It also includes collections of implementations for these abstractions.

These components are largely community driven. There are over 300 contributors on the Python repo alone. Some highlights:

- Integrations with [20+ different model providers](https://python.langchain.com/docs/modules/model_io/models/?ref=blog.langchain.com) or hosting platforms
- Collection of [50+ Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com) to load data from different sources
- Collection of [10+ methods for splitting text](https://python.langchain.com/docs/modules/data_connection/document_transformers/?ref=blog.langchain.com) data into chunks so that a Language Model can easily use it
- Integrations with [10+ different vector databases](https://python.langchain.com/docs/modules/data_connection/vectorstores/?ref=blog.langchain.com)
- Collection of [15+ different tools](https://python.langchain.com/docs/modules/agents/tools/?ref=blog.langchain.com) to let Language Models use

### **Pre-built Chains and Agents**

Chains allow developers to assemble components in a specific manner to accomplish a particular task, such as summarizing a large pdf document or querying a SQL database. Agents can be thought of as “dynamic chains” in which the sequence of steps taken are determined by a language model on the fly. In addition to providing a high-level interface that makes it easy for developers to create custom chains and agents, LangChain provides many pre-built ones that can be used out-of-the-box.

Again, these components are largely community driven. Some highlights:

- Implementations of [~20 different chains](https://python.langchain.com/docs/modules/chains/?ref=blog.langchain.com)
- Implementations of [6 different generic agent types](https://python.langchain.com/docs/modules/agents/?ref=blog.langchain.com) (chains specifically designed to use tools and interact with the outside world)
- Implementations of [7 different “Agent Toolkits”](https://python.langchain.com/docs/modules/agents/toolkits/?ref=blog.langchain.com) (agents equipped with a specific set of tools to accomplish a specific task)

## **Future Plans**

As mentioned earlier, we believe that language models are unlocking new types of high-value applications, and it is still non-trivial to create and maintain these applications — particularly in production settings. Some of our more recent releases are focused on addressing these problems:

- Bringing the TypeScript package up to feature parity with Python to enable more full-stack and frontend developers to create LLM applications
- Implementing several types of [OutputParsers](https://python.langchain.com/docs/modules/model_io/output_parsers/?ref=blog.langchain.com), to allow for more safety and guidance on the text returned by a LLM
- Introducing a [Retriever abstraction](https://blog.langchain.com/retrieval/) to enable more complicated and necessary types of document retrieval
- Building integrations with solutions like Weights &amp; Biases, AIM, ClearML to enable more observability and experimentation with LLM applications

We will continue to add features to LangChain and provide other offerings that will:

- Make it easy to quickly prototype applications.
- Bridge the gap between prototyping and putting something into production.

We’re incredibly excited to see what will be built and to do more to support you. We are also especially grateful to the entire LangChain community. LangChain will continue to be open-source and focused on developers — our funding allows us to allocate more resources to take it to the next level. If this mission and journey sounds interesting to you, we are [actively hiring founding engineers](https://docs.google.com/forms/d/e/1FAIpQLScrz8YeKJI6F5bnM1Mvq4wkK91f0RQPVIvXBDULeqbQSwJ0tQ/viewform?usp=sf_link&amp;ref=blog.langchain.com). If you have suggestions on new features or are interested in evaluating and running your LangChain applications in production, we’d especially love to hear from you at support@langchain.dev!

Thank you for everything so far, and let’s build some cool stuff 🙂

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)