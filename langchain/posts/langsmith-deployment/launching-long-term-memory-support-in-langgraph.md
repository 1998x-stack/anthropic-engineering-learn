---
title: "Launching Long-Term Memory Support in LangGraph"
author: "LangChain Accounts"
date: "2024-10-08"
url: "https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph"
---

LangGraphCompany Announcements

# Launching Long-Term Memory Support in LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 8, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf45765e3cf29f5ff10a_Long-term-memory-blog-post--3-.png)Today, we are excited to announce the first steps towards long-term memory support in LangGraph, available both in [Python](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/?ref=blog.langchain.com). Long-term memory lets you store and recall information between conversations so your agent can **learn from feedback** and adapt to **user preferences**. This feature is part of the OSS library, and it is enabled by default for all LangGraph Cloud &amp; Studio users.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf45765e3cf29f5ff11c_short-vs-long.png)Memory: from short (thread-scoped) to long (cross-thread)

## On Memory

Most AI applications today are goldfish; they forget everything between conversations. This isn&#x27;t just inefficient— it fundamentally limits what AI can do.

Over the past year at LangChain, we&#x27;ve been working with customers to build memory into their agents. Through this experience, we&#x27;ve realized something important: there&#x27;s no universally perfect solution for AI memory. The best memory for each application still contains very application specific logic. By extension, most &quot;agent memory&quot; products today are too high-level. They try to create a one-size-fits-all product that doesn&#x27;t satisfy many production users&#x27; needs.

This insight is why we have built our initial memory support into LangGraph as a simple document store. High level abstractions can be easily built on top (as we will show below), but beneath it all is a simple, reliable, persistent memory layer that comes built in to all LangGraph applications.

## Cross-Thread Memory

LangGraph has always excelled at managing state **within** a single conversation thread using [checkpointers](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com#checkpoints). This &quot;short-term memory&quot; lets you maintain context within a single conversation.

Today, we&#x27;re extending that capability **across** **multiple threads**, enabling your agents to easily remember information across multiple conversations, all integrated in the LangGraph framework.

At its core, cross-thread memory is &quot;just&quot; a persistent document store that lets you **put**, **get**, and **search** for memories you&#x27;ve saved. These basic primitives enable:

- **Cross-Thread Persistence**: Store and recall information across different conversation sessions.
- **Flexible Namespacing**: Organize memories using custom namespaces, making it easy to manage data for different users, organizations, or contexts.
- **JSON Document Storage**: Save memories as JSON documents for easy manipulation and retrieval.
- **Content-Based Filtering**: Search for memories across namespaces based on content.

For a deeper understanding of these concepts, we&#x27;ve prepared a set of documents to provide framing and guidance on how to get started:

- A [conceptual video](https://youtu.be/JTL0yp85FsE?ref=blog.langchain.com) walking through memory concepts
- Conceptual guides on memory in LangGraph [Python](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com) &amp; [JS](https://langchain-ai.github.io/langgraphjs/concepts/memory/?ref=blog.langchain.com)
- How-to guide for sharing memories across threads in [Python](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/?ref=blog.langchain.com) &amp; [JS](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence/?ref=blog.langchain.com)

## Practical Implementation

To help you get started with implementing long-term memory in your applications, we&#x27;ve prepared a new LangGraph [template](https://studio.langchain.com/?ref=blog.langchain.com):

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf45765e3cf29f5ff121_image.png)

This LangGraph Template shows a chatbot agent that manages its own memory. Key resources for this are

- An [end-to-end tutorial video](https://youtu.be/-xkduCeudgY?ref=blog.langchain.com) walking through the implementation
- A [LangGraph Memory Agent](https://github.com/langchain-ai/memory-agent?ref=blog.langchain.com) in Python
- A [LangGraph.js Memory Agent](https://github.com/langchain-ai/memory-agent-js?ref=blog.langchain.com) in JavaScript

These resources demonstrate one way to leverage long-term memory in LangGraph, bridging the gap between concept and implementation.

We encourage you to explore these materials and experiment with incorporating long-term memory into your LangGraph projects. As always, we welcome your feedback and look forward to seeing how you apply these new capabilities in your applications.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)