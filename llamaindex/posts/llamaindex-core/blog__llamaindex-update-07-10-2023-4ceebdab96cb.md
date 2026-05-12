---
title: "LlamaIndex Update: New Features, Tutorials &amp; Events | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-update-07-10-2023-4ceebdab96cb"
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







Greetings once again, LlamaIndex community!

Welcome back to our second installment in the LlamaIndex Update series. In our ongoing commitment to keep you informed and engaged with our rapidly evolving open-source project, this blog post brings you more exciting updates on features, webinars, hackathons, and community events.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Building on the foundation of our inaugural post, we will continue to strive to keep both our long-standing contributors and fresh faces synced with our progress. We aim to not just inform but also inspire you to partake in our collective journey towards growth and innovation.

Without further delay, let’s delve into the latest happenings in this edition of the LlamaIndex Update.

## Features And Integrations:

- LlamaIndex’s partnership with Anyscale uses the Ray platform to boost performance and deployment. It accelerates LlamaIndex’s operations by a factor of ten and streamlines deployment to production servers. The core Ray Distributed Toolkit aids in efficient task parallelization, while Ray Serve ensures easy deployment of query engines to production.
[Blogpost](https://www.anyscale.com/blog/build-and-scale-a-powerful-query-engine-with-llamaindex-ray), [Tweet](https://twitter.com/llama_index/status/1673451316398653440?s=20)
- LlamaIndex enhanced metadata representation in documents. The `extra_info` and `node_info` fields are now replaced with a `metadata `dictionary. This facilitates precise control over data and allows users to exclude metadata keys during embedding or LLM prediction. This boosts LLM and retrieval performance and offers customizable metadata injection, formatting, and template creation.
[Docs](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_documents.html), [Tweet](https://twitter.com/llama_index/status/1673721486757199872?s=20)
- LlamaIndex supports both Text Completion API, involving output parsing and input prompt modification, and Structured API, requiring input function signatures and output conversion. Despite Structured API being easier to use, its limited availability keeps Text Completion API relevant. Both are supported by LlamaIndex’s `PydanticProgram`.
[Docs](https://gpt-index.readthedocs.io/en/latest/how_to/structured_outputs/root.html), [Tweet](https://twitter.com/llama_index/status/1674075533548871681?s=20)
- LlamaIndex now collaborates with Chainlit.io, facilitating swift construction of advanced chat UIs for any LLM app. This integration, beyond providing a basic chat interface, also logs intermediate results and sources.
[Blogpost](https://docs.chainlit.io/integrations/llama-index), [Tweet](https://twitter.com/jerryjliu0/status/1674107773758611456?s=20)
- LlamaIndex now incorporates the DePlot model for interpreting charts and plots in QA/chatbot applications. Primarily effective for simple charts, such as bar charts and time series, DePlot converts these visuals into text format for easy embedding, indexing, and usage in downstream applications. This functionality is now accessible via the LlamaHub data loader, expanding LlamaIndex’s capabilities for diverse applications.
[Docs](https://llama-hub-ui.vercel.app/l/file-image_deplot), [Tweet](https://twitter.com/jerryjliu0/status/1674442367087316992?s=20)
- LlamaIndex now incorporates the Github Issues reader, which allows for comprehensive loading and querying of issues from any GitHub repository. Additionally, the Sitemap Loader reader enables users to read all webpages from a specified sitemap.
[Tweet](https://twitter.com/llama_index/status/1674443061118791680?s=20)
- LlamaIndex introduces the `ContextRetrieverOpenAIAgent` feature, which enhances tool picking by incorporating more context from user messages. It performs a retrieval step before the LLM call, ensuring increased reliability and better mapping of queries to the right tools, especially in the presence of domain-specific terms. Unlike a “retrieval tool”, this feature guarantees retrieval before any action is taken.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/agent/openai_agent_context_retrieval.html), [Tweet](https://twitter.com/jerryjliu0/status/1674807074918928385?s=20)
- LlamaIndex now features code-based extraction for efficient data extraction from arbitrary text. This feature includes a “Fit” step to generate functions based on training data, and an “Inference” step to run these functions on new data. It offers two versions: DFEvaporateProgram for extracting one value per field from a text, and MultiValueEvaporateProgram for extracting multiple values per field. This feature can be used to extract structured data from raw HTML sources and also offers the ability to identify salient fields in a text given a topic.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/output_parsing/evaporate_program.html), [Tweet](https://twitter.com/jerryjliu0/status/1675901084840390656?s=20)
- LlamaIndex has significantly improved its text-to-SQL capabilities, offering a “Default” SQL query engine and an SQL query engine with an object index for handling large table schemas. These upgrades simplify the process, requiring only a SQL database for the default engine and enabling indexing of large table schemas with the ObjectIndex. Additionally, LlamaIndex now also integrates with [duckdb](http://twitter.com/duckdb), further enhancing the SQL querying process.
[Docs_SQL](https://gpt-index.readthedocs.io/en/latest/guides/tutorials/sql_guide.html), [Docs_duckdb](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/struct_indices/duckdb_sql_query.html), [Tweet](https://twitter.com/llama_index/status/1676002583381692421?s=20)
- LlamaIndex 0.7.0 enhances modularity for LLM app development. It includes native LLM abstractions for platforms like OpenAI and Hugging Face, a standalone Response Synthesis module, and improved Document Metadata Management. These abstractions can be used independently or integrated into indices/query engines. The Response Synthesis module abstracts away context window limitations, while the Document Metadata Management feature allows deep customization of metadata, potentially boosting retrieval performance.
[Blogpost](https://medium.com/llamaindex-blog/llamaindex-0-7-0-better-enabling-bottoms-up-llm-application-development-959db8f75024), [Tweet](https://twitter.com/llama_index/status/1676255154662969345?s=20)
- LlamaIndex introduces Recursive Retrieval, a concept that utilizes the hierarchical nature of knowledge. A Node in LlamaIndex can contain references to other retrievers or query engines. This process starts with a retriever and recursively explores links to others. For instance, structured tables from a PDF can be extracted, each represented as a data frame. These tables can be referenced by `IndexNode` objects embedded with other Nodes. During a query, if an IndexNode is among the top-k nodes, it triggers another retriever or query engine, allowing sophisticated querying overall data.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/pdf_tables/recursive_retriever.html), [Tweet](https://twitter.com/jerryjliu0/status/1676606169002004481?s=20)
- LlamaIndex introduces OpenAI agent streaming for efficient function calling and enhances user experience by providing progress bars during index creation for a real-time understanding of the process duration.
[Tweet](https://twitter.com/llama_index/status/1676742253669408768?s=20)
- LlamaIndex introduces personalized data interaction through system prompts, callback events for SubQuestionQueryEngine, and a streamlined process for Azure OpenAI integration.
[Docs_AOI](https://gpt-index.readthedocs.io/en/latest/examples/customization/llms/AzureOpenAI.html), [Notebook_personality](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/chat_engine/chat_engine_personality.ipynb), [Tweet](https://twitter.com/llama_index/status/1676981157513265153?s=20)
- LlamaIndex leverages LLM’s to automatically extract metadata, significantly enhancing the relevance and precision of information retrieval. This is achieved through five key MetadataExtractor modules (SummaryExtractor, QuestionsAnsweredExtractor, TitleExtractor, MetadataFeatureExtractor) that augment text with rich, context-specific details.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/metadata_extraction/MetadataExtractionSEC.html), [Tweet](https://twitter.com/jerryjliu0/status/1677706208017518593?s=20)

## **Tutorials:**

- [Anyscale tutorial](https://www.youtube.com/watch?v=Vd_8lS1iDBg) on “How to Build an LLM Query Engine in 10 Minutes using LlamaIndex.”
- [Erika Cardenas tutorial](https://www.youtube.com/watch?v=Bu9skgCrJY8) on how to load data into Weaviate and how to connect LlamaIndex to a Weaviate instance using LlamaIndex.
- [Wenqi Glantz tutorial](https://betterprogramming.pub/refreshing-private-data-sources-with-llamaindex-document-management-1d1f1529f5eb) on Refreshing Private Data Sources with LlamaIndex Document Management.
- [Michael Hunger tutorial](https://medium.com/llamaindex-blog/enriching-llamaindex-models-from-graphql-and-graph-databases-bcaecec262d7) on** **Load in data from [neo4j](https://twitter.com/neo4j), [NebulaGraph](https://twitter.com/NebulaGraph), and index/query with LlamaIndex using GraphDB Cypher and GraphQL data loaders.
- [Pradip Nichite video tutorial](https://www.youtube.com/watch?v=XGBQ_f-Yy48) and [blogpost](https://blog.futuresmart.ai/mastering-llamaindex-create-save-load-indexes-customize-llms-prompts-embeddings) on Mastering LlamaIndex: Create, Save &amp; Load Indexes, Customize LLMs, Prompts &amp; Embeddings.

## Webinars And Podcasts:

- [Webinar](https://www.youtube.com/watch?v=bPoNCkjDmco) on Graph Databases, Knowledge Graphs, and RAG with Wey (NebulaGraph).
- [Webinar](https://www.youtube.com/watch?v=gbyfXRxU0Gw) with Albus — a comprehensive Slackbot for enterprise search, [xpress.ai](http://Xpress.ai) — a low-code solution for building LLM workflows + agents and [ImmigrantFirst.ai](https://t.co/QAJyGqZPcB) — assistant to help immigrants complete their EB-1A/O1 apps more efficiently.
- [Data Exchange Podcast](https://www.youtube.com/watch?v=NAoqOJrE8rQ&amp;list=PLnTmH22EvTFTtWJRPTNzosDIDblnSg0PD&amp;t=1s) with Ben Lorica on LlamaIndex

## Events:

Ravi Theja gave talks on “LlamaIndex: Basics To Production” at Accel Partners and Together VC Fund in India.