---
title: "Text-to-SQL Agents: Smarter Queries With SkySQL | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/how-skysql-enables-smarter-text-to-sql-agents-with-llamaindex"
category: "llamaindex-core"
---

Content



- [ Challenge: Accurate and Reliable Answers from Operational Data  ](#challenge-accurate-and-reliable-answers-from-operational-data)
- [ Solution: Agentic RAG + Expert-in-the-Loop Context Refinement  ](#solution-agentic-rag-expert-in-the-loop-context-refinement)
- [ Why LlamaIndex?  ](#why-llamaindex)
- [ Results &amp; Key Metrics  ](#results-and-key-metrics)
- [ Conclusion  ](#conclusion)



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







 [SkySQL](http://skysql.com) is an AI-driven, serverless, fully managed Database-as-a-Service (DBaaS) designed for modern AI and SaaS workloads. With the no-code [**SkyAI Agent**](https://skysql.com/blog/in-database-semi-autonomous-ai-agents) builder, developers can build agentic apps relying on DB-level agents for reliable natural language conversations with their operational data. These AI agents semi-autonomously build context to generate highly accurate and efficient SQL queries and utilize an evaluation process to score the responses.



 SkySQL also provides built-in AI agents to improve developer and DBA productivity by assisting with SQL queries or stored procedure generation, database optimization, and performance analysis. This makes database management more efficient and accessible, as repetitive or complex tasks can be handled through conversational AI guidance.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  **Challenge: Accurate and Reliable Answers from Operational Data**



 Operational databases often have messy, evolving schemas—dozens or hundreds of tables, ambiguous column names, sparse foreign keys, and inconsistent relationships. This complexity trips up most text-to-SQL systems, especially those relying on LLMs without schema grounding.
SkySQL identified several key challenges in delivering high-accuracy answers from real-world operational data:


-  **Schema Complexity &amp; Ambiguity**: Cross-table joins and nested queries often resulted in errors or imprecise outputs from LLMs lacking contextual understanding.
  -  **Security &amp; Governance**: Ensuring strict control over what metadata and sample data reaches the LLM, while still providing enough context for meaningful query generation.
  -  **Evolving Context**: Operational schemas change frequently. Maintaining accurate, session-aware metadata and prompt context was critical to avoid stale or broken logic.
  -  **Human-in-the-Loop Needs**: Developers and DBAs needed a way to easily inspect, correct, and refine the agent’s understanding—especially for non-obvious relationships or naming conventions.
  -  **Latency vs. Cost Trade-offs**: Complex multi-turn interactions increase LLM token usage, creating a tension between query accuracy, latency, and cost.



###  **Solution: Agentic RAG + Expert-in-the-Loop Context Refinement**



 To address these challenges, SkySQL [uses LlamaIndex](https://skysql.com/blog/building-ai-agent-systems-with-llamaindex-and-skysql) as the core orchestration engine for its SkyAI agents—backed by a carefully designed feedback loop between auto-generated context and human-guided refinement.
Key architectural choices include:


-  **Agentic RAG Pipelines**: SkySQL automatically constructs a rich context window for each agent, including relevant table schemas, sample rows, and prompt instructions. LlamaIndex orchestrates retrieval and synthesis, enabling accurate SQL generation grounded in live data.
  -  **Expert-in-the-Loop Context Editing**: Developers and DBAs can easily view, tweak, or override agent context—adding missing relationships, renaming columns for clarity, or refining instructions. These corrections get persisted and reused, increasing agent reliability over time.
  -  **Built-in Evaluation Loop**: Each response is scored using an “LLM-as-Judge” model, enabling agents to assess the confidence of their outputs. Low-confidence answers trigger fallbacks, logging, or reruns using golden SQL patterns.
  -  **SQL Table Retriever Engine**: LlamaIndex’s structured query engine reliably transforms context and prompts into executable SQL, minimizing syntactic and logical errors.
  -  **In-Database Agent Execution**: SkySQL runs agents close to the data—in a secure, sandboxed environment—eliminating reliance on stale metadata or external vector stores. MariaDB Vector is used natively for fast semantic search with no added orchestration layers.



 Together, these capabilities enable SkySQL to offer highly accurate, governable, and production-ready text-to-SQL agents—without requiring deep ML expertise or extensive manual engineering.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/6c305a4f524720f4e59960a4375e31d41917b052-1750x966.png)

###  **Why LlamaIndex?**



 SkySQL evaluated several frameworks before adopting LlamaIndex. Key differentiators that drove their choice included:


-  **Superior Connectivity**: Extensive integration options with relational databases, structured data sources, and external document repositories, providing flexibility for current and future needs.
  -  **Advanced Agentic Capabilities**: LlamaIndex enabled more nuanced, goal-oriented agent behaviors, essential for generating reliable and contextually accurate SQL queries.
  -  **Rapid Implementation**: Pre-built connectors, rich ecosystem, documentation, community examples, and streamlined integration significantly reduced development time, accelerating SkySQL&#39;s go-to-market timeline.



###  **Results &amp; Key Metrics**



 SkySQL’s integration of LlamaIndex delivered substantial benefits, including:


-  **Significantly Improved SQL Accuracy**: The agentic RAG approach and structured query engine yielded precise and contextually correct SQL queries, dramatically reducing errors and ensuring reliable results.
  -  **Enhanced Developer Productivity**: Switching from ChromaDB to MariaDB vector storage was seamless, requiring minimal code changes due to LlamaIndex’s flexible design.
  -  **Flexible AI Model Integration**: SkySQL now easily integrates different LLMs, optimizing performance and providing the flexibility to use the best model for each use case.



###  **Conclusion**



 Through the adoption of LlamaIndex, [SkySQL](https://app.skysql.com/) has significantly transformed how databases can be queried and managed via natural language interfaces. By streamlining how natural language interfaces can be embedded in applications, SkySQL has made complex database AI agent solutions more accessible and scalable for developers. Try SkySQL yourself for [free](https://skysql.com/blog/the-fastest-vector-database-is-now-serverless-and-free) today!



 “LlamaIndex has been a game-changer for us, accelerating our AI agent development efforts, embedding reliable conversational interfaces directly within applications, and providing a flexible and scalable agentic framework.” **— Jags Ramnarayan, Chief Technology Officer and Co-Founder, SkySQL**