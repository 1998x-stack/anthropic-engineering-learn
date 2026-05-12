---
title: "LlamaIndex Newsletter 2023–12–19"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-12-19-2965a2d03726"
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







What’s up, Llama Followers 🦙,

We’re excited to bring you another week packed with the latest updates, features, exciting community demos, insightful tutorials, guides, and webinars. This week, don’t miss our special holiday [workshop](https://lu.ma/0eru1il4) on 12/21, where we’ll dive into innovative LLM + RAG use cases with Google Gemini team.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Got a groundbreaking project, compelling article, or captivating video? We’re all ears! Reach out to us at [news@llamaindex.ai](mailto:news@llamaindex.ai). Remember to subscribe to our newsletter via our [website](https://www.llamaindex.ai/) to get all these exciting developments straight to your inbox.

🤩 **First, the highlights:**

- **Google Gemini Partnership:** Now offering day 1 support for Gemini API on LlamaIndex, complete with comprehensive cookbooks for advanced RAG capabilities. [Tweet](https://x.com/llama_index/status/1734965271004340610?s=20).
- **MistralAI Integrations:** Introduced day-0 integrations with MistralAI LLMs and Embedding model for building RAG solutions on LlamaIndex. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/mistralai.ipynb), [Tweet](https://x.com/llama_index/status/1734387934722499022?s=20).
- **Docugami Multi-Doc Llama Dataset:** Launched the Multi-Doc SEC 10Q Dataset by Taqi Jaffri, offering a range of question complexities for advanced RAG research. [Docs](https://llamahub.ai/l/llama_datasets-docugami_kg_rag-sec_10_q), [Tweet](https://twitter.com/llama_index/status/1735370350316405058?s=20).
- **Proposition-Based Retrieval:** Implemented a new retrieval unit based on propositions, enhancing QA performance with LLMs. [Docs](https://llamahub.ai/l/llama_packs-dense_x_retrieval?from=llama_packs), [Tweet](https://x.com/llama_index/status/1735102459000013283?s=20).
- **RAG Pipeline Enhancement Guide:** Introduced a guide featuring modules like Routing, Query-Rewriting, and Agent Reasoning for more complex QA over documents. [Docs](https://docs.llamaindex.ai/en/latest/examples/query_transformations/query_transform_cookbook.html).

**✨ Feature Releases and Enhancements:**

- We launched a partnership with Google Gemini, offering day 1 support for the Gemini API on LlamaIndex, including full-feature support for Gemini (text and multi-modal) and Semantic Retriever API, complemented by three comprehensive cookbooks: [Gemini LLM](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/gemini.ipynb), [Gemini Multi-modal](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/gemini.ipynb), and [Semantic Retriever API](https://github.com/run-llama/llama_index/blob/main/docs/examples/managed/GoogleDemo.ipynb), promising advanced RAG capabilities and multi-modal integrations. [Tweet](https://x.com/llama_index/status/1734965271004340610?s=20).
- We introduced day-0 integrations with the MistralAI LLMs (mistral-tiny, mistral-small, mistral-medium) and the MistralAI Embedding model for building RAG solutions with LlamaIndex both on Python and Typescript versions. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/mistralai.ipynb), [Tweet](https://x.com/llama_index/status/1734387934722499022?s=20).
- We launched the COVID-QA dataset on LlamaHub, a human-annotated, substantial set of 300+ QA pairs about COVID from various web articles, complete with source URLs for easy integration into RAG pipelines, offering ample scope for improvement. [Docs](https://llamahub.ai/l/llama_datasets-covidqa?from=llama_datasets), [Tweet](https://x.com/llama_index/status/1734383167711441000?s=20).
- We launched a new multi-modal template in Create-llama, enabling image input and output generation using the latest GPT-4-vision model from OpenAI, expanding possibilities for diverse use cases. [Docs](https://github.com/run-llama/create_llama_projects/tree/main/nextjs-multi-modal), [Tweet](https://x.com/llama_index/status/1735017333180223585?s=20).
- We have introduced Proposition-Based Retrieval in LlamaIndex: Implementing a new retrieval unit based on propositions, as introduced in the ‘Dense X Retrieval’ paper, enhancing QA performance with LLMs by indexing propositions and linking to the underlying text. [Docs](https://llamahub.ai/l/llama_packs-dense_x_retrieval?from=llama_packs), [Tweet](https://x.com/llama_index/status/1735102459000013283?s=20).
- We partnered with Docugami to launch a new Multi-Doc SEC 10Q Dataset by [Taqi Jaffri](https://twitter.com/tjaffri), aimed at advancing QA datasets for RAG evaluation. This dataset offers a range of question complexities: Single-Doc, Single-Chunk RAG; Single-Doc, Multi-Chunk RAG; and Multi-Doc RAG, addressing the need for more intricate datasets in RAG research. [Docs](https://llamahub.ai/l/llama_datasets-docugami_kg_rag-sec_10_q), [Tweet](https://twitter.com/llama_index/status/1735370350316405058?s=20).
- We launched a SharePoint data loader, enabling direct integration of SharePoint files into LLM/RAG pipelines. [Docs](https://llamahub.ai/l/microsoft_sharepoint?from=all), [Tweet](https://x.com/llama_index/status/1735829020187767092?s=20).

**👀 Community Demos**:

- MemoryCache: Mozilla’s new experimental project that curates your online experience into a private, on-device RAG application using PrivateGPT_AI and LlamaIndex, enhancing personal knowledge management while maintaining privacy. [Website](https://memorycache.ai/), [Repo](https://github.com/Mozilla-Ocho/Memory-Cache).
- OpenBB Finance showcases its enhanced chat widget feature in Terminal Pro, utilizing LlamaIndex’s data chunking combined with Cursor AI for improved large context management and accuracy. [Tweet](https://x.com/josedonato__/status/1734992691090325616?s=20)
- AI Chatbot Starter (from the DataStax team), a web server powered by AstraDB and LlamaIndex, allows easy setup for chatting over web documentation. It can be used as a standalone service or integrated into full-stack applications, with simple credential setup and document ingestion. [Repo](https://github.com/datastax/ai-chatbot-starter), [Tweet](https://x.com/llama_index/status/1735350801609179371?s=20).
- Na2SQL (by [**Harshad**](https://twitter.com/HarshadSurya1c)**)** to ****Build an End-to-End SQL Analyst App on Streamlit featuring interactive database viewing, SQL query displays, and integration with Llama Index. [Blog](/transforming-natural-language-to-sql-and-insights-for-e-commerce-with-llamaindex-gpt3-5-e08edefa21f9), [Repo](https://github.com/AI-ANK/Na2SQL/tree/main).
- LionAGI (by [**Ocean Li**](https://twitter.com/quantoceanli)) is an agent framework for efficient data operations and support for concurrent calls and JSON mode with OpenAI. Check it to integrate it with a Llama Index RAG pipeline for automated AI assistants like an ArXiv research assistant. [Docs](https://lionagi.readthedocs.io/en/latest/index.html), [Repo](https://github.com/lion-agi/lionagi).
- Local RAG for Windows (from Marklysze): A comprehensive resource for integrating advanced LLMs into RAG workflows using Windows Subsystem for Linux, featuring five detailed cookbooks.

**🗺️ Guides:**

- [Guide](https://docs.llamaindex.ai/en/latest/examples/query_transformations/query_transform_cookbook.html) for enhancing RAG pipelines with a Query Understanding Layer, featuring modules like Routing, Query-Rewriting, Sub-Question creation, and Agent Reasoning, all designed to enable more complex and ‘agentic’ QA over documents.
- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/gemini.ipynb) to Building a Restaurant Recommendation QA System with Gemini to extract structured image data and utilize multi-modal Retrieval-Augmented Generation for enhanced query responses.
- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/managed/GoogleDemo.ipynb) to building Advanced RAG with Safety Guardrails to create constrained RAG systems with Gemini API’s semantic search, safety features, and Google Semantic Retriever integrations.
- Guide on [Qdrant’s Multitenancy with LlamaIndex](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/) on setting up payload-based partitioning for user data isolation in vector services.
- [Guide](/llamaindex-rag-evaluation-showdown-with-gpt-4-vs-open-source-prometheus-model-14cdca608277) on using Prometheus — an open-source 13B LLM for RAG Evaluations, comparing it with GPT-4 evaluation with insights on its performance in terms of cost-effectiveness, accuracy, and scoring biases.

**✍️ Tutorials:**

- [Laurie’s](https://twitter.com/seldo) [Advanced Querying &amp; Retrieval Techniques comprehensive code-level tutorial](https://www.youtube.com/watch?v=Y0FL7BcSigI) on 7 advanced querying and retrieval techniques including SubQuestionQuery Engine, Small-to-big retrieval, Metadata filtering, Hybrid search, Recursive Retrieval, Text to SQL, and Multi-document agents.
- [Hubel Labs](https://www.youtube.com/@hubel-labs)’ Advanced RAG [video tutorial](https://www.youtube.com/watch?v=oDzWsynpOyI) with Llamaindex &amp; OpenAI GPT: Sentence Window Retrieval vs Basic Chunking
- [Developers Digest](https://twitter.com/Dev__Digest) [video tutorial](https://www.youtube.com/watch?v=i1qTOKpTUWo) on getting started with llamaindex.ts .
- [Anil’s](https://twitter.com/matchaman11) [tutorial](/how-to-train-a-custom-gpt-on-your-data-with-embedai-llamaindex-8a701d141070) on How to train a custom GPT on your data with EmbedAI + LlamaIndex.

🎥 **Webinars:**

- [Tony Kipkemboi](https://twitter.com/tonykipkemboi) (Streamlit) and [Yi Ding](https://twitter.com/yi_ding) (LlamaIndex) [webinar](https://www.youtube.com/watch?v=PLKkudXYCNI) on Demystifying RAG apps with LlamaIndex!

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex even more Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)