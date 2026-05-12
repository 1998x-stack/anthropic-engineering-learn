---
title: "Chat Loaders: Fine-tune a ChatModel in your Voice"
author: "LangChain Accounts"
date: "2023-08-25"
url: "https://www.langchain.com/blog/chat-loaders-finetune-a-chatmodel-in-your-voice"
---

Observability &amp; EvalsAgent Architecture

# Chat Loaders: Fine-tune a ChatModel in your Voice

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 25, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb19057c432b84a74635e_photo-1593697723815-e1c957debea8.jpeg)

### Summary

We are adding a new integration type, ChatLoaders, to make it easier to fine-tune models on your own unique writing style. These utilities help convert data from popular messaging platforms to chat messages compatible with fine-tuning formats like that supported by OpenAI.

Thank you to [Greg Kamradt](https://twitter.com/GregKamradt?ref=blog.langchain.com) for [Misbah Syed](https://twitter.com/MisbahSy?ref=blog.langchain.com) for their thought leadership on this.

**Important Links:**

- [**Chat Loaders**](https://python.langchain.com/docs/integrations/chat_loaders/?ref=blog.langchain.com)
- [**Twitter Finetune Example**](https://elon-twitter-clone.streamlit.app/?ref=blog.langchain.com)
- [**Code for Twitter Finetune Example**](https://github.com/langchain-ai/twitter-finetune?ref=blog.langchain.com)
- [**Webinar on this topic next week**](https://www.crowdcast.io/c/lzafugqtyata?ref=blog.langchain.com)

### Context

On Tuesday, OpenAI [announced](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates?ref=blog.langchain.com) improved fine-tuning support, extending the service to  larger chat models like GPT-3.5-turbo. This enables anyone to customize these larger, more capable models for their own use cases. They also teased support for fine-tuning GPT-4 later this year.

While fine-tuning is typically  [not](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb?ref=blog.langchain.dev) [advised](https://www.glean.com/blog/lessons-and-learnings-from-building-an-enterprise-ready-ai-assistant?ref=blog.langchain.dev) for teaching an LLM substantially new knowledge or for factual recall; it *is* good for style transfer.

We&#x27;ve had a lot of community members ask about the best ways to get ChatGPT to respond &quot;in your own voice&quot; - fine-tuning is an excellent way to do so!

Great people on Twitter like Greg Kamdrat have also been bullish on this use case:

Setting the tone/style of the output is top of the list for me

Fine-tuning as a service to businesses that matches their tone

Currently investigating...will report back [https://t.co/235WSJzxet](https://t.co/235WSJzxet?ref=blog.langchain.com) [pic.twitter.com/KDzMrdqccv](https://t.co/KDzMrdqccv?ref=blog.langchain.com)

> — Greg Kamradt (@GregKamradt) [August 22, 2023](https://twitter.com/GregKamradt/status/1694063901724610995?ref_src=twsrc%5Etfw&amp;ref=blog.langchain.com)

Fine-tuning on your communications could be useful for a variety of applications, such as responding to customers in your brand&#x27;s voice, generating content that is more aware of your team&#x27;s unique jargon, chatting reliably in a target language, or just for fun!

Why is this better than direct instructions? Style and tone can be hard to describe! Most of us don&#x27;t write like ChatGPT, and it can sometimes be frustratingly difficult to get the LLM to consistently respond in a particular voice (especially over longer conversations).

Why is this better than few-shot examples? It can be challenging to capture your voice in only a few concise snippets! Fine-tuning lets you provide a larger number of examples the model can learn from without having to see them every time you want to query the model.

### ChatLoaders

At LangChain, we want to make it as easy as possible for you to take advantage of this improved fine-tuning support. To make it simple to adapt a model to your voice, we&#x27;re adding a new integration type: `ChatLoaders`.

These utilities take data exported from popular messaging platforms and convert them to LangChain message objects, which you can then easily convert platform-agnostic message formats, such as OpenAI, Llama 2, and others. This training data can be used directly for fine-tuning a model.

We&#x27;ve added loaders for the following popular messaging platforms so far:

- Facebook Messenger
- Slack
- Telegram
- WhatsApp

We have also added a recipe on how to do so for Discord and Twitter (using Apify) and plan to integrate additional chat loaders in the near future. If you have a favorite messaging platform you&#x27;d like to support, we&#x27;d love to help you land a PR!

To get you started, we&#x27;ve added an  [end-to-end example notebook](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/extras/integrations/chat_loaders/facebook.ipynb?ref=blog.langchain.com)  to the LangChain documentation showing how to fine-tune `gpt-3.5-turbo` (the model behind ChatGPT) on an example set of Facebook messages.

❗

Please ensure all participants of your conversations support the decision to train a model on the chat data before proceeding.

Once you have your fine-tuned model, you can use the model name directly in  LangChain&#x27;s [ChatOpenAI](https://api.python.langchain.com/en/latest/chat_models/langchain.chat_models.openai.ChatOpenAI.html?ref=blog.langchain.com#langchain.chat_models.openai.ChatOpenAI) class:

`from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model=&quot;ft:gpt-3.5-turbo-0613:{openaiOrg}::{modelId}&quot;)
llm.predict(&quot;What classes are you taking this year?&quot;)
`

Then you can plug this into any other LangChain component!

### End-to-End Example

We&#x27;ve also created an end-to-end example of finetuning a model based on Elon Musk&#x27;s tweets. This uses Apify to load data. Note that it&#x27;s less than 100 examples so results may not be the most amazing they could be.

We open-sourced this example at the GitHub repo [here](https://github.com/langchain-ai/twitter-finetune?ref=blog.langchain.com). We also hosted it on Streamlit app so you can easily play around with it [here](https://elon-twitter-clone.streamlit.app/?ref=blog.langchain.com).

### Webinar

There is a lot more to discuss on this topic. What types of messages are best for finetuning? What others sources of data exist for this? How many points do you need?

We&#x27;ll be discussing this and more next week in a [webinar](https://www.crowdcast.io/c/lzafugqtyata?ref=blog.langchain.com) with Greg Kamradt. Come join!

### Conclusion

We&#x27;re excited to see all the creative applications fine-tuning unlocks.  We have implemented a few ChatLoaders already, but we need your help to make it easier to create your own personalized model.  Help us create more ChatLoaders!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)