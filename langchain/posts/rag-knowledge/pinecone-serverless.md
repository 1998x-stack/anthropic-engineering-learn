---
title: "Build and deploy a RAG app with Pinecone Serverless"
author: "LangChain Accounts"
date: "2024-01-16"
url: "https://www.langchain.com/blog/pinecone-serverless"
---

Tutorials &amp; How-Tos

# Build and deploy a RAG app with Pinecone Serverless

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 16, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf997fb97c3e9f4d58474e_Screenshot-2024-01-16-at-6.49.13-AM.webp)

## Key Links

- Repo: [https://github.com/langchain-ai/pinecone-serverless](https://github.com/langchain-ai/pinecone-serverless?ref=blog.langchain.com)
- Video: [https://youtu.be/EhlPDL4QrWY](https://youtu.be/EhlPDL4QrWY?ref=blog.langchain.com)

## Context

LLMs are unlocking a new era of generative AI applications, becoming the kernel process of [a new kind of operating system](https://www.youtube.com/watch?v=zjkBMFhNj_g&amp;ref=blog.langchain.com). Just as modern computers have RAM and file access, LLMs have a context window that can be loaded with information retrieved from external data sources, such as databases or vectorstores.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf99a771199c1b468cabaf_photocontext.png)

Retrieved information can be loaded into the context window and used in LLM output generation, a process called [retrieval augmented generation](https://arxiv.org/pdf/2312.10997.pdf?ref=blog.langchain.com) (RAG). RAG is [a central concept in LLM app development](https://arxiv.org/abs/2312.10997?ref=blog.langchain.com) because it can reduce hallucinations by grounding output and adds context that is not present the training data.

## Challenges with production

With these points in mind, vectorstores have gained considerable popularity in production RAG applications because they offer a good way to store and retrieve relevant context. In particular, [semantic similarity search](https://www.pinecone.io/learn/what-is-similarity-search/?ref=blog.langchain.com) is commonly used to retrieve chunks of information that are relevant to a user-provided input.

A large number of RAG demos have been shared over the past months, often using tools such as Jupyter notebooks and local vectorstores. Yet, several pain points create a gap between these demos and production RAG applications. Below, we&#x27;ll discuss several ways to overcome these gaps and provide both a repo and a hands-on video that builds a production RAG application from scratch.  

**Pain Point**

**Detail**

**Solutions**

Hosted vectorstore management

Usage-based-pricing and unlimited scalability

Pinecone serverless

Rapid RAG application deployment

Rapid deployment of prototype RAG applications

Hosted LangServe

RAG observability

Seamless observability of the RAG application

LangSmith

## Support for production

### Pinecone Serverless

[Pinecone](https://www.pinecone.io/?ref=blog.langchain.com) is one of the most popular LangChain vectorstore integration [partners](https://integrations.langchain.com/vectorstores?ref=blog.langchain.com) and has been widely used in production due to its support for hosting. Yet, at least two pain points we&#x27;ve heard from the community include: (1) the need to provision your own Pinecone index and (2) pay a fixed monthly price for the index regardless of usage. The launch of Pinecone serverless addresses both of these challenges, providing “unlimited” index capacity via cloud object storage (ex. S3 or GCS) along with considerably reduce cost to serve (allowing users to pay for what they use).

### LangServe

While LangChain has become popular for rapid prototyping RAG applications, we saw an opportunity to support rapid deployment of any chain to a web service that is suitable for production. This motivated [LangServe](https://blog.langchain.com/introducing-langserve/). Any chain composed using [LCEL](https://python.langchain.com/docs/expression_language/?ref=blog.langchain.com) has a runnable interface with a common set of invocation methods (e.g., batch, stream). With LangServe, these methods are mapped to HTTP endpoints in of a web service, which can be managed using Hosted LangServe.

### LangSmith

[LangSmith](https://blog.langchain.com/announcing-langsmith/) offers a platform for [LLM observability](https://www.langchain.com/articles/llm-monitoring-observability?ref=blog.langchain.com) that integrates seamlessly with LangServe. We can compose a RAG chain that connects to Pinecone Serverless using LCEL, turn it into an a web service with LangServe, use Hosted LangServe deploy it, and use LangSmith to monitor the input / outputs.  

## Example Application

To show how all these pieces come together, we provide a [template repo](https://github.com/langchain-ai/pinecone-serverless?ref=blog.langchain.com).

- It shows how to connect a Pinecone Serverless index to a RAG chain in LangChain, which includes Cohere embeddings for similarity search on the index as well as GPT-4 for answer synthesis based upon the retrieved chunks.
- It shows how to convert the RAG chain into a web service with Langserve. With LangServe, the chain can then be deployed using hosted LangServe.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf99d3c71f7f8464aa2a69_photo2.png)

## Conclusion

We see demand for tools that bridge the gap between prototyping and production. With usage based pricing and support for unlimited scaling, Pinecone Serverless helps to address pain points with vectorstore productionization that we&#x27;ve seen from the community. Pinecone Serverless pairs well with LCEL, Hosted LangServe, and LangSmith to support easly deployment of RAG applications.

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