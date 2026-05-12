---
title: "LlamaIndex Update: RAG, Fine-Tuning, Integrations | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-update-20-09-2023-86ed66f78bac"
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







**Hello LlamaIndex Enthusiasts!**

Welcome to the fifth edition of our LlamaIndex Update series.

## **Most Important Takeaways:**

- We’ve open-sourced [**SECInsights.ai**](http://secinsights.ai/) — your gateway to the production RAG framework.
- Replit templates — kickstart your projects with zero environment setup hassles.
- Build RAG from scratch and get hands-on with our processes.

But wait, there’s more!

- Feature Releases and Enhancements
- Fine-Tuning Guides
- Retrieval Tips for RAG
- Building RAG from Scratch Guides
- Tutorials
- Integration with External Platforms
- Events
- Webinars

So, let’s embark on this journey together. Dive in and explore the offerings of the fifth edition of the LlamaIndex Update series!



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# **Feature Releases and Enhancements**

- **Open-Sourced RAG Platform**: LlamaIndex open-sourced [**http://secinsights.ai**](http://secinsights.ai), accelerating RAG app development with chat-based Q&amp;A features. [Tweet](https://twitter.com/llama_index/status/1699116440056651976?s=20)
- **Linear Adapter Fine-Tuning**: LlamaIndex enables efficient fine-tuning of linear adapters on any embedding without re-embedding, enhancing retrieval/RAG across various models. [Tweet](https://twitter.com/llama_index/status/1699566421506671043?s=20), [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/embeddings/finetune_embedding_adapter.html), [BlogPost](https://medium.com/llamaindex-blog/fine-tuning-a-linear-adapter-for-any-embedding-model-8dd0a142d383)
- **Hierarchical Agents**: By structuring LLM agents in a parent-child hierarchy, we enhance complex search and retrieval tasks across diverse data, offering more reliability than a standalone agent. [Tweet](https://twitter.com/llama_index/status/1699929022027718729?s=20)
- **SummaryIndex**: We’ve renamed ListIndex to SummaryIndex to make it clearer what its main functionality is. Backward compatibility is maintained for existing code using ListIndex. [Tweet](https://twitter.com/llama_index/status/1698728395948081247?s=20)
- **Evaluation:** LlamaIndex’s new RAG evaluation toolkit offers async capabilities, diverse assessment criteria, and a centralized BaseEvaluator for easier developer integrations. [Tweet](https://x.com/llama_index/status/1703074307763818775?s=20), [Docs](https://gpt-index.readthedocs.io/en/latest/core_modules/supporting_modules/evaluation/modules.html).
- **Hybrid Search for Postgres/pgvector**: LlamaIndex introduces a hybrid search for Postgres/pgvector. [Tweet](https://twitter.com/llama_index/status/1700892425592696915?s=20), [Docs](https://gpt-index.readthedocs.io/en/stable/examples/vector_stores/postgres.html#hybrid-search).
- **Replit Templates:** LlamaIndex partners with Replit for easy LLM app templates, including ready-to-use Streamlit apps and full Typescript templates. [Tweet](https://x.com/llama_index/status/1702847763183235278?s=20), [Replit Templates](https://replit.com/@LlamaIndex).

## **LlamaIndex.TS:**

- Launches with MongoDBReader and type-safe metadata. [Tweet](https://x.com/llama_index/status/1702382520631959721?s=20).
- Launches with chat history, enhanced keyword index, and Notion DB support. [Tweet](https://twitter.com/llama_index/status/1701292211764338898?s=20).

# Fine-Tuning Guides:

- **OpenAI Fine-Tuning:** LlamaIndex unveils a fresh guide on harnessing OpenAI fine-tuning to embed knowledge from any text corpus. In short: generate QA pairs with GPT-4, format them into a training dataset, and proceed to fine-tuning. [Tweet](https://twitter.com/llama_index/status/1701264116311322937?s=20), [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/knowledge/finetune_knowledge.html).
- **Embedding Fine-Tuning:** LlamaIndex has a more advanced embedding fine-tuning feature, enabling complex NN query transformations on any embedding, including custom ones, and offering the ability to save intermediate checkpoints for enhanced model control. [Tweet](https://twitter.com/llama_index/status/1701983207946965285?s=20), [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/embeddings/finetune_embedding_adapter.html).

# Retrieval Tips For RAG:

- Use references (smaller chunks or summaries) instead of embedding full text.
- Results in 10–20 % improvement.
- Embeddings decoupled from main text chunks.
- Smaller references allow efficient LLM synthesis.
- Deduplication applied for repetitive references.
- Evaluated using synthetic dataset; 20–25% MRR boost.

[Tweet](https://twitter.com/jerryjliu0/status/1698727872721285282?s=20)

# Building RAG from Scratch Guides:

- Build Data Ingestion from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/ingestion.html).
- Build Retrieval from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/retrieval.html).
- Build Vector Store from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/vector_store.html).
- Build Response Synthesis from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/response_synthesis.html).
- Build Router from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/router.html).
- Build Evaluation from scratch. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/low_level/evaluation.html).

# Tutorials:

- [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial](https://betterprogramming.pub/fine-tuning-gpt-3-5-rag-pipeline-with-gpt-4-training-data-49ac0c099919) on Fine-Tuning GPT-3.5 RAG Pipeline with GPT-4 Training Data with LlamaIndex fine-tuning abstractions.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial](https://betterprogramming.pub/fine-tuning-gpt-3-5-rag-pipeline-with-gpt-4-training-data-49ac0c099919) on Fine-Tuning Your Embedding Model to Maximize Relevance Retrieval in RAG Pipeline with LlamaIndex.

Tutorials from the LlamaIndex Team.

- [Sourabh](https://twitter.com/thesourabhd) [tutorial](https://www.youtube.com/watch?v=2O52Tfj79T4) on SEC Insights, End-to-End Guide on [secinsights.ai](https://t.co/VY9we1zhip)
- [Adam’s](https://twitter.com/ajhofmann18) [tutorial](https://www.youtube.com/watch?v=lcuL6Gqw_-g) on Custom Tools for Data Agents.
- [Logan](https://twitter.com/LoganMarkewich) [tutorial](https://www.youtube.com/watch?v=mIyZ_9gqakE) on retrieval/reranking, covering Node Parsing, AutoMergingRetriever, HierarchicalNodeParser, node post-processors, and the setup of a RouterQueryEngine.

# **Integrations with External Platforms**

- **Integration with PortkeyAI**: LlamaIndex integrates with PortkeyAI, boosting LLM providers like OpenAI with features like auto fallbacks and load balancing. [Tweet,](https://x.com/llama_index/status/1699087716183638256?s=20) [Documentation](https://gpt-index.readthedocs.io/en/latest/examples/llm/portkey.html)
- **Collaboration with Anyscale**: LlamaIndex collaborates with anyscalecompute, enabling easy tuning of open-source LLMs using Ray Serve/Train. [Tweet,](https://twitter.com/llama_index/status/1699444987627466986?s=20) [Documentation](https://gpt-index.readthedocs.io/en/latest/examples/llm/anyscale.html)
- **Integration with Elastic**: LlamaIndex integrates with Elastic, enhancing capabilities such as vector search, text search, hybrid search models, enhanced metadata handling, and es_filters. [Tweet,](https://twitter.com/llama_index/status/1700195709041954929?s=20) [Documentation](https://gpt-index.readthedocs.io/en/stable/examples/vector_stores/ElasticsearchIndexDemo.html)
- **Integration with MultiOn**: LlamaIndex integrates with MultiOn, enabling data agents to navigate the web and handle tasks via an LLM-designed browser. [Tweet,](https://twitter.com/llama_index/status/1700221470427754610?s=20) [Documentation](https://llamahub.ai/l/tools-multion)
- **Integration with Vectara**: LlamaIndex collaborates with Vectara to streamline RAG processes from loaders to databases. [Tweet,](https://twitter.com/llama_index/status/1701673229675552876?s=20) [Blog Post](https://medium.com/llamaindex-blog/llamaindex-vectara-7a3889cd34cb)
- **Integration with LiteLLM**: LlamaIndex integrates with LiteLLM, offering access to over 100 LLM APIs and features like chat, streaming, and async operations. [Tweet,](https://x.com/llama_index/status/1703188185323561432?s=20) [Documentation](https://gpt-index.readthedocs.io/en/stable/examples/llm/litellm.html)
- **Integration with MonsterAPI**: LlamaIndex integrates with MonsterAPI, allowing users to query data using LLMs like Llama 2 and Falcon. [Tweet,](https://x.com/monsterapis/status/1702252516061372595?s=20) [Blog Post](https://blog.monsterapi.ai/llama-index-monsterapi-integration-llm-rag/)

# **Events:**

- [Jerry Liu](https://twitter.com/jerryjliu0) spoke on [Production Ready LLM Applications](https://docs.google.com/presentation/d/1uzhz1aFWbyXSrWBzQ1FPQWtVjMgJqAYGoGoVzEnNmAg/edit#slide=id.p) at the Arize AI event.
- [Ravi Theja](https://twitter.com/ravithejads) conducted a [workshop](https://x.com/ravithejads/status/1699644440002826350?s=20) at LlamaIndex + Replit Pune Generative AI meetup.
- [Jerry Liu](https://twitter.com/jerryjliu0) [session](https://www.youtube.com/watch?v=wlKe9U8hmi0) on Building a Lending Criteria Chatbot in Production with Stelios from MQube.

# **Webinars**:

- [Webinar](https://www.youtube.com/watch?v=l-SGgWRe58A) on How to Win an LLM Hackathon by Alex Reibman, Rahul Parundekar, Caroline Frasca, and Yi Ding.
- [Webinar](https://www.youtube.com/watch?v=eGC7m8_SgDk) on LLM Challenges in Production with Mayo Oshin, AI Jason, and Dylan.