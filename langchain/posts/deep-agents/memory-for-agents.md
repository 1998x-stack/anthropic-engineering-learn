---
title: "Memory for agents"
author: "LangChain Accounts"
date: "2024-10-19"
url: "https://www.langchain.com/blog/memory-for-agents"
---

Harrison&#x27;s In the Loop

# Memory for agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseOctober 19, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf3ed2a13d9d6050877f_Screenshot-2024-10-19-at-9.59.50-AM.png)*At Sequoia’s AI Ascent conference in March, I talked about three limitations for agents: planning, UX, and memory. Check out that talk *[*here*](https://www.youtube.com/watch?v=pBBe1pk8hf4&amp;ref=blog.langchain.com)*. In this post I will dive more into memory. See the previous post on planning *[*here*](https://blog.langchain.com/planning-for-agents/)*, and the previous posts on UX *[*here*](https://blog.langchain.com/ux-for-agents-part-1-chat-2/)*, *[*here*](https://blog.langchain.com/ux-for-agents-part-2-ambient/)*, and *[*here*](https://blog.langchain.com/ux-for-agents-part-3/)*.*

If agents are the biggest buzzword of LLM application development in 2024, memory might be the second biggest. But what even is memory?

At a high level, memory is just a system that remembers something about previous interactions. This can be crucial for building a good agent experience. Imagine if you had a coworker who never remembered what you told them, forcing you to keep repeating that information - that would be insanely frustrating!

People often expect LLM systems to innately have memory, maybe because LLMs feel so human-like already. However, LLMs themselves do NOT inherently remember things — so you need to intentionally add memory in. But how exactly should you think about doing that?

## Memory is application-specific

We’ve been thinking about memory for a while, and we believe that memory is application-specific.

What [Replit’s coding agent](https://blog.langchain.com/customers-replit/) may choose to remember about a given user is very different than what [Unify’s research agent](https://blog.langchain.com/unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith/) might remember. Replit may choose to remember Python libraries that the user likes; Unify may remember the industries of the companies a user is researching.

Not only does **what** an agent remember vary by application, but **how** the agent remembers may differ too. As discussed in [a previous post](https://blog.langchain.com/ux-for-agents-part-1-chat-2/), a key aspect of agents is the UX around them. Different UXs offer distinct ways to gather and update feedback accordingly.

So, how are we approaching memory at LangChain?

💡

Much like our approach to agents: we aim to give users low-level control over memory and the ability to customize it as they see fit.

This philosophy guided much of our development of the [Memory Store](https://blog.langchain.com/launching-long-term-memory-support-in-langgraph/), which we added into LangGraph last week.

## Types of memory

While the **exact** shape of memory that your agent has may differ by application, we do see different high level types of memory. These types of memory are nothing new - they mimic [human memory types](https://www.psychologytoday.com/us/basics/memory/types-of-memory?ref=blog.langchain.com).

There’s been some great work to map these human memory types to agent memory. My favorite is the [CoALA paper](https://arxiv.org/pdf/2309.02427?ref=blog.langchain.com). Below is my rough, ELI5 explanation of each type and **practical ways** for how todays agents may use and update this memory type.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf3ed2a13d9d60508789_download--23-.png)

Decision procedure diagram from CoALA paper (Sumers, Yao, Narasimhan, Griffiths 2024)

### Procedural Memory

This term refers to long-term memory for how to perform tasks, similar to a brain’s core instruction set.

Procedural memory in humans: remembering how to ride a bike.

Procedural memory in Agents: the CoALA paper describes procedural memory as the combination of LLM weights and agent code, which fundamentally determine how the agent works.

In practice, we don’t see many (any?) agentic systems that update the weights of their LLM automatically or rewrite their code. We do, however, see some examples of an agent updating its own system prompt. While this is the closest practical example, it remains relatively uncommon.

### Semantic Memory

This is someone’s long-term store of knowledge.

Semantic memory in humans: it’s composed of pieces of information such as facts learned in school, what concepts mean and how they are related.

Semantic memory in agents: the CoALA paper describes semantic memory as a repository of facts about the world.

Today, this is most often used by agents to personalize an application.

Practically, we see this being done by using an LLM to extract information from the conversation or interactions the agent had. The exact shape of this information is usually application-specific. This information is then retrieved in future conversations and inserted into the system prompt to influence the agent’s responses.

### Episodic Memory

This refers to recalling specific past events.

Episodic memory in humans: when a person recalls a particular event (or “episode”) experienced in the past.

Episodic memory in agents: the CoALA paper defines episodic memory as storing sequences of the agent’s past actions.

This is used primarily to get an agent to perform as intended.

In practice, episodic memory is implemented as few-shot example prompting. If you collect enough of these sequences, then this can be done via dynamic few-shot prompting. This is usually great for guiding the agent if there is a **correct** way to perform specific actions that have been done before. In contrast, semantic memory is more relevant if there isn’t necessarily a correct way to do things, or if the agent is constantly doing new things so the previous examples don’t help much.

## How to update memory

Besides just thinking about the type of memory to update in their agents, we also see developers thinking about **how** to update agent memory.

One way to update agent memory is [“in the hot path”](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#writing-memories-in-the-hot-path). This is where the agent system explicitly decides to remember facts (usually via tool calling) before responding. This is the approach taken by ChatGPT.

Another way to update memory is [“in the background”](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#writing-memories-in-the-background). In this case, a background process runs either during or after the conversation to update memory.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf3ed2a13d9d60508786_hot_path_vs_background--2-.png)

Comparing these two approaches, the “in the hot path” approach has the downside of introducing some extra latency before any response is delivered. It also requires combining the memory logic with the agent logic.

However, running in the background avoids those issues - there’s no added latency, and memory logic remains separate. But running “in the background” also has its own drawbacks: the memory is not updated immediately, and extra logic is needed determine when to kick off the background process.

Another way to updating memory involves user feedback, which is particularly relevant to episodic memory. For example, If the user marks an interaction as a positive one, you can save that feedback to recall in the future.

## Why do we care about memory for agents?

How does this impact what we’re building at LangChain? Well, memory greatly affects the usefulness of an agentic system, so we’re extremely interested in making it as easy as possible to leverage memory for applications

To this end, we’ve built a lot of functionality for this into our products. This includes:

- [Low-level abstractions for a memory store](https://blog.langchain.com/launching-long-term-memory-support-in-langgraph/) in LangGraph to give you full control over your agent’s memory
- [Template](https://github.com/langchain-ai/memory-template?ref=blog.langchain.com) for running memory both “in the hot path” and “in the background” in LangGraph
- [Dynamic few shot example selection](https://docs.langchain.com/langsmith/manage-datasets) in LangSmith for rapid iteration

We’ve even built [a few applications of our own](https://github.com/langchain-ai/open-canvas?ref=blog.langchain.com) that leverage memory! It’s still early though, so we’ll keep on learning about agent memory and the areas it can be used effectively 🙂

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd19c522dc1bc339c55041_image--9--1.webp)Harrison&#x27;s In the Loop

#### Your harness, your memory

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseApril 11, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/your-harness-your-memory)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b40927fd1d366828376_HFEylQUaIAAA88g.webp)Harrison&#x27;s In the Loop

#### Continual learning for AI agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseApril 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/continual-learning-for-ai-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)