---
title: "Implementing advanced RAG strategies with Neo4j"
author: "LangChain Accounts"
date: "2023-11-07"
url: "https://www.langchain.com/blog/implementing-advanced-retrieval-rag-strategies-with-neo4j"
---

LangChain

# Implementing advanced RAG strategies with Neo4j

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 7, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f02c87c962360cb552_Untitled-Diagram.drawio--13-.png)**Editor&#x27;s note: We&#x27;re excited to share this blogpost as it covers several of the advanced retrieval strategies we introduced in the past month, specifically a lot of the ones that rely on changing the ingestion step. A lot of these advanced retrieval strategies can be summarized as changing how indexing of documents is done to retain some concept of hierarchy. Neo4j is an exciting database to use for these tasks since it can represent these hierarchies as part of the graph. This also allows you to switch between indexing strategies pretty easily.**

[**Tomaz**](https://twitter.com/tb_tomaz?ref=blog.langchain.com)** has implemented a single LangChain template that contains four different RAG strategies. Check it out here:**

- [**Neo4j Advanced RAG Template**](https://github.com/langchain-ai/langchain/tree/v0.2/templates/neo4j-advanced-rag?ref=blog.langchain.com)

Retrieval-augmented generation applications seem to be the “Hello World” of AI applications. Nowadays, you can implement a “Chat with your PDF” application in only a couple of minutes due to the help of LLM framework libraries like LangChain.

“Chat with your PDF” applications typically rely on vector similarity search to retrieve relevant information, which are then fed to an LLM to generate a final answer that is returned to a user.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb56a_poJ-9QsO-AF2JOqrL9cfewhmykbAMOtbSr4J-5Tzf3_BTZE7eiUMsZpbmETUb6WfXzR-RDxf4yvs88sb-RPZzpsYxIbnjL1AgFf9ZPpNKQ5shZmJ90IPZNByKAH0ZgHRHppVnBgISaW-I8RkwqMd7Tw.png)Vector similarity search is used to retrieve relevant information.

Lately, it is becoming more and more obvious that naive vector similarity search might not be accurate enough for all use cases. For example, we have seen the introduction of [step-back approach to prompting](https://arxiv.org/abs/2310.06117?ref=blog.langchain.com), which emphasizes the importance of taking a step back from the immediate details of a task to focus on a higher-level abstraction.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb56e_TMku0mUGhLAEJEBmYyQ_tu22R_YHuwyEiyHCsLHQ53AHaKT7c4sIhi_8XjojhVAHLcxsqX6TjGsDlj4Gxlq5mXAwVZ6H7b4_w_n4wB-fHU_gHRszXbBl_hO9xStI9GMz3zpzDGIcmKgtWvBpl69-HCQ.png)Step-back prompting. Image from[ research paper](https://arxiv.org/abs/2310.06117?ref=blog.langchain.com) licensed under CC BY 4.0.

The step-back prompting technique is based on the observation that directly addressing intricate tasks can lead to errors, especially when there are numerous specifics to consider. Instead of plunging straight into the complexities, the model first prompts itself to ask a more generic question that encapsulates the core essence of the original query. By focusing on this broader concept or principle, it can retrieve more relevant and comprehensive facts. Once armed with this foundational knowledge, the model can then proceed to reason and deduce the answer to the specific task at hand.

On the other hand, we have also seen the introduction of so-called parent document retrievers, where the hypothesis is that directly using a document’s vector might not be efficient.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb571_b4vP8TVQ56RO-yxswCuelFvamTgaYwviVJWVYZgkay32Kkkp_BJzle4nu1b0kLOzj7RqZxWHdfnIgI9k8lGlT1kpU3PHEv8FB9Y4-AJ69iLGhkvTrv3MsKeq3v_33Ggqvi2lPaj4YLzUMqg4IRMm2xI.jpeg)Types of parent document retrieval strategies. Image by[ Damien Benveniste, PhD](https://www.linkedin.com/in/ACoAAAT2LbsB3xS0kxwoZu8TsNvAXS5jonOKqiw?ref=blog.langchain.com) from[ AiEdge.io](https://newsletter.theaiedge.io/?ref=blog.langchain.com)

Large documents can be split into smaller chunks, where the smaller chunks are converted to vectors, improving indexing for similarity searches. Although these smaller vectors better represent specific concepts, the original large document is retrieved as it provides better context for answering questions. Similarly, you can use an LLM to generate questions the document answers. The document is then indexed by these question embeddings, providing closer similarity with user questions. In both examples, the full parent document is retrieved to provide complete context for answers, hence the name “Parent Document Retriever”.

In this blog post, you will learn how to use the [neo4j-advanced-rag template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-advanced-rag?ref=blog.langchain.com) and host it using LangServe.

**Neo4j Environment Setup**

You need to set up a Neo4j 5.11 or greater to follow along with the examples in this blog post. The easiest way is to start a free instance on[ Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=blog.langchain.com), which offers cloud instances of the Neo4j database. Alternatively, you can also set up a local instance of the Neo4j database by downloading the[ Neo4j Desktop](https://neo4j.com/download/?ref=blog.langchain.com) application and creating a local database instance.

`from langchain.graphs import Neo4jGraph

url = &quot;neo4j+s://databases.neo4j.io&quot;
username =&quot;neo4j&quot;
password = &quot;&quot;
graph = Neo4jGraph(
   url=url,
   username=username,
   password=password
)`

**Neo4j Advanced RAG template**

[LangChain Templates](https://blog.langchain.com/langserve-hub/) offers a collection of easily deployable reference architectures that anyone can use. This is a new way to create, share, maintain, download, and customize chains and agents. They are all in a standard format that allows them to easily be deployed with [LangServe](https://github.com/langchain-ai/langserve?ref=blog.langchain.dev), allowing you to easily get production-ready APIs and a playground for free.

The [`neo4j-advanced-rag` template](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-advanced-rag?ref=blog.langchain.com) allows you to balance precise embeddings and context retention by implementing advanced retrieval strategies.

**Available Strategies**

*1. Typical RAG:*

- Traditional method where the exact data indexed is the data retrieved.

*2. Parent retriever:*

- Instead of indexing entire documents, data is divided into smaller chunks, referred to as Parent and Child documents.

- Child documents are indexed for better representation of specific concepts, while parent documents are retrieved to ensure context retention.

*3. Hypothetical Questions:*

- Documents are processed to generate potential questions they might answer.

- These questions are then indexed for better representation of specific concepts, while parent documents are retrieved to ensure context retention.

*4. Summaries:*

- Instead of indexing the entire document, a summary of the document is created and indexed.

- Similarly, the parent document is retrieved in a RAG application.

To be able to use LangChain templates, you should first install the LangChain CLI:

`pip install -U &quot;langchain-cli[serve]&quot;`

Retrieving the LangChain template is then as simple as executing the following line of code:

`langchain app new my-app --package neo4j-advanced-rag`

This code will create a new folder called my-app, and store all the relevant code in it. Think of it as a “git clone” equivalent for LangChain templates. This will construct the following structure in your filesystem.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb567_qdvXt_GWRW6VUie83fVM7lVqxljf5e-3OGBqrIVzb9GplpVOkjTRqy1YkHNbSpLSqtxgokklPq2TAuVxkSIaj-d-mcxb6YKvnY0L2oLbq-tMOpq0XDj0pqhez4uth0zYr2AOAxFXp_r-Qsfib_QmJo0.png)

There are two top-level folders created:

- App: stores the FastAPI server code
- Packages: stores all the templates that you selected to use in this application. Remember, you can use multiple templates in a single application

Every template is a standalone project with its own poetry file, readme, and potentially also an ingest script, which you can use to populate the database. In the `neo4j-advanced-rag` template, the ingest script will construct a small graph based on the information from the Dune wikipedia page. Before running, you need to make sure to add relevant environment variables:

`export OPENAI_API_KEY=sk-..
export NEO4J_USERNAME=neo4j
export NEO4J_PASSWORD=password
export NEO4J_URI=bolt://localhost:7687`

Make sure to change the environment variables to appropriate values. Then, you can run the ingest script with the following command.

`python ingest.py`

The ingest can take a minute as we use the LLM to generate hypothetical questions and summaries. If you inspect the generated graph in Neo4j Browser, you should get a similar visualization:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb574_n-HoWy2UL6W0ke45rLp81I8qXRpy7rlbdv6jKPd7Bqs05sT_nyqCVNagWwlmHnk8jTN2ZZV1EdfFvaWcLhw27dCHMSNRyGTU7bFqAIYETwM7XJJNt0A5aLbyEBczmWuPWiW12gPLWibMG5xjerBEmzw.png)

The purple nodes are the parent documents, which have a length of 512 tokens. Each parent document has multiple child nodes (orange) that contain a subsection of the parent document. Additionally, the parent nodes also have potential questions represented as blue nodes and a single summary node in red. As we have all the data needed for different strategies in a single store, we can easily compare the results of using different advanced retrieval strategies in the Playground application. One thing you need to do is to change the `server.py` to include the `neo4j-advanced-rag` template as an endpoint.

`from fastapi import FastAPI
from langserve import add_routes

from neo4j_advanced_rag import chain as neo4j_advanced_chain

app = FastAPI()

# Add this
add_routes(app, neo4j_advanced_chain, path=&quot;/neo4j-advanced-rag&quot;)

if __name__ == &quot;__main__&quot;:
    import uvicorn

    uvicorn.run(app, host=&quot;0.0.0.0&quot;, port=8000)`

You can now serve this template by executing the following line of code in the root application directory.

`langchain serve`

Finally, you [can open the playground application](http://localhost:8000/neo4j-advanced-rag/playground?ref=blog.langchain.com) in your browser and compare different advanced RAG retrieval approaches.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb57b_jfDNiPa5ccefX6h0HiVzJbqnlgAZgfPda90truHSfbwSs3JkfxZ-xbA9mZE8y2fNf_3n5cgVhbdhN0ryuMoK2JNbMgTe1OLJMA6CQRhWBxzdKRLVurUFDndT7ki4vMh-cdv3SAn040HTpab9XkzGj5Q.png)

The playground is really nice as it offers a nice user interface to test out and inspect various LangChain Templates. For example, you can expand the “Intermediate steps” and inspect which documents were passed to the LLM, what is in the prompt, and all the other details of a chain.

Since the strategy can be selected in the dropdown menu, you can easily compare how the output differs based on the selected retrieval strategy (or inspect documents in the Intermediate steps section).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f12c87c962360cb578_PGQFaFMCEVGmewddSJ_3QcG8Eybopu4GpYfLfes603ptg9caczemP-fY6qRkd9Twpdz3RFNdroiY76Jdpw60Vt7kP3YEWT-rIJtDJKZYTtF5gfOjPEyf11GC7pqvS3r6v1YE5QGvFfLdc7H6h1nXU-0.png)

💡

Even with such a tiny dataset (17 documents of 512 tokens), I was able to find examples where the typical RAG retrieval might fail. Therefore, it seems imperative to learn about advanced retrieval RAG strategies and implement them into your application for better user experience.

### Summary

In today’s RAG applications, the ability to retrieve accurate and contextual information from a large text corpus is crucial. The traditional approach to vector similarity search, while powerful, might sometimes overlook the specific context when longer text is embedded. By splitting longer documents into smaller vectors and indexing these for similarity, we can increase the retrieval accuracy while retaining the contextual information of parent documents to generate the answers with LLMs. Similarly, we can use LLMs to generate hypothetical questions or summaries of text and index those instead but still return the text of the parent document.

Test it out and let us know how it goes!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)