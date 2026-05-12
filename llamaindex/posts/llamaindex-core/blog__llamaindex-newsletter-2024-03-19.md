---
title: "LlamaIndex Newsletter 2024-03-19"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-03-19"
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







 Greetings, LlamaIndex enthusiasts! 🦙



 Welcome to another exciting weekly update from the world of LlamaVerse!



 We have an amazing news for you from LlamaIndex. We&#39;ve officially launched LlamaParse, a GenAI-native document parsing solution. With state-of-the-art table and chart extraction, natural language steerable instructions, and compatibility with over a dozen document types, LlamaParse excels in creating accurate RAG applications from complex documents. After a successful private preview with 2k users and 1M pages parsed, it&#39;s now ready to transform your document handling. Check out our [launch post](https://www.llamaindex.ai/blog/launching-the-first-genai-native-document-parsing-platform) for all the details!



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



 🤩 **The highlights:**


-  **New observability with Instrumentation:** Enhanced developer workflow with a new Instrumentation module for improved observability. [Docs](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation.html), [Tweet](https://x.com/llama_index/status/1768730443921396220?s=20).
  -  **LlamaParse accepts natural language parsing instructions**: Easily extract math snippets from PDFs into LaTeX with LlamaParse. [Blogpost](https://www.llamaindex.ai/blog/launching-the-first-genai-native-document-parsing-platform), [Tweet](https://x.com/llama_index/status/1768443551267049492?s=20).
  -  **Financial Data Parsing:** Transform PowerPoint parsing, utilizing LlamaParse to extract and interpret complex financial data from .pptx files, enabling detailed and accurate financial analysis. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/other_files/demo_ppt_financial.ipynb), [Tweet](https://x.com/llama_index/status/1768303288381030408?s=20).



 **✨ Feature Releases and Enhancements:**


-  We introduced LlamaIndex v0.10.20, featuring our new Instrumentation module, a leap in observability that simplifies developer workflows by providing a module-level dispatcher, reducing the need for individual callback managers and facilitating comprehensive handler sets across your application. [Docs](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation.html), [Tweet](https://x.com/llama_index/status/1768730443921396220?s=20).
  -  We have launched parsing by prompting feature in LlamaParse to properly extract out any math snippets from PDFs into LaTex which helps you to plug easily into your RAG pipeline. [Blogpost](https://www.llamaindex.ai/blog/launching-the-first-genai-native-document-parsing-platform), [Tweet](https://x.com/llama_index/status/1768443551267049492?s=20).
  -  We have launched an advanced RAG pipeline for Financial PowerPoints, using LlamaParse to tackle the challenge of parsing .pptx files. Our solution accurately extracts slides, including text, tables, and charts, enabling precise question-answering over complex financial data. [Notebook](https://github.com/run-llama/llama_parse/blob/main/examples/other_files/demo_ppt_financial.ipynb), [Tweet](https://x.com/llama_index/status/1768303288381030408?s=20).
  -  We collaborated with langfuse to launch open-source observability for your RAG pipeline, enhancing your application with integrated tracing, prompt management, and evaluation in just two lines of code. [Blogpost](https://www.llamaindex.ai/blog/one-click-open-source-rag-observability-with-langfuse), [Docs](https://docs.llamaindex.ai/en/stable/examples/callbacks/LangfuseCallbackHandler.html), [Tweet](https://x.com/llama_index/status/1769790083564208218?s=20).
  -  Search-in-the-Chain: a method by Shicheng Xu et al., is now integrated into LlamaIndex, enhancing question-answering with an advanced system that interleaves retrieval and planning. This approach verifies each reasoning step in a chain, allowing for dynamic replanning and application in various agent reasoning contexts. [LlamaPack](https://llamahub.ai/l/llama-packs/llama-index-packs-searchain?from=), [Tweet](https://x.com/llama_index/status/1769035278063399208?s=20)



 **🎥 Demos:**


-  Home AI, a tool created with create-llama, to help home searches by using LLMs to automate the parsing of complex property disclosures, enabling users to filter searches with unprecedented detail and efficiency. [Blogpost](https://devpost.com/software/home-ai), [Code](https://github.com/2sunflower33/homeai), [Tweet](https://x.com/llama_index/status/1767289805719978288?s=20).



 **🗺️ Guides:**


-  [Guide](https://github.com/tensorsense/Retrieval-Framework/blob/main/hierarchical_retrieval.ipynb) to using LlamaIndex and Mathpix to parse, index, and query complex mathematics within scientific papers, detailing steps from parsing tables and extracting images to indexing in a RAG app and answering questions with precise LaTeX outputs, to showcase hierarchical retrieval technique.



 **✍️ Tutorials:**


-  [Thomas Reid](https://twitter.com/taupirho)’s [tutorial](https://ai.gopubby.com/llamaparse-rag-beats-all-comers-60948c6cc0e4) on using LlamaParse can help properly extract text from a Tesla quarterly filings.
  -  [Sudarshan Koirala](https://twitter.com/mesudarshan) [video tutorial](https://www.youtube.com/watch?v=w7Ap6gZFXl0) on RAG with LlamaParse, Qdrant, and Groq.
  -  Kyosuke Morita [tutorial](https://pub.towardsai.net/rag-based-job-search-assistant-98dd72c98fbd) showing how to match a candidate to jobs based on their CV with LlamaParse + LlamaIndex.
  -  [Cobus Greyling](https://twitter.com/CobusGreylingZA) [tutorial](https://cobusgreyling.medium.com/agentic-rag-context-augmented-openai-agents-578e96212bc0) on Agentic RAG: Context-Augmented OpenAI Agents.
  -  [Roey Ben Chaim](https://twitter.com/RoeyBC)’s [tutorial](https://www.llamaindex.ai/blog/pii-detector-hacking-privacy-in-rag) on PII Detector: hacking privacy in RAG.



 🎥 **Webinars:**


-  [Webinar](https://www.youtube.com/watch?v=Bhnq8grQm5Y) with Charles Packer, lead author of MemGPT on Long-Term, Self-Editing Memory with MemGPT



 📅 Events:


-  We are hosting a RAG [meetup](https://www.meetup.com/paris-retrieval-augmented-generation-group/events/299374545/) in Paris on March 27th featuring talks on advanced RAG strategies, building a RAG CLI, and the significance of open-source RAG in business.