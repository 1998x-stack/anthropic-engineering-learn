---
title: "LlamaParse V2: Simpler, Better &amp; Cheaper Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-llamaparse-v2-simpler-better-cheaper"
category: "document-processing"
---

Content



- [ What&#39;s New in v2  ](#whats-new-in-v2)
- [ Tiers Replace Parsing Modes  ](#tiers-replace-parsing-modes)
- [ What About the API?  ](#what-about-the-api)
- [ Why This Matters  ](#why-this-matters)
- [ Get Started  ](#get-started)



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



   26



 At LlamaIndex, we’re pushing the frontiers of document understanding research, translating scientific advances into consistent improvements across our core document ingestion APIs for millions of users. Today, we mark a major milestone in that journey and are excited to announce LlamaParse v2: a major update that introduces core improvements to our parsing technology with updated price points.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  What&#39;s New in v2



 LlamaParse v2 brings a number of improvements to developers building high-quality document ingestion pipelines:


-  Simpler tier-based configuration
  -  Stable versions with long-term support
  -  Improved performance with reduced pricing



 The result for our users is higher accuracy, lower costs, and production-ready parsing in minutes, not hours.



##  Tiers Replace Parsing Modes



 LlamaParse v1 required a deep understanding of parsing configs, choosing modes, LLM providers, and dozens of parameters, just to get started. We learned from user feedback that most users preferred less complexity and felt the extra choices burdened engineering teams, favoring a simpler approach.



 LlamaParse v2 flips that model. Instead of tuning internals, you focus on outcomes: the level of performance you need, what content matters in your documents, and how you want the output structured. LlamaParse takes care of the rest, automatically routing to the optimal models while still offering version control when stability matters.



 Instead of choosing between parsing modes and model providers, v2 introduces a simple tier system with version control. Pick the tier that matches your use case—**Fast**, **Cost Effective**, **Agentic**, or **Agentic Plus**—and optionally pin to a specific version for production consistency.



 We support all major model providers under the hood, but now you get better results without the decision overhead.



 This abstraction also enables us to move faster. As we integrate new models and parsing techniques, users on the `latest`  version automatically benefit from improvements without changing any code. Meanwhile, users who need stability can pin to specific versions. This means we can ship performance upgrades and new capabilities more frequently—without breaking production workflows.



 **The new tiers:**


-  **Fast** (1 credit/page): Perfect for simple, text-heavy documents
  -  **Cost Effective** (3 credits/page): Balanced performance for everyday use
  -  **Agentic** (10 credits/page): Advanced parsing for complex layouts and multimodal content
  -  **Agentic Plus** (45 credits/page): Maximum accuracy for mission-critical documents

  ![](https://cdn.sanity.io/images/7m9jw85w/production/a52e52df122017de8f736e24a6aa22205d300617-1224x1184.png)

####  Significant Performance and Cost Improvements



 We&#39;re not just simplifying LlamaParse, we&#39;re also improving our core parsing modes to offer better accuracy, lower latency, and more cost-effective parsing modes at every price point. We’re also re-introducing a new version of our ‘Fast mode’ to offer industry-best accuracy at an entry-level price point.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/1f405d534685c33e1a3dfca387f8f17757f80c4e-3504x2064.png)

 **Cost Effective tier**:


-  Improved accuracy
  -  Same 3 credits/page pricing as the previous Cost-efficient preset



 **Agentic tier**:


-  Improved faithfulness and reduced hallucinations
  -  Better performance with significantly less dropped content
  -  Better handling of complex documents at the same 10 credits/page



 **Agentic Plus tier**:


-  50% price reduction with comparable accuracy
  -  Equivalent accuracy to the previous Agentic Plus



####  Version Control for Production Stability



 LlamaParse users can now also lock their default parsing behavior to a specific version (using `YYYY-MM-DD`  format) or always use `latest`  for automatic improvements. This means you can productionize with confidence, and your parsing won&#39;t change unexpectedly when you&#39;re not ready for it.



###  What About the API?



 We will be releasing updates to the LlamaParse API in the new year, which will allow you to focus on *what* you want parsed, rather than *how* to parse. Stay tuned for API v2 release in the new year!



###  Why This Matters



 **For builders**: You no longer need to become a parsing expert to get production-quality results. Choose a tier, optionally lock a version, and let LlamaParse handle the complexity.



 **For applications**: More targeted parsing means better retrieval and context for agents, cleaner data extraction, and documents structured exactly how your workflow expects them—at better prices and with improved performance.



 **For production deployments**: Version pinning gives you control over when parsing behavior changes, eliminating surprises in production.



##  Get Started


-  Learn more about [LlamaParse](https://developers.llamaindex.ai/python/cloud/llamaparse/getting_started/) and the new [Tiers](https://developers.llamaindex.ai/python/cloud/llamaparse/tiers/)
  -  [Sign up to LlamaParse ](https://cloud.llamaindex.ai/)to get started