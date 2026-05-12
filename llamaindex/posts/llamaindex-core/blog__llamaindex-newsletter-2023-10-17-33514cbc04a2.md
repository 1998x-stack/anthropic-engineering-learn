---
title: "LlamaIndex Newsletter 2023–10–17"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-10-17-33514cbc04a2"
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







Hello Llama Enthusiasts 🦙!

Another week has flown by, and we’re back with a jam-packed newsletter filled with updates on hackathons, guides, integrations, features, webinars, tutorials, blogs, and demos. If you have a project, blog post, or video that deserves a spotlight, we’d love to feature it! Just reach out to us at [news@llamaindex.ai](mailto:news@llamaindex.ai).



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Bonus: You can now get all these updates straight to your inbox! Simply visit our [homepage](https://www.llamaindex.ai/) and sign up for our email updates.

🤩 **First, the highlights:**

- **AI.Engineer Summit**: At the AI.Engineer Summit, Jerry Liu discussed RAG applications, while Simon led a workshop on RAG app optimization (Jerry’s [slides](https://docs.google.com/presentation/d/1v7T6ejrSo87ndGeGC7tt6zeq-cftu03WWw7WL8Jskug/edit#slide=id.p), Simon’s [slides](https://github.com/run-llama/ai-engineer-workshop/blob/main/presentation.pdf))
- **Text to pgVector**: we launched PGVectorSQLQueryEngine for combined SQL and vector queries on PostgreSQL. ([Docs](https://t.co/4h3nTzzJ5E), [Tweet](https://x.com/jerryjliu0/status/1712496323742851188?s=20))
- **Hugging Face Integration**: Integrated with HuggingFace’s text-embeddings-inference server for high-speed, large-scale BERT model serving. ([Docs](https://docs.llamaindex.ai/en/latest/examples/embeddings/text_embedding_inference.html), [Tweet](https://x.com/jerryjliu0/status/1712943016590381554?s=20))
- **Multi-Document Agents**: New V1 agents support advanced multi-document retrieval and async query planning. ([Docs](https://t.co/bWYv0R7J2B), [Tweet](https://x.com/llama_index/status/1712129914386993295?s=20))
- **Unstructured Parsing**: Unveiled UnstructuredElementNodeParser, a hierarchical parser for embedded tables/text using UnstructuredIO. ([Docs](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table.html), [Tweet](https://x.com/llama_index/status/1711768906866864403?s=20))
- **LLM Compatibility**: We have charted LLM performances on various tasks and found that the Zephyr-7b-alpha model stands out as the top-performing 7B model in advanced RAG tasks. ([Docs](https://docs.llamaindex.ai/en/latest/core_modules/model_modules/llms/root.html#llm-compatibility-tracking))

# 🏆 Congratulations to our AGI House Hackathon Winners!

We love seeing people build amazing things with LlamaIndex!

**Build:**

- [Demostify](https://drive.google.com/file/d/18Ru1FCchVpMi8jzjr2dHdDuZtCG83zOJ/view)
- [Stick with Fit](https://docs.google.com/presentation/d/1pOa8AppiKpuF-aQvsD5vKebeL6Gf9lmP505FavrFOm4/edit#slide=id.g2899cea0752_0_15), [SafeQuery](https://github.com/chisler/safequery), Cherry

**Break:**

- [Fuzzy Access](https://github.com/jeremy-brouillet/agi-hackathon)

**Test:**

- X-Ray Insight

**Honorable Mentions:**

- [KindleGPT](https://glasp.co/know-thyself/)
- PenTest

# 🎤 LlamaIndex at [AI.Engineer Summit](https://twitter.com/aiDotEngineer):

- [Jerry Liu](https://twitter.com/jerryjliu0) gave a talk on Building production-ready RAG applications. [Slides](https://docs.google.com/presentation/d/1v7T6ejrSo87ndGeGC7tt6zeq-cftu03WWw7WL8Jskug/edit#slide=id.p).
- [Simon](https://twitter.com/disiok) conducted a workshop on Building, Evaluating, and Optimizing your RAG App for Production with LlamaIndex. [Slides](https://github.com/run-llama/ai-engineer-workshop/blob/main/presentation.pdf), [Code](https://github.com/run-llama/ai-engineer-workshop/tree/main).

# 🗺️ Guides:

- **LLM Compatibility Tracking:** We’ve charted LLM performances on various tasks, revealing zephyr-7b-alpha as the only current 7B model excelling in advanced RAG/ Agentic tasks. [Docs](https://docs.llamaindex.ai/en/latest/core_modules/model_modules/llms/root.html#llm-compatibility-tracking).
- **Evaluations:** Adjusting chunk size is essential for RAG apps. Having more chunks isn’t necessarily better, and re-ranking might be counterproductive. To fine-tune, experiment with different chunk sizes and top-k values. The Arize AI team has provided a guide to help you evaluate using Arize AI Phoenix and Llama Index. [Slides](https://docs.google.com/presentation/d/18Z7H3WSncPzLOTHKZAj36w0E7HSGY78VkDooSzvvySE/edit), [Notebook](https://colab.research.google.com/drive/1Siufl13rLI-kII1liaNfvf-NniBdwUpS?usp=sharing).

# ✍️ Tutorials:

- [Shahul’s](https://twitter.com/Shahules786) [tutorial](https://t.co/oTA2O8sE21) demonstrates how to choose the best embeddings for your data, emphasizing that retriever performance and embedding quality are crucial for a RAG system’s efficacy using the LlamaIndex and RAGAS libraries.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz)’s [tutorial](https://levelup.gitconnected.com/evaluation-driven-development-the-swiss-army-knife-for-rag-pipelines-dba24218d47e) on Evaluation Driven Development for RAG Pipelines.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz)’s [tutorial](https://betterprogramming.pub/masking-pii-data-in-rag-pipeline-326d2d330336) on Masking PII Data in the RAG Pipeline.
- Ofer Mendelevitch’s from [Vectara](https://twitter.com/vectara) has a [tutorial](https://vectara.com/retrieval-augmented-generation-rag-done-right-retrieval/) on Retrieval Augmented Generation with LlamaIndex on comparing Vectara’s new Boomerang model to OpenAI and Cohere.
- [Patrick Loeber](https://twitter.com/patloeber) from AssemblyAI has a [tutorial](https://www.youtube.com/watch?v=alT-0mNRF-c) on Build LlamaIndex Audio Apps.
- [Pradip Nichite](https://www.linkedin.com/in/pradipnichite/) made a [tutorial](https://www.youtube.com/watch?v=ZRSI8LHpqBA) on NL2SQL with LlamaIndex: Querying Databases Using Natural Language.
- [Mayo Oshin](https://twitter.com/mayowaoshin) has a [tutorial](https://www.youtube.com/watch?v=UmvqMscxwoc) on How to Compare Multiple Large PDF Files.
- [Sudarshan Koirala](https://twitter.com/mesudarshan) made a [tutorial](https://www.youtube.com/watch?v=4kwAhzzaW4A) on Chat With Documents with LlamaIndex and Pinecone.

# 💡 Demos:

- [Siva Surendira](https://twitter.com/siva_1gc) built [YC Bot](https://www.theycbot.com/) to get instant startup advice from your favorite YC mentors.

# ✨ Feature Releases and Enhancements:

- **Text to pgVector:** We introduced the PGVectorSQLQueryEngine, which allows you to query a PostgreSQL database using both full SQL and vector search simultaneously. [Docs](https://t.co/4h3nTzzJ5E), [Tweet](https://x.com/jerryjliu0/status/1712496323742851188?s=20).
- **Multi-Document Agents:** We introduce Multi-Document Agents (V1) that can now retrieve across multiple docs and plan queries asynchronously, offering a superior analysis compared to standard RAG. [Docs](https://t.co/bWYv0R7J2B), [Tweet](https://x.com/llama_index/status/1712129914386993295?s=20).
- **UnstructuredIO:** We’ve partnered with UnstructuredIO to enhance LLM/RAG applications. By extracting tables from PDFs, we’ve improved query methods beyond basic vector indexing, enabling hybrid queries and cross-document comparisons, especially for tabular questions. [Docs](https://t.co/Ezts2C9Rpw), [Tweet](https://x.com/jerryjliu0/status/1710685292913668595?s=20).
- **UnstructuredElementNodeParser:** Going beyond basic text-splitting, we introduce the UnstructuredElementNodeParser. It models embedded tables/text hierarchically in a data graph using UnstructuredIO. [Docs](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table.html), [Tweet](https://x.com/llama_index/status/1711768906866864403?s=20).
- **Cross-Encoder Fine-Tuning:** Cross-encoders enhance RAG by refining post-embedding search results. With LlamaIndex, you can now fine-tune cross-encoders on any document, boosting performance. [Docs](https://t.co/vAyv94dFk2), [Tweet](https://x.com/jerryjliu0/status/1712856457413370110?s=20).

# ⚙️ Integrations &amp; Collaborations:

- **Assembly AI:** We introduced a new data reader for audio data integration with AssemblyAI. This integration allows effortless audio loading and facilitates building vector store indices and query engines for inquiries. [Docs](https://llamahub.ai/l/assemblyai), [Tweet](https://x.com/llama_index/status/1711156989106299249?s=20).
- **Nougat — MetaAI:** We integrated Nougat, an exceptional OCR tool from Meta, that excels in interpreting scientific papers, notably mathematical notations, and LaTeX as a loader in LlamaHub, allowing streamlined processing of ArXiv papers within the RAG pipeline. [Docs](https://llamahub.ai/l/nougat_ocr), [Tweet](https://x.com/llama_index/status/1711896904928292976?s=20).
- **Hugging Face-Text Embeddings Inference:** We integrated with the new text-embeddings-inference server from HuggingFace offering production-scale serving with distributed tracing for all BERT models at impressive speeds. [Docs](https://docs.llamaindex.ai/en/latest/examples/embeddings/text_embedding_inference.html), [Tweet](https://x.com/jerryjliu0/status/1712943016590381554?s=20).

# 🎥 Webinars And Podcast:

- [Webinar](https://www.youtube.com/watch?v=EYMZVfKcRzM) with Timescale on Time-based retrieval for RAG.
- [Webinar](https://www.youtube.com/watch?v=POBcYr0sbcg) with Omar Khattab and Thomas Joshi on DSPy — a framework for LLMs that emphasizes programming over prompting.
- Jerry Liu’s [podcast](https://www.latent.space/p/llamaindex#details) with Latent Space on LlamaIndex’s origin story, fine-tuning, and more.