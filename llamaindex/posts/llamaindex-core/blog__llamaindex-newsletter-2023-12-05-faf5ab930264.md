---
title: "LlamaIndex Newsletter 2023–12–05"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-12-05-faf5ab930264"
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







Hello Llama Community 🦙,

We are excited to collaborate with DeepLearningAI and TruEraAI to launch an extensive course on advanced Retrieval-Augmented Generation (RAG) and its evaluations. The course includes Sentence Window Retrieval, Auto-merging Retrieval, and Evaluations with TruLensML, providing practical tools for enhanced learning and application. To make the most of this learning opportunity, we invite you to [take the course](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/?utm_campaign=truerallamaindex-launch&amp;utm_medium=video&amp;utm_source=youtube&amp;utm_content=teaser).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We appreciate your support and are always excited to see your projects and videos. Feel free to share them at [news@llamaindex.ai](mailto:news@llamaindex.ai). Also, remember to subscribe to our newsletter on our [website](https://www.llamaindex.ai/) for the latest updates and to connect with our vibrant community.

🤩 **First, the highlights:**

- **Launch of Seven Advanced Retrieval LlamaPacks**: Simplifies building advanced RAG systems to nearly a single line of code, offering techniques like Hybrid Fusion and Auto-merging Retriever. [Tweet](https://x.com/llama_index/status/1729303619760259463?s=20).
- **Introduction of the OpenAI Cookbook**: A comprehensive guide for evaluating RAG systems with LlamaIndex, covering system understanding, building, and performance evaluation. [Blog](/openai-cookbook-evaluating-rag-systems-fe393c61fb93), [Notebook](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/Evaluate_RAG_with_LlamaIndex.ipynb)
- **Speed Enhancement in Structured Metadata Extraction**: Achieved 2x to 10x faster processing in extracting structured metadata from text, boosting RAG performance. [Docs](https://t.co/sBVWeO8jKo), [Tweet](https://x.com/llama_index/status/1730400634757939691?s=20).
- We launched versions 3 of [RAGs](https://github.com/run-llama/rags), our project that lets you use natural language to generate a RAG bot customized to your needs. This version incorporates web search, so your bot can incorporate answers fresh from the web. [Tweet](https://x.com/llama_index/status/1730320635279331524?s=20).
- **Core **[**guide**](https://docs.llamaindex.ai/en/latest/community/full_stack_projects.html#) **for Full-Stack LLM App Development**: Simplifies complex app development with tools like ‘create-llama’ for full-stack apps, ‘SEC Insights’ for multi-document processing, and ‘LlamaIndex Chat’ for chatbot customization.

**✨ Feature Releases and Enhancements:**

- We’ve launched seven advanced retrieval LlamaPacks, serving as templates to easily build advanced RAG systems. These packs simplify the process to almost a single line of code, moving away from the traditional notebook approach. The techniques include Hybrid Fusion, Query Rewriting + Fusion, Retrieval with Embedded Tables, Auto-merging Retriever, Sentence Window Retriever, Node Reference Retriever, and Multi-Document Agents for handling complex queries. [Tweet](https://x.com/llama_index/status/1729303619760259463?s=20).
- We introduce new abstractions for structured output extraction in multi-modal settings, enabling the transformation of images into structured Pydantic objects. This enhancement is particularly useful for applications like product reviews, restaurant listings, and OCR. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/multi_modal_pydantic.ipynb), [Tweet](https://x.com/llama_index/status/1729535952912290050?s=20).
- We introduce the [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/Evaluate_RAG_with_LlamaIndex.ipynb), a guide focused on evaluating RAG systems using LlamaIndex. It encompasses understanding RAG systems, building them with LlamaIndex, and evaluating their performance in retrieval and response generation. [Blog](/openai-cookbook-evaluating-rag-systems-fe393c61fb93), [Notebook](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/Evaluate_RAG_with_LlamaIndex.ipynb), [Tweet](https://x.com/llama_index/status/1729587400240967761?s=20).
- We launched RAGs v3 — a bot that transcends traditional limits by incorporating web search capabilities. This bot, designed to operate in natural language rather than code, offers an enhanced experience compared to the combination of ChatGPT and Bing. Leveraging our integration with Metaphor Systems — a search engine tailored for Large Language Models (LLMs) — the bot can retrieve relevant text from the internet to provide answers beyond its internal corpus. Additionally, users can now view the tools the agent uses, with the web search feature exclusively accessible to our OpenAI agent. [Repo](https://t.co/838BDVOEbA), [Tweet](https://x.com/llama_index/status/1730320635279331524?s=20).
- We have significantly improved the speed of extracting structured metadata (like titles and summaries) from text to enhance RAG performance. Our new implementation offers 2x to 10x faster processing, overcoming the limitations of previous slower methods. [Docs](https://t.co/sBVWeO8jKo), [Tweet](https://x.com/llama_index/status/1730400634757939691?s=20).
- We have made it incredibly easy to set up a RAG + Streamlit app, now possible with just a single line of code using our `**StreamlitChatPack**`. This pack provides a ready-to-use RAG pipeline and a Streamlit chat interface, customizable in terms of data sources and retrieval algorithms. [Docs](https://llamahub.ai/l/llama_packs-streamlit_chatbot), [Tweet](https://x.com/llama_index/status/1731121252142878982?s=20).

**👀 Demo:**

AInimal Go — an innovative multi-modal app inspired by Pokemon-Go. This interactive application, developed by [Harshad Suryawanshi](https://harshadsuryawanshi.medium.com/), lets users capture or upload images of animals, classify them using the ResNet-18 model, and engage in conversations with the animals, augmented by a knowledge base of over 200 Wikipedia articles. Notably, the app employs a targeted ResNet model for classification, offering enhanced speed and cost efficiency, instead of using GPT-4V.

[Blog](/multimodal-rag-building-ainimal-go-fecf8404ed97), [Repo](https://github.com/AI-ANK/AInimalGo-Chat-with-Animals), [HuggingFace Space](https://huggingface.co/spaces/AI-ANK/AInimal_Go), [Tweet](https://x.com/llama_index/status/1729246724911477165?s=20).

**🗺️ Guides:**

- We introduce a core [guide](https://docs.llamaindex.ai/en/latest/community/full_stack_projects.html#) within the LlamaIndex ecosystem, designed to simplify “full-stack” app development, which is notably more complex than notebook development. This includes ‘create-llama’ for building full-stack apps with advanced templates, ‘SEC Insights’ for multi-document handling of over 10,000 filings, and ‘LlamaIndex Chat’ for a customizable chatbot experience. All tools are open-source with full guides and tutorials available.
- [Guide](https://t.co/2Ygxs6bPoX) on using the Table Transformer model with GPT-4V for advanced RAG applications in parsing tables from PDFs: Our method involves CLIP for page retrieval, Table Transforms for table image extraction, and GPT-4V for answer synthesis. This approach is compared with three other multi-modal table understanding techniques, including using CLIP for whole page retrieval, text extraction and indexing with GPT-4V, and OCR on table images for context.
- [Guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/multi_modal_pydantic.ipynb) on analyzing various multi-modal models for their ability to extract structured data from complex product images on an Amazon page. The models compared include GPT-4V, Fuyu-8B, MiniGPT4, CogVLM-4, and LLaVa-13B. Key findings reveal that all models incorrectly identified the number of reviews (correct answer: 5685), only GPT-4V and Fuyu accurately determined the price, each model’s product description varied from the original, and Mini-GPT4 incorrectly assessed the product rating.

**✍️ Tutorials:**

- [Jo Kristian Bergum](https://www.linkedin.com/in/jo-bergum/) [blog post](https://blog.vespa.ai/scaling-personal-ai-assistants-with-streaming-mode/) on Hands-On RAG guide for personal data with Vespa and LLamaIndex.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz) made a [tutorial](https://levelup.gitconnected.com/llama-packs-the-low-code-solution-to-building-your-llm-apps-269eec05557b) on Llama Packs: The Low-Code Solution to Building Your LLM Apps.
- [Liza Shulyayeva](https://twitter.com/Lazer)’s in-depth [tutorial](https://www.daily.co/blog/search-your-video-content-library-with-llamaindex-and-chroma/) on building and deploying a retrieval-augmented generation (RAG) app to conversationally query the contents of your video library

🎥 **Webinars:**

- [Webinar](https://www.youtube.com/watch?v=0zGHrcE-Zy4) on PrivateGPT — Production RAG with Local Models.

🏆 **Hackathons:**

- Your reminder that there’s still time to join [the TruEra Challenge](https://lablab.ai/event/truera-challenge-build-llm-applications?utm_medium=post&amp;utm_source=twitter&amp;utm_campaign=truera_challenge_hackathon&amp;utm_term=hackathon_page&amp;utm_content=event_promo), an online hackathon from Dec 1st to 8th, and explore AI observability with technology from TruEra AI and Google Vertex AI. Use the LlamaIndex framework to enhance your LLM-based app. Participants receive $30 in Google Cloud credits, plus an additional $100 upon solution submission. Winners share a $9,000 cash prize pool and $14,000 in Google Cloud credits.
- We partnered with Zilliz Universe to participate in their [Advent of Code](https://t.co/hGzBA1acf6) event. This December, explore 25 open-source projects, with daily challenges to build something in 30 minutes or less. It’s a great opportunity to learn new skills and have winter fun. For tips, tutorials, and resources, visit the Advent of Code channel in Discord each day.