---
title: "Async Support in LangChain"
author: "LangChain Accounts"
date: "2023-02-08"
url: "https://www.langchain.com/blog/async-api"
---

Company AnnouncementsOpen Source

# Async Support in LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 8, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)1min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)We’re excited to roll out initial asynchronous support in LangChain by leveraging the [asyncio](https://docs.python.org/3/library/asyncio.html?ref=blog.langchain.com) library. Asyncio uses uses coroutines and an event loop to perform non-blocking I/O operations; these coroutines are able to “pause” (`await`) while waiting on their ultimate result and let other routines run in the meantime. To learn more about asyncio and how it compares to multithreading and multiprocessing, check out this [awesome tutorial](https://realpython.com/async-io-python/?ref=blog.langchain.com).

## Motivation

Since LangChain applications tend to be fairly I/O and network bound (calling LLM APIs and interacting with data stores), asyncio offers significant advantages by allowing you to run LLMs, chains, and agents concurrently: while one agent is waiting for an LLM call or tool to complete, another one can continue to make progress. Async support in LangChain also allows you to more seamlessly integrate your async chains and agents into frameworks that support asyncio, such as [`FastAPI`](https://fastapi.tiangolo.com/?ref=blog.langchain.com).

Check out the async agent [docs](https://python.langchain.com/docs/modules/agents/how_to/async_agent?ref=blog.langchain.com) in particular to see how significantly concurrent execution can speed things up!

## Usage

As a starting point, we’ve implemented async support for:

`LLM` via `agenerate` (see [docs](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/async_llm?ref=blog.langchain.com)):

- `OpenAI`

`Chain` via `arun` and `acall` (see [docs](https://python.langchain.com/docs/modules/chains/how_to/async_chain?ref=blog.langchain.com)):

- `LLMChain`
- `LLMMathChain`

`Agent` and `Tool` via `arun` (see [docs](https://python.langchain.com/docs/modules/agents/how_to/async_agent?ref=blog.langchain.com)):

- `SerpAPIWrapper`
- `LLMMathChain`

## Up Next

We’re just getting started with asyncio. In the near future, we hope to add:

- Async support for more LLMs, Chains, and Agent tools
- Ability to run multiple tools concurrently for a single action input
- Async support for callback handlers
- More seamless support with tracing

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)