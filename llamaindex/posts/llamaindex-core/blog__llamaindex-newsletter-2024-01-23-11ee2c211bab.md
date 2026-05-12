---
title: "LlamaIndex Newsletter 2024–01–23"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-23-11ee2c211bab"
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







Hello LlamaIndex Explorers 🦙,

Another exciting week at LlamaIndex, filled with vibrant community contributions and educational resources. Explore our array of new features, tutorials, guides, and demos, all tailored to enrich your experience with LlamaIndex.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Before delving into the updates, we have two significant announcements:

- We’re thrilled to host our [first in-person hackathon](https://rag-a-thon.devpost.com/), set for February 2nd-4th. This is a fantastic opportunity to meet fellow RAG enthusiasts, collaborate, and compete for prizes totaling over $8000!
- Don’t miss our [webinar](https://lu.ma/lf9iroox) featuring Sehoon Kim and Amir Gholami, scheduled for Thursday at 9 am PT. They will introduce LLMCompiler, an agent compiler for parallel multi-function planning and execution.

We’re always excited to see your projects, articles, or videos. If you’ve created something you’re proud of, share it with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). Also, remember to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) to get all the latest news straight to your inbox.

🤩 **The highlights:**

- **RankGPT:** Introducing RankGPT leveraging GPT-3.5 and GPT-4 for top-tier document ranking and a novel sliding window technique for extensive context management. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/rankGPT.ipynb), [Tweet](https://x.com/llama_index/status/1747681530347216995?s=20).
- **Composable Retrievers:** An interface centralizing advanced retrieval and RAG techniques, enhancing RAG setups with IndexNodes for linking diverse retrievers and pipelines. [Docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers.html), [Tweet](https://x.com/llama_index/status/1748019272679649386?s=20).
- **Advanced QA over Tabular Data Tutorial:** A detailed guide to crafting query pipelines over tabular data, featuring Pandas, SQL, and Query Pipelines for an integrated few-shot, LLM, and custom function setup. [Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql.html), [Text-to-Pandas](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas.html).
- **Long-Context Embedding Models:** Explore models like M2-BERT-80M-32k-retrieval tackling the embedding chunking problem in RAG, with a focus on hybrid retrieval methods and hierarchical retrieval approaches. [Guide](https://docs.llamaindex.ai/en/latest/examples/retrievers/multi_doc_together_hybrid.html).

**✨ Feature Releases and Enhancements:**

- We have introduced RankGPT in our advanced module that utilizes GPT-3.5 and GPT-4 for efficient document ranking, featuring a unique sliding window strategy for handling large contexts. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/rankGPT.ipynb), [Tweet](https://x.com/llama_index/status/1747681530347216995?s=20).
- We have launched Composable Retrievers which centralizes various advanced retrieval and RAG techniques into a versatile interface. It simplifies creating complex RAG setups by allowing you to define IndexNodes to link different retrievers or RAG pipelines. [Docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers.html), [Tweet](https://x.com/llama_index/status/1748019272679649386?s=20).
- Anoop Sharma has introduced LlamaPack for Multi-Stock Ticker Analysis for analyzing various stock tickers with a single code line, enabling easy specification of tickers, time frames, and structured queries. [LlamaPack](https://llamahub.ai/l/llama_packs-stock_market_data_query_engine?from=llama_packs), [Tweet](https://x.com/llama_index/status/1748422554841448600?s=20).
- LlamaIndex.TS (LITS) supports streaming on all endpoints. [Tweet](https://x.com/llama_index/status/1747746779058290800?s=20).
- We announced a new integration with Tonic Validate to allow simple access to LLM-powered evaluations. [Blog post](https://www.tonic.ai/blog/tonic-ai-and-llamaindex-join-forces-to-help-developers-build-more-performant-rag-systems)

🎥 **Demo:**

- **RAG-Maestro for ArXiv Research:** Developed by Aymen Kallala, this web app utilizes RAG to efficiently search scientific concepts in ArXiv papers. It extracts keywords using RAKE, queries ArXiv for relevant papers, and offers on-the-fly indexing with in-line citations — a valuable tool for ML researchers navigating through ArXiv’s extensive library. [Demo](https://rag-maestro-o2wbip4gla-uc.a.run.app/), [GitHub Repo](https://github.com/AymenKallala/RAG_Maestro).

**🗺️ Guides:**

- Guide to Advanced QA over Tabular Data which provides a comprehensive tutorial on creating sophisticated query pipelines over tabular data using Pandas or SQL, constructing a query DAG using our Query Pipelines, integrating few-shot examples, linked prompts, LLMs, custom functions, retrievers, and more. [Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql.html), [Text-to-Pandas](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas.html).
- [Guide](https://medium.com/@marco.bertelli/revolutionizing-chatbot-performance-unleashing-three-potent-strategies-for-rag-enhancement-c1188e395d9d) to a Five-Part Series on Building a Full-Stack RAG Chatbot by [Marco Bertelli](https://medium.com/@marco.bertelli), extensive tutorials covering every aspect of creating an RAG chatbot — from model selection and Flask backend setup to constructing the ChatEngine and optimizing the RAG pipeline.
- [Guide](https://docs.llamaindex.ai/en/latest/examples/retrievers/multi_doc_together_hybrid.html) to Long-Context Embedding Models: The models, like M2-BERT-80M-32k-retrieval, offer a solution to the embedding chunking issue in RAG by grounding retrieval in broader semantic contexts. Learn about hybrid retrieval, combining chunk and document-level similarity, and other approaches like hierarchical retrieval.

**✍️ Tutorials:**

- [Wenqi](https://twitter.com/wenqi_glantz) [tutorial](https://towardsdatascience.com/democratizing-llms-4-bit-quantization-for-optimal-llm-inference-be30cf4e0e34) on Democratizing LLMs: 4-bit Quantization for Optimal LLM Inference with LlamaIndex.
- [Andrej](https://twitter.com/andrejusb) [tutorial](https://www.youtube.com/watch?v=vntNI33wrcI) on FastAPI and LlamaIndex RAG: Creating Efficient APIs.
- [Lulia Brezeanu](https://medium.com/@brezeanu.iulia) [tutorial](https://towardsdatascience.com/advanced-query-transformations-to-improve-rag-11adca9b19d1) on Advanced Query Transformations to Improve RAG.
- [Akash Mathur](https://akash-mathur.medium.com/) in-depth [tutorial](https://akash-mathur.medium.com/advanced-rag-query-augmentation-for-next-level-search-using-llamaindex-d362fed7ecc3) on Advanced RAG: Query Augmentation for Next-Level Search using LlamaIndex.
- [Ryan Nguyen](https://medium.com/@ryanntk) [tutorial](https://levelup.gitconnected.com/live-indexing-for-rag-a-guide-for-real-time-indexing-using-llamaindex-and-aws-51353083ace4) on Live Indexing for RAG: A Guide For Real-Time Indexing Using LlamaIndex and AWS.
- [Nipuna](https://www.youtube.com/watch?v=TOeAe8KB68E) (Paragon AI) tutorial on Building a Full-Stack Complex PDF AI chatbot with LlamaIndex.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex, even more, Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)