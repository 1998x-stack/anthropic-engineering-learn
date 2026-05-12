---
title: "Engineering Insights: Failure Modes That Break VLM-Powered OCR in Production"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/engineering-insights-failure-modes-that-break-vlm-powered-ocr-in-production"
category: "document-processing"
---

Content



- [ Outage 1: The &quot;Infinite Loop&quot; (Whitespace &amp; Repetition Errors)  ](#outage-1-the-infinite-loop-whitespace-and-repetition-errors)
- [ Outage 2: The &quot;Hard Stop&quot; (Recitation &amp; Content Blocking)  ](#outage-2-the-hard-stop-recitation-and-content-blocking)
- [ Engineering Solutions and Mitigation Strategies  ](#engineering-solutions-and-mitigation-strategies)
- [ Moving Forward  ](#moving-forward)



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







 At LlamaIndex, we’re passionate about building the infrastructure that empowers developers to create robust, context-aware LLM applications. Handling document processing using agentic processes and LLMs at scale brings unique engineering challenges.



 Recently, we experienced a few isolated LlamaParse service disruptions that provided valuable—if frustrating—insights into the unexpected ways large language models can behave in production. To be fully transparent with our community, we want to unpack what happened. Not all outages were attributable solely to LLM failures, and in many cases our engineering designs failed to consider shifting traffic patterns. We traced a number of the isolated outages back to two phenomena that just happened to strike our agentic document OCR/document parsing pipelines around the same time: Repetition Loops and Recitation Errors.



 While they sound similar, they are structurally different problems with entirely different root causes, API behaviors, and mitigation strategies. Here is a deep dive into what went wrong and how we fixed it.



###  **Outage 1: The &quot;Infinite Loop&quot; (Whitespace &amp; Repetition Errors)**



 The first issue we encountered was a classic case of resource exhaustion, triggered by repetition or token probability collapse. [[ref](https://www.nature.com/articles/s41586-024-07566-y)]



 In agentic workflows, an LLM processes text and generates an output that often serves as the input for the next agent in the chain. Sometimes, particularly when dealing with messy real-world documents containing unconventional formatting, an LLM can get stuck in a localized loop. It begins outputting repeating characters—often excessive whitespace (multiple spaces, newlines, tabs) or repetitive boilerplate phrasing. Because LLMs use their own recent output as context for the next token, this repetition becomes self-reinforcing. This problem has been significantly exacerbated by the introduction of always-on thinking models, and is more common for systems such as LlamaParse, handling binary and raw document content, to run into.



 To illustrate the problem, we have seen:


-  When Agent A outputs 500 lines of empty space, Agent B spends valuable time computating it, and might even adopt that pattern itself.
  -  Thinking models are also especially prone to looping
 Wait I should maybe consider that [....] Wait I should consider this [...] ....

    -  Even in non-repetition cases, LLM tokenizers can represent 50+ empty space characters within a single token – polluting agent context as it gets passed down to subsequent steps. [[ref](https://platform.openai.com/tokenizer)]



 **How this surfaces across providers:** When a model falls into a repetition loop, it almost never stops voluntarily. It keeps generating until it hits the hard limit of the context window or your configured maximum tokens.


-  **OpenAI:** You will typically see a response return with finish_reason: &quot;length&quot;. This means the model hit the max_tokens limit or the overall context limit before naturally finishing its thought.
  -  **Anthropic (Claude):** Similarly, the model will exhaust its token output limit. Without strict max_tokens constraints or repetition penalties configured, it will stream repetitive content until the hard cap is reached. [[ref](https://platform.claude.com/docs/en/api/messages#message.stop_reason)]
  -  **Gemini:** The API will return finishReason: MAX_TOKENS, indicating the generation was forcibly cut off because it hit the token ceiling. [[ref](https://ai.google.dev/api/generate-content#candidate)]



 **The LlamaParse Impact:** This initially caused an isolated outage because these repetition loops can lead to sudden, massive spikes in latency and token usage. This cascaded beyond the isolated jobs experiencing reasoning loops. Agent workflows across our fleet stalled out waiting for massive blocks of whitespace to generate, tying up concurrent connections and exhausting system resources across our network layer.



###  **Outage 2: The &quot;Hard Stop&quot; (Recitation &amp; Content Blocking)**



 The second issue was caused by **Recitation Errors**. While repetition is the model getting confused, recitation is the model&#39;s safety filters working *too* well.



 LLM providers implement strict content filters to prevent their models from regurgitating exact training data, copyrighted material, or proprietary technical standards. If you ask an LLM to extract or structure data from a source document that closely resembles copyrighted text (like a public law, a technical standard, or a widely published article), the provider&#39;s internal safety classifier might flag the output as a copyright violation and abruptly kill the generation. We believe that this class of error will become increasingly common as the model providers deal with increasing litigation, regulation, and discovered attack vectors.



 **How this surfaces across providers:** Unlike a repetition loop that drags on forever, a recitation block is an immediate, hard stop.


-  **OpenAI:** You will see a finish_reason: &quot;content_filter&quot;. While this can flag various safety violations, it is the standard finish reason when OpenAI&#39;s system detects and interrupts the stream due to copyright/recitation policies.
  -  **Anthropic:** Claude&#39;s API will typically block the request outright with an explicit refusal in the text, or return an error indicating a violation of their Acceptable Use Policy (AUP) regarding copyrighted material. [[ref](https://privacy.claude.com/en/articles/10023638-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error, https://github.com/anthropics/claude-code/issues/2111)]
  -  **Gemini:** The Google Gen AI SDK will return a highly specific error: finishReason: &quot;RECITATION&quot;. This explicitly means token generation was stopped because the content potentially contains copyright violations or unauthorized citations. [[ref](https://ai.google.dev/gemini-api/docs/troubleshooting#recitation-issue, https://github.com/google/generative-ai-docs/issues/257)]



 **The LlamaParse Impact:** In our agentic document processing, users frequently ingest highly structured, boilerplate, or standardized text. When intermediate agents attempted to extract and pass this text down the chain, provider-level recitation filters misidentified our legitimate RAG (Retrieval-Augmented Generation) extractions as copyright violations. This resulted in sudden None or abruptly truncated outputs, causing downstream agents to crash and resulting in an isolated outage for specific ingestion pipelines. This can cascade into system-wide 429 and 503 responses from model providers as LlamaParse attempts to retry with different temperatures settings, since model providers often still charge and bill for recitation errors. (Don’t ask us how much money we’ve burnt on this…)



###  **Engineering Solutions and Mitigation Strategies**



 Once we decoupled these two issues, we implemented targeted solutions for both.



 **1. Mitigating Repetition Loops (The &quot;Length&quot; Problem)**


-  **Streaming, Strict max_tokens and Timeouts:** We implemented aggressive hard caps on agent execution times and token outputs, and terminated response streams when repetition was detected. We also implemented continuation routines for jobs with genuinely longer context needs.
  -  **Whitespace Sanitization:** We built robust pre- and post-processing regex filters to collapse excessive spaces and newlines between agent handoffs.
  -  **Fairness &amp; Concurrency: **We built out additional fairness and resource sharing mechanisms between customers and selected LLM model providers.
  -  **Model Cutover:** We enabled specific model fallbacks, as changing models often addresses unique failure scenarios like repetition.
  -  **Dynamic Temperature Adjustment:** When repetition is flagged, our fallback mechanism automatically retries the request with a different temperature parameter. By injecting a small amount of entropy on the retry, we hope to steer LLMs away from these spiraling states. [[ref](https://www.statsig.com/perspectives/tempsettingscontroloutputrandomness)]



 Things we considered but did not try


-  **Parameter Tuning:** Where supported by the provider, we are utilizing presence_penalty and frequency_penalty (or repetition_penalty) to mathematically discourage models from repeating the same tokens. This is not feasible where the actual content we want to output may be repetitive in nature and we want to remain faithful to the original data (i.e. when transcribing documents).



 **2. Mitigating Recitation Blocks (The &quot;Content Filter&quot; Problem)**


-  **Finish Reason Routing:** Our framework previously parsed the finish_reason of every API call. If we detect RECITATION (Gemini) or content_filter (OpenAI), we immediately catch the exception and propagate upstream instead of crashing the pipeline, and retry. We updated our retry policies to consider nested retry conditions to prevent nested retry explosion.
  -  **Dynamic Temperature Adjustment:** When a recitation block is flagged, our fallback mechanism automatically retries the request with a different temperature parameter. Similar to what was mentioned above, lower temperatures force models toward highly deterministic, verbatim outputs—which is exactly what triggers exact-match copyright classifiers. By injecting a small amount of entropy on the retry, we encourage the model to naturally paraphrase the extracted data, effectively bypassing the filter while still preserving the core factual information.



###  **Moving Forward**



 The failure conditions we have observed are not unique to a single model provider, and are exacerbated by LlamaParse’s specific document-heavy input and spiky low-latency traffic patterns.



 These failure scenarios (repetition and content filtering) are an artifact that remind us that LLMs are not magic bullets. We are constantly evaluating closed source and open source models for improvements not just on benchmarks, but on real world use and failure scenarios like we have discussed here. This was a major motivation for why we released [LlamaParse V2](https://www.llamaindex.ai/blog/introducing-llamaparse-v2-simpler-better-cheaper): to make sure we could provide the best reliability and accuracy on both closed-source and open-weight models regardless of announced benchmarks.



 Building agentic systems requires us to be defensive engineers. We have to design for the reality that LLMs will sometimes spiral into infinite loops, and provider-level safety filters will sometimes abruptly block perfectly legitimate tasks. At the end of the day, we’re glad to say that LlamaParse is now significantly more resilient to the unpredictable nature of hosted LLM APIs.