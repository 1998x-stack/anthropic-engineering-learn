---
title: "LlamaIndex Newsletter 2024-07-02"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-02"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 💡 Demos:  ](#demos)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)



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







 Hello, Llama enthusiasts! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! In this issue, we’re excited to bring you exciting updates about `llama-agents` , live demos, extensive guides, and in-depth tutorials to enhance your understanding of our tools.







 Before moving into our newsletter, we have an exciting update on our enterprise offerings. We are thrilled to announce the waitlist release of LlamaParse, our fully-managed ingestion service. [Sign up](http://bit.ly/llamacloud) now if you’re eager to collaborate and build LLM applications with LlamaParse.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Launched Llama-Agents Framework:** Our new alpha-release, llama-agents, enables multi-agent AI systems for production with a distributed architecture, HTTP API communication, and agentic orchestration. It’s designed for easy deployment, scalability, and observability. [Blogpost](https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems), [Tweet](https://x.com/llama_index/status/1806116419995844947).
  -  **`create-llama`  Integrated with LlamaParse:** Streamline your LLM application data pipelines with create-llama, now integrated with LlamaParse for faster setup and efficient system maintenance. [Tweet](https://x.com/MarcusSchiesser/status/1806960577299767767).



##  **✨ Feature Releases and Enhancements:**


-  We have launched llama-agents - new alpha-release framework that enables multi-agent AI systems to go into production. It features a distributed, service-oriented architecture, communication through standard HTTP APIs, agentic orchestration of flows, and is designed for easy deployment, scalability, and observability. [Blogpost](https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems), [Tweet](https://x.com/llama_index/status/1806116419995844947).
  -  create-llama is now integrated with LlamaParse to streamline the setup and management of data pipelines for LLM applications, providing a fast and efficient way to deploy and maintain these systems. [Tweet](https://x.com/MarcusSchiesser/status/1806960577299767767).
  -  We have integrated with DSPy for Optimized RAG by utilizing DSPy’s optimization capabilities with LlamaIndex’s data tools to enhance your query pipelines, optimize prompts, or repurpose DSPy predictors. [Cookbook](https://github.com/stanfordnlp/dspy/blob/main/examples/llamaindex/dspy_llamaindex_rag.ipynb), [Tweet](https://x.com/llama_index/status/1805622494130586078).



##  **💡 Demos:**


-  Automating Code Reviews, [project](https://x.com/GanatraSoham/status/1807787558157320376) by [Composio](https://x.com/composiohq) with LlamaIndex automates code reviews using an AI agent in under 100 lines of code that monitors GitHub PRs, reviews them immediately upon creation, and posts feedback directly to your Slack channel. [Codebase](https://github.com/ComposioHQ/composio/tree/master/python/examples/pr_agent/pr_agent_llama_index).



##  **🗺️ Guides:**


-  [Guide](https://github.com/run-llama/llama-agents/blob/main/examples/agentic_rag_toolservice.ipynb) to Building an Agentic RAG Service with our comprehensive notebook that walks you through creating vector indexes, transforming them into query engines, turning each engine into a tool, providing these tools to agents, and launching the agents as services.
  -  Guide to AI Agents with LlamaIndex: Andrei’s comprehensive workshop from Gen AI Philippines, showcasing LLM applications through LlamaIndex. This beginner-friendly session covers topics from RAG to multi-hop agents. [Video](https://drive.google.com/file/d/1kInT-szYWH71DvKvhhE5XAUVhTl8ZXJA/view), [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/presentations/materials/2024-06-22-genai-philippines.ipynb).



##  **✍️ Tutorials:**


-  [Kingzzm’s](https://x.com/kingzzm) [tutorial](https://generativeai.pub/advanced-rag-retrieval-strategies-hybrid-retrieval-997d39659720) on crafting a custom hybrid retriever using LlamaIndex’s flexible abstractions. This tutorial teaches you how to integrate full text and dense search capabilities from Elastic, and how to write your own reciprocal rank fusion function for optimal retrieval strategy.
  -  [Jeff’s](https://x.com/gswithai) [tutorial](https://www.youtube.com/watch?v=i8ldunneSW8) on which outlines the essential tools needed to construct a report generator using a ReAct agent. Learn how to integrate a RAG tool over guideline documents, a web search tool, and a report generation tool that converts markdown text into PDFs.
  -  [1littlecoder’s](https://x.com/1littlecoder) [tutorial](https://www.youtube.com/watch?v=_aTEI3ISkQA) on llama-agents provides a detailed introduction to transforming multi-agent systems into microservices for production, including setup examples and a walkthrough of the architecture involving the control plane, message queue, and agent services using LlamaIndex abstractions.
  -  [Mervin Praison’s](https://x.com/MervinPraison) [tutorial](https://www.youtube.com/watch?v=nEQCpSd5mx8) on the llama-agents framework provides a concise guide to setting up agent services, from notebook synchronization to server-client interactions, complete with over 10 practical examples.