---
title: "Limitations of Running AI Agents Locally"
author: "Tereza Tizkova"
date: "2024-02-09"
url: "https://e2b.dev/blog/limitations-of-running-ai-agents-locally"
category: "integrations"
site: "e2b"
---

Like many developers, I have been recently building my own coding AI agent.

I was inspired by a lot of popular code interpreters and AI coding frameworks I have seen lately, like [Open Interpreter](https://openinterpreter.com/), [Autogen](/ai-agents/open-interpreter), or [ChatGPT Code Interpreter plugin](https://openai.com/blog/chatgpt-plugins#code-interpreter).

The coding agents' value for daily usage has increased after they have **evolved from just chatting, to doing the actual work**. Developers are equipping their agents with the ability to **execute LLM-generated code output**.

Imagine you are using an AI agent that can analyze and visualize given data, but instead of just providing you a code that you can copy-paste to do the task, the agent conducts the next step and also runs the code to produce a chart and saves it to your local filesystem.

For example, when I used AutoGen to analyze stock data. The AI agents generated the required code, executed it, and saved the resulting data analysis chart in a PDF format on my computer:

When a human user chooses to execute the code, the output opens in a new window like this:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797874f99cf3b77c548221d_679786eb61d6b9b50cd00a5c_i4D0DFLwLMzYJv1b3OQTuBn6QbI.png)

The code execution is often done locally via containers, e.g., Docker, like in the case of Autogen. Many developers that I talked to started building their own in-house solutions for running AI code.

Running the AI output on the user's computer is an achievable, but risky way. Here are a few obvious and less obvious issues that I had, and noticed other AI developers mentioning:

## 1. Security + isolation

Allowing AI tools to autonomously run untrusted LLM-generated operations on users' computers can be problematic.

Take for example Docker containers, that (according to [their docs](https://docs.docker.com/engine/security/)) possess a risk of providing incomplete isolation, either independently, or when used in combination with kernel vulnerabilities.

When using containers, ensuring isolation is very difficult even when adding barriers.

## 2. User-centric approach

The approach to building AI agents has begun as developer-centric, which is understandable for any emerging field or technology.

This can result in end users facing difficulties with all the AI products that were built using Docker or another type of local solution.
The majority of AI assistants with nice user experience I came across were browser apps - people often ask how to filter AI tools based on whether they provide nice UI. It's worth noting that apps don't necessarily have to be used solely on desktop and some provide better functionalities on a mobile version.

Non-technical users may struggle with installing an app locally, let alone controlling it via a terminal.

## 3. Scalability

Another challenge that is particularly important for agent-building frameworks is deploying AI agent instances so they can scale. An AI platform or service that accommodates thousands of users, each developing its own AI applications, will require thousands of containers, as each agent instance needs to run in its own isolated environment. 

## 4. Session length

A lot of developers want their end users to be able to return to their work after some time or even after closing and re-opening the app. Developers need to ensure long-running sessions for their AI products.

In conclusion, end users apply their UX and security standards from using "traditional" software to AI apps.

Issues like security and data privacy have been discussed even more in relation to AI.

Within the new AI tech stack that is being formed, developers need to think of a solution that would be tailored for building AI products.

‍

#### E2B - Remote execution of AI-generated output

[E2B](https://github.com/e2b-dev/E2B) (5.7K+ ⭐️) provides the cloud runtime for AI agents and apps.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797874f99cf3b77c5482219_6797872c0c8d0972a99ede23_Hm93puCXmYFZYhT5bU2AAkiyoRE.avif)

The E2B Sandbox is a secure way to run your AI app. It is a long-running cloud environment where you can let any LLM (GPTs, Claude, local LLMs, etc) use tools as you would do locally.

Check out the quick start in the docs to start with E2B for free: [https://e2b.dev/docs](/docs).