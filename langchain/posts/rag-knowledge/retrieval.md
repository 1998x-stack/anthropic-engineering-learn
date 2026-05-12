---
title: "Retrieval"
author: "LangChain Accounts"
date: "2023-03-24"
url: "https://www.langchain.com/blog/retrieval"
---

Agent ArchitectureLangChain

# Retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb248a83bd2fbf570c3cb_photo-1576201836106-db1758fd1c97.jpeg)TL;DR: We are adjusting our abstractions to make it easy for other retrieval methods besides the LangChain `VectorDB` object to be used in LangChain. This is done with the goals of (1) allowing retrievers [constructed elsewhere](https://github.com/openai/chatgpt-retrieval-plugin?ref=blog.langchain.com) to be used more easily in LangChain, (2) encouraging more experimentation with alternative retrieval methods (like [hybrid search](https://www.pinecone.io/learn/hybrid-search-intro/?ref=blog.langchain.com)). This is backwards compatible, so all existing chains should continue to work as before. However, we recommend updating from `VectorDB` chains to the new `Retrieval` chains as soon as possible, as those will be the ones most fully supported going forward.

[Python Docs](https://python.langchain.com/docs/modules/data_connection/retrievers/?ref=blog.langchain.com)

[JS Docs](https://hwchase17.github.io/langchainjs/docs/modules/indexes/retrievers/vectorstore?ref=blog.langchain.com)

## Introduction

Ever since ChatGPT came out, people have been building a personalized ChatGPT for their data. We even wrote [a tutorial on this](https://blog.langchain.com/tutorial-chatgpt-over-your-data/), and then [ran a competition](https://blog.langchain.com/chat-your-data-challenge/) about this a few months ago. The desire and demand for this highlights an important limitation of ChatGPT - it doesn&#x27;t know about YOUR data, and most people would find it more useful if it did. So how do you go about building a chatbot that knows about your data?

The main way of doing this is through a process commonly referred to as &quot;Retrieval Augmented Generation&quot;. In this process, rather than just passing a user question directly to a language model, the system &quot;retrieves&quot; any documents that could be relevant in answering the question, and then passes those documents (along with the original question) to the language model for a &quot;generation&quot; step.

The main way most people - including us at LangChain - have been doing retrieval is by using semantic search. In this process, a numerical vector (an embedding) is calculated for all documents, and those vectors are then stored in a vector database (a database optimized for storing and querying vectors). Incoming queries are then vectorized as well, and the documents retrieved are those who are closest to the query in embedding space. We&#x27;re not going to go into too much detail on that here - but [here](https://blog.langchain.com/tutorial-chatgpt-over-your-data/) is a more in depth tutorial on the topic, and below is a diagram which nicely summarizes this.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb248a83bd2fbf570c3f7_image-1.png)Diagram of typical retrieval step

## Problems

This process works pretty well, and a lot of the components and abstractions we&#x27;ve built (embeddings, vectorstores) are aimed at facilitating this process.

But we&#x27;ve noticed two problems.

**First:** there a lot of different variations in how you do this retrieval step. People want to do things beyond semantic search. To be concrete:

- We support two different query methods: one that just optimizes similarity, another with optimizes for [maximal marginal relevance](https://blog.langchain.com/content/files/~jgc/publication/the_use_mmr_diversity_based_ltmir_1998.pdf).
- Users often want to specify metadata filters to filter results before doing semantic search
- Other types of indexes, [like graphs](https://python.langchain.com/docs/modules/chains/additional/graph_qa?ref=blog.langchain.com), have piqued user&#x27;s interests

**Second:** we also realized that people may construct a retriever outside of LangChain - for example OpenAI released their [`ChatGPT Retrieval Plugin`](https://github.com/openai/chatgpt-retrieval-plugin?ref=blog.langchain.com). We want to make it as easy as possible for people to use whatever retriever they created within LangChain.

We realized we made a mistake - by making our abstractions centered around VectorDBQA we were limiting to use of our chains, making them hard to use (1) for users who wanted to experiment with other retrieval methods, (2) for users who created a retriever outside the LangChain ecosystem.

## Solution

So how did we fix this?

In our most recent Python and TypeScript releases, we&#x27;ve:

- Introduced the concept of a `Retriever`. Retrievers are expected to expose a `get_relevant_documents` method with the following signature: `def get_relevant_documents(self, query: str) -&gt; List[Document]`. That&#x27;s the only assumption we make about Retrievers. See more about this interface below.
- Changed all our chains that used VectorDBs to now use Retrievers. `VectorDBQA` is now `RetrievalQA`, `ChatVectorDBChain` is now `ConversationalRetrievalChain`, etc. *Note that, moving forward, we are intentionally using the `Conversational` prefix to indicate that the chain is using memory and the `Chat` prefix to indicate the chain is using a chat model.*
- Added the first instance of a non-LangChain Retriever - the [`ChatGPT Retrieval Plugin`](https://github.com/openai/chatgpt-retrieval-plugin?ref=blog.langchain.com). This was a module open-sourced yesterday by OpenAI to help companies expose retrieval endpoints to hook into ChatGPT. NB: for all intents and purposes, the inner workings of the `ChatGPT Retrieval Plugin` are extremely similar to our VectorStores, but we are still extremely excited to integrate this as a way highlighting the new flexibility that exists.

Expanding on the `Retriever` interface:

- We purposefully only require one method (`get_relevant_documents`) in order to be as permissive as possible. We do not (yet) require any uniform methods around construction of these retrievers.
- We purposefully enforce `query: str` as the only argument. For all other parameters - including metadata filtering - this should be stored as parameters on the retriever itself. This is because we anticipate the retrievers often being used nested inside chains, and we do not want to have plumb around other parameters.

***This is all done with the end goal of making it easier for alternative retrievers (besides the LangChain VectorStore) to be used in chains and agents, and encouraging innovation in alternative retrieval methods. ***

## Q&amp;A

**Q: What&#x27;s the difference between an index and a retriever?**

**A: **An index is a data structure that supports efficient searching, and a retriever is the component that uses the index to find and return relevant documents in response to a user&#x27;s query. The index is a key component that the retriever relies on to perform its function.

**Q: If I was using a VectorStore before in `VectorDBQA` chain (or other `VectorDB`-type chains), what do I now use in `RetrievalQA` chain?**

**A:** You can use a `VectorStoreRetriever`, which you can create from an existing vectorstore by doing `vectorstore.as_retriever()`

**Q: Does `VectorDBQA` chain (or other `VectorDB`-type chains) still exist?**

**A:** Yes, although we will be no be focusing on it any more. Expect any future development to be done on `RetrievalQA` chain.

**Q: Can I contribute a new retrieval method to the library?**

**A:** Yes! We started a new `langchain/retrievers` module exactly for this purpose

**Q: What are real world examples this enables?**

**A: **The main one is better question-answering over your documents. However, if start to ingest and then retrieve previous messages, this can then be thought of as better long term memory for AI.

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