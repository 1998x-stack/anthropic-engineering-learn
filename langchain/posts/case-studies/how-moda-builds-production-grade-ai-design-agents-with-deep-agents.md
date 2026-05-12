---
title: "How Moda Builds Production-Grade AI Design Agents with Deep Agents"
author: "LangChain Accounts"
date: "2026-03-24"
url: "https://www.langchain.com/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents"
---

Case StudiesDeep AgentsDeployment

# How Moda Builds Production-Grade AI Design Agents with Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 24, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f4795_Nullframe-Moda.png)[Moda](https://moda.app/?ref=blog.langchain.com) is an AI-native design platform for non-designers like marketers, founders, salespeople, and small business owners who need professional-grade presentations, social media posts, brochures, and PDFs without a design background. Think Canva or Figma, but with a Cursor-style AI sidebar that builds and iterates on designs directly on a fully editable 2D vector canvas.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f47c0_moda-chat.png)

At the core of Moda is a multi-agent system built with **Deep Agents**, with **LangSmith** providing the observability layer that lets the team iterate quickly and ship with confidence.

## The Challenge: Making AI Good at Visual Design

AI code generation works well partly because HTML and CSS already have layout abstractions like Flexbox and grid. You describe relationships and relative sizes, not pixel coordinates.

Visual design has no equivalent. The closest thing to a standard is PowerPoint&#x27;s XML spec, a 40-year-old format packed with verbose, absolute XY coordinates that LLMs are notoriously bad at reasoning about. Tools that use XML produce designs that look like every other AI-generated deck.

Moda needed a system that could generate designs that actually look good, and an agent architecture capable of handling complex, multi-turn, visually-grounded tasks at production quality.

## Agent Harness: Built on Deep Agents

Moda&#x27;s AI system consists of three agents:

