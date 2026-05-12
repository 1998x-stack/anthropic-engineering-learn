---
title: "LlamaIndex Update: New Features &amp; Benchmarks | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-update-08-01-2023-185514d9b897"
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

Welcome to the third installment of our LlamaIndex Update series. Your active participation continues to drive our open-source community forward. We appreciate every contribution whether you’re an experienced LlamaIndex contributor or a newcomer!



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



In our latest edition, we’ve prepared an assortment of updates for you. From advancements in Data Agents and LlamaIndex TS, benchmarking, and a host of inspiring events, webinars, blog posts, and demos, we’ve got plenty in store.

Without more ado, let’s dive into these updates.

# New Features:

- We heard you! LlamaIndex has completely revamped our documentation. The update includes new clearer documents on high-level concepts, detailed module guides, comprehensive tutorials, and an all-inclusive API reference. [Docs](https://gpt-index.readthedocs.io/en/latest/index.html), [Tweet](https://twitter.com/llama_index/status/1678558820552040448?s=20)
- LlamaIndex launched Data Agents, an innovative feature that combines AI agents with data. This launch introduces components like an agent reasoning loop and tool abstractions. Accompanied by an extensive upgrade to LlamaHub, the new feature offers more than 15 tool specs for easy integration. Data Agents enhance query capabilities and are designed to handle varied data applications. [Docs](https://gpt-index.readthedocs.io/en/latest/core_modules/agent_modules/agents/root.html), [Tweet](https://twitter.com/jerryjliu0/status/1679185930287222784?s=20), [Blog Post](https://medium.com/llamaindex-blog/data-agents-eed797d7972f)
- LlamaIndex launched LlamaIndex.TS, a lean Typescript package for building robust Retrieval Augmented Generation (RAG) systems. It simplifies tasks like document parsing and tackling context window limitations. LlamaIndex.TS is ideal for quickly building apps like using frameworks like Next.JS to chat over your data. [Docs](https://ts.llamaindex.ai/), [Tweet](https://twitter.com/llama_index/status/1683556970945736704?s=20), [Blogpost](https://medium.com/llamaindex-blog/introducing-llamaindex-ts-89f41a1f24ab)
- LlamaIndex teams up with Zapier Natural Language API (NLA), reducing the cognitive load on the data agent when handling APIs with multiple parameters. Zapier NLA translates complex third-party APIs into simpler interfaces using a single natural language parameter: instruction. This helps the data agent concentrate on tool selection and action orchestration. [Tweet](https://twitter.com/llama_index/status/1683880312173129728?s=20), [Blogpost](https://medium.com/llamaindex-blog/data-agents-zapier-nla-67146395ce1)
- LlamaIndex’s `ContextChatEngine`addresses the issue of conversational agents hallucinating information by ensuring retrieval of context with every user interaction. This feature, compatible with all ReAct and OpenAI Function agent types, prepends retrieved-context as a system message. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/chat_engine/chat_engine_context.html), [Tweet](https://twitter.com/llama_index/status/1685690590527430656?s=20)
- This month marked the launch of two new exciting LLMs. First off was Anthropic Claude 2.0. We launched with day 1 support of the new model. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/llm/anthropic.html), [Tweet](https://twitter.com/jerryjliu0/status/1678944607965708288?s=20). The other one was Llama2, and LlamaIndex now offers best-in-class integration with the Llama2 model on Replicate. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/llm/llama_2.html), [Tweet](https://twitter.com/llama_index/status/1681438906296991749?s=20)
- LlamaIndex is day one compatible with Chroma v0.4.0, enhancing support for in-memory, persisted, and self-hosted databases. This upgrade simplifies the use of Chroma within LlamaIndex, making database handling easier and more efficient. [Tweet](https://twitter.com/llama_index/status/1681167979176665088?s=20)
- LlamaIndex’s newly launched Data Agents can automatically interact with any API defined via an OpenAPI spec. It handles indexing/loading of large data from API specs and facilitates easy integration of the OpenAPI Tool, enhancing the ability to call web services. [Docs](https://llamahub.ai/l/tools-openapi), [Tweet](https://twitter.com/llama_index/status/1679522417558040577?s=20)
- LlamaIndex now utilizes the `rebel-large` model for high-speed relation extraction. Combined with CUDA, you can generate knowledge graphs from your text data. [Tweet](https://twitter.com/jerryjliu0/status/1685078740555169793?s=20)
- LlamaIndex introduced a code interpreter tool. This feature equips any LLM with the ability to analyze data and generate visualizations, expanding their capabilities similar to those of ChatGPT. [Tweet](https://twitter.com/jerryjliu0/status/1681304143930212357?s=20)
- LlamaIndex now integrates with Eduardo Reis’s Llama 2 functions API at [llama-api.com](http://llama-api.com). [Tweet](https://twitter.com/llama_index/status/1683231608038641664?s=20)
- LlamaIndex TS now supports integration with OpenAI Whisper. [Docs](https://www.npmjs.com/package/llamaindex-whisper), [Tweet](https://twitter.com/yi_ding/status/1683990169815502848?s=20)
- LlamaIndex now seamlessly integrates with [Kùzudb](https://twitter.com/kuzudb), allowing users to directly store extracted knowledge graphs/triples for advanced processing, querying, and visualization. [Docs](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/KuzuGraphDemo.html), [Tweet](https://twitter.com/kuzudb/status/1685010132277530624?s=20)
- LlamaIndex combines data agents with text-to-image models enhancing user prompts with relevant context from a knowledge base. This integration allows for more advanced multimodal reasoning by merging LLM RAG systems with text-to-image tools. [Docs](https://llamahub.ai/l/tools-text_to_image), [Tweet](https://twitter.com/jerryjliu0/status/1686026926442315778?s=20)

# Benchmarking:

- LlamaIndex now supports BEIR, an Information Retrieval benchmark. Users can define custom retrievers within LlamaIndex, apply the vector index, or implement reranking steps, and then easily evaluate their methods using any dataset from BEIR. [Tweet](https://twitter.com/llama_index/status/1680569394198372352?s=20)
- LlamaIndex’s Llama2 agents have shown promising performance in our agent task benchmark. Especially notable is their capability to appropriately use tools within a ReACT loop. However, the tasks’ difficulty varies, with both 13B and 70B models notably refraining from dialing a phone number, underlining the AI’s limitations. [Tweet](https://twitter.com/llama_index/status/1681724356764872704?s=20)
- LlamaIndex now has integration with the HotpotQA benchmark! This enables rigorous testing of LLM’s multi-hop reasoning capabilities by providing the full context to the models, helping you evaluate their performance more accurately. Perfect for stress-testing LLMs like ChatGPT, Claude 2, PaLM, and more. Plus, explore how context reordering can simplify tasks for your LLMs. [Tweet](https://twitter.com/jerryjliu0/status/1684589377614413825?s=20)
- LlamaIndex now supports over 20 vector databases, each with unique features and capabilities. To help understand their differences, we have compiled a comprehensive comparison table, guiding the choice of the optimal database for the use case. [Tweet](https://twitter.com/llama_index/status/1685326422175535104?s=20)

# Tutorials:

We were excited to see so many people making tutorials for LlamaIndex this month!

- [Adam Hofmann](https://medium.com/@adam.hofmann)’s blog post on [Building Better Tools for LLM Agents](https://medium.com/llamaindex-blog/building-better-tools-for-llm-agents-f8c5a6714f11).
- [Weav](https://weaviate.io/)iate’s [tutorial](https://github.com/weaviate/recipes/blob/main/integrations/llama2-demo/notebook.ipynb) on using the Llama2 model with LlamaIndex and Weaviet on external data.
- [Erika](https://twitter.com/ecardenas300)’s [tutorial](https://twitter.com/ecardenas300/status/1681669892741775361?s=20) on VectorStore Index, List Index, and Tree Index.
- [James Maslek](https://www.linkedin.com/in/james-maslek/)’s [tutorial](https://openbb.co/blog/breaking-barriers-with-openbb-and-llamaIndex) on Breaking Barriers with OpenBB and LlamaIndex: Simplifying data access to 100+ trusted sources.
- [Ayush Thakur](https://wandb.ai/ayush-thakur)’s tutorial on [Building Advanced Query Engine and Evaluation with LlamaIndex and W&amp;B](https://wandb.ai/ayush-thakur/llama-index-report/reports/Building-Advanced-Query-Engine-and-Evaluation-with-LlamaIndex-and-W-B--Vmlldzo0OTIzMjMy).
- [Trulens](https://www.trulens.org/)’s [tutorial](https://github.com/truera/trulens/blob/main/trulens_eval/examples/frameworks/llama_index/llamaindex-yelp-agent.ipynb) on using LlamaIndex Yelp agent to answer queries using Yelp data, and evaluate it for definitiveness and accuracy using custom feedback functions, compare its performance against a standalone LLM.
- [Airbyte](https://twitter.com/AirbyteHQ)’s [tutorial](https://airbyte.com/tutorials/airbyte-and-llamaindex-elt-and-chat-with-your-data-warehouse-without-writing-sql) on Chat with your data warehouse without writing SQL.
- [Anil Chandra Naidu](https://twitter.com/matchaman11)’s tutorial on [Retrievers](https://github.com/SamurAIGPT/LlamaIndex-course/blob/main/retrievers/Retrievers.ipynb) and [QueryEngines](https://github.com/SamurAIGPT/LlamaIndex-course/blob/main/query_engines/Query_Engines.ipynb).
- [Wenqi Glantz](https://medium.com/@wenqiglantz)’s tutorial on [Exploring Snowflake and Streamlit With LlamaIndex Text-to-SQL](https://betterprogramming.pub/exploring-snowflake-and-streamlit-with-llamaindex-text-to-sql-f66fec6e321b).

And from the LlamaIndex team:

- [Logan](https://twitter.com/LoganMarkewich)’s [tutorial](https://www.youtube.com/watch?v=2c64G-iDJKQ) on a comprehensive understanding of embedding models, their benchmarking, and their implementation in LlamaIndex, with a focus on OpenAI and Instructor embeddings, enabling semantic search through numerical text representations.
- [Logan](https://twitter.com/LoganMarkewich)’s [tutorial](https://www.youtube.com/watch?v=LQy8iHOJE2A) on the evaluation of query engines using LlamaIndex, learn to handle uncontrolled outputs and runtime costs while measuring performance with GPT-4.
- [Ravi Theja](https://twitter.com/ravithejads)’s [tutorial](https://www.youtube.com/watch?v=A3iqOJHBQhM) on Key Components to build QA Systems.

# Webinars:

- [Webinar](https://www.youtube.com/watch?v=s8ZNLqi9hzc) with Didier Lopes, CEO/Co-Founder at OpenBB on LLMs for Investment Research.
- [Webinar](https://llamaindex-and.wandb.events/) on Building &amp; Evaluating an Advanced Query Engine Over Your Data with Weights and Biases.
- [Webinar](https://www.youtube.com/watch?v=TdVbH7uJR_Y) with [Jason](https://twitter.com/jxnlco) Liu on From Prompt to Schema Engineering with Pydantic.

# Events:

- LlamaIndex and Arize [workshop](https://arize.com/resource/llm-search-retrieval-systems-with-arize-and-llamaindex-powering-llms-on-your-proprietary-data/) on LLM Search &amp; Retrieval Systems with Arize and LlamaIndex: Powering LLMs on Your Proprietary Data.
- LlamaIndex and TruLens [workshop](https://go.truera.com/event-llm-app-workshop-with-llamaindex-and-trulens?utm_campaign=event-2023-07-27-san-francisco&amp;utm_source=twitter&amp;utm_medium=social) on building an LLM App.
- [TPF](https://twitter.com/TheProductfolks) (The Product Folks) [workshop session](https://www.youtube.com/watch?v=2ul5XQXp-YI) on Building QA Systems With LlamaIndex by [Ravi Theja](https://twitter.com/ravithejads).
- [Ravi Theja](https://twitter.com/ravithejads) [talk](https://twitter.com/ravithejads/status/1684768609111801856?s=20) at the [Speciale VC](https://twitter.com/specialeinvest?lang=en) GenAI meetup in Chennai on Beyond the Basics: Leveraging LlamaIndex from Concept to Production.
- Data Agents session at TPF X Nexus VC [Buildathon](https://twitter.com/TheProductfolks/status/1685167361060737024?s=20) by [Ravi Theja](https://twitter.com/ravithejads).

# Demos:

- [Tali.AI](https://twitter.com/TryTaliAI) at the Augment hackathon dove into the future of support roles by developing an Autonomous Support Bot using LlamaIndex. [Tweet](https://twitter.com/TryTaliAI/status/1683960220702371845?s=20)
- [SuperAGI](https://superagi.com/) integrated with LlamaIndex which enables AI agents to process a wide variety of data from both structured and unstructured sources including Docx, PDF, CSV files, videos, and images. [Tweet](https://twitter.com/_superAGI/status/1679058876023603201?s=20)