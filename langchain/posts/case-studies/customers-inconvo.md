---
title: "How Inconvo is improving customer-facing analytics with conversational AI built on LangGraph"
author: "LangChain Accounts"
date: "2025-03-19"
url: "https://www.langchain.com/blog/customers-inconvo"
---

Case Studies

# How Inconvo is improving customer-facing analytics with conversational AI built on LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 19, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadd857c432b84a726e15_Inconvo-case-study.png)[Inconvo](https://inconvo.ai/?ref=blog.langchain.com) is a YC S23 startup that simplifies data analysis for non-technical users. This case study will focus on how Inconvo utilizes [LangGraph](https://langchain.com/langgraph?ref=blog.langchain.com) and [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) to streamline their data querying process.

## **Problem: Overcoming the barrier for data analysis **

Inconvo addresses a common challenge faced by many non-technical users who struggle with traditional Business Intelligence (BI) workflows to extract simple insights from data. For example, a user of a SaaS application might find it cumbersome to navigate complex BI tools just to answer straightforward questions like &quot;How much product have I sold over the last two weeks?&quot; This inefficiency not only wastes time but also limits the ability of users to make data-driven decisions.

The need for a more intuitive solution became apparent as Inconvo sought to empower users to ask questions in natural language, thereby eliminating the need for technical expertise in data analysis. By providing a simple API, Inconvo aims to make it easy for developers to add conversational analytics to their applications.

## **Agent UX: API for conversational data analysis **

Inconvo&#x27;s agent interface provides users with multiple ways to visualize and interact with their data. When users submit natural language queries, the API returns JSON results in the following forms:

- Bar charts for comparing categorical data
- Line graphs for time-series analysis
- Tables for detailed data examination
- Text for simple answers

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadda57c432b84a726ec7_AD_4nXf5vDILU4HEjl98I5fLFpJwWK7Z5ARWsJggz46VjTb3iLEGyF-d2sDLFKLbg0bG9dBls42sHKdBLDif5GwT7ncdPFtcV3Gyb7SHYnWsZuRNsUsBWq0YHYjBTUNXOhV46iAHKZjFJA.png)

The API allows users to refine their queries conversationally. For example, after seeing initial results, a user can ask for a different visualization or request to filter the data further. This interactive experience makes complex data analysis accessible to non-technical users without requiring them to learn SQL or specialized BI tools.

## **Building a powerful query processing system with LangGraph**

[LangGraph](https://langchain.com/langgraph?ref=blog.langchain.com) plays a key role in Inconvo&#x27;s architecture and has enabled a multi-step workflow that efficiently processes user queries. When a user submits a question, LangGraph orchestrates the entire data retrieval process, starting with an introspection of the database to understand its schema. This allows Inconvo to configure which data is accessible and how it can be queried.

Inconvo’s architecture utilizes LangGraph to manage conditional workflows, where different operations can be executed based on the user&#x27;s input. This includes selecting tables, executing SQL queries, and returning structured outputs in various formats. By integrating with LangGraph, Inconvo can handle complex queries with multiple steps, ensuring that users receive accurate and relevant results quickly.

The cognitive architecture follows a deliberate reasoning pattern:

- Parse the user&#x27;s natural language query
- Map the query to relevant database tables and fields
- Generate appropriate SQL queries

## **Conclusion**

Inconvo&#x27;s use of LangGraph has transformed how non-technical users interact with their data, breaking down barriers to data analysis through natural language processing. By eliminating the need for specialized technical skills, Inconvo has democratized access to data insights, enabling users across various industries to make informed decisions quickly and efficiently. This case study demonstrates how innovative AI solutions can solve real-world problems and create more intuitive user experiences in the data analytics space.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)