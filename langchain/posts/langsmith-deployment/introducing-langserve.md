---
title: "Introducing LangServe, the best way to deploy your LangChains"
author: "LangChain Accounts"
date: "2023-10-12"
url: "https://www.langchain.com/blog/introducing-langserve"
---

Company AnnouncementsLangChain

# Introducing LangServe, the best way to deploy your LangChains

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 12, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb12e90227306de7e251b_Screenshot-2023-10-12-at-13.13.48-1.png)We think the [LangChain Expression Language](https://blog.langchain.com/langchain-expression-language/) (LCEL) is the quickest way to prototype the brains of your LLM application. The next exciting step is to ship it to your users and get some feedback! Today we&#x27;re making that a lot easier, launching [LangServe](https://github.com/langchain-ai/langserve?ref=blog.langchain.com). LangServe is the easiest and best way to deploy any any LangChain chain/agent/runnable.

Important Links:

- [LangServe Github Repo](https://github.com/langchain-ai/langserve?ref=blog.langchain.com)
- [Example repo](https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.com) (deploy on GCP)
- [Replit Template](https://github.com/langchain-ai/langserve-replit-template?ref=blog.langchain.com)

## Why it exists

Whether you’re building a customer-facing chatbot, or an internal tool powered by LLMs, you’ll probably start by building a prototype (maybe in a Jupyter notebook), and iterate on it until it’s good enough to get people using it.

And that’s where LangServe comes in, we’ve taken our experience scaling applications in production, and made it available as a python package you can use for your own LLM apps.

💡

Your Idea + LCEL = Prototype+ LangServe = Production-ready API+ [Hosting Provider] = Live deployment+ LangSmith Tracing = Monitor your production deployment

We&#x27;ve been hesitant to release anything around deployment because, to be honest, we weren&#x27;t entirely sure what value we could add. With some key improvements and additions over the past few months, we now believe that LangServe can provide real value. Most of the features we highlight in the release today make it significantly easier to go from prototype to production and get a production ready API. Over next few weeks, we&#x27;ll be adding more features that add in new functionality (as opposed to just making it easier to create an API).

We&#x27;ve used LangServe to deploy [ChatLangChain](https://blog.langchain.com/building-chat-langchain-2/) and [WebLangChain](https://blog.langchain.com/weblangchain/) over the past week, and this has help battle test it.

## The road to LangServe

The journey to build LangServe really started a few months ago when we launched LCEL and the Runnable protocol. This was designed from day 1 to support putting prototypes in production, with no code changes, from the simplest “prompt + LLM” chain to the most complex chains (we’ve seen folks successfully running in production LCEL chains with 100s of steps). To highlight a few:

- first-class support for streaming: when you build your chains with LCEL you get the best possible time-to-first-token (time elapsed until the first chunk of output comes out). For some chains this means eg. we stream tokens straight from an LLM to a streaming output parser, and you get back parsed, incremental chunks of output at the same rate as the LLM provider outputs the raw tokens. We’re constantly improving streaming support, recently we added a [streaming JSON parser](https://twitter.com/LangChainAI/status/1709690468030914584?ref=blog.langchain.com), and more is in the works.
- first-class async support: any chain built with LCEL can be called both with the synchronous API (eg. in your Jupyter notebook while prototyping) as well as with the [asynchronous API](https://python.langchain.com/docs/expression_language/interface?ref=blog.langchain.com#async-invoke) (eg. in a LangServe server). This enables using the same code for prototypes and in production, with great performance, and the ability to handle many concurrent requests in the same server.
- optimized parallel execution: whenever your LCEL chains have steps that can be [executed in parallel](https://python.langchain.com/docs/expression_language/how_to/map?ref=blog.langchain.com) (eg if you fetch documents from multiple retrievers) we automatically do it, both in the sync and the async interfaces, for the smallest possible latency.
- support for retries and fallbacks: more recently we’ve added support for [configuring retries and fallbacks](https://python.langchain.com/docs/expression_language/how_to/fallbacks?ref=blog.langchain.com) for any part of your LCEL chain. This is a great way to make your chains more reliable at scale. We’re currently working on adding streaming support for retries/fallbacks, so you can get the added reliability without any latency cost.
- accessing intermediate results: for more complex chains it’s often very useful to access the results of intermediate steps even before the final output is produced. This can be used let end-users know something is happening, or even just to debug your chain. We’ve added support for [streaming intermediate results](https://x.com/LangChainAI/status/1711806009097044193?s=20&amp;ref=blog.langchain.com), and it’s available on every LangServe server.
- [input and output schemas](https://x.com/LangChainAI/status/1711805322195861934?s=20&amp;ref=blog.langchain.com): this week we launched input and output schemas for LCEL, giving every LCEL chain Pydantic and JSONSchema schemas inferred from the structure of your chain. This can be used for validation of inputs and outputs, and is an integral part of LangServe.

To this ever-growing list of the benefits of building with LCEL today we’re adding LangServe, which takes advantage of all these to give you the fastest path from LLM idea to scalable LLM app in production.

## How it works

First we create our chain, here using a conversational retrieval chain, but any other chain would work. This is the `my_package/chain.py` file.

`&quot;&quot;&quot;A conversational retrieval chain.&quot;&quot;&quot;

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

vectorstore = FAISS.from_texts(
    [&quot;cats like fish&quot;, &quot;dogs like sticks&quot;],
    embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

model = ChatOpenAI()

chain = ConversationalRetrievalChain.from_llm(model, retriever)`

Then, we pass that chain to `add_routes`. This is the `my_package/server.py` file.

`#!/usr/bin/env python
&quot;&quot;&quot;A server for the chain above.&quot;&quot;&quot;

from fastapi import FastAPI
from langserve import add_routes

from my_package.chain import chain

app = FastAPI(title=&quot;Retrieval App&quot;)

add_routes(app, chain)

if __name__ == &quot;__main__&quot;:
    import uvicorn

    uvicorn.run(app, host=&quot;localhost&quot;, port=8000)`

That&#x27;s it! This gets you a scalable python web server with

- Input and Output schemas automatically inferred from your chain, and enforced on every API call, with rich error messages
- `/docs` endpoint serves API docs with JSONSchema and Swagger (insert example link)
- `/invoke` endpoint that accepts JSON input and returns JSON output from your chain, with support for many concurrent requests in the same server
- `/batch` endpoint that produces output for several inputs in parallel, batching calls to LLMs where possible
- `/stream` endpoint that sends output chunks as they become available, using [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events?ref=blog.langchain.com) (same as OpenAI Streaming API)
- `/stream_log` endpoint for streaming all (or some) intermediate steps from your chain/agent
- Built-in (optional) tracing to [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com), just add your API key as an environment variable
- Support for hosting multiple chains in the same server under separate paths
- All built with battle-tested open-source Python libraries like FastAPI, Pydantic, uvloop and asyncio.

## Deployment

After an API is created, the next step is to deploy it on a hosting platform. We&#x27;re launching with two examples:

- [GCP](https://github.com/langchain-ai/langserve/tree/main?ref=blog.langchain.com#deployment): Deploy to GCP Cloud Run with one command.
- [Replit](https://replit.com/@LangChain/langserve-replit-template?ref=blog.langchain.com): Deploy (and also build) on Replit. This can be done by cloning an [existing Github repo](https://github.com/langchain-ai/langserve-replit-template?ref=blog.langchain.com).

We will add instructions and templates for other platforms. If you have suggestions for what you want to see, please let us know.

## See it in action

Let&#x27;s see it in action. We have deployed [this repo](https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.com) as an example.

The API docs are available [here](https://langserve-launch-example-vz4y4ooboq-uc.a.run.app/docs?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb12e90227306de7e251b_Screenshot-2023-10-12-at-13.13.48-1.png)

We can stream a response:

`curl https://langserve-launch-example-vz4y4ooboq-uc.a.run.app/stream -X POST -H &quot;Content-Type: application/json&quot; --data &#x27;{&quot;input&quot;: {&quot;topic&quot;: &quot;bears&quot;}}&#x27;`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb12e90227306de7e2521_langserve-stream-gif.gif)

## What&#x27;s next

We&#x27;re always improving LangChain/LCEL, just recently we&#x27;ve added support for [input and output schemas](https://x.com/LangChainAI/status/1711805322195861934?s=20&amp;ref=blog.langchain.com), [streaming intermediate results](https://x.com/LangChainAI/status/1711806009097044193?s=20&amp;ref=blog.langchain.com), and a [streaming JSON parser](https://twitter.com/LangChainAI/status/1709690468030914584?ref=blog.langchain.com).

We&#x27;ll also be working to add features over the next few weeks: the next two we are adding are (1) a playground to experiment with different prompts/retrievers for deployed chains, (2) a way to save multiple configurations for the same chain.

Let us know what you&#x27;d like to see next!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)