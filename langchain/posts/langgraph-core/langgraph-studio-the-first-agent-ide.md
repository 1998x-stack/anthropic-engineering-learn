---
title: "LangGraph Studio: The first agent IDE"
author: "LangChain Accounts"
date: "2024-08-01"
url: "https://www.langchain.com/blog/langgraph-studio-the-first-agent-ide"
---

Agent Architecture

# LangGraph Studio: The first agent IDE

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 1, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf7403935dbc92df45ea_Screenshot-2024-07-31-at-8.00.36-PM-1.png)LLMs have paved the way for the development of new types of *agentic* applications — and as LLM applications evolve, so must the tooling needed to efficiently develop them. Today, we&#x27;re announcing LangGraph Studio - the first IDE designed specifically for agent development - in open beta.

LangGraph Studio offers a new way to develop LLM applications, providing a specialized agent IDE for visualizing, interacting with, and debugging complex agentic applications. In this blog, we&#x27;ll give a brief overview of LangGraph and then explore how LangGraph Studio streamlines the development of agentic applications.

## LangGraph: Balancing agent control with agency

In [January 2023](https://blog.langchain.com/langgraph/), we launched LangGraph, a highly controllable, low-level orchestration framework for building agentic applications. Since then, we&#x27;ve seen  teams build more complex agentic applications for production; in turn, we&#x27;ve heavily invested in LangGraph, leading to [a stable 0.1 release](https://blog.langchain.com/langgraph-cloud/) this past June.

LangGraph features a persistence layer that enables human-in-the-loop interactions, and it excels at building complex (i.e. more than a single LLM call) applications that require highly domain-specific cognitive architecture. Most of the agents we see in production fit this description.

LangGraph is fully open source, available in both [Python](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) and [Javascript](https://github.com/langchain-ai/langgraphjs?ref=blog.langchain.com). It works with or without LangChain, and integrates seamlessly with LangSmith.

## LangGraph Studio: Visualize and interact with agent graphs for quick iteration

While LangGraph offers a new framework for developing agentic applications, we also strongly believe that new tooling is needed to make the development process easier. Building LLM applications differs from traditional software development, requiring different tooling outside of the traditional code editor.

Coding is still important to developing LLM applications — after all, production-ready LangGraph applications have complicated custom logic in the nodes and edges of the graphs that are created. We don&#x27;t aim to replace code editors but, instead, to **augment** the development experience with tools tailored for LangGraph applications.

LangGraph Studio facilitates this by making it easy to visualize and interact with agent graphs, even if development still primarily happens in code. Visualizing graphs helps developers understand their structure. Furthermore, you can modify an agent result (or the logic underlying a specific node) halfway through the agent&#x27;s trajectory. This creates an iterative process, by letting you interact with and manipulate the state at that point in time.

While there is much more to explore, we&#x27;re excited to introduce LangGraph Studio to start with bringing some of the core features of an agent IDE to the world.

## How to use LangGraph Studio

LangGraph Studio is a desktop app, currently available for Apple Silicon. You can download a version [here](https://github.com/langchain-ai/langgraph-studio?ref=blog.langchain.com). Support for more platforms is coming soon.

After you download and open LangGraph Studio, you will be prompted to log in with your LangSmith account. All users of LangSmith (including those with free accounts) currently have access to LangGraph Studio while it is in beta. You can sign up for a LangSmith account [here](https://smith.langchain.com/?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf7503935dbc92df45f1_login_screen.png)

After downloading LangSmith, you can open a directory. At a bare minimum, this directory needs to contain a Python file with a graph defined in it.

Next, you will need to create a `langgraph.json` file containing details such as where the agent is defined, which dependencies to install, and which environment variables to load. This file can be created in the UI, or can exist as a file in the directory already. For an example repository which meets these requirements, see [this GitHub repo](https://github.com/langchain-ai/langgraph-example?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf7503935dbc92df45fb_select_project_screen.png)

After you open a directory, we will build an environment for you agent to run. After it builds, you should see a visualization of the graph along with a box for interacting with the agent.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf7503935dbc92df45f6_graph_screen.png)

When you interact with the agent, you&#x27;ll get a stream of real-time information about what steps are happening. You can see the agent decide which tools to call, call those tools, and then continue looping.

You can interrupt the agent at any time if veers off course, or you can interrupt the agent to run it in a “debug mode” where it pauses after each step of the graph (so you can walk-through step by step).

0:00                            /0:191×

💡

At any point, you can interact with the **state** of the agent.

If you don’t like what the agent responded with at a specific step, you can directly modify the response and then continue with that new response. This can be useful for simulating what would have happened if the agent or a tool returned something different.

0:00                            /0:141×

You can also modify the underlying code and then replay the node. LangGraph Studio detects changes to the underlying code files, allowing you to update prompts in your code editor and rerun nodes if an agent responds poorly. This can make it much easier to iterate on long-running agents.

0:00                            /0:201×

## Conclusion

Building agentic applications differs from traditional software development. While code editors remain important, new IDEs designed for agents are also needed. LangGraph Studio is a step in this direction, and we&#x27;re excited to see how it enhances your workflow.

**For more on LangGraph Studio, check out our **[**documentation**](https://github.com/langchain-ai/langgraph-studio?ref=blog.langchain.com).** You can also watch a **[**video walkthrough on YouTube**](https://www.youtube.com/watch?v=pLPJoFvq4_M&amp;ref=blog.langchain.com)** if that&#x27;s more your style. You can **[**sign up for LangSmith**](https://smith.langchain.com/?ref=blog.langchain.com)** today to try out LangGraph Studio for free.**

**We&#x27;d also love your feedback - drop us a line at hello@langchain.dev or on **[**Twitter**](https://x.com/LangChainAI?ref=blog.langchain.com)** to share your thoughts.**

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)