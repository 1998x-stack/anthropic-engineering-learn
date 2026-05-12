---
title: "LlamaIndex Newsletter 2025-12-16"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-16"
category: "llamaindex-core"
---

Content



- [ 📣 Call for Feedback:  ](#call-for-feedback)
- [ 🤩 The Highlights:  ](#the-highlights)
- [ 🗺️ LlamaParse:  ](#llamaparse)
- [ ✨ Framework:  ](#framework)



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



 Welcome to this week&#39;s edition of the LlamaIndex newsletter! We&#39;re excited to share some major updates including our new LlamaSplit API for automatic document segmentation, enhanced security for coding agents with virtual filesystems, LlamaSheets for complex spreadsheet handling, and powerful async batch processing capabilities. Plus, we&#39;ve added new CLI functionality to SemTools that makes document search even more intuitive.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



###  📣 Call for Feedback:



 We&#39;re collecting feedback from early users of our newest products:


-  **Take a feedback call for LlamaAgents**: Tell us about your agent workflows and use cases - [Submit Form](https://docs.google.com/forms/d/e/1FAIpQLSe96FHwy3yvS4nMUHJL9H944luEKkqwDggbmkpOKwGkS3MJAQ/viewform?usp=sharing&ooid=117925267046539208209)
  -  **Take a feedback call for LlamaSheets**: Share your experience with our spreadsheet parsing API - [Submit Form](https://docs.google.com/forms/d/e/1FAIpQLSdnIv6pU6rA_m53zzOM4sieAaPL3_k3bwDjqv7nX52hKjBy2Q/viewform?usp=sharing&ouid=117925267046539208209)



 Users who schedule calls with us will be entered into a raffle for $50 gift cards!







###  **🤩 The Highlights:**


-  **Secure AI Coding Agents:** Build safe coding agents with virtual filesystem isolation, enhanced document processing via LlamaParse, and workflow orchestration that prevents accidental file deletions while maintaining full functionality. [Blog Post](https://www.llamaindex.ai/blog/making-coding-agents-safe-using-llamaindex?utm_source=socials&utm_medium=li_social), [GitHub](https://github.com/run-llama/agentfs-claude)
  -  **LlamaSplit API (Beta):** Automatically separate bundled documents into clear, targeted sections using AI - perfect for resume stacks, mixed financial documents, court filings, and research collections with precise page ranges and confidence scores. [Blog Post](https://www.llamaindex.ai/blog/split-document-into-clear-targeted-sections-with-llamasplit?utm_source=newsletter), [Docs](https://developers.llamaindex.ai/python/cloud/split/getting_started/?utm_source=newsletter)
  -  **Async Batch PDF Processing:** Process entire folders of PDFs simultaneously with LlamaParse using asyncio and semaphores to control concurrency, prevent rate limits, and maximize throughput for large document collections. [Tutorial](https://developers.llamaindex.ai/python/cloud/llamaparse/examples/async_parse_folder/?utm_source=newsletter)



###  🗺️ LlamaParse:


-  **LlamaSheets (Public Beta):** Handle complex, messy spreadsheets with multiple sub-sheets and regions. LlamaSheets automatically identifies sub-regions, creates summaries, and returns structured data as parquet files. [Get Started](https://developers.llamaindex.ai/python/cloud/llamasheets/getting_started/?utm_source=newsletter)
  -  **LlamaSplit Document Segmentation:** New beta API that uses AI to automatically classify and separate bundled documents into targeted sections based on your defined categories, with exact page ranges and confidence scores. [Blog Post](https://www.llamaindex.ai/blog/split-document-into-clear-targeted-sections-with-llamasplit?utm_source=newsletter), [Docs](https://developers.llamaindex.ai/python/cloud/split/getting_started/?utm_source=newsletter)



###  ✨ Framework:


-  **SemTools &quot;Ask&quot; Command:** New dedicated CLI command for agentic search over documents - combine with parse to create QA workflows over unstructured data and cache indexes with workspaces. [Learn More](https://t.co/3f2Mfg3xCc)