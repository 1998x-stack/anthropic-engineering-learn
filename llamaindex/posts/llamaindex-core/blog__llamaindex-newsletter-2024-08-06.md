---
title: "LlamaIndex Newsletter 2024-08-06"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-08-06"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:   ](#feature-releases-and-enhancements)



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







 Greetings, Llama Lovers! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re excited to share our latest updates including dynamic features like LlamaIndex Workflows and retrieval capabilities in LlamaParse. Check out our in-depth guides, tutorials, and the upcoming webinars that will help you make the most of these new developments.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **LlamaIndex Workflows Launched:** LlamaIndex Workflows, a new event-driven architecture for building multi-agent applications, supports batching, async operations, and streaming. Agents subscribe to and emit events for complex, readable, Pythonic orchestration. [Blogpost](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex), [Tweet](https://x.com/llama_index/status/1819048068798616058).
  -  **Dynamic Retrieval Feature in LlamaParse:** A new feature in LlamaParse now supports dynamic retrieval for QA assistants, enabling both chunk-level and file-level document retrieval based on query similarity to intelligently route queries. [Blogpost](https://www.llamaindex.ai/blog/dynamic-retrieval-with-llamacloud), [Notebook](https://github.com/run-llama/llamacloud-demo/blob/main/examples/10k_apple_tesla/demo_file_retrieval.ipynb), [Tweet](https://x.com/llama_index/status/1818337133746360623).
  -  **LongRAG LlamaPack:** LongRAG is now available as a LlamaPack in LlamaIndex, utilizing larger document chunks and long-context LLMs for more effective synthesis. [Notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-longrag/examples/longrag.ipynb), [Tweet](https://x.com/llama_index/status/1818802688274100578).



##  **✨ Feature Releases and Enhancements: **


-  We have launched LlamaIndex Workflows, a new event-driven way to build multi-agent applications where each agent acts as a component that subscribes to and emits events, allowing for complex, readable, and Pythonic orchestration with enhanced support for batching, async operations, and streaming. [Blogpost](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex), [Tweet](https://x.com/llama_index/status/1819048068798616058).
  -  We have introduced a new feature in LlamaParse to improve your QA assistant with our latest capability for dynamic retrieval, allowing both chunk-level and file-level retrieval. This feature enables the retrieval of entire documents based on query similarity, which supports building agents that can intelligently route queries based on their content. [Blogpost](https://www.llamaindex.ai/blog/dynamic-retrieval-with-llamacloud), [Notebook](https://github.com/run-llama/llamacloud-demo/blob/main/examples/10k_apple_tesla/demo_file_retrieval.ipynb), [Tweet](https://x.com/llama_index/status/1818337133746360623).
  -  We have launched LongRAG as a LlamaPack in LlamaIndex. LongRAG simplifies retrieval by using larger document chunks and leveraging long-context LLMs for synthesis. [Notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-longrag/examples/longrag.ipynb), [Tweet](https://x.com/llama_index/status/1818802688274100578).



 **🗺️ Guides:**


-  [Guide](https://docs.llamaindex.ai/en/latest/examples/workflow/react_agent/) to building a ReAct agent from scratch using LlamaIndex workflows.
  -  [Guide](https://docs.llamaindex.ai/en/latest/examples/workflow/rag/) to Building an Event-Driven RAG Pipeline with LlamaIndex, featuring distinct event-driven steps for retrieval, reranking, and synthesis, enhanced with graph tracing and async processing.
  -  [Guide](https://docs.llamaindex.ai/en/latest/module_guides/observability/#mlflow) to MLflow in LlamaIndex to manage, deploy, and monitor your genAI applications with MLflow&#39;s tracking, packaging, evaluation, and tracing capabilities.



 **✍️ Tutorials:**


-  [Pavan Kumar’s](https://x.com/pavan_mantha1) [tutorial](https://blog.gopenai.com/building-smarter-agents-using-llamaindex-agents-and-qdrants-hybrid-search-50c0ecbbfb0d) on Building Smarter Agents using LlamaIndex Agents and Qdrant’s Hybrid Search.
  -  [Farzad Sunavala’s](https://www.linkedin.com/in/farzadsunavala) [tutorial](https://farzzy.hashnode.dev/rag-observability-and-evaluation-with-azure-ai-search-azure-openai-llamaindex-and-arize-phoenix) on RAG Observability and Evaluation with Azure AI Search, Azure OpenAI, LlamaIndex, and Arize Phoenix.
  -  [Composio’s](https://x.com/composiohq) [tutorial](https://github.com/ComposioHQ/composio/tree/master/python/examples/pr_agent/pr_agent_llama_index) on building a PR review agent using Composio&#39;s GitHub/Slack tools and LlamaIndex agent abstractions.
  -  [Benito Martin’s](https://medium.com/@benitomartin) [tutorial](https://medium.com/@benitomartin/find-your-code-scaling-a-llamaindex-and-qdrant-application-with-google-kubernetes-engine-2db126f16344) on Scaling a LlamaIndex and Qdrant Application with Google Kubernetes Engine.
  -  [Chew Loong Nian’s](https://medium.com/@chewloongnian) [tutorial](https://pub.towardsai.net/introducing-llamaextract-beta-transforming-metadata-extraction-for-enhanced-rag-queries-de3d74d34cd7) on Transforming Metadata Extraction for Enhanced RAG Queries using LlamaExtract.
  -  [Pavan Kumar’s](https://x.com/pavan_mantha1) [tutorial](https://medium.com/@manthapavankumar11/practical-implementation-of-agentic-rag-workflows-with-llama-index-and-qdrant-3b6622cd3124) on Practical Implementation of Agentic RAG Workflows with Llama-Index and Qdrant.
  -  AI21 Labs [tutorial](https://www.llamaindex.ai/blog/jamba-instruct-s-256k-context-window-on-llamaindex) on using Jamba-Instruct Model with LlamaIndex.



 **🎤 Webinars And Hackathons:**


-  [Join us](https://lu.ma/ka5xtyqo) for a webinar on August 8th with [Dedy Kredo](https://x.com/DedyKredo) from [CodiumAI](https://x.com/CodiumAI) on using RAG with LlamaIndex to help build a code generation solution that’s contextually aware of the right elements of source code.
  -  [Join us](https://lu.ma/p13pkknm?tk=SsniSt) on RAG Hack Night at GitHub with [Weaviate](https://x.com/weaviate_io), [Neosync](https://x.com/neosynccloud), [Arize AI](https://x.com/arizeai) on August 13th.