---
title: "LangChain x Context: Building Better Chat Products With User Analytics"
author: "LangChain Accounts"
date: "2023-07-13"
url: "https://www.langchain.com/blog/langchain-x-context-building-better-chat-products-with-user-analytics"
---

Partner

# LangChain x Context: Building Better Chat Products With User Analytics

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 12, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb201ba9d0fc7237808dc_screenshot-2023-07-12-at-9.38.26-am.png)**Today we’re announcing a **[**Langchain integration**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com)** for **[**Context**](http://getcontext.ai/?ref=blog.langchain.com). This integration allows builders of Langchain chat products to receive user analytics with a one line plugin.

Building compelling chat products is hard. Developers need a deep understanding of user behaviour and user goals to iteratively improve their products. Common questions that builders ask include:*** how are people using my product? How well is my product meeting user needs?**** *And* ****where does my product need improvement?* **

Today, answering these questions can involve reading thousands of chat transcripts captured in logs, with little tooling to help identify conversation themes or areas of weak product performance. A better solution now exists with Langchain’s integration with Context.

## What is Context?

**Context is a product analytics platform for LLM-powered chat products.** Context gives builders visibility into how real people use their chat products, with analytics to help developers understand:

- **How people are using their products**, by automatically clustering conversations into groups and tracking user-defined conversation topics,
- **How their product is meeting user needs**, by reporting user satisfaction, sentiment, and regeneration rates for each conversation topics,
- **Where their product is introducing risk,** by monitoring discussion of risky topics like politics or gambling:
- **Exactly what users are discussing**, by providing filtering and search over transcripts to allow debugging

These analytics give builders an understanding of how people are using their product, how their product is performing, and where sensitive topics are being discussed. This user understanding helps ensure user needs are being met, and allows developers to improve their products over time.

## Getting Started

To get started, [Context](http://getcontext.ai/?ref=blog.langchain.com) can be accessed for free [here](http://getcontext.ai/?ref=blog.langchain.com), and the Context x LangChain documentation can be accessed [here](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com). The first 50 signups using *LANGCHAIN100* promo code will receive 3 free months of Context’s $100/month membership tier.

## Installation and Setup

To get started with the Context LangChain integration, install the Context Python package:

**`pip install context-python --upgrade`**

**Getting API Credentials**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#getting-api-credentials)

To get your Context API token:

- Go to the settings page within your Context account ([https://go.getcontext.ai/settings](https://go.getcontext.ai/settings?ref=blog.langchain.com)).
- Generate a new API Token.
- Store this token somewhere secure.

**Setup Context**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#setup-context)

To use the ContextCallbackHandler, import the handler from Langchain and instantiate it with your Context API token.
Ensure you have installed the context-python package before using the handler.

`import os

from langchain.callbacks import ContextCallbackHandler

token = os.environ[&quot;CONTEXT_API_TOKEN&quot;]

context_callback = ContextCallbackHandler(token)`

## Usage

**Using the Context callback within a Chat Model**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#using-the-context-callback-within-a-chat-model)

The Context callback handler can be used to directly record transcripts between users and AI assistants.

**Example**[**​**](https://python.langchain.com/docs/modules/callbacks/integrations/context?ref=blog.langchain.com#example)

`import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
   SystemMessage,
   HumanMessage,
)
from langchain.callbacks import ContextCallbackHandler

token = os.environ[&quot;CONTEXT_API_TOKEN&quot;]

chat = ChatOpenAI(
   headers={&quot;user_id&quot;: &quot;123&quot;}, temperature=0, callbacks=[ContextCallbackHandler(token)]
)

messages = [
   SystemMessage(
       content=&quot;You are a helpful assistant that translates English to French.&quot;
   ),
   HumanMessage(content=&quot;I love programming.&quot;),
]

print(chat(messages))`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808fc_screenshot-2023-07-12-at-9.43.07-am.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808f7_screenshot-2023-07-12-at-9.43.13-am.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb202ba9d0fc7237808f4_screenshot-2023-07-12-at-9.43.19-am.png)

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