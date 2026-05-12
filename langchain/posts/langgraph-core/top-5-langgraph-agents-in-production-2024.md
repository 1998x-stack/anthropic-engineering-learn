---
title: "Top 5 LangGraph Agents in Production 2024"
author: "LangChain Accounts"
date: "2024-12-31"
url: "https://www.langchain.com/blog/top-5-langgraph-agents-in-production-2024"
---

LangGraphDeployment

# Top 5 LangGraph Agents in Production 2024

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 31, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae1957c432b84a729afb_all.png)2024 was the year that agents started to work in production. Not the wide-ranging, fully autonomous agents that people imagined with [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT?ref=blog.langchain.com). But more vertical, narrowly scoped, highly controllable agents with custom [cognitive architectures](https://blog.langchain.com/what-is-a-cognitive-architecture/). It&#x27;s still not easy to build these agents - but it&#x27;s entirely possible.

We launched [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) in early 2024 as a new take on an agentic framework. Incorporating lessons learned from LangChain, we made LangGraph very low level, controllable agentic framework. No hidden prompts, no obfuscated &quot;[cognitive architecture](https://blog.langchain.com/what-is-a-cognitive-architecture/)&quot;. Soon after it&#x27;s launch, we saw LangGraph become the go-to default framework for agents.

As the year closes, we wanted to highlight some of our favorite stories of companies building agents with LangGraph. As mentioned before, it&#x27;s still hard to build agents, but these companies have figured out how. They&#x27;ve shared their lessons learned in various forms - blogs, case studies, talks, fireside chats. We hope that by amplifying their stories, their lessons learned, it enables every more agents to be built in 2025.

## Honorable mentions:

- [Unify](https://blog.langchain.com/unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith/): An agent for GTM account qualification, featuring o1 as a planning agent
- [OpenRecovery](https://blog.langchain.com/customers-openrecovery/): An innovative and forward-looking application, especially with respect to memory
- [Rexera](https://blog.langchain.com/customers-rexera/): Great example of &quot;single agent -&gt; multi agent but uncontrollable (CrewAI) -&gt; controllable multi agent (LangGraph)&quot; journey that we see many user go through
- [Komodo Health](https://www.komodohealth.com/perspectives/new-gen-ai-assistant-empowers-the-enterprise/?ref=blog.langchain.com): Exciting to see agents working in highly-regulated domains like healthcare
- [Airtop](https://blog.langchain.com/customers-airtop/): Web agents are a big area, so it&#x27;s great to see them for browser automation
- [Tradestack](https://blog.langchain.com/customers-tradestack/): The first public-facing agent launched on LangGraph platform
- [Athena Intelligence](https://blog.langchain.com/customers-athena-intelligence/): One of the most advanced research agent platforms we know of
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher/blob/master/docs/blog/2024-05-19-gptr-langgraph/index.md?ref=blog.langchain.com): The most advanced open-source research assistant

## #5: Uber

At DPE, Uber talked about how they formed a dedicated Developer Platform AI team, and how they adopted LangGraph as a part of that. Especially interesting is how they are tackling large-scale code migrations with agentic systems

We like this example because it shows that while general coding agents are undoubtably useful, there is also a large amount of value to be gained from building some internal coding tools yourself, which perform workflows that only really you know how to do best.

- [DPE session video](https://dpe.org/sessions/ty-smith-adam-huda/this-year-in-ubers-ai-driven-developer-productivity-revolution/?ref=blog.langchain.com)

## #4: AppFolio

AppFolio&#x27;s AI-powered copilot Realm-X has saved property managers over 10 hours per week. Realm-X provides a conversational interface that helps users understand the state of their business, get help, and execute actions in bulk – whether it’s querying information, sending messages, or scheduling actions related to residents, vendors, units, bills, or work orders and many more

On their journey, they needed a controllable agent architecture to make this a reality — and so they chose LangGraph

- [Case study](https://blog.langchain.com/customers-appfolio/)

## #3: LinkedIn

One of the big use cases for LLMs is in making data more accessible to everyone. LinkedIn recently rolled out SQL Bot, an AI-powered assistant internally

This internal tool transforms natural language questions into SQL: it finds the right tables, writes queries, fixes errors, and enables employees across functions to independently access the data insights they need under the appropriate permissions.

Behind the scenes, SQL Bot is a multi-agent system built on top of LangChain and LangGraph.

- [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics?ref=blog.langchain.com)

## #2: Elastic

Elastic was one of the first companies in my mind to launch an AI &quot;agent&quot;. We covered their AI assistant in late January of 2024 - right at the start of the year. Back then it was using LangChain, but as they added more features, they migrated to LangGraph.

- [Initial case study](https://blog.langchain.com/langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant/)
- [Follow up blog](https://www.elastic.co/blog/building-automatic-import-attack-discovery-langchain?ref=blog.langchain.com)

Excited to see the continued development of AI assistant!

## #1: Replit

Replit released their agent this fall to pretty widespread adoption. When we&#x27;ve talked with them about the agent they&#x27;ve emphasized human-in-the-loop and multi-agent setup — both things we think will be key for agents in the future.

We&#x27;ve chatted with them a few times about Replit Agent:

- [Fireside Chat](https://www.youtube.com/watch?v=ViykMqljjxU&amp;ref=blog.langchain.com)
- [Case study](https://blog.langchain.com/customers-replit/)
- [Breakout Agents](https://www.langchain.com/breakoutagents/replit?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f4795_Nullframe-Moda.png)Case StudiesDeep AgentsDeployment

#### How Moda Builds Production-Grade AI Design Agents with Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 24, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)6min[](/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92becc1b0764b5d200f1_agent-identity-banner.png)Harrison&#x27;s In the LoopDeploymentAgent Architecture

#### Two different types of agent authorization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMarch 23, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/two-different-types-of-agent-authorization)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)