---
title: "Debugging Deep Agents with LangSmith"
author: "LangChain Accounts"
date: "2025-12-10"
url: "https://www.langchain.com/blog/debugging-deep-agents-with-langsmith"
---

Deep AgentsLangSmithObservability &amp; Evals

# Debugging Deep Agents with LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 10, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1b866be8993c5156a1_Debugging-deep-agents-blog-header.png)Debugging is the process of finding and fixing errors. This is a critical step in software engineering, and even more critical in [agent engineering](https://blog.langchain.com/agent-engineering-a-new-discipline/). One of the key capabilities of [LangSmith](https://docs.langchain.com/langsmith/home?ref=blog.langchain.com) is tooling to debug LLM applications.

Today we are doubling down on solving that problem for the new wave of [“deep agents”](https://blog.langchain.com/doubling-down-on-deepagents/) we see being developed.

In this blog we:

- Explain why debugging deep agents is different than debugging simpler LLM applications
- Introduce [Polly](https://blog.langchain.com/introducing-polly-your-ai-agent-engineer/) (an AI assistant for agent engineering) to help in LangSmith for debugging deep agents
- Launch l[angsmith-fetch](https://blog.langchain.com/introducing-langsmith-fetch/), a CLI for equipping coding agents like Claude Code or DeepAgents CLI with debugging capabilities

## How Deep Agents are different than simpler LLM applications

Unlike simple LLM calls or short workflows, deep agents run for minutes, span dozens or hundreds of steps, and often involve multiple back-and-forth interactions with users.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156b3_Screenshot-2025-12-09-at-1.57.42---PM.png)

As a result, the traces produced by a single deep agent execution can contain an ton of information, far more than a human can easily scan or reason about. When something goes wrong, it may not be obvious which decision, prompt instruction, or tool call caused the behavior you’re seeing.

This is where tracing with LangSmith — and using AI to analyze those traces — becomes important. So, what specifically makes deep agents more complex?

- **Longer prompts:** The prompts for deep agents often span hundreds if not thousands of lines — usually containing a general persona, instructions on calling tools, important guidelines, and few-shot examples. When behavior degrades, it’s difficult to know which part of the prompt is responsible.
- **Longer traces:** Deep agents can run for dozens if not hundreds of steps (taking minutes to complete). When presented with such a large trace, there is simply more content for a human to parse through to find meaningful sections.
- **Multiple turns:** Deep agents enable human-in-the-loop workflows by default. A meaningful example conversation with a deep agent often involves several back and forth interactions. In order to understand what the agent did and see its full trajectory, you need to look across multiple interactions.

## Tracing captures relevant information

In order to debug an agent, you need to have visibility into what is happening inside. This is where tracing comes in.

We use the umbrella term **tracing** to describe logging your agent execution data to LangSmith. The data format consists of **runs, traces, and threads.**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156aa_Screenshot-2025-12-09-at-1.30.00---PM.png)
- **Runs:** A step that your agent takes. Examples include LLM model calls and tool calls. Runs are nested in a tree structure.
- **Traces:** A single execution of your agent. A trace is made up of a tree of Runs.
- **Threads:** A collection of Traces. A thread is a full conversation between a User and an application.

Tracing is super easy to set up - you can set it up in a few minutes by following this [guide](https://www.youtube.com/watch?v=fA9b4D8IsPQ&amp;ref=blog.langchain.com).

Once your application data is in LangSmith, you can leverage AI to analyze full agent trajectories to figure out what is going on, and then suggest updates to the prompt. There are two main ways to do this.

## Polly - an AI assistant for agent engineering

Polly is a [new in-app feature](https://blog.langchain.com/p/162fa797-0446-4a2b-86b5-49fdc007bfc3/?member_status=free) that allows you to chat with an agent to analyze your thread and trace data. See our [video overview here](https://youtu.be/4Ox2gdZnM6c?ref=blog.langchain.com).

Here are a few ways to chat with Polly!

**In the Trace view**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156ad_Screenshot-2025-12-09-at-7.29.41---PM.png)

You can use Polly to debug, analyze, and understand what happened in the Trace. Instead of manually scanning dozens or hundreds of steps, you can ask Polly questions like:

- “Did the agent do anything that could be more efficient”
- “Did the agent make any mistakes”

This is particularly helpful for deep agents, which tend to have longer traces where failure modes can be distributed across many steps.

**In the Thread view**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156b7_Screenshot-2025-12-09-at-7.30.46---PM.png)

This is similar to a single Trace, but here, Polly can access information from an entire thread. Threads span several conversational turns, and can oftentimes also span several hours or days. It’s hard for a person to stay aware of all of that context.

**In the Prompt Playground**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156b0_Screenshot-2025-12-09-at-7.32.17---PM.png)

