---
title: "LlamaIndex Newsletter 2024-07-09"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-09"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 💡 Demos:  ](#demos)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 🎥 Webinar:  ](#webinar)



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







 Hello, Llama Lovers! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re thrilled to share some exciting updates about `llama-agents` , along with demos, extensive guides, and in-depth tutorials to enhance your understanding of our tools.







 Before we dive into our newsletter, we’re excited to announce the return of Community Office Hours. If you have use-cases, in-depth questions, or feedback for the team at LlamaIndex, join us during our community office hours! We’ll set up a 15-30 minute Zoom call to discuss it.



 [**Sign up here**](https://docs.google.com/forms/d/e/1FAIpQLSefrnmxQWD-1OhSP51kUKtdbw9EGDjrMLefkZFACKD19TKsuQ/viewform?usp=sf_link) to participate.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Multi-Agent Kubernetes Kit Launched:** Deploy multi-agent systems easily with our new Kubernetes Starter Kit featuring ready-to-use tools and configurations. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/docker-kubernetes), [Tweet](https://x.com/llama_index/status/1807801281324765469).
  -  **Enhanced Communication with RabbitMQ:** Boost multi-agent system reliability and scalability in production with our new RabbitMQ integration. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/rabbitmq), [Tweet](https://x.com/llama_index/status/1810342085171855753).
  -  **Reflection as a Service Guide:** Improve agent reliability with our guide on building Reflection as a Service, perfect for output validation and correction. [Notebook](https://github.com/run-llama/llama-agents/blob/main/examples/reflection/toxicity_reflection_service.ipynb), [Tweet](https://x.com/llama_index/status/1808898730638389262).
  -  **Corrective RAG as a Service Guide:** Create a self-correcting RAG that ensures context relevance and integrates search fallbacks before generation. [Notebook](https://github.com/run-llama/llama-agents/blob/main/examples/corrective_rag.ipynb), [Tweet](https://x.com/llama_index/status/1809282069606068486).
  -  **Tutorial series on Property Graphs:** 6-part video series on Property Graphs in LlamaIndex using MistralAI, Neo4j, and Ollama. [Videos](https://www.youtube.com/playlist?list=PLTZkGHtR085ZYstpcTFWqP27D-SPZe6EZ), [Tweet](https://x.com/llama_index/status/1810410943215710510).



##  **✨ Feature Releases and Enhancements:**


-  We have launched a Multi-Agent on Kubernetes Starter Kit to build and deploy a multi-agent system using Docker Compose and Kubernetes using llama-agents. This kit includes prebuilt agent loops and tools, as well as Dockerfiles and Kubernetes manifests for easy production deployment. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/docker-kubernetes), [Tweet](https://x.com/llama_index/status/1807801281324765469).
  -  We have integrated RabbitMQ with llama-agents to enhance multi-agent communication, offering scalability and reliability for handling large request volumes in production. [Notebook](https://github.com/run-llama/llama-agents/tree/main/examples/rabbitmq), [Tweet](https://x.com/llama_index/status/1810342085171855753).
  -  [[Yi-01.AI](http://Yi-01.AI)]([http://Yi-01.AIhttps](http://Yi-01.AIhttps)://x.com/01AI_Yi) is integrated with LlamaIndex for enhanced retrieval and indexing, streamlining the development of smarter, faster RAG applications. [Docs](https://docs.llamaindex.ai/en/latest/examples/llm/yi/).
  -  We have launched a [6-part video series](https://www.youtube.com/playlist?list=PLTZkGHtR085ZYstpcTFWqP27D-SPZe6EZ) on Property Graphs in LlamaIndex using MistralAI, Neo4j and Ollama. [Tweet](https://x.com/llama_index/status/1810410943215710510).



##  **💡 Demos:**


-  [OpenContracts](https://github.com/JSv4/OpenContracts) by [John Scrudato](https://x.com/johnscrudato): A fully open-source, AI-powered Document Analytics Tool, integrates genAI capabilities and LlamaIndex for robust query handling and data extraction across documents. This tool is particularly valuable for legal analysis, enabling users to manage, process, and query vast arrays of contracts and legal documents. [Docs](https://jsv4.github.io/OpenContracts/).



##  **🗺️ Guides:**


-  Guide to build Reflection as a Service to enhance agent reliability with our new standalone service, ideal for validating and correcting outputs across multiple agents. [Notebook](https://github.com/run-llama/llama-agents/blob/main/examples/reflection/toxicity_reflection_service.ipynb), [Tweet](https://x.com/llama_index/status/1808898730638389262).
  -  Guide to build Corrective RAG as a Service, a self-correcting RAG that dynamically validates context relevance, seamlessly integrating web search fallbacks before generation. [Notebook](https://github.com/run-llama/llama-agents/blob/main/examples/corrective_rag.ipynb), [Tweet](https://x.com/llama_index/status/1809282069606068486).



##  **✍️ Tutorials:**


-  [Pavan Kumar’s](https://x.com/pavan_mantha1) [tutorial](https://blog.gopenai.com/harnessing-ai-at-the-edge-building-a-rag-system-with-ollama-qdrant-and-raspberry-pi-45ac3212cf75) to build a RAG pipeline that lives on a Raspberry Pi device with docker, Ollama, Qdrant, and using LlamaIndex as the orchestration layer.
  -  [Trade Mamba’s](https://x.com/AdiDror6) video [tutorial](https://www.youtube.com/watch?v=uOLhleiOM84) to build an AI-enabled trading assistant using LlamaIndex’s agent/tool/RAG abstractions for tasks like tracking portfolio values, managing stock orders, and conducting vector searches for semantic information.
  -  [Giskard’s](https://x.com/giskard_ai) [toolkit](https://docs.giskard.ai/en/stable/reference/notebooks/RAGET.html) enables diverse question generation featuring question types like simple, complex, distracting, situational, double, and conversational for RAG evaluation, as demonstrated in the tutorial on using a LlamaIndex pipeline with an IPCC Climate Report.
  -  [Pavan Kumar’s](https://x.com/pavan_mantha1) [tutorial](https://blog.stackademic.com/building-a-multi-document-react-agent-for-financial-analysis-using-llamaindex-and-qdrant-72a535730ac3) demonstrates building a Multi-Document Financial Analyst Agent using LlamaIndex RAG and ReAct tools, analyzing categorized SEC documents with SnowflakeDB embeddings and MistralAI via Ollama.
  -  Ross A.’s [tutorial](https://medium.com/@rossashman/the-art-of-rag-part-4-retrieval-evaluation-427bb5db0475) on retrieval evaluations for RAG delves into essential metrics like precision@K and NDCG, and demonstrates how to convert datasets to BEIR format for assessing LlamaIndex retrievers.



##  **🎥 Webinar:**


-  Join us for a [webinar](https://lu.ma/dywrdye5) on July 10th, featuring Jerry Liu (LlamaIndex) and Ayush Thakur (Weights &amp; Biases) on **A Principled Approach to RAG Experimentation + Evaluation** to learn how to build, evaluate, and refine RAG pipelines.