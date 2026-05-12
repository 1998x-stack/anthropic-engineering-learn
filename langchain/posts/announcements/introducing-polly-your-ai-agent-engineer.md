---
title: "Introducing Polly: Your AI Agent Engineer"
author: "LangChain Accounts"
date: "2025-12-10"
url: "https://www.langchain.com/blog/introducing-polly-your-ai-agent-engineer"
---

Agent Architecture

# Introducing Polly: Your AI Agent Engineer

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 10, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa230728009988d3ef59_Polly.png)Today, we&#x27;re launching **Polly:** an AI-powered assistant built directly into LangSmith that helps you debug, analyze, and improve your agents.

And yes, we see the irony: we&#x27;re adding an agent to a product for building agents.

We&#x27;ve spent a lot of time working with thousands of developers build production agents on LangSmith. We&#x27;ve seen what agents are genuinely good at (analyzing complex traces, spotting patterns across hundreds of steps) and what they&#x27;re not (replacing thoughtful engineering decisions). We wanted to get this right.

The result is Polly: an AI agent engineer that understands agent architectures, recognizes failure patterns, and actually helps you ship better agents faster. Polly is now available in beta.

## Why agents need an AI debugging partner

Through working with thousands of teams building agents on LangSmith, we&#x27;ve seen the same debugging challenges emerge repeatedly. Agents are fundamentally different from simple LLM calls due to:

- **Longer prompts:** System prompts often span hundreds or thousands of lines. When behavior degrades, finding which instruction is responsible is nearly impossible.
- **Longer traces:** Agents can run for hundreds of steps, generating thousands of data points in a single trace - far more than a human can parse effectively.
- **Multiple turns:** Agents involve multi-turn conversations that span hours or days. Understanding what happened requires looking across the entire interaction history.

When something goes wrong, you can&#x27;t easily pinpoint which decision, prompt instruction, or tool call caused it. This is the kind of problem where an AI agent engineer excels - and why we built Polly.

## Polly helps with debugging traces, analyzing conversations, and engineering better prompts

Instead of manually scanning through endless traces or guessing which prompt change will fix an issue, you can simply ask Polly questions in natural language. It&#x27;s like having an expert agent engineer on your team. Here&#x27;s what Polly can do today:

### Debug Individual Traces

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156ad_Screenshot-2025-12-09-at-7.29.41---PM.png)

In the Trace view, Polly analyzes single agent executions to help you understand what happened. This is where Polly really shines - deep agents can have traces with hundreds of steps, and failure modes are often subtle, distributed across many steps, or buried in the middle of a long execution.

Ask Polly questions like:

- &quot;Did the agent do anything that could be more efficient?&quot;
- &quot;Did the agent make any mistakes?&quot;
- &quot;Why did the agent choose this approach instead of that one?&quot;
- &quot;Where exactly did things go wrong?&quot;

Polly doesn&#x27;t just surface information. It understands agent behavior patterns and can identify issues you&#x27;d miss even after careful manual inspection.

### Analyze Entire Conversations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156b7_Screenshot-2025-12-09-at-7.30.46---PM.png)

In the Thread view, Polly can access information from entire conversations which sometimes span hours, days, or dozens of back-and-forth interactions. This is context that&#x27;s impossible for a human to keep in their head.

Ask Polly to:

- Summarize what happened across multiple interactions
- Identify patterns in agent behavior over time
- Explain why the agent&#x27;s approach changed between turns
- Spot when the agent lost track of important context

This is especially powerful for debugging those frustrating issues where &quot;the agent was working fine, and then suddenly it wasn&#x27;t&quot;. Polly can pinpoint exactly where and why things changed.

### Engineer Better Prompts

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa1c866be8993c5156b0_Screenshot-2025-12-09-at-7.32.17---PM.png)

This is where Polly gets really powerful. The system prompt is the most important part of any deep agent, and Polly is an expert prompt engineer.

Just describe the behavior you want in natural language, and Polly will update your prompt accordingly. No more manually tweaking hundreds of lines of instructions, trying to figure out the right phrasing, or wondering if you&#x27;ve broken something else while fixing one issue.

Polly can also help you:

- Define structured output schemas
- Configure tool definitions
- Add or refine few-shot examples
- Optimize prompt length without losing critical instructions

## How Polly works with LangSmith tracing

Polly&#x27;s intelligence comes from LangSmith&#x27;s comprehensive tracing infrastructure. LangSmith captures everything your agent does:

- **Runs:** Individual steps like LLM calls and tool executions
- **Traces:** A single execution of your agent, made up of a tree of runs
- **Threads:** A full conversation, containing multiple traces

Setting up tracing in LangSmith takes just a few minutes - [follow this guide](https://www.youtube.com/watch?v=fA9b4D8IsPQ&amp;ref=blog.langchain.com) to get started. Once your data is flowing into LangSmith, Polly can immediately start helping you analyze agent behavior, identify issues, and improve prompts.

## Get started with Polly

Polly can already analyze traces, debug conversations, and engineer prompts. But overtime we will teach it how to analyze experiments, optimize prompts, and more.

**Ready to get started with Polly?**

- [Set up tracing](https://www.youtube.com/watch?v=fA9b4D8IsPQ&amp;ref=blog.langchain.com) in just a few minutes
- Start building and debugging your agents with LangSmith
- Chat with Polly and experience the future of agent engineering

You can see [this video walkthrough](https://youtu.be/4Ox2gdZnM6c?ref=blog.langchain.com) for more more details on how to start using Polly.

LangChain is the agent engineering platform trusted by thousands of teams shipping production agents. And now, with Polly, you have an AI expert helping you every step of the way.

[Try Polly today](https://smith.langchain.com/?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)