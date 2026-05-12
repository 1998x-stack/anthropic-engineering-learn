---
title: "Announcing the LlamaIndex integration with Azure AI"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/announcing-the-llamaindex-integration-with-azure-ai"
category: "tools-integrations"
---

Content



- [ Core components  ](#core-components)
- [ Storage and memory  ](#storage-and-memory)
- [ Enhancing agents with tools  ](#enhancing-agents-with-tools)
- [ Getting to production quickly  ](#getting-to-production-quickly)
- [ Looking to the future  ](#looking-to-the-future)



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







 At Microsoft Ignite in Chicago, LlamaIndex announces that years of productive collaboration with Microsoft have resulted in a complete stack for end-to-end Retrieval-Augmented Generation (RAG) and knowledge-augmented agents, available entirely on Azure.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Core components



 The stack starts at the fundamental base of any generative AI application, the LLM, with [Azure OpenAI Service](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/). The powerful models available can be enhanced with your private data by using [Azure AI Embeddings](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_inference/) stored in the scalable, performant [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/) vector store. Using these core components and LlamaIndex, you can easily put together a world-class RAG app.







 [Learn more about RAG in LlamaIndex](https://docs.llamaindex.ai/en/stable/understanding/rag/).



##  Storage and memory



 LlamaIndex integration with Azure AI also provides for further refinement of a RAG stack, with the combination of the [Azure Doc Store](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/) and [Azure KV Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/#llama_index.storage.kvstore.azure.AzureKVStore) allowing incremental loading of new data into RAG applications while the [Azure Chat Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/#llama_index.storage.chat_store.azure.AzureChatStore) gives a chatbot application fast, persistent memory of previous interactions.



##  Enhancing agents with tools



 In 2024 LlamaIndex has pushed beyond our foundations in the RAG space to supporting full agents via our powerful, flexible [Workflows](https://docs.llamaindex.ai/en/stable/understanding/workflows/) abstraction and we’ve seen enthusiastic adoption in the community. Azure’s services come into play here too, with a suite of agentic tools including the [Azure Code Interpreter](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/) providing fast, safe execution of generated code, as well as agentic tools for [text-to-speech generation](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/), [computer vision](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/) and [language translation](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)



##  Getting to production quickly



 Most recently, the ongoing collaboration between LlamaIndex and Azure AI has resulted in LlamaIndex templates in the [AI App Template Gallery](https://azure.github.io/ai-app-templates/), an easy path to get from zero to sixty with your Azure-based agentic AI applications using LlamaIndex.



##  Looking to the future



 “We’re excited that our collaboration with Microsoft has resulted in so many happy customers already, and we can’t wait to see what else we come up with together in the years ahead,” said Jerry Liu, CEO and co-founder, “Microsoft’s AI ecosystem has been invaluable to users of LlamaParse and LlamaParse in giving them the confidence to deploy cutting-edge AI solutions with security they can trust.”