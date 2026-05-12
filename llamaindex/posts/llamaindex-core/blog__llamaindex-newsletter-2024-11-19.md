---
title: "LlamaIndex Newsletter 2024-11-19"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-11-19"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ 🗺️ LlamaParse And LlamaParse:  ](#llamaparse-and-llamaparse)
- [ ✨ Framework:  ](#framework)
- [ 💡 Use-case:  ](#use-case)
- [ ✍️ Community:  ](#community)
- [ 🎙️Webinar:  ](#webinar)



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











 Hello, Llama Followers! 🦙



 Welcome to this week’s edition of the LlamaIndex newsletter! We’re excited to share updates on dynamic section retrieval, a new RAG technique for cohesive document retrieval, and the integration of ColPali for enhanced multimodal RAG results. This edition also features the launch of create-llama with a &quot;Form Filler&quot; agent for Typescript applications, and a guide to building multimedia research report generators combining text and images. Don’t miss these updates along with interesting use cases and tutorials from the community.



 If you haven&#39;t explored LlamaParse yet, make sure to [sign up](https://cloud.llamaindex.ai/) and [get in touch with us](https://www.llamaindex.ai/contact) to discuss your specific enterprise use case.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Dynamic Section Retrieval Introduced:** A new RAG technique fetches entire document sections cohesively with metadata and a two-pass retrieval process. [Cookbook](https://github.com/run-llama/llama_parse/blob/main/examples/advanced_rag/dynamic_section_retrieval.ipynb), [Tweet](https://x.com/llama_index/status/1856743483941556640).
  -  **ColPali Integration for Multi-Modal RAG:** ColPali as re-ranker combining Cohere’s multimodal embeddings with ColPali for precise text and image-based results. [Cookbook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/node_postprocessor/ColPaliRerank.ipynb), [Tweet](https://x.com/llama_index/status/1856388716354515279).
  -  **Create-Llama v0.3.12 Launched:** The new version includes a &quot;Form Filler&quot; agent, streamlining LlamaIndex Workflow integration for Typescript applications. [Tweet](https://x.com/MarcusSchiesser/status/1856589050129592809).
  -  **Multimedia Research Report Guide:** A tutorial on generating structured reports combining text and images from complex documents using agentic RAG workflows. [Cookbook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_report_generation.ipynb), [Tweet](https://x.com/llama_index/status/1857851103058211215).



##  **🗺️ LlamaParse And LlamaParse:**


-  We have introduced dynamic section retrieval, a new RAG technique that enhances retrieval by ensuring entire sections of a document are fetched cohesively. This approach starts with simple page-level chunking, adds section metadata, and completes with a two-pass retrieval process to maintain contextual continuity. [Cookbook](https://github.com/run-llama/llama_parse/blob/main/examples/advanced_rag/dynamic_section_retrieval.ipynb), [Tweet](https://x.com/llama_index/status/1856743483941556640).
  -  Guide to create a multimedia research report generator that synthesizes insights from complex documents into structured reports combining text and images, utilizing the potential of structured outputs for agentic RAG and report generation workflows. [Cookbook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_report_generation.ipynb), [Tweet](https://x.com/llama_index/status/1857851103058211215).
  -  Guide to create a multi-agent workflow using LlamaParse and OpenAI GPT-4o for generating structured financial reports from 10K documents, demonstrating advanced retrieval of text, tables, and diagrams and detailing the researcher and writer steps involved in producing the final structured analysis. [Tweet](https://x.com/llama_index/status/1858207641732084076).
  -  We have released a blog post and video detail the building blocks for advanced report generation, highlighting how structured outputs, advanced document processing, knowledge base integration, multi-agent workflows, and template systems can automate complex document creation, saving teams 10-15 hours per report. [Video](https://www.youtube.com/watch?v=3jnViQZKYHE), [Blogpost](https://www.llamaindex.ai/blog/building-blocks-of-llm-report-generation-beyond-basic-rag), [Tweet](https://x.com/llama_index/status/1853882080658424226).



##  **✨ Framework:**


-  We have integrated ColPali as a re-ranker for building multimodal RAG, ensuring highly relevant results in both text and image modalities. We use Cohere’s multimodal embeddings for initial retrieval and Cohere, ColPali for re-ranking for text and images respectively before generating responses. [Cookbook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/node_postprocessor/ColPaliRerank.ipynb), [Tweet](https://x.com/llama_index/status/1856388716354515279).
  -  We have launched create-llama v0.3.12 with a &quot;Form Filler&quot; agent, simplifying the integration of LlamaIndex Workflows for Typescript applications. [Tweet](https://x.com/MarcusSchiesser/status/1856589050129592809).
  -  We have launched a new &quot;Ask AI&quot; widget in our Python documentation, powered by RunLLM, featuring an agentic RAG system that provides accurate, up-to-date coding solutions directly in response to user queries. [Tweet](https://x.com/llama_index/status/1857536223566508061).
  -  We have launched day-0 integration with latest Mistral Pixtral model - Pixtral-large. [Docs](https://docs.llamaindex.ai/en/latest/examples/multi_modal/mistral_multi_modal/), [Tweet](https://x.com/llama_index/status/1858591461421519275).



##  💡 **Use-case:**


-  PureML, utilizes LLMs with LlamaIndex, and Reflex to enhance ML dataset management through automated cleaning, intelligent feature creation, and data consolidation. [Blogpost](https://www.llamaindex.ai/blog/pureml-automated-data-clean-up-and-refactoring).
  -  PursuitGov uses LlamaParse to transform their B2G services, parsing 4 million pages in a weekend, boosting document accuracy, and enabling clients to discover opportunities in public sector data. [Blogpost](https://www.llamaindex.ai/blog/pursuit-transforms-public-sector-insights-with-llamaparse).
  -  RAGformation, a tool that automatically generates cloud configurations from natural language descriptions, complete with visual flow diagrams, pricing estimates, and customizable recommendations. [Blogpost](https://www.llamaindex.ai/blog/automatically-generating-cloud-configurations-introducing-ragformation).



##  **✍️ Community:**


-  [Ravi Theja’s](https://x.com/ravithejads) [video tutorial](https://www.youtube.com/watch?v=jxhvIoMqAxQ) on Multi-Modal RAG with ColPali as re-ranker.
  -  [Lingzhen Chen’s](https://medium.com/@lzchen.cs) [tutorial](https://towardsdatascience.com/building-an-interactive-ui-for-llamaindex-workflows-842dd7abedde) on Building an Interactive UI for Llamaindex Workflows.
  -  [Fermin Blanco’s](https://luillyfe.medium.com/) [tutorial](https://medium.com/google-cloud/resume-insights-with-llamaindex-structured-data-extraction-from-unstructured-documents-28c3ff4546a8) on Structured Data Extraction from Unstructured Documents using Llamaindex.
  -  [Tutorial](https://www.llamaindex.ai/blog/using-nvidia-nim-for-agent-enhanced-ai-query-engines-with-llamaindex) on building an Agentic RAG Query Engine with NVIDIA NIM and LlamaIndex.
  -  [Tutorial](https://www.llamaindex.ai/blog/rag-context-refinement-agent) on building a Context Refinement Agent for RAG Systems.



##  🎙️**Webinar:**


-  [Join us](https://www.crowdcast.io/c/how-to-build-genai-apps-with-llamaindex-and-memgraph) in the Memgraph Community Call, where we’ll explore using LlamaIndex and Memgraph for powerful GraphRAG applications.
  -  [Join us](https://lu.ma/zxnxgl5v) for a hands-on workshop on building local agentic RAG applications using open-source LLMs with AIMakerspace on November 27. Learn from experts Dr. Greg Loughnane and Chris Alexiuk about setting up an &quot;on-prem&quot; LLM app stack.