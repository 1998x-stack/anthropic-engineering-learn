---
title: "LlamaIndex Newsletter 2024-08-13"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-08-13"
category: "llamaindex-core"
---

Content



- [ 🤩 The highlights:  ](#the-highlights)
- [ 🗺️ LlamaParse And LlamaParse:  ](#llamaparse-and-llamaparse)
- [ ✨ Framework:  ](#framework)
- [ ✍️ Community:  ](#community)
- [ 🎤 Webinar:  ](#webinar)



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







 Hi there, Llama Fans! 🦙







 Welcome to this week’s edition of the LlamaIndex newsletter! We’re excited to share our latest updates, including interesting features like data observability in LlamaParse, cookbooks on multimodal RAG, automated report generation, and the integration of constrained sampling in LlamaIndex. Plus, enjoy in-depth guides and tutorials from the community.







 If you haven&#39;t explored LlamaParse yet, make sure to [sign up](https://cloud.llamaindex.ai/) and [get in touch with us](https://www.llamaindex.ai/contact) to discuss your specific enterprise use case.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  🤩 **The highlights:**


-  **Data Observability in LlamaParse:** Introducing a feature for observing document chunking and analyzing query-time traces to refine RAG pipeline development. [Tweet](https://x.com/llama_index/status/1821332562310205918).
  -  **Multimodal RAG Pipeline Cookbooks:** Release of cookbooks for building multimodal RAG pipelines tailored to complex documents, using LlamaParse and advanced models. [Notebook1](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/insurance_rag.ipynb), [Notebook2](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/legal_rag.ipynb), [Notebook3](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/product_manual_rag.ipynb).
  -  **Automated Report Generation Guide:** A new guide for generating detailed reports combining text and images from complex data sources using Advanced RAG and LlamaParse. [Tweet](https://x.com/llama_index/status/1822297438058946623).
  -  **Constrained Sampling in LlamaIndex:** Integration of OpenAI&#39;s constrained sampling with `strict=True`  in LlamaIndex to ensure schema adherence in RAG and agentic flows, boosting precision and reliability. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/structured_outputs/structured_outputs.ipynb), [Tweet](https://x.com/llama_index/status/1820981141681401914).



##  **🗺️ LlamaParse And LlamaParse:**


-  We have introduced a new Data Observability Feature in LlamaParse to improve your RAG pipeline development with the ability to observe how documents are chunked and analyze query-time traces. This feature supports ad-hoc experimentation, allowing you to test QA pairs, identify retrieval issues, examine source document chunks, and refine chunk parameters for improved responses. [Tweet](https://x.com/llama_index/status/1821332562310205918).
  -  We have released a series of cookbooks on building multimodal RAG pipelines for complex documents, including insurance claims, legal documents, and product manuals, utilizing LlamaParse and advanced models like GPT-4o and Sonnet. [Notebook1](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/insurance_rag.ipynb), [Notebook2](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/legal_rag.ipynb), [Notebook3](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/product_manual_rag.ipynb).
  -  [Guide](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_report_generation.ipynb) to automatically generate reports combining text and images from complex data sources using Advanced RAG and LlamaParse, featuring structured outputs for detailed, multimodal documents. [Tweet](https://x.com/llama_index/status/1822297438058946623).
  -  [Thierry Santos](https://x.com/0xthierry) has developed a [CLI tool](https://github.com/0xthierry/llama-parse-cli) that simplifies converting any PDF into machine and LLM-readable markdown with a single terminal command, powered by LlamaParse.



##  **✨ Framework:**


-  We have integrated OpenAI&#39;s new constrained sampling feature into LlamaIndex with `strict=True`  for guaranteed adherence to schemas in RAG and agentic flows, enhancing application precision and reliability. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/structured_outputs/structured_outputs.ipynb), [Tweet](https://x.com/llama_index/status/1820981141681401914).
  -  We have implemented the Mixture Of Agents paper into a fully async, event-driven workflow, enabling each &#39;small LLM&#39; to independently process and respond to events in parallel for efficient batch processing. [LlamaPack](https://llamahub.ai/l/llama-packs/llama-index-packs-mixture-of-agents), [Tweet](https://x.com/llama_index/status/1821938263483150357).



##  **✍️ Community:**


-  [Laurie Voss’s](https://x.com/seldo) [video tutorial](https://www.youtube.com/watch?v=f3f_ctJyoWY) showcases rebuilding LlamaIndex&#39;s Sub-Question Query Engine using our workflows feature, highlighting step-by-step implementation, visualization, and the effectiveness of ReAct agents.
  -  [Laurie Voss’s](https://x.com/seldo) [tutorial](https://www.youtube.com/watch?v=R2sy6kI-uBk) on Workflows in LlamaIndex demonstrates how to create, manage, and debug complex agentic applications, covering everything from basic setup to advanced workflow visualization and error handling.
  -  [ArizeAI&#39;s](https://x.com/arizeai) [video tutorial](https://www.youtube.com/watch?v=XOV4RHMqZR4) demonstrates building complex, cyclic multi-agent systems using our new event-driven workflows, contrasting with traditional graph-based programming and showcasing the benefits for intricate agent communication and reasoning.
  -  [Michael Ryaboy’s](https://medium.com/@aimichael) [tutorial](https://medium.com/kx-systems/building-a-smarter-documentation-chatbot-a-practical-guide-using-firecrawl-and-kdb-ai-d3edbfbde277) on Building a Smarter Documentation Chatbot Using Firecrawl and [KDB.AI](http://kdb.ai/).
  -  [AnalyticsVidhya&#39;s](https://x.com/AnalyticsVidhya) [tutorial](https://www.analyticsvidhya.com/blog/2024/07/llama-agents-agents-as-a-service/) on Building Multi-agents as a Service offers an in-depth look at llama-agents, exploring its architecture and how to develop everything from simple to complex agent systems.
  -  [Pavan Kumar’s](https://x.com/pavan_mantha1) tutorial on Building Smarter Agents using LlamaIndex Agents and Qdrant’s Hybrid Search.



##  **🎤 Webinar:**


-  [Webinar](https://youtu.be/n90qZRlS1ek) with [Dedy Kredo](https://www.linkedin.com/in/dedy-kredo/) - Co-Founder of CodiumAI, on RAG with LlamaIndex for Large-Scale Generative Coding