---
title: "LlamaIndex Newsletter 2024–02–27"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-02-27-4b9102a0f824"
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







 Yo, LlamaIndex Fans 🦙,



 Dive into a week brimming with thrilling developments at LlamaIndex! The dynamic input from our community and our rich selection of learning materials are all set to enhance your journey with LlamaIndex.



 Last week, the LlamaIndex ecosystem took a significant leap forward with the launch of LlamaParse, a suite of advanced services designed for **production-level** **context enhancement** in LLM and RAG applications:


-  **LlamaParse:** Offers sophisticated parsing for complex documents, making it possible to answer detailed queries.
  -  **Managed Ingestion and Retrieval API:** Facilitates easier data management, connecting with over 150 sources and 40+ storage solutions.



 LlamaParse is now available for a public preview, primarily focusing on PDFs with a user cap, while the API is in a private preview for select enterprise partners. If you haven’t explored these new features yet, we invite you to [check them out](https://blog.llamaindex.ai/introducing-llamacloud-and-llamaparse-af8cedf9006b) for more details or to discuss commercial terms.



 Your innovation inspires us! We’re eager to see the projects, articles, or videos that inspire you. Share your remarkable works with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). And if you haven’t already, subscribe to our newsletter on our website to receive the latest LlamaIndex updates straight to your inbox.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



 🤩 **The highlights:**


-  **Enhanced RAG Retrieval with Sub-Document Summaries:** Introducing a novel chunking method that improves RAG performance by incorporating hierarchical metadata into chunks, ensuring precise and context-aware information retrieval. [Notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-subdoc-summary/examples/subdoc-summary.ipynb), [Tweet](https://x.com/llama_index/status/1761793821422264757?s=20).
  -  **MistralAI Cookbook:** A comprehensive guide to leveraging the Mistral-Large model from MistralAI, featuring near-GPT-4 reasoning, function calling, and JSON output for cutting-edge applications. [Docs](https://docs.llamaindex.ai/en/latest/cookbooks/mistralai.html), [Tweet](https://x.com/llama_index/status/1762231085243719748?s=20).
  -  **Gemma Cookbook:** A comprehensive guide to using Gemma, GoogleDeepMind’s latest LLM offering, with options for 2B and 7B parameters, facilitating the development of local RAG systems on your laptop. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/ollama_gemma.ipynb), [Tweet](https://x.com/jerryjliu0/status/1760471196402069771?s=20).
  -  **ColBERT Integration:** Document reranking with ColBERT via LlamaIndex, delivering a solution that is about 100x faster than BERT-based models for more efficient data processing. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/ColbertRerank.ipynb), [Tweet](https://x.com/llama_index/status/1760830777179471933?s=20).
  -  **Counselor Copilot — Social Impact Through RAG:** Spotlight on Counselor Copilot, an innovative RAG project supporting the Trevor Project’s crisis counselors, providing real-time assistance with context, suggestions, and actions to aid LGBTQ+ youth effectively. [BlogPost](https://blog.llamaindex.ai/bridging-the-gap-in-crisis-counseling-introducing-counselor-copilot-db42e26ab4f3), [Tweet](https://x.com/llama_index/status/1761433854458614075?s=20).



 **✨ Feature Releases and Enhancements:**


-  We have launched a new chunking strategy to enhance RAG retrieval: Sub-Document Summaries. This approach overcomes the limitations of naive chunking by injecting hierarchical metadata, offering a nuanced balance of global context awareness and precision through subdocument summaries for improved performance. [Notebook](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-subdoc-summary/examples/subdoc-summary.ipynb), [Tweet](https://x.com/llama_index/status/1761793821422264757?s=20).
  -  We have launched a cookbook for the latest `mistral-large`  model from MistralAI offering advanced features like near GPT-4 level reasoning, Function calling, JSON Output, and more. [Docs](https://docs.llamaindex.ai/en/latest/cookbooks/mistralai.html), [Tweet](https://x.com/llama_index/status/1762231085243719748?s=20).
  -  We have launched a cookbook on Gemma, a new family of state-of-the-art LLMs by GoogleDeepMind, with 2B and 7B parameter options using Ollama to build local RAG on your laptop. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/ollama_gemma.ipynb), [Tweet](https://x.com/jerryjliu0/status/1760471196402069771?s=20).
  -  We have introduced ColBERT through LlamaIndex, offering a one-line integration for a reranking model that’s ~100x faster than traditional BERT-based models, ensuring efficient document handling with superior performance. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/node_postprocessor/ColbertRerank.ipynb), [Tweet](https://x.com/llama_index/status/1760830777179471933?s=20).
  -  We have introduced a way to integrate advanced RAG into full-stack web apps with create-llama, using LlamaPacks, in just two lines of code. [create-llama](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama), [Tweet](https://x.com/llama_index/status/1761159412629336404?s=20).



 **🎥 Demos:**



 [Counselor Copilot](https://github.com/zrizvi93/trevorhack): An interesting RAG project by [Riya Jagetia](https://twitter.com/FintechRiya) and team, designed to assist crisis counselors at the Trevor Project in supporting LGBTQ+ youth. This tool acts as a real-time copilot, offering context, suggested replies, and various actions to enhance counselor effectiveness, showcasing a unique and socially impactful application of advanced RAG techniques. [BlogPost](https://blog.llamaindex.ai/bridging-the-gap-in-crisis-counseling-introducing-counselor-copilot-db42e26ab4f3), [Tweet](https://x.com/llama_index/status/1761433854458614075?s=20).



 **🗺️ Guides:**


-  [Guide](https://docs.google.com/presentation/d/1NAAI6DoLEIw7RDvx4vXvFG2jz3WUKVpL4j39-E9MouQ/edit#slide=id.g2b99c281f78_0_0) to simplifying advanced RAG development: Our latest insights pinpoint solutions for key challenges, including our innovative LlamaParse for complex PDF QA, shared in our AI in Production presentation.



 **✍️ Tutorials:**


-  [Marco Bertelli](https://medium.com/@marco.bertelli) [tutorial](https://medium.com/@marco.bertelli/unveiling-the-power-of-rag-building-an-interactive-chatbot-with-react-a-comprehensive-guide-99c409a5f69a) on Building an Interactive Chatbot with React.
  -  [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial](https://towardsdatascience.com/the-journey-of-rag-development-from-notebook-to-microservices-cc065d0210ef) on The Journey of RAG Development: From Notebook to Microservices.
  -  [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial video](https://www.youtube.com/watch?v=EBpT_cscTis) on 12 RAG Pain Points and Solutions in the RAG pipeline.



 🎥 **Webinar:**


-  [Webinar](https://www.youtube.com/watch?v=ZP1F9z-S7T0) with Sisil from JasperAI on Practical Tips and Tricks for Productionizing RAG.