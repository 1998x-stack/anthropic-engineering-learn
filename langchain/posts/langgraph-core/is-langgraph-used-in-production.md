---
title: "Is LangGraph Used In Production?"
author: "LangChain Accounts"
date: "2025-02-05"
url: "https://www.langchain.com/blog/is-langgraph-used-in-production"
---

Company AnnouncementsLangGraphAgent Architecture

# Is LangGraph Used In Production?

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 4, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadfe4cf06727c05bfa15_Screenshot-2025-02-04-at-4.35.59-PM.png)[Leading companies](https://www.langchain.com/built-with-langgraph?ref=blog.langchain.com) like Uber, LinkedIn, and Replit are choosing LangGraph to build agents that are not only powerful but also reliable. In 2024, the focus shifted towards specialized AI agents designed for specific business needs. But getting [AI agents](https://blog.langchain.com/what-is-an-agent/) production-ready isn’t as simple as plugging in an LLM to produce intelligent outputs. Companies need solutions that provide **reliability, observability, and control.**

This piece explores the key challenges of putting AI agents into production and how leading companies like Uber, LinkedIn, and Replit are overcoming them, with some help from LangGraph. 🪄

## **Many companies are choosing LangGraph for reliable agents**

Companies across a variety of industries are turning to LangGraph to build scalable agent systems. **LinkedIn** streamlined hiring by building an AI-powered recruiter that automates candidate sourcing, matching, and messaging. Their hierarchical agent system, built on LangGraph, has freed up their human recruiters to focus on high-level strategy – resulting in more efficient hiring.

Another example of operational efficiency —** AppFolio** created a copilot that’s [saved over 10 hours a week](https://blog.langchain.com/customers-appfolio/) for their property managers, as LangGraph helped them cut app latency and 2x the accuracy of their decisions.

For **Uber** and **Replit**, LangGraph greatly sped up the development cycle when scaling up complex workflows. Replit’s AI agent acts as a [copilot for building software from scratch](https://www.langchain.com/breakoutagents/replit?ref=blog.langchain.com); with LangGraph under the hood, they’ve architected a multi-agent system with human-in-the-loop capabilities (so users can **see their agent actions**, from package installations to file creation) - making development more transparent.

Uber integrated LangGraph to streamline large-scale code migrations within their developer platform. They carefully structured a network of specialized agents so that each step of their unit test generation was handled with precision. Similarly, **Elastic** has used LangGraph to orchestrate their network of AI agents for real-time threat detection – which has helped them respond to security risks much more quickly and effectively.

## **Why is it so hard to put AI agents into production?**

While LLM-powered agents hold immense promise, getting them production-ready is challenging - especially when it comes to ensuring [performance quality](https://www.langchain.com/stateofaiagents?ref=blog.langchain.com) and reliability.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadff4cf06727c05bfa87_AD_4nXd_SvIil7Jwr08T7ix3XKNGiD4mOMmNoAeHhGKybbHQWTIwPLB8ZyZajlRZi0RkrRFRbtj1Sbe-XrYIA-_YFrhbax1C7w8XFLAjntv4c8-N8-4Jlt4nYqIK3By3uBtgEP9lkZ6yEg.png)Performance quality was the top challenge for respondents in the &quot;State of AI Agents&quot; survey ran by LangChain in the tail end of 2024

From working closely with hundreds of companies, we see the following key hurdles to deploying agents in production:

- **Unpredictability of LLMs** - Unlike traditional software, AI agents don’t follow a fixed set of rules. Instead, they generate responses dynamically. On top of that, the UX for agents allows for free-form text input, including unpredictable human speech – making it difficult to guarantee accurate and contextually-appropriate responses.
- **Complexity of orchestration - **Many real-world applications require multiple agents to work together, with each handling different tasks. Coordinating them effectively — including managing task dependencies, error recovery, and communication – adds another layer of difficulty.
- **Observability and debugging limitations **- When an agent makes a bad decision, understanding *why* can feel like a shot in the dark. Diagnosing failures and maintaining performance require robust tracing and monitoring, which most agent frameworks don’t have built-in.

Given these hurdles, we see most companies choosing a framework to have the right tool set to meet their bar for shipping to production. This is also where LangGraph comes into play.

## **What is LangGraph?**

[LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.com) is a controllable agent framework designed for production use. Unlike other agentic frameworks, LangGraph is:

- **Low-level and customizable** – LangGraph allows you to flexibly design agents for your company’s bespoke needs. LangGraph primitives are fully descriptive and, unlike higher-level abstractions, can scale beyond prototyping.
- **Highly reliable** – Gain full control over agent actions with moderation checks, human-in-the-loop, and persisted context for long-running workflows — so your agent can stay on course.
- **Optimized for observability** – While LangGraph doesn’t depend on any other LangChain product, it integrates seamlessly with [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) for added visibility into agent interactions, performance monitoring, and debugging.

When we built LangGraph in early 2024, we intentionally gave developers the choice to structure their agents without the limitations of black-box architectures. LangGraph has since become the default framework for many agentic applications in production. We learned from LangChain that while higher level abstractions helped developers get started quickly, it’s the lower level flexibility that can handle varied production queries. LangGraph has a steeper learning curve, but users find they don&#x27;t scale off of it.

## **The future of AI agents with LangGraph**

As we enter 2025, LangGraph is poised to drive the next wave of AI agent adoption. By building on the lessons learned from these leading companies, we aim to empower more developers to build reliable, production-ready AI agents.

Looking for more insights? Check out the [latest stories](https://www.langchain.com/built-with-langgraph?ref=blog.langchain.com) on how companies are using LangGraph, or explore our latest [video tutorial ](https://www.youtube.com/watch?v=aHCDrAbH_go&amp;ref=blog.langchain.com)on how to build effective AI agents.

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