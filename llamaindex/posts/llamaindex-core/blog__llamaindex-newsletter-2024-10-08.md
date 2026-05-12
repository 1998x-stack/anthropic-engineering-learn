---
title: "LlamaIndex Newsletter 2024-10-08"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-10-08"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ 🗺️ LlamaParse And LlamaParse:  ](#llamaparse-and-llamaparse)
- [ ✨ Framework:  ](#framework)
- [ 💡 Use-case:  ](#use-case)
- [ ✍️ Community:  ](#community)
- [ 📅💻 Webinar And Hackathon:  ](#webinar-and-hackathon)
- [ 👥 Recruitment:  ](#recruitment)



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







 Hello, Llama Admirers! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re excited to announce a significant price reduction for LlamaParse Premium—now just $45 per 1,000 pages—to streamline your work with complex documents like slide decks and multi-table Excel sheets. This edition also features the guide to build multimodal RAG pipeline using LlamaParse Premium, AnthropicAI&#39;s contextual retrieval, and LlamaParse for improved content accuracy. Additionally, we introduce the new Voice Chat PDF feature, integrated with OpenAI&#39;s Realtime API. Don’t miss these updates and check out our detailed guides and tutorials.







 If you haven&#39;t explored LlamaParse yet, make sure to [sign up](https://cloud.llamaindex.ai/) and [get in touch with us](https://www.llamaindex.ai/contact) to discuss your specific enterprise use case.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Voice Chat PDF Feature:** Integration of OpenAI&#39;s Realtime API with LlamaIndex and Next.js enables real-time voice conversations over documents.
  -  **Multimodal RAG Pipeline with Prompt Caching and Contextual Retrieval:** Utilize LlamaParse Premium, AnthropicAI’s contextual retrieval, and LlamaParse to improve slide deck content, reduce costs, and boost retrieval accuracy with detailed contextual summaries.
  -  **Contextual Retrieval RAG Guide:** AnthropicAI&#39;s technique for enhanced retrieval by appending metadata to document chunks and using prompt caching to reduce token costs.
  -  **LlamaParse Premium Price Cut:** The price for LlamaParse Premium is now $45 per 1,000 pages, previously $75. This service efficiently manages complex documents including slide decks, diagrams, and multi-table Excel sheets.







##  **🗺️ LlamaParse And LlamaParse:**


-  We&#39;ve reduced the price of LlamaParse Premium to $45 per 1,000 pages, down from $75. It efficiently handles complex documents like slide decks, diagrams, multi-table Excel sheets, scanned texts, and more, managing extensive text, tables, and visual elements effectively. [Code](https://github.com/run-llama/llama_parse).
  -  Guide to Building Multimodal RAG Pipelines: Utilize LlamaParse Premium, AnthropicAI’s contextual retrieval, and LlamaParse to index and improve slide deck content visually and textually, reduce costs, and improve retrieval accuracy with detailed contextual summaries. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_contextual_retrieval_rag.ipynb), [Tweet](https://x.com/llama_index/status/1843317002041274450).
  -  Guide to Multimodal RAG for Market Research Reports: Set up a RAG pipeline with LlamaParse to interpret and query numeric and visual data from complex charts in market research surveys. [Notebook](https://github.com/run-llama/llamacloud-demo/blob/main/examples/multimodal/mm_market_survey_ai.ipynb), [Tweet](https://x.com/llama_index/status/1840920249346240534).



##  **✨ Framework:**


-  Guide to Contextual Retrieval RAG: Utilize AnthropicAI&#39;s technique for enhanced retrieval by appending metadata to each document chunk, using prompt caching to reduce token costs. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/contextual_retrieval.ipynb), [Tweet](https://x.com/llama_index/status/1841210062167294287).
  -  We have updated Create-Llama to simplify starting with multi-agent systems via LlamaIndex. The latest version features interactive dialogues with agents, making it perfect for creating content like blog posts. [Tweet](https://x.com/MarcusSchiesser/status/1841423248954909057).
  -  We have integrated Box tools with LlamaIndex for enabling advanced searches, content extraction from your Box content. [BlogPost](https://medium.com/box-developer-blog/introducing-box-tools-for-llamaindex-dc5daaa1c284), [Tweet](https://x.com/llama_index/status/1841587489527759085).
  -  We have integrated OpenAI&#39;s Realtime API to offer a Voice Chat PDF feature, allowing real-time conversations over documents using LlamaIndex and Next.js. [Code](https://github.com/run-llama/voice-chat-pdf), [Tweet](https://x.com/MarcusSchiesser/status/1842141645082640482).
  -  We have integrated CleanlabAI TLM to minimize hallucinations in RAG, improving reliability by scoring each LLM response for trustworthiness, improving data quality, and boosting system performance. [Docs](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cleanlab_tlm_rag/), [Tweet](https://x.com/llama_index/status/1842259131274817739).



##  💡 **Use-case:**


-  Building a multi-agent system for AI-generated YouTube videos: [Tomisin Jenrola’s](https://x.com/lifeoftomi) project showcases an agent &quot;swarm&quot; that crafts scripts, creates video sequences via Livepeer, and uploads to YouTube, all initiated by a simple language prompt. [Project](https://docs.swarmzero.ai/examples/swarms/livepeer-youtube-video-generator-swarm).



##  **✍️ Community:**


-  [Fahd Mirza&#39;s](https://x.com/fahdmirza) [tutorial](https://www.youtube.com/watch?v=RK0MN_d6mzk) on configuring dynamic retrieval for RAG pipelines with LlamaParse, detailing how to optimize metadata filters.
  -  MongoDB’s [tutorial](https://www.mongodb.com/developer/products/atlas/optimize-relevance-mongodb-llamaindex/) on Optimizing for Relevance Using MongoDB Atlas and LlamaIndex.
  -  [Sourabh Desai’s](https://x.com/thesourabhd) [video tutorial](https://www.youtube.com/live/3mWIFsooibQ) on Building Agents with LlamaIndex &amp; Qdrant.
  -  [Scott Hurrey’s](https://medium.com/@shurrey_54711) [tutorial](https://medium.com/box-developer-blog/explore-secure-rag-techniques-for-content-fa9f68f52bdd) on using Box’s enterprise-grade security with LlamaIndex to deploy secure, permission-aware RAG applications.
  -  [Qdrant’s](https://x.com/qdrant_engine) [tutorial](https://medium.com/@benitomartin/building-a-multimodal-llm-application-with-pymupdf4llm-59753cb44483) on building a Multimodal LLM Application with PyMuPDF4LLM.
  -  [Farzad Sunavala’s](https://hashnode.com/@Farzzy528) [tutorial](https://farzzy.hashnode.dev/building-a-legal-ai-agent-using-azure-ai-search-azure-openai-llamaindex-and-crewai) on Building a Legal AI Agent using Azure AI Search, Azure OpenAI, LlamaIndex, and CrewAI.



##  **📅💻 Webinar And Hackathon:**


-  Join us on October 11th for our second hackathon hosted by [AI Makerspace](https://x.com/AIMakerspace), featuring over $10k in prizes. Start with a pre-event workshop, then participate in the competition on Friday evening.
  -  [Webinar](https://www.youtube.com/watch?v=5-VJrj3FEMk) with [Sepanta Zeighami](https://www.linkedin.com/in/zeighami/) on [NUDGE](https://www.arxiv.org/pdf/2409.02343): Lightweight Non-Parametric Fine-Tuning of Embeddings for Retrieval.



##  **👥 Recruitment:**


-  We are actively seeking talented individuals for our team at LlamaIndex. If you believe you are a good fit for any of the following roles, please feel free to reach out to us.
 [Founding AI Engineer](https://jobs.ashbyhq.com/llamaindex/d9b390a3-2514-4067-86fe-111912f67b56)
  -  [Founding AI Data Engineer](https://jobs.ashbyhq.com/llamaindex/7406b3bd-2ad7-4e79-956b-ae9728fbf2e3)
  -  [Founding AI Engineer, Backend](https://jobs.ashbyhq.com/llamaindex/51d2bc49-b342-4392-856e-c0e2a598dbf6)
  -  [Founding Full-Stack Product Engineer](https://jobs.ashbyhq.com/llamaindex/5db34762-0a45-4cb6-9874-607b6583d530)