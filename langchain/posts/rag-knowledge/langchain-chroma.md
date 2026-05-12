---
title: "LangChain + Chroma"
author: "LangChain Accounts"
date: "2023-02-13"
url: "https://www.langchain.com/blog/langchain-chroma"
---

PartnerLangChain

# LangChain + Chroma

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 13, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25f3fe3e9a95a565d26_langchain-chroma-light.png)Today we’re announcing LangChain&#x27;s integration with Chroma, the first step on the path to the Modern A.I Stack.

### LangChain - The A.I-native developer toolkit

We started LangChain with the intent to build a modular and flexible framework for developing A.I-native applications. Some of the use cases which immediately jumped to mind are [chat bots](https://python.langchain.com/docs/use_cases/chatbots/?ref=blog.langchain.com), [question answering](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) services, and [agents](https://python.langchain.com/docs/use_cases/agents/?ref=blog.langchain.com). Thousands of developers are now hacking, tinkering, and building all kinds of LLM-powered applications using LangChain’s flexible, easy to use framework.

One of the key components of those of applications is embeddings, and vector stores to hold and work with those embeddings.

One pain point that we noticed with a lot of existing vector stores is they often involved connecting to an external server that stored the embeddings. While that is fine for putting applications into production, it does make it a bit tricky to easily prototype applications locally.

The best solution we had for local vector stores was using FAISS, which many community members noted had some tricky dependencies that caused installation issues.

### [Chroma](https://www.trychroma.com/?ref=blog.langchain.com) - The A.I-native vector store

Chroma was founded to build tools which leverage the power of embeddings. Embeddings are the A.I-native way to represent any kind of data, making them the perfect fit for working with all kinds of A.I-powered tools and algorithms.

While exploring the possibilities of model embeddings at Chroma, the Chroma team needed an easy to use, performant, and lightweight vector store which could handle modern A.I workloads.

While there are already several vector database solutions, they found that these were mostly geared to other use-cases and access patterns, like large-scale semantic search. Additionally, they were often a hassle to set up and run, especially in a development environment.

In short, the Chroma team didn’t find what we needed, **so Chroma built it.**

Chroma is a vector store and embeddings database designed from the ground-up to make it easy to build AI applications with embeddings. It comes with [everything you need to get started built in](https://docs.trychroma.com/getting-started?ref=blog.langchain.com), and runs on your machine - just `pip install chromadb`!

### LangChain and Chroma

Working together, with our mutual focus on flexibility and ease of use, we found that LangChain and Chroma were a perfect fit.

Specifically, LangChain provides a framework to easily prototype LLM applications locally, and Chroma provides a vector store and embedding database that can run seamlessly during local development to power these applications.

Today, we are announcing Chroma’s integration with LangChain. Chroma aims to be the first, easiest, and best choice for most developers building LLM apps with LangChain. It’s ready to use today! Just get the latest version of LangChain, and `from langchain.vectorstores import Chroma` and you&#x27;re good to go!

To help get started, we put together an [example GitHub repo](https://github.com/hwchase17/chroma-langchain?ref=blog.langchain.com) for you to play around with.

### The Future

The launch of StableDiffusion and ChatGPT sparked an explosion of A.I creativity. Today, thousands of people around the world are working on discovering and unlocking the full power of A.I. At the same time, A.I research continues at a blistering pace. More kinds of data, more ways to interact with A.I, and more insights about how the models work, are being invented every day.

There’s no doubt this is a transformative era, not just in how we build software, but in what’s possible. LangChain and Chroma will remain on the forefront.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)