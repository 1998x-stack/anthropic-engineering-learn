---
title: "LLM-powered Code Interpreters"
author: "Tereza Tizkova"
date: "2024-02-14"
url: "https://e2b.dev/blog/llm-powered-code-interpreters"
category: "ai-agents"
site: "e2b"
---

When I was talking to developers and community contributors about their projects with E2B, a few of them asked what is meant by **"code interpreter" in the context of AI agents**, and especially, how they differ from other AI coding apps. I summarized my understanding of this term and examples of popular LLM-powered code interpreters.

## Traditional definition

In the context of "traditional" software, a [code interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing)) is a type of program that reads and executes instructions written in a programming language. The interpreter translates ("interprets") high-level programming language into low-level machine language which the computer can understand and execute.

In the past, these code instructions were usually written by a human programmer. Just recently, we have added AI to the equation. Since the [boom of AI agents in 2023](/blog/the-state-of-ai-agents-reliability-sdks-benchmarking-and-market-trends), developers have been building code interpreters that include an intermediary in the form of an AI agent or assistant translating human prompts written in natural language into the code instructions for computers.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797884d17163e9c50349ee0_679787c6750db8dc69ab2919_OOVU6ff6YzTOJKRVgfge0ZjL2w.avif)

## LLM-powered code interpreter

How do AI code interpreters fit into the world of AI agents? One of the key features of  LLM-powered code interpreters is the ability to execute code, as opposed to only generating pieces of code that you as a user subsequently have to copy-paste and execute within your own program. The code execution capabilities are not a necessary part of every AI coding agent or assistant. 

The code execution capability implies for example an ability to create a new file on a given path, download files, or provide the result of an operation written as a code (e.g. executing a code that results in generating a chart based on data provided).

## Examples

These are popular examples of LLM-powered code interpreters, as described above:

- [Open Interpreter](https://openinterpreter.com/) - controls your computer via a terminal
- [Autogen](https://microsoft.github.io/autogen/) agents - Autogen is Microsoft's framework for AI agents. Autogen is Microsoft’s framework for AI agents. Autogen’s agents have the ability to execute code, for example, visualize your data in the form of a chart and save it as a file.
- [ChatGPT's Code Interpreter feature](https://openai.com/blog/chatgpt-plugins#code-interpreter) - one of the plugins for ChatGPT has the ability to execute code. (Without the plugin, ChatGPT just generates code and other content.)

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797884d17163e9c50349ee5_679787e531f719448b921b84_enCdBwUn5oKIYxgwANxsYknU.avif)](https://www.youtube.com/watch?v=HblQ_gx_4MI&ab_channel=E2B-CloudRuntimeforAIAgents)*Example: an *[*AI code interpreter*](https://www.youtube.com/watch?v=HblQ_gx_4MI&ab_channel=E2B-CloudRuntimeforAIAgents)* for GitHub that can execute LLM-generated output in a sandbox environment.*

In comparison, examples of products that (to this day) do not have code interpreter capabilities:

- LLM-powered chatbots like [ChatGPT](https://chat.openai.com/) (without code interpreter plugin), [Phind](https://www.phind.com/agent?home=true), [Perplexity](https://www.perplexity.ai/)
- [GitHub Copilot](https://github.com/features/copilot) —This coding assistant is able to automate users’ work and produce code in a text format, but not for example changing the content of your directory.

#### Read more

See a [blog post](/blog/limitations-of-running-ai-agents-locally) about the limitations of executing LLM-generated code locally.

‍