---
title: "LlamaIndex Newsletter 2026-03-24"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-03-24"
category: "llamaindex-core"
---

Content



- [ 🎉 LiteParse: New Open-Source Document Parsing  ](#liteparse-new-open-source-document-parsing)
- [ 🤩 The Highlights  ](#the-highlights)
- [ ☁️ LlamaParse  ](#llamaparse)



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







 Hi there, Llama Enthusiasts! 🦙



 Welcome to this week&#39;s edition of the LlamaIndex newsletter! We&#39;re excited to share some major developments in document parsing, including the launch of our new open-source LiteParse tool, enhanced visual grounding capabilities, and powerful new agent integrations. Plus, we dive deep into context engineering principles and showcase real-world applications from financial assistants to legal discovery workflows.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  🎉 LiteParse: New Open-Source Document Parsing



 **Introducing LiteParse:** We&#39;ve open-sourced a lightweight, local document parser built from years of LlamaParse development. Features layout preservation, local OCR, and multimodal LLM support with simple npm i -g @llamaindex/liteparse installation. [Read the announcement blog](https://www.llamaindex.ai/blog/liteparse-local-document-parsing-for-ai-agents) and [explore the GitHub repo](https://github.com/run-llama/liteparse).







###  🤩 **The Highlights**


-  **Context Engineering Deep Dive:** Learn why context engineering is the new prompt engineering and how proper document parsing sits at the heart of building better AI agents. Discover techniques for filling context windows with structured information for optimal agent performance. [Read the full guide](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)
  -  **LiteParse Agent Skills:** Ready-to-use agent skills for the new open-source LiteParse that integrate seamlessly with coding agents using simple npx skills add run-llama/llamaparse-agent-skills --skill liteparse commands. [Documentatio](https://developers.llamaindex.ai/liteparse/guides/agent-skill/)



###  ☁️ **LlamaParse**


-  **Smart Financial Assistant with Google:** New collaboration with Google Developers showing how to build intelligent financial assistants using LlamaParse and Gemini 3.1, featuring VLM-enabled agentic OCR for accurate text and table extraction. [Blog](https://developers.googleblog.com/build-a-smart-financial-assistant-with-llamaparse-and-gemini-31/) | [Demo repo](https://github.com/run-llama/llamaparse-gemini-demo)
  -  **Agent Skills Integration:** LlamaParse now offers official Agent Skills that work across 40+ agents, providing built-in instructions for parsing complex documents, tables, charts, and images for deeper document understanding. [Documentation](https://developers.llamaindex.ai/python/cloud/llamaparse/agent-skill) | [Get started](https://login.llamaindex.ai/?client_id=client_01K39WZXHMNYBR1MSJSYAQRVFT&redirect_uri=https%3A%2F%2Fapi.cloud.llamaindex.ai%2Fapi%2Fv1%2Fauth%2Fworkos%2Fcallback&state=eyJyZWRpcmVjdCI6ICJodHRwczovL2Nsb3VkLmxsYW1haW5kZXguYWkvc2lnbnVwP3V0bV9zb3VyY2U9c29jaWFscyZ1dG1fbWVkaXVtPWxpX3NvY2lhbCJ9&authorization_session_id=01KMFGPX7RFH7SVCH7VWZ6AMM8)
  -  **Legal Discovery Parsing:** Comprehensive guide on handling challenging legal documents including low-resolution scans, handwritten annotations, and complex charts using LlamaParse&#39;s vision models and custom parsing instructions. [Read the blog](https://www.llamaindex.ai/blog/parsing-the-unreadable-how-llamaparse-handles-legal-discovery-documents)
  -  **Visual Grounding with Bounding Boxes:** LlamaParse Agentic Plus mode now provides precise visual grounding with bounding box citations, enabling exact location tracking for complex LaTeX formulas, handwriting, and infographics. [Try it now](https://login.llamaindex.ai/?client_id=client_01K39WZXHMNYBR1MSJSYAQRVFT&redirect_uri=https%3A%2F%2Fapi.cloud.llamaindex.ai%2Fapi%2Fv1%2Fauth%2Fworkos%2Fcallback&state=eyJyZWRpcmVjdCI6ICJodHRwczovL2Nsb3VkLmxsYW1haW5kZXguYWkvP3V0bV9zb3VyY2U9c29jaWFscyZ1dG1fbWVkaXVtPWxpX3NvY2lhbCJ9&authorization_session_id=01KMFGPYM42Y4ERHEB3NZ0E5TG)
  -  **Agentic Document Extraction:** Learn how agentic AI transforms document extraction from simple OCR to intelligent reasoning, dramatically reducing manual review queues and maintenance overhead with plan-act-verify loops. [Full breakdown](https://www.llamaindex.ai/blog/agentic-document-extraction)