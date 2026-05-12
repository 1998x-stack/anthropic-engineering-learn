---
title: "How Dataherald Makes Natural Language to SQL Easy"
author: "LangChain Accounts"
date: "2024-02-14"
url: "https://www.langchain.com/blog/dataherald"
---

Case StudiesLangSmithObservability &amp; Evals

# How Dataherald Makes Natural Language to SQL Easy

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 14, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02bb02f04cb69c54f9e_Screenshot-2024-02-06-at-4.43.40-PM.png)**Editor&#x27;s Note: we&#x27;re excited to feature this guest post from the **[**Dataherald**](https://www.dataherald.com/?ref=blog.langchain.com)** team. Text-to-SQL is a HUGE use case, and Dataherald is the open-source leader in the space. This is a great look behind the curtains to see what makes it tick.**

When ChatGPT came out in late 2022, everyone went over to see if AI could do their day to day work. Marketers wanted their blog posts written, college students their essays, and developers their helper functions. For those working with relational data, the test was to see how well these advanced LLMs could write SQL.

It turned out that while modern LLMs had become very good at writing *syntactically* correct SQL, the code they generated often was *semantically* incorrect. In fact, it soon became clear that LLMs are better at writing procedural code than SQL. This is because:

- Metadata and business definition are not stored in the relational database schema.
- LLMs do not do well when it comes to complex SQL requiring window functions, complex JOINs or temporal calculations. Furthermore on large schemas users will often run into context window issues
- To get best performance, you need to fine-tune the LLM to the dataset. Creating the training datasets for NL-to-SQL is hard.
- Assessing the accuracy of the AI generated SQL is extremely challenging.

At Dataherald, we set out to build an engine that would allow developers to deploy state of the art NL-to-SQL in their applications. We built it on LangChain, leveraging LangSmith for observability.

## How Dataherald works

Dataherald is an [open source](https://github.com/Dataherald/dataherald?ref=blog.langchain.com) NL-to-SQL engine which can also be accessed via a [hosted API](https://www.dataherald.com/news/introducing-dhai?ref=blog.langchain.com). Users can add business context, create training data and fine-tune LLMs to their schema. In the hosted version, users can monitor performance and configure the engine through a UI. However, the core part of the product are the two LangChain agents that do the NL to SQL translation.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02cb02f04cb69c54fdb_s6Fck1wSFleCMDVrXRLDqu2YplHeRzZm5frwrHQNLUDSYUq3cJwMbN5fhoON1fiL3xVVLZI6Kr5spoYbP1Z-MroVwrgpTCeLfvmz8Mvgzqxk55nI6_PKg2-s8vYo8qYAN1ZKbqs44CLCj9Tp7QBiFP8.png)Dataherald Admin Console Query List![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02cb02f04cb69c54fd4_N8BDfNuxHUighhysKqYz4TqEN2wuPAUu0HrJNEzuiBHax9UlxTLiD51sLwfN6RB79ec-gMAKXlfKINspIyHcNWhaJJQzaKlSicOkP9c89xy__iM90wZt0hIOwzVtHqbTZXSKN7nlXzkKGW5NRLdGK88.png)Dataherald Admin Console Database Instructions

## How the agents work

Dataherald has two LangChain agents: a RAG-only agent which relies on few-shot prompting and the more advanced agent which uses a fine-tuned LLM-as-a-tool.

### RAG agent:

The RAG agent is used for scenarios where the developer does not have access to a substantial set of sample Question&lt;&gt;SQL pairs (golden SQL) for fine-tuning or training the LLM. It connects to the database and extracts essential information for SQL generation, such as table schema, categorical values, table and column descriptions. It also then leverages the following tools:

- A schema-linking tool to identify relevant tables and columns
- A SQL execution tool that executes the generated SQL queries against the database to validate its correctness and recover from errors.
- Few-shot sample retriever tool to fetch golden SQL based on the similarity to the incoming prompt and use it for few shot prompting

Developers can further augment prompts with business-specific instructions that are injected into the prompts based on relevance

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02bb02f04cb69c54fcb_PfC5vRgowgs453i1sNDM_dResL1WWRwcTDrLBCkoqFBwliAw_ttsdH_wy6r8WqXLsYrUXVsAtcr-fj4IE94CFonuelGEpjR5R-TaLBg6eAI4RhUcR7Qqeup9X3_lCzjbM58jhYJGy3DJ9ZLT2mm4V6Y.png)

Developers often use this agent to create golden SQLs which can then be used to fine-tune an LLM for the more advanced model. The hosted version allows users to do modify SQL and add samples to the training data with a single click through the UI and code editor

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02cb02f04cb69c54fd1__d2nfgKkSDXbUYhXkWJjpWQB5TLvQ3OmuXghTzsJkmLBwzwGXXANiDt1Pn_h_autkWgxUGJWjpuNy-YDcHug7QewHkoJeKQOJL4R9eCz1zJj7Ws2hBRGjYvYrRgUvTkOQDggAO6scCFasQ9z3eiuLTs.png)

### Agent with LLM-as-a-tool:

Once there are more than 10 golden SQL per table, our recommendation is to fine-tune a model and use the more advanced agent, which can be done with a single API call. For this agent, the fine-tuned NL-to-SQL model serves as a tool itself. However, since the fine-tuned model does not possess all the business context, it is still deployed within an agent that is responsible for retrieving business context.

Similar to the RAG agent, this agent has direct access to the database and can execute the generated SQL queries, ensuring they accurately retrieve the necessary information to answer the question and doesn’t contain any syntax errors.

The diagram below shows how this agent works:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02bb02f04cb69c54fc6_I0BEsVWI6XJO5G6JLSlzpTzOfLv5VK_pACSRYQ0IksqQakQYOb4qqzIUdpEthlqzWqwldX8hiLv4uc_42vgDMAPK06MQqaoeRG6yEaOo1-PDZGz31jRhWo9iCR8jTbFIUrAimJO-saNORA4QgDdb0hw.png)

## Conclusion

Developers and data teams at companies ranging in size from startups to Fortune 500 companies use Dataherald today to power conversational interfaces for their customers and empower internal business users to self-serve from the data warehouse.

We are just getting started and we have a lot lined up for the next few months: a LangChain integration, increased support for open source LLMs, and allowing agents to ask follow up questions (human as a tool) are all items currently in development.

If you are tired of wrangling with prompts to get NL-to-SQL to work, try out [Dataherald](https://dataherald.com/?ref=blog.langchain.com).

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