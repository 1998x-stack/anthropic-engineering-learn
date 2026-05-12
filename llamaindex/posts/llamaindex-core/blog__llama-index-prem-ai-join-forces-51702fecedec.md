---
title: "LlamaIndex + Prem AI Integration Guide For Private LLMs | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llama-index-prem-ai-join-forces-51702fecedec"
category: "llamaindex-core"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







**Co-authors:** Simone Giacomelli (co-founder at Prem), Jerry Liu (co-founder/CEO at LlamaIndex)

We’re pleased to share the successful integration of Prem App and Llama Index, a union that brings a new level of privacy to AI development. Prem’s self-hosting AI models and Llama’s versatile data framework enhances the ability to build AI applications in a customizable and flexible manner.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



## Integration Details

By combining Prem’s self-hosting AI models with Llama Index’s data framework, developers can now connect custom data sources to large language models easily. This simplifies the process of data ingestion, indexing, and querying, streamlining the overall AI development cycle.

## Getting Started

To leverage this integration, simply download the Prem App and connect your data sources through the Llama Index platform. This allows you to self-host your AI models with Prem App and utilize Llama Index’s capabilities to manage your data efficiently. This integration, therefore, significantly boosts AI application development, giving developers greater control and flexibility over their projects.

# Getting Started

## Install Prem

You can run Prem in two different ways:

- MacOS: go to [https://premai.io](https://premai.io) and download Prem App.
- Server: run the installer script: `wget -q &lt;https://get.prem.ninja/install.sh&gt; -O install.sh; sudo bash ./install.sh`

## Run the services in the GUI

When the UI is up and running, you can see all the services available. With just one click you can download the service you are interested in. In the background, the docker image associated with the service will be downloaded based on your hardware requirements.

![](/blog/images/1*UP-b2xFiA2q7WwJNGDuv2A.gif)

While waiting for the download to be completed, read more about the service, in the detail view. Just click on the card and you will be redirected to the service page. Each service page is packaged with some general info as well as complete documentation giving more details into the model exposed. When the download has been completed, just click on Open and the service will start. You can interact with the service from the playground or from APIs.

![](/blog/images/1*4C2QF5rzVNs17v6xMpXUQA.gif)

You can check the port on which the service is running from the service detail view.

![](/blog/images/1*BfMngT11QbMp5S3kLlgu1Q.gif)

# Start Building Your App

In this quick tutorial will show you how to build a simple Talk to your Data use case using Prem landing page content.

In order to achieve that we will need to run three services:

- Redis: we will use Redis as a vector store to store the embeddings.
- Vicuna 7B Q4: we will use Vicuna in order to generate a proper response for the user based on the most similar document we get using Redis similarity search
- All MiniLM L6 V2: we will use sentence transformers in order to generate the embeddings out of our documents.

If all the services necessary are running, you will see a similar interface as the one beyond.

![](/blog/images/1*0sBCH9iYZlIv1lC7qrOP2g.png)

You can now start integrating the services using Llama Index library. In the following code snippets, we will show you how you can build a simple talk to your data use case using Prem and Llama Index.

- Import all necessary dependencies and assign a random string to `OPENAI_API_KEY` environment variable.

import os

from llama_index.vector_stores import RedisVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import ListIndex, LLMPredictor, Document

from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

from llama_index import LangchainEmbedding, ServiceContext

os.environ["OPENAI_API_KEY"] = "random-string"2. Load the Data / Create some Documents. In this example, I am using Prem landing page content creating manually some documents.

doc1 = Document(text="Prem is an easy to use open source AI platform. With Prem you can quickly build privacy preserving AI applications.")
doc2 = Document(text="""
Prem App

An intuitive desktop application designed to effortlessly deploy and self-host Open-Source AI models without exposing sensitive data to third-party.

""")
doc3 = Document(text="""
Prem Benefits

Effortless Integration
Seamlessly implement machine learning models with the user-friendly interface of OpenAI's API.

Ready for the Real World
Bypass the complexities of inference optimizations. Prem's got you covered.

Rapid Iterations, Instant Results
Develop, test, and deploy your models in just minutes.

Privacy Above All
Your keys, your models. We ensure end-to-end encryption.

Comprehensive Documentation
Dive into our rich resources and learn how to make the most of Prem.

Preserve Your Anonymity
Make payments with Bitcoin and Cryptocurrency. It's a permissionless infrastructure, designed for you.
""")3. Instantiate the LLMs connecting to the running services.

# Instantiate a llm predictor using Langchain pointing to vicuna-7b-q4 service
llm_predictor = LLMPredictor(llm=ChatOpenAI(openai_api_base="http://localhost:8111/api/v1", max_tokens=128))

# Instantiate the embeddings object using Langchain pointing to all-MiniLM-L6-v2 service
embeddings = OpenAIEmbeddings(openai_api_base="http://localhost:8444/api/v1")
embed_model = LangchainEmbedding(embeddings)

# define a service context using the embeddings and llm defined above.
service_context = ServiceContext.from_defaults(embed_model=embed_model, llm_predictor=llm_predictor)4. Configure the Vector Store

# instantiate the vectorstore connecting to Redis service
vector_store = RedisVectorStore(
    index_name="prem_landing",
    index_prefix="llama",
    redis_url="redis://localhost:6379",
    overwrite=True
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)5. Index the documents

index = ListIndex.from_documents([doc1, doc2, doc3], storage_context=storage_context)6. Perform an example query

query_engine = index.as_query_engine(
    retriever_mode="embedding",
    verbose=True,
    service_context=service_context
)
response = query_engine.query("What are Prem benefits?")
print(response)The benefits of using Prem include: Effortless Integration, Ready for the Real World, Rapid Iterations, Instant Results, Privacy Above All, Comprehensive Documentation, Preserve Your Anonymity, and an intuitive desktop application designed to effortlessly deploy and self-host Open-Source AI models without exposing sensitive data to third-party.And Done 🎉 You are now using Prem with Llama Index.

# More Information

Check out our documentation at: [https://github.com/premai-io/prem-app](https://github.com/premai-io/prem-app)

Check out a simple talk to your data notebook with Llama Index: [https://github.com/premAI-io/prem-daemon/blob/main/resources/notebooks/llama_index.ipynb](https://github.com/premAI-io/prem-daemon/blob/main/resources/notebooks/llama_index.ipynb)

Checkout our YouTube tutorials

- Getting Started with Prem: [https://www.youtube.com/watch?v=XixH46Ysl5A](https://www.youtube.com/watch?v=XixH46Ysl5A)
- Deploy Prem in your Paperspace instance: [https://www.youtube.com/watch?v=aW8t6wouwx0](https://www.youtube.com/watch?v=aW8t6wouwx0)

# Join Us

Our partnership is based on a shared understanding that the future of AI is open, composable, and privacy-centric.

[Join us on this journey](https://discord.com/invite/kpKk6vYVAn)!