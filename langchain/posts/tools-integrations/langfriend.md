---
title: "LangFriend: a Journal with Long-Term Memory"
author: "LangChain Accounts"
date: "2024-03-28"
url: "https://www.langchain.com/blog/langfriend"
---

LangGraph

# LangFriend: a Journal with Long-Term Memory

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 28, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff9e48474b2f8b40ee3_Memory---Blog.png)**One of the concepts we are most interested in at LangChain is memory. Whenever we are interested in a concept, we like to build an example app showing off that concept. For memory, we decided to build a journaling app! We&#x27;re hosting a version of it that anyone can try out. We&#x27;re also starting to work with a few alpha users on a developer facing API. If you are interested in this, please sign up below.**

**Key Links:**

- [**YouTube**](https://www.youtube.com/watch?v=tSicjawrfUY&amp;ref=blog.langchain.com)[](https://journal.langchain.com/?ref=blog.langchain.com)
- [**Developer API Access**](https://forms.gle/j3Aaa2ibNpg5pC4q7?ref=blog.langchain.com)

💡

We are also doing a memory related hackathon with New Computer, MongoDB and Anthropic on 4/6/2024. Sign up [here](https://lu.ma/taa6ijxt?ref=blog.langchain.com).

One of the components of LLM systems that we are most bullish on is memory. A lot of the power of generative AI is its ability to generate unique content on the fly. This can be incredibly powerful for customizing a user experience. This can be done by drawing upon existing information about users, but it can also be done by remembering previous user interactions and learning from those.

Is is this type of &quot;remembering&quot; that we are excited about exploring. We think that more and more interactions will occur between a user and an LLM - chatbots are the dominant form factor for LLM applications. This means that more and more valuable user information will be exchanged in those conversation - a persons likes or dislikes, who their friends are, what their goals are. Learning these attributes - and then incorporating them back into the application can greatly improve the user experience.

As we were exploring memory, we thought it would be helpful to put together a use case example to motivate and ground a lot of our work. We chose a journaling app to be this use case. We named this journaling app &quot;LangFriend&quot;, and are opening it up to the public today. While still just a humble research preview, we hope to gather community feedback on what works well and how to improve it, before open sourcing it.

In this post we&#x27;ll talk a bit about prior academic work in memory, other companies doing interesting things and why we chose a journaling app to focus on. We&#x27;ll then deep dive into the journaling app, walking through its functionality. If you are interested in exploring memory with us, please reach out here.

## Academic Work

There are two main academic papers we found inspiring for our work on memory.

First: [MemGPT](https://github.com/cpacker/MemGPT?ref=blog.langchain.com). From researchers at UC Berkley, the TLDR of this paper is that they give the LLM the ability to call a few functions. These functions can do things like remember specific facts, recalls related things, etc.

> Large language models (LLMs) have revolutionized AI, but are constrained by limited context windows, hindering their utility in tasks like extended conversations and document analysis. To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems which provide the illusion of an extended virtual memory via paging between physical memory and disk. Using this technique, we introduce MemGPT (MemoryGPT), a system that intelligently manages different storage tiers in order to effectively provide extended context within the LLM’s limited context window

Second: [Generative Agents](https://arxiv.org/pdf/2304.03442.pdf?ref=blog.langchain.com). From researchers at Stanford, the TLDR of this paper is that they use reflection over experiences to form memories, which are then stored and retrieved programmatically.

> We demonstrate through ablation that the components of our agent architecture—observation, planning, and reflection—each contribute critically to the believability of agent behavior. By fusing large language models with computational interactive agents, this work introduces architectural and interaction patterns for enabling believable simulations of human behavior.

One interesting difference between these two papers is the degree to which the LLM actively decides to use memory, versus having it be more of background process. MemGPT forces the LLM to use memory functions, while Generative Agents is more of a background process.

## Companies

There are a few companies doing awesome stuff with memory.

Plastic Labs is a startup building projects like [TutorGPT](https://github.com/plastic-labs/tutor-gpt?ref=blog.langchain.com).

> LangChain LLM application. Dynamic metaprompting for theory-of-mind-powered tutoring.

[Good AI](https://github.com/GoodAI/charlie-mnemonic?ref=blog.langchain.com) is a startup that just open-sourced a chat assistant with long-term memory.

> At first glance, Charlie might resemble existing LLM agents like ChatGPT, Claude, and Gemini. However, its distinctive feature is the implementation of LTM, enabling it to **learn from every interaction**. This includes **storing and integrating user messages, assistant responses, and environmental feedback into LTM** for future retrieval when relevant to the task at hand.

OpenAI has [recently incorporated memory features](https://www.wired.com/story/chatgpt-memory-openai/?ref=blog.langchain.com) into ChatGPT.

Looking at these companies also displays a difference between implementing memory as something active that the LLM needs to consciously invoke (ChatGPT) versus a background process that is automatically incorporated (TutorGPT).

## Why a Journal App?

When thinking about a good use case to implement to test out long-term memory, a journaling app jumped to mind. The main reason for this is that we believed the interactions in this app would contain more relevant information to remember than a standard chat application.

With a standard chat application, there may a lot of superfluous exchanges - &quot;hey!&quot;, &quot;hi&quot;, &quot;whats up&quot;, etc. In a journal setting, you more quickly get to a point where you are sharing real, interesting feelings and insights.

Still - we wanted to add a chat component to this app. The main reason for this was to show that our application was learning and remembering information about the user. It would be able to use this information to craft personalized responses to the user.

Here you can see it remember that I&#x27;m a fan of Italian cuisine, and that I feel refreshed after working out.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaffae48474b2f8b40f08_lang_friend_chat_ss.png)

After adding your first journal, and chatting with our companion, you&#x27;ll see a &quot;Memories&quot; button appear in the navigation bar. Clicking on this will show you all the main memories we were able to extract from your journals.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaffae48474b2f8b40efe_Screenshot-2024-03-26-at-4.19.53-PM.png)

You&#x27;ll notice the list is slim, and doesn&#x27;t contain too much information. These are just the most important, high level facts we extracted. Behind the scenes we&#x27;re pulling many more facts than this from your entries, and you can search through all of them!

Start typing in the &quot;Search memories...&quot; input, and in real time you&#x27;ll see the wide variety of facts LangFriend is storing about you:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaffae48474b2f8b40f05_Screenshot-2024-03-26-at-4.25.12-PM.png)

## Customizing

We wanted to make LangFriend as appealing as possible to all users. Because of this, we allow anyone to update the system message that prefixes, and sets the tone of all chats with our companion. A default is included, which we carefully crafted to suit the needs of many users. However if you&#x27;re looking for something slightly, or entirely different you can change as little, or as much of it as you&#x27;d like.

Find the system prompt, and update it by visiting the &quot;Logs&quot; page, and clicking on the &quot;Config&quot; button. From here, a dialog will popup with your system prompt.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaffae48474b2f8b40f01_Screenshot-2024-03-26-at-4.35.24-PM.png)

Any changes made will persist between sessions, and will prefix all your future chat conversations!

## Conclusion

LangFriend is an exciting research preview that showcases the potential of incorporating long-term memory into LLM applications. By focusing on a journaling app, we aim to capture meaningful user information to provide personalized responses and enhance the user experience. Inspired by academic work and innovative companies in the field, LangFriend demonstrates how memory can be actively utilized or incorporated as a background process to create engaging and adaptive interactions. We&#x27;re excited to invite the community to explore LangFriend, provide feedback, and join us in pushing the boundaries of what&#x27;s possible with memory in LLM applications, unlocking the full potential of generative AI for more powerful, personalized, and meaningful user experiences.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa18703c727fd28ab4de_Vodafone-Italy---Oct-2025--1-.png)Case StudiesLangGraphLangSmith

#### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/customers-vodafone-italy)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)