---
title: "LlamaIndex Update: New Features &amp; RAG Tips | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-update-09-03-2023-4a7c21c0f60b"
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







Hello LlamaIndex Community!

We’re thrilled to bring you the latest edition of our LlamaIndex Update series. Whether you’ve been a part of our journey from the start or have just recently joined us, your engagement and input are invaluable to us.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In this update, we’re excited to unveil some significant advancements. We’ve got comprehensive updates on new features for both the Python and TypeScript versions of LlamaIndex. In addition, we’re offering some expert insights on RAG tips that you won’t want to miss. To keep you ahead of the curve, we’ve also curated a selection of webinars, tutorials, events, and demos.

So without further ado, let’s delve into the latest developments.

# **New Features:**

## LlamaIndex

- LlamaIndex introduces the Sweep AI code splitter for RAG apps, addressing the challenges of traditional code splitting. This tool features recursive splitting combined with CSTs across 100+ languages, enhancing the LlamaIndex experience. [BlogPost](https://docs.sweep.dev/blogs/chunking-2m-files), [Tweet](https://twitter.com/jerryjliu0/status/1686413452988878849?s=20).
- LlamaIndex now supports streaming data ETL, enhancing structured data extraction with the OpenAI Function API. By inputting a Pydantic object class in LlamaIndex, users can receive streamed data objects from OpenAI individually. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/output_parsing/openai_pydantic_program.html#extraction-into-album-streaming), [Tweet](https://twitter.com/jerryjliu0/status/1686752090197008387?s=20).
- LlamaIndex has teamed up with Neo4j to amplify knowledge graph capabilities with LLM’s. This integration not only allows for storing any knowledge graph created in LlamaIndex directly in Neo4j but also introduces a specialized text-to-cypher prompt for Neo4j users. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/Neo4jKGIndexDemo.html), [Tweet](https://twitter.com/llama_index/status/1687224679340064768?s=20).
- LlamaIndex, in collaboration with Mendable AI and Nomic AI, unveils a Nomic Atlas visual map detailing user questions from the Mendable AI bot. This innovative tool groups similar questions, providing insights for improved app deployment, prompt control, language support, and documentation. New users can find the helpful Mendable AI bot on LlamaIndex’s documentation site. [Tweet](https://twitter.com/llama_index/status/1687485785228906496?s=20).
- LlamaIndex, in collaboration with Predibase, offers an optimal way to operationalize LLMs. Experience top-tier RAG by privately hosting open-source LLMs on managed infrastructure right within your VPC. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/llm/predibase.html), [Tweet](https://twitter.com/predibase/status/1687493843619598336?s=20).
- The LlamaIndex playground [app](https://llama-playground.vercel.app/) enhances the RAG experience. Updates include new Temperature and Top P options, along with intuitive tooltips offering plain language explanations.
- LlamaIndex Tip💡: Boost your RAG systems by adding structured data to raw text. This allows for easier metadata filtering and optimal embedding biases. Dive into our guide on harnessing the HuggingFace span marker for targeted entity extraction. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/metadata_extraction/EntityExtractionClimate.html), [Tweet](https://twitter.com/llama_index/status/1688711638537682944?s=20).
- LlamaIndex now has the Semantic Scholar Loader. With it, users can swiftly set up citation-based Q&amp;A systems. [Docs](https://llamahub.ai/l/semanticscholar), [Tweet](https://twitter.com/shauryr/status/1687858252481236993?s=20).
- LlamaIndex highlights the significance of text chunk size in LLM QA systems. To determine the best chunk size without human intervention, we suggest ensembling different sizes and using a reranker for context relevance during queries. This method involves simultaneous queries across retrievers of various sizes and consolidating results for reranking. Though experimental, this approach aims to discern the optimal chunk size strategy. [Docs](https://gpt-index.readthedocs.io/en/stable/examples/retrievers/ensemble_retrieval.html), [Tweet](https://twitter.com/jerryjliu0/status/1688948298781249536?s=20).
- LlamaIndex’s customer support bot seamlessly interfaces with Shopify’s 50k-line GraphQL API Spec. Through smart tools and LlamaIndex features, it offers quick insights like `refunded orders` despite the vast spec size. Efficient indexing ensures precise user query responses. [Docs](https://llamahub.ai/l/tools-shopify), [Tweet](https://twitter.com/jerryjliu0/status/1689295239822069760?s=20).
- LlamaIndex’s integration with Xinference enables users to effortlessly expand models like llama 2, chatglm, and vicuna to incorporate RAG and agents. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/llm/XinferenceLocalDeployment.html), [Tweet](https://twitter.com/llama_index/status/1689426281015005184?s=20).
- LlamaIndex introduces `One-click Observability`. With just a single code line, integrate LlamaIndex with advanced observability tools from partners like Weights &amp; Biases, ArizeAI, and TruEra, simplifying LLM app debugging for production. [Docs](https://gpt-index.readthedocs.io/en/latest/end_to_end_tutorials/one_click_observability.html), [Tweet](https://twitter.com/llama_index/status/1689659395465191424?s=20).
- LlamaIndex has updated the LLM default temperature value to 0.1. [Tweet](https://twitter.com/yi_ding/status/1689692197871042561?s=20).
- LlamaIndex integration with Zep, enhancing the memory layer of LLM apps. It’s not just about storage but also enriching data with summaries, metadata, and more. [BlogPost](https://medium.com/llamaindex-blog/zep-and-llamaindex-a-vector-store-walkthrough-564edb8c22dc), [Tweet](https://twitter.com/jerryjliu0/status/1690018390059225088?s=20).
- LlamaIndex has revamped its defaults! Now, gpt-3.5-turbo is the go-to LLM, with enhanced prompts and a superior text splitter. Additionally, if OpenAI’s key isn’t set, it has backup options with llama.cpp. New embedding features have also been added. [Tweet](https://twitter.com/llama_index/status/1690081661453803520?s=20).
- LlamaIndex now seamlessly integrates with FastChat by [lmsysorg](https://twitter.com/lmsysorg). Elevate your LLM deployments like Vicuna and Llama 2, serving as an alternative to OpenAI. [Tweet](https://twitter.com/jerryjliu0/status/1691114369705533440?s=20).
- LlamaIndex provides a seamless integration with Azure AI Services. Dive into a richer ecosystem of AI tools from Computer Vision, Translation, and speech enhancing your multi-modal AI interactions. [Docs1](https://llamahub.ai/l/tools-azure_translate), [Docs2](https://llamahub.ai/l/tools-azure_speech), [Docs3](https://llamahub.ai/l/tools-azure_cv), [Tweet](https://twitter.com/llama_index/status/1691605500079800674?s=20).
- LlamaIndex unveils `Graph RAG` — an approach to enhance LLMs with context from graph databases. Extract valuable subgraphs from any knowledge graph for superior question-answering capabilities. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/knowledge_graph_rag_query_engine.html), [Tweet](https://twitter.com/jerryjliu0/status/1691835187519459338?s=20).
- LlamaIndex has expanded native async support, enhancing the scalability of full-stack LLM apps. We now offer async agents, tool execution, and callback support, and have introduced async methods in vector stores. [Tweet](https://twitter.com/llama_index/status/1691965149840908642?s=20).
- LlamaIndex enhances debugging with data agent trace observability. Additionally, system prompts can now be added to any query engine and we have begun the transition of LLM and embedding modules to Pydantic. [Docs](https://twitter.com/llama_index/status/1692696993900974399?s=20), [Tweet](https://gpt-index.readthedocs.io/en/latest/examples/callbacks/LlamaDebugHandler.html#see-traces-events-for-agents).
- LlamaIndex’s `Recursive Document Agents` enhance RAG by retrieving based on summaries and adjusting chunk retrieval per need. This boosts querying across varied documents, offering both question-answering and summarization within a document. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/recursive_retriever_agents.html), [Tweet](https://twitter.com/jerryjliu0/status/1693421308674289822?s=20).
- LlamaIndex integrates with Metaphor to supercharge data agents. This integration offers a specialized search engine tailored for LLMs, allowing dynamic data lookup beyond just RAG, and answering a broader range of questions. [BlogPost](https://medium.com/llamaindex-blog/llamaindex-metaphor-towards-automating-knowledge-work-with-llms-5520a32efa2f), [Tweet](https://twitter.com/llama_index/status/1693649115983618278?s=20).
- LlamaIndex now supports integration with OpenAI’s fine-tuned models via their new endpoint. Seamlessly integrate these models into your RAG pipeline. [Docs](https://gpt-index.readthedocs.io/en/latest/core_modules/model_modules/llms/usage_custom.html), [Tweet](https://twitter.com/llama_index/status/1694116968008401201?s=20).
- LlamaIndex introduces the `OpenAIFineTuningHandler` to streamline data collection for fine-tuning gpt-3.5-turbo with GPT-4 outputs. Run RAG with GPT-4 and effortlessly generate a dataset to train a more cost-effective model. [Notebook](https://github.com/jerryjliu/llama_index/blob/main/experimental/openai_fine_tuning/openai_fine_tuning.ipynb), [Tweet](https://twitter.com/llama_index/status/1694395355725746397?s=20).
- LlamaIndex presents the `Principled Development Practices` guide, detailing best practices for LLM app development Observability, Evaluation, and Monitoring. [Docs](https://gpt-index.readthedocs.io/en/latest/end_to_end_tutorials/principled_dev_practices.html), [Tweet](https://twitter.com/llama_index/status/1694736328276271248?s=20).
- LlamaIndex introduces a refined Prompt system. With just three core classes: `PromptTemplate`, `ChatPromptTemplate`, and `SelectorPromptTemplate`, users can effortlessly format as chat messages or text and tailor prompts based on model conditions. [Docs](https://gpt-index.readthedocs.io/en/latest/core_modules/model_modules/prompts.html#), [Tweet](https://twitter.com/llama_index/status/1695093392378880324?s=20).
- LlamaIndex delves into `chunk dreaming` a concept inspired by [Thomas H. Chapin IV](https://twitter.com/tomchapin). By auto-extracting metadata from a text chunk, it can identify potential questions and provide summaries over neighboring nodes. This enriched context boosts RAG’s performance. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/metadata_extraction/MetadataExtraction_LLMSurvey.html), [Tweet](https://twitter.com/llama_index/status/1695233836983144764?s=20).
- LlamaIndex is integrated with BagelDB, enabling developers to effortlessly tap into vector data stored on BagelDB. [Tweet](https://twitter.com/BagelDB_ai/status/1695158701387059319?s=20).
- LlamaIndex now lets the LLM choose between vector search for semantic queries or our BM25 retriever for keyword-specific ones. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/retrievers/bm25_retriever.html), [Tweet](https://twitter.com/llama_index/status/1695590257054630149?s=20).
- LlamaIndex introduces the `AutoMergingRetriever`, crafted with insights from [Jason](https://twitter.com/jxnlco) and ChatGPT. This technique fetches precise context chunks and seamlessly merges them, optimizing LLM responses. Using the HierarchicalNodeParser, we ensure interconnected chunks for enhanced context clarity. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/retrievers/auto_merging_retriever.html), [Tweet](https://twitter.com/llama_index/status/1695832757560356871?s=20).
- LlamaIndex introduces embedding finetuning for optimized retrieval performance. Beyond enhancing RAG, we’ve simplified retrieval evaluations with automatic QA dataset generation from text, streamlining both finetuning and evaluation processes. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/embeddings/finetune_embedding.html), [Tweet](https://twitter.com/llama_index/status/1696583119539966070?s=20).
- LlamaIndex now integrates directly with Airbyte sources including Gong, Hubspot, Salesforce, Shopify, Stripe, Typeform, and Zendesk Support. Easily enhance your LlamaIndex application with these platforms implemented as data loaders. [BlogPost](https://airbyte.com/blog/introducing-airbyte-sources-within-llamaindex), [Tweet](https://twitter.com/AirbyteHQ/status/1696633858316243046?s=20).
- LlamaIndex integrates with DeepEval, a comprehensive library to evaluate LLM and RAG apps. Assess on four key metrics: Relevance, Factual Consistency, Answer Similarity, and Bias/Toxicity. [Docs](https://gpt-index.readthedocs.io/en/latest/community/integrations/deepeval.html), [Tweet](https://twitter.com/llama_index/status/1696674470566764846?s=20).
- LlamaIndex recommends evaluating LLM + RAG step-by-step, especially retrieval. Create synthetic retrieval datasets from text chunks using LLMs. This method not only evaluates retrieval but also fine-tunes embeddings. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/finetuning/embeddings/finetune_embedding.html#generate-corpus), [Tweet](https://twitter.com/jerryjliu0/status/1696675525442609166?s=20).
- LlamaIndex unveils a managed index abstraction simplifying RAG’s ingestion and storage processes with Vectara. [Docs](https://gpt-index.readthedocs.io/en/latest/community/integrations/managed_indices.html), [Tweet](https://twitter.com/llama_index/status/1696919525151899671?s=20).
- LlamaIndex has significantly enhanced its callback handling support, encompassing features like tracebacks, LLM token counts, templates, and detailed agent tool information. These advancements pave the way for smoother integrations with evaluation and observability applications. [Tweet](https://twitter.com/llama_index/status/1697407787154997754?s=20).
- LlamaIndex has integrated with AskMarvinAI, enabling automated metadata extraction from text corpora. Just annotate a Pydantic model and effortlessly log metadata from all associated text chunks. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/metadata_extraction/MarvinMetadataExtractorDemo.html), [Tweet](https://twitter.com/llama_index/status/1697632035186372745?s=20).
- LlamaIndex is integrated with RunGPT by JinaAI, an outstanding framework for one-click deployment of various open-source models such as Llama, Vicuna, Pythia, and more. Coupled with LlamaIndex’s innate chat/streaming capabilities, users can now deploy and utilize powerhouse models like Llama-7B seamlessly. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/llm/rungpt.html), [Tweet](https://twitter.com/llama_index/status/1698001332563837165?s=20).

## LlamaIndex.TS

- LITS has Full Azure OpenAI integration. [Tweet](https://twitter.com/yi_ding/status/1688564790007087104).
- LITS Enhanced Llama2 support, new default temperature (0.1), and GPT chat integration. [Tweet](https://twitter.com/llama_index/status/1689086106036547584?s=20).
- LITS helps to use `fromDocuments` without repeat checks; auto SHA256 comparison. [Tweet](https://twitter.com/llama_index/status/1691502243286228993?s=20).
- LITS now supports OpenAI v4, Anthropic 0.6, &amp; Replicate 0.16.1., CSV loader, Merged NodeWithEmbeddings &amp; BaseNode. [Tweet](https://twitter.com/llama_index/status/1691984600506257462?s=20).
- LITS now supports PapaCSVLoader for math. [Tweet](https://twitter.com/yi_ding/status/1691991221974217104?s=20).
- LITS is now integrated with LiteLLM. [Tweet](https://twitter.com/yi_ding/status/1692408213340340328).
- LITS now has additional session options for proxy server support, Default timeout reset to 60 seconds for OpenAI. [Tweet](https://twitter.com/llama_index/status/1693072438404276460?s=20).
- LITS now has Pinecone integration. [Tweet](https://twitter.com/yi_ding/status/1693275444848840745?s=20).
- LITS has Optimized ChatGPT prompts, fixed metadata rehydration issues, and OpenAI Node v4.1.0 with fine-tuned model support. [Tweet](https://twitter.com/llama_index/status/1694382741218005153?s=20).
- LITS has introduced enhanced text-splitting features, including a specialized tokenizer for Chinese, Japanese, and Korean, and refinements to the SentenceSplitter for handling decimal numbers. [Tweet](https://twitter.com/llama_index/status/1694719208217588070?s=20).
- LITS has a Markdown loader and metadata support in the response synthesizer. [Tweet](https://twitter.com/llama_index/status/1695156772783395255?s=20).
- LITS revamped usability: `ListIndex` is now `SummaryIndex` for clarity, and prompts have been made typed and customizable to enhance user control and experience. [Tweet](https://twitter.com/llama_index/status/1696626780277481491?s=20).
- LITS has Notion Reader. Now, users can effortlessly import their documents directly into their RAG or Data Agent application in LITS. [Tweet](https://twitter.com/llama_index/status/1698053712521146389?s=20).

# RAG Tips:

LlamaIndex shares [four tactics](https://gpt-index.readthedocs.io/en/latest/end_to_end_tutorials/dev_practices/production_rag.html) to boost your RAG pipeline:

1️⃣ Use summaries for retrieval, and a broader context for synthesis.

2️⃣ Use metadata for structured retrieval over large docs.

3️⃣ Deploy LLMs for dynamic retrieval based on tasks.

4️⃣ Fine-tune embeddings for better retrieval.

# Tutorials:

- [Jason's](https://twitter.com/jasonzhou1993) [tutorial](https://www.youtube.com/watch?v=qKtM2AlDTs8&amp;t=475s) on adding Image Responses to GPT knowledge retrieval apps.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial](https://betterprogramming.pub/building-production-ready-llm-apps-with-llamaindex-document-metadata-for-higher-accuracy-retrieval-a8ceca641fb5) on Building Production-Ready LLM Apps with LlamaIndex: Document Metadata for Higher Accuracy Retrieval
- Streamlit [tutorial](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/) on Building a chatbot with custom data sources, powered by LlamaIndex.
- [Wenqi Glantz](https://twitter.com/wenqi_glantz) [tutorial](https://betterprogramming.pub/building-production-ready-llm-apps-with-llamaindex-recursive-document-agents-for-dynamic-retrieval-1f4b25287918) on Building Production-Ready LLM Apps With LlamaIndex: Recursive Document Agents for Dynamic Retrieval.
- [Erika Cardenas](https://twitter.com/ecardenas300) covers the usage of [LlamaIndex in building an RAG app](https://twitter.com/ecardenas300/status/1695816617207153016?s=20).
- [Argilla](https://argilla.io/) blog post on [Fine-tuning and evaluating GPT-3.5 with human feedback for RAG using LlamaIndex](https://docs.argilla.io/en/latest/guides/llms/examples/fine-tuning-openai-rag-feedback.html#Evaluating-base-vs-fine-tuned-with-human-preference-data).
- [KDNuggests](https://www.kdnuggets.com/) blog post on [Build Your Own PandasAI with LlamaIndex](https://www.kdnuggets.com/build-your-own-pandasai-with-llamaindex).

From the LlamaIndex team:

- [Jerry Liu](https://twitter.com/jerryjliu0)’s [tutorial](https://medium.com/llamaindex-blog/easily-finetune-llama-2-for-your-text-to-sql-applications-ecd53640e10d) on fine-tuning Llama 2 for Text-to-SQL Applications.
- [Jerry Liu's](https://twitter.com/jerryjliu0) [tutorial](https://medium.com/llamaindex-blog/fine-tuning-embeddings-for-rag-with-synthetic-data-e534409a3971) on Fine-Tuning Embeddings for RAG with Synthetic Data.
- [Ravi Theja’s](https://twitter.com/ravithejads) [tutorial](https://medium.com/llamaindex-blog/llamaindex-harnessing-the-power-of-text2sql-and-rag-to-analyze-product-reviews-204feabdf25b) on combining Text2SQL and RAG with LlamaIndex to analyze product reviews.
- [Ravi Theja’s](https://twitter.com/ravithejads) tutorial on different [Indicies, Storage Context, and Service Context of LlamaIndex.](https://www.youtube.com/watch?v=gQXXeLHTxkI)
- [Ravi Theja’s](https://twitter.com/ravithejads) tutorial on [Custom Retrievers and Hybrid Search in LlamaIndex.](https://www.youtube.com/watch?v=hsEWohYtg0I)
- [Adam's](https://twitter.com/ajhofmann18) tutorial on [Introduction to Data Agents for Developers](https://www.youtube.com/watch?v=GkIEEdIErm8).
- [Ravi Theja’s](https://twitter.com/ravithejads) tutorial on creating [Automatic Knowledge Transfer (KT) Generation for Code Bases using LlamaIndex.](https://medium.com/llamaindex-blog/llamaindex-automatic-knowledge-transfer-kt-generation-for-code-bases-f3d91f21b7af)

# Webinars:

- [Webinar](https://www.youtube.com/watch?v=njzB6fm0U8g) with members from Docugami on Document Metadata and Local Models for Better, Faster Retrieval.
- [Webinar](https://www.youtube.com/watch?v=CwdAi1tts9c) with Shaun and Piaoyang on building Personalized AI Characters with RealChar.
- [Webinar](https://www.youtube.com/watch?v=Zj5RCweUHIk) with Bob (Weaviet), Max (sid.ai), and Tuana (HayStack) on making RAG Production-Ready.
- [Workshop](https://www.youtube.com/watch?v=hb8uT-VBEwQ) by Wey Gu on Building RAG with Knowledge Graphs.
- [Webinar](https://www.youtube.com/watch?v=mndiDJ5k26A) with Jo Bergum and Shishir Patil on fine-tuning and RAG.

# Events:

- [Jerry Liu](https://twitter.com/jerryjliu0) spoke about LlamaIndex at the [NYSE Floor Talk](https://www.youtube.com/watch?v=QtYL4Cm-pjE).
- [Ravi Theja](https://twitter.com/ravithejads) spoke about LlamaIndex at the [Fifth Elephant conference](https://twitter.com/ravithejads/status/1689491855543599104?s=20) in Bengaluru, India.
- [Ravi Theja](https://twitter.com/ravithejads) conducted a [workshop](https://twitter.com/fifthel/status/1692785973283656052?s=20) on LlamaIndex in Bengaluru, India.

# Demos And Papers:

- The paper titled [Performance of ChatGPT, human radiologists, and context-aware ChatGPT in identifying AO codes from radiology reports](https://www.nature.com/articles/s41598-023-41512-8) is an intriguing medical research. It leverages both LlamaIndex and ChatGPT to pinpoint AO codes within radiology reports, enhancing fracture classification. A fantastic fusion of tech and medicine!
- [SEC Insights AI](https://www.secinsights.ai/) does SEC document analysis using LlamaIndex is on Product Hunt as the 5th product of the day.
- [RentEarth](https://lablab.ai/event/autonomous-agents-hackathon/kbve/atlas): an agent to build your own startup with an amazing 3D interface and LlamaIndex.

In wrapping up this edition of our LlamaIndex Update series, we’re reminded of the power of collaboration and innovation. From new features to integrations and tutorials, our mission to revolutionize the AI realm marches forward. To every member of our community, thank you for your unwavering support and enthusiasm. Let’s continue to elevate the world of AI together!