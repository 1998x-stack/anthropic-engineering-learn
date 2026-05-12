---
title: "LangChain + Vectara: better together"
author: "LangChain Accounts"
date: "2023-06-06"
url: "https://www.langchain.com/blog/langchain-vectara-better-together"
---

LangChainPartner

# LangChain + Vectara: better together

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 6, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21590227306de7e78fa_screenshot-2023-06-05-at-8.48.36-pm.png)

## Introduction

One of the main use cases of LangChain is connecting LLMs to user data, allowing users to build personalized LLM applications. A key part of this is retrieval - fetching relevant documents based on user queries.

Today we’re happy to announce the integration of [Vectara](http://www.vectara.com/?ref=blog.langchain.com) into LangChain to help make retrieval easier. In this blog post, we’ll dig deeper into why retrieval is so important and how to use Vectara’s LangChain integration to build scalable LLM-powered applications.

## What is Vectara?

Vectara is a GenAI [conversational search](http://vectara.com/?ref=blog.langchain.com) platform, providing an easy-to-use “ChatGPT for your own data&#x27;&#x27; experience using “[Grounded Generation](https://vectara.com/grounded-generation/?ref=blog.langchain.com)”.

Developers can use Vectara’s API, based on a neural search core, which enables highly accurate matching between queries and relevant documents, to build GenAI conversational search applications, such as our [AskNews](http://asknews.demo.vectara.com/?ref=blog.langchain.com) sample application.

Using Vectara simplifies LLM application development: the search platform does a lot of the heavy lifting of interfacing with user data, letting developers focus on the application logic unique to their product.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21590227306de7e7901_830391a7.png)**Figure 1:** Vectara’s API platform for “Grounded Generation”

## Grounded Generation with LangChain

LLMs are extremely powerful models, but they have a problem with data recency and hallucinations. For example, as mentioned in this blog post about [LLM hallucinations](https://vectara.com/avoiding-hallucinations-in-llm-powered-applications/?ref=blog.langchain.com), if you ask ChatGPT about Silicon Valley Bank, it will provide a response based on the pre-2022 data it was trained on, and will have no idea above the bank’s recent collapse.

“Grounded Generation” is a general approach to address this issue and is one of the main use cases available through LangChain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb21590227306de7e790f_screenshot-2023-06-05-at-8.49.41-pm.png)**Figure 2: Grounded Generation. **Content is first transformed into embeddings, and stored in a vector store. When a user issues a query, we first identify relevant facts by matching the query embedding with relevant pieces of content previously indexed and provide those facts to the summarization model (along with the query) to provide an accurate response based on all the relevant known facts.

Let’s look at a simple [example](https://github.com/hwchase17/langchain/blob/b95002289409077965d99636b15a45300d9c0b9d/docs/use_cases/evaluation/data_augmented_question_answering.ipynb?ref=blog.langchain.com#L8) of question-answering with retrieval augmented generation from the LangChain codebase.

`from langchain.document_loaders import TextLoader
from langcain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitters import CharacterTextSplitter
from langchain.vectorstores import FAISS

raw_docs = TextLoader(‘state_of_the_union.txt&#x27;).load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)
qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=vectorstore.as_retriever())`

**Figure 3:** Default implementation of retrieval augmented generation with LangChain

First, we take the document text (in this case, a transcript of the 2022 State of the Union) and use langchain.text_splitter.CharacterTextSplitter to split the text into small chunks (1000 characters each).

Then we get embeddings for each chunk using OpenAIEmbeddings, and store them in a vector database like FAISS.

Finally, we build a RetrievalQA ( retrieval question-answer) chain.

And the answer we get is.

> “Putin miscalculated that the world would roll over when he rolled into Ukraine.”

Pretty cool!

## LangChain question-answering with Vectara

Let’s run the same program, but this time use Vectara as the vector store. Doing this will take advantage of Vectara’s “Grounded Generation”.

First, we [set up](https://console.vectara.com/signup?ref=blog.langchain.com) a Vectara account and create a corpus. After creating an API key for that corpus, we can set up the required arguments as environment variables:

`export VECTARA_CUSTOMER_ID=&lt;your-customer-id&gt;
export VECTARA_CORPUS_ID=&lt;the-corpus-id&gt;
export VECTARA_API_KEY=&lt;...API-KEY…&gt;`

Vectara provides its own embeddings that are optimized for accurate retrieval, so we actually don’t have to use (or pay for) an additional embedding model. Instead, we simply use Vectara.from_documents() to upload the documents into Vectara’s index for this corpus, and use that as a retriever in the chain:

`from langchain.vectorstores import Vectara
loader = TextLoader(“state_of_the_union.txt”)
documents = loader.load()
vectara  = Vectara.from_documents(documents)
qa = RetrievalQA.from_llm(llm=OpenAI(), retriever=vectara.as_retriever())
print(qa({“query”:  “According to the document, what did Vladimir Putin miscalculate?”}))`

**Figure 3:** Question answering with LangChain + Vectara. Architecture is much simpler and more robust as the storage of document embedding and matching queries to relevant facts is taken care of by the Vectara platform/API.

Vectara takes the source documents and automatically chunks it in an optimized manner and creates the embeddings, so we don’t even have to use the TextSplitter (and decide on chunk size), nor do we need to call (or pay for) OpenAIEmbeddings. Since Vectara has its own internal vector storage, we don’t need to use FAISS or any other commercial vector database.

Finally, we build a RetrievalQA (retrieval question-answer) chain in the same way as before, and again we get the response:

> “Putin miscalculated that the world would roll over when he rolled into Ukraine.”

## Summary

We are excited to have Vectara fully integrated with LangChain, making it easier for developers who already love LangChain to build LLM-powered applications with Grounded Generation.

Big thanks to the Vectara team ([Ofer](https://twitter.com/ofermend?ref=blog.langchain.com),  [Amr](https://twitter.com/awadallah?ref=blog.langchain.com) and many others) for their support and contribution.

If you’d like to experience the benefits of Vectara + LangChain firsthand, you can sign up for a free Vectara account [here](https://console.vectara.com/signup?ref=blog.langchain.com).

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