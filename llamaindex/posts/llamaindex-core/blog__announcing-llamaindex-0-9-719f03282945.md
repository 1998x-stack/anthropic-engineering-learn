---
title: "LlamaIndex 0.9 Release: Ingestion Pipeline &amp; Caching | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/announcing-llamaindex-0-9-719f03282945"
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



   1



Our hard-working team is delighted to announce our latest major release, LlamaIndex 0.9! You can get it right now:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



`pip install --upgrade llama_index`

In LlamaIndex v0.9, we are taking the time to refine several key aspects of the user experience, including token counting, text splitting, and more!

As part of this, there are some new features and minor changes to current usage that developers should be aware of:

- New `IngestionPipline` concept for ingesting and transforming data
- Data ingestion and transforms are now automatically cached
- Updated interface for node parsing/text splitting/metadata extraction modules
- Changes to the default tokenizer, as well as customizing the tokenizer
- Packaging/Installation changes with PyPi (reduced bloat, new install options)
- More predictable and consistent import paths
- Plus, in beta: MultiModal RAG Modules for handling text and images!

Have questions or concerns? You can [report an issue](https://github.com/run-llama/llama_index/issues) on GitHub or [ask a question on our Discord](https://discord.com/invite/eN6D2HQ4aX)!

Read on for more details on our new features and changes.

# IngestionPipeline — New abstraction for purely ingesting data

Sometimes, all you want is to ingest and embed nodes from data sources, for instance if your application allows users to upload new data. New in LlamaIndex V0.9 is the concept of an `IngestionPipepline` .

An `IngestionPipeline` uses a new concept of `Transformations` that are applied to input data.

What is a `Transformation` though? It could be a:

- text splitter
- node parser
- metadata extractor
- embeddings model

Here’s a quick example of the basic usage pattern:

from llama_index import Document
from llama_index.embeddings import OpenAIEmbedding
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import TitleExtractor
from llama_index.ingestion import IngestionPipeline, IngestionCache

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)
nodes = pipeline.run(documents=[Document.example()])

# Transformation Caching

Each time you run the same `IngestionPipeline` object, it caches a hash of the input nodes + transformations and the output of that transformation for each transformation in the pipeline.

In subsequent runs, if there is a cache hit, that transformation will be skipped and the cached result will be used instead. The greatly speeds up duplicate runs, and can help improve iteration times when deciding which transformations to use.

Here’s an example with a saving and loading a local cache:

from llama_index import Document
from llama_index.embeddings import OpenAIEmbedding
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import TitleExtractor
from llama_index.ingestion import IngestionPipeline, IngestionCache

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ]
)
# will only execute full pipeline once
nodes = pipeline.run(documents=[Document.example()])
nodes = pipeline.run(documents=[Document.example()])
# save and load
pipeline.cache.persist("./test_cache.json")
new_cache = IngestionCache.from_persist_path("./test_cache.json")
new_pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TitleExtractor(),
    ],
    cache=new_cache,
)
# will run instantly due to the cache
nodes = pipeline.run(documents=[Document.example()])And here’s another example using Redis as a cache and Qdrant as a vector store. Running this will directly insert the nodes into your vector store and cache each transformation step in Redis.

from llama_index import Document
from llama_index.embeddings import OpenAIEmbedding
from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import TitleExtractor
from llama_index.ingestion import IngestionPipeline, IngestionCache
from llama_index.ingestion.cache import RedisCache
from llama_index.vector_stores.qdrant import QdrantVectorStore

import qdrant_client
client = qdrant_client.QdrantClient(location=":memory:")
vector_store = QdrantVectorStore(client=client, collection_name="test_store")
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TitleExtractor(),
        OpenAIEmbedding(),
    ],
    cache=IngestionCache(cache=RedisCache(), collection="test_cache"),
    vector_store=vector_store,
)
# Ingest directly into a vector db
pipeline.run(documents=[Document.example()])
# Create your index
from llama_index import VectorStoreIndex
index = VectorStoreIndex.from_vector_store(vector_store)

# Custom Transformations

Implementing custom transformations is easy! Let’s add a transform to remove special characters from the text before calling embeddings.

The only real requirement for transformations is that they must accept a list of nodes and return a list of nodes.

import re
from llama_index import Document
from llama_index.embeddings import OpenAIEmbedding
from llama_index.text_splitter import SentenceSplitter
from llama_index.ingestion import IngestionPipeline
from llama_index.schema import TransformComponent

class TextCleaner(TransformComponent):
  def __call__(self, nodes, **kwargs):
    for node in nodes:
      node.text = re.sub(r'[^0-9A-Za-z ]', "", node.text)
    return nodes
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=25, chunk_overlap=0),
        TextCleaner(),
        OpenAIEmbedding(),
    ],
)
nodes = pipeline.run(documents=[Document.example()])

# Node Parsing/Text Splitting — Flattened and Simplified Interface

We’ve made our interface for parsing and splitting text a lot cleaner.

# Before:

