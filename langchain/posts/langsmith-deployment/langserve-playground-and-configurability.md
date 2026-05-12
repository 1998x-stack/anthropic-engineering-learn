---
title: "LangServe Playground and Configurability"
author: "LangChain Accounts"
date: "2023-10-19"
url: "https://www.langchain.com/blog/langserve-playground-and-configurability"
---

Company AnnouncementsAgent Architecture

# LangServe Playground and Configurability

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaOctober 19, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1102f433e4fdba55e8f_Screenshot-2023-10-19-at-18.07.14-1.png)Last week we launched [LangServe](https://blog.langchain.com/introducing-langserve/), a way to easily deploy chains and agents in a production-ready manner. Specifically, it takes a chain and easily spins up a FastAPI server with streaming and batch endpoints, as well as providing a way to stream intermediate steps.

This week, we&#x27;re making some additions – a playground and configurability. Both are centered around the same ideas: common architectures, experimentation, and collaboration.

## Playground

Now when you use LangServe to deploy your chain you get for free a playground experience. In this playground you can change the values of certain, configurable parameters (more on that later) as well as try out different inputs and get the response streamed back in real time.

The screenshot below is from a playground for [WebLangChain](https://blog.langchain.com/weblangchain/), which you can access [here](https://weblangchain.fly.dev/chat/playground/?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1102f433e4fdba55e8f_Screenshot-2023-10-19-at-18.07.14-1.png)

Why is this useful?

First, this immediately provides a (simple) UI for your chains and agents. Although simple, this UI does have necessary things like:

- Streaming outputs
- Full log of intermediate steps
- Configurable options

This will make it possible to share a link with colleagues and let them interact with in the UI, facilitating collaboration among a larger team. Specifically, we imagine this being a way for engineers to easily expose a way for non-technical folks to interact with their chains/agents (without having to connect it to the frontend).

Second, this provides a way to experiment with different parameters. In the WebLangChain examples, we&#x27;ve exposed multiple different models (Anthropic and OpenAI) as well as multiple different retrievers:

- [Tavily](https://python.langchain.com/docs/integrations/retrievers/tavily?ref=blog.langchain.com)
- [You.com](https://blog.langchain.com/you-com-x-langchain/)
- Google
- [Kay SEC Retriever](https://python.langchain.com/docs/integrations/retrievers/sec_filings?ref=blog.langchain.com)
- [Kay Press Release Retriever](https://github.com/langchain-ai/langchain/blob/master/cookbook/press_releases.ipynb?ref=blog.langchain.com)

This makes it super easy for any one - technical or non-technical - to experiment to different components.

## Configurability

One new feature which makes this experimentation possible is configuration of runnables. Specifically, we recently added syntax to allow for any components (or parts of components) to be configurable. This is doable whether you are using LangServe or not - it&#x27;s just part of LangChain Expression Language. See our cookbook for this [here](https://python.langchain.com/docs/expression_language/how_to/configure?ref=blog.langchain.com).

We&#x27;ve now exposed this configuration in a few places. First, as seen above, we&#x27;ve easily exposed this in the playground. However, this configuration can be used outside of the playground. We&#x27;ve also exposed it in our main WebLangChain app.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1102f433e4fdba55e96_Screenshot-2023-10-18-at-5.44.48-PM.png)

With configuration, you can save different versions of configurations via a URL. This can be used in a few ways. With WebLangChain, we expose this to the end user so that they can use that configuration in the UI. We imagine this more being used for internal apps, where you want to let internal users choose between different configuration options. We also expose this functionality in the playground, as seen below where you can copy a URL for a given configuration.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1102f433e4fdba55e99_Screenshot-2023-10-18-at-5.48.43-PM.png)

Note that for configuration options, the configuration is currently not persisted. We are currently alpha testing a deployment platform where the configuration is persisted - and can be persisted for multiple different users. If this is interesting to you, please reach out to sales@langchain.dev.

## Common Architectures

We see that there are common architectures for LLM applications fast emerging. These architectures are fairly generalizable, and can parametrized in a few different ways. This observation is motivating a lot of this work.

For example, let&#x27;s look at at our [WebLangChain](https://github.com/langchain-ai/weblangchain?ref=blog.langchain.com) app from last week. This is a cognitive architecture aimed at retrieval augmented generation, and the ways it can be configured are:

- LLM to use to answer
- Prompt to use to generate the search query for followups
- Prompt to use to generate the answer
- Retriever to use to look up queries

We see that the architecture of the app often takes a lot of engineering to get up and running. But after that, a lot of the configuration is best done in some sort of GUI. This enables easier collaboration.

This insight - and belief that this is a good path towards application development - is driving a lot of our work in this vein.

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