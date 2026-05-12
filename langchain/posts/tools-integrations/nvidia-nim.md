---
title: "LangChain Integrates NVIDIA NIM for GPU-optimized LLM Inference in RAG"
author: "LangChain Accounts"
date: "2024-03-18"
url: "https://www.langchain.com/blog/nvidia-nim"
---

PartnerCompany Announcements

# LangChain Integrates NVIDIA NIM for GPU-optimized LLM Inference in RAG

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 18, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0011082f68faaecfcdb_NVIDIA-3.png)Roughly a year and a half ago, OpenAI launched ChatGPT and the generative AI era really kicked off. Since then we’ve seen rapid growth and widespread adoption by all types of industries and all types of enterprises. As enterprises turn their attention from prototyping LLM applications to productionizing them, they often want to turn from third-party model services to self-hosted solutions. We’ve seen many folks struggle with this, and that’s why LangChain is so excited to integrate the new [NVIDIA NIM](https://nvidianews.nvidia.com/news/generative-ai-microservices-for-developers?ref=blog.langchain.com) inference microservices.

## What is NVIDIA NIM?

[NVIDIA NIM](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/?ref=blog.langchain.com) is a set of easy-to-use microservices designed to accelerate the deployment of generative AI across enterprises. This versatile runtime supports a broad spectrum of AI models—from open-source community models to NVIDIA AI foundation models, as well as custom AI models. Leveraging industry-standard APIs, developers can quickly build enterprise-grade AI applications with just a few lines of code. Built on robust foundations including inference engines like [NVIDIA Triton Inference Server](https://www.nvidia.com/en-us/ai-data-science/products/triton-inference-server/?ref=blog.langchain.com), NVIDIA TensorRT, [NVIDIA TensorRT-LLM](https://developer.nvidia.com/blog/optimizing-inference-on-llms-with-tensorrt-llm-now-publicly-available/?ref=blog.langchain.com), and PyTorch, NIM is engineered to facilitate seamless AI inferencing at scale, ensuring that you can deploy AI applications anywhere with confidence. Whether working on premises or in the cloud, NIM is the fastest way to achieve accelerated generative AI inference at scale.

## Why are we excited about NVIDIA NIM?

There are a few reasons we are excited about NIM.

First, the big one: It’s all self-hosted. This means any data you send to NVIDIA-based models will never leave your premises. This is particularly exciting for RAG-based applications where you are often passing in sensitive data.

Second: It comes with several prebuilt containers out of the box. This makes it so that you can choose from the latest generative AI models without having to do much work.

Third: It’s scalable. It’s one thing to run models locally on your laptop. It’s another to host them as a service with the same reliability and uptime as you get from a managed service provider. Luckily, NIM is taking on this challenge for you.

## How can I get access to NVIDIA NIM?

Getting started with NIM is straightforward. Within the NVIDIA API catalog, developers can access a wide range of AI models to build and deploy generative AI applications. NIM is available as part of [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/?ref=blog.langchain.com), an end-to-end, cloud-native software platform that streamlines the development and deployment of production-grade AI applications. Check out [this blog](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/?ref=blog.langchain.com) for a step-by-step guide on how to get started.

## How can I use NVIDIA NIM with LangChain?

Finally, for the fun stuff. We’ve added a new integration package that supports NIM. To get started with the integration, you will need to install our dedicated integration package:

`pip install langchain_nvidia_ai_endpoints`

After that, you can import models like:

`from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA`

## Integration Example

For the rest of this document we will focus on building an example application. If you are more of a visual learner, you can find a video walkthrough [here](https://www.loom.com/share/d92b3cb9d86c4787ada2adb148e9a96b?ref=blog.langchain.com).

We will build a RAG application over part of the LangSmith documentation. To make it a little more interesting we will use an advanced retrieval method: hypothetical document embeddings (HyDE). The motivation for HyDE is that a search query may not be in a similar embedding space as the documents we are retrieving over. In order to fix this, we can use an LLM to generate a hypothetical document and then retrieve documents similar to that hypothetical document.

To get started, we will need to install some other packages.

`pip install langchain-community langchain-text-splitters faiss-cpu`

We will then load some data we want to do RAG over - the LangSmith docs!

`from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(&quot;https://docs.smith.langchain.com/user_guide&quot;)

docs = loader.load()`

Before indexing the documents, we can then initialize our embedding model.

`from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
embeddings = NVIDIAEmbeddings()`

We can now perform the indexing step, using the FAISS vectorstore.

`from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)
retriever = vector.as_retriever()`

We can then initialize our LLM:

`from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser

model = ChatNVIDIA(model=&quot;mistral_7b&quot;)
`

Now, we will create our hypothetical document generator. This chain consists of a prompt, LLM, and a simple output parser.

`hyde_template = &quot;&quot;&quot;Even if you do not know the full answer, generate a one-paragraph hypothetical answer to the below question:

{question}&quot;&quot;&quot;
hyde_prompt = ChatPromptTemplate.from_template(hyde_template)
hyde_query_transformer = hyde_prompt | model | StrOutputParser()`

We can then wrap this chain and the original retriever into a new chain:

`from langchain_core.runnables import chain

@chain
def hyde_retriever(question):
    hypothetical_document = hyde_query_transformer.invoke({&quot;question&quot;: question})
    return retriever.invoke(hypothetical_document)`

We can then create the chain that will take the retrieved documents and the question to produce a final answer:

`template = &quot;&quot;&quot;Answer the question based only on the following context:
{context}

Question: {question}
&quot;&quot;&quot;
prompt = ChatPromptTemplate.from_template(template)
answer_chain = prompt | model | StrOutputParser()`

Finally, we can combine this with the hypothetical document retriever to create a final chain:

`@chain
def final_chain(question):
    documents = hyde_retriever.invoke(question)
    for s in answer_chain.stream({&quot;question&quot;: question, &quot;context&quot;: documents}):
        yield s`

Notice that we yield back tokens so that we can stream this final chain! Let’s give it a go:

`for s in final_chain.stream(&quot;how can langsmith help with testing&quot;):
    print(s, end=&quot;&quot;)`

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)