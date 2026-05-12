---
title: "RAG Command-Line Tool: How To Use Llamaindex-CLI | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-the-llamaindex-retrieval-augmented-generation-command-line-tool-a973fa519a41"
category: "rag"
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







Want to try out retrieval-augmented generation (RAG) without writing a line of code? We got you covered! Introducing the new `llamaindex-cli` tool, installed when you `pip install llama-index` ! It uses [Chroma](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo.html) under the hood, so you’ll need to `pip install chromadb` as well.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



# How to use it

- **Set the **`**OPENAI_API_KEY**`** environment variable:** By default, this tool uses OpenAI’s API. As such, you’ll need to ensure the OpenAI API Key is set under the `OPENAI_API_KEY` environment variable whenever you use the tool.

$ export OPENAI_API_KEY=&amp;lt;api_key&amp;gt;**2. Ingest some files:** Now, you need to point the tool at some local files that it can ingest into the local vector database. For this example, we’ll ingest the LlamaIndex `README.md` file:

$ llamaindex-cli rag --files "./README.md"You can only specify a file glob pattern such as

$ llamaindex-cli rag --files "./docs/**/*.rst"**3. Ask a Question**: You can now start asking questions about any of the documents you’d ingested in the prior step:

$ llamaindex-cli rag --question "What is LlamaIndex?"
LlamaIndex is a data framework that helps in ingesting, structuring, and accessing private or domain-specific data for LLM-based applications. It provides tools such as data connectors to ingest data from various sources, data indexes to structure the data, and engines for natural language access to the data. LlamaIndex follows a Retrieval-Augmented Generation (RAG) approach, where it retrieves information from data sources, adds it to the question as context, and then asks the LLM to generate an answer based on the enriched prompt. This approach overcomes the limitations of fine-tuning LLMs and provides a more cost-effective, up-to-date, and trustworthy solution for data augmentation. LlamaIndex is designed for both beginner and advanced users, with a high-level API for easy usage and lower-level APIs for customization and extension.**4. Open a Chat REPL**: You can even open a chat interface within your terminal! Just run `llamaindex-cli rag --chat` and start asking questions about the files you’ve ingested.

# Customize it to your heart’s content!

You can customize `llamaindex-cli` to use any LLM model, even local models like Mixtral 8x7b through [Ollama](https://docs.llamaindex.ai/en/stable/examples/llm/ollama.html), and you can build more advanced query and retrieval techniques. [Check the documentation](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html) for details on how to get started.