One of the most important parts of a Deep Agent is the system prompt. Polly is tuned to be an excellent prompt engineer! Just describe the behavior you want in natural language and Polly will update your prompt accordingly. Polly can also help you define structured output or mock tools on your model call as well.

## LangSmith Fetch CLI - a tool to make your coding agent an expert agent engineer

If you prefer to work in your IDE or code agents (e.g., DeepAgents, Claude Code, etc), we have a CLI [`LangSmith Fetch`](https://github.com/langchain-ai/langsmith-fetch?ref=blog.langchain.com) that connects to LangSmith traces or threads easily. Whether you&#x27;re debugging an agent, analyzing conversation flows, or building datasets from production traces, this [CLI](https://blog.langchain.com/p/647419d5-fa7e-493f-a997-d81fd0009f7a/?member_status=free) provides fast, flexible access to your LangSmith traces and threads.

It bridges the gap between the LangSmith UI and your local workflow, letting you fetch traces or threads by ID when you know exactly what you want, or by time when you need to grab whatever just happened. With support for multiple output formats (human-readable panels, pretty JSON, or compact raw JSON), the tool adapts to your use case—whether you&#x27;re inspecting data in the terminal, piping to `jq`, or feeding results to an LLM for analysis.

It enables two key workflows. First, the &quot;I just ran something&quot; workflow to grab recent threads: you execute your agent, then immediately run `langsmith-fetch threads ./my_data` to grab the most recent traces in the project without hunting for IDs in the UI. Add temporal filters like `--last-n-minutes 30` to narrow your search, or use `--project-uuid` to target a specific project.

`# Just ran your agent? Grab the most recent trace immediately
langsmith-fetch traces --project-uuid &lt;your-uuid&gt; --format json

# Or grab the last 5 traces
langsmith-fetch traces --project-uuid &lt;your-uuid&gt; --limit 5
`

Second, the bulk export workflow: when you need datasets for evaluation or analysis, commands like `langsmith-fetch threads ./my-data --limit 50` fetch multiple threads and save each as a separate JSON file, perfect for batch processing or building test sets.

`# Or grab the last 5 traces from a specific project
langsmith-fetch traces --project-uuid &lt;your-uuid&gt; --limit 5
`

Of course, you can also supply a desired thread or trace ID. The output formats adapt to your needs: `--format pretty` for terminal viewing with Rich panels, `--format json` for readable structured data, or `--format raw` for piping to other tools.

## LangSmith makes it easy to debug and improve your deep agents

Deep Agents are powerful but longer running and more complex than simple LLM workflows. To understand and improve them, you need visibility into what your deep agents are actually doing.

With LangSmith, you can trace your deep agents and see what&#x27;s going on — then, chat with [Polly](https://blog.langchain.com/p/162fa797-0446-4a2b-86b5-49fdc007bfc3/?member_status=free) to analyze your deep agent’s behavior and use AI to help you improve your prompts. If you&#x27;d rather analyze it with Claude Code or another coding agent - you can use [LangSmith Fetch](https://blog.langchain.com/p/647419d5-fa7e-493f-a997-d81fd0009f7a/?member_status=free) to equip your coding agents with all the debugging tools necessary.

Set up tracing in just a few minutes, and try chatting with Polly today on LangSmith to debug and improve your deep agents!

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