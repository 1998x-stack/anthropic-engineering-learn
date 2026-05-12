---
title: "A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense"
author: "LangChain Accounts"
date: "2026-04-16"
url: "https://www.langchain.com/blog/secure-agents-cisco-ai-defense"
---

LangChainPartner

# A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)

## Key Takeaways

- **Middleware is the right place to enforce agent security.** Adding security checks at the middleware layer keeps your `langchain` code clean and creates one consistent enforcement point across the agent loop, instead of bolting on logic across prompts, tools, and custom orchestration code.
- **Cisco AI Defense gives you two modes: monitor and enforce.** Monitor mode records risk signals and decision traces without interrupting the agent. Enforce mode blocks policy violations with an auditable reason, so you can always point to exactly what was stopped and why.
- **Protection applies across LLM calls, MCP tool calls, and middleware.** Agents don&#x27;t just generate text, they call tools, retrieve data, and take actions autonomously. Runtime protection needs to cover all three layers, especially in multi-agent systems where an orchestrator is chaining agents together at runtime.

*This is a guest post by Siddhant Dash, Senior Product Manager @ Cisco AI Defense.*

## The problem

`langchain` makes it easy to move from a working prototype to a useful agent in very little time. That is exactly why it has become such a common starting point for enterprise agent development. 

Agents don’t just generate text. They call skills, tools, retrieve data, and take actions autonomously. That means an agent can touch sensitive systems and real customer data within a single workflow. This compounds with multi-agent systems where an orchestrator agent is chaining many agents together and executing commands at runtime. 

But visibility alone isn’t enough. In real deployments, you need clear enforcement points, places where you can apply policy consistently, block risky behavior, and keep an auditable record of what happened and why.

## Why middleware is the right seam

Middleware is the clean integration point for agent security because it sits in the path of agent execution, without forcing developers to scatter checks across prompts, tools, and custom orchestration code.

This matters for two reasons.

- It keeps the application readable. Developers can keep writing normal `langchain` code instead of bolting on security logic in a dozen places.
- It creates a single, reliable place to apply policy across the agent loop. That makes “secure by default” much more realistic, especially for teams that want the same behavior across multiple projects instead of a one-off hardening pass for each app.

## Cisco AI Defense + LangChain: How it works

At a high-level, [Cisco AI Defense Runtime Protection ](https://github.com/cisco-ai-defense/ai-defense-python-sdk)integrates into a `langchain` agent through middleware and produces a consistent runtime contract:

- **Decision: **allow / block
- **Classifications:** what was detected (ex: prompt injection, sensitive data, exfiltration patterns)
- **`request_id` / `run_id`: **correlation for audit and debugging
- **`raw logs`: **full trace for investigation

There are a few ways to apply that protection, depending on where you want the control to live:

**LLM mode (model calls): **Protects the prompt/response path around LLM invocation.

**MCP mode (tool calls): **Protects MCP tool calls made by the agent (where a lot of real-world risk lives).

**Middleware mode: **Protects the `langchain` execution flow at the middleware layer, which is often the cleanest fit for modern agent apps.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e266ec3ff3fadff70eba_image1.gif)

### Monitor vs. Enforce (the “aha”)

**Monitor mode** gives you visibility without breaking developer flow. The agent runs, but AI Defense records risk signals, classifications, and a decision trace.

**Enforce mode** turns those signals into a control: Policy violations are blocked with an auditable reason. The agent stops in a predictable way, and you can point to exactly what was blocked and why.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e28b66e3b119de5f930f_image3.png)

## Check out the Cisco AI Defense developer quickstart

To make this easy to evaluate, we built a [developer launchpad](http://dev.aidefense.cisco.com) that lets you run both LLM mode and MCP mode workflows side-by-side in monitor and enforce modes.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e3165773cb47199cf613_image2.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e328a0a14544e83f0a62_image5.png)

### 3-step quick start (10 minutes)

- Open the demo runner

Link: [http://dev.aidefense.cisco.com/demo-runner](http://dev.aidefense.cisco.com/demo-runner)

- Pick a mode

LLM mode (model calls)
- MCP mode (tool calls)
- Middleware mode (LangChain middleware)

- Run a scenario

Choose one of the built-in prompts, such as a safe prompt, a prompt injection attempt, or a sensitive data request.
- Watch the workflow execute side-by-side in Monitor and Enforce modes so you can compare behavior against the same input.

**Monitor: **see the decision trace without blocking
- **Enforce: **trigger a policy violation and see “blocked and why”

## Upstream LangChain Path

We’re contributing this integration upstream via LangChain’s middleware framework so teams can adopt it using standard LangChain extension points.

LangChain middleware docs are available on [their website](https://docs.langchain.com/oss/python/langchain/middleware/overview).

If you’re a `langchain` user and want to shape how runtime protections should integrate, we’d welcome feedback and reviews.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77e612836396625baafec_69--2-.webp)Company AnnouncementsPartner

#### Announcing the LangChain + MongoDB Partnership: The AI Agent Stack That Runs On The Database You Already Trust

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 31, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)6min[](/blog/announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)