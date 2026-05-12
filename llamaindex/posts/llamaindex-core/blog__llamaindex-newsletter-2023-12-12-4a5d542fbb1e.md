---
title: "LlamaIndex Newsletter 2023–12–12"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-12-12-4a5d542fbb1e"
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







Howdy, Llama Enthusiasts 🦙,

We are thrilled to announce another exciting week filled with full of the latest updates, features, insightful tutorials, guides, webinars, and so much more. Have a groundbreaking project, compelling article, or captivating video? We’re all ears! Reach out to us at [news@llamaindex.ai](mailto:news@llamaindex.ai).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Don’t forget to subscribe to our newsletter via our [website](https://www.llamaindex.ai/) to have all these exciting developments delivered directly to your inbox.

🤩 **First, the highlights:**

- **Llama Datasets:** A diverse collection of community-contributed datasets for benchmarking RAG pipelines. [Blog](/introducing-llama-datasets-aadb9994ad9e), [Tweet](https://x.com/llama_index/status/1731718080223707148?s=20).
- **RAGs v5:** Enables multi-modal data handling with natural language for both text and image sources. [Tweet](https://x.com/llama_index/status/1731843485115064531?s=20).
- **Production RAG Pipeline:** New features and a guide for efficient RAG while handling updates to your data, including incremental re-indexing for Google Docs and enhanced transformation and caching processes. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/ingestion_gdrive.ipynb), [Tweet](https://x.com/llama_index/status/1732121799033487361?s=20).
- **Revamped LlamaHub:** A community-driven hub with universal data loaders, a new user interface, and a range of tools, templates, and datasets. [Tweet](https://x.com/llama_index/status/1732814499235962907?s=20).
- **AutoTranslateDoc:** An open-source project for translating GitHub repository documentation into over 15 languages. [Blog](/bridging-the-language-gap-in-programming-introducing-autotranslatedoc-ccc93fbcd3a8), [Repo](https://github.com/run-llama/automatic-doc-translate), [Tweet](https://x.com/jerryjliu0/status/1732926141118472448?s=20)

**✨ Feature Releases and Enhancements:**

- We launched **Llama Datasets** 🦙📝, a collection of community-contributed datasets tailored for benchmarking RAG pipelines in various use cases. These datasets offer flexibility in selecting the most appropriate one for specific LLM applications. The initial release includes a diverse range, such as Code Help Desk, FinanceBench, Mini TruthfulQA, Mini Squad V2, Blockchain Solana, Uber 10K, Llama 2 Paper, Paul Graham Essay, Origin of COVID-19, CovidQADataset, MiniCovidQADataset and LLM Survey Paper. Each dataset, designed as a QA set, integrates smoothly with Llama Index abstractions, providing a platform for comprehensive benchmarking across multiple metrics. All datasets are available on LlamaHub for easy download and evaluation. [Blog](/introducing-llama-datasets-aadb9994ad9e), [Tweet](https://x.com/llama_index/status/1731718080223707148?s=20).
- We launched **RAGs v5**, enabling multi-modal data handling with natural language for both text and image sources. Key features include enhanced multi-modal indexing, the capability to view sources in any RAG agent, and support for loading entire directories, not just single files. [Tweet](https://x.com/llama_index/status/1731843485115064531?s=20).
- We have launched new features and a guide for building a **production RAG pipeline**, enabling efficient question-answering with LLMs on production data even while it is continuously updated. This includes incremental re-indexing for Google Docs changes and enhanced transformation and caching processes in our updated `**IngestionPipeline**`. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/ingestion_gdrive.ipynb), [Tweet](https://x.com/llama_index/status/1732121799033487361?s=20).
- We launched a one-click, full-stack LlamaIndex template now available on **Replit**! This template features a full-stack Next.js app in TypeScript, capable of reading any files you provide, and includes a chat interface for querying those documents. It’s completely customizable and based on our popular create-llama generator. [Replit Template](https://replit.com/@LlamaIndex/createllama), [Tweet](https://x.com/llama_index/status/1732150579928150247?s=20).
- We have introduced `**RAGEvaluatorPack**` to easily benchmark your RAG pipeline on any dataset with a single line of code, offering metrics like correctness, relevancy, and context similarity. [Docs](https://llamahub.ai/l/llama_packs-rag_evaluator), [Tweet](https://x.com/llama_index/status/1732210229574824357?s=20).
- We released community templates for create-llama, offering a selection of community-contributed starter templates during setup. Current examples include `embedded-tables` for analyzing complex tables in large PDFs, and `multi-document-agent` for comparing multiple documents. [Tweet](https://x.com/llama_index/status/1732480745804022240?s=20).
- We launched multi-modal support in create-llama, our user-friendly command-line tool for generating full-stack LlamaIndex apps. Now, easily integrate GPT-4-vision in your app, allowing you to upload images to the web interface and receive answers about them in just seconds. [Tweet](https://x.com/llama_index/status/1732480613763215783?s=20).
- We launched the Ollama LlamaPack, a new offering that integrates local LLMs and embeddings into a fully local RAG pipeline, enhancing language model accessibility and capabilities. [Docs](https://docs.llamaindex.ai/en/latest/examples/llama_hub/llama_pack_ollama.html), [Tweet](https://x.com/llama_index/status/1732565478546223322?s=20).
- We launched the revamped [LlamaHub](https://llamahub.ai/), a hub for community-driven modules to enhance LLM app development, featuring universal data loaders, a new user interface, and a range of tools, templates, and datasets. [Tweet](https://x.com/llama_index/status/1732814499235962907?s=20).
- We introduced AutoTranslateDoc, an open-source project for translating GitHub repository documentation into over 15 languages, including Chinese, Spanish, and French. This tool, successfully implemented in our own LlamaIndex.TS docs, simplifies the internationalization process for open-source projects. [Blog](/bridging-the-language-gap-in-programming-introducing-autotranslatedoc-ccc93fbcd3a8), [Repo](https://github.com/run-llama/automatic-doc-translate), [Tweet](https://x.com/jerryjliu0/status/1732926141118472448?s=20)
- We released support for exact match and range queries in 4 vector databases including Weaviate, Chroma, Qdrant and Pinecone, allowing auto-retrieval via metadata filters, elevating the functionality of structured and unstructured data querying. [Tweet](https://x.com/llama_index/status/1733289204380311703?s=20).

**🗺️ Guides:**

- [Guide](https://docs.google.com/presentation/d/1o4OeOvyaXAGNF1Dlbw4s5KYOMAE-2fUzqxo2lproprw/edit#slide=id.g2a2d0d2fc2a_0_0) on building LLM apps for financial data which is presented at MindsDB event. Learn to query diverse financial data using advanced RAG with techniques for multi-document comparisons, embedded tables, and converting text queries into domain-specific languages.
- [Guide](https://docs.google.com/presentation/d/1IJ1bpoLmHfFzKM3Ef6OoWGwvrwDwLV7EcoOHxLZzizE/edit#slide=id.g23d546514bd_0_290) on advanced RAG Cheat Sheet, a concise guide offering solutions for different RAG-related pain points and techniques. It’s part of our Snowflake BUILD talk and PyData Global talk.

**✍️ Tutorials:**

- [Blog](/llamaindex-waii-combining-structured-data-from-your-database-with-pdfs-for-enhanced-data-647a9e66be82) by [Waii.ai](http://waii.ai/) on creating an agent that queries both enterprise databases and PDF data, combining advanced text-to-SQL techniques and a Llama Index RAG pipeline, for effective analysis of structured and unstructured data like retail sales trends.
- Wenqi Glantz’s [tutorial](https://levelup.gitconnected.com/a-simpler-way-to-query-neo4j-knowledge-graphs-99c0a8bbf1d7) on using LLMs for querying knowledge graphs introduces seven strategies, now easily accessible through our LlamaPacks and featured in our Neo4j query engine.
- An hour comprehensive workshop [tutorial](https://www.youtube.com/watch?v=oa82yoJ6zYc) by [AIMakerspace](https://twitter.com/AIMakerspace) on RAG strategies over complex documents through recursive retrieval.
- [Laurie’s](https://twitter.com/seldo) [video](https://www.notion.so/Content-roadmap-6f27c002d67e428497326d972afa7eb6?pvs=21) on using LlamaIndex for multi-modal retrieval-augmented generation apps teaches you to build indexes and retrieve data from text and images, for enhanced query responses.
- [Ravi Theja’s](https://twitter.com/ravithejads) [video](https://www.youtube.com/watch?v=_vU-biwMoGk) on Understanding LlamaIndex 0.9v abstractions and features.

**🤝 Integrations:**

- We integrated AssemblyAI with Llama Index TS, enhancing the capabilities and offering new, innovative solutions. [Blog](https://www.assemblyai.com/blog/announcing-the-assemblyai-integration-for-llamaindex-ts/).
- We integrated Panel, a powerful framework for building interactive data apps as a LlamaPack. This provides you with a robust chat interface for talking to your data with full streaming support in a single line of code. [Docs](https://t.co/QSVdFxvfAi), [Tweet](https://x.com/llama_index/status/1733894204076720551?s=20).
- We integrated FlagEmbeddingReranker to further boost your RAG pipeline. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/FlagEmbeddingReranker.ipynb), [Tweet](https://x.com/llama_index/status/1734019264166953421?s=20).

🎥 **Webinars:**

Webinar featuring Haotian Liu, the author of LLaVa which includes a deep dive into the open-source multi-modal models of LLaVa, which are competitive with GPT-4V, and a presentation on multi-modal use cases with LLaVa + LlamaIndex by Haotian Zhang from the LlamaIndex team.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex even more Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)