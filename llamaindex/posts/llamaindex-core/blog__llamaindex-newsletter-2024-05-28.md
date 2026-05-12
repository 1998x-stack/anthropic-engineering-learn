---
title: "LlamaIndex Newsletter 2024-05-28"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-05-28"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 🗺️ Guides:  ](#guides)
- [ 🖥️ Demos:  ](#demos)
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







 Greetings, LlamaIndex Family! 🦙



 Welcome to your latest weekly update from LlamaIndex! We&#39;re excited to present a variety of outstanding integration updates, detailed guides, demos, educational tutorials, and informative webinars this week.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Secure Code Execution with AzureCodeInterpreterTool:** Securely run LLM-generated code with Azure Container Apps, integrated with LlamaIndex for safe code execution.
  -  **Build Automated Email Agents:** Create email agents with MultiOn and LlamaIndex that autonomously read, index, and respond to emails.
  -  **LlamaFS for Organized Files:** Alex Reibman&#39;s team developed LlamaFS to automatically structure messy file directories, enhanced by Llama 3 and Groq Inc.&#39;s API.
  -  **RAGApp&#39;s No-Code Chatbots:** Deploy RAG chatbots easily with RAGApp&#39;s no-code interface, fully open-source and cloud-compatible.



##  **✨ Feature Releases and Enhancements:**


-  We have launched Azure Container Apps dynamic sessions to securely run LLM-generated code in a sandbox. Integrated into LlamaIndex, this feature ensures safe execution of complex code tasks by your agents. Set up a session pool on Azure, add the AzureCodeInterpreterTool to your agent, and you’re ready to go. [Blogpost](https://www.llamaindex.ai/blog/secure-code-execution-in-llamaindex-with-azure-container-apps-dynamic-sessions), [Tweet](https://x.com/llama_index/status/1792958928357335115).
  -  We have integrated with the open source Nomic embed, now fully operable locally. This integration allows for completely local embeddings and introduces a dynamic inference mode that optimizes embedding latency. The system automatically selects between local and remote embeddings based on speed, ensuring optimal performance. [Docs](https://docs.llamaindex.ai/en/stable/examples/embeddings/nomic/), [Tweet](https://x.com/llama_index/status/1793677965978673598).
  -  We have integrated the Vespa vector store, supporting hybrid search with BM25. [Docs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/), [Tweet](https://x.com/llama_index/status/1794106979213869413).
  -  We have integrated with MyMagic AI to facilitate batch data processing for GenAI applications. This setup allows you to pre-process large datasets with an LLM, enabling advanced analysis and querying capabilities. [Docs](https://www.llamaindex.ai/blog/batch-inference-with-mymagic-ai-and-llamaindex), [Tweet](https://x.com/llama_index/status/1793385512386150856).



##  **🗺️ Guides:**


-  [Guide](https://www.llamaindex.ai/blog/automate-online-tasks-with-multion-and-llamaindex) to building an automated Email Agent with MultiOn and LlamaIndex that can autonomously read and index emails for easy retrieval and draft responses using advanced browsing capabilities.
  -  [Guide](https://www.koyeb.com/tutorials/using-llamaindex-and-mongodb-to-build-a-job-search-assistant#create-a-job-indexing-api-endpoint) to building Full-Stack Job Search Assistant by Rishi Raj Jain using Gokoyeb, MongoDB, and LlamaIndex. This guide takes you through setting up MongoDB Atlas, crafting a Next.js application, developing UI components, and deploying your app on Koyeb, complete with real-time response streaming and continuous job updates.



##  **🖥️ Demos:**


-  LlamaFS, a project developed by [Alex Reibman](https://x.com/AlexReibman) and his team, automatically organizes messy file directories into neatly structured folders with interpretable names. Enhanced by Llama 3 and supported by Groq Inc.&#39;s API, Ollama&#39;s fully local mode and LlamaIndex, this tool significantly improves file management efficiency. [Code](https://github.com/iyaja/llama-fs), [Tweet](https://x.com/llama_index/status/1794762651769430381).
  -  RAGApp, a project developed by [Marcus Schiesser](https://x.com/MarcusSchiesser), offers a no-code interface for configuring RAG chatbots as simply as GPTs by OpenAI. This fully open-source docker container can be deployed on any cloud platform, allowing users to set up the LLM, define system prompts, upload knowledge bases, and launch chatbots via UI or API. [Code](https://github.com/ragapp/ragapp), [Tweet](https://x.com/llama_index/status/1794030544415818062).



##  **✍️ Tutorials:**


-  [Phil Chirchir’s](https://x.com/ronoh4) [tutorial](https://medium.com/@leighphil4/dspy-rag-with-llamaindex-programming-llms-over-prompting-1b12d12cbc43) on DSPy RAG with LlamaIndex. It demonstrates how to integrate DSPy bootstrapping models with a LlamaIndex RAG pipeline powered by LlamaParse.
  -  [Pavan Kumar’s](https://x.com/pavan_mantha1) [tutorial](https://towardsdev.com/harnessing-gpt-4os-vision-for-advanced-search-building-image-embeddings-with-qdrant-5dd887cf40b5) on advanced image indexing for RAG demonstrates how to combine image embeddings with structured annotations using multimodal models. It details how to enhance image search with LlamaIndex and Qdrant Engine’s capabilities.
  -  Jayita Bhattacharyya’s [tutorial](https://itsjb13.medium.com/building-a-rag-chatbot-using-llamaindex-groq-with-llama3-chainlit-b1709f770f55) on Building a RAG Chatbot using Llamaindex, Groq with Llama3 &amp; Chainlit.



##  **📹 Webinar:**


-  [Webinar](https://www.youtube.com/watch?v=_1JZfv7r4mY) with OpenDevin team to learn how to build an Open-Source Coding Assistant using OpenDevin.