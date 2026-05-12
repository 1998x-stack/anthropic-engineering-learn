---
title: "Doubling down on Deep Agents"
author: "LangChain Accounts"
date: "2025-10-28"
url: "https://www.langchain.com/blog/doubling-down-on-deepagents"
---

Deep Agents

# Doubling down on Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 28, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa51703c727fd28ad682_Doubling-down-on-DeepAgents.png)Two months ago [we wrote about Deep Agents](https://blog.langchain.com/deep-agents/) - a term we coined for agents that are able to do complex, open ended tasks over longer time horizons. We hypothesized that there were four key elements to those agents: a planning tool, access to a filesystem, subagents, and detailed prompts.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa52703c727fd28ad70b_Visual-1-2.png)

We launched [`deepagents`](https://github.com/hwchase17/deepagents?ref=blog.langchain.com) as an Python package that had a base of all these elements, so that you would only have to bring your custom tools and a custom prompt and you could build a Deep Agent easily.

We&#x27;ve seen strong interest and adoption, and today we&#x27;re excited to double down with a 0.2 release. In this blog we want to talk about whats new in 0.2 release compared to the launch, as well as when to use [`deepagents`](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com) (vs [`langchain`](https://docs.langchain.com/oss/python/langchain/overview?ref=blog.langchain.com) or [`langgraph`](https://docs.langchain.com/oss/python/langgraph/overview?ref=blog.langchain.com))

## **Pluggable Backends**

The main new addition in 0.2 release comes in the form of pluggable backends. Previously, the &quot;filesystem&quot; that `deepagents` had access to was a &quot;virtual filesystem&quot;. It would use LangGraph state to store files.

In 0.2, we have a new `Backend` abstraction, which allows you to plug in anything as the &quot;filesystem&quot;. Built in implementations include:

- LangGraph State
- LangGraph Store (cross thread persistence)
- The actual local filesystem

We&#x27;ve also introduced the idea of a &quot;composite backend&quot;. This allows you to have a base backend (eg local filesystem) but then map on top of it other backends at certain subdirectories. An example use case of this is to empower long term memory. You could have a local filesystem as a base backend, but then map all file operations in `/memories/` directory to an s3 backed &quot;virtual filesystem&quot;, allowing your agent to add things there and have them persist beyond your computer.

You can write your own backend to create a &quot;virtual filesystem&quot; over any database or any data store you want.

You can also subclass an existing backend and add in guardrails around which files can be written to, format checking for these files, etc.

## Other things in 0.2

We also added a number of other improvements making their way to `deepagents` in the 0.2 release:

- [Large tool result eviction](https://docs.langchain.com/oss/python/deepagents/harness?ref=blog.langchain.com#large-tool-result-eviction): automatically dump large tool results to the filesystem when they exceed a certain token limit.
- [Conversation history summarization](https://docs.langchain.com/oss/python/deepagents/harness?ref=blog.langchain.com#conversation-history-summarization): automatically compress old conversation history when token usage becomes large.
- [Dangling tool call repair](https://docs.langchain.com/oss/python/deepagents/harness?ref=blog.langchain.com#dangling-tool-call-repair): fix message history when tool calls are interrupted or cancelled before execution.

## When to use deepagents vs LangChain, LangGraph

This is now our third open source library we are investing in, but we believe that all three serve different purposes. In order to distinguish these purposes, we will likely refer `deepagents` as an &quot;agent harness&quot;, `langchain` as an &quot;agent framework&quot;, and `langgraph` as an agent runtime.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa52703c727fd28ad70e_Visual-2.png)

LangGraph is great if you want to build things that are combinations of workflows and agents.

LangChain is great if you want to use the core agent loop without anything built in, and built all prompts/tools from scratch.

Deep Agents is great for building more autonomous, long running agents where you want to take advantage of built in things like planning tools, filesystem, etc.

They built on top of each other - `deepagents` is built on top of `langchain`&#x27;s agent abstraction, which is turn is built on top of `langgraph`&#x27;s agent runtime.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa51703c727fd28ad705_Visual-3-5.png)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ea236ce872ec8be413bd2f_runtime-behind-production-deep-agents-thumbnail.png)Conceptual GuideDeep Agents

#### The runtime behind production deep agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Sydney RunkleVivek TrivedyApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)24min[](/blog/runtime-behind-production-deep-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)