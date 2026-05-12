---
title: "Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs"
author: "LangChain Accounts"
date: "2023-08-17"
url: "https://www.langchain.com/blog/langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms"
---

Partner

# Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 17, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b8e3229bd0c68de60a_5-social--1-.png)*Editor&#x27;s Note: This post was written in collaboration with the Predibase team. We&#x27;re really excited about the way their integration with LangChain helps bring production-grade standards and workflows to open-source to open-source models. *

Today, we’re announcing a Langchain Integration for [Predibase](https://predibase.com/?ref=blog.langchain.com). This integration allows Langchain developers to seamlessly integrate hosted OSS models on Predibase into their workflows.

## What is Predibase?

 Predibase is a Developer platform for OSS LLMs. Predibase allows builders to:

- Deploy and query pre-trained or custom open source LLMs without the hassle
- Operationalize an end-to-end Retrieval Augmented Generation (RAG) system
- Fine-tune their own LLM in just a few lines of code

If using commercial LLM providers like OpenAI / Anthropic / Cohere might not be a good fit due to privacy or cost, Predibase might be a natural choice to explore. While Predibase is focused on helping you productionize open-source LLMs, the platform itself is also built on top of open-source foundations including Ludwig and Horovod. It supports multiple interfaces including a UI and a Python SDK, making it accessible to users of all levels. Best of all, the platform can be deployed on Predibase-managed infrastructure or securely inside your own Cloud VPC so your data and models stay within your secure environment.

## Langchain + Predibase

Setup:

- Sign up for Predibase for free: [https://predibase.com/free-trial](https://predibase.com/free-trial?ref=blog.langchain.com)
- Create an Account
- Go to Settings &gt; My profile and Generate a new API Token

### Q/A Example ([Colab Notebook](https://colab.research.google.com/drive/1ASRX6BOVMfgAEkTmcCDYATCSbfzfg3S4?usp=sharing&amp;ref=blog.langchain.com))

Below is an example of a simple Q/A system you can build using Langchain and Predibase-hosted LLMs.

`pip install predibase
pip install langchain
pip install chromadb
pip install sentence_transformers

# Replace with your Predibase API Token
import os
os.environ[“PREDIBASE_API_TOKEN”] = “{PREDIBASE_API_TOKEN}”

from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import Predibase

# Document loader
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader(&quot;https://lilianweng.github.io/posts/2023-06-23-agent/&quot;)
data = loader.load()

# Split into Chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

# Store Embeddings in Chroma
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
vectorstore = Chroma.from_documents(documents=all_splits,embedding = HuggingFaceEmbeddings())

# Pull in any LLM from Predibase, including fine-tuned LLM’s
llm = Predibase(model=&quot;llama-2-13b&quot;, predibase_api_key=os.environ.get(&quot;PREDIBASE_API_TOKEN&quot;))

# Fetch relevant chunks into LLM
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
qa_chain({&quot;query&quot;: question})
`

We’re very excited to make these capabilities available for all LangChain users and we couldn’t be more excited to see what the community builds! If you have ideas, comments, or questions, feel free to reach out on the [LangChain](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) Discord or via [support@predibase.com](mailto:support@predibase.com).

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