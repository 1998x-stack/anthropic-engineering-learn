---
title: "LlamaIndex Update: Features, Integrations, Webinars | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-update-6-26-2023-ed30a9d45f84"
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







Greetings, LlamaIndex community!

We’re excited to introduce our new blog series, the LlamaIndex Update. Recognizing the fast pace of our open-source project, this series will serve as your continual guide, tracking the latest advancements in features, webinars, hackathons, and community events.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Our goal is simple: to keep you updated, engaged, and inspired. Whether you’re a long-time contributor or a new joiner, these updates will help you stay in sync with our progress.

So, let’s explore the recent happenings in our premier edition of the LlamaIndex Update.

## **Features And Integrations:**

- LLMs with Knowledge Graphs, supported by NebulaGraph. This new stack enables unique retrieval-augmented generation techniques. Our Knowledge Graph index introduces a GraphStore abstraction, complementing our existing data store types.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/KnowledgeGraphIndex_vs_VectorStoreIndex_vs_CustomIndex_combined.html), [Tweet](https://twitter.com/jerryjliu0/status/1667196231863656448)
- Better LLM app UX supports in-line citations of its sources, enhancing interpretability and traceability. Our new `CitationQueryEngine` enables these citations and ensures they correspond with retrieved documents. This feature marks a leap towards improving transparency in LlamaIndex applications.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/citation_query_engine.html), [Tweet](https://twitter.com/jerryjliu0/status/1667563694472175616?s=20)
- LlamaIndex integrates with Microsoft Guidance to ensure structured outputs from LLMs. It allows direct prompting of JSON keys and facilitates the conversion of Pydantic objects into the Guidance format, enhancing structured interactions. It can be used independently or with the SubQuestionQueryEngine.
[Docs](https://gpt-index.readthedocs.io/en/latest/how_to/integrations/guidance.html), [Tweet](https://twitter.com/llama_index/status/1668281830347530242)
- The GuidelineEvaluator module allows users to set text guidelines, thereby aiding in the evaluation of LLM-generated text responses. This paves the way toward automated error correction capabilities.
[Notebook](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/evaluation/RetryQuery.ipynb), [Tweet](https://twitter.com/llama_index/status/1667920234500751361?s=20)
- We now include a simple `OpenAIAgent`, offering an agent interface capable of sequential tool use and async callbacks. This integration was made possible with the help of the OpenAI function API and the LangChain abstractions.
[Tweet](https://twitter.com/llama_index/status/1668995630356725762)
- `OpenAIPydanticProgram` in LlamaIndex enhances structured output extraction. This standalone module allows any LLM input to be converted into a Pydantic object, providing a streamlined approach to data structuring.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/output_parsing/openai_pydantic_program.html), [Tweet](https://twitter.com/llama_index/status/1668995632873234435)
- We now incorporate the FLARE technique for a knowledge-augmented long-form generation. FLARE uses iterative retrieval to construct extended content, deciding to perform retrieval with each sentence. Unlike conventional vector index methods, our FLARE implementation builds a template iteratively, filling gaps with retrieval for more pertinent responses. Please note, this is a beta feature and works best with GPT-4.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/flare_query_engine.html), [Tweet](https://twitter.com/jerryjliu0/status/1669719509987643392?s=20)
- We now employ the Maximal Marginal Relevance (MMR) algorithm to enhance diversity and minimize redundancy in retrieved results. This technique measures the similarity between a candidate document and the query while minimizing similarity with previous documents, depending on a user-specified threshold. Please note that careful calibration is necessary to ensure that increased diversity doesn’t introduce irrelevant context. The threshold value is key to balancing diversity and relevance.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/SimpleIndexDemoMMR.html), [Tweet](https://twitter.com/llama_index/status/1669801174109925377?s=20)
- We now support recursive Pydantic objects for complex schema extraction. This enhancement, inspired by parsing directory trees, employs a mix of recursive (Node) and non-recursive (DirectoryTree) Pydantic models, facilitating more sophisticated agent-tool interactions.
[Tweet](https://twitter.com/jerryjliu0/status/1670823521801621505?s=20)
- We have developed agents that can perform advanced query planning over data using the Function API and Pydantic. These agents input a full Pydantic graph in the function signature of a query plan tool, which is then executed. This system can work with any tool and has the potential to construct complex query plans. However, it has limitations like difficulty in producing deep nesting and the possibility of outputting invalid responses.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/agent/openai_agent_query_plan.html), [Tweet](https://twitter.com/jerryjliu0/status/1671183584072470529?s=20)
- `OpenAIAgent` is capable of advanced data retrieval and analysis, such as auto-vector database retrieval and joint text-to-SQL and semantic search. We have also built a query plan tool interface that allows the agent to generate structured/nested query plans, which can then be executed against any set of tools, enabling advanced reasoning and analysis.
Docs:[ OpenAI Agent + Query Engine](https://gpt-index.readthedocs.io/en/latest/examples/agent/openai_agent_query_cookbook.html), [Retrieval Augmented OpenAI Agent](https://gpt-index.readthedocs.io/en/latest/examples/agent/openai_agent_retrieval.html), [OpenAI Agent Query Planning](https://gpt-index.readthedocs.io/en/latest/examples/agent/openai_agent_query_plan.html).
[Tweet](https://twitter.com/llama_index/status/1671185213538578433?s=20)
- The new multi-router feature allows for QA over complex data collections, where answers may be spread across multiple sources. It uses a “MultiSelector” object to select relevant choices given a query. The router can pick up to a maximum number of choices. It can use either a raw LLM completion API or the OpenAI Function API. If the Function API is used, schema validity can be enforced. A simple usage example involves a RouterQueryEngine, where the PydanticMultiSelector selects the relevant vector and keyword index to synthesize an answer.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/RouterQueryEngine.html#define-router-query-engine), [Tweet](https://twitter.com/jerryjliu0/status/1671536412498477057?s=20)
- We have made a significant upgrade to our token tracking feature. Users can now easily track prompt, completion, and embedding tokens through the platform’s callback handler. The upgrade aims to make token counting more efficient and user-friendly.
[Docs](https://gpt-index.readthedocs.io/en/latest/how_to/callbacks/token_counting_migration.html), [Tweet](https://twitter.com/llama_index/status/1671893230412247042?s=20)
- We released a guide that demonstrates how to build a custom retriever that combines vector similarity search with knowledge graphs in LLM RAG systems. It involves constructing a vector index and a knowledge graph index and combining the results from both during query time. This method can improve results by providing additional context for entities. However, it may lead to a slight increase in latency.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/KnowledgeGraphIndex_vs_VectorStoreIndex_vs_CustomIndex_combined.html), [Tweet](https://twitter.com/jerryjliu0/status/1671895098270031872?s=20)
- In an LLM workflow, managing large amounts of data, including PDFs, agent Tools, SQL table schemas, etc., requires efficient indexing. To handle this, we introduce our Object Index, a wrapper over our existing index data structures. This allows any object to be converted into an indexable text format, providing a unified interface that enhances the functionality of our indices over various data types.
[Tweet](https://twitter.com/jerryjliu0/status/1672263302628646912?s=20)
- The OpenBB Finance Terminal is a great platform for investment research and is completely open-source. It now includes a feature called AskOBB, powered by Llama Index, which allows users to easily access any financial data through natural language.
[Tweet](https://twitter.com/jerryjliu0/status/1672637698136489989?s=20)
- The TruLens team has introduced tracing for LlamaIndex-based LLM applications in its latest release. This new feature allows developers to evaluate and track their experiments more efficiently. It automatically evaluates various components of the application stack, including app inputs and outputs, LLM calls, retrieved-context chunks from an index, and latency. This is part of an ongoing collaboration between the LlamaIndex and TruLens teams to improve the development, evaluation, and iteration of LLM apps.
[Notebook](https://github.com/truera/trulens/blob/releases/rc-trulens-eval-0.3.0/trulens_eval/examples/vector-dbs/llama_index/quickstart.ipynb), [Blogpost](https://medium.com/llamaindex-blog/build-and-evaluate-llm-apps-with-llamaindex-and-trulens-6749e030d83c)
- Prem App has successfully integrated with Llama Index, enhancing privacy in AI development. This union allows developers to connect custom data sources to large language models easily, simplifying data ingestion, indexing, and querying. To use this integration, download the Prem App and connect your data sources through the Llama Index platform. This allows for efficient data management and boosts AI application development, providing developers with more control and flexibility.
[Notebook](https://github.com/premAI-io/prem-daemon/blob/main/resources/notebooks/llama_index.ipynb), [Blogpost](https://medium.com/llamaindex-blog/llama-index-prem-ai-join-forces-51702fecedec)
- We now enable the extraction of tabular data frames from unstructured text. This feature, powered by the OpenAI Function API and Pydantic models, simplifies text-to-SQL or text-to-DF conversions within structured data workflows. Note that effective use may require significant prompt optimization.
[Docs](https://gpt-index.readthedocs.io/en/latest/examples/output_parsing/df_output_parser.html), [Tweet](https://twitter.com/jerryjliu0/status/1673004155227750401?s=20)

**Tutorials:**

- [James Brigg’s tutorial](https://www.youtube.com/watch?v=WKvAWub8VCU&amp;t=2s) on using LlamaIndex with Pinecone.
- [Jerry Liu's tutorial](https://weaviate.io/blog/llamaindex-and-weaviate) on using LlamaIndex with Weaviate.
- [Sophia Yang tutorial](https://www.youtube.com/watch?v=cNMYeW2mpBs) on LlamaIndex overview, Use cases, and integration with LangChain.
- Anil Chandra Naidu is building a [course](https://github.com/SamurAIGPT/LlamaIndex-course) on LlamaIndex. The course presently covers topics such as introduction, fundamentals, and data connectors.
- [OpenAI cookbook by Simon](https://github.com/openai/openai-cookbook/blob/main/examples/third_party_examples/financial_document_analysis_with_llamaindex.ipynb) on how to perform financial analysis with LlamaIndex.

## **Webinars And Podcasts:**

- [Webinar](https://www.youtube.com/watch?v=6ot9io-brzI&amp;t=2s) on Demonstrate-Search-Predict (DSP) with Omar Khattab.
- [Webinar](https://www.youtube.com/watch?v=7aIzxFyJP-A&amp;t=22s) on Practical challenges of building a Legal Chatbot over your PDFs with Sam Yu
- [MaML podcast](https://podcasters.spotify.com/pod/show/maml-podcast/episodes/Jerry-Liu---Building-LlamaIndex--the-Data-Framework-for-LLMs-e25u3ga) with Jerry Liu.

## **Hackathons:**

The LlamaIndex team has presented at the UC Berkeley Hackathon and the Stellaris VP Hackathon in India. The community has warmly welcomed LlamaIndex, and teams at these hackathons have developed intriguing use cases — Customer support during emergency cases, Understanding Legal documents.

## **Events:**

- Jerry Liu spoke on Building and troubleshooting an AI Search &amp; Retrieval System at Arize — LlamaIndex event.
- Ravi Theja presented about LlamaIndex and its applications at Together in India.

That’s all for this edition of the LlamaIndex Update. We hope you found this information useful and are as excited as we are about the progress we’re making. We’re grateful for the continued support and contributions from our community. Remember, your feedback and suggestions are invaluable to us, so don’t hesitate to reach out.

Stay tuned for our next update, where we’ll share more exciting developments from the LlamaIndex project. Until then, happy indexing!