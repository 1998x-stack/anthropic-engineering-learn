---
title: "Embeddings Drive the Quality of RAG: Voyage AI in Chat LangChain"
author: "LangChain Accounts"
date: "2023-11-02"
url: "https://www.langchain.com/blog/voyage-embeddings-in-langchain-and-chat-langchain"
---

LangChainTutorials &amp; How-Tos

# Embeddings Drive the Quality of RAG: Voyage AI in Chat LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 2, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f4ba9d0fc72377bb72_Twitter-post---21--1-.png)*Editor&#x27;s Note: This post was written by the *[*Voyage AI*](https://www.voyageai.com/?ref=blog.langchain.com)* team.*

This post demonstrates that the choice of embedding models significantly impacts the overall quality of a chatbot based on [Retrieval-Augmented Generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/?ref=blog.langchain.com). We focus on the case of [Chat LangChain](https://chat.langchain.com/?ref=blog.langchain.com), the LangChain chatbot for answering questions about LangChain documentation, which currently uses fine-tuned Voyage embeddings in production. We finish by showing how to access general Voyage embedding models via LangChain.

## Brief background on RAG, retrieval system, and embeddings

**Retrieval-augmented generation**, commonly called RAG, is a powerful design pattern for chatbots where a **retrieval system** fetches validated sources/documents that are pertinent to the query, in real-time, and inputs them to a generative model (e.g., GPT-4) to generate a response. With high-quality retrieved data, RAG can ensure that generated responses are not just intelligent, but also contextually accurate and informed.

Modern retrieval system are empowered by semantic search using dense-vector representations of the data. **Embedding models,** which are neural nets models, transform the queries and documents into vectors, which are called embeddings. Then, the documents whose embeddings are closest to the embedding of the query are retrieved. The quality of the retrieval is thus solely decided by how the data are represented as vectors; vice versa, the effectiveness of embedding models is evaluated based on their accuracy in retrieving relevant information.

Please check out this introduction post to [RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/?ref=blog.langchain.com) for more details.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bba8_Untitled201.png)

## Evaluating the effect of embeddings in the RAG stack

**Methodology.** RAG has two main AI components, embedding models and generative models. We ablate the effect of embedding models by keeping the generative model component to be the state-of-the-art model, GPT-4. We measure two metrics, (1) the retrieval quality, which is a modular evaluation of embedding models, and (2) the end-to-end quality of the response of the RAG. We will show that retrieval quality directly affects end-to-end response quality.

**Evaluation scenarios.** In this post, we focus on the scenario of the Chat LangChain bot that answers questions about [LangChain](https://python.langchain.com/?ref=blog.langchain.com) documentation. The [open-source](https://github.com/langchain-ai/chat-langchain?ref=blog.langchain.com) chatbot uses a RAG stack with a pool of 6,522 documents sourced directly from the LangChain docs. From the partnership with [LangChain](https://www.langchain.com/?ref=blog.langchain.com), we obtained a collection of 50 pairs of queries and corresponding gold standard answers, which are the main dataset for evaluating the response quality.

**Models.** We consider three embedding models, OpenAI’s industry-leading embedding model [`text-embedding-ada-002`](https://openai.com/blog/new-and-improved-embedding-model?ref=blog.langchain.com) , Voyage’s generalist model [`voyage-01`](https://docs.voyageai.com/embeddings/?ref=blog.langchain.com) , and an enhanced version fine-tuned on LangChain docs , `voyage-langchain-01`.

**Measuring response quality.** To evaluate the response’s quality, we compare the semantic similarity between the generated responses and the gold standard responses by asking GPT-4 to evaluate the similarity with a score out of 10. A score of 1 indicates that the generated answer is incorrect and bears no relevance to the gold standard answer, while a score of 10 signifies a perfect alignment with the gold standard answer.

**Measuring retrieval quality.** For the 50 queries, we manually curate the gold-standard documents that are most relavent to the queries. We retrieve 10 documents for each queries, and use the standard [NDCG@10](https://en.wikipedia.org/wiki/Discounted_cumulative_gain?ref=blog.langchain.com) metric to calculate the relevance of the retrieve docs to the gold-stand document.

**Results.** The table below shows that `voyage-01` surpasses OpenAI’s `text-embedding-ada-002` in both the retrieval quality and response quality. Furthermore,  `voyage-langchain-01`, which was specifically fine-tuned on LangChain documents, has the highest retrieval and response quality. The data suggest that indeed the quality of the final response is highly correlated with the retrieval quality, and `voyage-01` and `voyage-langchain-01` improve the final response’s quality by improving the retrieval quality.

Model Name

Response quality(1-10) ↑

Retrieval quality ↑

Voyage (`voyage-langchain-01`)

6.25

52.40

Voyage (`voyage-01`)

5.08

47.55

OpenAI (`text-embedding-ada-002`)

4.34

45.81

## Demonstrating examples

We support the quantitive results above by showcasing a few intuitive examples where more accurate retrieval with Voyage’s embeddings enables more accurate responses.

### **Example 1:  `voyage-01` vs **[**`text-embedding-ada-002`**](https://openai.com/blog/new-and-improved-embedding-model?ref=blog.langchain.com)

**Query***: “What is html2texttransformer? Does it omit urls?”*

Given the query above, `voyage-01` (left) fetches the correct document, the detailed description of the `html2texttransformer` function, whereas `text-embedding-ada-002` (right) retrieves a less relavent document, the documentation of `html2text` which contains `html2texttransformer` as a method. The latter document does contain the string `html2texttransformer` but only in an exemplar code block.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bbb0_image-2.png)**Left**: Top-1 doc retrieved by voyage-01. **Right**: Top-1 doc retrieved by text-embedding-ada-002.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bba3_Untitled-2.png)

Consequently, the response generated by RAG using the `voyage-01` (left) is accurate, whereas the response with `text-embedding-ada-002` (right) confuses `html2texttransformer` with the class that contains it.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f5ba9d0fc72377bb8f_Screenshot-2023-10-31-at-10.43.22-PM.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f5ba9d0fc72377bb93_Screenshot-2023-10-31-at-10.43.27-PM.png)

