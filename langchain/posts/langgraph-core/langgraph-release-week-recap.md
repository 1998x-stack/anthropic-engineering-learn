---
title: "LangGraph Release Week Recap"
author: "LangChain Accounts"
date: "2025-06-09"
url: "https://www.langchain.com/blog/langgraph-release-week-recap"
---

LangGraphCompany Announcements

# LangGraph Release Week Recap

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 9, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaabcbf847dfe35ef4f90_Theme-Digital-Nebula--Format-Blog--Colour-Blue--Text-Alignment-Centred--With-Image-Text-Only--1-.png)Over the past few weeks, we rolled out new features for both LangGraph.js and LangGraph Python, improving both low level workflows and prebuilt agents.

These new features make it easier to build workflows with faster development cycles, more efficient runs, and greater control at every level of your graph.

Here’s a quick recap of what’s new:

### **1. Node Caching ♻️**

We kicked off the week by introducing **node/task level caching**. Now you can cache the results of individual nodes in your LangGraph workflow, reducing redundant computation and speeding up execution. Node caching is particularly helpful for speeding up development cycles.

🔗 [Python docs](https://langchain-ai.github.io/langgraph/concepts/low_level/?h=node+cach&amp;ref=blog.langchain.com#node-caching) | [JS docs](https://langchain-ai.github.io/langgraphjs/how-tos/node-caching/?ref=blog.langchain.com)

### **2. Deferred Nodes 🕰️**

Next, we added support for **deferred nodes** — nodes whose execution is postponed until all upstream paths complete. Deferred nodes are ideal for map-reduce, consensus, and agent collaboration workflows.

🔗 [Python docs](https://langchain-ai.github.io/langgraph/how-tos/graph-api/?h=defer&amp;ref=blog.langchain.com#defer-node-execution) | [JS docs](https://langchain-ai.github.io/langgraphjs/how-tos/defer-node-execution/?ref=blog.langchain.com)

### 3. Pre/Post Model Hook 🪝

Our prebuilt ReAct agents now support more customizable message flow with pre/post model hooks. Pre model hooks ag great for summarizing message history (controlling context bloat) and post model hooks are ideal for guardrails and human-in-the-loop interactions.

As a nice bonus, check out these [interactive docs](https://langchain-ai.github.io/langgraph/agents/overview/?ref=blog.langchain.com#visualize-an-agent-graph) that help you visualize react agent workflows.

🔗  [Python docs](https://langchain-ai.github.io/langgraph/reference/agents/?h=post_model_hook&amp;ref=blog.langchain.com#langgraph.prebuilt.chat_agent_executor.create_react_agent) | [JS docs](https://langchain-ai.github.io/langgraphjs/reference/types/langgraph_prebuilt.CreateReactAgentParams.html?ref=blog.langchain.com#__type.postModelHook)

### 4. Builtin Provider Tools 🔍

You can now use builtin provider tools like [web search](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat&amp;ref=blog.langchain.com) and [Remote MCP](https://platform.openai.com/docs/guides/tools-remote-mcp?ref=blog.langchain.com) tools with the prebuilt ReAct agent. Simply pass in the tool specification dict to the list of `tools`, and you’re golden!

## JS Enhancements

In addition to the above features introduced in both Python and JS, we’ve also added a few improvements specifically on the JS side.

### 1. Resumable Streams ⏩

Make your app resilient to page reloads or network hiccups with `reconnectOnMount`. Streams resume automatically — no lost tokens, no extra code.

🔗 [JS docs](https://langchain-ai.github.io/langgraph/cloud/how-tos/use_stream_react/?ref=blog.langchain.com#resume-a-stream-after-page-refresh)

### 2. DevX Improvements 🧘

Finally, we&#x27;ve made a bunch of changes to improve the day-to-day developer experience with LangGraph JS v0.3:

- `.stream()` method is now fully type-safe, returning the state updates and values depending on your streamMode. No more any and unsafe casts littered throughout the code. The same is coming in Python soon!
- `.addNode({node1, node2, ...})` and `.addSequence({node1, node2, ...})` is now available for StateGraph, reducing the boilerplate of constructing a simple workflow.
- Interrupts are now returned in `.invoke()` and `&quot;values&quot;` stream modes, allowing you to handle the interrupt directly without the need to call `getState()` afterwards.

Follow [@LangChainAI](https://x.com/langchainai?ref=blog.langchain.com), [@SydneyRunkle](https://x.com/sydneyrunkle?ref=blog.langchain.com) (Python), and [@__dqbd](https://x.com/__dqbd?ref=blog.langchain.com) (JS) to stay up to date on what’s next. 👀

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)