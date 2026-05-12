---
title: "LlamaIndex Newsletter 2024-04-16"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-04-16"
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







 Hello, LlamaIndex Family! 🦙



 Welcome to another thrilling weekly update from LlamaGalaxy! We&#39;re excited to bring you a variety of outstanding updates, including the Chain of Abstraction LlamaPack, create-tsi, demos, guides, tutorials, and much more.



 Before we delve into these updates, we have an exciting tutorial series on Agents and Tools for you to check out. Perfect for beginners, this series covers everything from advanced QA/RAG implementations to step-wise execution. By the end, you’ll have gained a deeper understanding of how to use agent reasoning with tool use to build simple applications. Check them out:


-  [Overview](https://www.youtube.com/watch?v=-AuHlVMyEA0)
  -  [ReAct agents](https://youtu.be/pRUc6JPw6CY)
  -  [Function Calling agents](https://youtu.be/6INvyrC4WrA)
  -  [Retrieval-Augmented agent](https://youtu.be/K7h17Jjtbzg)
  -  [Controlling tool outputs](https://youtu.be/gFRbkRtLGZQ)
  -  [Agents with step-by-step execution](https://youtu.be/JGkSxdPFgyQ)



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Chain of Abstraction LlamaPack:** Chain of Abstraction technique as llamapack a method enabling multi-step reasoning for enhanced tool use introduced by Silin Gao&#39;s team. [LlamaPack](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/coa_agent.ipynb), [Tweet](https://x.com/llama_index/status/1778845258119524640).
  -  **Create-tsi Toolkit:** Launched a toolkit for building full-stack RAG applications with customizable features like web crawling, local file indexing, and multilingual support, all hosted in EU data centers. [Code](https://github.com/telekom/create-tsi), [Tweet](https://x.com/llama_index/status/1778812761893650551).
  -  **Improved Agent Control**: **`return_direct` ** feature in tools allows direct output returns, reducing costs and enhancing response efficiency. [Docs](https://docs.llamaindex.ai/en/latest/examples/agent/return_direct_agent/), [Tweet](https://x.com/llama_index/status/1778072285003550932).



##  **✨ Feature Releases and Enhancements:**


-  We have introduced the Chain of Abstraction Technique Developed by Silin Gao, and team as LlamaPack, this new method enables LLMs to generate multi-step reasoning chains for efficient sequence planning, enhancing tool use beyond single-shot functions. [LlamaPack](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/coa_agent.ipynb), [Tweet](https://x.com/llama_index/status/1778845258119524640).
  -  We have launched create-tsi: A toolkit in collaboration with T-Systems and Marcus Schiesser to generate GDPR-compliant, full-stack AI applications via a CLI interface. Build enterprise-grade RAG bots with customizable features like web crawling, local file indexing, and multilingual support, all hosted in EU data centers. [Code](https://github.com/telekom/create-tsi), [Tweet](https://x.com/llama_index/status/1778812761893650551).
  -  We have introduced **`return_direct` ** feature in tools that enhances agent controllability by allowing direct output returns as final responses. This optimizes for reduced latency and costs, and effectively halts the agent after crucial actions like booking confirmations or answering queries. [Docs](https://docs.llamaindex.ai/en/latest/examples/agent/return_direct_agent/), [Tweet](https://x.com/llama_index/status/1778072285003550932).



##  **🎥 Demos:**


-  [RAG-enhanced MetaGPT](https://x.com/llama_index/status/1777851305308102845): A robust multi-agent framework that features structured team dynamics for problem-solving, now supercharged with domain-specific knowledge from LlamaIndex modules. This framework supports diverse data inputs, sophisticated retrieval options, and efficient data management for enhanced agent performance.



##  **🗺️ Guides:**


-  [Guide](https://towardsdatascience.com/mastering-rag-systems-from-fundamentals-to-advanced-with-strategic-component-evaluation-3551be31858f) to Building and Evaluating Advanced RAG by Hamza Gharbi for setting up a basic RAG pipeline, defining custom evaluation functions, and optimizing retrieval techniques.
  -  [Paper](https://arxiv.org/abs/2403.11996) by Prof. [Markus J. Buehler](https://twitter.com/ProfBuehlerMIT): Using LLM-Generated Knowledge Graphs to Accelerate Biomaterials Discovery - This study showcases how a comprehensive knowledge graph from over 1000 scientific papers reveals novel insights and connections, driving innovation in biomaterials through art as inspiration. The KG construction was done with the help of LlamaIndex modules.
  -  [Guide](https://aws.plainenglish.io/rag-implementation-using-aws-bedrock-and-llamaindex-62b346fd0156) to Full-Stack RAG Application with AWS Bedrock: Set up Bedrock embeddings, use LlamaIndex for PDF retrieval, and build an interactive Streamlit interface, an ideal resource for enterprises starting with AWS services.
  -  [Guide](https://docs.llamaindex.ai/en/latest/examples/pipeline/query_pipeline_memory/) to Building a Lightweight ColBERT Retrieval Agent: Learn how to create an agent capable of advanced document retrieval and maintaining conversation memory, without the complexity of heavyweight agent frameworks.
  -  [Guide](https://arxiv.org/pdf/2404.01037.pdf) to the Best RAG Techniques: &#39;ARAGOG&#39; [paper](https://arxiv.org/pdf/2404.01037.pdf) by Matous Eibich is a comprehensive evaluation survey exploring various RAG methods from classic vector databases to LlamaIndex&#39;s advanced techniques. Key findings highlight the effectiveness of HyDE, LLM reranking, and sentence window retrieval for improving precision and answer similarity.



##  **✍️ Tutorials:**


-  [Akash Mathur](https://akash-mathur.medium.com/)’s [tutorial](https://akash-mathur.medium.com/data-management-in-llamaindex-smart-tracking-and-debugging-of-document-changes-7b81c304382b) on Data Management in LlamaIndex: Featuring LlamaParse and its open-source counterpart, this tutorial showcases efficient live data handling to minimize costs and latency in LLM applications.
  -  [Leonie](https://twitter.com/helloiamleonie)’s interactive [tutorial](https://lightning.ai/weaviate/studios/chat-with-your-code-rag-with-weaviate-and-llamaindex) to create an app that lets you converse with code from a GitHub repository.
  -  [kingzzm’s](https://twitter.com/kingzzm) [tutorial](https://generativeai.pub/advanced-rag-retrieval-strategies-auto-merging-retrieval-dc3f869654c4) on enhancing RAG Performance to overcome the issue of &#39;broken&#39; context in RAG construction by dynamically creating contiguous chunks with auto-merging retrieval.
  -  [Activeloop](https://twitter.com/activeloop)’s [tutorial](https://www.activeloop.ai/resources/ai-pill-identifier/) on Multimodal RAG for Pill Search teaches how to identify pills using images and text. This helps in identifying unknown pills, checking drug interactions and side effects, and confirming proper dosage amounts.
  -  Fanghua Yu&#39;s [tutorial](https://medium.com/@yu-joshua/using-llamaparse-for-knowledge-graph-creation-from-documents-3bd1e1849754) on using LlamaParse for Knowledge Graph Creation from Documents.



##  🎥 **Webinars:**


-  [Webinar](https://www.youtube.com/watch?v=pira_p6aRVA) with [Tianjun Zhang](https://twitter.com/tianjun_zhang) and [Shishir Patil](https://twitter.com/shishirpatil_), the two lead co-authors of RAFT, where they presented RAFT and discussed fine-tuning and RAG.