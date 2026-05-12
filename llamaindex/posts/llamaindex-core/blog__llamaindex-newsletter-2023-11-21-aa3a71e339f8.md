---
title: "LlamaIndex Newsletter 2023–11–21"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-21-aa3a71e339f8"
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







Hello Llama Fam 🦙

What an amazing week we’ve had! We’re excited to share that, according to the [Retool State of AI 2023 survey](https://retool.com/reports/state-of-ai-2023), 1 in 12 respondents are now using LlamaIndex. We’re grateful for all your support.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



If you have a fascinating project or video you’d like to share, we’d love to see it! Feel free to send it to us at [news@llamaindex.ai](mailto:news@llamaindex.ai). And remember to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) to stay in the loop. We can’t wait to connect with you there!

🤩 **First, the highlights:**

- **LlamaIndex 0.9 Release:** we introduced LlamaIndex version 0.9 featuring streamlined data handling with a new IngestionPipeline, automated caching, improved text processing interfaces, tokenizer updates, PyPi packaging enhancements, consistent import paths, and a beta version of MultiModal RAG Modules. [Blog post](/announcing-llamaindex-0-9-719f03282945), [Tweet](https://twitter.com/llama_index/status/1724836383259582548?s=20).
- **Multi-Modal Evaluation Tools:** we launched multi-modal evaluation with the introduction of MultiModalRelevancyEvaluator and MultiModalFaithfulnessEvaluator, plus a guide for their application in multi-modal settings. [Blog post](https://t.co/gw4txOw0gY), [Tweet](https://x.com/llama_index/status/1725249971551879601?s=20).
- `**create-llama**`** CLI Tool:** we unveiled `**create-llama**`, a versatile CLI tool for building full-stack LLM apps with options like FastAPI, ExpressJS, and Next.js for backends and a Next.js frontend with Vercel AI SDK components. [Blog post](https://t.co/JpH5Trq4Yb), [Tweet](https://x.com/jerryjliu0/status/1724481554528014660?s=20).
- **Cohere Reranker Fine-Tuning:** we enhanced RAG pipeline retrieval performance with the fine-tuning of the Cohere reranker. [Blog post](/improving-retrieval-performance-by-fine-tuning-cohere-reranker-with-llamaindex-16c0c1f9b33b), [Tweet](https://x.com/llama_index/status/1725189652003610888?s=20).

Coming up this week: we have a YouTube live event in partnership with [AI Makerspace](https://www.youtube.com/channel/UCbDZFHUjTCCUKyXgcp3g50Q) exploring the potential of LlamaIndex to handle complex PDFs with tables, charts and more. [Register for free!](https://lu.ma/RAG4PDF)

**✨ Feature Releases and Enhancements:**

- We introduced the LlamaIndex 0.9 version with updates on streamlined data handling with new IngestionPipeline, automated caching, improved interfaces for text processing, tokenizer updates, enhanced PyPi packaging, consistent import paths, and a beta of MultiModal RAG Modules for text and image integration. [Blog post](/announcing-llamaindex-0-9-719f03282945), [Tweet](https://twitter.com/llama_index/status/1724836383259582548?s=20).
- We introduced multi-modal evaluation which includes MultiModalRelevancyEvaluator and MultiModalFaithfulnessEvaluator, and a guide on using them in multi-modal applications. [Blog post](https://t.co/gw4txOw0gY), [Tweet](https://x.com/llama_index/status/1725249971551879601?s=20).
- We introduced `**create-llama**`, a CLI tool for easily building full-stack LLM apps, offering choices like FastAPI, ExpressJS, and Next.js backends with Llama Index, and a Next.js frontend with Vercel AI SDK components, enabling extensive customization for AI engineers. [Blog post](https://t.co/JpH5Trq4Yb), [Tweet](https://x.com/jerryjliu0/status/1724481554528014660?s=20).
- We introduced fine-tuning of the cohere reranker to improve retrieval performance in the RAG pipeline. [Blog post](/improving-retrieval-performance-by-fine-tuning-cohere-reranker-with-llamaindex-16c0c1f9b33b), [Tweet](https://x.com/llama_index/status/1725189652003610888?s=20).

Integrations:

- We integrated with Chroma’s multi-modal collections which allows for indexing both text and images in a single collection, enhancing RAG pipelines by combining text and image information for use with multi-modal models like GPT-4V, LLaVa, and Fuyu. [Docs](https://docs.llamaindex.ai/en/latest/examples/multi_modal/ChromaMultiModalDemo.html), [Tweet](https://x.com/llama_index/status/1724228502168518857?s=20).

**🗺️ Guides:**

- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/multi_modal_retrieval.ipynb) on Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles.
- [Guide](https://nanonets.com/blog/llamaindex/#using-index-to-chat-with-data) on LlamaIndex by Nanonets covering over 12 key areas such as data management, indexing/storage, querying with top-k RAG, structured outputs, chat functionalities with memory, and agent development incorporating tool use.
- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/transforms/TransformsEval.ipynb) on using Ingestion pipeline focusing on showcasing experiments on chunk overlaps and the use of metadata extractors, including title, summary, and other elements.
- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/perplexity.ipynb) on using Perplexity API with LlamaIndex by [Vishhvak](https://twitter.com/vishhvak).
- [Guide](https://docs.llamaindex.ai/en/stable/community/integrations/fleet_libraries_context.html) on using [Fleet Context](https://twitter.com/fleet_ai) to download the embeddings for LlamaIndex’s documentation and build a hybrid dense/sparse vector retrieval engine on top of it.
- [Guide](https://github.com/jerryjliu/create_llama_projects) on building a full-stack financial analysis bot using `**create-llama**` and Llama Index's RAG, capable of querying text and tables across SEC filings.

**✍️ Tutorials:**

- [Wenqi Glantz](https://medium.com/@wenqiglantz) made a [tutorial](https://levelup.gitconnected.com/llava-vs-gpt-4v-amidst-snow-geese-migration-c2561b16113d) on LLaVA vs. GPT-4V Amidst Snow Geese Migration.
- [Glenn Parham’s](https://twitter.com/glenn__parham) [cookbook](https://github.com/deptofdefense/LLMs-at-DoD/blob/main/tutorials/Chatting%20with%20your%20Docs.ipynb) on LlamaIndex, hosted in the Department of Defense’s official repository, showcases methods for applying RAG on unclassified DoD policy documents.
- [Sudarshan Koirala](https://www.youtube.com/watch?v=PHEZ6AHR57w) made a tutorial on Using Perplexity API with LlamaIndex.
- [Ravi Theja](https://twitter.com/ravithejads) [analysis](/gpt4-v-experiments-with-general-specific-questions-and-chain-of-thought-prompting-cot-techniques-49d82e6ddcc9) on GPT4-V Experiments with General, Specific questions and Chain Of Thought prompting(COT) techniques

🎥 **Webinars:**

- Check out our CEO — [Jerry Liu’s](https://twitter.com/jerryjliu0) talk on Building Production-Ready RAG Applications at [AI.engineer](https://t.co/46VrFt8GCV) Summit.