---
title: "LlamaIndex Newsletter 2023-11–07"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-07-cf20b9a833aa"
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







Hi again Llama Fans! 🦙

We hope you enjoyed our [OpenAI Dev Day special edition](/llamaindex-news-special-edition-openai-developer-day-e955f16db4e2) yesterday! Here’s our wrap-up of everything else that happened last week. As always, if you’ve got a project, article, or video that’s turning heads? We’re all ears! Drop us a line at [news@llamaindex.ai](mailto:news@llamaindex.ai).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



And for all this goodness delivered directly to you, don’t forget to subscribe to our newsletter via our [website](https://www.llamaindex.ai/).

🤩 **First, the highlights:**

- **LlamaIndex Chat:** We unveiled a customizable LLM chatbot template with system prompts and avatars, all within an open-source MIT-licensed framework using LlamaIndex for TypeScript. Explore the [Demo](https://chat.llamaindex.ai/) or check the [Tweet](https://x.com/llama_index/status/1719021921462067654?s=20).
- **Evaluator Fine-Tuning:** We launched a method to enhance LLM output assessment by distilling GPT-4 into GPT-3.5, optimizing both cost and speed. See our [Tweet](https://x.com/llama_index/status/1719868813318271242?s=20).
- **ParamTuner:** We introduced a new hyperparameter tuning abstraction to refine RAG pipeline performance, featuring objective functions, grid search, and Ray Tune integration. Check out the [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/param_optimizer/param_optimizer.ipynb) and [Tweet](https://twitter.com/llama_index/status/1721209688703062234?s=20).
- **CohereAI Embed v3 &amp; Voyage AI Integration:** We strengthened the LlamaIndex RAG pipeline with two powerful embedding model additions: the latest Embed v3 from CohereAI and the high-performing embedding model from Voyage AI. [Tweet](https://twitter.com/llama_index/status/1720216603584069875?s=20) and [tweet](https://x.com/llama_index/status/1720578050180686129?s=20).

**✨ Feature Releases and Enhancements:**

- We introduced LlamaIndex Chat, a new feature allowing users to create and share custom LLM chatbots tailored to their data, complete with personalized system prompts and avatars. Additionally, we’re proud to share that it’s a fully open-source template under the MIT license, crafted using LlamaIndexTS for a seamless start to LLM application development. [Demo](https://chat.llamaindex.ai/), [Tweet](https://x.com/llama_index/status/1719021921462067654?s=20).
- We introduced a method for fine-tuning an Evaluator to distill GPT-4 into GPT-3.5, enhancing LLM output assessment while reducing costs and improving speed. [Tweet](https://x.com/llama_index/status/1719868813318271242?s=20).
- We introduced `ParamTuner`, a hyperparameter tuning abstraction for LlamaIndex RAG, streamlining the process with objective functions and support for grid search, including integration with Ray Tune for enhanced optimization. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/param_optimizer/param_optimizer.ipynb), [Tweet](https://twitter.com/llama_index/status/1721209688703062234?s=20).

**🎥** Demos:

- GPTDiscord is a versatile LLM-powered Discord bot with over 20 features, including multi-modal image understanding and advanced data analysis. It boasts an infinite conversational memory and the ability to interact with various file types and internet services. [Tweet](https://twitter.com/llama_index/status/1720151524280881335?s=20).

**🗺️ Guides:**

- We shared a [guide](https://docs.llamaindex.ai/en/latest/examples/retrievers/deep_memory.html) for integrating Activeloop’s Deep Memory with LlamaIndex, a module that enhances your embeddings at ingestion and can improve RAG metrics by 15%, all while seamlessly fitting into LlamaIndex’s automated dataset and vector store features.
- We shared a [guide](https://docs.llamaindex.ai/en/latest/examples/prompts/prompt_optimization.html) inspired by [**Chengrun Yang**](https://twitter.com/chengrun_yang) and GoogleDeepMind’s `Optimization by Prompting` paper, demonstrating how to automate prompt tuning in LlamaIndex RAG pipelines using meta-prompting, boosting evaluation performance while acknowledging the experimental nature of this technique.
- We shared a [guide](https://docs.llamaindex.ai/en/latest/examples/prompts/emotion_prompt.html) on how to implement Emotion Prompting in LlamaIndex, allowing you to enhance your RAG pipeline with various emotional stimuli and evaluate their impact on task performance.
- We showcased MongoDB [starter](https://github.com/run-llama/mongodb-demo) kit, a comprehensive LlamaIndex RAG setup with Flask backend, Next frontend, and easy deployment to Render.

**✍️ Tutorials:**

- [Wenqi Glantz](https://medium.com/@wenqiglantz) made a [blog post](https://levelup.gitconnected.com/optimizing-text-embeddings-with-huggingfaces-text-embeddings-inference-server-and-llamaindex-ef7df35882a4) on deploying the HuggingFace `**text-embeddings-inference**` server on an AWS EC2 GPU instance, enhancing LlamaIndex RAG pipeline's performance and results.
- [Sophia Yang’s](https://twitter.com/sophiamyang) [tutorial](https://www.youtube.com/watch?v=QqDZVg9S_Vk) on Zephyr-7b-beta showcases its leading capabilities in LLM technology, including how it’s benchmarked with LlamaIndex for diverse AI tasks.
- [Sudarshan Koirala](https://twitter.com/mesudarshan) gave a [tutorial](https://www.youtube.com/watch?v=vJz9WVgsu9g) on how to build a multi-modal retrieval system with LlamaIndex, Qdrant, and bge/CLIP embeddings.
- [Sophia Yang’s](https://twitter.com/sophiamyang) gave another [tutorial](https://www.youtube.com/watch?v=ihSiRrOUwmg), this time on Small-to-Big Retrieval with LlamaIndex in building advanced RAG systems.
- [Ravi Theja’s](https://www.linkedin.com/in/ravidesetty/) [tutorial](https://www.youtube.com/watch?v=X8BHWGXXdW0) on the Router Query Engine that helps you to set up multiple indices/ query engines for your dataset, allowing the LLM to choose the most suitable one for each specific question.

**⚙️ Integrations &amp; Collaborations:**

- We integrated the [**Tavily AI**](https://tavily.com/) research API into the LlamaIndex RAG pipeline, offering a robust tool for web research to enhance LLM agent automation. [Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/tools/notebooks/tavily.ipynb), [Tweet](https://x.com/llama_index/status/1719745197729599681?s=20).
- We integrated [**Noam Gat**](https://twitter.com/noamgat)’s LLM Enforcer into the LlamaIndex RAG pipeline to ensure structured outputs for various models. [Docs](https://docs.llamaindex.ai/en/latest/community/integrations/lmformatenforcer.html), [Tweet](https://twitter.com/llama_index/status/1720103157412647265?s=20).
- We integrated the latest Embed v3 model from CohereAI, enhancing document retrieval quality within the LlamaIndex RAG pipeline. [Notebook](https://t.co/NOQxN9RJi3), [Tweet](https://twitter.com/llama_index/status/1720216603584069875?s=20).
- We integrated the new Voyage AI embedding model, a top-performing option for RAG pipelines. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/embeddings/voyageai.ipynb), [Tweet](https://x.com/llama_index/status/1720578050180686129?s=20).