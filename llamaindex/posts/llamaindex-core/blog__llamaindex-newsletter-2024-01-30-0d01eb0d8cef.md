---
title: "LlamaIndex Newsletter 2024–01–30"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-30-0d01eb0d8cef"
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







Hello LlamaIndex Adventurers 🦙,

Welcome to another thrilling week at LlamaIndex! It’s brimming with community contributions and a wealth of educational content that will take your LlamaIndex experience to new heights. Dive into our latest features, comprehensive tutorials, insightful guides, and interactive demos, all designed to supercharge your journey with LlamaIndex.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



But first, let’s ignite your excitement with a reminder about our upcoming [first-ever in-person hackathon](https://rag-a-thon.devpost.com/), happening February 2nd-4th. Don’t miss this incredible chance to mingle with fellow RAG aficionados, collaborate on exciting projects, and vie for a share of over $16,000 in prizes!

Your creations inspire us! Whether it’s a project, article, or video that you’re proud of, we’d love to see it. Share your brilliance with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). And for those who haven’t yet, make sure to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) — it’s your gateway to all the latest and greatest from LlamaIndex, delivered directly to your inbox.

🤩 **The highlights:**

- **RAG CLI**: Easy-to-use tool for local file indexing and search, with advanced integration and customization features. [Docs](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html), [Tweet](https://x.com/llama_index/status/1750950516925079777?s=20).
- **JSONalyze**: Efficiently summarizes large JSON datasets, transforming them into SQLite for detailed SQL queries. [Docs](https://docs.llamaindex.ai/en/latest/examples/query_engine/JSONalyze_query_engine.html), [Tweet](https://x.com/llama_index/status/1749541492191039873?s=20).
- **OpenAI Embeddings**: We now support the latest OpenAI `**text-embedding-3-small**`** and **`**text-embedding-3-large**` embeddings for improved accuracy and cost-effectiveness in data retrieval. [Docs](https://docs.llamaindex.ai/en/latest/examples/embeddings/OpenAI.html), [Tweet](https://x.com/llama_index/status/1750640685894783068?s=20).
- **ReAct Agent **[**Guide**](https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/agent_runner/query_pipeline_agent.ipynb): From scratch guide for building ReAct agents, covering all key aspects from setup to memory management.
- **Slack Bot**: Step-by-step [guide](/building-a-slack-bot-that-learns-with-llamaindex-qdrant-and-render-c88d4aa72840) for developing a learning Slack bot, integrated with advanced data engines and deployment tools.

**✨ Feature Releases and Enhancements:**

- We have launched RAG CLI: A straightforward command-line tool for indexing and searching any local file, featuring integration with IngestionPipeline, QueryPipeline, and ChromaDB, with support for local models and customizable logic. [Docs](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html), [Tweet](https://x.com/llama_index/status/1750950516925079777?s=20).
- We have introduced JSONalyze, a query engine that swiftly summarizes large JSON datasets. It transforms JSON data into an SQLite table, enabling precise SQL queries for efficient data analysis, combining LlamaIndex’s capabilities with text-to-SQL technology. [Docs](https://docs.llamaindex.ai/en/latest/examples/query_engine/JSONalyze_query_engine.html), [Tweet](https://x.com/llama_index/status/1749541492191039873?s=20).
- We have launched day 0 support for OpenAI’s latest embedding models featuring cost-effective `**text-embedding-3-small**` and high-performance `**text-embedding-3-large**`, both with customizable dimensions for enhanced retrieval accuracy in Python and TypeScript versions of LlamaIndex. [Docs](https://docs.llamaindex.ai/en/latest/examples/embeddings/OpenAI.html), [Tweet](https://x.com/llama_index/status/1750640685894783068?s=20).
- We have launched Infer-Retrieve-Rerank as a LlamaPack, a technique developed by Karel Doostrlnck, as a simple yet effective LLM-based approach for tackling complex classification challenges with numerous categories, applicable in areas like medical diagnosis and job skill assessment. [LlamaPack](https://llamahub.ai/l/llama_packs-research-infer_retrieve_rerank?from=all), [Tweet](https://x.com/llama_index/status/1752008109835559123?s=20).
- We have launched LlamaPack with Vanna AI: An advanced text-to-SQL tool using RAG for storing, indexing, and generating SQL queries. [LlamaPack](https://llamahub.ai/l/llama_packs-vanna?from=all).
- We have integrated with Zilliz Cloud Pipeline in partnership with Zilliz Universe. This fully managed, scalable retrieval service supports multi-tenancy. [Blog](/building-scalable-rag-applications-with-llamaindex-and-zilliz-cloud-pipelines-4879e9768baf), [Tweet](https://x.com/llama_index/status/1750621271250096558?s=20).
- We have partnered with Exa which created an advanced RAG-powered web search, designed for LLMs and now integrated with Llama Index agents, enhancing workflow automation and data source combination. [Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/tools/notebooks/exa.ipynb), [Tweet](https://x.com/llama_index/status/1751011851952152710?s=20).
- We have integrated with Neutrino, offering GPT-4 level performance at significantly reduced costs by smartly allocating queries to the most suitable model from a diverse range. [Docs](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino.html), [Twitter](https://x.com/llama_index/status/1749504764172493161?s=20).

**🗺️ Guides:**

- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/agent_runner/query_pipeline_agent.ipynb) to Building a ReAct Agent from Scratch and cookbook detailing the essential components for creating your agents, including reasoning prompts, output parsing, tool selection, and memory management.
- [Guide](/building-a-slack-bot-that-learns-with-llamaindex-qdrant-and-render-c88d4aa72840) to Building Slack Bot: Create and deploy an intelligent Slack bot that learns from conversations and accurately answers organizational queries, featuring integration with Qdrant Engine and Render.

**✍️ Tutorials:**

- [Marco Bertelli](https://medium.com/@marco.bertelli) [tutorial](https://medium.com/@marco.bertelli/empowering-your-chatbot-unveiling-dynamic-knowledge-sources-with-advanced-integration-e8353e85099c) on Empowering Your Chatbot: Unveiling Dynamic Knowledge Sources with Advanced Integration.
- [Tonic Validate](/tonic-validate-x-llamaindex-implementing-integration-tests-for-llamaindex-43db50b76ed9) tutorial on Implementing integration tests for LlamaIndex.
- [Chia Jeng Yang](https://chiajy.medium.com/) [tutorial](https://medium.com/enterprise-rag/injecting-knowledge-graphs-in-different-rag-stages-a3cd1221f57b) on Injecting Knowledge Graphs in different RAG stages.
- [Wenqi Glantz](https://medium.com/@wenqiglantz) [tutorial](https://towardsdatascience.com/jump-start-your-rag-pipelines-with-advanced-retrieval-llamapacks-and-benchmark-with-lighthouz-ai-80a09b7c7d9d) on Jump-start Your RAG Pipelines with Advanced Retrieval LlamaPacks and Benchmark with Lighthouz AI.

🎥 **Webinar**

- LlamaIndex [Webinar](https://www.youtube.com/watch?v=aoLtTIYAafY) on Efficient Parallel Function Calling Agents with LLMCompiler with Sehoon Kim and Amir Gholami.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex, even more, Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)