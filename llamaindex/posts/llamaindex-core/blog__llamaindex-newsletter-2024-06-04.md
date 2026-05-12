---
title: "LlamaIndex Newsletter 2024-06-04"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-06-04"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 🗺️ Guides:  ](#guides)
- [ 🖥️ Demos:  ](#demos)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 📑 Papers:  ](#papers)
- [ 📹 Webinar:  ](#webinar)
- [ 📅 Events:  ](#events)



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







 Hello, LlamaIndex Family! 🦙



 We&#39;re thrilled to connect with you again and bring you the latest and greatest from the world of LlamaIndex. This week, we&#39;re excited to present an array of updates and a diverse lineup of content designed to enhance your LlamaIndex experience, particularly when working with Knowledge Graphs. From integrations and guides to demos and tutorials, we&#39;ve got you covered with all the tools and insights you need.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Elevating Knowledge Graphs:** The Property Graph Index, introduced in LlamaIndex, transforms how knowledge graphs (KGs) are built and queried. This powerful toolkit enhances graph searches with vector capabilities. [Docs](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/), [Tweet](https://x.com/llama_index/status/1795869279457546447).
  -  **Spreadsheet Insights with LlamaParse:** LlamaParse now supports spreadsheet parsing, turning complex Excel files into LLM-friendly tables for improved performance and data handling. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/demo_excel.ipynb), [Tweet](https://x.com/llama_index/status/1796237002364613040).
  -  **Code Generation with Codestral:** Codestral, a cutting-edge model from MistralAI, is now integrated into LlamaIndex. This code-generating tool supports over 80 programming languages. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/codestral/), [Tweet](https://x.com/llama_index/status/1795900182439276731).



##  **✨ Feature Releases and Enhancements:**


-  We have introduced the Property Graph Index, a major feature that establishes LlamaIndex as the premier framework for building knowledge graphs (KGs) with LLMs. This sophisticated toolkit enables the construction and querying of KGs, allowing for joint vector and graph searches even in graph stores that lack native vector support. [Docs](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/), [Tweet](https://x.com/llama_index/status/1795869279457546447).
  -  We have launched support for parsing spreadsheets in LlamaParse, allowing you to convert complex Excel files and other spreadsheet formats into clean, LLM-friendly tables for improved RAG pipeline performance. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/demo_excel.ipynb), [Tweet](https://x.com/llama_index/status/1796237002364613040).
  -  We have integrated Codestral from MistralAI into LlamaIndex, providing day 0 support for this cutting-edge code-generating model trained on over 80 programming languages. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/codestral/), [Tweet](https://x.com/llama_index/status/1795900182439276731).
  -  We have integrated PostgresML into LlamaIndex, perfect for those who love Postgres and want to build AI applications. It serves open-source models locally, handles embeddings, and allows you to train or fine-tune models directly in Python and JavaScript. [Blogpost](https://www.llamaindex.ai/blog/simplify-your-rag-application-architecture-with-llamaindex-postgresml), [Tweet](https://x.com/llama_index/status/1795561227319734360).
  -  We have integrated with Milvus Lite to provide an easy start to vector search, offering day-1 support with LlamaIndex. [Docs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/), [Tweet](https://x.com/llama_index/status/1796305277073174654).



##  **🗺️ Guides:**


-  [Guide](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/) to Building a Custom Graph Retriever to create a custom graph retriever for your specific needs by combining vector search and graph search with reranking for improved results.
  -  [Guide](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_nim/) to Building GenAI Applications in minutes with NVIDIA&#39;s NIM inference microservices, offering an easy and fast way to deploy GenAI applications. This step-by-step guide teaches you how to run models, generate embeddings, and re-rank data for optimal results.
  -  [Guide](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/property_graph/property_graph_advanced.ipynb) to Constructing Knowledge Graphs with LLMs**,** build knowledge graphs using local models and Neo4j, starting with defining entities and relationships, using SchemaLLMPathExtractor to create structured graphs, and querying to uncover insights.



##  **🖥️ Demos:**


-  [Omakase RAG Orchestrator](https://github.com/ammirsm/llamaindex-omakase-rag), a project developed by [Amir Mehr](https://x.com/thatisamir), is a web app template designed to help you build scalable RAG applications using Django, LlamaIndex, and Google Drive. It features a full-featured RAG API, data source management, user access control, and an admin panel.
  -  [gmail-extractor](https://github.com/run-llama/gmail-extractor), a project by Laurie project that trains a Python script with an LLM to extract structured data from Gmail. By iteratively improving the script based on email data, the LLM can effectively modify and enhance it to extract information with precision.



##  **✍️ Tutorials:**


-  Sherlock Xu’s [tutorial](https://www.bentoml.com/blog/serving-a-llamaindex-rag-app-as-rest-apis) from BentoML on Serving A LlamaIndex RAG App as REST APIs.



##  **📑 Papers:**


-  FinTextQA, a new benchmark dataset for long-form financial question answering, has been introduced by Jian Chen and their team. This benchmark was evaluated using LlamaIndex&#39;s Auto-Merging and Sentence Window Retrievers, along with various embeddings, rerankers, and LLMs, offering a comprehensive question-answering system for financial text.



##  **📹 Webinar:**


-  [Webinar](https://www.youtube.com/watch?v=o0DPxvgML5c) with authors of memary - Julian Saks, Kevin Li, Seyeong Han. Memary is a fully open-source reference implementation for long-term memory in autonomous agents



##  📅 **Events:**


-  [Join](https://www.meetup.com/nlp_london/events/301171675/) Pierre from LlamaIndex along with speakers from Weaviate, and Weights &amp; Biases on June 12th at the London NLP meetup, focusing on the challenges and solutions for using LLMs with financial services data in production settings.