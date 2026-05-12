---
title: "Discussing agents' tracing, observability, and debugging with Ismail Pelaseyed, the founder of Superagent"
author: "Tereza Tizkova"
date: "2023-08-22"
url: "https://e2b.dev/blog/discussing-agents-challenges-with-ismail-pelaseyed-the-founder-of-superagent"
category: "case-studies"
site: "e2b"
---

We talked with [Ismail Pelaseyed](https://twitter.com/pelaseyed) about AI agents, their current challenges, and potential solutions.

Ismail is the founder of [Superagent](https://www.superagent.sh/) - **a framework for web or no-code developers**. Being active for around two months, Superagent already gained **around 2000 users and over 1500 agents running in the production every da**y. It is a completely [open-source](https://github.com/homanp/superagent) platform, with a cloud version free to use.

## Users and Use Cases

Superagent tries to approach **no-code developers** to **integrate agents into their applications**.

They have two main types of agents built with Superagent:

1.** Chatbots** - **Retrieval types of agents**, used to Q&A over structured or unstructured documents.

2. **Action-based assistant** - Run either through a **chat interface **or just through an API.

‍

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67995347ff9dc23d3b02db12_67995338ba8a39e39ec2002d_Screenshot%25202025-01-28%2520at%252013.58.51.png)

‍

## Architecture and Techstack

[Superagent](https://www.superagent.sh/) has a **database layer on top of the agents' infrastructure**. When a user creates an agent, they create an entry into that database with a configuration of how an agent should run. They have an **API service hosted on **[**render.com**](http://render.com/) which picks the configuration depending on the API call, creates the agent on the fly, and runs it.

They are currently using [Langchain](https://github.com/e2b-dev/awesome-sdks-for-ai-agents/tree/main#langchain), which has a very **prompt-based agent infrastructure**, to call various LLMs and [LlamaIndex](https://github.com/e2b-dev/awesome-sdks-for-ai-agents/tree/main#llamaindex) to ingest various data.

They are deep into replacing currently used frameworks, moving away from the core Langchain Agent-LLM loop (e.g. [ReAct](https://arxiv.org/abs/2210.03629), [Chain of Thought](https://www.promptingguide.ai/techniques/cot)).

The [Superagent](https://www.superagent.sh/) team has a **wrapper around some individual types of agents **which they have tested and are **ready to be run in production**. These agents can then be easily configured without the need to consider various components that are involved in running agents, mainly:

- **Memory**
- **Vectorizations**
- **The agent's acting and whole logic.**

## Current Challenges

The **agent architecture** **is still in its early stages**, making configuration for specific use cases challenging. 

*“Many people attempt to create agents but often give up due to its inability to meet their desired functionality, "* says Ismail. *“Our goal is to develop agents that are not only demo-worthy but also practical and useful for business purposes.”*

Ismail has been noticing the **many and many specific ways** in which people want to use their agents **for the same use case**. *“People really do have specific ways of working on the same thing, which therefore requires deep developers’ understanding.”*

Creating efficient agents that work effectively in production for **specific use cases** demands significant expertise at this stage. Especially with high pressure being placed on ensuring user-friendliness for no-code users.

With that come the challenges of **debugging, tracing, monitoring, and observability** of the agents.

## Debugging the Agents

The current process of solving a bug is very simple. If an agent instance fails, end users go to the [Superagent Discord](https://discord.com/invite/mhmJUTjW4b). There they describe the bug, for example, that a retrieval agent did not use a document to make a query, but hallucinated instead.

*“It is not the actual software that is failing, it is ****mostly the setup that the user has****. It can be prompt, it can be the document being ingested, or anything else. That is what we are trying to debug.”*

Ismail emphasizes looking for a powerful debugging solution that would be **user-centric**. It is not the developer team, but the end users who are not currently able to debug the agent themselves.

## Tracing and Observability

**The tracing currently lacks WHY and HOW**. That is, the user sees that an agent instance failed, but doesn't understand WHY exactly it happened and HOW to fix the problem. This problem can be solved on an individual level but will grow big when Superagent gains even more regular users and bigger customers.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67979ce86c45c550e3bbbb2a_67979c9eb8db373ed9c3341b_WVxAw1bhz6zHDYRz0Dm0r23lOo.webp)Monitoring agents' logs.* *Source: [*Superagent*](https://www.superagent.sh/)* dashboard*

## Agents's tools and SDKs

To overcome the challenges of tracing and debugging, the Superagent team can envision themselves using an **equivalent of **[**Sentry**](https://sentry.io/welcome/) (a software error tracking and monitoring platform), which could provide **insights into the origin of a bug.** They have tried [**Langsmith**](https://github.com/e2b-dev/awesome-sdks-for-ai-agents/tree/main#langsmith)** **(a web-based GUI to test and monitor calls from LLM apps), which, however, won't give the root cause of the bug and possible solutions.

*“We need a tool that would**** also tell a user what they should do with the bug****,” *says Ismail.

The [Superagent](https://www.superagent.sh/) team has a UI where end users can see agents’ runs. It is very similar to Langsmith or any other type of logging framework.

When a user faces a problem, the [Superagent](https://www.superagent.sh/) team can log into the system, see what the agent tries to do in each step, and then **visualize the log**. This is in **principle similar to regular server logs visualizations**. 

## Conclusion

Right now the [Superagent](https://www.superagent.sh/) team focuses on **re-doing their whole infrastructure**, aiming to **run the agents in a separate queue**, and creating a queue system, instead of running them on the fly.

*“We would go for big ****changes in our infrastructure**** if it solves the discussed problems,”* says Ismail.

Without a doubt, in the very young agents space ([AutoGPT](https://news.agpt.co/), the first well-known agent, launched only in March 2023), [Superagent](https://www.superagent.sh/) and other agents are steadily gaining traction among end users. Despite the current drawbacks, this shows the **real demand for agents**.

If you want to try [Superagent](https://www.superagent.sh/) yourself, check the [web](https://www.superagent.sh/), [GitHub](https://github.com/homanp/superagent), or join the [Discord community](https://www.superagent.sh/).