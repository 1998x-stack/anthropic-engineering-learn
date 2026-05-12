---
title: "LlamaIndex Newsletter 2024-04-02"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-04-02"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 🎥 Demos:  ](#demos)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 🎥 Webinars:  ](#webinars)



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







 Greetings, LlamaIndex community! 🦙







 Welcome to another exciting weekly update from LlamaGalaxy! We&#39;re thrilled to share a range of fantastic updates with you, including the introduction of RAFT LlamaPack, enhanced memory and cost efficiency in RAG with Cohere&#39;s embeddings, and much more.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  🤩 **The highlights:**


-  **DeepLearningAI Course:** JavaScript RAG Web Apps with LlamaIndex collaborative course with DeepLearningAI. [Course](https://www.deeplearning.ai/short-courses/javascript-rag-web-apps-with-llamaindex/), [Tweet](https://x.com/AndrewYNg/status/1773006786058219889?s=20).
  -  **RAFTDatasetPack LlamaPack**: Introduced RAFTDatasetPack for dataset generation using RAFT - Retrieval Augmented Fine Tuning for training models to differentiate between relevant &#39;oracle&#39; documents and &#39;distractor&#39; documents. [LlamaPack](https://github.com/run-llama/llama_index/tree/main/llama-index-packs/llama-index-packs-raft-dataset), [Tweet](https://x.com/llama_index/status/1772662480210198809?s=20).
  -  **Memory Efficiency with Cohere Embeddings:** Utilize Cohere&#39;s Int8 and binary embeddings for cost-effective and low-memory RAG operations. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/cohere_retriever_eval.ipynb), [Tweet](https://x.com/llama_index/status/1773402379016138955?s=20).
  -  **Python Docs Makeover:** Revamped Python documentation with accessible example notebooks, advanced search, and comprehensive API details. [API Ref](https://docs.llamaindex.ai/en/stable/api_reference/), [Tweet](https://x.com/llama_index/status/1772355240299520083?s=20), [Docs](https://t.co/BS7oDqZ7qW)



###  **✨ Feature Releases and Enhancements:**


-  We introduced RAFT - Retrieval Augmented Fine Tuning, a method from [Tianjun Zhang](https://www.linkedin.com/in/tianjun-zhang-333bb2126/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B1dQCZFffT4aXk6ePSYdUYg%3D%3D) and [Shishir Patil](https://www.linkedin.com/in/shishir-patil/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BNG6wPCQHTaWKxcdltRvvjw%3D%3D) to enhance domain-specific RAG performance in LLMs. By training models to differentiate between relevant &#39;oracle&#39; documents and &#39;distractor&#39; documents, RAFT improves context understanding. Try it out with our new RAFTDatasetPack LlamaPack for dataset generation. [LlamaPack](https://github.com/run-llama/llama_index/tree/main/llama-index-packs/llama-index-packs-raft-dataset), [Tweet](https://x.com/llama_index/status/1772662480210198809?s=20).
  -  We collaborated with DeepLearningAI for a course that goes beyond teaching RAG techniques; it guides you on integrating RAG into a full-stack application. Learn to construct a backend API, develop an interactive React component, and tackle the unique challenges of deploying RAG on a server rather than just in a notebook. [Course](https://www.deeplearning.ai/short-courses/javascript-rag-web-apps-with-llamaindex/), [Tweet](https://x.com/AndrewYNg/status/1773006786058219889?s=20).
  -  We integrated with Cohere&#39;s Int8 and Binary Embeddings for a memory-efficient solution for your RAG pipeline. This addresses the high memory usage and costs associated with large dataset operations in RAG. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/cohere_retriever_eval.ipynb), [Tweet](https://x.com/llama_index/status/1773402379016138955?s=20)
  -  We launched revamped Python docs with top-level example notebooks, improved search with previews, and overhauled API documentation. [API Ref](https://docs.llamaindex.ai/en/stable/api_reference/), [Tweet](https://x.com/llama_index/status/1772355240299520083?s=20), [Docs](https://t.co/BS7oDqZ7qW)



###  **🎥 Demos:**


-  [RestAI](https://x.com/llama_index/status/1774159755675898010?s=20), a project by [Pedro Dias](https://twitter.com/pedromdias) is a nifty platform that offers RAG, advanced text-to-SQL, and multimodal inference as a service with a nifty UI.
  -  [Ragdoll](https://github.com/bennyschmidt/ragdoll) and [Ragdoll Studio](https://github.com/bennyschmidt/ragdoll-studio) by bennyschmidt: Create AI Personas for characters, web assistants, or game NPCs using LlamaIndex TS, local LLMs, and image generation with Ollama and StabilityAI.



###  **🗺️ Guides:**


-  [Guide](https://towardsdatascience.com/designing-rags-dbb9a7c1d729) to Designing RAG Systems by [Michał Oleszak](https://michaloleszak.medium.com/) for an in-depth look at crucial design decisions in building efficient RAG systems, spanning five key areas: Indexing, Storing, Retrieval, Synthesis, and Evaluation.



###  **✍️ Tutorials:**


-  [Sujit Patil](https://twitter.com/palsujit) [tutorial](https://sujitpal.blogspot.com/2024/03/hierarchical-and-other-indexes-using.html) on combining semantic chunking with hierarchical clustering and indexing for RAG content enrichment.
  -  Florian June&#39;s [tutorial](https://ai.gopubby.com/advanced-rag-08-self-rag-c0c5b5952e0e) on crafting a dynamic RAG system with integrated reflection, a guide to building Self-RAG from scratch.
  -  Laurie&#39;s [video tutorial](https://x.com/llama_index/status/1773783011785585141?s=20) on using LlamaParse&#39;s LLM-powered parsing turns complex insurance policies into clear yes-or-no statements, improving LLM responses on coverage queries.
  -  [Akriti’s](https://twitter.com/AkritiUpadhya13) [tutorial](https://medium.com/@akriti.upadhyay/building-real-time-financial-news-rag-chatbot-with-gemini-and-qdrant-64c0a3fbe45b) on Building Real-Time Financial News RAG Chatbot with Gemini, and Qdrant.
  -  Marco Bertelli&#39;s [tutorial](https://python.plainenglish.io/deploying-a-production-ready-rag-server-a-comprehensive-guide-with-llamaindex-dbe57cc960df) on deploying a RAG server for real-time use, and covering efficient embedding serving, concurrent request handling, and failure resilience.
  -  [Sudarshan Koirala’s](https://twitter.com/mesudarshan) [tutorial](https://www.youtube.com/watch?v=wCFXae8hiYA) on building advanced PDF RAG with LlamaParse and purely local models for embedding, LLMs, and reranking.



###  🎥 **Webinars:**


-  [Register for a webinar](https://lu.ma/v1bdat63) with [Tianjun Zhang](https://www.linkedin.com/in/tianjun-zhang-333bb2126/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3B1dQCZFffT4aXk6ePSYdUYg%3D%3D) and [Shishir Patil](https://www.linkedin.com/in/shishir-patil/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BNG6wPCQHTaWKxcdltRvvjw%3D%3D) on how to do retrieval-augmented fine-tuning (RAFT).
  -  [Webinar](https://www.youtube.com/watch?v=TeEX7CoHT9k) with [Daniel](https://twitter.com/dani_avila7) on [CodeGPT](https://codegpt.co/) - a platform for AI Copilots that help your coding workflows, with components built on top of LlamaIndex components.
  -  [Vectara’s](https://twitter.com/vectara?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) [Panel Discussion](https://www.youtube.com/watch?v=R5pddHfUThQ&t=351s) on &#39;Why RAG will Never Die?’.