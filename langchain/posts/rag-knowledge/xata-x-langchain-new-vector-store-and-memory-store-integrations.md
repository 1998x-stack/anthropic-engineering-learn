---
title: "Xata x LangChain: new vector store and memory store integrations"
author: "LangChain Accounts"
date: "2023-08-29"
url: "https://www.langchain.com/blog/xata-x-langchain-new-vector-store-and-memory-store-integrations"
---

Partner

# Xata x LangChain: new vector store and memory store integrations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 29, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18dba9d0fc72377ea11_5-social--12-.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Xata*](https://xata.io/?ref=blog.langchain.com)* team. We&#x27;re excited about their new integrations and really enjoyed their deepdive on implementation a Q&amp;A chat bot with them.  *

Over the past few weeks, we’ve merged four Xata integrations to the LangChain repositories, and today we’re happy to unveil them as part of [Xata’s launch week](https://xata.io/blog/launch-week-august-2023?ref=blog.langchain.com)! In this blog post, we’ll take a brief look at what Xata is and why it is a good data companion for AI applications. We’ll also show a code example for implementing a Q&amp;A chat bot that answers questions based on the info in a Xata database (as a vector store) and has long-term memory stored in Xata (as a memory store).

## What is Xata?

[Xata](https://xata.io/?ref=blog.langchain.com) is a database platform powered by PostgreSQL. It stores the source-of-truth data in PostgreSQL, but also replicates it automatically to Elasticsearch. This means that it offers functionality from both Postgres (ACID transactions, joins, constraints, etc.) and from Elasticsearch (BM25 full-text search, vector search, hybrid search), behind the same simple serverless API. This covers the functionality needed by the majority of AI applications and because it’s based on PostgreSQL and Elasticsearch, it is reliable and scalable.

Xata has client SDKs for both TypeScript/JavaScript and Python and built-in integrations with platforms like GitHub, Vercel, and Netlify.

In the AI space, beside the LangChain integrations announced here, Xata offers a deep integration with OpenAI for the “[ChatGPT on your data](https://xata.io/chatgpt?ref=blog.langchain.com)” use case.

## The integrations

As of today, the following integrations are available :

- Xata as a [vector store in LangChain](https://python.langchain.com/docs/integrations/vectorstores/xata?ref=blog.langchain.com). This allows one to store documents with embeddings in a Xata table and perform vector search on them. The integration takes advantage of the [newly GA-ed Python SDK](https://xata.io/blog/announcing-the-python-sdk-ga?ref=blog.langchain.com). The integration supports filtering by metadata, which is represented in Xata columns for the maximum performance.
- Xata as a [vector store in LangChain.js](https://js.langchain.com/docs/modules/data_connection/vectorstores/integrations/xata?ref=blog.langchain.com). Same as the Python integration, but for your TypeScript/JavaScript applications.
- Xata as a [memory store in LangChain](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history?ref=blog.langchain.com). This allows storing the chat message history for AI chat sessions in Xata, making it work as “memory” for LLM applications.The messages are stored in
- Xata as a [memory store in LangChain.js](https://js.langchain.com/docs/modules/memory/integrations/xata?ref=blog.langchain.com).  Same as the Python integration, but for TypeScript/JavaScript.

Each integration comes with one or two code examples in the doc pages linked above.

**The four integrations already make Xata one of the most comprehensive data solutions for LangChain, and we’re just getting started!** For the near future, we’re planning to add custom retrievers for the Xata keyword and hybrid search and the Xata [Ask AI](https://xata.io/docs/typescript-client/ask?ref=blog.langchain.com) endpoint.

## Example: Conversational Q&amp;A with memory

While each LangChain integration comes with at least one minimal code example, in this blog post we’ll look at a more complex example that uses Xata both as a vector store and as a memory store. The application implements the “chat with your data” use case, and allows for follow-up questions. The full code can be found in this [repo](https://github.com/tsg/langchain-xata-example?ref=blog.langchain.com), which you can also use as a starter-kit for LangChain + Xata applications.

While the example application here is written in TypeScript, a similar example using the Python LangChain can be found in this [Jupyter notebook](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history?ref=blog.langchain.com#conversational-qa-chain-on-your-data-with-memory).

The main part of the code looks like this:

`import * as dotenv from &quot;dotenv&quot;;
import { XataVectorSearch } from &quot;langchain/vectorstores/xata&quot;;
import { OpenAIEmbeddings } from &quot;langchain/embeddings/openai&quot;;
import { Document } from &quot;langchain/document&quot;;
import { ConversationalRetrievalQAChain } from &quot;langchain/chains&quot;;
import { BufferMemory } from &quot;langchain/memory&quot;;
import { XataChatMessageHistory } from &quot;langchain/stores/message/xata&quot;;
import { ChatOpenAI } from &quot;langchain/chat_models/openai&quot;;

import { getXataClient } from &quot;./xata.ts&quot;;

dotenv.config();

const client = getXataClient();

/* Create the vector store */
const table = &quot;docs&quot;;
const embeddings = new OpenAIEmbeddings();
const vectorStore = new XataVectorSearch(embeddings, { client, table });

/* Add documents to the vector store */
const docs = [
  new Document({
    pageContent: &quot;Xata is a Serverless Data platform based on PostgreSQL&quot;,
  }),
  new Document({
    pageContent:
      &quot;Xata offers a built-in vector type that can be used to store and query vectors&quot;,
  }),
  new Document({
    pageContent: &quot;Xata includes similarity search&quot;,
  }),
];

const ids = await vectorStore.addDocuments(docs);

// eslint-disable-next-line no-promise-executor-return
await new Promise((r) =&gt; setTimeout(r, 2000));

/* Create the chat memory store */
const memory = new BufferMemory({
  chatHistory: new XataChatMessageHistory({
    table: &quot;memory&quot;,
    sessionId: new Date().toISOString(), // Or some other unique identifier for the conversation
    client,
    createTable: false,
  }),
  memoryKey: &quot;chat_history&quot;,
});

/* Initialize the LLM to use to answer the question */
const model = new ChatOpenAI({});

/* Create the chain */
const chain = ConversationalRetrievalQAChain.fromLLM(
  model,
  vectorStore.asRetriever(),
  {
    memory,
  }
);

/* Ask it a question */
const question = &quot;What is Xata?&quot;;
const res = await chain.call({ question });
console.log(&quot;Question: &quot;, question);
console.log(res);
/* Ask it a follow up question */
const followUpQ = &quot;Can it do vector search?&quot;;
const followUpRes = await chain.call({
  question: followUpQ,
});
console.log(&quot;Follow-up question: &quot;, followUpQ);
console.log(followUpRes);

/* Clear both the vector store and the memory store */
await vectorStore.delete({ ids });
await memory.clear();
`

Let’s take it piece by piece and see what it does:

First, we use Xata as a vector store. In this vector store, we index a few sample documents, but in a real application you can index tens of thousands of documents. These are the documents that our chatbot will use to find answers for user questions. While not shown here, it’s also possible to add custom metadata columns to these documents. You can see the examples on the [integration page](https://js.langchain.com/docs/modules/data_connection/vectorstores/integrations/xata?ref=blog.langchain.com#example-similarity-search-with-a-metadata-filter).

`/* Create the vector store */
const table = &quot;docs&quot;;
const embeddings = new OpenAIEmbeddings();
const vectorStore = new XataVectorSearch(embeddings, { client, table });

/* Add documents to the vector store */
const docs = [
  new Document({
    pageContent: &quot;Xata is a Serverless Data platform based on PostgreSQL&quot;,
  }),
  new Document({
    pageContent:
      &quot;Xata offers a built-in vector type that can be used to store and query vectors&quot;,
  }),
  new Document({
    pageContent: &quot;Xata includes similarity search&quot;,
  }),
];

const ids = await vectorStore.addDocuments(docs);
`

Next, we create a chat memory store, again based on Xata. This stores the messages exchanged by the chat bots with the users in a Xata table. Each conversation gets a session ID, which is then used to retrieve the previous messages in the conversation, so that the context is not lost.

`/* Create the chat memory store */
const memory = new BufferMemory({
  chatHistory: new XataChatMessageHistory({
    table: &quot;memory&quot;,
    sessionId: new Date().toISOString(), // Or some other unique identifier for the conversation
    client,
    createTable: false,
  }),
  memoryKey: &quot;chat_history&quot;,
});
`

Then we initialize the client for interrogating the model, in this case the OpenAI ChatGPT API:

`/* Initialize the LLM to use to answer the question */
const model = new ChatOpenAI({});
`

And finally, put all of them together in a conversational QA chain:

`/* Create the chain */
const chain = ConversationalRetrievalQAChain.fromLLM(
  model,
  vectorStore.asRetriever(),
  {
    memory,
  }
);
`

If you look at the data via the Xata UI while the example is running, you will see two tables: `docs` and `memory`. The `docs` table is populated with the documents from the vector store, having a `content` column and an `embedding` column of type `vector`:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18eba9d0fc72377ea4c_Screenshot-2023-08-20-at-20.33.32.png)

The `memory` table is populated with the questions and answers from the user and from the AI:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18eba9d0fc72377ea4f_Screenshot-2023-08-20-at-20.36.04.png)

## Content hackathon

As part of the launch week, Xata is also organizing a content hackathon, where you can win prizes and swag by creating apps, writing blogs, recording videos, and more. See the [launch week blog post](https://xata.io/blog/launch-week-august-2023?ref=blog.langchain.com) for details.

If you have any questions or ideas or if you need help implementing Xata with LangChain, join us on [Discord](https://xata.io/discord?ref=blog.langchain.com) or reach out on [Twitter](https://twitter.com/xata?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)