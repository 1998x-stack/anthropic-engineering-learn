---
title: "LangGraph 0.3 Release: Prebuilt Agents"
author: "LangChain Accounts"
date: "2025-02-27"
url: "https://www.langchain.com/blog/langgraph-0-3-release-prebuilt-agents"
---

Observability &amp; EvalsOpen SourceTutorials &amp; How-Tos

# LangGraph 0.3 Release: Prebuilt Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 27, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbade43d7d286a58fa49d0_Youtube-and-Blog-Self-Serve-Components--1-.png)By Nuno Campos and Vadym Barda

Over the past year, we’ve invested heavily in making [LangGraph](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com) the go-to framework for building AI agents. With companies like [Replit](https://blog.langchain.com/customers-replit/), [Klarna](https://blog.langchain.com/customers-klarna/), [LinkedIn](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics?ref=blog.langchain.dev) and [Uber](https://dpe.org/sessions/ty-smith-adam-huda/this-year-in-ubers-ai-driven-developer-productivity-revolution/?ref=blog.langchain.dev) choosing to build on top of LangGraph, we have more conviction than ever that we are on the right path.

A core principle of LangGraph is to be as low level as possible. There are no hidden prompts or no enforced “[cognitive architectures](https://blog.langchain.com/what-is-a-cognitive-architecture/)” in LangGraph. This has served to make it production ready and also distinguishes itself from all other frameworks.

At the same time, we **do** see the value in higher level abstractions. They make it easy to get started, easy to try out new cognitive architectures, and provide a nice entrypoint to the field.

Up to this point, we’ve had one higher level abstraction and it’s lived in the main `langgraph` package. It was [`create_react_agent`](https://langchain-ai.github.io/langgraph/how-tos/?ref=blog.langchain.com#prebuilt-react-agent), a wrapper for creating a simple tool calling agent. Today, we are splitting that out of `langgraph` as part of a 0.3 release, and moving it into `langgraph-prebuilt`.

We are also introducing a new set of [prebuilt agents](https://langchain-ai.github.io/langgraph/prebuilt/?ref=blog.langchain.com) built on top of LangGraph, in both Python and JavaScript.

Over the past three weeks, we’ve already released a few of these:

- [Trustcall](https://github.com/hinthornw/trustcall?ref=blog.langchain.com): for doing reliable structured extraction
- [LangGraph Supervisor](https://github.com/langchain-ai/langgraph-supervisor-py?ref=blog.langchain.com): for getting started with a supervisor multi-agent architecture
- [LangMem](https://github.com/langchain-ai/langmem?ref=blog.langchain.com): for long term memory
- [LangGraph Swarm](https://github.com/langchain-ai/langgraph-swarm-py?ref=blog.langchain.com): for getting started with a swarm multi-agent architecture

We believe that these prebuilt libraries can combine the best of both worlds:

- They make it easy to get started with common agent patterns
- They are built on top of LangGraph, so if you want to modify them it’s easy and familiar

We hope that this will foster a large collection of prebuilt agents built by the community. To that end, we have added [instructions](https://langchain-ai.github.io/langgraph/prebuilt/?ref=blog.langchain.com#contributing-your-library) for creating your own prebuilt package and adding it to our registry of agents. We have seen this work well with LangChain integrations. We have over 700 integrations, a large number maintained by the community in third party packages. We hope the same will happen with LangGraph prebuilt agents.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)Agent ArchitectureDeep AgentsOpen Source

#### Running Subagents in the Background

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)Hunter LovellColin FrancisApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/running-subagents-in-the-background)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)