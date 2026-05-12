---
title: "OpenAI DevDay Updates: GPT-4 Turbo &amp; Vision | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-news-special-edition-openai-developer-day-e955f16db4e2"
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







Hello Llama fans!

Yesterday was a big day in the world of LLMs; OpenAI held their [developer day conference](https://devday.openai.com/) and there were a slew of new features. The team were all hands on deck to bring support for these features to the library as fast as possible — which is to say, [the same day](https://twitter.com/llama_index/status/1721737484961480836)!



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In case you missed our tweet about it, if you install the [latest build](https://github.com/run-llama/llama_index/releases) of LlamaIndex you’ll get everything below:

# Support for two new models released today

- `gpt-4-1106-preview` , aka **GPT-4 Turbo**, the latest GPT-4 model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and a 128,000 token context window
- `gpt-4-vision-preview` , aka **GPT 4 Turbo with vision** with long-awaited multimodal support, has the ability to understand images in addition to all the other GPT-4 Turbo capabilities.

You can use these models just as you would any other OpenAI model:

from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext

llm = OpenAI(model="gpt-4-1106-preview")
service_context = ServiceContext.from_defaults(llm=llm)
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

# Azure OpenAI endpoints

Check out the [OpenAI Azure notebook](https://docs.llamaindex.ai/en/stable/examples/llm/azure_openai.html) for examples.

# New embeddings abstractions

Including Azure embeddings.

# Function calling

Check out [our notebook](https://docs.llamaindex.ai/en/stable/examples/llm/openai.html#function-calling) for examples.

# SEC insights

Our demo of the power of retrieval-augmented generation for financial filings, [SEC Insights](https://www.secinsights.ai/), has been updated to use the latest version of GPT-4! Watch as you instantly get deeper insights and more relevant responses.

Look out for more OpenAI updates soon! Our regular newsletter will also be posted tomorrow.