### **Example 2:  `voyage-01` vs `voyage-langchain-01`**

The fine-tuned model `voyage-langchain-01` has a superior retrieval quality and response quality than `voyage-01`. The examples below demonstrate how `voyage-langchain-01` can fetch documents with more pertinent information given the query below.

**Query**: *“I’m running my own model using vllm. How do I connect it to LangChain?”*

As we can see below, `voyage-01` (left) doesn’t give a document that is relevant to vLLM, whereas `voyage-langchain-01` (right) retrieves the correct document. Here the reason is that vLLM is a highly specialized concept that a generalist embedding model is difficult to grasp; but a fine-tuned model has seen the LangChain documentation and thus can catch up with the terminology and concept.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bbab_Screenshot-2023-10-31-at-1.28.36-PM.png)**Left**: Top-1 doc retrieved by voyage-01. **Right**: Top-1 doc retrieved by voyage-langchain-01.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bba0_Untitled1.png)

Not surprisingly, the RAG with `voyage-langchain-01` (right) accurately answers the question. On the other hand, without retrieving the correct document, RAG with `voyage-01` (left) hallucinates an answer.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bb9c_Screenshot-2023-10-31-at-10.32.50-PM.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f6ba9d0fc72377bb99_Screenshot-2023-10-31-at-10.32.55-PM.png)

## Using Voyage in LangChain

As of `langchain &gt;= 0.0.327`, Voyage is integrated into the LangChain Python package, allowing anyone to access the `voyage-01` model for their own applications.

You can get a Voyage API key [here](https://www.voyageai.com/?ref=blog.langchain.com), which should be set as an environment variable:

`export VOYAGE_API_KEY=&quot;...&quot;`

Install the latest version of LangChain:

`pip install -U langchain`

And you can start using `VoyageEmbeddings` . Here&#x27;s a simple example of how to use Voyage to power KNN retrieval:

`from langchain.embeddings import VoyageEmbeddings
from langchain.retrievers import KNNRetriever

texts = [
  &quot;Caching embeddings enables the storage or temporary caching of embeddings, eliminating the necessity to recompute them each time.&quot;,
  &quot;The agent executor is the runtime for an agent. This is what actually calls the agent and executes the actions it chooses&quot;,
  &quot;A Runnable represents a generic unit of work that can be invoked, batched, streamed, and/or transformed.&quot;
]

embeddings = VoyageEmbeddings(model=&quot;voyage-01&quot;, batch_size=8)
retriever = KNNRetriever.from_texts(texts, embeddings, k=1)

result = retriever.get_relevant_documents(
  &quot;How do I build an agent?&quot;
)
print(result[0].page_content)The agent executor is the runtime for an agent. This is what actually calls the agent and executes the actions it chooses
`

You can find the full [LangChain integration docs here](https://python.langchain.com/docs/integrations/text_embedding/voyageai?ref=blog.langchain.com) and the [Voyage docs here](http://docs.voyageai.com/?ref=blog.langchain.com).

## Takeaways

The retrieval quality of the embedding models is highly correlated with the quality of the final responses — to make your RAG more successful, you should consider improving your embeddings! Try Voyage embeddings `voyage-01` or contact us for early access to the fine-tuned models at  [contact@voyageai.com](mailto:contact@voyagei.com). Follow up on [twitter](https://twitter.com/voyage_ai_?ref=blog.langchain.com) and/or [linkedin](https://www.linkedin.com/company/voyageai?ref=blog.langchain.com) for more updates!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)