- **Design Agent:** the primary agent behind the Cursor-style sidebar, handling all real-time design creation and iteration on the canvas
- **Research Agent:** fetches and stores structured content from external sources (e.g., a company&#x27;s website) into a per-user file system within Moda
- **Brand Kit Agent:** ingests brand assets (colors, fonts, logos, brand voice) from websites, uploaded brand books, or existing slide decks, so every design feels on-brand from the start

The **Research Agent and Brand Kit Agent both run on Deep Agents**. These are the team&#x27;s newest agents, which they&#x27;ve invested in heavily. The Design Agent runs on a custom LangGraph loop — an older implementation built before Deep Agents — and the team is actively evaluating migrating it as well.

All three agents share the same overall architecture: a lightweight triage step, a main agent loop, dynamic context loading, and full tracing in LangSmith.

## Context Engineering: The Details That Matter

Getting a design agent to produce genuinely good output that is visually coherent and brand-accurate (not just technically correct) required a lot of intentional context engineering.

Here&#x27;s what Moda figured out.

### A Custom DSL Instead of Raw Scene Graph

One of the hardest parts of building a design agent is figuring out how to represent visual layouts in a way LLMs can reason about effectively. Raw canvas state is verbose, coordinate-heavy, and token-expensive — not a natural fit for how models think about structure and layout.

Moda developed a context representation layer that gives the agent a cleaner, more compact view of what&#x27;s on the canvas, which reduces token cost and improves output quality. The specifics are proprietary, but the general principle is the same one that makes LLMs effective at web development: give the model layout abstractions it can reason about, rather than raw numerical coordinates.

&quot;LLMs are not good at math. PowerPoint&#x27;s XML spec has a bunch of XY coordinates — that&#x27;s a fine representation of the data, but it&#x27;s not a great way for an LLM to describe where it wants things to live.&quot; — Ravi Parikh, Co-Founder, Moda.app

Deep Agents and LangSmith were critical here. The team used LangSmith traces extensively to evaluate how different context representations affected agent behavior, iterating on what information to include, how to structure it, and where caching breakpoints made the biggest difference to cost and latency.

### Triage → Skills → Main Loop

Every request passes through a lightweight triage node (using fast and cheap Haiku models) before reaching the main agent. The triage node classifies the output format (slide deck, PDF, LinkedIn carousel, logo, etc.) and pre-loads the relevant **skills,** which are Markdown documents containing design best practices, format guidelines, and task-specific creative instructions.

Skills are injected as human messages, with **prompt caching breakpoints** placed after the system prompt and after the skills block. This keeps the system prompt fixed and always cached while allowing dynamic context injection per request.

The main agent can also pull in additional skills mid-loop if it determines it needs them. The triage step just front-loads the high-confidence ones to avoid an unnecessary extra turn.

### Dynamic Tool Loading

The design agent runs with 12–15 core tools in context at all times. An additional ~30 tools are available on demand via a `RequestToolActivation` tool the agent can call when it recognizes a specialized need, like parsing an uploaded PowerPoint file.

Each additional tool costs 50–300 tokens in the prefix, and loading new tools breaks prompt caching. But the math works out: the vast majority of requests don&#x27;t need the extra tools, so keeping context lean wins overall.

&quot;If I just look at the data, most requests do not need any additional tools activated, and there&#x27;s something really nice about only having 12 to 15 tools in context.&quot; — Ravi Parikh

### Scaling Context to Canvas Size

Not every request needs full visibility into the entire project. For smaller canvases, the agent works with a complete view of the current state. For larger projects — a 20-slide deck, for instance — Moda dynamically manages how much context the agent receives, giving it a higher-level summary and letting it pull in details as needed through tooling.

This keeps token usage bounded without sacrificing the agent&#x27;s ability to make informed design decisions across complex, multi-page projects. LangSmith&#x27;s cost tracking per node made it straightforward to find the right balance between context richness and efficiency.

## UX: The Cursor Moment for Design

One of Moda&#x27;s most deliberate product choices is the interaction model. Rather than a generate-and-replace flow, where AI produces a static output and hands it off, Moda&#x27;s AI works directly on a fully editable 2D vector canvas. Every element the agent creates is immediately selectable, movable, resizable, and styleable by the user.

This changes the relationship between user and AI from &quot;accept or reject&quot; to genuine collaboration. The AI generates a solid starting point and the user refines it. Neither has to do all the work.

The Cursor-style sidebar reinforces this: it&#x27;s always present, always contextually aware of what&#x27;s on the canvas, and designed for iterative back-and-forth rather than one-shot generation. For non-designers especially, this removes the intimidation of the blank canvas while keeping them in control of the final result.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f47c3_moda-ui.png)

## Observability with LangSmith

Because all three agents are traced through LangSmith, Ravi has full visibility into every execution. He keeps it open whenever he&#x27;s actively developing.

Key workflows:

- **Prompt &amp; tool iteration:** make a change, run a query, pull up the trace immediately to see exactly what the agent did and why
- **Cost tracking:** token cost broken down per node, making expensive steps easy to spot
- **Cache hit analysis:** especially important given the dynamic skill and tool loading; quickly surfaces where caching is working and where it&#x27;s breaking down
- **Error diagnosis:** surfacing tool call failures and unexpected model behavior before they become user-facing issues

&quot;If I&#x27;m iterating on the prompt, if I&#x27;m iterating on the tool set, I&#x27;m going to make a change, run a query, and then pull up that trace in LangSmith and just look at what happened... It&#x27;s made us move faster.&quot; — Ravi Parikh

Moda doesn&#x27;t yet run formal evals but it&#x27;s on the roadmap. For now, LangSmith traces serve as the primary feedback loop for catching regressions and validating improvements.

## Results &amp; What&#x27;s Next

Moda has found strong early product-market fit with B2B companies doing enterprise sales: teams that need polished, brand-accurate pitch decks fast. The combination of the fully editable canvas and the Deep Agents-powered backend means users get a professional starting point they can actually refine, not a static output they&#x27;re stuck with.

Next up: wiring up the memory primitives that are already in place, completing the Deep Agents migration for the Design Agent, and expanding the brand context system to support multi-team, multi-brand enterprise customers.

Interested in building production AI agents? [Get started with LangChain Deep Agents](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)