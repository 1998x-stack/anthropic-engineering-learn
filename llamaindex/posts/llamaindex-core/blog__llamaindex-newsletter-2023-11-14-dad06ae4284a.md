---
title: "LlamaIndex Newsletter 2023–11–14"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-14-dad06ae4284a"
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







Hello Llama Friends 🦙

LlamaIndex is 1 year old this week! 🎉 To celebrate, we’re taking a stroll down memory lane on our [blog](/llamaindex-turns-1-f69dcdd45fe3) with twelve milestones from our first year. Be sure to check it out.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Last week we had a blast with all the new things from OpenAI Dev day to learn and explore at LlamaIndex. There was a [special edition newsletter](/llamaindex-news-special-edition-openai-developer-day-e955f16db4e2) with the things we released the same day as the conference, but this week’s newsletter is full of follow-up releases and explorations — don’t miss our slide deck summing up all the new features!

As always, if you’ve got a cool project or a video to share we’d love to see it! Just drop us a line at [news@llamaindex.ai](mailto:news@llamaindex.ai).

🤩 **First, the highlights:**

- **Multi-Modal RAG Stack:** we unveiled Multi-Modal RAG ****for complex Q&amp;A on documents and images, with new text/image queries and retrieval solutions. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/gpt4v_multi_modal_retrieval.ipynb), [Tweet](https://x.com/jerryjliu0/status/1723076174698672417?s=20), [Blog post](/multi-modal-rag-621de7525fea).
- **OpenAIAssistantAgent Abstractions:** we released new abstractions to connect OpenAI Assistant API with any vector database. [Docs](https://t.co/W78d2WCpnn), [Tweet](https://twitter.com/jerryjliu0/status/1722276583883657388?s=20).
- **Parallel Function Calling:** we enhanced our data extraction and tool execution using OpenAI’s parallel function calling. [Tweet](https://x.com/llama_index/status/1722686015276753073?s=20).
- **MechGPT Project:** Prof. [**Markus J. Buehler**](https://twitter.com/ProfBuehlerMIT)’s work merges LLM fine-tuning with knowledge graphs for scientific discovery. [Tweet](https://x.com/llama_index/status/1723379654550245719?s=20), [Paper](https://t.co/l8J55BqUfn).
- **Feature Slide Deck:** Released a [slide deck](https://docs.google.com/presentation/d/1i1bUDWXeCYPd6O8pio57ST6AQIuSTWXM3rvvkvrBpBM/edit#slide=id.p) with 10+ new features and guides post-OpenAI updates.

**✨ Feature Releases and Enhancements:**

- We introduced a multi-modal RAG stack for complex document and image QA, featuring text/image queries, joint text/ image embeddings, and versatile storage and retrieval options. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/multi_modal/gpt4v_multi_modal_retrieval.ipynb), [Tweet](https://x.com/jerryjliu0/status/1723076174698672417?s=20), [Blog post](/multi-modal-rag-621de7525fea).
- We now offer experimental GPT-4-vision support in [chat.llamaindex.ai](http://chat.llamaindex.ai) . Users can now upload images for enhanced chatbot interactions. [Tweet](https://x.com/llama_index/status/1723120887988384177?s=20).
- We integrated OpenAI’s parallel function calling for efficient extraction of structured data from unstructured text and improving tool execution with agents. [Tweet](https://x.com/llama_index/status/1722686015276753073?s=20).
- We introduced `**OpenAIAssistantAgent**` abstractions for seamless connection of OpenAI Assistants API with your chosen vector database. [Docs](https://t.co/W78d2WCpnn), [Tweet](https://twitter.com/jerryjliu0/status/1722276583883657388?s=20).
- We introduced a new agent leveraging OpenAI Assistants API with features like in-house code interpretation, file retrieval, and function calling for external tools integration. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/openai_assistant_agent.ipynb), [Tweet](https://x.com/llama_index/status/1721949693754917035?s=20).

**🎥** Demos:

- MechGPT by Professor [**Markus J. Buehler**](https://twitter.com/ProfBuehlerMIT) showcases the integration of LLM fine-tuning and knowledge graph creation with LlamaIndex, leading to interesting insights in cross-disciplinary scientific research and hypothesis generation. [Tweet](https://x.com/llama_index/status/1723379654550245719?s=20), [Paper](https://t.co/l8J55BqUfn).

**🗺️ Guides:**

- We released a concise [slide deck](https://docs.google.com/presentation/d/1i1bUDWXeCYPd6O8pio57ST6AQIuSTWXM3rvvkvrBpBM/edit#slide=id.p) that aggregates over 10+ newly shipped features, guides, and analyses, complete with links to accompanying notebooks for developer use based on OpenAI’s recent updates.
- We also released a full [cookbook](https://docs.llamaindex.ai/en/latest/examples/agent/openai_assistant_query_cookbook.html) showing how you can build advanced RAG with the Assistants API — beyond just using the in-house Retrieval tool.
- We produced a [guide](https://docs.llamaindex.ai/en/latest/examples/agent/openai_retrieval_benchmark.html) on evaluating the OpenAI Assistant API vs RAG with LlamaIndex.
- Here’s a [guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/response_synthesizers/long_context_test.ipynb) on evaluating How well long-context LLMs (gpt-4-turbo, claude-2) recall specifics in BIG documents? (&gt;= 250k tokens).
- Here’s another [guide](https://github.com/run-llama/llama_index/blob/main/docs/examples/llm/openai_json_vs_function_calling.ipynb) that highlights how function calling simplifies structured data extraction, while JSON mode ensures format correctness without schema enforcement.
- Finally, we released a guide to craft a GPT Builder, enabling an agent to programmatically construct another task-specific agent. This builder streamlines the creation of systems for specific functions. [Notebook](https://github.com/run-llama/llama_index/blob/main/docs/examples/agent/agent_builder.ipynb), [Tweet](https://x.com/jerryjliu0/status/1721639447207583882?s=20).

**✍️ Tutorials:**

- [**Bhavesh Bhat**](https://twitter.com/_bhaveshbhatt) gave us a [tutorial](https://twitter.com/_bhaveshbhatt/status/1721551513103839392) on How to Chat with YouTube Videos Using LlamaIndex.
- [David Garnitz](https://twitter.com/DGarnitz)’s tutorial blog explores the use of VectorFlow alongside ArizePhoenix, Weaviate, and LlamaIndex to manage large data sets.
- [Harshad Suryawanshi](https://harshadsuryawanshi.medium.com/)’s [tutorial](/building-my-own-chatgpt-vision-with-palm-kosmos-2-and-llamaindex-9f9fdd13e566) covers Building My Own ChatGPT Vision with PaLM, KOSMOS-2 and LlamaIndex.
- [Sudarshan Koirala](https://twitter.com/mesudarshan)’s made a [tutorial](https://www.youtube.com/watch?v=LRP-0iSVQaA) on Creating OpenAI Assistant Agent with LlamaIndex.
- Our own [Ravi Theja](https://twitter.com/ravithejads) released his [tutorial](/boosting-rag-picking-the-best-embedding-reranker-models-42d079022e83) on Boosting RAG with Embeddings &amp; Rerankers.

**🎥** Webinars:

- Check out our [webinar](https://www.youtube.com/watch?v=upPK6pRbZYQ) with Dan Shipper, CEO of [every](http://every.to/) to talk about the implications of OpenAI’s release updates.
- A second [webinar](https://www.youtube.com/watch?v=rBpZvMAim5E) with Victoria Lin, author of the RA-DIT paper on Fine-tuning + RAG.
- Last but not least, [Mayo Oshin](https://twitter.com/mayowaoshin)’s [webinar](https://www.youtube.com/watch?v=xT6JpDELKPg&amp;t=61s) with [Jerry Liu](https://twitter.com/jerryjliu0) on How to Analyze Tables In Large Financial Reports Using GPT-4.