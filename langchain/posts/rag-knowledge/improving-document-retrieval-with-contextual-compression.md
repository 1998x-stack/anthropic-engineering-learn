---
title: "Improving Document Retrieval with Contextual Compression"
author: "LangChain Accounts"
date: "2023-04-21"
url: "https://www.langchain.com/blog/improving-document-retrieval-with-contextual-compression"
---

LangChain

# Improving Document Retrieval with Contextual Compression

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 20, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb238f4d459ecdf60b0d8_photo-1562654501-a0ccc0fc3fb1.jpeg)*Note: This post assumes some familiarity with LangChain and is moderately technical.*

💡 **TL;DR**: We’ve introduced a new abstraction and a new document Retriever to facilitate the post-processing of retrieved documents. Specifically, the new abstraction makes it easy to take a set of retrieved documents and extract from them only the information relevant to the given query.

## Introduction

Many LLM-powered applications require some queryable document storage that allows for the retrieval of application-specific information that&#x27;s not already baked into the LLM.

Suppose you wanted to create a chatbot that could answer questions about your personal notes. One simple approach is to embed your notes in equally-sized chunks and store the embeddings in a vector store. When you ask the system a question, it embeds your question, performs a similarity search over the vector store, retrieves the most relevant documents (chunks of text), and appends them to the LLM prompt.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb239f4d459ecdf60b0e3_screenshot-2023-04-20-at-4.49.13-pm.png)A simple retrieval Q&amp;A system

## Problem

One problem with this approach is that when you ingest data into your document storage system, you often don’t know what specific queries will be used to retrieve those documents. In our notes Q&amp;A example, we simply partitioned our text into equally-sized chunks. That means that when we get a specific user question and retrieve a document, even if the document has some relevant text it likely has some irrelevant text as well.

Inserting irrelevant information into the LLM prompt is bad because:

- It might distract the LLM from the relevant information
- It takes up precious space that could be used to insert other relevant information.

## Solution

To help with this we’ve introduced a `DocumentCompressor` abstraction which allows you to run `compress_documents(documents: List[Document], query: str)` on your retrieved documents. The idea is simple: instead of immediately returning retrieved documents as-is, we can compress them using the context of the given query so that only the relevant information is returned. “Compressing” here refers to both compressing the contents of an individual document and filtering out documents wholesale.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb239f4d459ecdf60b0e0_screenshot-2023-04-20-at-4.52.12-pm.png)Retrieval Q&amp;A system with contextual document compression

The goal of compressors is to make it easy to pass **only** the relevant information to the LLM. By doing this, it also enables you to pass along **more** information to the LLM, since in the initial retrieval step you can focus on recall (e.g. by increasing the number of documents returned) and let the compressors handle precision.

## Features

We’ve implemented a couple new features in the LangChain Python package:

- A set of DocumentCompressors that you can use out of the box.
- A `ContextualCompressionRetriever` which wraps another Retriever along with a DocumentCompressor and automatically compresses the retrieved documents of the base Retriever.

Some example DocumentCompressors:

- The `LLMChainExtractor` uses an LLMChain to extract from each document only the statements that are relevant to the query.
- The `EmbeddingsFilter` embeds both the retrieved documents and the query and filters out any documents whose embeddings aren’t sufficiently similar to the embedded query. On it’s own this compressor does something very similar to most VectorStore retrievers, but it becomes more useful as a component in…
- … the `DocumentCompressorPipeline`, which makes it easy to create a pipeline of transformations and compressors and run them in sequence. A simple example of this is you may want to combine a `TextSplitter` and an `EmbeddingsFilter` to first break up your documents into smaller pieces and then filter out the split documents that are no longer relevant.

You can try these out with any existing Retriever (whether VectorStore based or otherwise) with something like:

`from langchain.llms import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# base_retriever defined somewhere above...

compressor = LLMChainExtractor.from_llm(OpenAI(temperature=0))
compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)
contextual_retriever.get_relevant_documents(&quot;insert query here&quot;)
`

Head to the walkthrough [here](https://python.langchain.com/docs/modules/data_connection/retrievers/how_to/contextual_compression?ref=blog.langchain.com) to get started!

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