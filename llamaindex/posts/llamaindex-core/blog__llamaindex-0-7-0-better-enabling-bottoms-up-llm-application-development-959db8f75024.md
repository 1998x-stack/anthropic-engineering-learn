---
title: "LlamaIndex 0.7.0 Release: Key Updates Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-0-7-0-better-enabling-bottoms-up-llm-application-development-959db8f75024"
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







A few months ago, we launched LlamaIndex 0.6.0, which included a massive rewrite of our codebase to make our library more modular, customizable, and accessible to both beginner and advanced users:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)


- We created modular storage abstractions (data, indices), and compute abstractions (retrievers, query engines).
- We created a lower-level API where users could use our modules (retrievers, query engines) independently and customize it as part of a larger system.

Today, we’re excited to launch LlamaIndex 0.7.0. Our latest release continues the theme of improving modularity/customizability at the lower level to enable **bottoms-up development of LLM applications over your data.** You now have even more control over using key abstractions: the LLM, our response synthesizer, and our Document and Node objects.

- We’ve created **standalone LLM abstractions** (OpenAI, HuggingFace, PaLM).
- We’ve made our **response synthesis module an independent module** you can use completely independently of the rest of our abstractions — get rid of the prompt boilerplate of trying to figure out how to fit context within a context window.
- We’ve added **extensive metadata management capabilities** to our Document/Node objects — now you have complete control over context you decide to inject into your documents.

Below, we describe each section more in detail. We also outline a full list of breaking changes at the bottom.

# Standalone LLM Abstractions

We’ve created standalone LLM abstractions for OpenAI, HuggingFace, and PaLM. These abstractions can be used on their own, or as part of an existing LlamaIndex system (query engines, retrievers).

## High-level Motivation

We did this for multiple reasons:

- Cleaner abstractions in the codebase. Before, our `LLMPredictor` class had a ton of leaky abstractions with the underlying LangChain LLM class. This made our LLM abstractions hard to reason about, and hard to customize.
- Slightly cleaner dev UX. Before, if you wanted to customize the default LLM (for instance, use “text-davinci-003”, you had to import the correct LangChain class, wrap it in our LLMPredictor, and then pass it to ServiceContext. Now it’s easy to just import our LLM abstraction (which is natively documented with our docs) and plug it into ServiceContext. Of course, you can still use LangChain’s LLMs if you wish.
- Conducive to bottoms-up development: it makes sense to play around with these LLM modules independently before plugging them in as part of a larger system. It’s reflective of our bigger push in 0.7.0 to let users compose their own workflows.

## **Using on their own**

Our LLM abstractions support both `complete` and `chat` endpoints. The main difference is that `complete` is designed to take in a simple string input, and output a `CompletionResponse` (containing text output + additional fields). `chat` takes in a `ChatMessage` and outputs a `ChatResponse` (containing a chat message + additional fields).

These LLM endpoints also natively support streaming via `stream_complete` and `stream_chat`.

Here’s on how you can use the LLM abstractions on their own:

from llama_index.llms import OpenAI

# using complete endpoint
resp = OpenAI().complete('Paul Graham is ')
print(resp)
# get raw object
resp_raw = resp.raw
# using chat endpoint
from llama_index.llms import ChatMessage, OpenAI
messages = [
    ChatMessage(role='system', content='You are a pirate with a colorful personality'),
    ChatMessage(role='user', content='What is your name')
]
resp = OpenAI().chat(messages)
print(resp)
# get raw object
resp_raw = resp.raw
# using streaming endpoint
from llama_index.llms import OpenAI
llm = OpenAI()
resp = llm.stream_complete('Paul Graham is ')
for delta in resp:
    print(delta, end='')Here’s how you can use the LLM abstractions as part of an overall LlamaIndex system.

from llama_index.llms import OpenAI
from llama_index.indices.service_context import ServiceContext
from llama_index import VectorStoreIndex

llm = OpenAI(model='gpt-3.5-turbo', temperature=0)
service_context = ServiceContext.from_defaults(llm=llm)
index = VectorStoreIndex.from_documents(docs, service_context=service_context)
response = index.as_query_engine().query("&amp;lt;question&amp;gt;")Note: Our top-level `LLMPredictor` still exists but is less user-facing (and we might deprecate in the future). Also, you can still use LangChain LLMs through our `LangChainLLM` class.

## **Resources**

All of our notebooks have by default been updated to use our native OpenAI LLM integration. Here’s some resources to show both the LLM abstraction on its own as well as how it can be used in the overall system:

- [OpenAI LLM](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/llm/openai.ipynb)
- [Using LLM in LLMPredictor](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/llm/llm_predictor.ipynb)
- [Changing LLM within Index/Query Engine](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html#example-changing-the-underlying-llm)
- [Defining a custom LLM Model](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html#example-using-a-custom-llm-model-advanced)

# Standalone Response Synthesis Modules

## **Context**

In any RAG system, there is retrieval and there is synthesis. The responsibility of the synthesis component is to take in incoming context as input, and synthesize a response using the LLM.

Fundamentally, the synthesis module needs to synthesize a response over **any** context list, regardless of how long that context list is. This is essentially “boilerplate” that an LLM developer / [“AI engineer”](https://www.latent.space/p/ai-engineer) must write.

We had this as an internal abstraction in LlamaIndex before (as a `ResponseSynthesizer`), but the external-facing UX was unfriendly to users. The actual piece that gathered responses (the `ResponseBuilder` ) was hard to customize, and the `ResponseSynthesizer` itself was adding an extra unnecessary layer.

Now we have a set of standalone modules that you can easily import. Previously, when you set the `response_mode` in the query engine, these were being setup for you. Now they are more directly available and user-facing.

Here’s a list of all the new `Response Synthesiszer` modules available from `llama_index.response_synthesizer`:

- `Refine` - Query an LLM, sending each text chunk individually. After the first LLM call, the existing answer is also sent to the LLM for updating and refinement using the next text chunk.
- `Accumulate` - Query an LLM with the same prompt across multiple text chunks, and return a formatted list of responses
- `Compact` - The same as `Refine`, but puts as much text as possible into each LLM call
- `CompactAndAccumulate` - The same as `Accumulate`, but puts as much text as possible
- `TreeSummarize` - Create a bottom-up summary from the provided text chunks, and return the root summary
- `SimpleSummarize` - Combine and truncate all text chunks, and summarize in a single LLM call

## **Usage**

As detailed above, you can directly set a response synthesizer in a query engine, or let the `response_mode` fetch the relevant response synthesizer.

Furthermore though, you can directly call and use these synthesizers as low level modules. Here’s a small example:

from llama_index import ServiceContext
from llama_index.response_synthesizers import CompactAndRefine

# you can also configure the text_qa_template, refine_template,
# and streaming toggle from here
response_synthesizer = CompactAndRefine(
  service_context=service_context.from_defaults()
)
response = response_synthesizer.get_response(
 "What skills does Bob have?",
  text_chunks=[" ..."]  # here would be text, hopefully about Bob's skills
)

## Resources

Here are some additional notebooks showing how to use `get_response_synthesizer` :

- [Low-level API Usage Pattern](https://gpt-index.readthedocs.io/en/latest/guides/primer/usage_pattern.html#low-level-api)
- [Custom Retrievers](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/CustomRetrievers.html#plugin-retriever-into-query-engine)

# Metadata Management Capabilities

If you want to have good performance in any LLM application over your data (including a RAG pipeline), you need to make sure that your documents actually contain relevant context for the query. One way to do this is to add proper metadata, both at the document-level and after the documents have been parsed into text chunks (into Nodes).

We allow you to define metadata fields within a Document, customize the ID, and also customize the metadata text/format for LLM usage and embedding usage.

**Defining Metadata Fields**

document = Document(
    text='text',
    metadata={
        'filename': '&amp;lt;doc_file_name&amp;gt;',
        'category': '&amp;lt;category&amp;gt;'
    }
)**Customizing the ID**

The ID of each document can be set multiple ways

- Within the constructor: `document = Document(text="text", doc_id_="id")`
- After constructing the object: `document.doc_id = "id"`
- Automatically using the `SimpleDirectoryReader` : `SimpleDirectoryReader(filename_as_id=True).load_data()`

**Customizing the Metadata Text for LLMs and Embeddings**

As seen above, you can set metadata containing useful information. By default, all the metadata will be seen by the embedding model and the LLM. However, sometimes you may want to only include data to bias embeddings, or only include data as extra information for the LLM!

With the new `Document` objects, you can configure what each metadata field is used for:

document = Document(
    text='text',
    metadata={
        'filename': '&amp;lt;doc_file_name&amp;gt;',
        'category': '&amp;lt;category&amp;gt;'
    },
    excluded_llm_metadata_keys=['filename', 'category'],
    excluded_embed_metadata_keys=['filename']
)**Customizing the Metadata Format Template**

When the metadata is inserted into the text, it follows a very specific format. This format is configurable at multiple levels:

from llama_index.schema import MetadataMode

document = Document(
  text='text',
  metadata={"key": "val"},
  metadata_seperator="::",
    metadata_template="{key}=&amp;gt;{value}",
    text_template="Metadata: {metadata_str}\\n-----\\nContent: {content}"
)
# available modes are ALL, NONE, LLM, and EMBED
print(document.get_content(metadata_mode=MetadataMode.ALL))
# output:
# Metadata: key=&amp;gt;val
# -----
# textPlease check out this guide for more [details](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_documents.html)!

# Full List of Breaking Changes

## Response Synthesis + Node Postprocessors

The `ResponseSynthesizer` object class has been removed, and replaced with `get_response_synthesizer` . In addition to this, node post processors are now handled by the query engine directly, and the old `SentenceEmbeddingOptimizer` has been switched to become a node post processor instance itself.

Here is an example of the required migration to use all moved features.

**Old**

from llama_index import (
    VectorStoreIndex,
    ResponseSynthesizer,
)
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.optimizers import SentenceEmbeddingOptimizer
from llama_index.query_engine import RetrieverQueryEngine

documents = ...
# build index
index = VectorStoreIndex.from_documents(documents)
# configure retriever
retriever = index.as_retriever(
   similarity_top_k=3
)
# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
   response_mode="tree_summarize",
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7),
        SentenceEmbeddingOptimizer(percentile_cutoff=0.5)
    ]
)
# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)**New**

from llama_index import (
    VectorStoreIndex,
    get_response_synthesizer,
)
from llama_index.indices.postprocessor import (
    SimilarityPostprocessor,
    SentenceEmbeddingOptimizer
)

documents = ...
# build index
index = VectorStoreIndex.from_documents(documents)
# configure response synthesizer
response_synthesizer = get_response_synthesizer(
   response_mode="tree_summarize",
)
# assemble query engine
query_engine = index.as_query_engine(
  similarity_top_k=3,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7),
        SentenceEmbeddingOptimizer(percentile_cutoff=0.5)
    ]
)

## LLM Predictor

While introducing a new LLM abstraction, we cleaned up the LLM Predictor and removed several deprecated functionalities:

- Remove `ChatGPTLLMPredictor` and `HuggingFaceLLMPredictor` (use `OpenAI` and `HuggingFaceLLM` instead, see [migration guide](https://gpt-index.readthedocs.io/en/latest/how_to/customization/llms_migration_guide.html))
- Remove support for setting `cache` via `LLMPredictor` constructor.
- Removed `llama_index.token_counter.token_counter` module (see [migration guide](https://gpt-index.readthedocs.io/en/latest/how_to/callbacks/token_counting_migration.html)).

Now, the LLM Predictor class is mostly a lightweight wrapper on top of the `LLM` abstraction that handles:

- conversion of prompts to the string or chat message input format expected by the LLM
- logging of prompts and responses to a callback manager

We advice users to configure the `llm` argument in `ServiceContext` directly (instead of creating LLM Predictor).

## Chat Engine

We updated the `BaseChatEngine` interface to take in a `List[ChatMessage]]` for the `chat_history` instead of tuple of strings. This makes the data model consistent with the input/output of the `LLM` , also more flexibility to specify consecutive messages with the same role.

**Old**

engine = SimpleChatEngine.from_defaults(
	chat_history=[("human message", "assistant message")],
)
response = engine.chat("new human message")**New**

engine = SimpleChatEngine.from_defaults(
    service_context=mock_service_context,
    chat_history=[
        ChatMessage(role=MessageRole.USER, content="human message"),
        ChatMessage(role=MessageRole.ASSISTANT, content="assistant message"),
    ],
)
response = engine.chat("new human message")We also exposed `chat_history` state as a property and supported overriding `chat_history` in `chat` and `achat` endpoints.

## Prompt Helper

We removed some previously deprecated arguments: `max_input_size`, `embedding_limit`, `max_chunk_overlap`

# Conclusion

At a high-level, we hope that these changes continue to enable bottoms-up development of LLM applications over your data. We first encourage you to play around with our new modules on their own to get a sense what they do and where they can be used. Once you’re ready to use them in more advanced workflows, then you can figure out how to use our outer components to setup a sophisticated RAG pipeline.

As always, our [repo](https://github.com/jerryjliu/llama_index) is here and our [docs](https://gpt-index.readthedocs.io/en/latest/) are here. If you have thoughts/comments, don’t hesitate to hop in our [Discord](https://discord.gg/dGcwcsnxhU)!