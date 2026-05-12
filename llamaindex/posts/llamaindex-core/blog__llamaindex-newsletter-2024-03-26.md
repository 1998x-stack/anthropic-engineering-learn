---
title: "LlamaIndex Newsletter 2024-03-26"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-03-26"
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







 Hi there, LlamaIndex followers! 🦙







 Welcome to another thrilling weekly update from the LlamaUniverse. We&#39;re excited to bring you a fantastic array of updates, including Privacy-Preserving In-Context Learning with LlamaPacks and RAG Networks. Dive into our guides on MistralAI, explore Gemma LLMs, and enjoy a plethora of engaging tutorials using LlamaIndex, alongside upcoming webinars and events.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



####  🤩 **The highlights:**


-  **Privacy-Preserving In-Context Learning:** Leveraging **[Xinyu Tang](https://twitter.com/XinyuTang7)’s** [paper](https://arxiv.org/abs/2309.11765), we&#39;ve introduced LlamaPack for LLM/RAG apps, enabling the creation of few-shot demonstrations that maintain privacy and data integrity. [LlamaPack](https://llamahub.ai/l/llama-packs/llama-index-packs-diff-private-simple-dataset?from=llama-packs), [Tweet](https://x.com/llama_index/status/1770837291855991085?s=20).
  -  **Privacy-Preserving RAG Network:** We present Privacy-Preserving RAG Network which facilitates the use of confidential datasets in healthcare and online platforms while safeguarding user privacy. [Blogpost](https://www.llamaindex.ai/blog/retrieving-privacy-safe-documents-over-a-network), [Tweet](https://x.com/llama_index/status/1770966231769854076?s=20).
  -  **Advanced RAG and Agents with MistralAI:** [Guide](https://docs.google.com/presentation/d/1dbfoxzNcoI-D45RKZfO1UfBJIr4v0YtHhj1cwuCj020/edit#slide=id.p) on using MistralAI with LlamaIndex and LlamaParse, advancing RAG capabilities and agent development through custom pipelines and sophisticated parsing.



####  **✨ Feature Releases and Enhancements:**


-  We launched a LlamaPack based on **[Xinyu Tang](https://twitter.com/XinyuTang7)’s** [paper](https://arxiv.org/abs/2309.11765) ****for secure in-context learning in LLM/RAG apps, focusing on generating few-shot demonstrations from private datasets with differential privacy, ensuring the synthetic examples reflect the data distribution without exposing sensitive details. [LlamaPack](https://llamahub.ai/l/llama-packs/llama-index-packs-diff-private-simple-dataset?from=llama-packs), [Tweet](https://x.com/llama_index/status/1770837291855991085?s=20).
  -  We introduced a privacy-preserving RAG network by [Andrei](https://www.linkedin.com/in/nerdai/) in LlamaIndex, enabling the use of sensitive datasets like healthcare and online user data without compromising individual privacy. This approach allows data providers to synthetically generate and share data for RAG queries securely. [Blogpost](https://www.llamaindex.ai/blog/retrieving-privacy-safe-documents-over-a-network), [Tweet](https://x.com/llama_index/status/1770966231769854076?s=20).
  -  We introduce a template by [**Sasha**](https://twitter.com/hackgoofer) for agent-human interaction in RAG implementations, focusing on minimal human input. It triggers human intervention only for vague or malformed queries, enhancing clarity and precision in the response process. [LlamaPack](https://llamahub.ai/l/llama-packs/llama-index-packs-query-understanding-agent?from=llama-packs), [Tweet](https://x.com/llama_index/status/1771207903439159404?s=20).
  -  [BAM Elevate](https://twitter.com/BAMelevate) integrated Databricks Vector Search into LlamaIndex, enabling vector search capabilities within the Databricks ecosystem. [Blogpost](https://www.bamelevate.com/news/llamaindex-and-databricks-integration-announcement), [Tweet](https://x.com/llama_index/status/1770585400840699974?s=20).
  -  We launched LlamaParse integration with LlamaIndex TypeScript, an industry-leading parser for PDFs and various document types accessible directly from JS/TS. Utilize the create-llama command-line tool or integrate LlamaParse directly into your app for enhanced document processing. [Example](https://github.com/run-llama/LlamaIndexTS/blob/main/examples/readers/src/llamaparse.ts), [Tweet](https://x.com/llama_index/status/1770496142020895159?s=20).



####  **🗺️ Guides:**


-  [Guide](https://docs.google.com/presentation/d/1dbfoxzNcoI-D45RKZfO1UfBJIr4v0YtHhj1cwuCj020/edit#slide=id.p) to Advanced RAG and Agents with MistralAI using LlamaIndex and LlamaParse to construct sophisticated RAG and agents, including custom query pipelines, document parsing, and reference applications.
  -  [Guide](https://www.kaggle.com/code/iamleonie/advanced-rag-with-gemma-weaviate-and-llamaindex) to Integrating Custom Models with LlamaIndex: [Leonie Monigatti](https://twitter.com/helloiamleonie) demonstrates the process of incorporating your custom model, like Gemma, into LlamaIndex
  -  [Guide](https://www.llamaindex.ai/blog/secure-rag-with-llamaindex-and-llm-guard-by-protect-ai) to combat prompt injection attacks, like the &quot;white text&quot; attack, by rigorously screening data during ingestion and retrieval, ensuring the integrity of LLM-powered systems against deceptive manipulations by [Oleksandr Yaremchuk](https://twitter.com/alex_yaremchuk) from [Protect AI](https://twitter.com/ProtectAICorp).



####  **✍️ Tutorials:**


-  [Akriti Upadhyay](https://twitter.com/AkritiUpadhya13)’s [tutorial](https://medium.com/@akriti.upadhyay/integrating-llamaindex-and-qdrant-similarity-search-for-patient-record-retrieval-7090e77b971e) to prototype on patient data safely, featuring synthetic dataset generation, storage in Qdrant Vector DB, and querying with llama.cpp LLM using LlamaIndex.
  -  [Frank Baele](https://twitter.com/BaeleFrank)’s [tutorial](https://franz.be/blogpost/bringing-a-naive-rag-to-production) on developing a production-grade RAG pipeline with LlamaParse, detailing document parsing, advanced ingestion techniques, Vector DB selection, and insights on evaluation, deployment, and budget management.
  -  [Video tutorial](https://www.youtube.com/watch?v=xwfR8fC_Azs) by Ashish on creating an advanced PDF RAG agent, utilizing LlamaParse for text and tables extraction, defining retrievers and routers, and adding a sub-question layer, all integrated with LlamaIndex and MistralAI.
  -  [UpTrain](https://twitter.com/UpTrainAI) [tutorial](https://www.llamaindex.ai/blog/supercharge-your-llamaindex-rag-pipeline-with-uptrain-evaluations) on Supercharge your LlamaIndex RAG Pipeline with UpTrain Evaluations.
  -  [Ravi Theja](https://twitter.com/ravithejads) [tutorial](https://ravidesetty.medium.com/introducing-navarasa-2-0-indic-gemma-7b-2b-instruction-tuned-model-on-15-indian-languages-31f6565b2750) on showcasing RAG with LlamaIndex on 15 Indian languages using Navarasa-2.0 - a Gemma finetuned model on 15 Indian languages.



####  🎥 **Webinars:**



 [Register for a webinar](https://lu.ma/z2vhi06e) with [**Daniel Huynh**](https://twitter.com/dhuynh95) featuring LaVague, an agent that can navigate the web in your Jupyter/Colab notebook.



####  📅 Events:


-  [Join us](https://x.com/lablabai/status/1770847744313241637?s=20) for a Panel discussion on &#39;Why RAG Will Never Die - The Context Window Myth’ with panelists from LlamaIndex, Vectara, Nvidia, and TogetherAI.
  -  We are hosting a RAG [meetup](https://www.meetup.com/paris-retrieval-augmented-generation-group/events/299374545/) in Paris on March 27th featuring talks on advanced RAG strategies, building a RAG CLI, and the significance of open-source RAG in business.