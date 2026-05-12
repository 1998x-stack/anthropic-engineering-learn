---
title: "Standard message content"
author: "LangChain Accounts"
date: "2025-09-03"
url: "https://www.langchain.com/blog/standard-message-content"
---

Company AnnouncementsDeep AgentsOpen Source

# Standard message content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa80b4cdea28e90f79a4_Standard-message-content-2.png)TLDR: We’ve introduced a [new view of message content](https://docs.langchain.com/oss/python/langchain/messages?ref=blog.langchain.com#content) that standardizes reasoning, citations, server-side tool calls, and other modern LLM features across providers. This makes it easier to build applications that are agnostic of the inference provider, while taking advantage of the latest features of each. This feature is fully backward-compatible as it can be computed lazily from existing message content.

## Motivation

One of LangChain&#x27;s core strengths is providing a **&quot;write once, run anywhere&quot;** abstraction for large language models. This abstraction allows developers to build applications that can seamlessly switch between different LLM providers without rewriting code.

There’s been a recent explosion in the richness and variety of features offered by major inference providers, including OpenAI, Anthropic, and Google Gemini. LLMs can now take multiple distinct steps in service of a query, from laying out their reasoning, to performing web searches and invoking code interpreters, to generating a final response with citations and potentially multimodal data, such as images. Although the set of features supported by each provider is similar, their APIs have diverged, and compatibility layers— such as Chat Completions APIs offered by each provider— typically lag in supporting (or don’t support at all) the full set of provider-native features.

## Standard content in LangChain 1.0

We’ve introduced new standard types for the latest LLM features, and exposed them on all LangChain message objects, making it easier to build provider-agnostic applications without sacrificing support for any available features. These features will be available in `langchain` 1.0 and are available for both [Python](https://docs.langchain.com/oss/python/releases/langchain-v1?ref=blog.langchain.com) and [JS](https://docs.langchain.com/oss/javascript/releases/langchain-v1?ref=blog.langchain.com).

[Standard content blocks](https://docs.langchain.com/oss/python/langchain/messages?ref=blog.langchain.com#content) ensure that **identical capabilities are represented identically** across providers. In practice, they are a set of typed data structures that normalize message content across all LLM providers. They include:

- Standard text output from models (including citations)
- Model reasoning and chain-of-thought output
- Images, audio, video, and documents from any source (URL, base64, bucket file ID)
- Tool/function calls and invocations
- Provider-specific tools including built-in web search capabilities and code execution

## Details

All LangChain message objects now implement a `.content_blocks` property which will lazily load the new representation from the existing message content. Consider results from Anthropic’s Claude and OpenAI’s Responses API. In this example we engage their reasoning and web search features. The raw `.content` will pass through the provider-native format:

**Anthropic**:

`from langchain.chat_models import init_chat_model

llm = init_chat_model(
    &quot;anthropic:claude-sonnet-4-20250514&quot;,
    thinking={&quot;type&quot;: &quot;enabled&quot;, &quot;budget_tokens&quot;: 5_000},
).bind_tools([
    {
        &quot;type&quot;: &quot;web_search_20250305&quot;,
        &quot;name&quot;: &quot;web_search&quot;,
        &quot;max_uses&quot;: 1,
    }
])

response = llm.invoke(&quot;When was LangChain created?&quot;)

response.content
# [
#   {
#     &quot;type&quot;: &quot;thinking&quot;,
#     &quot;thinking&quot;: &quot;...&quot;,
#     &quot;signature&quot;: &quot;...&quot;,
#   },
#   {
#     &quot;type&quot;: &quot;server_tool_use&quot;,
#     &quot;name&quot;: &quot;web_search&quot;,
#     &quot;input&quot;: {...},
#     &quot;id&quot;: &quot;...&quot;,
#   },
#   {
#     &quot;type&quot;: &quot;web_search_tool_result&quot;,
#     &quot;content&quot;: [...],
#     &quot;tool_use_id&quot;: &quot;...&quot;,
#   }
#   {
#     &quot;type&quot;: &quot;text&quot;,
#     &quot;text&quot;: &quot;...&quot;,
#     &quot;citations&quot;: [...],
#   }
`

**OpenAI**:

`from langchain.chat_models import init_chat_model

llm = init_chat_model(
    &quot;openai:gpt-5-nano&quot;,
    reasoning={&quot;effort&quot;: &quot;low&quot;, &quot;summary&quot;: &quot;auto&quot;},
).bind_tools([{&quot;type&quot;: &quot;web_search_preview&quot;}])

response = llm.invoke(&quot;When was LangChain created?&quot;)

response.content
# [
#   {
#     &quot;type&quot;: &quot;reasoning&quot;,
#     &quot;summary&quot;: [...],
#     &quot;id&quot;: &quot;...&quot;,
#   },
#   {
#     &quot;type&quot;: &quot;web_search_call&quot;
#     &quot;action&quot;: {...},
#     &quot;id&quot;: &quot;...&quot;,
#     ...
#   },
#   {
#     &quot;type&quot;: &quot;text&quot;,
#     &quot;text&quot;: &quot;...&quot;,
#     &quot;annotations&quot;: [...],
#     &quot;id&quot;: &quot;...&quot;,
#   }
`

Although the content of these responses are similar, small differences in the APIs add compounding friction to building an application that would let you swap between these two providers.

The new `.content_blocks` property will parse both responses into a consistent representation:

`response.content_blocks
# [
#   {
#     &quot;type&quot;: &quot;reasoning&quot;,
#     &quot;reasoning&quot;: &quot;...&quot;,
#   },
#   {
#     &quot;type&quot;: &quot;web_search_call&quot;,
#     &quot;query&quot;: &quot;...&quot;,
#     &quot;id&quot;: &quot;...&quot;,
#     &quot;extras&quot;: {...},
#   },
#   {
#     &quot;type&quot;: &quot;web_search_result&quot;,
#     &quot;urls&quot;: [...],
#     &quot;id&quot;: &quot;...&quot;,
#     &quot;extras&quot;: {...},
#   },
#   {
#     &quot;type&quot;: &quot;text&quot;,
#     &quot;text&quot;: &quot;...&quot;,
#     &quot;annotations&quot;: [...],
#   }

`

The output of `.content_blocks` includes new types for reasoning, citations, web searches, code interpreter calls, and also includes LangChain types for (client side) tool calls and multimodal data, such as images, PDF documents, and audio.

Standard content blocks are currently available in alpha for

- Providers implementing chat completions APIs (including OpenAI)
- OpenAI Responses API
- Anthropic (Claude)

`langchain` 1.0 will feature support for all major providers.

## Backward compatibility

- No breaking changes; **100% compatible** with existing LangChain applications
- `.content_blocks` works on all message types, including legacy ones stored in cache

## Looking forward

Standard content blocks represent a fundamental step toward more reliable, maintainable LLM applications.

By providing consistent interfaces across providers, you can:

- **Build with confidence**: Type safety catches errors before production
- **Scale across providers**: Switch models without spending time rewriting application logic
- **Future-proof applications**: New provider features work immediately without breaking existing code

**Ready to try it?** Check out our [migration guide](https://docs.langchain.com/oss/python/releases/langchain-v1?ref=blog.langchain.com) and [technical docs](https://docs.langchain.com/oss/python/langchain/messages?ref=blog.langchain.com#content).

**Questions or feedback?** Please comment on the dedicated [Github issue](https://github.com/langchain-ai/langchain/issues/32794?ref=blog.langchain.com) for the release. We’d appreciate any thoughts you have to share!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)