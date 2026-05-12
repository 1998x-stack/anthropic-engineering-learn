---
title: "Query-Response System Guide With OpenLLM | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-an-intelligent-query-response-system-with-llamaindex-and-openllm-ff253a200bdf"
category: "case-studies"
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







Over the past year, Large Language Models (LLMs) like GPT-4 have not only transformed how we interact with machines but also have redefined the possibilities within the realm of natural language processing (NLP). A notable trend in this evolution is the increasing popularity of open-source LLMs like Llama 2, Falcon, OPT and Yi. Some may prefer them over their commercial counterparts in terms of accessibility, data security and privacy, customization potential, cost, and vendor dependency. Among the tools gaining increasing traction in the LLM space are OpenLLM and LlamaIndex — two powerful platforms that, when combined, unlock new use cases for building AI-driven applications.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



[OpenLLM](https://github.com/bentoml/OpenLLM) is an open-source platform for deploying and operating any open-source LLMs in production. Its flexibility and ease of use make it an ideal choice for AI application developers seeking to harness the power of LLMs. You can easily fine-tune, serve, deploy, and monitor LLMs in a wide range of creative and practical applications.

[LlamaIndex](https://github.com/run-llama/llama_index) provides a comprehensive framework for managing and retrieving private and domain-specific data. It acts as a bridge between the extensive knowledge of LLMs and the unique, contextual data needs of specific applications.

OpenLLM’s support for a diverse range of open-source LLMs and LlamaIndex’s ability to seamlessly integrate custom data sources provide great customization for developers in both communities. This combination allows them to create AI solutions that are both highly intelligent and properly tailored to specific data contexts, which is very important for query-response systems.

In this blog post, I will explain how you can leverage the combined strengths of OpenLLM and LlamaIndex to build an intelligent query-response system. This system can understand, process, and respond to queries by tapping into a custom corpus.

# Setting up the environment

The first step is to create a virtual environment in your machine, which helps prevent conflicts with other Python projects you might be working on. Let’s just call it `llamaindex-openllm` and activate it.

python -m venv llamaindex-openllm
source llamaindex-openllm/bin/activateInstall the required packages. This command installs OpenLLM with the optional `vllm` component (I will explain it later).

pip install "openllm[vllm]" llama-index llama-index-llms-openllm llama-index-embeddings-huggingfaceFor handling requests, you need to have an LLM server. Here, I use the following command to start a Llama 2 7B local server at [http://localhost:3000](http://localhost:3000). Feel free to choose any model that fits your needs. If you already have a remote LLM server, you can skip this step.

openllm start meta-llama/Llama-2-7b-chat-hf --backend vllmOpenLLM automatically selects the most suitable runtime implementation for the model. For models with vLLM support, OpenLLM uses vLLM by default. Otherwise, it falls back to PyTorch. vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. According to[ this report](https://www.anyscale.com/blog/continuous-batching-llm-inference), you can achieve 23x LLM inference throughput while reducing P50 latency using vLLM.

>

***Note****: To use the vLLM backend, you need a GPU with at least the Ampere architecture (or newer) and CUDA version 11.8. This demo uses a machine with an Ampere A100–80G GPU. If your machine has a compatible GPU, you can also choose vLLM. Otherwise, simply install the standard OpenLLM package (*`*pip install openllm*`*) in the previous command.*

# v1: Creating a simple completion service

Before building a query-response system, let’s get familiar with the integration of OpenLLM and LlamaIndex and use it to create a simple completion service.

The integration offers two APIs for interactions with LLMs:

1. `OpenLLM`: This can be used to initiate a local LLM server directly without the need for starting a separate one using commands like `openllm start`. Here’s how you can use it:

from llama_index.llms.openllm import OpenLLM
llm = OpenLLM('meta-llama/Llama-2-7b-chat-hf')2. `OpenLLMAPI`: This can be used to interact with a server hosted elsewhere, like the Llama 2 7B model I started previously.

Let’s try the `complete` endpoint and see if the Llama 2 7B model is able to tell what OpenLLM is by completing the sentence “OpenLLM is an open source tool for”.

from llama_index.llms.openllm import OpenLLMAPI

remote_llm = OpenLLMAPI(address="http://localhost:3000")

completion_response = remote_llm.complete("OpenLLM is an open source tool for", max_new_tokens=1024)
print(completion_response)Run this script and here is the output:

learning lifelong learning models. It is designed to be easy to use, even for those without extensive knowledge of machine learning. OpenLLM allows users to train, evaluate, and deploy lifelong learning models using a variety of datasets and algorithms.

OpenLLM provides a number of features that make it useful for learning lifelong learning models. Some of these features include:

1. Easy-to-use interface: OpenLLM provides an easy-to-use interface that makes it simple to train, evaluate, and deploy lifelong learning models.
2. Support for a variety of datasets: OpenLLM supports a variety of datasets, including images, text, and time-series data.
3. Support for a variety of algorithms: OpenLLM supports a variety of algorithms for lifelong learning, including neural networks, decision trees, and support vector machines.
4. Evaluation tools: OpenLLM provides a number of evaluation tools that allow users to assess the performance of their lifelong learning models.
5. Deployment tools: OpenLLM provides a number of deployment tools that allow users to deploy their lifelong learning models in a variety of environments.

OpenLLM is written in Python and is available under an open source license. It is designed to be used in a variety of settings, including research, education, and industry.

Some potential use cases for OpenLLM include:

1. Training lifelong learning models for image classification: OpenLLM could be used to train a lifelong learning model to classify images based on their content.
2. Training lifelong learning models for natural language processing: OpenLLM could be used to train a lifelong learning model to process and analyze natural language text.
3. Training lifelong learning models for time-series data: OpenLLM could be used to train a lifelong learning model to predict future values in a time-series dataset.
4. Deploying lifelong learning models in a production environment: OpenLLM could be used to deploy a lifelong learning model in a production environment, such as a recommendation system or a fraud detection system.

Overall, OpenLLM is a powerful tool for learning lifelong learning models. Its ease of use, flexibility, and support for a variety of datasets and algorithms make it a valuable resource for researchers and practitioners in a variety of fields.Obviously, the model couldn’t correctly explain OpenLLM with some hallucinations 🤣. Nevertheless, the code works well as the server outputs a response for the request. This is a good start as we proceed with building our system.

# v2: Enhancing with a query-response system

The initial version revealed a key limitation: the model’s lack of specific knowledge about OpenLLM. One solution is to feed the model with domain-specific information, allowing it to learn and respond according to topic-specific queries. This is where LlamaIndex comes into play, enabling you to build a local knowledge base with pertinent information. Specifically, you create a directory (for example, `data`) and build an index for all the documents in the folder.

Create a folder and let’s import the GitHub README file of OpenLLM into the folder:

mkdir data
cd data
wget https://github.com/bentoml/OpenLLM/blob/main/README.mdGo back to the previous directory and create a script called `starter.py` like the following:

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms.openllm import OpenLLMAPI
from llama_index.core.node_parser import SentenceSplitter

# Change the address to your OpenLLM server
llm = OpenLLMAPI(address="http://localhost:3000")

# Break down the document into manageable chunks (each of size 1024 characters, with a 20-character overlap)
text_splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=20)

# Create a ServiceContext with the custom model and all the configurations
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model="local",
    text_splitter=text_splitter,
    context_window=8192,
    num_output=4096,
)

# Load documents from the data directory
documents = SimpleDirectoryReader("data").load_data()

# Build an index over the documents using the customized LLM in the ServiceContext
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Query your data using the built index
query_engine = index.as_query_engine()
response = query_engine.query("What is OpenLLM?")
print(response)To improve the quality of your response, I recommend you define a `SentenceSplitter` to provide finer control over the input processing, leading to better output quality.

In addition, you can set `streaming=True` to stream your response:

query_engine = index.as_query_engine(streaming=True)
response = query_engine.query("What is OpenLLM?")
response.print_response_stream()Your directory structure should look like this now:

├── starter.py
└── data
    └── README.mdRun `starter.py` to test the query-response system. The output should be consistent with the content of the OpenLLM README. Here is the response I received:

>

OpenLLM is an open-source platform for deploying and managing large language models (LLMs) in a variety of environments, including on-premises, cloud, and edge devices. It provides a comprehensive suite of tools and features for fine-tuning, serving, deploying, and monitoring LLMs, simplifying the end-to-end deployment workflow for LLMs.

# Conclusion

The exploration in this article underscores the importance of customizing AI tools to fit specific needs. By using OpenLLM for flexible deployment of LLMs and LlamaIndex for data management, I have demonstrated how to create an AI-powered system. It not only understands and processes queries but also delivers responses based on a unique knowledge base. I hope this blog post has inspired you to explore more capabilities and use cases of OpenLLM and LlamaIndex. Happy coding! ⌨️