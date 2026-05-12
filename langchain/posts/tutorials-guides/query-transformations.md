---
title: "Query Transformations"
author: "LangChain Accounts"
date: "2023-10-24"
url: "https://www.langchain.com/blog/query-transformations"
---

Tutorials &amp; How-Tos

# Query Transformations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 24, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0ff3fe3e9a95a559a08_figure.png)Naive RAG typically splits documents into chunks, embeds them, and retrieves chunks with high semantic similarity to a user question. But, this present a few problems: (1) document chunks may contain irrelevant content that degrades retrieval, (2) user questions may be poorly worded for retrieval, and (3) structured queries may need to be generated from the user question (e.g., for querying a vectorstore with metadata filtering or a SQL db).

LangChain has many [advanced retrieval methods](https://python.langchain.com/docs/modules/data_connection/retrievers/?ref=blog.langchain.com) to help address these challenges. (1) **Multi representation indexing**: Create a document representation (like a summary) that is well-suited for retrieval (read about this using the Multi Vector Retriever in [a blog post](https://blog.langchain.com/semi-structured-multi-modal-rag/) from last week). (2) **Query transformation**: in this post, we&#x27;ll review a few approaches to transform humans questions in order to improve retrieval. (3) **Query construction**: convert human question into a particular query syntax or language, which will be covered in a future post.

 If you think of a naive RAG pipeline, the general flow is that you take the users question and pass that directly to an embedding model. That embedding is then compared to documents stored in the vectorstore, and the top `k` most similar ones are returned.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10373a7146af5cae3f0_rag.png)

Query transformation deals with transformations of the user&#x27;s question before passing to the embedding model.

💡

Although this is not a new phenomenon ([query expansion](https://www.searchenginejournal.com/what-is-google-query-expansion-cases-and-examples/7924/?ref=blog.langchain.com) has been used in search for years) what is new is the ability to use LLMs to do it.

Below are a few variations of papers and retrieval methods that take advantage of this. They are all using an LLM to generate a new (or multiple new) queries, and the main difference is the prompt they use to do that generation.

## Rewrite-Retrieve-Read

This paper uses an LLM to **rewrite** a user query, rather than using the raw user query to retrieve directly.

> Because the original query can not be always optimal to retrieve for the LLM, especially in the real world... we first prompt an LLM to rewrite the queries, then conduct retrieval-augmented reading.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10473a7146af5cae3f8_Screenshot-2023-10-21-at-2.07.13-PM.png)

The prompt used is a relatively simple one (on the Hub [here](https://smith.langchain.com/hub/langchain-ai/rewrite)):

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10373a7146af5cae3e5_Screenshot-2023-10-23-at-6.27.50-PM.png)

Links:

- [Paper](https://arxiv.org/pdf/2305.14283.pdf?ref=blog.langchain.com)
- [LangChain Implementation](https://github.com/langchain-ai/langchain/blob/master/cookbook/rewrite.ipynb?ref=blog.langchain.com)

## Step back prompting

This paper uses an LLM to generate a &quot;step back&quot; question. This can be use with or without retrieval. With retrieval, both the &quot;step back&quot; question and the original question are used to do retrieval, and then both results are used to ground the language model response.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10473a7146af5cae3fb_Screenshot-2023-10-21-at-2.08.09-PM.png)

[Here](https://smith.langchain.com/hub/langchain-ai/stepback-answer?ref=blog.langchain.com) is the prompt used:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10373a7146af5cae3e8_Screenshot-2023-10-23-at-6.31.16-PM.png)

Links:

- [Paper](https://arxiv.org/pdf/2310.06117.pdf?ref=blog.langchain.com)
- [LangChain Implementation](https://github.com/langchain-ai/langchain/blob/master/cookbook/stepback-qa.ipynb?ref=blog.langchain.com)

## Follow Up Questions

The most basic and central place query transformation is used is in conversational chains to handle follow up questions. When dealing with follow up questions, there are essentially three options:

- Just embed the follow up question. This means that if the follow up question builds on, or references the previous conversation, it will lose that question. For example, if I first ask &quot;what can I do in Italy&quot; and then ask &quot;what type of food is there&quot; - if I just embed &quot;what type of food is there&quot; I will have no context of where &quot;there&quot; is.
- Embed the whole conversation (or last `k` messages). The problem with this is that if a follow up question is completely unrelated to previous conversation, then it may return completely irrelevant results that would distract during generation.
- Use an LLM to do a query transformation!

In this last option, you pass the whole conversation to date (including the follow up question) to the LLM and ask it generate a search term. This is what we do in [WebLangChain](https://blog.langchain.com/weblangchain/) and what most chat based retrieval applications likely do.

The question then becomes: what prompt do I use to transform the whole conversation into a search query? This is where a lot of prompt engineering needs to be done. Below is the prompt we use for WebLangChain (it phrases the &quot;query generation&quot; bit as constructing a standalone question). See it on the Hub [here](https://smith.langchain.com/hub/langchain-ai/weblangchain-search-query?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10373a7146af5cae3f3_Screenshot-2023-10-23-at-6.31.46-PM.png)

## Multi Query Retrieval

In this strategy, an LLM is used to generate multiple search queries. These search queries can then be executed in parallel, and the retrieved results passed in altogether. This is really useful when a single question may rely on multiple sub questions.

For example consider the following question:

> Who won a championship more recently, the Red Sox or the Patriots?

This really requires two sub-questions:

- &quot;When was the last time the Red Sox won a championship?&quot;
- &quot;When was the last time the Patriots won a championship?&quot;

Links:

- [LangChain Implementation](https://python.langchain.com/docs/modules/data_connection/retrievers/MultiQueryRetriever?ref=blog.langchain.com)

## RAG-Fusion

A recent article builds off the idea of Multi-Query Retrieval. However, rather than passing in all the documents, they use reciprocal rank fusion to reorder the documents.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb10373a7146af5cae3ed_1_5nG7iLyBoO-B5Tna6oDc-Q%402x.webp)

Links:

- [Blog Post](https://towardsdatascience.com/forget-rag-the-future-is-rag-fusion-1147298d8ad1?ref=blog.langchain.com)
- [LangChain Implementation](https://github.com/langchain-ai/langchain/blob/master/cookbook/rag_fusion.ipynb?ref=blog.langchain.com)

## Conclusion

As you can see, there are many different ways to do query transformation. Again, this is not a new topic - but what is new is using LLMs to do this. The differences in the methods comes down to the prompts used. It&#x27;s very easy to write prompts - almost as easy as it to think of them. Which begs the question - what query transformations are YOU going to come up with? Let us know!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)