---
title: "LlamaIndex Newsletter 2024–01–09"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-09-6209000da2e6"
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







Hola, LlamaIndex Lovers 🦙,

Welcome to another thrilling week at LlamaIndex, filled with vibrant community contributions and enriching educational content. Immerse yourself in our engaging tutorials, guides, community demos, and webinars, all crafted to amplify your LlamaIndex experience. Before we jump into our latest updates, we’re thrilled to share two major announcements:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



🧑‍🏫 **Join Our LlamaIndex Community Office Hours**: Struggling with complex LLM/RAG queries or have feedback that our documentation doesn’t cover? [Register](https://t.co/A16nitoIgV) for our community office hours for a chance to have an enlightening conversation and get your questions answered!

🗺️ [**Explore Our Open-Source Roadmap for 2024**:](https://github.com/run-llama/llama_index/discussions/9888) We’re excited to unveil our ambitious roadmap for the LlamaIndex ecosystem. Over the next 3–6 months, we aim to enhance LlamaIndex’s production readiness, accessibility, and its advanced features, including RAG, agents, and more. This [living document](https://github.com/run-llama/llama_index/discussions/9888) is available on our GitHub discussions page — a must-visit to be part of our exciting journey!

Additionally, if you’ve been working on an interesting project, written an insightful article, or created a captivating video, we’d love to hear about it! Please share your work with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). And remember to subscribe to our newsletter through our [website](https://www.llamaindex.ai/) to get all these exciting updates straight to your inbox

🤩 **The highlights:**

- **Query Pipelines**: Introducing a new declarative API for effortless orchestration of simple to complex RAG query workflows. [Docs](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html#), [Blogpost](/introducing-query-pipelines-025dc2bb0537), [Tweet](https://x.com/llama_index/status/1744406288724017278?s=20).
- **ETL Pipeline Launch**: New repository for setting up production ETL pipelines in RAG/LLM apps, boasting a 4x speed boost and integrating Hugging Face, RabbitMQ, and AWS EKS. [Github Repo](https://github.com/run-llama/llamaindex_aws_ingestion), [Blogpost](/scaling-llamaindex-with-aws-and-hugging-face-e2c71aa64716), [Tweet](https://x.com/llama_index/status/1742226327900721168?s=20).
- **Multimodal ReAct Agent**: Launch of an agent capable of processing text and images, enhancing RAG pipeline and web search functionalities using GPT-4V. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/mm_agent.ipynb), [Tweet](https://x.com/llama_index/status/1742588989884989477?s=20).
- **RAGatouille LlamaPack**: Introduction of an easy-to-use pack for ColBERT retrieval, enabling one-line code integration in LlamaIndex RAG pipelines. [Docs](https://llamahub.ai/l/llama_packs-ragatouille_retriever?from=llama_packs), [Tweet](https://x.com/llama_index/status/1743076579302105338?s=20).
- [**Advanced RAG Cheat Sheet**](/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b): A comprehensive cheat sheet with techniques for RAG enhancement, perfect for both new and experienced LLM users.

**✨ Feature Releases and Enhancements:**

- We have introduced Query Pipelines, a declarative API designed to simplify the creation and customization of advanced RAG workflows. This tool enables the orchestration of query workflows, ranging from basic sequential chains to complex DAGs, tailored to specific use cases. [Docs](https://docs.llamaindex.ai/en/latest/module_guides/querying/pipeline/root.html#), [Blogpost](/introducing-query-pipelines-025dc2bb0537), [Tweet](https://x.com/llama_index/status/1744406288724017278?s=20).
- We have launched a repository for easily setting up a production ETL pipeline for RAG/LLM apps, offering a 4x speed increase over laptop-based operations. This solution integrates Hugging Face, RabbitMQ, Llama Index, and AWS EKS, providing fast document indexing and efficient data handling, complete with an AWS Lambda API endpoint. Ideal for RAG apps transitioning to production, especially on AWS. [Github Repo](https://github.com/run-llama/llamaindex_aws_ingestion), [Blogpost](/scaling-llamaindex-with-aws-and-hugging-face-e2c71aa64716), [Tweet](https://x.com/llama_index/status/1742226327900721168?s=20).
- We have launched the Multimodal ReAct Agent, combining GPT-4V with the ability to process both text and images. This agent can perform tasks like querying a RAG pipeline or conducting web searches based on visual and textual inputs. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/mm_agent.ipynb), [Tweet](https://x.com/llama_index/status/1742588989884989477?s=20).
- RAGatouille LlamaPack: RAGatouille simplifies the use of ColBERT, a more advanced retrieval model compared to dense embedding-based retrieval techniques. This pack allows you to build an end-to-end LlamaIndex RAG pipeline with just one line of code by ingesting documents using any of our 150+ data loaders, combined with your preferred LLM for response synthesis. [Docs](https://llamahub.ai/l/llama_packs-ragatouille_retriever?from=llama_packs), [Tweet](https://x.com/llama_index/status/1743076579302105338?s=20).
- We have integrated with Pathway’s open data processing framework which enables us to handle dynamic data sources in production, automatically updating indexes based on real-time changes, ensuring up-to-date and accurate query responses. [Docs](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo.html), [Tweet](https://x.com/llama_index/status/1741862685103579476?s=20).
- [**Ian McCrystal**](https://twitter.com/ianmst) has added the StripeDocsLoader to LlamaHub, enabling a quick setup of RAG over Stripe’s documentation using Llama Index. [Docs](https://llamahub.ai/l/stripe_docs).
- [Jeremy Dyer](https://twitter.com/mightyjeremy) has integrated NVIDIA’s Triton Inference Server which allows you to run optimized inference on any AI framework. It supports the TensorRT-LLM backend, enhancing LLM performance on Nvidia GPUs. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/nvidia_triton.ipynb), [Tweet](https://x.com/llama_index/status/1744044446029901943?s=20).

**👀 Community Demos**:

- Context-Augmented Agent for Food Delivery: A full-stack application guide by lucastonon for creating an RAG agent. This tool performs in-browser tasks like opening restaurant pages and adding food to carts, purely via voice commands, integrating with Llama Index, Pinecone, OpenAI’s Whisper, LLMs, Function Calling, vue.js, and FastAPI. [Github Repo](https://github.com/lucastononro/llm-food-delivery), [Tweet](https://x.com/llama_index/status/1741987664272986534?s=20).
- [GRDN.AI](https://medium.com/@dheymann314/ai-infused-optimization-in-the-wild-developing-a-companion-planting-app-357e5da29d10): A fascinating side project from Danielle Heymann, using a genetic algorithm and LLM to optimize plant placement based on compatibility. This project harnesses local models from HuggingFace, accessed through LlamaIndex for the LLM part, combining traditional mathematical strategies with LLMs. [Blogpost](https://medium.com/@dheymann314/ai-infused-optimization-in-the-wild-developing-a-companion-planting-app-357e5da29d10), [Tweet](https://x.com/llama_index/status/1742703399081271555?s=20).
- [Build an AI Shopping Assistant with RAG and Agents](https://www.activeloop.ai/resources/use-llama-index-to-build-an-ai-shopping-assistant-with-rag-and-agents/): This assistant can analyze a picture of an item and suggest weather-appropriate accessories. The work by D. Kiedanski and Lucas Micol from Tryolabs explains how to transform APIs into problem-solving tools for a LlamaIndex agent.

**🗺️ Guides:**

- [Guide](/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) to Advanced RAG: Our comprehensive cheat sheet offers insights into improving RAG with techniques like optimized retrieval, effective document use in generation, and interleaving generation with retrieval. Ideal for both new and seasoned LLM users, it’s a must-have resource, complete with LlamaIndex links.
- [Guide](https://github.com/NVIDIA/GenerativeAIExamples/blob/main/notebooks/04_llamaindex_hier_node_parser.ipynb) to building advanced RAG CHATBOT with NVIDIA’S TensorRT-LLM: This chatbot is designed to maintain contiguous document or code blocks, avoiding awkward chunking. It features a stack combining Llama Index’s auto-merging retriever with NVIDIA’s TensorRT-LLM and a custom postprocessor, optimized for RAG using open-source models.

**✍️ Tutorials:**

- BentoML [tutorial](https://www.bentoml.com/blog/building-an-intelligent-query-response-system-with-llamaindex-and-openllm) on Building An Intelligent Query-Response System with LlamaIndex and OpenLLM.
- [Akash Mathur](https://www.linkedin.com/in/akashmathur22/) [tutorial](https://akash-mathur.medium.com/advanced-rag-optimizing-retrieval-with-additional-context-metadata-using-llamaindex-aeaa32d7aa2f) on Advanced RAG: Optimizing Retrieval with Additional Context &amp; MetaData using LlamaIndex.

🎥 **Webinars:**

- Weights &amp; Biases [podcast](https://www.youtube.com/watch?v=xejCaLsYzV4) with Jerry Liu on Revolutionizing AI Data Management.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex, even more, Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)