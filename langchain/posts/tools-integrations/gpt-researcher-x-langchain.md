---
title: "GPT Researcher x LangChain"
author: "LangChain Accounts"
date: "2023-08-13"
url: "https://www.langchain.com/blog/gpt-researcher-x-langchain"
---

Tutorials &amp; How-TosPartner

# GPT Researcher x LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 13, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1c6adb40d0919235bdb_photo-1587397070638-81d3cce10435.jpeg)Here at LangChain we think that web research is fantastic use case for LLMs. So much so that we wrote a [blog on it](https://blog.langchain.com/automating-web-research/) about a month ago. In that blog we mentioned the leading open-source implementation of a research assistant - [gpt-researcher](https://github.com/assafelovic/gpt-researcher?ref=blog.langchain.com). Today we&#x27;re excited to announce that GPT Researcher is integrated with LangChain. Specifically, it is integrated with our OpenAI adapter, which allows (1) easy usage of other LLM models under the hood, (2) easy logging with LangSmith.

What is GPT Researcher? From the GitHub repo:

> The main idea is to run &quot;planner&quot; and &quot;execution&quot; agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the planner filters and aggregates all related information and creates a research report. The agents leverage both gpt3.5-turbo-16k and gpt-4 to complete a research task.
More specifcally:
- Generate a set of research questions that together form an objective opinion on any given task.
- For each research question, trigger a crawler agent that scrapes online resources for information relevant to the given task.
- For each scraped resources, summarize based on relevant information and keep track of its sources.
- Finally, filter and aggregate all summarized sources and generate a final research report.

An image of the architecture can be seen below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1c6adb40d0919235be1_gpt-researcher-1.png)

Under the hood this uses OpenAI&#x27;s `ChatCompletion` endpoint. As number of viable models has started to increase (Anthropic, Llama2, Vertex models) we&#x27;ve been chatting with the GPT Researcher team about integrating LangChain. This would allow them to take advantage of the [~10 different Chat Model integrations](https://python.langchain.com/docs/integrations/chat/?ref=blog.langchain.com) that we have. It would also allow users to take advantage of [LangSmith](https://blog.langchain.com/announcing-langsmith/) - our recently announced debugging/logging/monitoring platform.

In order to make this transition as seamless as possible we added an OpenAI adapter that can serve as a drop-in replacement for OpenAI. For a full walkthrough of this adapter, see the documentation [here](https://python.langchain.com/docs/guides/adapters/openai?ref=blog.langchain.com). This adapter can be use by the following code swap:

`- import openai
+ from langchain.adapters import openai`

See [here](https://github.com/assafelovic/gpt-researcher/pull/124?ref=blog.langchain.com) for the full PR enabling it on the GPT Researcher repo.

The first benefit this provides is enabling easy usage of other models. By passing in `provider=&quot;ChatAnthropic&quot;, model=&quot;claude-2&quot;,` to create, you easily use Anthropic&#x27;s Claude model.

The second benefit this provides is seamless integration with LangSmith. Under the hood, GPT Researcher makes many separate LLM calls. This complexity is a big part of why it&#x27;s able to perform so well. As the same time, this complexity can also make it more difficult to debug and understand what is going on. By enabling LangSmith, you can easily track that.

For example, here is the [LangSmith trace](https://smith.langchain.com/public/84fb4bdc-f228-4192-a265-06f169b7d657/r?ref=blog.langchain.com) for the call to the language model when it&#x27;s generating an agent description to use:

And here is the [LangSmith trace](https://smith.langchain.com/public/37aa9e0a-ed65-4f9e-97eb-866b1bfa61f3/r?ref=blog.langchain.com) for the final call to the language model - when it asks it to write the final report:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1c6adb40d0919235be5_Screenshot-2023-08-13-at-1.40.32-PM.png)

We&#x27;re incredibly excited to be supporting GPT Researcher. We think this is one of the biggest opportunities for LLMs. We also think GPT Researcher strikes an appropriate balance, where the architecture is certainly very complex but it&#x27;s more focused than a completely autonomous agent. We think applications that manage to strike that balance are the future, and we&#x27;re very excited to be able to partner with and support them in any way.

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