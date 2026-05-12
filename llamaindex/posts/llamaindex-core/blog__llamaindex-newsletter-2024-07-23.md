---
title: "LlamaIndex Newsletter 2024-07-23"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-23"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ ✨ Feature Releases and Enhancements:  ](#feature-releases-and-enhancements)
- [ 💡 Use-cases:  ](#use-cases)
- [ 🗺️ Guides:  ](#guides)
- [ ✍️ Tutorials:  ](#tutorials)
- [ 🎤 Talks, Webinars and Podcasts:  ](#talks-webinars-and-podcasts)
- [ 💻 Hackathons:  ](#hackathons)



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







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re thrilled to share some exciting updates about our products, including LlamaParse, LlamaParse, and LlamaAgents. You’ll also find success stories with LlamaParse, extensive guides, in-depth tutorials, and information about upcoming hackathons.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **LlamaParse Updates:** New features including LlamaParse Chat, enhanced Teams collaboration, and expanded integrations with Notion, Slack, Jira, and SharePoint. [Blogpost](https://www.llamaindex.ai/blog/the-latest-updates-to-llamacloud), [Tweet](https://x.com/llama_index/status/1814363518726222119).
  -  **Scaleport AI’s Accelerated Development with LlamaParse:** Scaleport AI boosts development speed and sales with LlamaParse and LlamaIndex, improving data handling and OCR accuracy across multiple industries. [Blogpost](https://www.llamaindex.ai/blog/case-study-how-scaleport-ai-accelerated-development-and-improved-sales-with-llamacloud).
  -  **Claude Sonnet-3.5 Integration with LlamaParse:** Integration of Claude Sonnet-3.5 with LlamaParse improves chart understanding and data extraction capabilities. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/claude_parse.ipynb), [Tweet](https://x.com/llama_index/status/1813249175817232782).
  -  **Multimodal RAG Cookbook:** A new guide for processing text, diagrams, charts, and tables in slide decks using LlamaParse, LlamaIndex, and GPT-4o. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_rag_slide_deck.ipynb), [Tweet](https://x.com/llama_index/status/1812963306032013586).
  -  **Human in the Loop with LlamaAgents:** Implementation includes HumanService for math queries and agent handling for other inquiries, managed via Gradio app and RabbitMQ. [Code](https://github.com/run-llama/llama-agents/tree/main/examples/human-in-the-loop).



##  **✨ Feature Releases and Enhancements:**


-  We have released new features on LlamaParse like LlamaParse Chat for instant conversational data access, enhanced Teams functionality for collaboration, and expanded data integration with connectors for Notion, Slack, Jira, and improved SharePoint support. [Blogpost](https://www.llamaindex.ai/blog/the-latest-updates-to-llamacloud), [Tweet](https://x.com/llama_index/status/1814363518726222119).
  -  We integrated Claude Sonnet-3.5 with LlamaParse to enhance document parsing capabilities, offering advanced chart understanding and structured data extraction with improved validation and scalability. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/claude_parse.ipynb), [Tweet](https://x.com/llama_index/status/1813249175817232782).
  -  We have released a cookbook on Multimodal RAG for processing slide decks rich in text, diagrams, charts, and tables using LlamaParse, LlamaIndex, and GPT-4o, blending text and image data for comprehensive document analysis. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_rag_slide_deck.ipynb), [Tweet](https://x.com/llama_index/status/1812963306032013586).
  -  We have implemented Human in the Loop with LlamaAgents in our new example that integrates a HumanService object for handling math queries and an agent for other queries, all managed through a Gradio app and RabbitMQ messaging. [Code](https://github.com/run-llama/llama-agents/tree/main/examples/human-in-the-loop).
  -  We have made huge improvements to markdown-based table reconstruction in LlamaParse, enabling the parsing of very complex tables while ensuring that rows and columns remain well-aligned. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/demo_advanced.ipynb), [Tweet](https://x.com/llama_index/status/1813355957491273936).
  -  [Marcus Schiesser](https://x.com/MarcusSchiesser) has enhanced [RAGapp](https://github.com/ragapp/ragapp/tree/main), a docker-deployable, enterprise-ready RAG application, with MistralAI and Groq support for rapid inference, and a Cohere reranker to boost result relevance.



##  **💡 Use-cases:**


-  Scaleport AI accelerated development and improved sales with LlamaParse and LlamaIndex to streamline AI development, reducing prototype timelines, simplifying data ingestion, and improving OCR accuracy across key industries like Legal, eCommerce, Real Estate, and Finance. [Blogpost](https://www.llamaindex.ai/blog/case-study-how-scaleport-ai-accelerated-development-and-improved-sales-with-llamacloud).
  -  Merlinn, an open-source LLM-powered on-call copilot community project features a Slack assistant that manages production incidents automatically, integrating with tools like Datadog, PagerDuty, GitHub, Notion, and Confluence using core components from LlamaIndex in both Python and TypeScript. [Repository](https://github.com/merlinn-co/merlinn).



##  **🗺️ Guides:**


-  Guide to Building a Multi-Agent Concierge System to demonstrate how to create a complex tree system with specialized sub-agents and meta-agents for efficient customer interaction handling. [Blog](https://www.llamaindex.ai/blog/building-a-multi-agent-concierge-system), [Tweet](https://x.com/llama_index/status/1813618002405069173).
  -  [Guide](https://www.llamaindex.ai/blog/improving-vector-search-reranking-with-postgresml-and-llamaindex) on Improving Vector Search - Reranking with PostgresML and LlamaIndex



##  **✍️ Tutorials:**


-  [Laurie’s](https://x.com/seldo) [video tutorial](https://www.youtube.com/watch?v=lqRTCxsKBwc) on Building and deploying Multi-Agent RAG systems with LlamaIndex.
  -  [Pavan Kumar](https://x.com/pavan_mantha1) [tutorial](https://towardsdev.com/conversational-media-platform-chatting-with-podcasts-and-videos-using-openai-qdrant-and-gemma2-4208ab7e90ee) on Chatting with Podcasts and Videos using OpenAI, Qdrant and Gemma2.
  -  Lakshmi Narayana [tutorial](https://blog.stackademic.com/agentic-rag-enhancing-ai-systems-with-llamaindex-8c54bba41171) on Agentic RAG with LlamaIndex to enhance generative AI applications with intelligent routing, multi-step reasoning, and adaptive learning.



##  **🎤 Talks, Webinars and Podcasts:**


-  Jerry Liu’s [talk](https://www.youtube.com/watch?v=zeAyuLc_f3Q) on advanced LlamaIndex capabilities, introducing ‘Llama Agents’ for deploying microservice-based agents that communicate via a unified API.
  -  Jerry Liu discusses high-quality data, prompt engineering, long context windows, and RAG on the [StackOverflowPodcast](https://stackoverflow.blog/2024/07/16/the-framework-helping-devs-build-llm-apps/) with Jerry Chen.
  -  [Webinar](https://www.youtube.com/watch?v=44h94AJgQoM) with Yixin Hu (VU Amsterdam) and Thomas Hulard (McDermott) on Evaluating RAG with LlamaIndex.
  -  [Webinar](https://www.youtube.com/watch?v=V_-WNJgTvgg) with the cofounders of Deasie (Reece, Leonard, Mikko) on improving RAG with advanced parsing and metadata.



##  **💻 Hackathons:**


-  We’re sponsoring a month-long hackathon with PingCAP for their #TiDB database! Join us, AWS Cloud, Anyscale Compute, Dify AI, Jina AI, Lepton AI, and NPI AI to compete for over $30,000 in prizes, including $12,000 in cash for the first-place winner. [Sign up here](https://tidbhackathon2024.devpost.com/).