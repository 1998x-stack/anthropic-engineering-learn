---
title: "Pushing LangSmith to new limits with Replit Agent&#x27;s complex workflows"
author: "LangChain Accounts"
date: "2024-09-26"
url: "https://www.langchain.com/blog/customers-replit"
---

Case StudiesLangSmith

# Pushing LangSmith to new limits with Replit Agent&#x27;s complex workflows

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 26, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4b57c432b84a735887_Case-study---replit.png)[Replit](https://replit.com/?ref=blog.langchain.com) is at the forefront of AI innovation with its platform that simplifies writing, running, and collaborating on code for over 30+ million developers. They recently released Replit Agent, which immediately went viral due to the incredible applications people could easily create with this tool.

Behind the scenes, Replit Agent has a complex workflow which enables a highly custom agentic workflow with a high-degree of control and parallel execution. By using [LangSmith](http://langchain.com/langsmith?ref=blog.langchain.com), Replit gained deep visibility into their agent interactions to debug tricky issues.

The level of complexity required for Replit Agent also pushed the boundaries of LangSmith. The LangChain and Replit teams worked closely together to add functionality to LangSmith that would satisfy their [LLM observability](https://www.langchain.com/articles/llm-monitoring-observability) needs. Specifically, there were three main areas that we innovated on:

- Improved performance and scale on large traces
- Ability to search and filter within traces
- Thread view to enable human-in-the loop workflows

## **Improved performance and scale on large traces**

Most other LLMOps solutions monitor individual API requests to LLM providers, offering a limited view of single LLM calls. In contrast, LangSmith from day one has focused on tracing the entire execution flow of an LLM application to provide a more holistic context.

Tracing is important for agents due to their complex nature. It captures multiple LLM calls as well as other steps (retrieval, running code, etc). This gives you granular visibility into what’s happening, including at the inputs and outputs of each step, in order to understand the agent’s decision-making.

Replit Agent was a ripe example for advanced tracing needs. Their agentic tool goes beyond simply reviewing and writing code, but also performs a wider range of functions – including planning, creating dev environments, installing dependencies, and deploying applications for users.

As a result, Replit’s traces were very large - involving hundreds of steps. This posed significant challenges for ingesting data and displaying it in a visually meaningful way.

To address this, the LangChain team improved their ingestion to efficiently process and store large volumes of trace data. They also improved LangSmith’s frontend rendering to display long-running agent traces seamlessly.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4f03935dbc92df2468_replit-case-study-image.png)

## **Search and filter within traces to pinpoint issues**

LangSmith has always supported search **between** traces, which allows users to find a single trace among hundreds of thousands based on events or full text search. But as Replit Agent’s traces got longer and longer, the Replit team needed to search **within** traces for specific events (oftentimes issues reported by alpha testers). This required augmenting existing search capabilities.

In response, a new search pattern – searching within traces – was added to LangSmith. Instead of sifting and scrolling call-by-call within a large trace, users could now filter directly on a criteria they cared about (e.g. keywords in the inputs or outputs of a run). This greatly reduced Replit’s time needed to debug agent steps within a trace.

## **Thread view to enable human-in-the-loop workflows**

A key differentiator of Replit Agent was its emphasis on human-in-the-loop workflows. Replit Agent intends to be a tool where AI agents can collaborate effectively with human developers, who can come in and edit and correct agent trajectories as needed.

With separate agents to perform roles like managing, editing, and verifying generated code,  Replit’s agents interacted with users continuously - often over long periods with multiple turns of conversation. However, monitoring these conversational flows was often difficult, as each user session would generate disjoint traces.

To solve this, LangSmith’s thread view helped collate traces from multiple threads together that were related (i.e. from one conversation). This provided a logical view of all agent-user interactions across a multi-turn conversation, helping Replit better 1) find bottlenecks where users got stuck and 2) pinpoint areas where human intervention could be beneficial.

## **Conclusion**

Replit is pushing the frontier of AI agent monitoring using LangSmith’s powerful observability features. By reducing the effort of loading long, heavy traces, the Replit team has greatly sped up the process of building and scaling complex agents. With faster debugging, improved trace visibility, and better handling of parallel tasks, Replit is setting the standard for AI-driven development.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

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