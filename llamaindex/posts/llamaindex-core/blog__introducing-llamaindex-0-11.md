---
title: "LlamaIndex 0.11 Release Notes: New Features &amp; Changes | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llamaindex-0-11"
category: "llamaindex-core"
---

Content



- [ Workflows  ](#workflows)
- [ Instrumentation  ](#instrumentation)
- [ Property Graph Index  ](#property-graph-index)
- [ Reduced package size  ](#reduced-package-size)
- [ Other improvements and additions  ](#other-improvements-and-additions)
- [ Plus lots more!  ](#plus-lots-more)
- [ Breaking changes  ](#breaking-changes)
- [ Pydantic V2  ](#pydantic-v2)
- [ ServiceContext removed  ](#servicecontext-removed)
- [ LLMPredictor removed  ](#llmpredictor-removed)
- [ Enjoy!  ](#enjoy)



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







 LlamaIndex is delighted to announce that we have released the latest and greatest version of LlamaIndex for Python, version 0.11! There&#39;s been lots of updates since 0.10 was released, but here are a few highlights:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  Workflows



 We’ve introduced [Workflows](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex), an event-driven architecture for building complex gen AI applications. This replaces our previous experiment in this area, Query Pipelines, which should now be considered deprecated. We’re very excited about Workflows, so be sure to check out our [new tutorial](https://docs.llamaindex.ai/en/stable/understanding/workflows/) on how they work!



###  Instrumentation



 We significantly upped our observability game with our new [instrumentation](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/) feature, allowing better monitoring and debugging of LlamaIndex applications.



###  Property Graph Index



 Users have been delighted with our significantly improved support for property graphs with our [Property Graph Index](https://www.llamaindex.ai/blog/introducing-the-property-graph-index-a-powerful-new-way-to-build-knowledge-graphs-with-llms).



###  Reduced package size



 Everyone will be pleased to hear that we&#39;ve substantially reduced the size of the `llama-index-core`  package -- by 42%! We did this by removing OpenAI as a core dependency, adjusting how we depend on nltk, and making Pandas an optional dependency.



###  Other improvements and additions


-  Async streaming support for query engines and throughout the framework
  -  A Structured Planning Agent to improve our agentic capabilities
  -  Function Calling LLM to better handle tool-calling in LLMs
  -  Chat Summary Memory buffer to improve our ability to maintain context in conversations



###  Plus lots more!



 We&#39;ve added [hundreds of new features and bug fixes](https://github.com/run-llama/llama_index/blob/main/CHANGELOG.md) since 0.10, way too many to list!



##  Breaking changes



 In addition to all those goodies, 0.11 does bring some breaking changes:



###  Pydantic V2



 After a huge effort by [Andrei](https://x.com/_nerdai_) we are able to move fully to Pydantic V2. If you were previously needing to use `pydantic.v1`  imports to get around our lack of support for v2, you can now remove those.



 Pydantic V2 means LlamaIndex Pydantic types will work directly with FastAPI and other frameworks that use V2.



 This was a big change, so if you see any bugs please [report them](https://github.com/run-llama/llama_index/issues)!



###  ServiceContext removed



 Deprecated since 0.10, the `ServiceContext`  object is now completely removed in favor of using the `Settings`  object. If you import and use `ServiceContext`  in 0.11, you will get an error pointing you to our [migration docs](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/service_context_migration/).



###  LLMPredictor removed



 Also related to `Settings`  is the removal of the `LLMPredictor` . You should instead use the `LLM`  class, which is a drop-in replacement. Using `LLMPredictor`  in 0.11 will raise an error.



##  Enjoy!



 We hope you continue enjoying to use LlamaIndex, and we can&#39;t wait to see what you build!