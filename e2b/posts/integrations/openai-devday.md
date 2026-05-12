---
title: "OpenAI DevDay"
author: "Tereza Tizkova"
date: "2023-11-07"
url: "https://e2b.dev/blog/openai-devday"
category: "integrations"
site: "e2b"
---

This is a view by the E2B team, so the thoughts and comments are based on our experience with the AI space. [E2B](/) provides sandboxed cloud environments for AI-powered apps and agentic workflows. 

Check out our [sandbox runtime for LLMs](/docs?ref=october-newsletter)[.](https://github.com/e2b-dev)[‍](https://github.com/e2b-dev)

[We are open-source](https://github.com/e2b-dev), so please check out our [GitHub](https://github.com/e2b-dev/e2b), and support us with a star. ✴️

The highly anticipated OpenAI DevDay is likely to be remembered as the biggest AI event in 2023.

For weeks, rumors have been circulating, predicting that the way we use ChatGPT is about to change completely, and the announcements will kill many AI startups. After watching the[ DevDay Opening Keynote ](https://www.youtube.com/watch?v=U9mJuUkhUzk)together with our community, we are discussing the [major announcements](https://openai.com/blog/new-models-and-developer-products-announced-at-devday).

## The announcements

- **GPT-4 Turbo launch **- with longer context, more control, better knowledge, new modalities, customization, and higher rate limits
- **GPTs** - Customized versions of ChatGPT
- **Assistants API **- a playground for building AI assistants (the GPTs)

These are the three big news in detail:

### 1. GPT-4 Turbo

When we talked to medium/enterprise companies this year, many of them have AI projects just waiting for a lower price and better latency to launch. The new GPT-4 Turbo model is addressing this, among other things.

Starting now, it is much cheaper than GPT-4, in particular:

- 3 times less for input tokens.
- 2 times less for output tokens.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca6d_67976499cdc90069646170b1_H3jXbsdeDVBOlYIDwfKHIa0fsM4.webp)[Source](https://openai.com/blog/new-models-and-developer-products-announced-at-devday)

This is indeed great news for developers of AI agents and apps.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca73_679764b29f0ba3e08df0aca0_QewLomyAOGInbYjS5H4dXMxNc.webp)

The six major updates in GPT 4 Turbo are:

#### 01. Context length

While GPT-4 supports up to 8k (in some cases up to 32k) context length, GPT-4 Turbo offers 128k context length. That is approximately 300 pages of a standard book, so it could remember what happened to Tolkien’s [hobbits](https://www.amazon.com/Hobbit-J-R-Tolkien/dp/054792822X) throughout the book.

Sam mentioned that Turbo also is **more accurate**.

#### 02. More control

Reliability has been a huge problem for AI developers, given the unpredictable outputs of LLM models.

Addressing feedback from developers, there will be more control over the model's responses and outputs. This could partly compensate for the LLMs' stochasticity.

First, OpenAI announces a “JSON load” feature which ensures that the model will respond with valid JSON. That will make the API calls much easier.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272cb18_679764d3ab0dbc5fe7317d13_lF9NTdB6UdJtqYHKUIW2rDq3zCs.webp)Developers have struggled with invalid JSON output in the past. [Source](https://community.openai.com/search?q=invalid%20json)

Second, the GPT-4 Turbo is significantly better at function calling. You can now call many functions at once.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca70_679764f5268266ae89e7a02e_hCAsxqjGjZUDnA9ST6VTpI781IA.webp)[Source](https://x.com/IanSoh23/status/1721598405930082522?s=20)

The model will do better at following instructions in general.

Finally, Altman announced a beta of [reproducible outputs](https://platform.openai.com/docs/guides/text-generation/reproducible-outputs) as a new feature. That allows to pass the seed parameter to the model, which will make it return consistent outputs. That provides the user a higher degree of control over model behavior.

#### 03. Updated knowledge

The knowledge cutoff has been extended to April 2023 and will continue to see improvements.

Additionally, OpenAI is surfing on the current hype, adding built-in RAG. RAG [sparked a lot of interest ](https://www.ai.engineer/summit/)among developers and became a major topic at conferences. OpenAI is now introducing a retrieval feature in its platform. This allows users to incorporate information from external documents or databases into their projects. 

#### 04. New modalities

Surprising no one, DALL·E 3, GPT-4 Turbo with Vision, and the new text-to-speech (TTS) model are all going to into the OpenAI API now.

Developers can [integrate DALL·E 3](https://platform.openai.com/docs/guides/images) to ChatGPT Plus and Enterprise users, directly into their apps and products through our Images API by specifying dall-e-3 as the model. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca8d_67976524b76fb0853467db4a_WxOmtS32T6hvZA13T94BNpYUlo.webp)

#### 05. Customization

Fine-tuning has proven to be highly effective for GPT-3.5 since its launch a few months ago. Starting immediately, OpenAI is extending this approach to the 16k version of the model.

OpenAI is inviting active fine-tuning users to [apply ](https://openai.com/form/custom-models)for an experimental GPT-4 fine-tuning [Custom Models program](https://openai.com/form/custom-models).

It should allow close collaboration between the researchers and companies to create highly customized models for specific use cases. This includes modifying all aspects of the model training process, including domain-specific pre-training and post-training tailored to a particular domain.

#### 06. Higher rate limits

OpenAI is doubling tokens per minute for GPT-4 customers and allowing rate limit changes in API settings.

They're introducing Copyright Shield to cover legal costs for copyright claims in ChatGPT Enterprise and the API, emphasizing they don't train models using API or ChatGPT Enterprise data.

“And let me be clear,” adds Sam Altman. “This is a good time to remind people, that we do not train on data from the API or ChatGPT Enterprise ever.”

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca99_67976543d40f6aca1271a190_RBPFbrpIQxRympxI2pK4Bt8aZCQ.webp)

### 2. GPTs - Customized versions of ChatGPT

The OpenAI DevDay was the (first ever) conference for developers. However, the launch with the biggest hype, GPTs, is consumer-facing.

You may recall that OpenAI indicated in February that it intended to allow users to [define their own customizable AI agents](https://synthedia.substack.com/p/openai-to-offer-chatgpt-customization). The rumors prior to the DevDay were true - here come the OpenAI customizable GPTs.

You can now create custom versions of ChatGPT **without knowing how to code**. GPTs combine instructions, extra knowledge, and any combination of skills.

Example GPTs available for ChatGPT Plus and Enterprise users, with more users to follow.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca8a_6797655af3f364ab155daa61_N4RAHLHD4IhrXgnIEmGH82Crkw.webp)[Source](https://openai.com/blog/introducing-gpts)

OpenAI decided to include the AI community that is shaping the future, proven for example by the fact that “[ChatGPT Is More Famous, but Character.AI Wins on Engagement](https://www.similarweb.com/blog/insights/ai-news/character-ai-engagement/)”. (Users of Character.AI - a chatbot interface where you can customize your chat avatars - allegedly spend an average of two hours per day on the site.)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272cab5_679765940c79df0b1d227d56_WZWaCzeEunoBHWReNEv9w1cVDo.webp)[Source](https://x.com/mlejva/status/1721593994952532312?s=20)

GPT Store will be launched soon, featuring creations by verified builders.

#### Why “GPTs”?

OpenAI avoided the term “AI agent” and used "[GPTs](https://openai.com/blog/introducing-gpts)", even though they follow the characteristics of agents. 

It may be due to better connecting “GPT” with already publicly accepted “ChatGPT”. “GPTs” may be more relatable to the broader public. The emphasis is put on using natural language to program.

Recall the definition of[ LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) by Lilian Weng from OpenAI where agents were specified by

- Long-term memory
- Planning
- Tool use.

I see some parallels with GPTs, which have:

- Expanded Knowledge
- Custom Instructions
- Actions.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca93_679765b780cf9b10b68c0748_BPTToVRgFZoVmYTM2fOgP5arjg.webp)OpenAI is communicating its new product as "GPTs" while still referring to it as "agents". [Source](https://x.com/miramurati/status/1721668069796593958?s=20)

### 3. Assistants API

The [assistants API](https://platform.openai.com/docs/assistants/overview) is basically a **developer-facing part of the GPTs**. It works as self-coding API-level agents.

It simplifies the process for developers to create their own AI-powered assistants with well-defined objectives and the ability to call models and tools. You **no longer need to include all previous messages** for context when sending a new one to the API.

OpenAI also shipped a new [**playground**](https://platform.openai.com/playground?mode=assistant) to build the assistants. What is interesting to me is how OpenAI just targets both no-code "developers" and traditional developers with the Assistants API. I was expecting something more d

The Assistants API includes:

- Better function calling
- Built-in conversation management
- Python sandbox
- Memory

It offers using two tools so far:

- Retrieval
- Code interpreter (Which was called "Advanced Data Analyst" until recently).

We can probably expect more tools to be added soon, and there is already an option to add your custom tool. **The tools are essentially just OpenAI Functions**.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca90_679765d91b1e33c268630009_oSg5TRoSCbaOZYTC8aP5C8Cjv4.webp)

[**How is the OpenAI Code Interpreter different from E2B Sandboxes?**](/blog/e2b-sandbox)

### What are the implications?

OpenAI is shifting from focusing solely on AGI to prioritizing the commoditization of software development and building a platform. This will have a huge impact on coding and prototyping. 

Companies react quickly to the updates. Langchain, the most popular framework for building AI agents, quickly announced OpenGPTs as an alternative to OpenAI’s GPTs.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272cab8_679765f5c4b68e6acaf25d30_xPqV15zUlivaez74ycX3eFIODY.webp)[Source](https://github.com/langchain-ai/opengpts)

The announcements certainly put many companies in danger, e.g. vector database startups jeopardized by the Assistants API's retrieval.

Hopefully, most startups and companies won't go out of business. Instead, we'll see even more AI companies building and adding completely new AI features to their products.

For the AI developer community, 2024 will certainly be the production year, and we are excited to see what’s coming.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272ca96_679766103189a8a61d2c2869_GOPwmVfiKkK4vfFxRh4HIcZiCnk.webp)

### About OpenAI DevDay

OpenAI’s [first developer conference](https://openai.com/blog/announcing-openai-devday) took place in San Francisco, CA, on November 6, 202.

The goal was to bring hundreds of developers from around the world together with the team at OpenAI to preview new tools and exchange ideas

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67976660d40f6aca1272cabb_6797662cc4b68e6acaf29468_grMg2kpaYdKCqERVLBq0919ZaH8.webp)[Source](https://openai.com/devday/)