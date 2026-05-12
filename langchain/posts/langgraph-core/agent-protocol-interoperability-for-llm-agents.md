---
title: "Agent Protocol: Interoperability for LLM agents"
author: "LangChain Accounts"
date: "2024-11-19"
url: "https://www.langchain.com/blog/agent-protocol-interoperability-for-llm-agents"
---

LangGraph

# Agent Protocol: Interoperability for LLM agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaNovember 19, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3f07bc92c96efbbea3_Theme-Core-Spectrum--Format-Blog--Colour-Black--Text-Alignment-Centred--With-Image-Text-Only-1.png)LangGraph is a multi-agent framework. This means not only interacting with other LangGraph agents, but all other types of agents as well, regardless of how they are built. Today we are taking a few steps to build towards this vision. We are announcing:

- [**Agent Protocol**](https://github.com/langchain-ai/agent-protocol?ref=blog.langchain.com): a common interface for agent communication. This standardizes how agents (LangGraph or otherwise) can interact.
- [A guide](https://langchain-ai.github.io/langgraph/how-tos/local-studio/?ref=blog.langchain.com) and [video](https://youtu.be/o9CT5ohRHzY?ref=blog.langchain.com) showing how to connect LangGraph Studio to a locally running agent. This exposes a locally running server (implementing the Agent Protocol) to make it easier for everyone to use LangGraph Studio.
- [A guide](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/?ref=blog.langchain.com) showing how to use other frameworks (like AutoGen, CrewAI, and others) as sub-agents within a LangGraph agent.
- [A guide](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/?ref=blog.langchain.com) showing how to deploy other frameworks (like AutoGen, CrewAI, and others) using LangGraph Platform, taking advantage of the infrastructure we have built there.

## Agent Protocol: a standard way for agents to communicate

While we think LangGraph is the best way to build agents, we also recognize that there are plenty of other ways to do so. The vast majority of people not using LangGraph roll their own implementations, but we also see people using other frameworks like AutoGen, OpenAI&#x27;s Assistant API, CrewAI, LlamaIndex, and others.

This means most agents expose different APIs. As we move towards multi-agent world, this lack of uniformity poses an issue. [Communication is all you need](https://blog.langchain.com/communication-is-all-you-need/), but varying APIs make standard communication challenging.

In an effort to change this, we are open-sourcing an [**Agent Protocol**](https://github.com/langchain-ai/agent-protocol?ref=blog.langchain.com) - a standard interface for agent communication. Agent Protocol is our attempt at codifying the framework-agnostic APIs that are needed to serve LLM agents in production. These APIs center around concepts we think are central to reliably deploying agents:

- Runs: APIs for executing an agent
- Threads: APIs to organize multi-turn executions of agents
- Store: APIs to work with long-term memory

Any agent developer can implement this protocol - whether they are using LangGraph, a different framework, or no framework at all.

## Using Agent Protocol to connect LangGraph Studio to a locally running agent

A few months ago we released LangGraph Desktop - &quot;the first agent IDE.&quot; This UI allows you to visualize, interact with, and debug your LangGraph applications. When we initially released it as part of LangGraph Cloud, we soon realized it would provide more value running locally. This would allow you to pause execution mid-graph, change the underlying code, and rerun within a tight, low-latency feedback loop.

As innovative as LangGraph Desktop was, it suffered from three usability issues. First: it was available for Mac only. Second: it used Docker under the hood (more resource-intensive and slower to start up). Third: it ran in a separate Docker environment (not in your local environment &amp; harder to debug).

Today we&#x27;re excited to announce a version of LangGraph Studio that solves those issues. It is installable as Python package, and runs the backend locally inside your environment. This makes it usable on all platforms, and doesn&#x27;t require Docker. It connects to a web version of the Studio frontend. Note that your LangGraph application runs entirely locally and no data is sent to our servers.

You can install it with:

`pip install &quot;langgraph-cli[inmem]==0.1.55&quot;`

And you can run it with:

`langgraph dev`

For more information on installation and usage, [see here](https://langchain-ai.github.io/langgraph/how-tos/local-studio/?ref=blog.langchain.com). For more information on using the Studio to effectively debug your LangGraph applications, see our [YouTube video here](https://youtu.be/o9CT5ohRHzY?ref=blog.langchain.com).

The locally running server that `langgraph-cli` spins up implements the Agent Protocol, and LangGraph Studio will connect to any servers that implement the Agent Protocol.

## Integrating LangGraph with AutoGen, CrewAI, and other frameworks

LangGraph is a framework for building agentic and multi-agent applications. This includes integrating with other agent frameworks.

We&#x27;ve released [a new guide](https://langchain-ai.github.io/langgraph/how-tos/autogen-integration/?ref=blog.langchain.com) showing how to integrate LangGraph with other frameworks. The framework we show off integrating with is AutoGen, but this can easily be done with other frameworks.

At a high level, the way this works is by wrapping the other agent inside a LangGraph node. LangGraph nodes can be anything - arbitrary code. This makes it easy to define an AutoGen (or CrewAI, or LlamaIndex, or other framework) agent and then reference it inside your graph. This allows you to create multi-agent systems where some of the sub-agents are actually defined in other frameworks.

## Using LangGraph Platform to deploy AutoGen, CrewAI, and other frameworks

LangGraph Platform provides infrastructure for deploying agents. This integrates seamlessly with LangGraph, but can also work with other frameworks. The way to make this work is to wrap the agent in a single LangGraph node, and have that be the entire graph.

Doing so will allow you to deploy to LangGraph Platform, and allows you to get a lot of the benefits. You get horizontally scalable infrastructure, a task queue to handle bursty operations, a persistence layer to power short term memory, and long term memory support.

See our guide [here](https://langchain-ai.github.io/langgraph/how-tos/autogen-langgraph-platform/?ref=blog.langchain.com) for how to do this integration.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa18703c727fd28ab4de_Vodafone-Italy---Oct-2025--1-.png)Case StudiesLangGraphLangSmith

#### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/customers-vodafone-italy)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)