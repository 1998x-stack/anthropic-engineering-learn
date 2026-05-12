---
title: "LlamaIndex Newsletter 2023–11–28"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-28-a31be430a786"
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







Hello to Our Llama Community! 🦙

Hope your Thanksgiving was delightful! We’re thrilled to announce a major milestone: LlamaIndex has hit **1 million monthly downloads** on our Python package! A big thank you to everyone for your support, feedback, and contributions that have fueled our journey. Stay tuned for more exciting new products and features coming your way.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



If you have a fascinating project or video you’d like to share, we’d love to see it! Feel free to send it to us at [news@llamaindex.ai](mailto:news@llamaindex.ai). And remember to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) to stay in the loop. We can’t wait to connect with you there!

🤩 **First, the highlights:**

- **Launched Llama Packs:** Prepackaged modules and templates streamlining LLM app development. [Blog](/introducing-llama-packs-e14f453b913a), [Tweet](https://x.com/llama_index/status/1727365908119917016?s=20).
- **RAGs Project:** Build your own retrieval augmented generation app just by talking. [Project](https://github.com/run-llama/rags), [Tweet](https://x.com/llama_index/status/1727502719706132516?s=20).
- **Introduced FuzzyCitationEnginePack:** Precisely aligns LLM responses to source sentences via fuzzy matching, available as an easy-to-implement LlamaPack. [Docs](https://t.co/xiGJCjNCfc), [Tweet](https://x.com/llama_index/status/1729182899470311541?s=20).

Coming up this week: on Thursday 30th our very own Yi Ding will be giving a workshop on Building an Open Source RAG Application Using LlamaIndex. [Sign up for free here](https://www.datastax.com/workshops/building-an-open-source-rag-application-using-llamaindex?utm_medium=social_organic&amp;utm_source=linkedin&amp;utm_campaign=workshop&amp;utm_content=llamaindex-channels)

**✨ Feature Releases and Enhancements:**

- We introduced Llama Packs 🦙📦, a series of prepackaged modules and templates designed to jumpstart your LLM app development. These packs eliminate the need for assembling and tuning custom components for each use case. [Blog](/introducing-llama-packs-e14f453b913a), [Tweet](https://x.com/llama_index/status/1727365908119917016?s=20).
- We have introduced the RAGs project for programming AI agents using natural language, inspired by the interest in OpenAI’s GPTs. Our approach involves a ‘Builder Agent’ that crafts a ‘Custom Agent’ tailored to specific tasks, incorporating tools for system prompt setting, data loading, model configuration, and RAG parameter adjustments. [Project](https://github.com/run-llama/rags), [Tweet](https://x.com/llama_index/status/1727502719706132516?s=20).
- We introduced a LlamaPack that enables the setup of a fully local RAG pipeline with just one line of code. This pack includes Zephyr-7b as the LLM and bge-base as the embedding model. [Docs](https://t.co/IGIyPl5iE2), [Tweet](https://x.com/llama_index/status/1728931304211951944?s=20).
- We introduced `**FuzzyCitationEnginePack**` that maps parts of an LLM-generated response from a RAG pipeline to the exact sentences in the source context using fuzzy matching. This innovation elevates citation accuracy and is now available as a LlamaPack for easy implementation with just one line of code. [Docs](https://t.co/xiGJCjNCfc), [Tweet](https://x.com/llama_index/status/1729182899470311541?s=20).

**👀 Demo:**

- AI-Einblick Prompt is a JupyterLab extension that uses OpenAI’s GPT 3.5 and 4, powered by LlamaIndex, to assist in data science workflows by generating, modifying, and fixing code, creating charts, and building models, seamlessly integrated within the JupyterLab environment. [Project](https://pypi.org/project/ai-einblick-prompt/), [Tweet](https://x.com/llama_index/status/1727492316242583571?s=20).
- [**Ranya Khemiri**](https://twitter.com/khemiri_ranya) uploaded a research paper to RAGs to help with a school assignment and observed results better than file retrieval with ChatGPT. [Blog](https://raniaprojects.wixsite.com/raniakhemiri/post/i-set-up-a-rag-pipeline-to-help-with-a-school-assignment), [Tweet](https://x.com/llama_index/status/1728581037863961019?s=20).

**🤝 Integrations:**

- [CogniSwitch](https://twitter.com/CogniSwitch?lang=en) introduced a fusion RAG approach combining vectors, knowledge graphs, and rules for streamlined ingestion and retrieval. This allows for flexible usage, either as an independent query engine or as an integrated tool within an agent with LlamaIndex. [Docs](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine.html), [Tweet](https://x.com/llama_index/status/1727127794289959396?s=20).

**🗺️ Guides:**

- [Guide](/shipping-your-retrieval-augmented-generation-app-to-production-with-create-llama-7bbe43b6287d) on shipping your RAG application to production with create-llama.
- [Guide](https://t.co/ija26e25PR) on multi-modal models: Our comparison tables detail differences in image reasoning, embeddings, and synthesis capabilities. We also provide insights into multi-modal support for vector stores, focusing on image support with future audio/video integration.
- [Guide](https://gradient.ai/blog/rag-101-for-enterprise) on getting started with AI in your enterprise from Gradient AI. This introductory guide explains retrieval-augmented generation (RAG), its relevance for businesses, and how to balance fine-tuning, prompt engineering, and RAG for optimal results, along with strategies for RAG optimization.

**✍️ Tutorials:**

- [Ankush k Singal](https://medium.com/@andysingal) made a [tutorial](https://t.co/qabwKVuPSJ) on Document Extraction with Zephyr 7b LLM using LlamaIndex.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz) made a [tutorial](https://t.co/93XM9BnaCF) on Automating Hyperparameter Tuning with LlamaIndex.
- [Tonic AI](https://twitter.com/tonicfakedata) [analysis](https://www.tonic.ai/blog/rag-evaluation-series-validating-rag-performance-openai-vs-llamaindex) on OpenAI Assistant API vs LlamaIndex RAG.
- [**Pradip Nichite**](https://twitter.com/pradip_nichite) made ****a ****video [tutorial](https://t.co/v4TsPF9xmt) on using RAGs which provides easy-to-follow instructions on how to build or customize a chatbot capable of advanced summarization over your data, making it accessible even for non-developers.

🎥 **Webinars:**

- Jerry Liu presented a [webinar](https://arize.com/resource/advanced-llm-evals/) with Arize AI on LLM Retrieval Evaluations.