---
title: "On Agent Frameworks and Agent Observability"
author: "LangChain Accounts"
date: "2026-02-13"
url: "https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability"
---

Harrison&#x27;s In the LoopAgent Architecture

# On Agent Frameworks and Agent Observability

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseFebruary 12, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9ec0d1eacf7a3a646f1_On-Agent-Frameworks--1-.png)Every time LLMs get better, the same question comes back: &quot;Do you still need an agent framework?&quot; It&#x27;s a fair question. The best way to build agents changes as the models get more performant and evolve, but fundamentally, the agent is a system *around* the model, so they will not disappear – they just need to evolve too.We&#x27;ve now built three generations of agent frameworks, and each one looked different from the last. So here&#x27;s what we believe:

- Agent frameworks are still useful, but only if they evolve as fast as the models do.
- Agent observability should work no matter how you build. That’s why LangSmith works even if you don’t use our open source (LangChain or LangGraph).

This post is about both of those bets.

**Why agent frameworks are still relevant in 2026**

Agent patterns have moved from chaining to workflow orchestration to tool-calling-in-a-loop with file-systems and memory. We’ve built frameworks for them all and believe each has its place based on your use case. Here’s how they’ve evolved:

### Chaining

The original **langchain** got popular in 2023 because few people knew how to make practical use of LLMs. The framework offered one of the easiest ways to connect foundation models to your data or APIs through a set of integrations and core abstractions. It was arguably too opinionated at the start — more of an &quot;easy button&quot; for learning about prompting and RAG than a production-ready tool. As the first wave of generative AI started to settle by that summer, criticism that agent frameworks were pointless grew louder.

We heard the criticism, but it was hard to square with what we were seeing in actual usage. The vast majority of teams building LLM apps needed ways to move faster than going it completely alone. Good frameworks:

- Encode best practices into the framework itself
- Reduce boilerplate code
- Make it easier to reach a higher level of quality
- Create standards and readability across large teams
- Pave a cleaner path to production

So we doubled down. On a different framework.

### Orchestration and run-time

**langgraph** was lower level and more flexible. It included a runtime that supported durability and statefulness, which turned out to be important for human-agent and agent-agent collaboration. It addressed many of the control concerns people had raised about **langchain**. We did eventually rewrite the original **langchain** in 2025 to be more streamlined, but we also recognized that different problems need different tools.

### Harness

More recently, we built **deepagents**: a batteries-included agent harness that&#x27;s more performant and more flexible. It supports planning for long-horizon tasks, tool-calling-in-a-loop, context offloading to a filesystem, and subagent orchestration. An agent harness works now because LLMs are getting better at reasoning and you can delegate more decisions to the LLM vs. hard coding as many orchestration patterns. It&#x27;s most similar in concept to Claude Agent SDK, but model-agnostic. To our knowledge, it&#x27;s the only agent harness that is not tied to any specific LLM or application stack.

Today, we recommend these different frameworks for different use cases. **langchain and deepagents **are built on top of **langgraph’s** runtime for long running execution.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9ec0d1eacf7a3a646f7_data-src-image-d6a87a95-4aa7-4edd-bf29-fbed61103e87.png)

It sounds dramatic, but we’ve seen three generations of agents in three years: what started as RAG became agentic workflows, which evolved into more autonomous tool-calling-in-a-loop agents.

The biggest knock against frameworks is that the AI space evolves too quickly for standards to form. There&#x27;s truth to that. But we also believe that sitting out of the AI game waiting for things to settle is a losing strategy. Frameworks help you dive in, build faster, and increase your odds of success. Even knowing that, the tools will keep changing. And you also don’t need a framework for everything. If it’s a simple LLM request, adding a framework may be too heavy handed.

## **Why LangSmith is independent from LangChain open source**

Early on, we recognized that [quality](https://www.langchain.com/state-of-agent-engineering?ref=blog.langchain.com#biggest-barriers-to-production) was the biggest barrier to getting agents into production. We believed, and still do, that purpose-built [agent observability](https://www.langchain.com/articles/agent-observability) and evals were a required part of the toolkit.

We called it[ LangSmith](https://www.langchain.com/langsmith/observability?ref=blog.langchain.com), because we had the intuition that there wouldn&#x27;t be only one agent framework. And even if there were a dominant one, it would have to evolve at a pace that would make early versions unrecognizable. We acknowledged not everyone would use our frameworks, but wanted them still to be able to use this platform.

So we built LangSmith to work regardless of whether you used **langchain**, any of our other frameworks, or nothing at all. This wasn&#x27;t an obvious decision at the time. We drew inspiration from companies like Vercel, which supports many frontend frameworks beyond their own[ Next.js](http://next.js/?ref=blog.langchain.com).

Today, LangSmith integrates with[ a number of frameworks out of the box](https://docs.langchain.com/langsmith/integrations?ref=blog.langchain.com) — AutoGen, Claude Agent SDK, CrewAI, Mastra, OpenAI Agents, PydanticAI, Vercel AI SDK, and more. It supports OpenTelemetry-based tracing, so anything that emits the OTEL spec can be ingested by LangSmith. And it works with agents built using no framework at all. Many LangSmith customers, including Clay, Harvey, and Vanta, don&#x27;t use our open source frameworks but rely on LangSmith for observability and evals.

## **Building and testing converge in agent engineering**

Regardless of your agent framework, traces are critical to understanding agent behavior. We&#x27;ve been writing about [how important the agent trace](https://blog.langchain.com/in-software-the-code-documents-the-app-in-ai-the-traces-do/) is because it&#x27;s the foundation for agent debugging, monitoring, evals, and more. With agents, your app logic is documented in traces, not code. Building the agent is only the first step. Agents are non-deterministic systems, so you have no idea what inputs or outputs to expect until you ship it. That’s why debugging, testing, and monitoring are critical parts of[ agent engineering](https://blog.langchain.com/agent-engineering-a-new-discipline/) and the building process itself.

So if you’re not using our OSS frameworks, we’d like to hear why! But, don’t let it stop you from figuring out how and why your agent is failing with LangSmith.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)