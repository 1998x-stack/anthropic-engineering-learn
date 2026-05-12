---
title: "LlamaIndex Newsletter 2024-07-16"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-16"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 💡 Demos:  ](#demos)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 🎤 Events:  ](#events)



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







 Hello, Llama Family! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re thrilled to share some exciting updates about our products, the implementation of GraphRAG, demos that have achieved over $1M in ARR, extensive guides, in-depth tutorials, and hackathons.







 Before we get into the details of our newsletter, we’re thrilled to share the beta launch of LlamaParse. This new data processing layer boosts RAG workflows with sophisticated parsing, indexing, and retrieval functions. Alongside this, we’re also introducing LlamaTrace in partnership with Arize AI, which provides unmatched tracing, observability, and evaluation capabilities for LLM application workflows.







 Signup here: [cloud.llamaindex.ai](https://t.co/yQGTiRSNvj)







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **LlamaParse Launch:** We’ve launched the beta release of LlamaParse, a data processing layer designed to enhance RAG workflows with state-of-the-art parsing, indexing, and retrieval capabilities. [Blogpost](https://www.llamaindex.ai/blog/llamacloud-built-for-enterprise-llm-app-builders), [Tweet](https://x.com/llama_index/status/1810716602247348242).
  -  **LlamaTrace Launch:** In collaboration with Arize AI, we’ve introduced LlamaTrace, offering unmatched tracing, observability, and evaluation capabilities for LLM application workflows. It features detailed call stack tracing, one-click setup through LlamaIndex, and seamless integration with LlamaParse. [Blogpost](https://www.llamaindex.ai/blog/arize-ai-and-llamaindex-roll-out-joint-platform-for-evaluating-llm-applications), [Tweet](https://x.com/llama_index/status/1811462543535464796).
  -  **GraphRAG Implementation:** Implementation of GraphRAG with LlamaIndex, focusing on graph generation, community building, summaries, and community-based retrieval to improve answer aggregation. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/GraphRAG_v1.ipynb), [Tweet](https://x.com/llama_index/status/1812517033445396754).
  -  **Redis Queue Integration with Llama-Agents:** We have integrated Redis Queue with llama-agents to boost coordination and communication in multi-agent workflows, ensuring robust performance. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/redis/simple-redis-app), [Tweet](https://x.com/llama_index/status/1812202419025293784).



##  **✨ Feature Releases and Enhancements:**


-  We have launched the beta release of LlamaParse, a data processing layer that enhances RAG workflows with advanced parsing, indexing, and retrieval capabilities. [Blogpost](https://www.llamaindex.ai/blog/llamacloud-built-for-enterprise-llm-app-builders), [Tweet](https://x.com/llama_index/status/1810716602247348242).
  -  We have launched an implementation[beta] of GraphRAG concepts with LlamaIndex focussing on graph generation, building communities and community summaries, and community-based retrieval to aggregate answers from summaries. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/GraphRAG_v1.ipynb), [Tweet](https://x.com/llama_index/status/1812517033445396754).
  -  We have integrated Redis Queue with llama-agents to enhance coordination in multi-agent workflows, allowing for robust communication. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/redis/simple-redis-app), [Tweet](https://x.com/llama_index/status/1812202419025293784).
  -  We have introduced LlamaTrace in collaboration with Arize AI, offering unparalleled tracing, observability, and evaluation capabilities for LLM application workflows. LlamaTrace stands out for its detailed tracing, which logs the entire call stack, one-click setup through LlamaIndex, and seamless integration with LlamaParse for easy access and authentication. [Blogpost](https://www.llamaindex.ai/blog/arize-ai-and-llamaindex-roll-out-joint-platform-for-evaluating-llm-applications), [Tweet](https://x.com/llama_index/status/1811462543535464796).
  -  We have integrated NebulaGraph with LlamaIndex, enhancing PropertyGraph capabilities with sophisticated extractors, customizable properties on nodes and edges, and advanced retrieval options. [Docs](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_nebula/), [Tweet](https://x.com/llama_index/status/1811190191597773282).



##  **💡 Demos:**


-  [Lyzrai](https://www.llamaindex.ai/blog/case-study-lyzr-taking-autonomous-ai-agents-to-usd1m-arr-with-llamaindex) has achieved over $1M ARR using LlamaIndex! This full-stack autonomous AI agent framework enhances AI sales and marketing functions with LlamaIndex’s data connectors and RAG capabilities, boasting rapid revenue growth, high accuracy, and customer satisfaction.



##  **🗺️ Guides:**


-  [Guide](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_rag_slide_deck.ipynb) to Multi-Modal RAG for Document Processing that introduces a multi-modal RAG architecture using LlamaParse, LlamaIndex, and GPT-4o, designed to handle complex slide decks. [Tweet](https://x.com/llama_index/status/1812963306032013586).
  -  [Guide](https://x.com/llama_index/status/1812157431788835094) to using LlamaParse and GPT-4o for Financial Report RAG to to effectively parse and synthesize complex financial documents, enhancing clarity and accuracy in data analysis.
  -  [Guide](https://github.com/meta-llama/llama-recipes/tree/main/recipes/3p_integrations/llamaindex/dlai_agentic_rag) to Building Agentic RAG with Llama3: Explore our comprehensive cookbooks, created in collaboration with AI at Meta, featuring advanced techniques from routing and tool use to constructing complex agent reasoning loops and multi-document agents using purely local models like Llama3.



##  **✍️ Tutorials:**


-  [1LittleCoder’s](https://x.com/1littlecoder) [video tutorial](https://www.youtube.com/watch?v=aiySmi5JocQ) demonstrates how to deploy self-hosted llama-agents using Arcee AI, MistralAI, and Ollama, including setup, local model integration, and tool development.
  -  [kingzzm’s](https://x.com/kingzzm) [tutorial](https://ai.gopubby.com/advanced-rag-retrieval-strategies-flow-and-modular-672493acb4a7) on using LlamaIndex to build advanced RAG flows, detailing how to compose and visualize each step from basic retrieval and prompting to advanced techniques and evaluation with RAGAS.
  -  [Mervin Praison’s](https://x.com/MervinPraison) [tutorial](https://www.youtube.com/watch?v=nEQCpSd5mx8) on using llama-agents, detailing the framework’s purpose, a step-by-step setup guide for multi-agent services, and how it stands out from other frameworks.



##  **🎤 Events:**


-  [Join our online hackathon](https://lablab.ai/event/llama-3-ai-hackathon) this Friday, 19th, to build AI apps with Llama 3 from Meta and win cash, credits, and prizes from us and our co-hosts [TogetherAI](https://x.com/togethercompute), [Milvus](https://x.com/milvusio), and [LablabAI](https://x.com/lablabai).