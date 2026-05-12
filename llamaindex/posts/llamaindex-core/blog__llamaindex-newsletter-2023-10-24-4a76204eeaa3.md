---
title: "LlamaIndex newsletter 2023–10–24"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-10-24-4a76204eeaa3"
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







Hello Llama Fans 🦙!

Welcome back to our newsletter covering new features, guides, integrations, webinars, tutorials, and more. Got a project, blog, or video you’re proud of? Let’s spotlight it! Contact us at [news@llamaindex.ai](mailto:news@llamaindex.ai).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Plus, for direct updates in your email, just head to [our homepage](https://www.llamaindex.ai/) and subscribe to our newsletter.

🤩 **First, the highlights:**

- `**QueryFusionRetriever**`** Launch:** Inspired by [Adrian Raudaschl’s](https://twitter.com/Raudaschl) RAG-Fusion, enhancing multiple query generation with LLMs. [Tweet](https://twitter.com/jerryjliu0/status/1713573483228356733?s=20), [Docs](https://docs.llamaindex.ai/en/latest/examples/retrievers/simple_fusion.html).
- **Router Fine-Tuning:** Our innovative router fine-tuning approach has achieved an outstanding 99% match rate, outpacing both the gpt-3.5’s 65% and the base model’s 12%. [Tweet](https://twitter.com/jerryjliu0/status/1714668623510618346?s=20), [Docs](https://docs.llamaindex.ai/en/latest/examples/finetuning/router/router_finetune.html).
- **Fusion Retriever Guide:** Guide on building an advanced Fusion Retriever from scratch. [Docs](https://docs.llamaindex.ai/en/latest/examples/low_level/fusion_retriever.html)
- **Amazon Bedrock LLMs and AI21 Labs LLMs:** We have expanded our LLM compatibility, now seamlessly integrating with both Amazon Bedrock and AI21 Labs models.

**✨ Feature Releases and Enhancements:**

- `**QueryFusionRetriever**`: We introduced the `QueryFusionRetriever`, inspired by [Adrian Raudaschl’s](https://twitter.com/Raudaschl) work on RAG-Fusion. This retriever allows users to generate multiple queries with LLMs, run various retrieval methods, and apply reciprocal rank fusion for improved results. [Tweet](https://twitter.com/jerryjliu0/status/1713573483228356733?s=20), [Docs](https://docs.llamaindex.ai/en/latest/examples/retrievers/simple_fusion.html).
- **Router Fine-Tuning:** We introduced router fine-tuning (V0) for improved LLM automated decision-making. Our approach achieved a 99% match rate, outperforming gpt-3.5’s 65% and the base model’s 12%. [Tweet](https://twitter.com/jerryjliu0/status/1714668623510618346?s=20), [Docs](https://docs.llamaindex.ai/en/latest/examples/finetuning/router/router_finetune.html).
- **SQLRetriever:** We introduce SQLRetriever, merging Text-to-SQL and RAG, enabling a RAG pipeline setup over SQL databases for structured table node retrieval and response synthesis. [Tweet](https://twitter.com/llama_index/status/1715518806012092497?s=20), [Docs](https://docs.llamaindex.ai/en/latest/examples/index_structs/struct_indices/SQLIndexDemo.html).

**🗺️ Guides:**

- [Tutorial](https://docs.llamaindex.ai/en/latest/examples/low_level/fusion_retriever.html) guide on **Building an Advanced Fusion Retriever from Scratch.**

**✍️ Tutorials:**

- [Saurav Joshi](https://www.linkedin.com/in/sauravjoshi23/)’s [tutorial](https://medium.com/@sauravjoshi23/complex-query-resolution-through-llamaindex-utilizing-recursive-retrieval-document-agents-and-sub-d4861ecd54e6) on Complex Query Resolution through LlamaIndex Utilizing Recursive Retrieval, Document Agents, and Sub Question Query Decomposition.
- [Greg Loughnane](https://twitter.com/GregOnLock) and [Chris Alexiuk](https://twitter.com/llm_wizard) [tutorial](https://www.youtube.com/watch?v=0QaUqoICNBo) on tackling domain-specific fine tuning using LlamaIndex.
- [Vishwas Gowda](https://twitter.com/VishwasAiTech)’s [blog post](/how-i-built-the-streamlit-llm-hackathon-winning-app-finsight-using-llamaindex-9dcf6c46d7a0) on Streamlit LLM Hackathon winning app — FinSight using LlamaIndex.
- [Emanuel Ferreira](https://twitter.com/manelferreira_)’s blog post on the RA-DIT paper and its implementation in LlamaIndex.
- Yujian Tang’s [blog post](https://zilliz.com/blog/chat-with-towards-data-science-using-llamaindex?utm_source=twitter&amp;utm_medium=social&amp;utm_term=zilliz) on Chat with Towards Data Science using LlamaIndex.
- [Sudarshan Koirala](https://twitter.com/mesudarshan) [tutorial](https://www.youtube.com/watch?v=4kwAhzzaW4A) on Chat with documents with Pinecone and LlamaIndex.
- [Sudarshan Koirala](https://twitter.com/mesudarshan) [tutorial](https://www.youtube.com/watch?v=BngaodT1q_4) on Combined Text-TO-SQL + Semantic Search with LlamaIndex.
- [PromptEngineer](https://twitter.com/engineerrprompt) [tutorial](https://www.youtube.com/watch?v=JeruKKuMxCg) on building LLM-powered financial analyst with LlamaIndex.

**⚙️ Integrations &amp; Collaborations:**

- **Gradient AI:** We introduce a collaboration with Gradient AI to easily integrate fine-tuned LLMs into your LlamaIndex RAG pipeline. [Tweet](https://twitter.com/llama_index/status/1713970425422856477?s=20), [Blogpost](https://gradient.ai/blog/introducing-the-llamindex-integration).
- **PrivateGPT:** [PrivateGPT](https://twitter.com/PrivateGPT_AI) partners with LlamaIndex allowing private document interactions using default or custom integrations. [Tweet](https://twitter.com/PrivateGPT_AI/status/1715331924644815274).
- **VectorFlow &amp; LlamaHub Collaboration:** VectorFlow’s open-source vector-embedding pipeline now leverages LlamaHub for data connectors to streamline code and reduce maintenance. [Tweet](https://twitter.com/llama_index/status/1714446321078137015).
- **Amazon Bedrock &amp; AI21 Labs LLMs:** We’ve broadened our LLM compatibility range by integrating with Amazon Bedrock LLMs and AI21 Labs LLMs.
- **DashVector**: We have introduced an integration with DashVector, a robust, fully-managed vectorDB service.
- **Tencent Cloud:** We’ve integrated with Tencent Cloud VectorDB.
- PGVectorStore within LlamaIndex has been enhanced to support custom Postgres schemas. This facilitates better index management and promotes easy schema-based versioning.
- We now accommodate custom models that align with the OpenAI-compatible API.

**🎥 Webinars:**

- [Wenqi Glantz](https://www.linkedin.com/in/wenqi-glantz-b5448a5a/) workshop webinar on Evaluation-Driven Development (EDD).
- [Webinar](https://www.youtube.com/watch?v=mzb6WNSaLXQ) showcasing the winning projects from the recent AGI House hackathon: “Build, Test, and Launch LLM Apps”. This event was co-sponsored by LlamaIndex, TruEra, and Pinecone.