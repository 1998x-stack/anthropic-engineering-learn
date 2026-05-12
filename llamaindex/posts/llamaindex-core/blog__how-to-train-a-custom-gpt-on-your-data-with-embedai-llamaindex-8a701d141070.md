---
title: "Custom GPT Training Guide: EmbedAI + LlamaIndex | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/how-to-train-a-custom-gpt-on-your-data-with-embedai-llamaindex-8a701d141070"
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







ChatGPT, developed by OpenAI, has changed the way we interact online. Being a general purpose chatbot, ChatGPT is limited to answering generic queries. But it becomes even more useful if you can get it to answer your questions specific to your business. To do that, you need to train ChatGPT on your data.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



[EmbedAI](https://www.thesamur.ai/) is a no-code platform for creating AI chatbots trained on your business data. This includes data sourced from web pages, PDFs, Notion documents, or YouTube videos, allowing EmbedAI to adapt to a wide range of information sources.

In this blog post, we’ll show you how we used [LlamaIndex](https://www.llamaindex.ai/) with [EmbedAI](https://thesamur.ai/) to enable us to train ChatGPT on your own data, helping you create a customized and effective AI chatbot tailored for your business needs.

# Chat with your data use-cases

There’s a variety of ways that a chatbot trained on your data could be helpful, including:

- **Customer Support Bot**: Manages frequently asked questions about a product, addressing customer support inquiries efficiently.
- **Company Search Engine**: Finds internal company documents and information fast, boosting workplace efficiency.
- **Personalized Learning Assistant**: Offers tailored educational support and study guidance based on specific course content.
- **Technical Support assistant**: Provides in-depth help for complex software issues, from troubleshooting to usage tips.
- **Healthcare Assistant**: Gives general health advice and information, based on medical literature and FAQs.
- **Finance Chatbot**: Assists with financial queries, offering advice on products, market trends, and investment strategies by training on financial data

Let’s delve into creating our own chat apps that integrate with various data sources like PDFs, Notion documents, videos, webpages, and more.

# Case 1: Custom ChatGPT for your site

To train ChatGPT on your website content, we need to scrape the content from all the relevant webpages. The steps to do this are:

- Extract all the URLs from your website, such as from your sitemap
- Include only relevant URLs which you need to train on
- Use SimpleWebPageReader from [LlamaIndex](https://www.llamaindex.ai/) to download the content from these URLs

Here’s some sample code to do that:

![](/blog/images/1*CJ-nuYuvaqLKlFntUlQucw.png)

Once the data is ready, an AI chatbot can be trained on these documents by using LlamaIndex’s VectorStoreIndex class.

To create a ChatGPT chatbot on your website without coding you can use EmbedAI as outlined below which uses LlamaIndex internally:

# Case 2: Custom ChatGPT for your PDF documents

If your business specific data is stored in PDF documents and you wish to create a chatbot that can surface the information in them we can do that with LlamaIndex using the PDFMiner library. This time the steps are:

- Upload your PDFs and store them in the cloud
- Install the PDFMiner library
- Fetch the uploaded PDFs and extract the document text using LlamaIndex loader

Here’s the code for creating an AI chatbot trained on PDF documents with LlamaIndex

![](/blog/images/1*AonaZTh1O3srF5V5JBKC9w.png)

If you want to create a ChatGPT chatbot on your PDF content without coding you can use EmbedAI as in the demo below which uses LlamaIndex internally

# Case 3: Custom ChatGPT for your videos

Often, valuable information is embedded in videos, which isn’t as accessible for users searching for information. However, by training an AI chatbot with this content, it can become an incredibly rich resource for your users, significantly enhancing their experience.

Let’s see how we can fetch the information from our youtube videos to train an AI chatbot using LlamaIndex. The steps are:

- Find your Channel ID
- Install `scrapetube` and pass it your channel ID to get your list of videos
- Install the Youtube transcript api and pass the video URLs from above to LlamaIndex loader to get a list of documents

The code looks like this:

![](/blog/images/1*uRWGg31kdaA5htoU76rI1g.png)

Now you can train an AI chatbot on these documents by using SimpleVectorIndex from LlamaIndex to create a ChatGPT bot trained on your youtube videos, and as before, you can use EmbedAI to create a chatbot with no code.

# Case 4: Custom ChatGPT for Notion

In many modern companies, a significant portion of their content is stored in Notion. As this content grows, quickly locating specific information becomes increasingly challenging. To address this, we can develop a chatbot for Notion to streamline the process of finding the necessary information.

Steps to prepare the data:

- Fetch an access token from Notion following [their instructions](https://www.notion.so/help/create-integrations-with-the-notion-api)
- Using the Notion API, parse data from Notion and generate LlamaIndex documents
- Train a chatbot on these using VectorStoreIndex

![](/blog/images/1*OZBl3ccIHbMP0HnqjYQ7qQ.png)

If you prefer a No-code way to train a chatbot on your Notion documents, you can use EmbedAI as in the demo below which uses LlamaIndex internally:

This doesn’t stop here. With EmbedAI, you can connect data from even more sources like Google Docs, Shopify or even use Zapier to connect with 6000+ tools and chat with their data. You can achieve this by choosing your specific data connector from [LlamaHub](https://llamahub.ai/)

# Challenges while building EmbedAI

- In EmbedAI, while connecting with a data source like Notion, the data can keep changing regularly which needs to be auto-refreshed. So the data needs a periodic refresh to add new documents or edit existing documents which needs to be handled internally. Likewise, when indexing website data it can be refreshed regularly. LlamaIndex makes it easy to handle these scenarios. LlamaIndex has a [guide to handling continuous ingestion](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline.html).
- Querying over tabular data in EmbedAI is a major issue when dealing with PDF content containing tables. Naive chunking can give sub-optimal results and even hallucinations. LlamaIndex provides [a guide on how to deal with PDFs containing both text and tables](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table.html#joint-tabular-semantic-qa-over-tesla-10k) and achieve optimal results while querying.
- Shopify integration in EmbedAI needed hybrid search, as we needed to search not only on product description but also on product metadata. Thus a combination of semantic search and keyword search is needed to obtain optimal results. LlamaIndex provides a simple framework to build a hybrid search application, such as in [this example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid.html).

# Custom trained chatbots can help your business

Training ChatGPT with your own data provides a significant advantage for your business. From enhancing customer support with bots trained on specific product knowledge to creating sophisticated company search engines, the applications are as diverse as they are impactful. LlamaIndex provides a lot of abstractions to help with building a custom chatbot trained on your data, and we use them heavily at EmbedAI. For those seeking a no-code solution to develop an AI chatbot tailored to their data, starting with EmbedAI is a straightforward option and we encourage you to [try it out](https://www.thesamur.ai/).