---
title: "Not Another Workflow Builder"
author: "LangChain Accounts"
date: "2025-10-07"
url: "https://www.langchain.com/blog/not-another-workflow-builder"
---

Harrison&#x27;s In the LoopLangSmith

# Not Another Workflow Builder

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseOctober 7, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa6c1bfa8a96ce618649_Visual__Agent_Builder_Template_Assets.webp)*By Harrison Chase*

One of the most common requests we've gotten from day zero of LangChain has been a visual workflow builder. We never pursued it and instead let others (LangFlow, Flowise, n8n) build on top of us. With OpenAI launching a [workflow builder](https://openai.com/index/introducing-agentkit/?ref=blog.langchain.com) at Dev Day yesterday, I thought it would be interesting to write about why we haven't built one to date, and what different (but related) directions we are more interested in.

## The problem statement

First of all, it's worth aligning on the problem statement these no-code workflow builders solve. The main motivation is to allow non-technical users to build agents. There's two main reasons people are interested in this:

- Many companies are more resource constrained on engineering talent than others
- Non-technical users are the ones who know what agents to build / what they should do

We occasionally see other motivations, like allowing technical users to quickly prototype agents that will get ported into code later. But for the purpose of this blog let's assume that the motivation is to enable everyone in an organization to build their own apps and widgets without support from engineering.

## Workflows vs agents

Two words which I've used intentionally above are “workflows” and “agents”. We've written about this before - actually in a blog post [arguing for workflows](https://blog.langchain.com/how-to-think-about-agent-frameworks/) (ironically, in response to an OpenAI article arguing against workflows).

The developer community has largely settled on the [following definition of an agent](https://simonwillison.net/2025/Sep/18/agents/?ref=blog.langchain.com):

💡

An LLM agent runs tools in a loop to achieve a goal.

Workflows give you more predictability at the expense of autonomy, while agents give you more autonomy at the expense of predictability. **Notably, when building agentic systems we are in pursuit of *reliably good* outcomes, which neither predictability or autonomy alone guarantee.**

Workflows are often complicated - branching logic, parallel edges, many different paths. This complexity is represented in the “graph” of the workflow, which is represented in some DSL.

Agents can also contain complicated logic, but by contrast all that logic is abstracted away into natural language, which goes into the prompt. So the overall structure of an agent is simple (just a prompt + tools), though that “prompt” can often times be pretty complex.

OpenAI's AgentKit - and n8n, Flowise, LangFlow - are all visual **workflow** builders - not *agent* builders.

## The issue with visual workflow builders

So, with all that context, what is the problem with workflow builders:

**1.Visual workflow builders are not “low” barrier to entry.**

Despite being built for a mass audience, it is still not easy for the average non-technical user to use them.

**2.Complex tasks quickly get too complicated to manage in a visual builder.**

As soon as they pass a certain level of complexity (which happens pretty quickly) you end up with a mess of nodes and edges that you need to manage in the UI.

## Other alternatives

The goal is to create LLM powered systems (whether workflows or agents) that are *reliably good*. There are different types of problems that people may want to solve with LLM powered systems - ranging anywhere from low complexity to high complexity. The best alternative may depend on the level of complexity.

**High Complexity: Workflows in Code**

For high complexity problems, we've found that in order to achieve a certain level of reliability the systems are not just pure agents, but rather involve some aspect of a workflow. These high complexity problems often require complex workflows. In these scenarios, where you want lots of branching, parallelism and modularity, code is the best option ([LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) is designed for this).

Traditionally this would mean that these types of problems just aren’t actually solvable by a non-technical builder. As the cost of code generation goes to zero, however, we expect that more and builders will find themselves capable of building these solutions.

**Low Complexity: No-Code Agents**

For lower complexity use cases, I would assert that simple agents (prompt + tools) are getting reliably good enough to solve these use cases. Building these agents in a no-code way should be simpler than building a workflow in a no-code way.

As models get better and better, I would expect the ceiling of the type of problems these agents can solve to get higher and higher.

## The squeeze

The issue with no code workflow builders are that I think they are getting squeezed from both directions.

Complexity Level
Best Solution

Low
No-Code Agent

Medium
No-Code Workflow

High
Workflow in Code

I think agents (prompt + tools) should be strictly easier to create in a no-code way than workflows. I expect models, agent harnesses, and our interfaces for creating, modifying, and *teaching* these agents to get better. This means that these agents will be *reliably good* at more and more tasks.

In the other direction, visual workflow builders become unmanageable for a certain level of complexity. The only real alternative to that is code. Writing code has historically been limited to a small set of people, with the barrier to entry being pretty high. As models get better and better at code generation, and the cost of code generation goes to zero, I expect the decision to go to code becomes easier and easier.

## The interesting problems

To be very clear - there are companies that have done a fantastic job at democratizing LLM powered workflow builders (n8n, Flowise, LangFlow, Gumloop, etc). Many of them have found product-market fit - they solve a real problem that exists today and empower non-technical users to build fantastic things.

I do not think the world needs yet another workflow builder. Rather, I think the interesting problems to solve next are:

- How can we make it easier to create *reliably good* agents in a no-code way. These should be agents! Not low code workflows.
- How can we make code generation models better at writing LLM powered workflows/agents

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)