---
title: "LlamaIndex is more than a RAG Framework. It is Agentic Document Processing."
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-is-more-than-a-rag-framework"
category: "rag"
---

Content



- [ Where It Started  ](#where-it-started)
- [ Agent Orchestration and Retrieval Have Fundamentally Changed  ](#agent-orchestration-and-retrieval-have-fundamentally-changed)
- [ There’s a Lot of Alpha in Solving Document Understanding  ](#theres-a-lot-of-alpha-in-solving-document-understanding)
- [ Better OCR also Transforms the Legacy IDP Industry  ](#better-ocr-also-transforms-the-legacy-idp-industry)
- [ LlamaParse  ](#llamaparse)
- [ Automating Knowledge Work with Agents  ](#automating-knowledge-work-with-agents)
- [ On Open Source  ](#on-open-source)



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



   101



 We launched LlamaIndex as an open-source framework in late 2022, right at the start of the RAG wave. The framework grew fast (47K GitHub stars, 5.2M monthly downloads), and became a core starter toolkit for any developer building RAG and agentic applications in production.



 Since then, the AI orchestration landscape has drastically evolved. RAG was a big topic in 2023, but since then there have been exponential advancements both in terms of model reasoning capability (gpt-3.5 → gpt-5.3, opus 4.6), model harnesses (skills, mcp tools, memory, compaction, progressive disclosure), retrieval (files are all you need ?!), and the developer tooling itself (Claude Code, Codex). As a result a proper “AI framework” needs to constantly reinvent its own abstractions to stay relevant in this rapidly changing landscape.



 At the same time, even as agent orchestration has evolved, so has the need for high-quality unstructured context to ensure agents can perform useful human-level work. We became especially interested in this gap around document based data. The vast majority of enterprise knowledge is locked in PDFs, Powerpoints, Word docs, and Excel files, and there were no good tools that could adequately extract out information from these documents into high-quality text tokens. Providing this layer would allow agents to access a massive pool of high-quality unstructured context to automate an entire category of white-collar knowledge work.



 Over the past 2 years, we have narrowed and refined our mission as a company. While we have always been known for quality developer tooling, our focus is now on building best-in-class, enduring document infrastructure rather than framework abstractions for the future of agentic work automation.


-  We are no longer “just” a RAG framework with the mission of being solely the connective tissue between LLMs and data.
  -  **Instead, we are building deep-tech, best-in-class agentic document processing (OCR, extraction, and workflows). Our current mission is to provide the core infrastructure to automate knowledge work over documents.**



##  Where It Started



 Even back during the early days of LlamaIndex as a framework, it was clear that LLMs were incredible at making sense of unstructured text and taking actions on top of it, and one of the biggest opportunities was providing these LLMs high-quality context.



 The most common initial use case we observed was people building RAG chatbots over PDFs. We tried a variety of our OCR data connectors to help users parse the most complex documents. Without naming names, the results were terrible - existing OCR tools would misalign tables, ignore charts, and introduce text gibberish instead of a coherent reading order. This led to downstream failures in the applications themselves; the generated answers would be incomplete or hallucinated and the citations don&#39;t link back to good source data. We saw this over and over, and it kept being true even as models got better and agent architectures evolved.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/6489ef8b87608b5d55d39726d8148a3be2f18288-1200x676.png)

##  Agent Orchestration and Retrieval Have Fundamentally Changed



 We spent a lot of time building out the framework to advance RAG patterns and early agent architectures. Indexing abstractions, query engines, tool integrations, agent loops - these were the tools developers needed to actually get LLM apps to production, and they were genuinely useful for a while.



 But the stack moved faster than anyone expected, in three ways we didn&#39;t anticipate:


-  General agent reasoning loops got way more sophisticated. Simple ReAct agents or deterministic workflows used to be the best we had. Now agent loops can do extended reasoning, self-correction, and multi-step planning in ways that are fundamentally more trustworthy. The gap between what a basic tool-calling agent could do in 2023 and what Claude or GPT can do in an agent loop today is massive.
  -  New abstractions emerged around how agents discover and use tools. Skills and MCP created standardized ways for agents to access capabilities without needing framework-level integrations for everything. You no longer need a framework integration for every single tool - the agent can discover and call tools on its own.
  -  Coding agents changed how people build software. When Claude Code or Cursor can just write the Python for you, the value of framework abstractions drops significantly. Developers don&#39;t need a library to wrap an LLM call anymore.



 The net result is that general-purpose LLM frameworks - the kind of thing LlamaIndex and LangChain (and some others) built - aren&#39;t as central as they used to be. That&#39;s OK. The industry needed those tools to bootstrap, and now it&#39;s moved past the point where you need as many abstractions between you and the model.`



 RAG patterns have shifted too. We wrote about this in our &quot;[Files Are All You Need](https://www.llamaindex.ai/blog/files-are-all-you-need)&quot; post: it turns out that if you equip agents with good filesystem tools, they can do dynamic search over document collections that outperforms naive semantic search. The agent interleaves search with read operations, deciding what to look at based on what it&#39;s already found - similar to how a human would browse through a folder of files. The chunking and indexing part of traditional RAG has become less critical as a result.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/24d9172e9f31f13186820bd0d579b83589b5e664-1200x676.png)

##  There’s a Lot of Alpha in Solving Document Understanding



 When frontier models started to add vision capabilities, I like many others thought that document parsing would get commoditized: screenshot every page and prompt the model to parse the document into markdown. But it quickly became clear that accurate/cheap document parsing/extraction was far from being a solved problem ([we also wrote about this here](https://www.llamaindex.ai/blog/llm-apis-are-not-complete-document-parsers)).


-  Frontier vision models struggle with the long tail of accuracy parsing information-rich pages, like line charts, extremely dense tables (~hundreds or rows/columns in a single page), and handwritten forms. They also struggle with one-shot extraction that requires navigating relationships within large documents.
  -  They’re also not price optimized. Most production OCR stacks process millions if not billions of pages every month. Frontier models are tuned for general reasoning, and you could get equivalent performance at &lt;1/10th the cost. Also document types vary wildly; you’re unnecessarily burning vision tokens if most of your pages are text.
  -  A one-shot LLM call will miss a lot of crucial metadata like precise layouts, citations, and confidence scores.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/d97e422d75efe1279dfabdef4641a27385443bf8-1200x676.png)

 Document parsing remains a core need as the AI world has evolved from RAG to agentic workflows to general long-running agents. The latest agents are amazing at operating over plaintext files like .md or .txt, but by definition they cannot read any non-plaintext formats like .pdf or .docx unless there is an OCR layer in place.



##  Better OCR also Transforms the Legacy IDP Industry



 As we went deeper on document parsing, we started to realize we weren&#39;t just solving the LLM context problem. We were also building the right tooling for a massive existing industry that has been underserved for decades.



 OCR has been around for 20+ years, and it powers an entire category of enterprise software that most people in the LLM world don&#39;t think about much. IDP (intelligent document processing) is what happens when companies need to take unstructured documents and extract structured data from them at scale - insurance underwriting, invoice processing, claims review, financial document analysis. Companies like ABBYY and Kofax have built large businesses around these use cases. These are huge enterprise workflows where humans use software to manually review and extract data from documents every day, completely separate from anything related to LLMs or RAG.



 The existing OCR tools for these workflows have always been fragile. They break with layout changes, needs frequent retraining, can&#39;t interpret images or charts, and produces error rates that demand heavy manual review.



 When your parsing accuracy is 90% instead of 99%, the impact on these workflows is huge. That gap is the difference between automating a process end-to-end and needing a human to review every single output. It directly hits straight-through processing rates, which is what enterprises actually care about when they measure document automation ROI. And it turns out the same technology that makes a PDF readable by an LLM agent also makes it far more accurate for these traditional IDP workflows.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/47fa5913dd7d644457a36b1a3265f325ca2b6c66-1200x676.png)

##  LlamaParse



 We built [LlamaParse](https://www.llamaindex.ai/llamaparse) to solve both of these problems - accurate document understanding for LLM context and for traditional document extraction. It started as a parsing API and has grown into what I think is the best agentic document understanding system available today. The core architecture uses a multi-agent pipeline: traditional OCR for text extraction, computer vision for layout detection, and LLM-based reasoning to handle complex elements like tables, charts, and multi-column layouts. Tables get one treatment, text-heavy pages get another, charts get another. The output is clean Markdown, JSON, or HTML with confidence scores and bounding boxes for HITL verification.



 We&#39;ve now processed over half a billion pages through LlamaParse across 50+ file formats, and are used across enterprises like Carlyle, Cemex, KPMG to popular AI-native startups across coding, finance, insurance, and more.



 We have a dedicated applied AI research team making sure our OCR technology is best in class. LlamaParse wraps this and allows users to execute additional operations: “Extract” for pulling structured data out of docs using custom schemas, “Classify” for fast document routing, “Split” for breaking a document into subsections, and [“Sheets” for dealing with Excel files in particular](https://www.llamaindex.ai/blog/announcing-llamasheets-turn-messy-spreadsheets-into-ai-ready-data-beta). We also have indexing and retrieval built in so you can build searchable knowledge bases over everything you&#39;ve parsed.



##  Automating Knowledge Work with Agents



 The bigger opportunity is taking all of these capabilities and composing them into e2e workflows that automate real knowledge work. Completely separate from chatbots and RAG, there are a ton of existing workflows where humans manually process documents every single day. Financial analysts spend hours reading dense reports to find a few key figures. Operations teams update shipment data across systems constantly. Underwriters spend 60% of their time just extracting information from paperwork.



 These workflows have been running on bad OCR and manual review for years. With good enough document understanding and agent orchestration, we can start to model them as e2e agentic processes. Imagine an agent that ingests a stack of contracts, extracts key terms using your company&#39;s schema, checks them against compliance policies, and flags exceptions for human review. That takes a legal team hours to do manually. An agent does it in minutes.



 We&#39;re starting to help companies build exactly these kinds of workflows with [LlamaAgents](https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents) - our platform that lets you build complex document workflows either through code or [describing the workflow in plain English](https://www.llamaindex.ai/blog/llamaagents-builder-idea-to-deployed-agent-in-minutes). The underlying code layer is powered by our [Workflows framework](https://github.com/run-llama/workflows-py), a light but extremely powerful event-driven way of orchestrating an LLM workflow.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/b0cac3474e4b815b3cf5f2ce5c615a99328c9637-1200x676.png)

##  On Open Source



 We started as an open-source company, and that still matters to us. We&#39;ll keep supporting [framework](https://github.com/run-llama/llama_index) users, and we&#39;re going to evolve our OSS tooling to help developers process and use documents with agents in production. The focus has gotten narrower, but we&#39;re not abandoning the community. You will see a lot of exciting releases coming from us in the (near) future!



 Our North Star is automating knowledge work over documents, and we&#39;re excited about what&#39;s ahead.


-  If you’re dealing with document processing challenges, whether it’s within an agent or human workflow, come try [LlamaParse](https://www.llamaindex.ai/) and check out our [documentation](https://developers.llamaindex.ai/python/cloud/).
  -  If you want to talk about agentic document workflows for your use case, [reach out](https://www.llamaindex.ai/contact).
  -  If you’re excited about orchestrating and tuning the latest frontier/open-source LLMs/VLMs for solving document understanding, we have a few roles open on our [careers page](https://www.llamaindex.ai/careers)!