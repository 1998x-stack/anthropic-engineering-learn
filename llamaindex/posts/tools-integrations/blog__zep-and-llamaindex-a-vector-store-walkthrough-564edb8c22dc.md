---
title: "Zep Vector Store Guide With LlamaIndex | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/zep-and-llamaindex-a-vector-store-walkthrough-564edb8c22dc"
category: "tools-integrations"
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







Editor’s Note: This article was written by [Daniel](https://twitter.com/danielchalef) at Zep for the LlamaIndex blog.

Zep is a [long-term memory store for LLM applications](https://www.getzep.com/). With Zep, developers can easily add relevant documents, chat history memory &amp; rich user data to LLM app prompts. Document and chat history storage, embedding, enrichment, and more are taken care of by the Zep service.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In this article, we demonstrate how to use Zep’s new Document Vector Store with the (also new) ZepVectorStore for LlamaIndex.

# Installing Zep and some important concepts

[Zep is open source](https://github.com/getzep/zep) and may be [installed via Docker](https://docs.getzep.com/deployment/quickstart/), or to Kubernetes and hosting platforms such as Render. SDKs are available for Python and TypeScript, and frameworks such as LangChain and LlamaIndex ship with support for Zep.

Zep stores documents in Collections, with the document text, embeddings, and metadata all colocated. This enables hybrid semantic search over a collection, with results filtered by JSONPath queries against document metadata. When using Zep with LlamaIndex, LlamaIndex filters are translated for use by Zep.

A document or document chunk is equivalent to a LlamaIndex TextNode or NodeWithEmbedding.

Collections can be optionally set to automatically embed texts using a service such as OpenAI or locally using an embedding model of your choice. However, when using Zep with LlamaIndex, we rely on LlamaIndex’s integrations with embedded services and libraries.

# Creating a ZepVectorStore and Document Collection

You will need to have [installed Zep](https://docs.getzep.com/) and have your API URL and, optionally, authentication key handy.

from llama_index.vector_stores import ZepVectorStore
zep_api_url = "http://localhost:8000"
zep_api_key = "&amp;lt;optional_jwt_token&amp;gt;"
collection_name = "babbage" # The name of a new or existing collection
embedding_dimensions = 1536 # the dimensions of the embedding model you intend to use
vector_store = ZepVectorStore(
  api_url=zep_api_url,
  api_key=zep_api_key,
  collection_name=collection_name,
  embedding_dimensions=embedding_dimensions
)The collection name is a unique identifier for your vector index and should only contain alphanumeric characters. If the collection does not exist, Zep will automatically create one for you.

# Creating and populating an Index

Below we’ll use a common LlamaIndex pattern for loading content and adding it to an index. After loading the text data, we create a StorageContext backed by the ZepVectorStore.

We then create the index using our loaded documents and Zep-backed storage context.

from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext

documents = SimpleDirectoryReader("./babbages_calculating_engine/").load_data()

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

query = "the sun and stars"

query_engine = index.as_query_engine()
response = query_engine.query(query)

print(str(response))But one of the most signal examples of this kind, of which we are aware, is related by Mr Baily. The catalogue of stars published by the Astronomical Society was computed by two separate and independent persons, and was afterwards compared and examined with great care and attention by Mr Stratford. On examining this catalogue, and recalculating a portion of it, Mr Baily discovered an error in the case of the starFinally, we run a simple text query against the index and print the resulting node’s text.

# Hybrid search with metadata filters

As mentioned above, Zep also supports associating rich metadata with documents. This metadata can be an arbitrarily deep JSON structure. When working with LlamaIndex, we currently support filtering on top-level keys in the map.

The code below demonstrates running a vector search over an index and filtering on metadata using LlamaIndex’s MetadataFilters. We print the result and the normalized cosine similarity for the matching result.

from llama_index.schema import TextNode
from llama_index.vector_stores.types import ExactMatchFilter, MetadataFilters

nodes = [
   TextNode(
       text="Not aware that tables of these squares existed, Bouvard, who calculated the tides for Laplace, underwent the labour of calculating the square of each individual sine in every case in which it occurred.",
       metadata={
           "topic": "math",
           "entities": "laplace",
       },
   ),
   TextNode(
       text="Within the limits of the lunar orbit there are not less than one thousand stars, which are so situated as to be in the moon's path, and therefore to exhibit, at some period or other, those desirable occultations.",
       metadata={
           "topic": "astronomy",
           "entities": "moon",
       },
   ),
]

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)

filters = MetadataFilters(filters=[ExactMatchFilter(key="topic", value="astronomy")])

retriever = index.as_retriever(filters=filters)
result = retriever.retrieve("What is the structure of our galaxy?")

for r in result:
   print("\n", r.node.text, r.score)Within the limits of the lunar orbit there are not less than one thousand stars, which are so situated as to be in the moon's path, and therefore to exhibit, at some period or other, those desirable occultations.  0.6456785674

# Summing it up

Zep offers a single API for vector search over documents and chat history, allowing developers to populate prompts with both forms of long-term memory. LlamaIndex makes it extremely easy to populate Zep with content from a broad set of documents and data sources and query these sources when building prompts and other functionality for LLM apps.

# Next Steps

- Read the [Zep Quick Start Guide](https://docs.getzep.com/deployment/quickstart/)
- [Zep and LlamaIndex Walkthrough Notebook](https://github.com/jerryjliu/llama_index/tree/main/docs/examples/vector_stores/ZepIndexDemo.ipynb)
- [Getting Started with LllamaIndex](https://gpt-index.readthedocs.io/en/stable/index.html)