---
title: "How DocentPro Built a Multi-Agent Travel Companion with LangGraph"
author: "LangChain Accounts"
date: "2025-04-29"
url: "https://www.langchain.com/blog/customers-docentpro"
---

Case StudiesLangGraphLangSmith

# How DocentPro Built a Multi-Agent Travel Companion with LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 29, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab890f5dd76f29a46669_DocentPro-Case-study.png)[DocentPro](https://docentpro.ai/?ref=blog.langchain.com) is building an AI travel platform that helps travelers figure out where to go, what to do, and how to plan.

People love using ChatGPT and Perplexity for trip research - and they’re great at surfacing ideas. But to DocentPro, travel isn’t just about a research – it’s about creating a streamlined experience from discovery to planning to booking. These tools often stop short. You still end up mapping routes, comparing ratings, scanning reviews, and bouncing between apps to make it all work.

To solve that, they built a modular multi-agent system using LangGraph and LangSmith, blending the creativity of LLMs with the precision of deterministic logic, and designing reusable agents that work across trip planning and real-time conversation.

## Building Modular Agents that Work Across the Stack

DocentPro broke down the travel planning agent into four domains: attractions, restaurants, hotels, and activities. Each of these is managed by its own agent, and each agent is designed to be modular and reusable. That means the Restaurant Research Agent, for example, isn&#x27;t just used in their trip planner to suggest meals for each day. The same agent is also called by their chat assistant when a user asks, &quot;Where’s a good place to eat nearby?&quot;

This approach helps the DocentPro team avoid duplicating logic, keep things consistent, and make their agents easier to test and improve. With LangGraph, each part of the system is composed as a clear, traceable node - and with LangSmith, they can debug and refine behavior step-by-step. DocentPro thinks of this as a small but important step toward more collaborative AI - where agents don’t just operate in isolation, but work together across different workflows.

## Balancing LLM Flexibility with Deterministic Control

While LLMs are great at coming up with interesting ideas - like suggesting popular local spots - they don’t always stick to reality. Furthermore, while LLMs are great at suggesting interesting places, especially well-known spots, they often build itineraries based solely on what they “know,” not how people actually move. The result? Plans that zigzag across the regions in a day without considering realistic routes.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8a0f5dd76f29a46673_docentpro---k-means.png)

That’s why DocentPro built guardrails into the system to keep outputs grounded. This involved:

- **K-Means clustering** to group points of interest by geography
- **Route reordering** to minimize unnecessary travel
- **Filtering** out hallucinated or closed places
- LLM-generated explanations for every recommendation

This hybrid approach helps DocentPro strike the right balance between helpful suggestions and practical plans that users can actually follow.

## Observability and Debugging with LangSmith

LangSmith has been essential in helping DocentPro make their system reliable. They use it to:

- Trace and monitor every LangGraph run
- Quickly inspect where things go wrong (or right)
- Understand how users are interacting with our agents
- Replay sessions to iterate faster and improve behavior

It’s especially helpful in a multi-agent system, where it’s easy to lose track of who’s doing what. With LangSmith, the DocentPro team always has visibility into the decision-making process.

### Adding support for Audio Guides in 12 Languages

One of the earlier features DocentPro built was an on-demand audio guide system for global attractions. They initially implemented it with a custom RAG pipeline - but as they added support for 12 languages and more locations, maintaining and scaling the system became painful.

As a result, DocentPro decided to port their architecture to LangGraph in just two days, using a map-reduce style workflow tailored for content generation. This means that:

- For each point of interest, they break it down into multiple topics (e.g. history, architecture, fun facts)
- Each topic is passed through a chain of agents: research ⇒ narrative generation(RAG) ⇒ translation ⇒ TTS(Text to Speech)
- Final outputs are then aggregated into structured, per-language audio playlists

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8a0f5dd76f29a4666f_Screenshot-2025-04-13-at-2.37.17-PM.jpeg)

LangSmith helped DocentPro trace and debug the early runs, and now the system scales globally with minimal overhead.

### The Result

DocentPro’s current system:

- Uses modular, domain-specific agents across trip planning and chat
- Combines deterministic algorithms with LLM-based reasoning
- Is fully traceable and improvable via LangSmith
- Powers AI itineraries and multilingual audio guides for travelers around the world

DocentPro is continuing to improve how their agents interact and how they bring structure to flexible travel - one itinerary at a time.

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