---
title: "How AppFolio transformed property management workflows with Realm-X, built using LangGraph and LangSmith"
author: "LangChain Accounts"
date: "2024-12-16"
url: "https://www.langchain.com/blog/customers-appfolio"
---

Case StudiesLangGraphLangSmith

# How AppFolio transformed property management workflows with Realm-X, built using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf98b662c4aeedd72b241d_Appfolio-case-study.webp)AppFolio, the technology leader powering the future of the real estate industry, has released **Realm-X Assistant**, an AI-powered copilot designed to improve the efficiency of property managers’ day-to-day work. Realm-X is embedded generative AI that provides intelligent, real-time assistance by combining the latest foundation models with industry-specific context. Realm-X provides a conversational interface that helps users understand the state of their business, get help, and execute actions in bulk – whether it’s querying information, sending messages, or scheduling actions related to residents, vendors, units, bills, or work orders and many more. Early users have reported **saving over 10 hours a week **in completing their to-do list.

While designing Realm-X, AppFolio realized that they needed a better natural language interface to help property managers engage with the platform and simplify operational processes. The team turned to LangChain, LangGraph, and LangSmith to improve their execution flow and add visibility into how users were interacting with Realm-X.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf994f53a5cf6e64ada3e5_gif11-ezgif.com-optimize.gif)Realm-X assistant interface

## **Choosing LangGraph for flexibility and control**

Realm-X Assistant was initially built using LangChain for interoperability, making it easy to switch out model providers without changing any code. LangChain also made it easy to use tools and structured outputs when making requests with their tool calling agent.

As the Assistant evolved, AppFolio needed a way to handle even more complexity with their requests. Their team made a strategic transition from LangChain to LangGraph, which simplified response aggregation from different nodes to display to the user.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2557c432b84a72a1f7_AD_4nXcXpkZ-qSdAoCig0t3UeHQqscmlgopH_8sAJQtYbq7tK01-O6xgNDP_KIIv4MEaV_871n_8Y8aoMBirGcq9xhj2qIqMwVBYXS1goOneI6SA7sX2MjLtPGOB4CQl2XJo4k-DAGku.png)Realm-X architecture with LangGraph

‍

After switching to LangGraph, the AppFolio team could clearly see the execution flow of the Realm-X Assistant, which allowed them to design workflows that could reason before acting. By parallelizing branch execution, AppFolio has also been able to reduce latency and code complexity.  

One major benefit of LangGraph has been its ability to run independent code branches in parallel. While determining relevant actions, it simultaneously calculates fallbacks and runs a question-answering bot over help pages. This allows Realm-X to offer related suggestions which enhances the user experience, while keeping latency at a minimum.

## **Leveraging LangSmith to monitor and pinpoint issues in production**

To add a layer of visibility into their production traffic, AppFolio used LangSmith to facilitate debugging during development and gain more insights into user interactions. In production, the AppFolio team keeps a close eye on real-time feedback charts in LangSmith — tracking error rates, costs, and latency to keep everything on course. The team also added in automatic triggers to collect feedback when users submit an action drafted by Realm-X.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2457c432b84a72a1a0_image--44--1.png)

‍

In addition, automatic feedback is generated based on LLM or heuristic evaluators to continuously monitor system health.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2457c432b84a72a1f1_AD_4nXeYmTKItwBy4s0OyZHUlZpXluB2YWppUJhSWuFLzcxvMqrjnggbVLXHMm7G4SskYJMevdj24vOnKi6wLd1RZcimb9Ft4NoSiYVm4yEmc8cR90C8ZKxWFfrJoFXNCxITjk8hOnn8EQ.png)

‍

LangSmith’s tracing also makes it easy for AppFolio to pinpoint issues when they occur. During development, engineers rely on comparison views and the LangSmith playground to iterate on workflows, ensuring they&#x27;re battle-tested before deployment. Traces are also shareable across the team, streamlining the process of collaborating across stakeholders.

## **Iterating on prompts to improve system performance **

One key innovation that LangSmith supports in AppFolio’s system is dynamic few-shot prompting — which involves dynamically pulling relevant examples to deliver more personalized and accurate responses to Realm-X users. With LangSmith, the AppFolio team has been able to quickly identify whether wrong samples were used or if a relevant sample was missing or poorly formatted, ultimately helping optimize the examples pulled for a given query.

The comparison view in LangSmith was particularly useful for identifying subtle differences in how prompts were constructed, helping AppFolio ensure precise outputs. The LangSmith Playground also enabled the team to rapidly iterate on prompts, base models, or tool descriptions with modifying the underlying code – shortening the feedback cycle between stakeholders.

Dynamic few-shot prompting has been crucial in improving the performance of specific Realm-X features like its text-to-data functionality, where **performance significantly increased from ~40% to ~80%. **This showcases the impact of tailored examples in improving system accuracy. AppFolio has also maintained high performance as they’ve increased the number of actions and data models that users can query in Realm-X.

## **LLM evaluations for continuous improvement**

AppFolio prioritizes user experience and feedback in its testing and evaluation process. Every step in the Realm-X workflow— from individual actions to end-to-end executions— is rigorously tested using custom evaluators and LangSmith’s tools.

To ensure quality, AppFolio maintains a central repository of sample cases containing message history, metadata, and ideal outputs. These can be used as evals, unit tests, or examples. Evals are run in CI, with results tracked and integrated into PRs. To avoid regressions, code changes merge only when all unit tests pass and eval thresholds are met.

LangGraph also helps streamline complex workflows like text-to-data processing by organizing intricate if-statement logic into clear, flexible code paths. This, combined with rigorous testing, ensures that Realm-X Assistant produces accurate and reliable responses for property managers.

## **The path forward for AppFolio**

As AppFolio continues to innovate with the Realm-X Assistant, the focus remains on enhancing user-centric features and optimizing performance. As an early LangSmith user, AppFolio seamlessly integrated LangGraph with LangSmith’s robust monitoring, which helped Realm-X Assistant aggregate responses from multiple system parts to ensure clear, actionable user outputs.

Looking ahead, AppFolio is expanding Realm-X to further improve overall performance and reliability by using LangGraph for state management and self-validation loops. By combining these tools with their commitment to innovation, AppFolio continues to empower property managers everywhere to succeed.

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