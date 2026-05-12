---
title: "Deploy agents instantly with Agent Builder templates"
author: "LangChain Accounts"
date: "2026-01-21"
url: "https://www.langchain.com/blog/introducing-agent-builder-template-library"
---

Deep AgentsAgent Architecture

# Deploy agents instantly with Agent Builder templates

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 21, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa00c303b901d2c2375f_LangSmith-Agent-Builder.png)[LangSmith Agent Builder](https://www.langchain.com/langsmith/agent-builder?ref=blog.langchain.com) allows anyone to build an agent with a simple prompt. Ask it to build you a market research agent, and it will follow up with relevant questions to create what you need.

But sometimes you want to start with something that’s ready to go. Today we’re introducing the [Agent Builder Template Library](https://www.langchain.com/templates?ref=blog.langchain.com) and expanding our tool integrations to help you get from idea to working agent even faster.

Agent Builder templates are prebuilt agents for common jobs, with tools connected and agent instructions included. They’re ready to deploy and fully customizable. You can update your agent’s instructions, add tools, and set approval requirements.

Unlike traditional workflow automations, you don’t need to map every step and spend hours debugging changes. Just give your agent feedback like you would a teammate, and it learns.

0:00                            /0:331×

We built these templates with the companies who know their domains best, including Tavily, PagerDuty, Exa, Box, and Arcade, and we&#x27;re adding new templates regularly. [Explore the Template Library](https://www.langchain.com/templates?ref=blog.langchain.com)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa01c303b901d2c23776_Partner-logo-banner-7.png)

**Try out these agent templates today:**

- **Calendar Brief (Google Calendar): **Reviews your calendar each morning and sends you a summary with research on meeting participants.
- **Email Assistant (Gmail): **Categorizes your emails and drafts replies for your approval.
- **Incident Responder (PagerDuty):** Analyzes alerts, cross-references your runbook, and recommends actions.
- **Document intake review (Box): **Reviews file submissions and prepares a summary for your approval.
- **Talent sourcing (Exa):** Searches LinkedIn based on your job description and sends recommended candidate profiles.
- **Competitor research (Tavily):** Conducts deep competitive research and delivers concise reports.
- **Social Media Monitor (X + Slack): **Monitors X and sends a daily digest to Slack with the latest news.

> *“Agents are a powerful way to turn unstructured content into usable data. Across enterprises, a lot of document work is still manual today: checking completeness, validating accuracy, and extracting context for decision making. By combining the power of Box and Agent Builder, we are making it easy to add an agent to that loop, so teams can focus their time on decisions, not busywork.”*
— Ben Kus, CTO, Box

### See what’s possible with Arcade

Today, Agent Builder provides a set of ready made tool integrations and templates. However, there are a nearly infinite number of tools your team may want to connect via MCP. [Arcade](https://www.arcade.dev/?ref=blog.langchain.com)’s MCP Gateway makes an additional 8,000 tools available to Agent Builder for use cases spanning marketing, sales, recruiting, customer success, product, engineering, and general productivity.

To show what’s possible, Arcade developed a collection of 60+ ready-to-deploy Agent Builder templates, available in their own hosted gallery. Each template includes a step-by-step guide to set up and start using your agent. [Explore Arcade templates](https://www.arcade.dev/agents/langsmith-agentbuilder?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa01c303b901d2c23772_agent-builder-arcade-1.png)

### Choose the best model for your agent

Whether you&#x27;re starting from a prompt or a template, different jobs may call for different models. Cost, latency, and reasoning requirements vary depending on whether your agent is summarizing emails overnight or responding to questions in real time. That’s why Agent Builder doesn’t lock you into just one model. It supports OpenAI, Anthropic, and Google Gemini models, plus any custom or open source models that follow OpenAI or Anthropic specs.

To show what’s possible, Baseten [built an agent](https://www.baseten.co/blog/production-ai-for-non-technical-knowledge-workers-langchain-agent-builder-with-gl/?ref=blog.langchain.com) using their GLM 4.7 model that responds quickly for real-time user interaction. Connect your [preferred model provider](https://docs.langchain.com/langsmith/agent-builder-quickstart?ref=blog.langchain.com) to Agent Builder, and then you can get building.

### Turn your idea into a community template

This is only the beginning and we&#x27;re building alongside the community. If you&#x27;ve built an agent you love, whether it&#x27;s automating sales outreach, monitoring production systems, or conducting research, we’d love to hear about it.

Join our [Community Slack](https://www.langchain.com/join-community?ref=blog.langchain.com) and share it in #agent-builder-templates. We’re turning the best community agents into first-class templates.

## What&#x27;s next

We’re just getting started with Agent Builder and learning every day as more people build agents. Try Agent Builder for free today and share what you build in #agent-builder-templates.

Get started:

- [Try Agent Builder free](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com)
- [Explore the Template Library](https://www.langchain.com/templates?ref=blog.langchain.com)
- [Join the Community Slack](https://www.langchain.com/join-community?ref=blog.langchain.com)

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