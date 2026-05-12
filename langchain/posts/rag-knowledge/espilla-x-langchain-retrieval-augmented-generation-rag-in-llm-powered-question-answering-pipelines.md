---
title: "Epsilla x LangChain: Retrieval Augmented Generation (RAG) in LLM-Powered Question-Answering Pipelines"
author: "LangChain Accounts"
date: "2023-08-23"
url: "https://www.langchain.com/blog/espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines"
---

Tutorials &amp; How-TosPartner

# Epsilla x LangChain: Retrieval Augmented Generation (RAG) in LLM-Powered Question-Answering Pipelines

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19c9ace6ff2987bba6f_image1-1.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Epsilla*](https://www.epsilla.com/?ref=blog.langchain.com)* team. As more apps rely on Retrieval Augmented Generation (RAG) for building personalized applications on top of proprietary data, vector databases are becoming even more important. We&#x27;re really excited about what Epsilla is doing here to help builders quickly and accurately fetch the most relevant documents and data points.*

By leveraging the strengths of both LLMs and vector databases, this integration promises richer, more accurate, and context-aware answers.

The landscape of artificial intelligence is ever-evolving. As developers and businesses seek more effective ways to utilize Large Language Models (LLMs), integration tools like LangChain are paving the way. In this post, we&#x27;ll explore Epsilla&#x27;s recent integration with LangChain and how it revolutionizes the question-answering domain.

Retrieval Augmented Generation (RAG) in LLM-Powered Question-Answering Pipelines

Since October 2022, there has been a huge surge in the adoption and utilization of ChatGPT and other Large Language Models (LLMs). These advanced models have emerged as frontrunners in the realm of artificial intelligence, offering unprecedented capabilities in generating human-like text and understanding nuanced queries. However, despite their prowess, ChatGPT and similar models possess inherent limitations. One of the most significant challenges is their inability to incorporate updated knowledge post their last training cut-off, rendering them unaware of events or developments that have transpired since then. Moreover, while they possess vast general knowledge, they can&#x27;t access proprietary or private company data, which is often crucial for businesses looking for tailored insights or decision-making. This is where Retrieval Augmented Generation (RAG) steps in as a game-changer. RAG bridges the knowledge gap by dynamically retrieving relevant information from external sources, ensuring that the generated responses are not only factual but also up-to-date. Vector databases play an integral role in the RAG mechanism by enabling efficient and semantic retrieval of information. These databases store information as vectors, allowing RAG to quickly and accurately fetch the most relevant documents or data points based on the semantic similarity of the input query, enhancing the precision and relevance of the LLM&#x27;s generated responses.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19d9ace6ff2987bba75_JuA_MwHSyOD5WspB9LntncVa8aYdV4AlU3nlvoqVV_7I0nckDzLqbU5L83NF7OL9VcDT6WFc6JbSgMIx3_6u_cUCd86hv5EZDspMRinZfpxOX0WPvErbRy5pYJyJlT2PlSHtaRomrdK64C1rA-0wT3g.png)

## Implementing Question Answering Pipeline with LangChain and Epsilla

LangChain offers a unified interface and abstraction layer on top of LLM ecosystem components, simplifying the process of building generative AI applications. With LangChain, developers can avoid boilerplate code and focus on delivering value.

With the Epsilla integration with LangChain, now the AI application developers can easily leverage the superior performance provided by Epsilla ([benchmark](https://medium.com/@richard_50832/benchmarking-epsilla-with-some-of-the-top-vector-databases-543e2b7708e5?ref=blog.langchain.com)) while building the knowledge retrieval component in the AI applications.

Here is a step by step guide on implementing a question answering pipeline with LangChain and Epsilla.

Step 1. Install LangChain and Epsilla

`pip install langchain
pip install openai
pip install tiktoken
pip install pyepsilladocker pull epsilla/vectordb
docker run --pull=always -d -p 8888:8888 epsilla/vectordb`

Step 2. Provide your OpenAI key

`import os

os.environ[&quot;OPENAI_API_KEY&quot;] = &quot;YOUR_OPENAI_API_KEY&quot;`

Step 3. Prepare for knowledge and embedding model

`from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter

loader = WebBaseLoader(&quot;https://raw.githubusercontent.com/hwchase17/chat-your-data/master/state_of_the_union.txt&quot;)
documents = loader.load()

documents = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(documents)

embeddings = OpenAIEmbeddings()
`

Step 4. Vectorize the knowledge documents

`from langchain.vectorstores import Epsilla
from pyepsilla import vectordb

client = vectordb.Client()
vector_store = Epsilla.from_documents(
documents,
embeddings,
client,
db_path=&quot;/tmp/mypath&quot;,
db_name=&quot;MyDB&quot;,
collection_name=&quot;MyCollection&quot;
)`

Step 5. Create a RetrievalQA chain for question answering on the uploaded knowledge

`from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type=&quot;stuff&quot;, retriever=vector_store.as_retriever())
query = &quot;What did the president say about Ketanji Brown Jackson&quot;
qa.run(query)
`

Here is the response:

 The president said that Ketanji Brown Jackson is one of the nation&#x27;s top legal minds, a former top litigator in private practice, a former federal public defender, from a family of public school educators and police officers, a consensus builder, and has received a broad range of support from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.

## Conclusion

Epsilla&#x27;s integration with LangChain signifies a leap forward in the domain of question-answering systems. By leveraging the strengths of both LLMs and vector databases, this integration promises richer, more accurate, and context-aware answers. As AI continues to reshape our world, tools like LangChain, coupled with powerful vector databases like Epsilla, will be at the forefront of this transformation.

For those eager to dive deeper, LangChain&#x27;s source code and implementation details with Epsilla are available on [Google Colab](https://colab.research.google.com/drive/1asFJD_pNQbSQnbbjq-a7Q9SMzrpX-g-2?usp=sharing&amp;ref=blog.langchain.com).

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