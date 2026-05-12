---
title: "Build reliable agents in JavaScript with LangGraph.js v0.2: Now supporting Cloud and Studio"
author: "LangChain Accounts"
date: "2024-09-03"
url: "https://www.langchain.com/blog/javascript-langgraph-v02-cloud-studio"
---

LangGraph

# Build reliable agents in JavaScript with LangGraph.js v0.2: Now supporting Cloud and Studio

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 3, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf65d2a13d9d60509158_LANGGRAPH-JS.png)Today, we’re launching [LangGraph.js v0.2.0](https://github.com/langchain-ai/langgraphjs?ref=blog.langchain.com), our JavaScript/TypeScript framework for building LLM-powered agents. Here’s what’s new:

- [**Flexible streaming**](https://langchain-ai.github.io/langgraphjs/how-tos/stream-values/?ref=blog.langchain.com) of intermediate steps and chat model messages with different streaming modes
- [**A built-in checkpointing system**](https://langchain-ai.github.io/langgraphjs/how-tos/persistence/?ref=blog.langchain.com) that lets you to rewind to past states and debug errors like faulty model responses
- [**First-class human-in-the-loop support**](https://langchain-ai.github.io/langgraphjs/how-tos/breakpoints/?ref=blog.langchain.com) that allows you to interrupt, update internal state, and resume at any given point in the graph
- [**Parallel node support**](https://langchain-ai.github.io/langgraphjs/how-tos/map-reduce/?ref=blog.langchain.com) to run and combine results from multiple nodes simultaneously

We’re also introducing beta support for LangGraph.js projects in [LangGraph Studio](https://blog.langchain.com/langgraph-studio-the-first-agent-ide/), our agent IDE for desktop, and [LangGraph Cloud](https://blog.langchain.com/langgraph-cloud/), our scalable infrastructure for deploying agents..

LangGraph.js is already empowering top AI teams to tackle critical problems. James Spiteri, Director of Generative AI &amp; ML for Security Analytics at Elastic highlights that:

> *LangGraph.js and the entire LangChain ecosystem have been key pieces in our architecture in Elastic’s AI Assistant for Security, Attack Discovery and Automatic Import, helping us iterate and push *[*these features*](https://www.elastic.co/security/ai?ref=blog.langchain.com)* to production in record time. We’ve been impressed by the continual improvements and collaboration from the LangChain team, and are excited to continue building with LangChain.*

For the JavaScript community, these new features unlock an even more powerful loop for building, debugging, and deploying reliable agents.

There’s a lot to cover, so let’s dive in!

## **Build controllable agents with LangGraph 0.2 in JavaScript**

Unlike traditional APIs, LLMs pose unique challenges to developers due to their long-running, non-deterministic nature. These challenges compound as the number of LLM calls in your logic increases, especially as you introduce agentic steps that give models autonomy over your code execution.

LangGraph.js provides JavaScript developers with a powerful toolkit for addressing these complexities and creating delightful experiences around agents. LangGraph.js can improve your application’s:

- **Responsiveness:** By [streaming results token-by-token](https://langchain-ai.github.io/langgraphjs/how-tos/stream-tokens/?ref=blog.langchain.com), you can deliver real-time, interactive experiences and report progress immediately. Having various modes of streaming is crucial for web apps that demand instant feedback and smooth user experience.
- **Resilience:** Using node-level retry policies and checkpointing, ensure your app stays robust. If a service goes down or a step fails, your app can recover seamlessly and resume execution from previous states.
- **Access control: **Restrict sensitive tools to [require human approval](https://langchain-ai.github.io/langgraphjs/how-tos/review-tool-calls/?ref=blog.langchain.com). This lets you protect your application and reduce the risk of unintended consequences.

LangGraph.js also runs in most JS runtimes, including Node, Deno, Cloudflare Workers, Vercel’s Edge runtime and [even in the browser](https://langchain-ai.github.io/langgraphjs/how-tos/use-in-web-environments/?ref=blog.langchain.com) through the `@langchain/langgraph/web` entry point.

Check out our revamped [documentation](https://langchain-ai.github.io/langgraphjs/?ref=blog.langchain.com) for new how-to guides, tutorials, and conceptual guides that help you get started. For an overview of the latest changes and updates to the documentation, you can also view a summary [here](https://langchain-ai.github.io/langgraphjs/versions/?ref=blog.langchain.com).

## **Iterate and debug faster with LangGraph Studio**

[LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?ref=blog.langchain.com) provides a best-in-class experience for debugging agents. In dynamic TypeScript / JavaScript environments involving async operations, it’s often tough to understand the flow of data– with LLM-powered agents adding further branching logic complexity.

LangGraph Studio automatically detects your graph’s inputs and outputs using TypeScript&#x27;s type inference, giving you a clear visual overview of your logic. This eliminates the need to manually trace different data flows and simplifies debugging.

When testing, you can travel back to individual states and rerun them. This lets you identify and fix issues without restarting the entire application. You can also set interrupts to step through your logic and inspect how your code is executing step-by-step. LangGraph Studio even supports hot reload to apply changes in real-time and speed up development!

We’re excited to announce that LangGraph Studio now supports LangGraph.js. LangGraph Studio is currently in beta, and is free to all LangSmith users during the beta period. **You can download the latest release **[**here**](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file&amp;ref=blog.langchain.com#download)** and check out **[**this repo**](https://github.com/langchain-ai/langgraphjs-studio-starter?ref=blog.langchain.com)** for a JavaScript starter template. **

And if you have an existing graph, you’ll need to [update to the latest versions](https://langchain-ai.github.io/langgraphjs/how-tos/manage-ecosystem-dependencies/?ref=blog.langchain.com) of LangGraph.js and LangChain core, then export your graph from a file and add a langgraph.json file with the path and some metadata.

## **Deploy at scale with LangGraph Cloud**

Once you&#x27;ve perfected your LangGraph.js graphs locally, you can deploy them in one-click on [LangGraph Cloud](https://langchain-ai.github.io/langgraph/cloud/?ref=blog.langchain.dev). Designed for web-scale, LangGraph Cloud helps you manage and provision task queues and servers so that your agents can handle many concurrent users and high traffic.

For diagnosing issues in production, LangGraph Cloud integrates with LangSmith for detailed tracing and uses a built-in Postgres checkpointer. This out-of-the-box checkpointer stores states and threads so that you can rewind and rerun previous states, allowing you to troubleshoot and replicate issues as if you were developing locally.

In addition, LangGraph Cloud supports advanced real-world interaction patterns beyond streaming and human-in-the-loop. These include features like double-texting to handle new user inputs on active threads of the graph, async background jobs to manage long-running tasks, and cron jobs to automate scheduled processes.

**LangGraph Cloud is now available in beta for all LangSmith users on Plus or Enterprise plans. Try it out today for free **[**by signing up for LangSmith**](https://smith.langchain.com/?ref=blog.langchain.dev)**.**

## **What’s next?**

This is just the beginning - we’re committed to making LangGraph.js the most delightful way to build agents in JavaScript in the long run.

We’re closely listening to the community and their feedback, many of whom are already running LangGraph.js in production – and we invite you to share your thoughts.  [Connect with us on X](https://x.com/LangChainAI?ref=blog.langchain.com), or join our [community Slack workspace](https://join.slack.com/t/langchaincommunity/shared_invite/zt-2of5edn9u-kVYpEDdEkbg7JDQxpg0HsQ?ref=blog.langchain.com).

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