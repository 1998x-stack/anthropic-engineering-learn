---
title: "How Harmonic built an investment agent with LangGraph and LangSmith— so VCs can focus on founders"
author: "LangChain Accounts"
date: "2025-04-13"
url: "https://www.langchain.com/blog/customers-harmonic"
---

Case StudiesLangGraphLangSmith

# How Harmonic built an investment agent with LangGraph and LangSmith— so VCs can focus on founders

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 13, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad06d2a13d9d604fd82b_Harmonic-case-study.png)Harmonic is the startup discovery engine, tracking company formation and growth while providing valuable insights and workflow tools to venture capitalists (VCs). By aggregating vast amounts of public data and private data collected through partnerships with venture ecosystem players, Harmonic enables users to discover startups based on various criteria, enhancing their sourcing efforts. Using LangGraph and LangSmith, they’ve been able to move several steps further down the investment pipeline. With automatic market maps, research reports, and conversational interactions, VCs can now leverage Hamonic to pick and win the best deals in addition to sourcing.

## **Problem: Discovering the most exciting startups **

Navigating the complex landscape of early-stage startups is challenging for VCs and companies looking to connect with emerging businesses.  Historically, Harmonic has had an enormous search index, with a powerful search building UI.  For users, combining filters across hundreds of fields to find startups that met their interests was time-consuming at best, and prevented them from finding their best targets at worst.

Harmonic saw the need to enable far simpler and more effective search. By implementing natural language search and refinement capabilities on top of their extensive data, they aimed to significantly reduce the time it took for users to find the best-fit startups for their investment thesis.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad06d2a13d9d604fd83f_Harmonic-evolution%402x.jpeg)

# **LangGraph Studio for debugging agents &amp; modular workflow**

The Harmonic team chose to build with [LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.com) due to its ecosystem approach. This allowed for a unified stack so Harmonic could host all their prompts in LangSmith, invoke their target models with LangChain, and build composable workflows in LangGraph with nodes directly linking to execution traces.

LangGraph Studio proved to be a game-changer for Harmonic&#x27;s development process. The visual studio allowed engineers to track state, and directly link to any invoked LLMs in its exact invoked state, across every node in their agent workflows, significantly reducing debugging time.

> As CEO Max Ruderman notes: *&quot;This UI is invaluable for debugging—instead of rerunning every node, we can directly inspect graph state at any point, make changes, re-run from that point, and observe the difference. Or open up that execution in Playground, with all the context from execution time already there so you can instantly experiment with different models or instructions.&quot;*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad07d2a13d9d604fd852_AD_4nXeUivU9g0SxgMwC59I8aKAJDGTQMc77sIFhXOm4gloeeyW17uteM8N4_VxdVMTf_wys4wmStv_hX-5-gAjnPm9rrq1tkYvApzl2dp2xh5yrcMW7aRNdjLrqgJat390qtap9zmN4qA.png)

The modular framework of LangGraph empowered Harmonic to quickly bring agentic workflows to other parts of their product.  For example, because standalone workflows were modularized into subgraphs, they were able to bring a “research agent” (which was otherwise a subcomponent of a more complex workflow) to every company profile in their platform with almost no incremental backend work. That saves investors hours on screening, evaluation, and diligence, allowing them to show up prepared to every founder meeting.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad07d2a13d9d604fd85a_AD_4nXdCNnmuAQa9RyRgeXKZ7bUOIWS2dZHSGM9Dyq33-jA8uQyA_qwv4muYe-bskuUXHPQ_tmisRE7dyzVyxEnntvuGQXYeCxVJMJE3leMHp4CwOGT0U7yhpL0nzmwXG-_t0BwEG54C.jpeg)

By using LLMs to combine Harmonic’s millions of startup data points with live web data, Harmonic hoped to supercharge the insights and growth signals they could offer for early stage companies. But before LangGraph, building a reliable pipeline for real-time research on startup talent flow, market mapping, and media activity proved to be a tedious feat. Without a framework for composable development and graph visualization, tuning runs was a slow, iterative process of trial-and-error. Switching to LangGraph helped the team gain confidence that multiple engineers could collaborate on building these workflows quickly without introducing regressions.

Harmonic also leveraged LangGraph&#x27;s capabilities to rapidly develop subgraphs for refining user intent and structuring search queries. This allowed them to create a sophisticated search agent capable of executing complex queries like: *&quot;Show me AI companies in SF or NY that have raised funding in the last year from top investors and that have a connection to someone on my team, but no one on the team has been in touch with them in the last year.&quot;*

Now, investors can simply describe what they’re looking for—whether it’s a problem space, industry, a product that should exist, or a particular founder background—and Harmonic translates their natural language queries into precise, actionable search results.

# **LangSmith for evaluations &amp; collaborative prompt iteration **

With [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com), the Harmonic team could track every model invocation with seamless integration into a playground environment. This gave the team visibility into their model performance and user interactions, something they had struggled to achieve with previous disparate systems.

A key feature that attracted Harmonic to LangSmith was its robust prompt versioning system. The Harmonic team has a collaborative approach to prompt engineering, with one engineer handling more of the model writing and prompt tuning, and others coming in to collaborate on prompt refinements. This collaborative environment extended to their fine-tuning efforts for custom models, where LangSmith&#x27;s tracking capabilities provided essential data for optimization.

LangSmith&#x27;s integration with LangGraph created a powerful development ecosystem that accelerated Harmonic&#x27;s iteration cycles. The ability to link execution traces to specific prompts enabled developers to analyze performance patterns and make data-driven adjustments. When issues arose in their search agent, the team could quickly identify whether the problem stemmed from prompt design, model limitations, or graph structure.

Crucially, LangSmith made it incredibly easy to manage and view datasets and evaluations, which greatly sped up Harmonic’s development velocity. These evaluations ensured that any change to prompts or agent graph configurations could be tested against a suite of predefined metrics, whether at the level of individual nodes or the entire graph. This allowed the team to iterate rapidly and confidently, even as they frequently switched out underlying LLM models to keep pace with the latest advancements.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad07d2a13d9d604fd856_AD_4nXeRZ1G7GwUOh2gxwzUGmgba_wlgrUaRvWq-5u4n88TA6b6JeFz4KoFTYJHADL5wY5tm04TnMZmOL8Ze4JYodRv1SwznzoFU8YLVhqrVGjh8JVUbo425Tx941yBRCeD0WZC5QdOePA.png)

# **Impact &amp; Conclusion**

The implementation of LangChain&#x27;s LangSmith and LangGraph has significantly improved Harmonic&#x27;s search and research capabilities. Users reach their &quot;aha moment&quot; faster, with searches delivering more relevant results—especially for the most creative queries. Time to value dropped from hours to under a minute, and positive search outcomes **increased by 30%.**

Harmonic was also able to add new capabilities, increasing the leverage they bring users throughout the investing funnel by offering instant market-maps and the ability to conduct research that combines Harmonic’s unique data with synthesized insights from the public web, the user’s CRM data, and network. Now, leading investors can rely on Harmonic to find, pick, and win the best deals out there.

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