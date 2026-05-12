---
title: "How Middleware Lets You Customize Your Agent Harness"
author: "LangChain Accounts"
date: "2026-03-26"
url: "https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness"
---

Agent ArchitectureDeep Agents

# How Middleware Lets You Customize Your Agent Harness

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)Sydney RunkleMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b4ec0262e781f8493c_30.png)Agent harnesses are what help build an agent, they connect an LLM to its environment and let it do things.

When you’re building an agent, it’s likely you’ll want build an application specific agent harness. “Agent Middleware” empowers you to build on top of LangChain and Deep Agent’s solid foundation, but customize them for your use case.

## What are agent harnesses

An agent is a system built around a model. The model needs to be connected to an environment, data, memory, and tools. Agent harnesses are the system that helps you do that.

The core of every agent harness is the same, and remarkably simple: an LLM, running in a loop, calling tools. Simple as it is, there&#x27;s power in this core loop.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b5ec0262e781f84943_agent_loop.png)

LangChain contains `create_agent` - an abstraction with just this core loop.

## Why you would want to customize your agent harnesses

Different agent use cases have different needs. They may require different agent harnesses.

Some parts of the an agent harness - like instructions or tools - are pretty easy to customize. `create_agent` in LangChain lets you pass in a system prompt and tools for example.

Other parts are more involved. What if you want always run a certain step before the model executes? What if you always want to check the tool output for certain things?

Things that involve changing the core loop of the agent are trickier to change. When done correctly, it enables really powerful customization that still allows you to build on the core harness.

`AgentMiddleware` is our answer for this - how we let people customize LangChain agents.

## What is agent middleware?

💡

“Middleware” is a general term often used in other software engineering practices, but below we refer to a different system which we call agent middleware.

Middleware exposes a set of hooks that let you run custom logic before and after each step, so you can control what happens at every stage of the loop:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b5ec0262e781f84946_middleware.png)
- **`before_agent`**: Runs once on invocation. Good for loading memory, connecting to resources, or validating initial input.
- **`before_model`**: Fires before each model call. Use it to trim history or catch PII before it hits the LLM.
- **`wrap_model_call`**: Wraps the model call end-to-end. Caching, retries, and dynamic model requests like changing available tools all live here.
- **`wrap_tool_call`**: Wraps tool execution similarly. Inject context, intercept results, or gate which tools actually run.
- **`after_model`**: Runs after the model responds but before tools execute. The most natural place for human-in-the-loop.
- **`after_agent`**: Runs once on completion. Save results, send notifications, clean up.

Middleware are composable, so you can mix and match to your heart’s content.

LangChain ships a set of prebuilt middleware for the most common patterns, like summarization, retries, and PII redaction. Builders can also subclass the `AgentMiddleware` class to write your own for anything bespoke to your business.

## Examples of Middleware

Customization needs tend to cluster around the same themes. Below are the most common use cases:

**Business logic &amp; compliance.** Some things can&#x27;t live in a prompt, like PII redaction and content moderation. These are deterministic policies that have to fire every time. You can&#x27;t prompt your way to HIPAA compliance.

Deep dive: PII detection

LangChain’s builtin [PIIMiddleware](https://langchain-5e9cc07a-preview-srimpr-1771619406-31dcf4f.mintlify.app/oss/python/langchain/middleware/built-in?ref=blog.langchain.com#pii-detection) implements `before_model` and `after_model` hooks. It has the ability to mask/redact/hash PII on model inputs, outputs, and tool outputs. It can also raise a `PIIDetectionError` for the most critical PII detection situations.

**Dynamic agent control.** Middleware can reshape the agent at runtime: inject tools based on current state, swap the model mid-task, update the system prompt as context evolves. It&#x27;s active control over how the agent behaves at each step.

Deep dive: dynamic tool selection

LangChain’s [LLMToolSelectorMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in?ref=blog.langchain.com#llm-tool-selector) runs a fast LLM in the `wrap_model_call` hook to identify which tools from a registry are relevant for a given request. It then binds those tools to the model request to minimize context bloat from unnecessary tools in the main model call.

**Context management.** The model is only as good as what you put in front of it. For example, you might need to summarize when you&#x27;re approaching token limits and trim noisy tool inputs/outputs. Context engineering is a runtime problem, not a one-time prompt problem.

Deep dive: summarization and context offloading

LangChain’s builtin [SummarizationMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in?ref=blog.langchain.com#summarization) implements the `before_model` hook. To avoid context overflow, if message history exceeds a certain token threshold, its contents are summarized before being passed to the model. Extensions of this middleware implement a `wrap_tool_call` hook to extend verbose tool call inputs and outputs to the filesystem.

**Production readiness.** Middleware allows you to build in model/tool retry logic, model fallbacks, and human-in-the-loop with interrupts. These kinds of features don’t show up in demos, but are essential for production agents.

Deep dive: model retries

LangChain’s builtin [ModelRetryMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in?ref=blog.langchain.com#model-retry) implements the `wrap_model_call` hook in order to wrap a model’s API call with a retry handler. This handler supports retry configuration such as retry count, backoff factor, and initial delay (to troubleshoot rate limiting).

**Toolsets.** Inject tools that require custom setup and teardown around the agent loop like connecting to an external tool server, initializing a shell, or spinning up a sandbox.

Deep dive: shell tool middleware

LangChain’s [ShellToolMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in?ref=blog.langchain.com#shell-tool) implements the `before_agent` and `after_agent` hooks in order to initialize and teardown shell resources around the core agent loop. It also adds the shell tool to the model’s list of tools.

## Deep Agents case study

Deep Agents is a batteries included agent harness built entirely on `create_agent`, LangChain&#x27;s standard entry point for building agents, with an opinionated middleware stack on top.

Here are a few of the middlewares that power Deep Agents:

- `FilesystemMiddleware`: file-based context on/offloading and long-term memory
- `SubagentMiddleware`: subagents with context isolation
- `SummarizationMiddleware`: context overflow management for long-running tasks
- `SkillsMiddleware`: progressive disclosure of specialized capabilities
- And more!

For a full review of the middleware powering Deep Agents, see [this guide](https://docs.langchain.com/oss/python/deepagents/harness?ref=blog.langchain.com) and Vivek’s [anatomy of a harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) post.

On top of all of this - you can add even more middleware to Deep Agents to customize it for your use case!

## Why we’re betting on agent middleware

Models are getting more capable, and that will change parts of the middleware stack. Some of what Deep Agents does today — summarization, tool selection, output trimming — will eventually be absorbed into the model itself.

But the underlying need won&#x27;t change. Builders will always need levers for customization: deterministic policy enforcement, production readiness guardrails, use-case-specific business logic. None of that moves into the model. The harness is still where it lives, and middleware is still the cleanest way to expose it.

We&#x27;ve seen this play out since the LangChain v1 launch. Middleware lets different teams own different concerns, keeps business logic decoupled from core agent code, and makes it easy to reuse logic across an org. Building Deep Agents entirely on top of it convinced us it&#x27;s the right abstraction.

Want to get started from a barebones agent harness? Try out middleware in [`create_agent`](https://docs.langchain.com/oss/python/langchain/agents?ref=blog.langchain.com).

Want to build on top of a more robust agent harness? Try out middleware in [`create_deep_agent`](https://docs.langchain.com/oss/python/deepagents/quickstart?ref=blog.langchain.com).

Want to contribute your own middleware? See guides for that [here](https://docs.langchain.com/oss/python/integrations/middleware?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

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