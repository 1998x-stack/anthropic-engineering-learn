---
title: "Document Understanding for Claude Code: 3 Ways | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/adding-document-understanding-to-claude-code"
category: "document-processing"
---

Content



- [ Why Do We Care?  ](#why-do-we-care)
- [ Three Ways to Give Claude Code Document Understanding  ](#three-ways-to-give-claude-code-document-understanding)
- [ 1. Access your Docs through MCP  ](#1-access-your-docs-through-mcp)
- [ 2. Operate over your Docs through the CLI  ](#2-operate-over-your-docs-through-the-cli)
- [ 3. Teach Claude Code How to Build Agentic Document Workflows  ](#3-teach-claude-code-how-to-build-agentic-document-workflows)
- [ Get Started!  ](#get-started)



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



   20



 The rise of coding agents like Claude Code, Cursor, Windsurf, Cognition, Lovable, etc. marks a shift in how software is built. Instead of manually wiring APIs together, you can describe what you want through natural language, and the agent can handle the technical task of writing, executing, and iterating on the code. This opens up the possibility for “low-code IT” and allowing business users to quickly build internal and external-facing applications.



 But there’s a problem: by default, coding agents don’t natively *understand documents.* This limits their utility for building business applications. Enterprise applications live and breathe documents: contracts, financial reports, legal briefs, technical specifications, meeting notes. These documents are typically locked up within file formats like .pdf, .pptx, .docx, .xlsx and require *specialized tooling* to read and search over that information, tooling that coding agents don’t have.



 This may sound surprising at first glance. But coding agents have real limitations for understanding files:


-  Cursor doesn’t support PDF upload at all (and many other files).
  -  Claude Code has a `Read`  capability that has basic PDF understanding capabilities, but a max file size of 32 MB and 100 pages per request.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/2fa515399a9df24d11d3b716d8da40b0d8908580-2080x1192.png) Claude Code will error out on reading both large PDFs (and also not interpret complex documents well)





 By equipping coding agents with the right tools around document understanding:


-  They can pull in more context. This means building apps that better adapt to business requirements.
  -  They can use the tools within the generated code. This means building apps that are more *agentic, generalized, and higher accuracy.*



 In this blog we use Claude Code as a proxy for all coding agents. At its core, this post helps to explore what it means to equip Claude Code with the ability to understand and work with an entire bucket of PDFs.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Why Do We Care?



 A recent [MIT report](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf) mentioned that the 5% of AI agents that do make it to production are those that can deeply embed themselves in custom business workflows. A *lot* of those workflows are document-based - [90% of enterprise data is locked up within documents](https://blog.box.com/90-your-data-unstructured-and-its-full-untapped-value). Without document understanding tooling, coding agents are missing *core context* and are also *unable to build useful automations*.


-  **Missing Core Context:** When you ask Claude Code to build a financial reporting dashboard, it should understand what your quarterly reports actually look like, how your data is structured, and what metrics matter to your business. In a lot of enterprise settings, these documents are probably locked up as PRDs and product specs within a file repository like Google Drive or Sharepoint. Without this context, Claude Code will generate generic templates based on assumptions.
  -  **Unable to Build Useful Automations:** Ask Claude Code to build contract review software and it might generate code that looks for keywords like &quot;termination&quot; or &quot;liability,&quot; but completely miss the nuanced legal language that determines enforceability. This means that the automations Claude Code generates is brittle and not generalizable to various inputs, which also means they’re not very useful.



 Building most business applications requires Claude Code to have both (1) and (2). Imagine you’re a private equity analyst looking to automate due diligence analysis over a data room of financial documents. Claude Code would need an initial layer of document understanding to process an example set of financial docs (are they public filings, reports), along with previous due diligence reports, in order to understand the business requirements. It would also need to leverage these modules during the generated workflow.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/df3f30cf36f725628aa18fed1fb44caba18f30fb-3956x1528.png) End to end architecture of adding document understanding to Claude Code in an example scenario for building a due diligence application. It’s used both during the context gathering phase as well as app generation phase.

##  Three Ways to Give Claude Code Document Understanding



 Over the past few months, we’ve been exploring ways to bridge this gap. Here are three complementary patterns for adding document intelligence to Claude Code. Each approach has their own tradeoffs, and we describe them in detail so you can pick and choose which one(s) to use for your own purposes.



###  1. Access your Docs through MCP



 Claude Code natively supports the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/registry). There is a long list of official MCP integrations that allow connecting to any SaaS service, from [Salesforce](https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce) to [Confluence](https://www.atlassian.com/blog/announcements/remote-mcp-server) to [Figma](https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/). If your data source is primarily a collection of files, you will need to do *pre-processing* on the document collection before exposing it as an MCP endpoint to Claude Code.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/3e8d08b0305e2f2639b0b5f59f9843227947e55d-1920x1278.webp) Use LlamaParse as a core document indexing/retrieval layer





 **How**: You need a service to parse, chunk, and embed your documents (PRDs, financial reports, claims) into a storage system (vector db, structured database, graph database), and expose it as a set of MCP tools. During code generation, Claude Code can choose to query the MCP server to give it rich context about your business processes, policies, and data structures.



 **Why**: This gives your coding agent a quick and dirty way to access a large pile of context. When you ask it to &quot;create an expense approval workflow,&quot; it already knows your company&#39;s spending limits, approval hierarchies, and policy exceptions because it can query your indexed policy documents.



 **Tradeoffs**: There are a few downsides with this approach.


-  The quality of your context depends heavily on your indexing/retrieval/MCP implementation! There are no official MCP servers for popular file repositories like Sharepoint, and many of the community ones do not have robust endpoints for search.
  -  The coding agent can directly access context, but it cannot access the indexing implementation itself to build a robust document understanding workflow.
  -  If your coding agent is accessing dozens/hundreds of MCP servers, you run into the problem of federated search. This is where a centralized, high-accuracy index still matters. As we argued in [“Does MCP Kill Vector Search?”](https://www.notion.so/blog/does-mcp-kill-vector-search), federated MCP is powerful but insufficient without a preprocessing and indexing layer over unstructured data. (If you don’t believe us, Glean argued the same thing [here](https://www.glean.com/blog/federated-indexed-enterprise-ai)).



 Tools like LlamaParse made accessible through the open-source [LlamaParse MCP server](https://github.com/run-llama/llamacloud-mcp) or [https://mcp.llamaindex.ai/](https://mcp.llamaindex.ai/) help to alleviate (3) and partially (1): it provides centralized indexing to reduce the downsides of federated retrieval. It also has high-quality standardized modules for parsing, indexing, and retrieval, though it doesn’t have the richness of operations that you may get through a CLI (see below).



###  2. Operate over your Docs through the CLI



 Coding agents are extremely good at using command-line tools, which provide a diverse range of operations that you cannot get through “pure” semantic search (e.g. `grep` , `cat` , `find` ). Adding an agentic reasoning/tool calling layer to search allows you to get powerful results even if the search tools themselves are simplistic (see [Windsurf’s](https://x.com/_mohansolo/status/1899630153636118529) implementation of code search).



 **The main existing limitation is that coding agents suck at reasoning over files**: Standard CLI operations like `grep` , `cat` , and `find`  are designed for structured text, not complex documents. They can&#39;t parse a PDF&#39;s table structure, understand the semantic meaning of a passage, or extract specific fields from scanned invoices.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ec423615e7d33ad5b7986c0ae29550b3f594651d-983x1022.jpg) semtools equips Claude Code with parse and search operations





 **The solution**: Give the coding agent context on an *expanded set of CLI commands* that can do document parsing, extraction, and search. This lets them read documents, dump it to a cache, get all the benefits of `grep`  and `cat`  over the indexed data, but still give the coding agent access to semantic search.



 **Why**: Imagine tasking a coding agent with analyzing 100+ legal briefings to identify precedent cases. With enhanced CLI tools, it can efficiently search across the entire corpus, extract relevant citations, and cross-reference findings—all while staying within the familiar command-line interface that coding agents excel at using.



 **Tradeoffs:** You need to ensure 1) all the files are available locally / in an environment where you can access a CLI, and 2) we found this [approach works well over ~1k docs](https://www.llamaindex.ai/blog/semtools-are-coding-agents-all-you-need), but it is not entirely clear whether it works well over 1M+ documents, where you would need to fall back to semantic search.



 Tools like [SemTools](https://github.com/run-llama/semtools) add `parse`  and `search`  commands that give coding agents true document understanding capabilities. This approach is particularly powerful because it maintains the flexibility and composability that makes CLI tools so effective while adding the document intelligence that business applications require.



###  3. Teach Claude Code How to Build Agentic Document Workflows



 The first two sections above help Claude Code get more *enterprise context* through your documents, but don’t necessarily help it *structurally build a better business application.*



 **Rules-based approaches won’t generalize:** whether the generated app is interpreting contracts, invoices, or financial filings, it will not be very useful if the generated code is primarily rules-based and uses poor-quality document modules. All of these input documents are high-dimensional and can vary widely in complexity; rules-based approaches will easily break on the vast majority of inputs. The coding agent generates hard-coded rules to process invoices with a specific format. When invoice layouts change or new vendors use different templates, the application breaks. The agent can&#39;t interpret results or adapt to new document types.



 **The solution:** A better business application fundamentally needs to be AI-native. This final step “teaches Claude Code how to fish” - instead of just providing context in a one-off manner, it gives Claude Code the underlying document parsing, extraction, and workflow tooling so that it can directly use these modules in the generated application.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/9cae0dc5b21c79a74e8997e44affba0cc7f3404b-1004x720.gif)

 **How:** Append to [CLAUDE.md](http://CLAUDE.md) in a standardized way to use document parsing and workflow modules:


-  The document parsing APIs need to handle complex document layouts, provide confidence scores and citations for extracted data, and maintain consistency across different document types.
  -  The workflow APIs need to enable coding agents to build multi-step workflows that combine document processing with human oversight, error handling, and quality validation
  -  If you have a large amount of documentation to provide to your agent (for example, over 20K tokens), then you will likely get better results by developing a documentation retrieval tool with MCP. Overloading the [CLAUDE.md](http://CLAUDE.md) file will have negative impacts past a certain point.



 **Why:** This will give it a standardized language to build applications that interpret documents and reason over it in a general manner. When new invoice formats appear, the underlying document intelligence adapts automatically. The application can understand what it&#39;s processing and provide meaningful feedback about confidence levels and extracted data quality.



 Tools like [vibe-llama](https://github.com/run-llama/vibe-llama) give your coding agents standardized context on how to build these agentic document workflows, powered by LlamaParse for document understanding and LlamaIndex Workflows for agent orchestration.



##  Get Started!



 The best thing to do is all three!



 We&#39;re moving from a world where applications are built by engineers who understand both business requirements and technical implementation, to one where domain experts can directly express their needs to coding agents that handle the technical complexity.



 But this transition only works if coding agents can bridge the gap between natural language business requirements and the messy reality of enterprise data. Documents are where this gap is most apparent—and most critical to solve.



 We’re building that bridge at LlamaIndex. All this tooling is available *today* - whether you’re a more technical or less technical AI builder, our resources help provide **a robust, reusable foundation for document-centric workflows.**



 **Connector Resources:**


-  [LlamaParse MCP](https://github.com/run-llama/llamacloud-mcp)
  -  [SemTools](https://github.com/run-llama/semtools)
  -  [vibe-llama](https://github.com/run-llama/vibe-llama)



 **Core Services:**


-  [LlamaParse](https://cloud.llamaindex.ai/)
  -  [Workflows](https://developers.llamaindex.ai/python/workflows/)