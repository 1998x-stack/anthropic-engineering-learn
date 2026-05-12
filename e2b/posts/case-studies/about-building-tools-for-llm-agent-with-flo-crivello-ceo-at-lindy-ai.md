---
title: "Building tools for LLM agents with Flo Crivello - CEO at Lindy AI"
author: "Tereza Tizkova"
date: "2023-09-14"
url: "https://e2b.dev/blog/about-building-tools-for-llm-agent-with-flo-crivello-ceo-at-lindy-ai"
category: "case-studies"
site: "e2b"
---

[Lindy](https://www.lindy.ai/) is an AI assistant whose primary objective is to save users' time.  Lindy is described as “supremely reliable and attentive to detail.” We had an interview with its creator, [Flo Crivello](https://twitter.com/Altimor), about his methodology in developing Lindy AI and internal tooling for the agent.

## Overall approach towards building agents

Flo comments on how they are building Lindy.

“We think of our approach as two halves. An AI agent needs:

- The correct collection of tools
- To know how to utilize them."

They are building a framework focused on the second point in particular - integrations aren't the big risk here.

Right now, the Lindy AI team is especially focused on techniques here that will get the agent to self-improve / learn from its own experience how to use its tools better and better.“

## Main use cases and ideal users

Lindy AI is a personal assistant for making a user's life more efficient. It can assist with all daily tasks, from managing user's schedule and composing emails to sending contracts, and more.

“Our ideal user is a senior manager in the technology space,” says Flo.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67962e77def1bd0ef6bed78e_67962e22953e6ac687602d38_EcRZwGOCuhTuSNO35Hx5TFmlEqY.avif)Examples of use cases. **Source**:[ Lindy AI landing page](https://www.lindy.ai/)

## Reliability

Lindy has made great progress in reliability. When unsure about a task or when about to perform a high-stakes action, the agent asks the end user for confirmation.

"These confirmations become increasingly unnecessary as time goes by, both because we make Lindy smarter, and because she learns the user's preferences," explains Flo.

## Building agents tools

We asked Flo how they currently approach agent's debugging, monitoring, and tracing, what are the main struggles in this area, and how they are planning to solve them.

The Lindy AI team has developed all the agent tooling in-house.

"Our most important tool is probably the tracer, which shows step by step what the agent did exactly to fulfill a user query," says Flo. "It is similar to [Langsmith](https://smith.langchain.com/), but way better in our opinion."

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67962e77def1bd0ef6bed78b_67962e46093cf1f94c329c33_lZe576CyNkwoBh8iqYGegDvb8M.avif)**Source**: Lindy AI

**Lindy AI team also has tools for:**

- Seeing the "lessons" that the agent is learning over time (the Memory in the screenshot above) and editing them
- Reviewing the tools available, and editing the instructions about when and how to use each tool for the agent
- Editing global rules or action-level rules
- Monitoring benchmarks

## Other challenges

During the discussion, Flo mentioned additional problems that they are presently aiming to resolve, specifically fine-tuning and cognitive architecture.

"Right now, coming up with the right cognitive architecture is insanely challenging for us," says Flo, "but we wouldn’t outsource it, since we believe that’s our purpose. "

"Fine-tuning our model is also very painful, especially because we require a big model (40B+ parameters) and a big context window (8k+)," adds Flo. "I foresee that once we have that model, deploying it for inference at scale will be another significant challenge."