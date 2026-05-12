---
title: "LlamaIndex Newsletter 2023–10–31"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-10-31-36244e2b3f0c"
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







Greetings Llama Enthusiasts 🦙!

Another week has zoomed past, and here we are with our latest roundup of updates, features, tutorials, and so much more. Have a noteworthy project, article, or video to share? We’d love to feature it! Reach out to us at [news@llamaindex.ai](mailto:news@llamaindex.ai).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Want these updates straight to your inbox? Simply subscribe to our newsletter on our [homepage](https://www.llamaindex.ai/).

🤩 **First, the highlights:**

- **Revamped Documentation:** Overhauled [docs](https://docs.llamaindex.ai/en/stable/) for smoother LLM/RAG app development.
- **Contribution Board:** Our new [board](https://github.com/orgs/run-llama/projects/2) welcomes community-driven LlamaIndex enhancements.
- **Zephyr-7b-beta Insights:** [Tested and verified](https://colab.research.google.com/drive/1UoPcoiA5EOBghxWKWduQhChliMHxla7U?usp=sharing) for unmatched ReAct agent task efficiency on LlamaIndex.
- **Image Captioning Boost For RAG:** LLaVa’s outputs are now supercharged with knowledge-based augmentation. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/llava_multi_modal_tesla_10q.ipynb), [Tweet](https://x.com/jerryjliu0/status/1717205234269983030?s=20)

**✨ Feature Releases and Enhancements:**

- We introduced Retrieval-Augmented Image Captioning, enhancing LLaVa multi-modal model outputs with knowledge base insights. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/llava_multi_modal_tesla_10q.ipynb), [Tweet](https://x.com/jerryjliu0/status/1717205234269983030?s=20).
- We introduced the ability to view and set prompts for LlamaIndex modules in just two lines of code. [Docs](https://github.com/run-llama/llama_index/blob/main/docs/examples/prompts/prompt_mixin.ipynb), [Tweet](https://twitter.com/llama_index/status/1716847554401628516?s=20).
- We introduced the integration of our `OpenAILike` class, allowing users to tap into various open-source LLM projects with OpenAI-compatible APIs, irrespective of the model provider. [Tweet](https://x.com/llama_index/status/1716950167474356715?s=20).
- We introduced Prompt Compression for RAG: with LongLLMLingua, which helps to cut token usage and latency by up to 20x. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/LongLLMLingua.ipynb), [Tweet](https://x.com/llama_index/status/1717601235828973681?s=20).
- We introduced a method to refine open-source LLMs like llama2 for structured data outputs. Using LlamaIndex, transform llama2–7b to produce Pydantic objects without PyTorch. Our guide covers synthetic dataset creation, fine-tuning, and RAG pipeline integration. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/finetuning/gradient/gradient_structured.ipynb), [Tweet](https://x.com/llama_index/status/1718299602884137182?s=20).

**🎥** Demos:

- Harshad Suryawanshi did a [demo](https://ai-eqty-rsrch-anlyst.streamlit.app/) on equity research report generator using LlamaIndex and Streamlit.
- [Bharat Ramanathan](https://twitter.com/ParamBharat) built [Wandbot](https://x.com/llama_index/status/1717940770270011898?s=20), a live RAG app enabling chat over Weights &amp; Biases documentation, integrated with Discord and SlackHQ. Key features include periodic data ingestion, custom document and code parsing, model fallback, and logging with Weights and biases.

**🗺️ Guides:**

- We introduced a revamped documentation structure tailored to guide users from prototyping to production of LLM/RAG apps using LlamaIndex. Dive into our 200+ guides to enhance your app. [Docs](https://docs.llamaindex.ai/en/stable/), [Tweet](https://twitter.com/llama_index/status/1717627450690269284?s=20).
- We unveil our new Request For Contribution Github board [here](https://github.com/orgs/run-llama/projects/2). It’s your guide to contribute to LlamaIndex, streamlining community suggestions.
- We released the [guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/embeddings/jina_embeddings.ipynb) on using the Jina 8k open-source text embedding model with LlamaIndex.
- We introduce our comprehensive survey of llama2-chat models across varying capacities in LlamaIndex. The major insight: While reasoning is enhanced with more parameters, structured outputs remain a challenge. [Tweet](https://twitter.com/llama_index/status/1717337923853664573?s=20).
- We share a [guide](https://colab.research.google.com/drive/1UoPcoiA5EOBghxWKWduQhChliMHxla7U?usp=sharing) to test the newly released HuggingFace Zephyr-7b-beta model on LlamaIndex RAG/agent tasks, it stood out as the only 7B LLM capable of handling ReAct agent tasks over data.
- We share a new [guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/prompts/prompts_rag.ipynb) on Advanced Prompt Engineering for RAG. Learn about understanding, customizing, and extending RAG prompts, from QA templates to few-shot examples and context/query transformations. [Tweet](https://x.com/llama_index/status/1718657660697149509?s=20).

**✍️ Tutorials:**

- [Kiran](https://www.linkedin.com/in/kirannpanicker/) made a [blog post](/mastering-pdfs-extracting-sections-headings-paragraphs-and-tables-with-cutting-edge-parser-faea18870125) on Mastering PDFs: Extracting Sections, Headings, Paragraphs, and Tables with Cutting-Edge Parser.
- [Wenqi Glantz](https://medium.com/@wenqiglantz) gave us an excellent [blog post](https://levelup.gitconnected.com/optimizing-text-embeddings-with-huggingfaces-text-embeddings-inference-server-and-llamaindex-ef7df35882a4) on Optimizing Text Embeddings with HuggingFace’s text-embeddings-inference Server and LlamaIndex.
- [Ravi Theja’s](https://www.linkedin.com/in/ravidesetty/) [blog post](/nvidia-research-rag-with-long-context-llms-7d94d40090c4) delves into NVIDIA Research on RAG vs Long Context LLMs, questioning the necessity of RAG in the presence of long-context LLMs.
- [Sudarshan Koirala](https://twitter.com/mesudarshan) has a tutorial on Extracting Tables + Texts from .htm pages for RAG Using LlamaIndex.
- [Wenqi Glantz](https://medium.com/@wenqiglantz) also made a second [blog post](https://levelup.gitconnected.com/multimodal-retrieval-with-text-embedding-and-clip-image-embedding-for-backyard-birds-599f19057a70) on Multimodal Retrieval with Text Embedding and CLIP Image Embedding for Backyard Birds.

**⚙️ Integrations &amp; Collaborations:**

- We introduced our new cookbooks in partnership with Gradient AI, enabling effortless fine-tuning of open-source LLMs like Llama 2 and integration into your LlamaIndex RAG pipeline. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/gradient/gradient_text2sql.html), [Tweet](https://x.com/jerryjliu0/status/1716476285046952049?s=20).
- We introduced integration with HuggingFace Inference API which gives access to over 150,000 models. Now you can plugin any `conversational`, `text_generation`, `feature_extraction` endpoints into your LlamaIndex app. [Docs](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/huggingface.ipynb), [Tweet](https://twitter.com/llama_index/status/1716847554401628516?s=20).

**🎥 Webinars:**

- [Mayo Oshin](https://twitter.com/mayowaoshin) and [Jerry Liu](https://twitter.com/jerryjliu0) gave a [webinar](https://www.crowdcast.io/c/n0roka37yfw0) on Unlocking ChatGPT for Business.

📚Workshops:

- Jerry Liu and Simon conducted a Multipart LlamaIndex workshop in collaboration with Anyscale.
- Ravi Theja conducted a day-long [workshop](https://hasgeek.com/fifthelephant/llamaindex-workshop-10-28/) on Retrieval Augmented Generation with LlamaIndex.