---
title: "Chat Models"
author: "LangChain Accounts"
date: "2023-03-06"
url: "https://www.langchain.com/blog/chat-models"
---

LangChainOpen Source

# Chat Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 6, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25444d72d9752574945_photo-1611606063065-ee7946f0787a.jpeg)Last week OpenAI released a [ChatGPT endpoint](https://openai.com/blog/introducing-chatgpt-and-whisper-apis?ref=blog.langchain.com). It came marketed with several big improvements, most notably being 10x cheaper and a lot faster. But it also came with a completely new API endpoint. We were able to [quickly write a wrapper](https://twitter.com/hwchase17/status/1631023126472724480?s=20&amp;ref=blog.langchain.com) for this endpoint to let users use it like any normal LLM in LangChain, but this did not fully take advantage of the new message-based API. In this blog post we go over the new API schema and how we are adapting LangChain to accommodate not only ChatGPT but also all future chat-based models.

Key Links:

- [Python Documentation](https://python.langchain.com/docs/modules/model_io/models/chat/?ref=blog.langchain.com)
- [JS/TS Documentation](https://hwchase17.github.io/langchainjs/docs/modules/chat_models/overview?ref=blog.langchain.com)

## Why new abstractions?

So OpenAI released a new API - what’s the big deal? Why are new abstractions even needed?

Although the ChatGPT endpoint uses a language model under the hood, the API is quite different from the existing GPT-3 endpoint. This is a bit of a simplification, but the existing GPT-3 endpoint has an interface of:

- Input: text
- Output: text

The new ChatGPT endpoint has an interface of:

- Input: List of chat messages
- Output: chat message

This new interface means that some of our abstractions about the inputs/outputs to a language model are no longer correct. For example, the prompting strategies we had previously built all assumed that the output of the PromptTemplate was a string. However, now for chat models, the input needs to be a list of messages. Since prompting is at the core of a lot of LangChain utilities and functionalities, this is a change that cuts pretty deep.

## Why chat models?

Okay, so there’s a new type of model. Why are we rushing to support it? Is it really so different from the existing API that it deserves new abstractions?

To answer that, it’s worth thinking about why OpenAI chose to release a model in this format at all. This part is all speculation. The main difference between this API and the previous GPT-3 API is that there is now more structure to user input, coming in the form of different types of messages. To be specific, the ChatGPT API allows for differentiation between “user”, “assistant”, and “system” messages. This differentiation could allow for the model to treat different types of messages differently, which could in theory improve the safety of applications built on top of these models. For example, a commonly known type of attack against LLM applications is [prompt injection attacks](https://simonwillison.net/2022/Sep/12/prompt-injection/?ref=blog.langchain.com), where the end user directs the application to do something it wasn’t intended to do. By adding this structure into the prompt now, in theory, end applications could put all their application instructions in the “system” messages, all end user input in the “user” messages, and then the model could be trained to always “obey” system messages, despite what the user messages may tell it. In practice, it seems like prompt injection attacks against chat models are [still a thing](https://medium.com/seeds-for-the-future/tricking-chatgpt-do-anything-now-prompt-injection-a0f65c307f6b?ref=blog.langchain.com), so this may not fully address those concerns. Only time will tell.

The above example of “user” vs “assistant” vs “system” messages also speaks to why this format is different enough from the existing APIs to deserve its own abstractions.

There’s also more practical reasons. OpenAI has not yet released a “normal” LLM endpoint corresponding to the ChatGPT models, so if people want take full advantage of the speed/cost of these models they need to use the ChatGPT API. There are also rumors of other chat-style models coming to market soon ([Claude from Anthropic](https://scale.com/blog/chatgpt-vs-claude?ref=blog.langchain.com), [Bard from Google](https://blog.google/technology/ai/bard-google-ai-search-updates/?ref=blog.langchain.com), early rumors of a [dialogue model from Cohere](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/?ref=blog.langchain.com)). Although it is not yet known what format these models will be available in, it is not crazy to assume they will also have a chat based API option.

## What are our goals with the new abstractions?

When designing these new abstractions, we had three primary goals in mind:

**#1: Allow users to fully take advantage of the new chat model interface**

As mentioned above, the API for chat models is pretty different from existing LLM APIs. We want to let users take advantage of that.

**#2: Allow for interoperability of prompts between “normal” LLM APIs and chat-based APIs**

Although there are definitely differences in prompts for “normal” LLMs vs chat-based APIs, we wanted to make it as seamless as possible (within reason) to use the same prompt with either type of model. Practically, we prioritized this since most prompts in the code base are optimized for LLMs, and we did not want them to break terribly for chat-based models.

**#3: Make the abstractions generic beyond just OpenAI**

We did not want any abstractions we put in place to be OpenAI-specific. As mentioned above, there are rumors of other chat-style models coming to market soon, and we wanted to make sure we could seamlessly support them.

## What are these new abstractions?

While it may seem like we are introducing overly many abstractions into the codebase, they are all done with the goal of making anything added to codebase work as well as possible with these new models. One of the objectives of LangChain has always been to allow for interoperability between language model providers, and we hope this helps with that.

**Chat Messages**

We are adding abstractions for the different types of chat messages.

- `HumanMessage`: a message sent from the perspective of the human
- `AIMessage`: a message sent from the perspective of the AI the human is interacting with
- `SystemMessage`: a message setting the objectives the AI should follow
- `ChatMessage`: a message allowing for arbitrary setting of role

**Chat Models**

We are also adding abstractions for chat models. The interface these types of models expect is very similar to the underlying ChatGPT API - it takes in a list of Chat Messages and returns a Chat Message.

**Chat Message Templates**

Since most applications don’t hard code messages to send but rather utilize the idea of “PromptTemplates” (take in user input, and return a prompt) we are adding corresponding chat message prompt templates.

- `HumanMessagePromptTemplate`: a class that exposes a method to take in user input and return a HumanMessage
- `AIMessagePromptTemplate`: a class that exposes a method to take in user input and return an AIMessage
- `SystemMessagePromptTemplate`: a class that exposes a method to take in user input and return a SystemMessage
- `ChatMessagePromptTemplate`: a class that exposes a method to take in user input and return a ChatMessage

**Prompt Values**

To allow for interoperability of prompts between “normal” LLM APIs and chat-based APIs, we are adding the concept of a `PromptValue`. This is a class which has the following methods:

- `to_string`: converts the PromptValue into a string, to be used in “normal” LLM APIs
- `to_messages`: converts the PromptValue into a list of messages, to be used in chat-based APIs

To go along with this, we also added methods to `BaseLLM` and `BaseChatModel` class that take in `PromptValue`s, convert them to `string`s or `ChatMessages` respectively, and then pass them to the model.

## How do these align with our objectives?

Let’s make sure these abstractions align with the objectives we set out

**#1: Allow users to fully take advantage of the new chat model interface**

We cover all of the functionality in the ChatGPT interface. There are some things we do not explicitly have abstractions for (like the `name` parameter), but those are still usable and we may work on adding better support in the future should they become more relevant.

**#2: Allow for interoperability of prompts between “normal” LLM APIs and chat-based APIs**

The `PromptValue` abstraction should allow for this. We have very simple methods for converting a string to messages (make it a single `HumanMessage`) and messages to a string (just cast the whole list to string). These (especially the messages-to-string method) can definitely be improved.

**#3: Make the abstractions generic beyond just OpenAI**

We believe that by adding explicit concepts of Human/AI/System messages, rather than relying on dictionaries with `&quot;role&quot;` keys, we have set ourselves up for being model API agnostic. This way, if another model provider has different naming conventions (eg they call the AI `&quot;AI&quot;` rather than OpenAI’s `&quot;assistant&quot;`) we can easily map to these naming conventions in the model wrapper.

## Next steps

Hopefully this has helped to clarify some of our thinking around what abstractions we introduced. We would LOVE feedback on these abstractions. It is always scary to have to formulate abstractions on a completely new concept in less than a week, so we really appreciate any suggestions and comments.

We will also work on continuing to add in more functionality around chat models. For example, better message-to-string support, better few-shot example support, and better support for chat memory.

We also have accrued a massive backlog of items due to this unexpected release, so thank you for your patience as we try to sift through that.

Finally, a big thank-you to the Anthropic team (and Mike Lambert in particular) for thinking through some of these abstractions and making sure they were general beyond the ChatGPT API. It&#x27;s always hard to try to generalize abstractions when there&#x27;s only a single instance to look at, so we greatly appreciated their wisdom.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)Agent ArchitectureDeep AgentsOpen Source

#### Running Subagents in the Background

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)Hunter LovellColin FrancisApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/running-subagents-in-the-background)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)