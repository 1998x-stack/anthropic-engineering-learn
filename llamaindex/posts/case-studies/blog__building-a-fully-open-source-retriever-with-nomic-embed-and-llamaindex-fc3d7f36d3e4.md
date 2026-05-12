---
title: "Open Source Retriever Guide: Nomic Embed + LlamaIndex | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-a-fully-open-source-retriever-with-nomic-embed-and-llamaindex-fc3d7f36d3e4"
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



   51



# What is a Retriever?

Recently, retrieval augmented generation (RAG) has enabled language models to reduce hallucinations, improve response quality, and maintain up-to-date knowledge of the world *without* requiring retraining of the model itself. This is done by equipping a language model with a *retriever* and a *database.* At inference time, a RAG system uses the retriever to select relevant documents from the database, and passes them to the language model context window.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Today, the most popular type of retriever is based on an embedding model. This embedding model converts all of the documents in the database to a vector representation. Then, at inference time, it converts the query to a vector representation, and retrieves the most similar documents to the query vector from the database.

In this post, we are going to show you how to build a fully open source retriever using LlamaIndex and Nomic Embed, the first fully open source embedding model to exceed OpenAI Ada performance on both short and long context benchmarks.

# Why Open Source?

As AI becomes deployed in increasingly high impact domains, such as defense, medicine, and finance, end-to-end auditability of the entire system becomes a key component of safe AI deployment. Unfortunately, the closed source embedding models used in most RAG systems today have deliberately obfuscated training protocols and cannot be audited.

Further, as organizations adopting AI begin to mature, reliance on closed source embedding models will result in vendor lock-in and a limited ability to modify the embedding model to suit the needs of the business.

Luckily, fully open source embedding models like Nomic Embed offer end-to-end auditability of the training process as well as a strong basis for further improvements and modifications of the model.

# How To

To build an open source retriever with LlamaIndex and Nomic Embed, we will start by importing the relevant libraries

from llama_index.embeddings import NomicEmbedding
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
)Next, we need to download some data for our database. For this example, we are going to use an essay by Paul Graham, which we download from [here](https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt) and place into a directory named ./data/paul_graham.

Now, it’s time to get the vectors for the documents in our database. To do this, we are going to use the LlamaIndex SimpleDirectoryReader and Nomic’s hosted inference service. You’ll have to replace &lt;NOMIC_API_KEY&gt; with your Nomic API key, which you can get after signing up for Nomic Atlas [here](https://atlas.nomic.ai/).

documents = SimpleDirectoryReader("./data/paul_graham/").load_data()
nomic_api_key = "&amp;lt;NOMIC_API_KEY&amp;gt;"
embed_model = NomicEmbedding(
    api_key=nomic_api_key,
    model_name="nomic-embed-text-v1",
    task_type="search_document"
)
service_context = ServiceContext.from_defaults(
    embed_model=embed_model, chunk_size=1024,
)
index = VectorStoreIndex.from_documents(
    documents=documents, service_context=service_context, show_progress=True
)Notice that we set task_type to search_document in NomicEmbedding. Nomic Embed supports many different types of tasks, and search_document is optimized for building representations of documents for RAG databases.

Once our database is set up, we are ready to build our retriever. Using LlamaIndex, this is as simple as a few lines of python:

embed_model = NomicEmbedding(
    api_key=nomic_api_key,
    model_name="nomic-embed-text-v1",
    task_type="search_query"
)

service_context = ServiceContext.from_defaults(
    embed_model=embed_model
)

search_query_retriever = index.as_retriever(service_context=service_context, similarity_top_k=1)Again, notice that we are using a new NomicEmbedding model with task_type set to search_query. This task type is optimized for embedding queries for search over a retrieval database.

Finally, we can use our retriever to surface relevant documents given user queries! As an example:

retrieved_nodes_nomic = retriever_nomic.retrieve(
    "What software did Paul write?"
)returns a document that describes Paul’s first programs:

Node ID: 380fbb0e-6fc1-41de-a4f6-3f22cd508df3
Similarity: 0.6087318771843091
Text: What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.

I was puzzled by the 1401. I couldn't figure out what to do with it. And in retrospect there's not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn't have any data stored on punched cards. The only other option was to do things that didn't rely on any input, like calculate approximations of pi, but I didn't know enough math to do anything interesting of that type. So I'm not surprised I can't remember any programs I wrote, because they can't have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn't. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager's expression made clear.

With microcomputers, everything changed.

# Conclusion &amp; Next Steps

In this post, we showed you how to build a fully open source retriever using Nomic Embed and LlamaIndex. If you want to dive deeper, you can find the source code for Nomic Embed [here](https://github.com/nomic-ai/contrastors). You can also use Nomic [Atlas](https://atlas.nomic.ai/) to visualize your retrieval database, and [LlamaIndex](https://www.llamaindex.ai/) to connect it to a generative model for full RAG.