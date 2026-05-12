---
title: "Agent Toolkits"
author: "LangChain Accounts"
date: "2023-03-01"
url: "https://www.langchain.com/blog/agent-toolkits"
---

Agent ArchitectureLangChain

# Agent Toolkits

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 1, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb2593c7fbd0a6275f641_oIpwxeeSPy1cnwYpqJ1w_Dufer%2520Collateral%2520test.jpeg)Today, we&#x27;re announcing agent toolkits, a new abstraction that allows developers to create agents designed for a particular use-case (for example, interacting with a relational database or interacting with an OpenAPI spec). We hope to continue developing different toolkits that can enable agents to do amazing feats. Toolkits are supported in both [Python](https://github.com/hwchase17/langchain/tree/master/langchain/agents/agent_toolkits?ref=blog.langchain.com) and [TypeScript](https://github.com/hwchase17/langchainjs/tree/main/langchain/src/agents/agent_toolkits?ref=blog.langchain.com).

## Agents

Quick refresher: what do we mean by agents? And why use them?

By agents we mean a system that uses an LLM to decide what actions to take in a repeated manner, where future decisions are made based on observing the outcome of previous actions. This approach has several benefits. First, it allows combining the LLM with external sources of knowledge or computation (the tools themselves). Second, it allows iterative planning and action taking, useful for more complex tasks where there are a series of things to be done. Finally, it allows for error handling in a robust way, as an agent can observe if an action raised an error and try to correct it. These benefits are evident in the examples below.

## Toolkits

Toolkits allow you to logically group and initialize a set of tools that share a particular resource (such as a database connection or json object). They can be used to construct an agent for a specific use-case. Here are some examples of toolkits and agents created with them:

### SQLDatabaseAgent

This agent builds off of [SQLDatabaseChain](https://python.langchain.com/docs/modules/chains/popular/sqlite?ref=blog.langchain.com), and is able to answer general questions about the database, double check queries before executing them, and recover from errors.

Using the [`SQLDatabaseToolkit`](https://python.langchain.com/docs/modules/agents/toolkits/sql_database?ref=blog.langchain.com), the agent retrieves tables from the DB, picks relevant tables, gets their table information, creates and checks a query to answer the question, and repeat parts of this process when an error is encountered.

To see this in action, look at the example below. The agent is asked a question about the [Chinook database](https://github.com/lerocha/chinook-database?ref=blog.langchain.com); to do this, it asks for the list of tables, then the table metadata, then executes the query. It initially encounters an error caused by joining on a column that doesn&#x27;t exist. (See full [notebook](https://python.langchain.com/docs/modules/agents/toolkits/sql_database?ref=blog.langchain.com), TypeScript example [here](https://hwchase17.github.io/langchainjs/docs/modules/agents/agent_toolkits/sql?ref=blog.langchain.com)).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25a3c7fbd0a6275f64f_screenshot-2023-02-25-at-6.12.17-pm.png)

After double checking and rewriting the query, it is able to arrive at the final answer:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25a3c7fbd0a6275f64b_screenshot-2023-02-25-at-6.13.49-pm.png)

### OpenAPI Agent

This agent is able to interact with an OpenAPI spec and make a correct API request based on the information it has gathered from the spec.

In the below example, we are using the OpenAPI spec for the OpenAI API, which you can find [here](https://github.com/openai/openai-openapi/blob/master/openapi.yaml?ref=blog.langchain.com). Using the [`OpenAPIToolkit`](https://python.langchain.com/docs/modules/agents/toolkits/openapi?ref=blog.langchain.com), the agent is able to sift through the JSON representation of the spec (see JSON agent), find the required base URL, path, required parameters for  a `POST` request to the `/completions` endpoint, then make the request. (See full [notebook](https://python.langchain.com/docs/modules/agents/toolkits/openapi?ref=blog.langchain.com), TypeScript example [here](https://hwchase17.github.io/langchainjs/docs/modules/agents/agent_toolkits/openapi?ref=blog.langchain.com)).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25a3c7fbd0a6275f648_screenshot-2023-02-25-at-6.19.00-pm.png)

### Other agent toolkit examples:

- [JSON agent](https://python.langchain.com/docs/modules/agents/toolkits/json?ref=blog.langchain.com) - an agent capable of interacting with a large JSON blob.
- [Vectorstore agent](https://python.langchain.com/docs/modules/agents/toolkits/vectorstore?ref=blog.langchain.com) - an agent capable of interacting with vector stores.
- [Python agent](https://python.langchain.com/docs/modules/agents/toolkits/python?ref=blog.langchain.com) - an agent capable of producing and executing Python code.
- [Pandas DataFrame agent](https://python.langchain.com/docs/modules/agents/toolkits/pandas?ref=blog.langchain.com) - an agent capable of question-answering over Pandas dataframes, builds on top of the Python agent.
- [CSV agent](https://python.langchain.com/docs/modules/agents/toolkits/csv?ref=blog.langchain.com) - an agent capable of question answering over CSVs, builds on top of the Pandas DataFrame agent.

## Up Next

We&#x27;re just getting started with agent toolkits and plan on adding many more in the future. We believe that interacting with tools and utilities in an agentic manner opens up many exciting possibilities. If there are other use-cases you want to see, please reach out!

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