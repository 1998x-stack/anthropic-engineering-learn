---
title: "LlamaIndex Newsletter 2024-04-23"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-04-23"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 🎥 Demos:  ](#demos)
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







 Hello LlamaIndex Community! 🦙



 Welcome to another thrilling weekly update from LlamaWorld! We&#39;re excited to bring you a variety of outstanding updates, including Cookbooks, demos, guides, and tutorials.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **MistralAI&#39;s 8x22b Model Cookbook:** Released cookbook for MistralAI&#39;s 8x22b model with detailed guidance on RAG, query routing, and tool applications. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/mistralai/), [Tweet](https://x.com/llama_index/status/1780646484712788085).
  -  **Llama 3 Model Cookbook:** A comprehensive cookbook for Meta&#39;s Llama 3 model from simple prompt runs to complex RAG pipeline, agents and tools, accessible directly from Hugging Face. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/llama3_cookbook/), [Tweet](https://x.com/llama_index/status/1781039161325293981).
  -  **create-llama Llama 3 template**: create-llama template for Meta&#39;s Llama 3 to quickly start building full-stack LLM applications using the **`nextjs-llama3` ** template with a single CLI command. [Tweet](https://x.com/jerryjliu0/status/1781843300938666050).







##  **✨ Feature Releases and Enhancements:**


-  We have released a cookbook for the latest MistralAI model, the powerful 8x22b, which sets a new standard for open models. The cookbook covers RAG, query routing, and tool use cases. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/mistralai/), [Tweet](https://x.com/llama_index/status/1780646484712788085).
  -  We have released a cookbook for latest Meta&#39;s new Llama 3 model, available directly from Hugging Face. This guide covers everything from running basic prompts to setting up a full RAG pipeline, agents and tools. [Docs](https://docs.llamaindex.ai/en/latest/examples/cookbooks/llama3_cookbook/), [Tweet](https://x.com/llama_index/status/1781039161325293981).
  -  We have introduced a template for integrating Meta&#39;s Llama 3 in create-llama. Simply run **`npx create-llama` ** and select the **`nextjs-llama3` ** template to build full-stack LLM application with Llama 3 in one CLI command. [Tweet](https://x.com/jerryjliu0/status/1781843300938666050).







##  **🎥 Demos:**


-  [Open Source AI Diagram Generator](https://github.com/rsrohan99/ai-diagram-generator) by [Rohan](https://twitter.com/clusteredbytes) using LlamaIndex&#39;s Pydantic program with partial JSON parsing and Vercel AI SDK to generate and stream diagrams dynamically for an enhanced user experience.
  -  [DREAM](https://github.com/aishwaryaprabhat/goku/tree/main/goku/dream): A Distributed RAG Experimentation Framework by Aishwarya Prabhat, featuring a full-stack blueprint for optimizing RAG setups in a distributed environment. This setup includes Ray for computing, LlamaIndex for advanced techniques, Ragas for synthetic data, MinIO, MLflow, Project Jupyter, and ArgoCD.
  -  [Firecrawl](https://firecrawl.dev/?ref=github) from [Mendable](https://www.mendable.ai/) is an API service that crawls a given URL and converts its content, including all accessible subpages, into clean markdown format. It utilizes LlamaParse from LlamaIndex for PDF parsing.







##  **🗺️ Guides:**


-  [Guide](https://qdrant.tech/documentation/examples/hybrid-search-llamaindex-jinaai/) to integrating Qdrant Hybrid Cloud with LlamaIndex, featuring JinaAI embeddings, MistralAI&#39;s Mixtral 8x7b, and our LlamaParse document parser.
  -  [Guide](https://www.elastic.co/search-labs/blog/rag-with-llamaIndex-and-elasticsearch) to building RAG using completely open and free components from Elastic, featuring Ollama and MistralAI, demonstrates how to assemble a RAG application with LlamaIndex using entirely free software.
  -  [Guide](https://www.youtube.com/watch?v=JLmI0GJuGlY) to Building a Code-Writing Agent: [TechWithTimm](https://twitter.com/TechWithTimm) demonstrated how to create an agent that writes code by reading your documentation. Learn how to set up local LLMs with Ollama, parse documentation using LlamaParse, build an agent, and teach it to write code.
  -  [Guide](https://medium.com/@diagnosta/lora-fine-tuning-of-embedding-models-using-llamaindex-a60b823a2c94) to Fine-tuning Embedding Models for RAG with LoRA by Mariboo demonstrates how to enhance Hugging Face models using LlamaIndex&#39;s finetuning techniques, including steps from quantization to fine-tuning with QLoRA.







##  **✍️ Tutorials:**


-  Khye Wei&#39;s [tutorial](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/advanced-rag-with-azure-ai-search-and-llamaindex/ba-p/4115007) from Microsoft demonstrates how to use LlamaIndex with Azure&#39;s AI Search to create powerful RAG applications, including Hybrid Search, Query Rewriting, and SubQuestionQuery Engine.
  -  [Hanane Dupouy](https://www.linkedin.com/in/hanane-d-algo-trader/)&#39;s [tutorial](https://www.linkedin.com/posts/hanane-d-algo-trader_react-financial-agent-llamaindex-activity-7186333474256035840-jyQV/?utm_source=share&utm_medium=member_desktop) on Building a Finance Agent with LlamaIndex to query public companies with tools for looking up stock prices, summarizing financial news, and plotting stock data, all streamlined through LlamaIndex&#39;s ReAct agent and API abstractions.
  -  [Andy Singal](https://twitter.com/andysingal)&#39;s [tutorial](https://ai.gopubby.com/enhancing-document-retrieval-with-memory-a-tutorial-for-llamaindex-with-colbert-based-agent-1c3c47461122) on Building a ColBERT-powered Retrieval Agent with Memory demonstrates how to enhance a RAG pipeline with &quot;state&quot; storage for a more personalized, conversational assistant using LlamaIndex&#39;s custom agent and query pipeline abstractions.
  -  Mariboo’s [tutorial](https://medium.com/@diagnosta/lora-fine-tuning-of-embedding-models-using-llamaindex-a60b823a2c94) on Fine-tuning Embedding Models for RAG with LoRA using LlamaIndex&#39;s finetuning abstractions.