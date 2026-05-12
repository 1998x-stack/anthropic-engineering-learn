---
title: "LlamaIndex Newsletter 2024-06-18"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-06-18"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 💡 Real-World Use cases:  ](#real-world-use-cases)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 📹 Webinar:  ](#webinar)



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







 Hey Llama Followers🦙



 Welcome to this week’s edition of the LlamaIndex newsletter! We’re bringing you an exciting set of updates and valuable resources from Mixture-of-Agents (MoA) paper as LlamaPack to how AtomicWork’s Atom AI assistant leverages LlamaIndex to boost productivity and manage data effectively. Be sure to check out our in-depth guides, educational tutorials, and webinars for deeper insights into our tools.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Mixture-of-Agents (MoA) LlamaPack:** We have integrated the Mixture-of-Agents (MoA) demonstrating that open-source LLMs can boost task capabilities. MoA outperforms GPT-4 Omni in the AlpacaEval 2.0 benchmarks. [LlamaPack](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-mixture-of-agents/README.md), [Tweet](https://x.com/llama_index/status/1801305617878937959).
  -  **TiDB Integration with LlamaIndex:** PingCap has now integrated their TiDB database with our LlamaIndex’s knowledge graph functionality, making it available as an open-source project. [Docs](https://docs.llamaindex.ai/en/latest/examples/vector_stores/TiDBVector/), [Tweet](https://x.com/llama_index/status/1800987302837297387).
  -  **RAG and Agents Cookbook:** We have released a detailed cookbook on building RAG and Agents. This guide features enhanced observability through our LlamaIndex instrumentation module and ArizeAI. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/presentations/materials/2024-06-13-vector-ess-oss-tools.ipynb), [Tweet](https://x.com/llama_index/status/1801726691813036214).
  -  **AtomicWork’s Enterprise AI Assistant:** AtomicWork’s enterprise AI assistant, Atom, leverages LlamaIndex to handle diverse data formats, boosting productivity and improving the employee experience. Check out the details in their detailed [blog](https://www.atomicwork.com/blog/llamaindex-loaders-powering-atom).
  -  [Guide](https://github.com/run-llama/llama_parse/blob/main/examples/excel/dcf_rag.ipynb) to RAG Over Excel Files: Guide to use LlamaParse to accurately represent Excel files in a spatial grid format, enhancing data interpretation and reducing errors in question-answering.



##  **✨ Feature Releases and Enhancements:**


-  We have integrated Mixture-of-Agents (MoA) [paper](https://arxiv.org/abs/2406.04692) from [TogetherAI](https://x.com/togethercompute) as LlamaPack from demonstrating that open-source large language models (LLMs) can enhance task capabilities. The paper shows that MoA outperforms GPT-4 Omni in the AlpacaEval 2.0 benchmarks. [LlamaPack](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-mixture-of-agents/README.md), [Tweet](https://x.com/llama_index/status/1801305617878937959).
  -  [PingCap](https://x.com/pingcap) has integrated their TiDB database with our LlamaIndex’s knowledge graph functionality, now accessible as an open source project. [Docs](https://docs.llamaindex.ai/en/latest/examples/vector_stores/TiDBVector/), [Tweet](https://x.com/llama_index/status/1800987302837297387).
  -  We have released a detailed cookbook on building RAG and Agents, featuring supercharged observability throughout the call stack, enabled by our LlamaIndex instrumentation module and ArizeAI. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/presentations/materials/2024-06-13-vector-ess-oss-tools.ipynb), [Tweet](https://x.com/llama_index/status/1801726691813036214).
  -  We have released the workshop slides and notebooks from our presentation on “Building an Advanced Research Agent on Databricks” at the Data AI Summit. This workshop focused on enhancing research assistants beyond the standard RAG setups. [Slide deck](https://docs.google.com/presentation/d/1yiuHEQEAhWEvVskbD9jwmfjopznVeZGwwWUzBIZ_P9U/), [Notebook1](https://colab.research.google.com/drive/18RUkf8IpHVSJF-rDh8cOj0QJ6UwQonfh?usp=sharing), [Notebook2](https://colab.research.google.com/drive/18RUkf8IpHVSJF-rDh8cOj0QJ6UwQonfh?usp=sharing), [Tweet](https://x.com/llama_index/status/1802734801201623117).



##  **💡 Real-World Use cases:**


-  AtomicWork’s enterprise AI assistant, Atom, utilizes LlamaIndex to handle various data formats, ensuring accurate and secure data retrieval. Atom enhances decision-making and manages unstructured data effectively, boosting productivity and improving the employee experience. Check out the details in their detailed [blog](https://www.atomicwork.com/blog/llamaindex-loaders-powering-atom).



##  **🗺️ Guides:**


-  [Guide](https://github.com/run-llama/llama_parse/blob/main/examples/excel/dcf_rag.ipynb) to RAG Over Excel Files using LlamaParse to accurately represent Excel files in a spatial grid format, enhancing data interpretation and reducing errors in question-answering.
  -  [Guide](https://www.singlestore.com/blog/claude-3-multimodal-with-llamaindex-and-singlestore/?utm_medium=referral&utm_source=pavan&utm_term=lnkdn&utm_content=multimod) to Building a Multimodal RAG Pipeline by [Pavan Belagatti](https://x.com/Pavan_Belagatti/status/1802955250795417790) using Claude-3 and SingleStoreDB.
  -  [Guide](https://github.com/mistralai/cookbook/blob/main/third_party/LlamaIndex/ollama_mistral_llamaindex.ipynb) to building fully local RAG application using MistralAI, Ollama and LlamaIndex.



##  **✍️ Tutorials:**


-  [Tomaz Bratanic](https://x.com/tb_tomaz)’s [tutorial](https://www.llamaindex.ai/blog/customizing-property-graph-index-in-llamaindex) on constructing a knowledge graph, perform entity deduplication, design a custom graph retriever, and implement a question-answering flow.
  -  [Mervin Praison](https://x.com/MervinPraison)’s [tutorial](https://www.youtube.com/watch?v=jnWaUtS2Fr8) on creating the core components of an agent defining tools, integrating them into an agent reasoning loop, and wrapping everything with a user interface. using local models and [chainlit](https://github.com/Chainlit/chainlit).
  -  [Arkiti](https://x.com/AkritiUpadhya13)’s [tutorial](https://medium.com/@akriti.upadhyay/text-to-sql-using-singlestore-helios-groq-and-llama-3-0ebe1150cbe2) on building a dynamic text-to-SQL solution using Llama 3 and GroqInc, highlighting the scalable and fast capabilities of SingleStoreDB Helios for multi-cloud deployments.
  -  [Kingzzm](https://x.com/kingzzm)’s [tutorial](https://ai.gopubby.com/advanced-rag-retrieval-strategy-embedded-tables-fdb3e44003a5) on Advanced RAG Patterns detailing effective strategies for handling documents with embedded tables, utilizing tools like LlamaParse and Nougat for enhanced QA performance.



##  **📹 Webinar:**


-  [Webinar](https://www.youtube.com/watch?v=9AqdqJdCNCw) on The Future of Web Agents with MultiOn. [Div Garg](https://x.com/DivGarg9) provided a full demo walkthrough and discuss the agentification of the internet.