from llama_index.node_parser import SimpleNodeParser
from llama_index.node_parser.extractors import (
	MetadataExtractor, TitleExtractor
)
from llama_index.text_splitter import SentenceSplitter

node_parser = SimpleNodeParser(
  text_splitter=SentenceSplitter(chunk_size=512),
  metadata_extractor=MetadataExtractor(
  extractors=[TitleExtractor()]
 ),
)
nodes = node_parser.get_nodes_from_documents(documents)

# After:

from llama_index.text_splitter import SentenceSplitter
from llama_index.extractors import TitleExtractor

node_parser = SentenceSplitter(chunk_size=512)
extractor = TitleExtractor()

# use transforms directly
nodes = node_parser(documents)
nodes = extractor(nodes)Previously, the `NodeParser` object in LlamaIndex had become extremely bloated, holding both text splitters and metadata extractors, which caused both pains for users when changing these components, and pains for us trying to maintain and develop them.

In V0.9, we have **flattened** the entire interface into a single `TransformComponent` abstraction, so that these transformations are easier to setup, use, and customize.

We’ve done our best to minimize the impacts on users, but the main thing to note is that `**SimpleNodeParser**`** has been removed**, and other node parsers and text splitters have been elevated to have the same features, just with different parsing and splitting techniques.

Any old imports of `SimpleNodeParser` will redirect to the most equivalent module, `SentenceSplitter`.

Furthermore, the wrapper object `**MetadataExtractor**`** has been removed**, in favour of using extractors directly.

Full documentation for all this can be found below:

- [Node Parsers and Text Splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules.html)
- [Metadata Extractors](https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction.html)

# Tokenization and Token Counting — Improved defaults and Customization

A big pain point in LlamaIndex previously was tokenization. Many components used a non-configurable `gpt2` tokenizer for token counting, causing headaches for users using non-OpenAI models, or even some hacky fixes [like this](https://github.com/run-llama/llama_index/blob/336a88db4f13cfc598c473f9b5a3bc073b5d7ef4/llama_index/indices/prompt_helper.py#L119) for OpenAI models too!

In LlamaIndex V0.9, this **global tokenizer is now configurable and defaults to the CL100K tokenizer** to match our default GPT-3.5 LLM.

The single requirement for a tokenizer is that it is a callable function, that takes a string, and returns a list.

Some examples of configuring this are below:

from llama_index import set_global_tokenizer

# tiktoken
import tiktoken
set_global_tokenizer(
  tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
# huggingface
from transformers import AutoTokenizer
set_global_tokenizer(
  AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta").encode
)Furthermore, the `TokenCountingHandler` has gotten an upgrade with better token counting, as well as using token counts from API responses directly when available.

# Packaging — Reduced Bloat

In an effort to modernize the packaging of LlamaIndex, V0.9 also comes with changes to installation.

The biggest change here is that `LangChain` is now an optional package, and will not be installed by default.

To install `LangChain` as part of your llama-index installation you can follow the example below. There are also other installation options depending on your needs, and we are welcoming further contributions to the extras in the future.

# installs langchain
pip install llama-index[langchain]

# installs tools needed for running local models
pip install llama-index[local_models]

# installs tools needed for postgres
pip install llama-index[postgres]

# combinations!
pip isntall llama-index[local_models,postgres]**If you were previously importing **`**langchain**`** modules** in your code, please update your project packaging requirements appropriately.

# Import Paths — More Consistent and Predictable

We are making two changes to our import paths:

- We’ve removed uncommonly used imports from the root level to make importing `llama_index` faster
- We now have a consistent policy for making “user-facing” concepts import-able at level-1 modules.

from llama_index.llms import OpenAI, ...
from llama_index.embeddings import OpenAIEmbedding, ...
from llama_index.prompts import PromptTemplate, ...
from llama_index.readers import SimpleDirectoryReader, ...
from llama_index.text_splitter import SentenceSplitter, ...
from llama_index.extractors import TitleExtractor, ...
from llama_index.vector_stores import SimpleVectorStore, ...We still expose some of the most commonly used modules at the root level.

from llama_index import SimpleDirectoryReader, VectorStoreIndex, ...

# MultiModal RAG

Given the recent announcements of the GPT-4V API, multi-modal use cases are more accessible than ever before.

To help users use these features, we’ve started to introduce a number of new modules to help support use-cases for MultiModal RAG:

- MultiModal LLMs (GPT-4V, Llava, Fuyu, etc.)
- MultiModal Embeddings (i.e clip) for join image-text embedding/retrieval
- MultiModal RAG, combining indexes and query engines

Our documentation has a [full guide to multi-modal retrieval](https://docs.llamaindex.ai/en/latest/examples/multi_modal/gpt4v_multi_modal_retrieval.html).

# Thanks for all your support!

As an open-source project we couldn’t exist without our [hundreds of contributors](https://github.com/run-llama/llama_index/graphs/contributors). We are so grateful for them and the support of the hundreds of thousands of LlamaIndex users around the world. See you on the Discord!