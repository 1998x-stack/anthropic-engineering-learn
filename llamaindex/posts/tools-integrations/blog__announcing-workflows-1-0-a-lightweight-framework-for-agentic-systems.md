---
title: "Workflows 1.0: Lightweight Agentic Framework Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems"
category: "tools-integrations"
---

Content



- [ What can you build with Workflows  ](#what-can-you-build-with-workflows)
- [ A new home for Workflows  ](#a-new-home-for-workflows)
- [ What’s New in version 1.0  ](#whats-new-in-version-10)



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







 We’re excited to introduce the official release of LlamaIndex Workflows 1.0, a lightweight framework for building complex, multi-step agentic AI applications in Python and Typescript.



 We first [introduced Workflows](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex) showcasing how to build reusable, event-driven applications powered by `llama_index` . Since then, we’ve seen a growing need for developers to define complex AI application logic for agents without losing control of the execution flow.



 This first stable release of LlamaIndex Workflows introduces (and improves on) our approach to creating event-driven custom agentic workflows. This allows developers to make use of LLMs while still maintaining a high-level of control over the overall behaviour and architecture of the application.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  **What can you build with Workflows**



 Workflows shine when you need to orchestrate complex, multi-step processes that involve AI models, APIs, and decision-making. Here are some examples of what you can build:


-  **AI Agents** - Create intelligent systems that can reason, make decisions, and take actions across multiple steps
  -  **Document Processing Pipelines** - Build systems that ingest, analyze, summarize, and route documents through various processing stages
  -  **Multimodal AI Applications** - Coordinate between different AI models (LLMs, vision models, etc.) and data formats to solve complex tasks
  -  **Research Assistants** - Develop workflows that can search, analyze, synthesize information, and provide comprehensive answers
  -  **Role-based Multi Agent Systems** - Build agentic systems that can coordinate across multiple agents by handing over control to each other when needed.
  -  **Content Generation Systems** - Create pipelines that generate, review, edit, and publish content with human-in-the-loop approval
  -  **Customer Support Automation** - Build intelligent routing systems that can understand, categorize, and respond to customer inquiries



 The async-first, event-driven architecture makes it easy to build applications that route between different capabilities, implement parallel processing patterns, loop over complex sequences, and maintain state across multiple steps. All the features you need to make your AI applications production-ready.



##  A new home for Workflows



 Previously part of `llama_index`  and `LlamaIndexTS` , Workflows have eventually grown into their own dedicated package:


-  `pip install llama-index-workflows`  for the Python version
  -  `npm i @llamaindex/workflow-core`  for the Typescript version



 The code is also hosted in a dedicated git repository:


-  [https://github.com/run-llama/workflows-py](https://github.com/run-llama/workflows-py)
  -  [https://github.com/run-llama/workflows-ts](https://github.com/run-llama/workflows-ts)



 Both `llama_index`  and `LlamaIndexTS`  will continue offering Workflows functionalities by re-exporting the new libraries through the old import paths, so your existing code will keep working and benefit from the new features that will be shipped in the standalone package.



 This separation reflects what Workflows has become: a general-purpose orchestration framework for LLM-powered systems with these goals in mind:


-  Highlight Workflows independence from `llama_index` : You can use Workflows to write the orchestration logic of any Python and Typescript application
  -  Encourage contributions and experimentation: Workflows can easily be adopted in environments where `llama_index`  wasn&#39;t previously used
  -  Support a wider range of use cases, from agentic systems to task orchestration, with a limited set of dependencies



##  What’s New in version 1.0



 The v1.0 release marks the first **standalone version** of Workflows, with its own repository, package, and development path. While the underlying architecture hasn’t changed significantly, this release makes it easier to:


-  Use Workflows outside of the LlamaIndex ecosystem
  -  Contribute to the project in a focused, modular codebase



 Along with several bugfixes, the 1.0 release also introduces:


-  **Typed Workflow State** - Both Python and Typescript support typed state, improving type safety for developers
  -  **Resource Injection** - Python workflows support dynamic resource injection. Dynamically inject database clients and more.
  -  **Observability** - Python workflows support optional observability integrations. By installing `llama-index-instrumentation` , you can instrument your workflows with OpenTelemetry, Arize Phoenix, and more!



 While we transition to dedicated and updated doc material, the old documentation is still available via the LlamaIndex site and remains valid for this version:


-  [https://docs.llamaindex.ai/en/stable/module_guides/workflow/](https://docs.llamaindex.ai/en/stable/module_guides/workflow/)
  -  [https://ts.llamaindex.ai/docs/workflows](https://ts.llamaindex.ai/docs/workflows)