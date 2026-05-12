---
title: "LlamaIndex Newsletter 2024-03-05"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-03-05"
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







 Greetings, LlamaIndex devotees! 🦙



 It was another fun week to be at the center of the LLM universe, and we have tons to share!



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



 🤩 **The highlights:**


-  We shared our thoughts on the future of **long-context RAG.** As LLMs with context windows over 1M tokens begin to appear, what changes about RAG, and how will LlamaIndex evolve? [Tweet](https://twitter.com/llama_index/status/1763620476847632744), [Blog post](https://www.llamaindex.ai/blog/towards-long-context-rag)
  -  **llama-index-networks** lets you build a super-RAG application by combining answers from independent RAG apps over the network. [Tweet](https://twitter.com/llama_index/status/1762552542981230769), [Blog post](https://www.llamaindex.ai/blog/querying-a-network-of-knowledge-with-llama-index-networks-d784b4c3006f), [repo](https://github.com/run-llama/llama_index/tree/main/llama-index-networks)
  -  People loved our release of LlamaParse, a world-beating PDF parsing service, so we made it even better! [Tweet](https://twitter.com/llama_index/status/1763008808216060186), [blog post](https://www.llamaindex.ai/blog/introducing-llamacloud-and-llamaparse-af8cedf9006b)



 **✨ Feature Releases and Enhancements:**


-  We released a new llama-index-networks feature that lets you combine multiple independent RAG applications over the network, allowing you to run a single query across all the applications and get a single, combined answer. [Tweet](https://twitter.com/llama_index/status/1762552542981230769), [Blog post](https://www.llamaindex.ai/blog/querying-a-network-of-knowledge-with-llama-index-networks-d784b4c3006f), [repo](https://github.com/run-llama/llama_index/tree/main/llama-index-networks)
  -  Inference engine [Groq](https://groq.com/) wowed us and the world with their incredibly fast query times and we were delighted to introduce first-class support for their LLM APIs. [Tweet](https://twitter.com/llama_index/status/1762869201222639927), [notebook](https://docs.llamaindex.ai/en/stable/examples/llm/groq.html)
  -  Users love LlamaParse, the world-beating PDF parsing service we released last week. We pushed improved parsing and OCR support for 81+ languages! We also increased the usage cap from 1k to 10k pages per day. [Tweet](https://twitter.com/llama_index/status/1763008808216060186), [blog post](https://www.llamaindex.ai/blog/introducing-llamacloud-and-llamaparse-af8cedf9006b)
  -  We migrated our [blog off of Medium](https://www.llamaindex.ai/blog), we hope you like the new look and the absence of nag screens!
  -  RAPTOR is a new tree-structured technique for advanced RAG; we turned the paper into a LlamaPack, allowing you to use the new technique in one line of code. [Tweet](https://twitter.com/llama_index/status/1763972097628684607), [package](https://llamahub.ai/l/llama-packs/llama-index-packs-raptor?from=), [notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-raptor/examples/raptor.ipynb), [original paper](https://arxiv.org/pdf/2401.18059.pdf)



 **🎥 Demos:**


-  The Koda Retriever is a new retrieval concept: hybrid search where the alpha parameter controlling the importance of vector search vs. keyword search is tuned on a per-query basis by the LLM itself, based on a few-shot examples. [Tweet](https://twitter.com/llama_index/status/1763252392639042024), [notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-koda-retriever/examples/alpha_tuning.ipynb), [package](https://llamahub.ai/l/llama-packs/llama-index-packs-koda-retriever?from=), [blog post](https://www.llamaindex.ai/blog/llamaindex-enhancing-retrieval-performance-with-alpha-tuning-in-hybrid-search-in-rag-135d0c9b8a00)
  -  [Mixedbread.ai](http://Mixedbread.ai) released some state-of-the-art rerankers that perform better than anything seen before; we whipped up a quick cookbook to show you how to use them directly in LlamaIndex. [Tweet](https://twitter.com/llama_index/status/1763654691886674134), [Notebook](https://docs.llamaindex.ai/en/latest/cookbooks/mixedbread_reranker.html), [blog post](https://www.mixedbread.ai/blog/mxbai-rerank-v1)



 **🗺️ Guides:**


-  **Function-calling cookbook with open source models** shows you how to use Fireworks AI’s OpenAI-compatible API to use all native LlamaIndex support for function calling. [Notebook](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks_cookbook.html), [Tweet](https://twitter.com/llama_index/status/1762532341795487815).
  -  We released a best practices cookbook showing how to use LlamaParse, our amazing PDF parser. [Tweet](https://twitter.com/llama_index/status/1763729200106840548), [notebook](https://github.com/run-llama/llama_parse/blob/main/examples/demo_table_comparisons.ipynb)
  -  A **comprehensive guide to semantic chunking for RAG** by Florian June covers embedding-based chunking, BERT-based chunking techniques, and LLM-based chunking for everything you need to know about this highly effective technique to improve retrieval quality. [Tweet](https://twitter.com/llama_index/status/1764335221141631471), [Blog post](https://pub.towardsai.net/advanced-rag-05-exploring-semantic-chunking-97c12af20a4d)



 **✍️ Tutorials:**


-  Our own [Andrei](https://twitter.com/_nerdai_) presented a notebook on building Basic RAG with LlamaIndex at [Vector Institute](https://vectorinstitute.ai/)’s RAG bootcamp. [Tweet](https://twitter.com/_nerdai_/status/1762924582183350782), [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/presentations/materials/2024-02-28-rag-bootcamp-vector-institute.ipynb)
  -  ClickHouse presented an in-depth tutorial using LlamaIndex to query both structured and unstructured data, and built a bot that queries Hacker News to find what people are saying about the most popular technologies. [Tweet](https://twitter.com/llama_index/status/1763282902358585445), [blog post](https://clickhouse.com/blog/building-hackernews-stackoverflow-chatbot-with-llamaindex-and-clickhouse)
  -  POLM (Python, OpenAI, LlamaIndex, MongoDB) is a new reference architecture for building RAG applications and MongoDB has a beautiful, step-by-step tutorial for building it out. [Tweet](https://twitter.com/llama_index/status/1764078471276642469), [blog post](https://www.mongodb.com/developer/products/atlas/rag-with-polm-stack-llamaindex-openai-mongodb/)



 🎥 **Webinar:**


-  Our CEO Jerry Liu will do a joint webinar with Adam Kamor of [Tonic.ai](http://Tonic.ai) about building fully-local RAG applications with Ollama and Tonic. People love local models! [Tweet](https://twitter.com/llama_index/status/1763304038442192978), [Registration page](https://www.tonic.ai/webinars/preserve-privacy-using-local-rag-with-tonic-ai-llamaindex)
  -  Jerry also did a webinar with [Traceloop](https://www.traceloop.com/) on leveling up your LLM application with observability. [Tweet](https://twitter.com/llama_index/status/1763364010676900080), [YouTube](https://www.youtube.com/watch?v=if-2elFrfgM)
  -  Our hackathon at the beginning of February was a huge success! Check out this webinar in which we invited the winners to come and talk about their projects. [Tweet](https://twitter.com/llama_index/status/1764020728427667605), [YouTube](https://www.youtube.com/watch?v=THkeXnwwSw4).