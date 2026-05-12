---
title: "LlamaIndex Newsletter 2023–02–13"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-02-13-26fa79601ba5"
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







Greetings, LlamaIndex Adventurers 🦙,

Welcome to an exhilarating week of discoveries at LlamaIndex! Our community’s lively input and the abundance of learning tools await to supercharge your journey through LlamaIndex.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Before we dive into the updates, we have two major announcements:

- **LlamaIndex v0.10**: Our latest open-source release marks a monumental step towards production readiness. With a new core package and hundreds of integrations and LlamaPacks now available as separate PyPi packages, we’ve massively improved organization and version tracking. Major updates include the refactoring of LlamaHub into a central hub for all integrations and the deprecation of ServiceContext for an enhanced development experience. [Blog](/llamaindex-v0-10-838e735948f8), [Migration Guide](https://www.notion.so/6ede431dcb8841b09ea171e7f133bd77?pvs=21).
- Introducing Short Courses on Advanced RAG Development: Master complex RAG systems with our series, covering everything from unstructured data to agent integration. Learn through LlamaIndex Query Pipelines, from basic text-to-SQL to advanced query techniques, and build scalable RAG applications with hands-on guidance. [Video1](https://www.youtube.com/watch?v=CeDS1yvw9E4), [Video2](https://www.youtube.com/watch?v=L1o1VPVfbb0).

Your creativity fuels our inspiration! We’re excited to see any projects, articles, or videos you’re passionate about. Share your incredible creations with us at [news@llamaindex.ai](mailto:news@llamaindex.ai). Haven’t joined our newsletter yet? Make sure to subscribe on our [website](https://www.llamaindex.ai/) for the latest LlamaIndex updates delivered directly to your inbox.

🤩 **The highlights:**

- **Self-RAG**: Introducing Self-RAG, now part of LlamaIndex as a LlamaPack. Boosts LLM training and RAG workflows with dynamic capabilities. [Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/self_rag/self_rag.ipynb), [Tweet](https://x.com/llama_index/status/1754909796594221187?s=20).
- **LlamaIndex + FlowiseAI Integration**: Seamlessly merge LlamaIndex with FlowiseAI for effortless, no-code RAG app development. [Docs](https://docs.flowiseai.com/integrations/llamaindex), [Tweet](https://x.com/llama_index/status/1755641567174684953?s=20).
- **RAG Guide with MistralAI**: MistralAI’s new doc includes a RAG guide with LlamaIndex. Utilize Mistral-medium for enhanced RAG functions. [Docs](https://docs.mistral.ai/guides/basic-RAG/#rag-with-llamaindex).

**✨ Feature Releases and Enhancements:**

- We have introduced a seamless integration between LlamaIndex and FlowiseAI, enabling easy, no-code development of advanced RAG applications with a drag-and-drop interface for quick chatbot or agent integration. [Docs](https://docs.flowiseai.com/integrations/llamaindex), [Tweet](https://x.com/llama_index/status/1755641567174684953?s=20).
- We have introduced Self-RAG, a dynamic retrieval tool by [Akari Asai](https://twitter.com/AkariAsai)’s team, now available as a LlamaPack for easy integration, enhancing LLM training and RAG workflows with dynamic, iterative capabilities. [Notebook](https://github.com/run-llama/llama-hub/blob/main/llama_hub/llama_packs/self_rag/self_rag.ipynb), [Tweet](https://x.com/llama_index/status/1754909796594221187?s=20).
- We have introduced the RAG CLI tool that allows you to search any file on your filesystem using on-device language model embeddings, featuring the power of Mistral-7B and bge-m3 for an advanced, customizable experience. [Docs](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html), [Tweet](https://x.com/llama_index/status/1754678983881621595?s=20).
- We have launched full-stack agent servers with a single CLI command using `**create-llama**` from LlamaIndex, offering instant access to 50+ tools for any agent project. [Tweet](https://x.com/jerryjliu0/status/1755289964517167184?s=20).
- We have introduced agents in LlamaIndex.TS, enabling advanced AI software development in TypeScript with features like function calling and multi-document handling. [Blog](/how-to-build-llm-agents-in-typescript-with-llamaindex-ts-a88ed364a7aa), [Docs](https://ts.llamaindex.ai/modules/agent/), [Tweet](https://x.com/llama_index/status/1755688725106114818?s=20).
- DeepEval is integrated with LlamaIndex, significantly enhancing RAG evaluation capabilities and introducing unit testing for LlamaIndex apps in CI/CD environments. [Docs](https://docs.confident-ai.com/docs/integrations-llamaindex).

**🗺️ Guides:**

- [Guide](https://docs.mistral.ai/guides/basic-RAG/#rag-with-llamaindex) to RAG with LlamaIndex in MistralAI’s new documentation with Mistral-medium and Mistral embedding models.
- [Guide](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent.html#step-wise-queries) to Building Agentic RAG to incorporate user feedback in real-time enhancing complex searches with a human-in-the-loop approach.
- [Guide](https://huggingface.co/blog/tgi-messages-api) to Integrating Huggingface’s New Messages API with OpenAI compatibility, simplifying the integration process for Inference Endpoints and Text Generation Inference.

**✍️ Tutorials:**

- [Plaban Nayak](https://nayakpplaban.medium.com/) [tutorial](https://www.notion.so/LlamaIndex-Newsletter-2024-02-06-86c1d1db060249f2ab8032357f3df323?pvs=21) on Setting up Query Pipeline For Advanced RAG Workflow using LlamaIndex.
- [Krish Naik](https://www.youtube.com/@krishnaik06) [tutorial](https://www.youtube.com/watch?v=f-AXdiCyiT8) on Step-by-Step Guide to Building a RAG LLM App with Llama2 and LlamaIndex.
- HelixML [tutorial](https://helixml.substack.com/p/how-we-got-fine-tuning-mistral-7b) to Knowledge Memorization by fine-tuning Mistral-7B for enhanced knowledge memorization, offering a new way to reason across contexts without RAG’s limitations.
- [Wenqi Glantz](https://medium.com/@wenqiglantz) [tutorial](https://towardsdatascience.com/nemo-guardrails-the-ultimate-open-source-llm-security-toolkit-0a34648713ef) on NeMo Guardrails, the Ultimate Open-Source LLM Security Toolkit.

🎥 **Webinar:**

- [Webinar](https://www.youtube.com/watch?v=96mRmQD4RnE) of Laurie with Ankit Khare(Rockset) delves into the essentials of RAG — its purpose, methodology, how LlamaIndex facilitates it, and exciting developments for 2024.
- [Webinar](https://www.youtube.com/watch?v=Ya1DhVW9gTo) with Zilong Wang, and Tianyang Liu on Advanced Tabular Data Understanding with LLMs.

**🏢 Calling all enterprises:**

Are you building with LlamaIndex? We are working hard to make LlamaIndex, even more, Enterprise-ready and have sneak peeks at our upcoming products available for partners. Interested? [Get in touch.](https://docs.google.com/forms/d/e/1FAIpQLScBNdM2a_fn8UZOKmFQt6lBsrd1o6FflvsdPH-Pn3JkdlN_Rg/viewform)