---
title: "AI SDR Onboarding: Cut Ramp Time to Days | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/building-smarter-ai-sdrs-with-llamaparse-how-11x-ai-shrinks-ramp-time-to-days"
category: "document-processing"
---

Content



- [ The Challenge  ](#the-challenge)
- [ Tool Selection  ](#tool-selection)
- [ Implementation  ](#implementation)
- [ Results &amp; Impact  ](#results-and-impact)
- [ Why LlamaIndex  ](#why-llamaindex)



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







 **About 11x**



 11x empowers sales teams to scale faster by deploying AI SDRs that handle outbound with precision, speed, and consistency. 11x’s AI agents like Alice master the company’s messaging, research leads, personalize campaigns, and book meetings—all without human intervention. Enterprise teams use 11x to reduce SDR ramp time, cut costs, and increase outbound efficiency at scale.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  The Challenge



 11x’s customers create solution offerings for automated outbound campaigns. Customer onboarding workflows typically involved writing individual sequences and personalization that involved deep customer research and importing context from external websites. However, 11x realized that these manual onboarding workflows were time-intensive and did not scale at mid-market and enterprise scale customers, where hundreds (or thousands) of offerings exist.



 An ideal experience would involve seamless onboarding - users drop all resources into a shared drive and the automated AI agent develops campaign messaging from the context provided—similar to how a new human SDR is onboarded. While great in theory, the 11x system had no way to ingest varied document types due to the multi-modal unstructured formats, including images, texts, charts, and more(PDFs, PowerPoints, call recordings etc).



##  Tool Selection



 At first, 11x evaluated building an in-house OCR pipeline but encountered a number of common challenges with DIY solutions. For example, a combination of traditional OCR techniques and Mistral required significant engineering efforts, resulted in quality issues, and needed dedicated resources that would maintain and update capabilities



 Ultimately, 11x selected to build their application leveraging Llamaparse because of:


-  **Broad file type support:** Wide range of file types supported including audio, PDFs, Docx and web pages. This was significantly larger than the file types other vendors supported
  -  **Superior developer experience**: Llamaparse offered a better developer experience - robust Typescript SDK, webhook based retrieval, and a roadmap aligned with future needs of 11x.
  -  **Exceptional Team Responsiveness**: The product worked out of the box, but there were some issues identified in the SDK. The LlamaIndex team addressed these in hours, unblocking testing at 11x.



##  Implementation


-  **Rapid Integration:** Llamaparse worked out-of-the-box for the functionality 11x needed. 11x engineering team were able to self serve and build Llamaparse into their product
  -  **Fine-Grained Control:** 11x tailored LlamaParse fidelity per document, toggling deep parsing (extract tables, images) when needed versus lightweight extraction for certain documents
  -  **Production Scaling:** The solution moved from prototype to production in 3 days with minimal engineering effort other than initial set up



##  Results &amp; Impact

  ![](https://cdn.sanity.io/images/7m9jw85w/production/16927878ad3c567cd5ed3ae6a97f682079dac581-1920x914.gif) Figure 1. 11x&#39;s onboarding agent, Alice, leverages Llamaindex to turn raw PDFs into AI-ready markdown to quickly train an automated SDR that is an expert on your brand.

 Post rolling out the knowledge base capability, 11x saw:


-  **Immediate Adoption:** Prior to document support, users hesitated to migrate to the new knowledge base experience. After launch, there was strong uptake across accounts
  -  **Enhanced Productivity:** 11x&#39;s product now auto-ingests diverse resources and crafts messaging at scale, enabling teams to roll out outbound campaigns faster and with higher quality.



##  Why LlamaIndex


-  **Comprehensive File Support:** Handles PDFs, PowerPoints, audio, web pages—and soon video—out of the box.
  -  **Developer-First SDK:** Webhook-based async processing and granular control over parsing parameters.
  -  **Scalable &amp; Extensible:** Future-proofed for emerging file types and advanced agentic workflows.
  -  **Rapid Support &amp; Onboarding:** Dedicated Slack assistance accelerated time to value.



 Satwik Singh - lead engineer at 11x noted “LlamaParse’s support of a wide variety of filetypes and its accuracy of parsing made it the best tool we tested in our evaluations. The LlamaIndex team was very responsive and we were off to the races within a day”



 **Next Steps**



 11x plans to deepen capabilities of their existing agents, as well as introduce new digital workers. They see LlamaIndex as a close partner for the future. Video interpretation capabilities from LlamaIndex is one. LlamaIndex Workflows to automate more stages of various knowledge workers is another.