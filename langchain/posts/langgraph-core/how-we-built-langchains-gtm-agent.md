---
title: "How we built LangChain’s GTM Agent"
author: "LangChain Accounts"
date: "2026-03-09"
url: "https://www.langchain.com/blog/how-we-built-langchains-gtm-agent"
---

Tutorials &amp; How-Tos

# How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)11min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)*By Vishnu Suresh and Jess Ou*

Every outbound at LangChain used to start the same way: a rep toggling between tabs. Salesforce for the account record, Gong for call history, LinkedIn for the contact, the company website for context. Fifteen minutes of research before a single word was written, and no easy way to know if a teammate had already reached out yesterday. Inbound follow-up used to mean manually dropping the same message into Apollo for every new contact.

We built a GTM agent that runs the process end-to-end. It triggers on new Salesforce leads, checks whether we should reach out, gathers context (including meeting history), and sends a Slack draft (with reasoning + sources) for the rep to approve. We built it on [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com) because this is a long-running, multi-step process that has to orchestrate multiple tools and large amounts of data reliably.

## **Key results**

- Lead-to-qualified-opportunity conversion rate up 250% from December 2025 to March 2026, driving 3x more pipeline dollars in the same period
- Since December, reps have increased their follow up with lower intent leads by 97% and higher intent leads by 18%
- Sales reps reclaimed 40 hours per month each, totaling 1,320 hours across the team
- 50% daily and 86% weekly active usage for sales team members

**Team love**

The GTM agent started as an SDR agent and then became used by the broader GTM team.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d079f4_data-src-image-bd0d930c-3f79-45ec-a18f-7f61dcee8f4f.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d079fa_data-src-image-8135b29f-2698-4512-b56f-7dc099c75bc9.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a03_data-src-image-4474bd1f-1954-4ea6-81e6-1ff770264f37.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d079fd_data-src-image-c5528a22-ecdd-4d21-a90d-1a4e869bd568.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a00_data-src-image-5729db30-b848-48a9-b3aa-fcc0745c3206.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d079f7_data-src-image-4472e2ac-9cd2-48ec-a53b-cb2d8e84e8fa.png)

## **Constraints &amp; success criteria**

Before writing any code, we defined what the agent actually needed to do.

We had two goals: reduce the time reps spend researching and drafting per lead, and improve conversion on marketing-generated inbound. Outbound research and drafting is systematic enough to automate, but only if the system is safe, auditable, and improves with use.

#### **Non-negotiables**

- **Human-in-the-loop:** Nothing is sent without an explicit rep review and approval. A single poorly timed email can undo months of relationship-building.
- **Contact history knowledge:** The agent needed to check whether a rep or teammate had already reached out before drafting anything.

#### **Core capabilities**

- **Relationship-aware personalization:** The draft should reflect the current state of the account (customer vs. warm prospect vs. cold), and not treat every lead the same way.
- **Explainability:** Reps should be able to see key inputs and understand why the agent chose a particular angle so they could refine it and provide feedback.
- **Learning loop:** The agent should learn from rep edits over time so drafts improve without anyone manually updating prompts.

#### **Measurement**

Every rep action (send, edit, cancel) is logged to [LangSmith](https://www.langchain.com/langsmith-platform?ref=blog.langchain.com) and attached to the underlying trace so we can evaluate quality, catch regressions, and quantify what’s working.

#### **Scope expansion: account intelligence**

Beyond one-off drafts, we also wanted the agent to proactively surface account-level signals like deal risks, expansion opportunities, and competitive moves, so reps know where to focus each week.

## **What we built**

The GTM agent does two things: (1) it researches leads and writes personalized email drafts, and (2) it aggregates account-level signals across web activity, developer ecosystems, product usage, and marketing touchpoints to show reps where to focus. By tying that intent data back to a rep’s accounts, it surfaces meaningful activity, flags deal risks and competitive moves, and clarifies who is ideal to reach out to next.

We connected the agent to the following data sources:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a06_gtm-agent-diagram-1--5-.png)

### Inbound lead processing

When a new lead shows up in Salesforce, the agent takes over immediately. The first thing it does is look for reasons not to send anything. If someone just filed a support ticket, or if a teammate already reached out earlier in the week, sending an automated email would be a mistake. The agent is programmed to be cautious.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a16_Group-1--3-.png)

Once it clears those checks, it does the same research a rep used to do manually: pulls the full Salesforce record, reads through Gong transcripts, checks the prospect&#x27;s LinkedIn profile. If there isn&#x27;t much internal history, it goes to the web with Exa to understand what the company is doing with AI right now.

