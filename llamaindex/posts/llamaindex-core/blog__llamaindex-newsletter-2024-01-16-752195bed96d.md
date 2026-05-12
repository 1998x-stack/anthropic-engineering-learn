---
title: "LlamaIndex Newsletter 2024–01–16"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-16-752195bed96d"
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







Hello LlamaIndex Enthusiasts 🦙,

Get ready for an exciting week at LlamaIndex, teeming with dynamic community contributions and insightful learning resources. Dive into our range of new features, tutorials, guides, and events, all designed to enhance your LlamaIndex journey.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We’re excited to announce our [very first in-person hackathon](https://rag-a-thon.devpost.com/), scheduled for February 2nd-4th. Join us to connect with fellow RAG enthusiasts and compete for prizes totaling over $4,000!

If you’ve been working on a fascinating project, penned an insightful article, or produced an engaging video, we’re eager to see it! Share your contributions with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). Don’t forget to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) to receive all the latest updates directly in your inbox.

🤩 **The highlights:**

- **Chain-of-Table:** Step-by-step table reasoning and operations for enhanced LLM tabular data understanding. [LlamaPack](https://llamahub.ai/l/llama_packs-tables-chain_of_table?from=llama_packs), [Tweet](https://x.com/llama_index/status/1746217167706894467?s=20).
- **LLM Self-Consistency:** Merges textual and symbolic reasoning with majority voting for precise answers. [LlamaPack](https://t.co/pGcRG4ieD4), [Tweet](https://twitter.com/llama_index/status/1746937012798800272?s=20).
- **Semantic Text Splitting in RAG:** Greg Kamradt’s embedding similarity method for efficient document splitting. [LlamaPack](https://llamahub.ai/l/llama_packs-node_parser-semantic_chunking?from=all), [Tweet](https://x.com/llama_index/status/1745482959237615847?s=20).
- **Parallel RAG Ingestion:** Up to 15x faster document processing in LlamaIndex. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/parallel_execution_ingestion_pipeline.ipynb), [Tweet](https://x.com/llama_index/status/1745849571614539984?s=20).
- **TogetherAI’s Embeddings Support:** Guide to build retrieval-augmented apps with MistralAI’s 8x7b model and TogetherAI Embeddings. [Blogpost](https://www.together.ai/blog/rag-tutorial-llamaindex) , [Tweet](https://x.com/llama_index/status/1745551739368222815?s=20).

**✨ Feature Releases and Enhancements:**

- We launched Chain-of-Table Framework in LlamaPack for LLM Tabular Data Understanding. This approach enables step-by-step table reasoning and operations like adding columns, row selection, grouping, and sorting, mimicking a data scientist’s method for concise data representation. [LlamaPack](https://llamahub.ai/l/llama_packs-tables-chain_of_table?from=llama_packs), [Tweet](https://x.com/llama_index/status/1746217167706894467?s=20).
- We launched LLM Self-Consistency Mechanism for Tabular Data in LlamaPack. This method combines textual and symbolic reasoning, utilizing a novel mix self-consistency approach with majority voting to select the best answer. [LlamaPack](https://t.co/pGcRG4ieD4), [Tweet](https://twitter.com/llama_index/status/1746937012798800272?s=20).
- We have Introduced Semantic Text Splitting in RAG with LlamaPack. Check Greg Kamradt’s method of splitting documents based on embedding similarity between sentences. This auto-tuned threshold approach enhances RAG pipelines, soon to be available in LlamaPack using LlamaIndex abstractions. [LlamaPack](https://llamahub.ai/l/llama_packs-node_parser-semantic_chunking?from=all), [Tweet](https://x.com/llama_index/status/1745482959237615847?s=20).
- We launched Parallel RAG Ingestion in LlamaIndex for up to 15x Faster Document Processing. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/ingestion/parallel_execution_ingestion_pipeline.ipynb), [Tweet](https://x.com/llama_index/status/1745849571614539984?s=20).
- We have launched Support for TogetherAI’s Embeddings Endpoint. Check the blog for a step-by-step guide on creating a retrieval-augmented generation app with MistralAI’s 8x7b model and TogetherAI Embeddings. [Blogpost](https://www.together.ai/blog/rag-tutorial-llamaindex) , [Tweet](https://x.com/llama_index/status/1745551739368222815?s=20).
- We integrated AgentSearch-v1 as a data loader and Retriever in LlamaHub, offering a robust alternative for internet content search/retrieval without relying on Bing/Google APIs. [LlamaPack](https://llamahub.ai/l/llama_packs-agent_search_retriever?from=llama_packs), [Tweet](https://x.com/llama_index/status/1745903362128617842?s=20).
- Raduaschl introduced Ensembling and Fusion in Advanced RAG with LlamaPack. Learn to build an ensembling + fusion pipeline in about 30 lines of code using QueryPipeline syntax, featuring full async support. [LlamaPack](https://t.co/iD1v5FuIdy), [Tweet](https://x.com/llama_index/status/1745228497646449021?s=20).

**🗺️ Guides:**

- [Guide](https://www.youtube.com/watch?v=4U8viyAQkJ8) to Building Full-Stack RAG Applications with LlamaIndex and Azure Cosmos DB.
- [Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever.html) showing to combine auto-retrieval for semi-structured retrieval with metadata with MMR to enforce diversity in results.
- [Guide](https://github.com/mickymultani/RAG-with-Cross-Encoder-Reranker) by [MountainMicky](https://twitter.com/MountainMicky) to understanding the Importance of Reranking in Advanced RAG Pipelines.

**✍️ Tutorials:**

- [Andrej Baranovskij](https://twitter.com/andrejusb) [tutorial](https://www.youtube.com/watch?v=VKeYaIEk82s) on Transforming Invoice Data into JSON with LlamaIndex and Pydantic.
- NVIDIA [tutorial](https://developer.nvidia.com/blog/supercharging-llm-applications-on-windows-pcs-with-nvidia-rtx-systems/) on Building AI apps with local LLMs running on Windows with LlamaIndex and NVIDIA
- [Harshad Suryawanshi](https://harshadsuryawanshi.medium.com/) [tutorial](/ai-voice-assistant-enhancing-accessibility-in-ai-with-llamaindex-and-gpt3-5-f5509d296f4a) on AI Voice Assistant: Enhancing Accessibility in AI with LlamaIndex and GPT3.5.

🎥 Events:

- Ravi Theja gave talk on Building Multi-Tenancy RAG System with LlamaIndex and Qdrant at FOSS United, Bangalore, India.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex, even more, Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)