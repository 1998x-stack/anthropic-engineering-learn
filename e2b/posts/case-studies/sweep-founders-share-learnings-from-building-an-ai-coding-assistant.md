---
title: "Sweep Founders Share Learnings from Building an AI Coding Assistant"
author: "Tereza Tizkova"
date: "2023-09-01"
url: "https://e2b.dev/blog/sweep-founders-share-learnings-from-building-an-ai-coding-assistant"
category: "case-studies"
site: "e2b"
---

‍**Coding and code debugging** have been the most common use case of AI agents, just some of the many examples including [Smol Developer](https://github.com/smol-ai/developer), [GPT Engineer](https://github.com/AntonOsika/gpt-engineer), [AutoPR](https://github.com/irgolic/AutoPR), [ReactAgent](https://reactagent.io/), and [Bloop](https://bloop.ai/). [**Sweep**](https://github.com/sweepai)** represents this category of agents in **[**YC S23**](https://www.ycombinator.com/companies/sweep).

[Sweep](https://sweep.dev/) works by **generating code on GitHub issue submissions**, e.g. your bugs and feature requests. It generates code in the form of **pull requests**, which the user can **comment on and iterate** until reaching their desired result. The following diagram shows the pipeline of turning an issue into a pull request.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a260fc999445d5008218_6797a1d5dc0cc9f6e08d18e8_4E3lY34GoUhRYztcZdm7BT2xb7I.avif)Source: [docs.sweep.dev](https://docs.sweep.dev/blogs/sweeps-core-algo)

We asked the [Sweep](https://sweep.dev/) founders - [William Zeng](https://twitter.com/wwzeng1) and [Kevin Lu](https://twitter.com/kevinlu1248) - for their view on the current agents' space, and the challenges they are working on to solve for the agents.

## Users and Use Cases

[**Sweep**](https://github.com/sweepai)** works with Github issues**. Given an issue, the [Sweep](https://sweep.dev/) agent plans how to solve it, writes code, and turns the issues directly into a pull request (without an IDE). It uses **embedding-based code search**.

The **initial startup time usually takes 3-5 minutes**, depending on the codebase. Users can iterate on results by adding comments to pull requests.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a260fc999445d5008225_6797a1f10a7cba0488066f2e_tX527kq22PlIp7LXnPw5QSpgdnQ.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a260fc999445d5008221_6797a1ff94dfa88445bcc95e_7NTsrnhiDgeSqxIyJk7qfRtLKJ4.avif)Source: [github.com/sweepai](https://github.com/sweepai/sweep/blob/main/docs/installation.md)

‍

As many agents for developers, it is **open-source**, and getting increasingly popular, with over [5000 stars on GitHub](https://github.com/orgs/sweepai/repositories).

“We target really strong developers and try to help be as efficient as possible” say the founders.

The current total usage is **around 100 pull requests a day**. What the end users build with [Sweep](https://sweep.dev/) differs, since the developers are utilizing it for their existing projects. 

## Current Challenges

Sometimes the agent straight away gets the wrong idea or uses the wrong format for the result of the task. If there is a bug, they can go and twist a prompt a little bit, and fix it.

“Given that the **agent operates in a linear manner**, it is usually easy to determine what caused the issue and decompose the process into steps,” said Kevin and William.

The agent’s workflow is pretty constrained and so, there is no need to stop it in the middle. Instead, when a bug happens, **restarting the whole process is the most pragmatic way**. 

## Debugging tools

**Debugging has been a struggle for most agents’ developers**, and there is no strong consensus about agent-specific [tools or frameworks](https://github.com/e2b-dev/awesome-sdks-for-ai-agents) used for debugging agents' prompts and errors in general.

“With Sweep, the process of debugging usually involves **looking through the history of the conversation with the agent**,” summarize the Sweep founders, who **created their own internal tool to visualize the chats**.

“We built this **chat visualizer** in 2 hours,” say Kevin and William. “If a user contacts us, **with their permission to view their logs for debugging purposes, we can visualize what happened and fix what needs to be fixed, then click redeliver.**"

End users cannot access the visualization, so they usually contact the Sweep team. “This happens about once a day”, William and Kevin say. 

The following image shows [Sweep](https://sweep.dev/)’s internal visualization of agents’ bugs.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a260fc999445d500821e_6797a215cceddeedd918055f_NaC59pnPEAKA1HVojUGiR1xkSg.avif)Source: [Sweep](https://sweep.dev/), internal

## Communication with users

The **user experience is very server-centralized**, as Kevin and William comment: “If the servers have an issue, everyone has an issue.” The [Sweep](https://sweep.dev/) team often **learns about issues directly from the end users** and consequently assists in fixing them.

The Sweep team aspires for users to engage their agents in meaningful work-related tasks, not just playing with [test repositories](https://github.com/sweepai/create-react-app) or experimenting.  “Since we found at the start that developers are still using AI agents for the sake of exploring new technologies and having fun, we focused our strategy on **limiting the usage of Sweep**. This way, the **users are mindful and use Sweep for the actual work**.”

They hence limit to **5 uses a month of **[**GPT-4**](https://openai.com/gpt-4)**, the rest of GPT-3.5**. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a260fc999445d500821b_6797a229b624d694ac1eb4c8_ujfaOa0TXdOsxXTS3S5qkylfhk.avif)Source:  [Testing Sweep on E2B team GitHub](https://github.com/e2b-dev)

## Conclusion

Users can work with [Sweep](https://sweep.dev/) independently, without assistance. William and Kevin never stop developing their agent and **making even bigger progress toward agents becoming regular work tools**.  “Currently, we are reading a lot into the old style of indexing code. The goal is to become proficient in both code understanding and agent understanding.”

If you want to try [Sweep](https://github.com/sweepai/sweep), you can install it via [https://github.com/apps/sweep-ai](https://github.com/apps/sweep-ai). After installation, you can add the repository you want the agent to work on, make a ticket (e.g. writing tests), add the label "sweep" and watch the AI agent do the work.

If you are interested in open-source agents for developers and coding, check the whole [AI agents database](https://github.com/e2b-dev/awesome-ai-agents).