How it writes the email draft depends on the state of the relationship. The agent follows a defined outbound [skill](https://docs.langchain.com/oss/python/deepagents/skills?ref=blog.langchain.com), a playbook it loads before drafting. The skill is designed to cover both warm and cold cases. An existing customer gets something different than a warm prospect, who gets something different than a cold contact. For cold outreach, the agent keeps it brief and research-backed, following a playbook we&#x27;ve defined in the skill.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d079f1_data-src-image-07e8ab2a-6b27-4016-a06e-a3cbf2c00915.png)

The rep sees the finished draft in a Slack DM with buttons to send, edit, or cancel. They can also see the agent&#x27;s reasoning, so it&#x27;s clear why it took a particular angle. If they send it, the agent queues up a set of follow-up emails to optionally enroll the prospect in.

As we&#x27;ve refined the agent, we added a 48-hour SLA for silver leads: if a rep hasn&#x27;t approved or declined the draft within that window, it sends automatically. This has meaningfully increased our follow-up rate for leads that would otherwise slip through without a response.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a2f_lead-processing-engine--3--1--1-.png)

### Account intelligence

As our team scaled, reps started owning anywhere from 50 to over 100 accounts each. At that volume, it&#x27;s easy for things to go quiet or for expansion opportunities to slip through.

Every Monday morning, the agent pulls data from Salesforce and BigQuery. It then checks the outside world for funding rounds, product launches, and new AI initiatives. We tailored the reports for two audiences: our sales team and our deployed engineering team, since they care about different data points.

For sales, the agent aggregates signals across product usage, developer ecosystems, web activity, hiring trends, and company news to surface expansion opportunities. It flags executive moves, spikes in package installations, and whether a company is actively hiring AI engineers or building agentic systems – which is a strong signal they&#x27;re ready to expand. It also identifies potential good fits when we launch new features, matching accounts whose recent activity aligns well with the new features. And because knowing an account is active isn&#x27;t enough on its own, it surfaces which individuals are most engaged and suggests who to reach out to next.

For deployed engineers, the focus shifts to account health. The agent pulls product usage from BigQuery, highlights from recent customer calls, upcoming renewal dates, and cases where a customer is close to running out of credits. It also surfaces open questions and unresolved threads from recent calls. The goal is to flag what actually needs a person to step in, so the team isn&#x27;t spending Sunday evenings digging through dashboards.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a2c_account-intelligence-engine--1--1--1-.png)

## **How we built it**

The agent needed to pull from multiple sources, reason across them, and produce a personalized output. This is more than a simple LLM call can handle reliably.

We chose Deep Agents for the multi-step orchestration because the inputs are inherently spiky: meeting data, CRM history, and web research vary a lot in size and structure. With Deep Agents, large tool results get offloaded into a virtual filesystem automatically, so we didn&#x27;t have to build our own truncation and retrieval layer. We also used the harness&#x27;s native planning tooling to enforce a consistent checklist (do-not-send checks → research → draft → rationale → follow-ups), which made runs easier to debug and reduced agent wandering.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a0c_deep-agents-diagram-1--2-.png)

We connected the agent to [LangSmith](https://www.langchain.com/langsmith/observability?ref=blog.langchain.com) so we could understand how sales reps were actually using it and measure whether the agent was improving over time. That meant setting up evaluations from the start rather than retrofitting them later, which turned out to be critical for catching regressions when we iterated on prompts or swapped model versions.

## **Agent patterns**

Moving our GTM agent to production surfaced two problems we had to solve: how to make the agent learn from the people using it, and how to keep runs efficient at scale.

### Memory

When a rep edits a draft in Slack, the system compares the original against the revised version. If the changes are substantive, an LLM analyzes the diff and extracts structured style observations: what changed, what it implies about the rep&#x27;s preferences, and an optional quoted example. Those observations are stored in PostgreSQL, keyed per rep, and every future run reads them before drafting.

Each rep has stylistic preferences around tone and brevity. The feedback loop is automatic. Every edit teaches the agent, and the next draft reflects it. A weekly cron compacts these memories to keep them from getting bloated over time.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a09_memory-loop-diagram--6--1--1-.png)

### Subagent delegation

Account intelligence runs through compiled subagents: lightweight agents with constrained tool sets and structured output schemas that act as contracts with the main agent. The sales research subagent has access to Apollo, Exa, and BigQuery, and returns structured prospect and market context. The deployed engineer subagent uses Salesforce, Gong, and support tools to return usage trends, open tickets, and expansion signals.

The parent agent spawns one subagent per account, keeping tools isolated and outputs predictable. Because subagents run independently, we can execute them in parallel. [LangSmith Deployment](https://www.langchain.com/langsmith/deployment?ref=blog.langchain.com) handles horizontal scaling and durable execution, so the system stays reliable as volume grows.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a1c_account-intelligence-diagram--1--1--1-.png)

## **Evals and feedback**

Before writing any production code for a new workflow, we define what success looks like in [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com). We started with a small library of representative scenarios grounded in the situations our reps actually face, used those to build the initial agent or feature, and made sure the fundamentals work before expanding.

Once things were functional, we broadened the evaluation set in LangSmith to cover harder cases: a researcher deep in agentic AI or NLP, an existing customer we&#x27;re trying to re-engage, accounts with prior Gong transcripts, verticals with heavy jargon like healthcare. Everything runs through a test harness that mocks our external APIs so we can observe behavior in a controlled environment before it touches real data.

We evaluate on two levels. First, rule-based assertions check the basics: right tools, right order, no duplicate drafts. Second, an [LLM judge](https://www.langchain.com/articles/llm-as-a-judge?ref=blog.langchain.com) scores tone, word count, and formatting. Both run as part of a full eval suite in CI, and we treat any unexplained drift in agent behavior as a bug worth investigating.

But evals only tell part of the story. What actually matters is how reps use the drafts day to day. We track every Slack action (send, edit, cancel) and attach it directly to the trace in LangSmith. Over time, this lets us correlate writing patterns with real outcomes: which styles drive opens, which subject lines get replies. When something holds across enough reps, we codify it into the agent&#x27;s default behavior.

The LangSmith eval suite and the rep feedback loop reinforce each other. One catches regressions, the other drives improvement.

## **Adoption beyond the sales team**

The GTM agent started as an [ambient agent](https://blog.langchain.com/introducing-ambient-agents/), running as a background process. A lead appears in Salesforce, the agent runs, a draft lands in the rep&#x27;s Slack. No trigger, no manual work.

We later built a conversational Slack interface as a side experiment, mostly to give SDRs a way to interact with the agent directly. What we didn&#x27;t expect was how quickly it spread to the rest of the company. Because the agent was already connected to Salesforce, Gong, BigQuery, and Gmail, people found uses we hadn&#x27;t designed for. Engineers checked product usage without writing SQL. Customer success pulled support history before renewal calls. Account executives summarized Gong transcripts before meetings.

We didn&#x27;t build any of those workflows intentionally. The agent had the access, and people found the path of least resistance. Talking to the bot was easier than opening six different tabs.

We&#x27;ll cover how other teams are using the GTM agent in a follow-up post.

## **Learnings**

A few things we&#x27;d tell someone starting from scratch:

- **Start with a definition of success, not code. **Before we write any production code for a new workflow, we define what good looks like and build a small scenario library around it. That set expands as the agent matures. By the time something ships, we have an eval test suite that catches regressions, flags drift, and runs in CI automatically.
- **Human-in-the-loop goes beyond safety.** It turned out to be a data collection mechanism. Every rep action (send, edit, cancel) became a signal we could learn from. The memory system and feedback loop work because reps are in the flow.
- **Connect the agent to your systems of record from the start.** The organic adoption across the company happened because the agent already had access to the data people needed. We didn&#x27;t plan for engineers or customer success to use it, but that usage spread because the access was already there.
- **Long-running workflows need the right infrastructure.** This agent required much more than a simple LLM call with a tool or two. It needed to pull from multiple sources, reason across them, run subagents in parallel, and maintain state across turns. Picking an agent harness, Deep Agents, built for that kind of orchestration saved us from rebuilding infrastructure from scratch.
- **We&#x27;re still early.** The GTM agent handles a real workflow today, but the feedback loops we&#x27;ve built – including memory, evals, and rep actions tied to traces – are what will make it meaningfully better over the next six months.

## **And it’s an active member in Slack!**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9bbe7ec0692a2d07a19_data-src-image-0c420a8f-051d-4256-98ad-7a751c9f063c.png)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa69431a71bcb2864063_Agent-Auth.png)Deep AgentsTutorials &amp; How-Tos

#### Securing your agents with authentication and authorization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 13, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)6min[](/blog/agent-authorization-explainer)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)