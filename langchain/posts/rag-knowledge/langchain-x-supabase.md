---
title: "LangChain x Supabase"
author: "LangChain Accounts"
date: "2023-04-08"
url: "https://www.langchain.com/blog/langchain-x-supabase"
---

PartnerLangChain

# LangChain x Supabase

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 8, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb2433fe3e9a95a5646ac_supa.png)Supabase is holding an [AI Hackathon](https://supabase.com/blog/launch-week-7-hackathon?ref=blog.langchain.com) this week. Here at LangChain we are big fans of both Supabase and hackathons, so we thought this would be a perfect time to highlight the multiple ways you can use LangChain and Supabase together.

The reason we like Supabase so much is that it useful in multiple different ways. A big part of building interesting AI applications is connecting models like GPT-3 with your personal data. So in that way, the different types of databases that Supabase supports are incredibly helpful. But after you&#x27;ve built your application, you also need a way to share it with the world - Supabase can help with that as well.

## Supabase VectorStore

One of the main type of AI applications people have been building is ways to &quot;chat&quot; with your document data. Basically, ChatGPT but where it knows information about specific data, whether it be your personal writing or an esoteric website. For an in depth tutorial on this type of application, please see this [blog](https://blog.langchain.com/tutorial-chatgpt-over-your-data/). A big part of this application is storing embeddings of documents in a vectorstore. Supabase can do that! See our documentation [here](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase?ref=blog.langchain.com) for a walkthrough of how to do so.

## Supabase Hybrid Search

Vectorstores enable easy semantic search over documents, but that&#x27;s not the only way to do retrieval of documents. The MendableAI team, for example, found a [20% increase in retrieval performance](https://twitter.com/ericciarla/status/1643318182369796096?s=20&amp;ref=blog.langchain.com) by switching to a hybrid search technique. They used Supabase to so do! See our documentation [here](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid?ref=blog.langchain.com) for a walkthrough of how you can experiment with this as well.

## Supabase + LangChain Starter Template

To make it super easy to build a full stack application with Supabase and LangChain we&#x27;ve put together a GitHub repo [starter template](https://github.com/langchain-ai/langchain-template-supabase?ref=blog.langchain.com). Our template includes

- An empty Supabase project you can run locally and deploy to Supabase once ready, along with setup and deploy instructions
- In [`supabase/functions/chat`](https://github.com/langchain-ai/langchain-template-supabase/blob/main/supabase/functions/chat/index.ts?ref=blog.langchain.com) a Supabase Edge Function that uses LangChain to call the GPT-3.5 API, with support for both batch and streaming modes for an amazing user experience.
- In `supabase/migrations` a Postgres migration that sets you up for using the Supabase Vector Store for LangChain.
- In `src` a React + Next.js + Tailwind frontend already set up with the Supabase SDK, and with an [example of calling the Chat function](https://github.com/langchain-ai/langchain-template-supabase/blob/main/src/pages/index.tsx?ref=blog.langchain.com)

With this you can build a full-stack AI application with

- All the modules that LangChain offers, eg. Prompts, Chains, LLMs, Chat Models, Retrievers, Vector Stores, Document Loaders, Text Splitters, etc.
- All the amazing features that Supabase offers out-of-the-box, eg. database, auth, storage, realtime, etc.
- A frontend stack you can easily customise with React + Next.js + Tailwind

Supabase Edge Functions uses Deno under the hood, we&#x27;ve recently added support for running LangChain on Deno, any issues let us know on [Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) or [GitHub](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com)!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)