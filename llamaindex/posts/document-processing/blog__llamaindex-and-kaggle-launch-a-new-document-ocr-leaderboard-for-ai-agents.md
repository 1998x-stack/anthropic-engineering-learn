---
title: "LlamaIndex and Kaggle launch a new Document OCR leaderboard for AI agents"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-and-kaggle-launch-a-new-document-ocr-leaderboard-for-ai-agents"
category: "document-processing"
---

Content



- [ The challenge of enterprise document understanding  ](#the-challenge-of-enterprise-document-understanding)
- [ Introducing ParseBench for rigorous evaluation  ](#introducing-parsebench-for-rigorous-evaluation)
- [ Why partner with Kaggle  ](#why-partner-with-kaggle)
- [ Future plans for agentic evaluations  ](#future-plans-for-agentic-evaluations)



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



   1



 **The new leaderboard, ParseBench, is designed to accelerate progress building and evaluating document parsing models and agents that can read the messy, high‑stakes files enterprises run on.**



 Check out the new leaderboard on Kaggle: [ParseBench Leaderboard](https://www.kaggle.com/benchmarks/llamaindex-org/parsebench)



 AI agents are increasingly being put to work approving insurance claims, analyzing financial filings, and extracting terms from contracts inside the world&#39;s largest companies. Like any other software, an agent integrated into a business workflow needs to work reliably at scale, but today it isn&#39;t easy to verify that the parsers feeding those agents are reading documents the way engineers expect.



 Today, LlamaIndex is partnering with Kaggle to bring Parsebench, the first document OCR benchmark for AI agents, to thousands of AI engineers, developers, and scientists who visit the site every day. Practitioners can evaluate parsers, vision‑language models, and document agents on realistic extraction tasks drawn from insurance filings, financial reports, regulatory submissions, and contracts, and make informed choices about which models to plug into their agents.



##  **The challenge of enterprise document understanding**



 Enterprise content is messy. A single page of a SERFF filing or a 10‑K can contain merged table cells, hierarchical headers, footnoted superscripts, strikethrough pricing, and charts whose values live only in pixels. Humans can work around these quirks; agents can&#39;t — yet. If a coverage table&#39;s headers are transposed, the agent reads the wrong column. If a decimal is dropped, a calculation is off by orders of magnitude. If a strikethrough is silently stripped, the agent quotes the old price. The bar for OCR has shifted from &quot;good enough for a human to read&quot; to &quot;reliable enough for an agent to act on.&quot;



 This has led to a boom in document parsers and vision‑language models that promise to handle the problem; the challenge is telling them apart. Popular OCR benchmarks have driven real advances, but they don&#39;t reflect the demands of enterprise workflows, where agents must reason over tables, preserve meaningful formatting, ground every value back to a bounding box, and support high‑stakes decision‑making. Even [OmniDocBench](https://www.llamaindex.ai/blog/omnidocbench-is-saturated-what-s-next-for-ocr-benchmarks), the most diverse benchmark available, draws just 6% of its pages from enterprise content.



##  **Introducing ParseBench for rigorous evaluation**



 LlamaIndex is on a mission to unlock document understanding for AI agents. Just a few weeks ago, we released [ParseBench](https://www.llamaindex.ai/blog/parsebench), a benchmark that brings scientific rigor to how document parsing and OCR systems are evaluated for real agent workflows. Rather than scoring extractors on academic PDFs with fuzzy text‑similarity metrics, ParseBench evaluates ~2,000 human‑verified enterprise document pages with over 167,000 test rules across the five dimensions that actually break downstream agents: tables, charts, content faithfulness, semantic formatting, and visual grounding.



 In the case of ParseBench, that could be tasks like extracting a nested coverage table from an insurance filing, reading off specific data points from a bar chart in a financial report, identifying a footnote reference marked by a superscript, or tracing an extracted number back to its exact location on the page for audit. The benchmark tests 14 methods across general‑purpose VLMs (GPT‑5 Mini, Haiku 4.5, Gemini 3 Flash, Qwen 3 VL, Dots OCR 1.5), specialized document parsers (Textract, Azure Document Intelligence, Google Cloud Document AI, Docling, etc.), and LlamaParse in both Cost Effective and Agentic tiers.



 Agentic parsers have taken this a step further, routing pages through different models, self‑correcting on low‑confidence regions, and producing outputs structured enough that a downstream agent can act on them directly. ParseBench helps developers tell which approaches actually hold up.



##  **Why partner with Kaggle**



 This is where Kaggle comes in. It&#39;s where AI practitioners convene to compare models, explore datasets, and stress‑test the software they plan to implement. Through their SDK, the team made it simple to build, execute, and turn ParseBench into a leaderboard in a transparent, reproducible and verifiable way.



 *&quot;They remove the operational complexity of running and maintaining a high‑quality benchmark,*&quot; said a member of the LlamaIndex research team.



 *&quot;We want to bring academia, clients, startups, and model providers together to collectively innovate on what &#39;correct&#39; really means for agentic document understanding.&quot;*



##  **Future plans for agentic evaluations**



 The leaderboard marks the beginning of a broader effort between LlamaIndex, partner organizations, and the open community to help solve the document‑reading problems enterprises face every day. The team will continue expanding ParseBench, deepening the document types and failure modes it covers, and plans to introduce agentic evaluation — where parsers are scored end‑to‑end as part of a working agent.



 The dataset, evaluation code, and full scientific paper are publicly available:


-  Dataset: [HuggingFace](https://huggingface.co/datasets/llamaindex/ParseBench)
  -  Code &amp; evaluation: [GitHub](https://github.com/run-llama/ParseBench)
  -  Paper: [arXiv](https://arxiv.org/abs/2604.08538)