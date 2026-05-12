---
title: "Where AI Agents Are Heading: What We Learned from Recent YC Startups"
author: "Tereza Tizkova"
date: "2026-03-02"
url: "https://e2b.dev/blog/yc-companies-ai-agents"
category: "integrations"
site: "e2b"
---

AI agents are having a moment. Coding agents like [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/codex), and [Cursor](https://www.cursor.com/) are going mainstream, and highly autonomous ones are making a comeback, gaining the trust of enterprises. [Manus](/blog/how-manus-uses-e2b-to-provide-agents-with-virtual-computers) was acquired by Meta after just a few months of existence, and [Genspark](https://x.com/genspark_ai/status/1999358283052974414?s=20) (recently going viral with their Super Bowl ad) is serving Fortune 100 companies with 5M+ users. [OpenClaw](https://openclaw.ai/), the open-source AI agent that went massively viral, created 1.5 million agents in just weeks — showing that demand for autonomous agents is real and accelerating. Meanwhile, plenty of people still say AI is a bubble.

At [E2B](/), we are collaborating with selected agentic startups to help them grow and scale with our open-source cloud infrastructure. Our [startup program](/startups) is designed to support the companies that we believe will define the next generation of agent-powered software. From the latest batches, we talked to teams that are pushing the boundaries of what agents can do.

The founders behind these startups come from diverse backgrounds — some backed by top accelerators like Y Combinator and a16z, others supported by programs like Founders, Inc. and Z Fellows, and several are still pre-funding, building purely on conviction. Looking across these teams, several patterns become clear about where agents are actually headed — and what infrastructure they'll need to get there.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/69a5ddec7f99d2332001020d_Screenshot%202026-03-02%20at%2010.58.37.png)Some of the startups in the recent E2B for Startups program. Source: [e2b.dev/startups](/startups)

## Every Company Is Becoming an Agent Company

One of our biggest takeaways: agents are not a vertical anymore. They have become a layer in the product, and this layer has become an expected feature by many enterprises that are in turn starting to adopt the agentic product.

The numbers speak for themselves. Nearly [50% of some of the recent YC batches](https://pitchbook.com/news/articles/y-combinator-is-going-all-in-on-ai-agents-making-up-nearly-50-of-latest-batch) are AI agent companies. When we looked at the latest batch (YC W26 by the time of writing this article), we have identified even more. [80% of enterprises](https://www.salesmate.io/blog/future-of-ai-agents/?st_source=ai_mode#:~:text=By%202026%2C%20IDC%20expects%20AI,tools%20to%20proactive%20decision%2Dmakers.) are expected to implement AI agents by end of 2026.

The startups we selected for the E2B program aren't anymore just "AI agent companies" in the way we usually think about them. They're insurance companies, logistics companies, video production companies, DevOps platforms, and developer tools companies. The agent is how they deliver value, not what they sell to end users anymore.

> "We run Claude Code agents to generate Remotion video templates." — Resonate

‍

[Prox](https://www.getprox.com/) (YC F26) runs ticket resolution agents for logistics companies, [Arcline](https://arcline-ai.com) (YC W26) lets agents do legal documents drafting. These teams don't think about "AI agents" as a category, but they rather solve problems like insurance claims, shipping tickets, or video production. They focus on the end product, which is also the reason they are outsourcing the infrastructure building and maintenance to E2B AI cloud.

## Everything is Code

If we still try to point a finger at the most common use case, it is not surprisingly coding agents. That is, agents that write and run code to accomplish their tasks. The most popular ones — [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://openai.com/index/codex), [Cursor](https://www.cursor.com/), and [Gemini CLI](https://ai.google.dev/gemini-api/docs/gemini-cli) — are rapidly becoming the default way developers write software. Essentially, almost anything agents need to do comes down to writing code and running it in an isolated sandbox environment.

Claude Code alone went from $0 to [$1B in annualized revenue](https://x.com/selinazwang/status/1995975322953810055) in roughly six months after its public launch — the fastest product to hit that milestone. [Startups are the main early adopters](https://x.com/AnthropicAI/status/1916871421696917613), which tells you where the market will be moving. Agentic startup now primarily build products using other coding agents, or integrating them directly into products or offering them to enterprises in a secure way.

> "[E2B](https://www.linkedin.com/company/e2b-dev/) powers the orchestration layer that lets you go wild with --dangerously-skip-permissions without blowing up your local machines." — Runtime

[Rivet](https://rivet.gg/) (YC W23) is one of these examples, using E2B sandboxes for their [Sandbox Agent SDK](https://github.com/rivet-dev/sandbox-agent) — with many users running coding agents orchestrated through Rivet on E2B. [Fix.fast](https://fix.fast) is building a general-purpose productivity agent weorking in the E2B sandboxes. [Syntropy](http://syntropy.io/) (YC W26) uses E2B for agentic code execution — running unit and integration tests that the AI agents generate.

One of the critical requirements for agent infrastructure is concurrency — the ability to run many agent instances in parallel. Teams are running dozens of Claude Code and Codex instances simultaneously inside E2B sandboxes to accelerate engineering workflows.

> "We are running many Claude code and Codex instances in parallel to accelerate the team technical design process in large teams." — Scott AI (YC W25)

The maturity of the coding agent category tells us something about the broader market: once a category of agents proves out, adoption is fast and the focus immediately shifts to differentiation on top of the execution layer. Browser agents and vertical agents could be next.

## Agents Deserve Real Computers

E2B has been the pioneer in the AI sandbox category, starting from code interpreter use case, but evolving into a versatile long-running environment where agents install files, do research, or use diversity of tools. Since 2023 when we started, we've watched what teams expect from sandbox providers evolve. The expectations on the AI-first infrastructure have been rising, and features like persistence or good way of scaling have become the standard.

Manus, [Genspark](https://www.genspark.ai/), [OpenClaw](https://openclaw.ai/), and other general autonomous agents demonstrate that agents need to use computers the same way humans do. OpenClaw in particular showed the world what happens when you give an AI agent full system access — email, calendars, messaging, browsers, file systems — and let it act autonomously. The result was the [fastest-growing open-source project in GitHub history](https://x.com/aakashgupta/status/2021366401500664207): 9K to 182K stars in 60 days, outpacing Linux, React, and TensorFlow.

![OpenClaw GitHub stars growth chart — fastest growing open-source project, surpassing Linux and React](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/69a5d84c7300337b6f77bb62_69a4ed7c59b5be0527f931c3_openclaw-github-stars-growth.png)OpenClaw's explosive growth compared to Linux, React, TensorFlow, and AutoGPT. Source: [star-history.com](https://star-history.com) via [Aakash Gupta](https://x.com/aakashgupta/status/2021366401500664207)

But viral adoption also highlighted why [security and sandboxing](https://www.crowdstrike.com/en-us/blog/what-security-teams-need-to-know-about-openclaw-ai-super-agent/) are non-negotiable. [Critical authentication bypasses](https://aisle.com/blog/aisle-tops-openclaw-disclosures) and other issues were quickly discovered in OpenClaw. Problems like agents accessing operating system or critical data can be solved by the right isolation layer in the infrastructure.

![E2B sandbox architecture for autonomous AI agents — secure code execution with coordination layer](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/69a36ee7cf2c25731894c390_69a25495b5de00bd67dd3540_e2b-system-architecture.png)How agents run inside E2B: isolated sandboxes with coordinated task assignment, full tool access, and combined output — the same architecture powering Manus and Genspark.

> "Our E2B use case is Manus-like sandboxes for browser use, web research, voice calls, and image generation" — Waldium

## Build With Us

We're always looking for the next generation of agent-first companies to support through the [E2B startup program](/startups). The program includes E2B credits and all benefits of the E2B Pro tier plan. If you're building something ambitious with AI agents, we'd love to hear from you — apply for the next batch on the website, or get in touch at [startups@e2b.dev](mailto:startups@e2b.dev).

―

E2B is the open-source cloud infrastructure for AI agents. Secure virtual machines that spin up in milliseconds. [Get started →](/)