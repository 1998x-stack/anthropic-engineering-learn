---
title: "Making Data Ingestion Production Ready: a LangChain-Powered Airbyte Destination"
author: "LangChain Accounts"
date: "2023-08-08"
url: "https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination"
---

Observability &amp; EvalsPartner

# Making Data Ingestion Production Ready: a LangChain-Powered Airbyte Destination

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 8, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d4adb40d0919236580_5-social--18.png)A big focus of ours over the past few months has been enabling teams to go from prototype to production. To take apps they developed in an hour and get them into a place where they can actually be reliably used. Arguably the biggest category of applications LangChain helps enable is retrieval based applications (where you connect LLMs to your own data). There are a few things that are needed to take retrieval based applications from prototype to production.

One component of that is everything related to the querying of the data. That’s why we launched [LangSmith](https://blog.langchain.com/announcing-langsmith/) - to help debug and monitor how LLMs interact with the user query as well as the retrieved documents. Another huge aspect is the querying algorithms and UX around that - which is why we’re pushing on things like [Conversational Retrieval Agents](https://blog.langchain.com/conversational-retrieval-agents/). (If you are interested in this part in particular, we’re doing a webinar on “[Advanced Retrieval](https://www.crowdcast.io/c/kqz7nl8nps42?ref=blog.langchain.com)” on August 9th). A third - and arguably the most important part - is the ingestion logic itself. When taking an application into production, you want the data it’s connecting to be refreshed on some schedule in a reliable and efficient way.

Our first stab at tackling this is another, deeper integration with Airbyte. The [previous Airbyte integration](https://python.langchain.com/docs/integrations/document_loaders/airbyte_json?ref=blog.langchain.com) showed how to use one of their sources as a Document Loader within LangChain. This integration goes the other direction, and adds a LangChain destination within Airbyte.

To read more about this integration, you can check out Airbyte’s release blog [here](https://airbyte.com/blog/airbyte-now-supports-vector-databases-powered-by-langchain?ref=blog.langchain.com). We will try not to repeat too much of that blog, but rather cover why we think this is an important step.

LangChain provides “sources” and “destinations” of our own - we have hundreds of document loaders and 50+ vectorstore/retriever integrations. But far from being replacements for one another, this is rather a mutually beneficial integration that provides a lot of benefits for the community.

First, Airbyte provides [hundreds more sources](https://docs.airbyte.com/integrations/?ref=blog.langchain.com), a robust orchestration logic, as well as [tooling](https://docs.airbyte.com/connector-development/connector-builder-ui/overview?ref=blog.langchain.com) to create more sources. Let’s focus on the orchestration logic. When you create a chatbot that has access to an index of your data, you don’t just want to index your data there once and forget about it. You want to reindex it on some schedule, so that it stays up to date. This type of data pipelines is exactly what Airbyte excels at and has been building.

Second, the ingestion process isn’t only about moving data from a source to a destination. There’s also some important, non-trivial and nuanced transformations that are necessary to enable effective retrieval. Two of the most important - text splitting and embedding.

Splitting text is important because you need to create chunks of data to put in the vectorstore. You want these chunks to be semantically meaningful by themselves - so that they make sense when retrieved. This is why it’s often a bit trickier than just splitting a text every 1000 characters. LangChain provides implementations of 15+ different ways to split text, powered by different algorithms and optimized for different text types (markdown vs Python code, etc). To assist in the exploration of what these different text splitters offer, we&#x27;ve [open-source](https://github.com/langchain-ai/text-split-explorer?ref=blog.langchain.com) and [hosted](https://langchain-text-splitter.streamlit.app/?ref=blog.langchain.com) a playground for easy exploration.

Embeddings are important to enable retrieval of those chunks, which is often done by comparing embeddings of a user query to embeddings of ingested documents. There are many different embedding providers and hosting platforms - and LangChain provides integrations with 50+ of them.

Overall, we’re really excited about this LangChain - Airbyte integration. It provides robust orchestration and scheduling for ingestion jobs while leveraging LangChain’s transformation logic and integrations. We also think there’s more features (and integrations) to add to make data ingestion production ready - keep on the lookout for more of those over the next few weeks.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)