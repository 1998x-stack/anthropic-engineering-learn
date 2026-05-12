---
title: "Agent Engineering: A New Discipline"
author: "LangChain Accounts"
date: "2025-12-09"
url: "https://www.langchain.com/blog/agent-engineering-a-new-discipline"
---

Deep AgentsObservability &amp; Evals

# Agent Engineering: A New Discipline

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 9, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2ac540f9b55e27ee80_Agent-Engineering_-A-New-Discipline.png)If you’ve built an agent, you know that the delta between “it works on my machine” and “it works in production” can be huge. Traditional software assumes you mostly know the inputs and can define the outputs. Agents give you neither: users can say literally anything, and the space of possible behaviors is wide open. That’s why they’re powerful — and why they can also go a little sideways in ways you didn’t see coming.

Over the past 3 years, we’ve watched thousands of teams struggle with this reality. The ones who’ve succeeded in shipping something reliable to production — companies like Clay, Vanta, LinkedIn, and Cloudflare — aren’t following the traditional software playbook. They’re pioneering something new: **agent engineering.**

### What is agent engineering?

Agent engineering is the iterative process of refining non-deterministic LLM systems into reliable production experiences. It is a cyclical process: **build, test, ship, observe, refine, repeat.**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2ac540f9b55e27eead_Frame-1--2--1.png)

The key here is that shipping isn&#x27;t the end goal. It’s just the way you keep moving to get new insights and improve your agent. To make improvements that matter, you need to understand what’s happening in production. The faster you move through this cycle, the more reliable your agent becomes.

We see agent engineering as a new discipline that combines 3 skillsets working together:

- **Product thinking** defines the scope and shapes agent behavior. This involves:
Writing prompts that drive agent behavior (often hundreds or thousands of lines). Good communication and writing skills are key here.
- Deeply understanding the &quot;job to be done&quot; that the agent replicates
- Defining evaluations that test whether the agent performs as intended by the “job to be done”

- **Engineering** builds the infrastructure that makes agents production-ready. This involves:
Writing tools for agents to use
- Developing UI/UX for agent interactions (with streaming, interrupt handling, etc.)
- Creating robust runtimes that handle durable execution, human-in-the-loop pauses, and memory management.

- **Data science** measures and improves agent performance over time. This involves:
Building systems (evals, A/B testing, monitoring etc.) to measure agent performance and reliability
- Analyzing usage patterns and error analysis (since agents have a broader scope of how users use them than traditional software)

### Where agent engineering shows up

Agent engineering isn’t a new job title. Instead, it’s a set of responsibilities that existing teams take on when they’re building systems that reason, adapt, and behave unpredictably. The organizations shipping reliable agents today are extending the skills of engineering, product, and data teams to meet the demands of non-deterministic systems.

Here’s where the practice typically shows up:

- **Software engineers and ML engineers** writing prompts and building tools for agents to use, tracing why an agent made specific tool calls, and refining the underlying models
- **Platform engineers** building agent infrastructure that handles durable execution and human-in-the-loop workflows
- **Product managers** writing prompts, defining agent scope, and ensuring the agent solves the right problem
- **Data scientists** measuring agent reliability and identifying opportunities for improvement

These teams embrace rapid iteration, and you&#x27;ll often see software engineers tracing errors and handing off to PMs to tweak prompts based on those insights, or PMs identifying scope issues that require new tools from engineers. Each recognizes that the real work of hardening an agent happens through this cycle of observing production behavior and systematically refining based on what they learn.

### Why agent engineering, and why now?

Two fundamental shifts have made agent engineering necessary.

First, LLMs are powerful enough to handle complex, multi-step workflows. We’ve been seeing it with agents taking on whole jobs, not just tasks. Clay uses agents to handle everything from prospect research to personalized outreach and CRM updates. LinkedIn uses agents to scan massive talent pools for recruiting, ranking candidates and surfacing the strongest matches instantly. We’re starting to cross the threshold where agents are delivering meaningful business value in production.

Second, that power comes with real unpredictability. Simple LLM apps, though non-deterministic, tend to have more contained behavior. Agents are different. They reason across multiple steps, call tools, and adapt based on context. The same things that make agents useful also make them behave differently than traditional software. This usually means that:

- **Every input is an edge case.** There&#x27;s no such thing as a &quot;normal&quot; input when users can ask anything in natural language. When you type in “make it pop” or “do what you did last time but differently”, the agent (just like a human) can interpret the prompts in different ways.
- **You can’t debug the old way.** Because so much logic lives inside the model, you have to inspect each decision and tool call. Small prompt or config tweaks can create huge shifts in behavior.
- **“Working” isn’t binary.** An agent can have 99.99% uptime while still being off the rails and broken. There aren’t always simple yes/no answers to the questions that matter, like: is the agent making the right calls? Using tools the right way? Following the intent behind your instructions?

When you put this all together — agents running real, high impact workflows yet behaving in ways that traditional software can’t solve — there’s an opportunity and the need for a new discipline. Agent engineering lets you harness the power of LLMs while building systems you can actually trust in production.

### What does agent engineering look like in practice?

Agent engineering operates on a different principle than traditional software development. To achieve a reliable agent system, shipping is how you learn, not what you do after learning.

We’ve seen successful eng teams follow a cadence for agent development that looks something like this:

- **Build your agent’s foundation.** Start with designing your agent&#x27;s foundation, whether it&#x27;s a simple LLM call with tools or a complex multi-agent system. Your architecture depends on how much workflow (deterministic step-by-step processes) versus agency (LLM-driven decisions) you need.
- **Test based on scenario you can imagine**. Test your agent against example scenarios to catch obvious issues with prompts, tool definitions, and workflows. Unlike traditional software where you can map out user flows, you can&#x27;t anticipate every way users will interact with natural language input. Shift your mindset from &quot;test exhaustively, then ship&quot; to &quot;test reasonably, ship to learn what actually matters.”
- **Ship to see real-world behavior.** Once you ship, you’ll immediately start seeing inputs you hadn’t considered and every production trace shows what your agent actually needs to handle.
- **Observe.** Trace every every interaction to see the full conversation, every tool called, and the exact context that informed each decision the agent made. Run evals over your production data to measure agent quality, whether you care about accuracy, latency, user satisfaction, or other criteria.
- **Refine**. Once you’ve identified patterns in what&#x27;s failing, refine by editing prompts and modifying tool definitions. It’s all continuous, as you can add problematic cases back to your set of example scenarios for regression testing.
- **Repeat**. Ship your improvements and watch what’s changing in production. Each cycle teaches you something new about how users are interacting with your agent and what reliability actually means in your context.

### A new standard for engineering

The teams shipping reliable agents today share one thing: they&#x27;ve stopped trying to perfect agents before launch and started treating production as their primary teacher. In other words, tracing every decision, evaluating at scale, and shipping improvements in days instead of quarters.

Agent engineering is emerging because the opportunity demands it. Agents can now handle workflows that previously required human judgment, but only if you can make them reliable enough to trust. There is no shortcut, just the systematic work of iteration. The question isn&#x27;t whether agent engineering will become standard practice. It&#x27;s how quickly your team can adopt it to unlock what agents can do.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ea236ce872ec8be413bd2f_runtime-behind-production-deep-agents-thumbnail.png)Conceptual GuideDeep Agents

#### The runtime behind production deep agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Sydney RunkleVivek TrivedyApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)24min[](/blog/runtime-behind-production-deep-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)