---
title: "Giving AI Agents the Document Understanding Layer They&#39;ve Been Missing"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/beyond-raw-text-how-llamaparse-and-liteparse-give-agents-real-document-understanding"
category: "document-processing"
---

Content



- [ Why Existing Tools Fall Short  ](#why-existing-tools-fall-short)
- [ LlamaParse and LiteParse Come to the Rescue  ](#llamaparse-and-liteparse-come-to-the-rescue)
- [ LlamaParse: Cloud-Based Parsing for Complex Documents  ](#llamaparse-cloud-based-parsing-for-complex-documents)
- [ LiteParse: Local-First Parsing for Speed and Privacy  ](#liteparse-local-first-parsing-for-speed-and-privacy)
- [ Complex Knowledge Work Finally Available for Agents  ](#complex-knowledge-work-finally-available-for-agents)
- [ The Bigger Picture  ](#the-bigger-picture)



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







 AI agents are remarkably capable at tasks that require context understanding (reasoning, coding, summarization…), as long as that context reaches them in clean, structured form. The real world, though, runs on complex documents: dense PDFs, presentation decks, spreadsheets embedded in Word files, scanned contracts, research papers with charts and footnotes… in short, unstructured knowledge.



 When agents encounter one of these formats, they face an important limitation: the tools natively available to most agent runtimes (simple file-read utilities and basic text extractors) treat a PDF like “unfriendly text”, collapsing tables into garbled rows, making embedded iamges and charts disappear, scrambling layouts and much more.



 The agent still receives something, but that something is simply text, without any significant spacial distribution, as well as deprived of images and other multimodal assets. This means the quality of every downstream task (be it summarization, Q&amp;A, data extraction, compliance checking…) degrades significantly, and not because a model intelligence problem, but because of a data plumbing one.



##  Why Existing Tools Fall Short



 Most agent frameworks give agents a handful of document-adjacent tools by default:


-  **Shell execution** (`exec` ) can invoke system utilities like `pdftotext`  or `strings` , which strip formatting and structure entirely.
  -  **Image tools** can analyze a single page screenshot, but have no awareness of document structure across pages, no way to correlate a table header on a page with its data rows on the following ones, and no mechanism to extract structured metadata.



 Most of these tools were designed for general-purpose use (file manipulation, format conversion…), not for document understanding: they might be able to extract some form of information, but this is often not really useful for downstream processing.



 Knowledge work automation (the kind of work that requires agents to read, interpret, and act on real enterprise documents) demands something more precise, that allows the agent to unlock a deeper document understanding layer.



##  LlamaParse and LiteParse Come to the Rescue



 Based on our experience with document-oriented workflows, we created skills for **LlamaParse** and **LiteParse**, aiming to fill the gap we outlined in the previous paragraphs, giving agents access to a structured, semantically rich layer of document understanding, the missing piece in the context engineering toolbox.



 These skills are designed for all autonomous agent runtimes that support installable skill overlays, such as OpenClaw, Claude Code or OpenCode: skills are injected directly into the agent&#39;s context when invoked, without requiring complex setups such as MCP servers, and they can steer the agent’s behavior to produce specific scripts or commands that it can then run within its own harness (bash console, sandbox…).



 Let’s dive deeper into what the LlamaParse and LiteParse skills can help the agent with.



###  LlamaParse: Cloud-Based Parsing for Complex Documents



 **LlamaParse** connects agents to LlamaIndex&#39;s cloud parsing API. It is the right tool when a document is complex: mixed layouts, embedded images, data tables, charts, multi-language content, or anything where raw text extraction would easily lose semantic connections, multimodal assets and metadata.



 Here are the key capabilities the skill unlocks for agents:


-  **Multiple parsing tiers**: `fast`  for simple text extraction, `cost_effective`  for budget-sensitive workflows, `agentic`  (the default) for complex layouts and tables, and `agentic_plus`  for the highest-accuracy extraction of intricate documents.
  -  **Rich output formats**: agents can request plain text, structured Markdown, page-level JSON with bounding boxes, image extraction with presigned download URLs, or Excel-aware metadata, allowing them to choose the format that best fits the downstream task.
  -  **Guided extraction via custom prompts**: the `agentic_options`  parameter lets agents instruct the parser to translate, summarize, or extract specific structured fields.
  -  **Image and chart awareness**: LlamaParse can extract images embedded in documents and return them as URLs the agent can fetch and analyze, enabling true multimodal document reasoning.



 In order to upload the file and then invoke the parser with the appropriate configuration, the agent produces a TypeScript script, based on the examples provided alongside with the skill file: the skill then guides the agent through a multi-step workflow consisting of running the script, collecting the results and producing a report based on the user’s prompt.



###  LiteParse: Local-First Parsing for Speed and Privacy



 **LiteParse** is a fully-local version of LlamaParse, running on your machine through a CLI tool (`lit` ): LiteParse is optimized for speed and model-free parsing, with the ability to extract text preserving spatial distribution.



 LiteParse can handle PDFs natively, and has support for Office documents and images via LibreOffice and ImageMagick. Its OCR layer (powered by Tesseract.js by default, with support for external OCR backends like EasyOCR or PaddleOCR) ensures that even scanned documents and image-heavy PDFs are legible to agents.



 Here are the key capabilities the skill unlocks for agents:


-  **Structured JSON output**: bounding-box-aware extraction that preserves spatial relationships between text elements, enabling agents to understand layout *and* content, and use downstream processing tools like `jq`  to quickly move through the JSON output.
  -  **Page screenshots**: the `lit screenshot`  command generates visual renderings of document pages, which agents can pass to vision-capable models for layout-aware analysis.
  -  **Targeted parsing**: agents can parse specific page ranges (`--target-pages &quot;1-5,10&quot;` ) rather than entire documents, enabling efficient extraction from large files.
  -  **Batch processing**: entire directories of documents can be parsed in a single invocation, enabling pipeline-style document workflows.
  -  **Configuration files**: for repeated parsing tasks with consistent settings, agents can write and reuse `liteparse.config.json`  files, building reproducible document-processing pipelines.



##  Complex Knowledge Work Finally Available for Agents



 The combination of LlamaParse and LiteParse gives agents a solid answer to a previously hard problem: instead of hoping that a raw text dump contains enough signal to reason from, agents can now:


-  **Extract structured data from financial reports**, preserving table relationships and precision across multi-page documents.
  -  **Parse legal contracts** with layout-aware extraction that keeps clause hierarchy, defined terms, and cross-references intact.
  -  **Process research papers**, correctly segmenting abstract, methodology, results, and references, even when the paper uses two-column academic formatting.
  -  **Handle mixed document workflows**, routing simple text-dense files to LiteParse for speed and cost efficiency, while escalating complex or image-heavy documents to LlamaParse for maximum accuracy.
  -  **Operate within privacy boundaries**, running LiteParse entirely on-device for sensitive documents while reserving cloud parsing for appropriate use cases.



 In an agent runtime like OpenClaw, where skills are injected as instructional context at session start, these capabilities become first-class behaviors. The agent doesn&#39;t need to be told how to parse a PDF on every invocation, because the skill is carefully engineered to be a relevant part of its context, making document understanding one of the basics of the agent&#39;s operational vocabulary.



##  The Bigger Picture



 The hard reality for agents today is that documents cannot be ignored or partially understood: they are the primary medium through which organizations capture, store, and transmit the knowledge that drives decisions, which makes their understanding vital to build any application that touches knowledge work.



 Our goal with the LlamaParse and LiteParse skills is to close that gap, and not by building more powerful models, but simply giving existing models better tooling and inputs.



 *LlamaParse and LiteParse are available as agent skills for Claude Code and compatible runtimes. Install them via `npx skills add run-llama/llamaparse-agent-skills` .*