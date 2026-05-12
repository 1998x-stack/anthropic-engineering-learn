---
title: "OpenAI&#x27;s Bet on a Cognitive Architecture"
author: "LangChain Accounts"
date: "2023-11-28"
url: "https://www.langchain.com/blog/openais-bet-on-a-cognitive-architecture"
---

Harrison&#x27;s In the Loop

# OpenAI&#x27;s Bet on a Cognitive Architecture

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseNovember 28, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)10min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0abc83ac7211fe5741a_Screenshot-2023-11-27-at-8.22.59-PM-1.png)Three weeks ago OpenAI held a highly anticipated developer day. They released a myriad of new features. The two most interesting to me were the Assistants API and GPTs. To me, these represent the same bet – on a particular, agent-like, closed “cognitive architecture”. They appeal to different end users, but both speak to OpenAI’s ambitions to drive applications towards this particular cognitive architecture. At LangChain, we believe in a world where LLMs power agent-like systems that are truly transformative. However, we believe the route to get there is one where companies have control over their cognitive architectures. You can do that today with projects like [OpenGPTs](https://github.com/langchain-ai/opengpts?ref=blog.langchain.com) - an open, editable, and configurable version of the Assistants API (and GPTs).

## GPTs and the Assistants API

Of the two, [GPTs](https://openai.com/blog/introducing-gpts?ref=blog.langchain.com) are probably the more commonly discussed one on the internet. They provide a (largely) no-code way to create your own “GPT”. These GPTs can be customized with custom instructions, custom knowledge, and custom functions. These GPTs seem to be a second attempt at an app store of sorts, following up on Plugins (which - [in Sam Altman&#x27;s own words](https://matt-rickard.com/chatgpt-plugins-dont-have-pmf?ref=blog.langchain.com) - did not find product market fit).

The [Assistants API](https://platform.openai.com/docs/assistants/overview?ref=blog.langchain.com) is the more developer-centric version of this idea. The Assistants API is a stateful API that allows for storage of previous messages, uploading of files, access to built-in tools (code interpreter), and can be used to control other tools (through function calling, where the developer specifies a function to be called, which can then be executed client side).

## Cognitive Architectures

Under the hood, these both represent a similar type of “cognitive architecture”. Here, I use cognitive architecture to describe the orchestration of an LLM application. I first heard this term used by [Flo Crivello](https://twitter.com/Altimor?ref=blog.langchain.com) (creator of [Lindy](https://twitter.com/getlindy?ref=blog.langchain.com), an autonomous agent startup) and think it is a fantastic term.

💡

Most interesting LLM applications can be described as context-aware reasoning applications. There are two main components here: (1) how is context provided to the application, (2) how does the application “reason”. Both of these components make up the cognitive architecture of an application.

At LangChain, we’ve been thinking about cognitive architectures for a while. In a recent TedAI talk (video yet to be released) I spoke about the different levels of cognitive architectures that we see developers building. These include:

- A single LLM call, only determining the output of the application
- A chain of LLM calls, still only determining the output of the application
- Using an LLM as a router, to choose which action (tool, retriever, prompt) to use
- State machines - using LLMs to route between steps, in some sort of loop, but still with the allowed transition options enumerated in code
- Agents - removing a lot of the scaffolding, so that the transition options are wholly determined by the LLM

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0abc83ac7211fe5741a_Screenshot-2023-11-27-at-8.22.59-PM-1.png)A table showing our current mental model of cognitive architectures.

## Agents

Both the Assistants API and GPTs are examples of the “agent” cognitive architecture described above. Sam Altman even used that exact term (”agent”) when announcing them. Although agents can be an overloaded term, used to describe a myriad of different applications, OpenAI’s use of the term largely tracks with our understanding: using the LLM alone to define transition options.

What do applications like this look like in practice? This can best be thought of as a loop. Given user input, this loop will be entered. An LLM is then called, resulting in either a response to the user OR action(s) to be taken. If it is determined that a response is required, then that is passed to the user, and that cycle is finished. If it is determined that an action is required, that action is then taken, and an observation (action result) is made. That action &amp; corresponding observation are added back to the prompt (we call this an “agent scratchpad”), and the loop resets, ie. the LLM is called again (with the updated agent scratchpad).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0acc83ac7211fe5742f_CleanShot-2023-11-14-at-19.09.59%402x.png)An overview of an &quot;agent&quot; architecture

At a high level, this is what GPTs are doing. When they call a tool you give them (or a built-in tool like retrieval or code interpreter) you can see a widget on the screen that spins. This represents the action being taken, and the GPT is waiting for an observation. As some point, it just responds with text - no action to be taken - and the loop is finished.

The Assistants API is the same. The only difference is that the API doesn’t call the tools for you - unless it is a built in tool like retrieval or code interpreter. Instead, it responds with a certain type of message, telling you which tool(s) should be called (and what the inputs to those tools should be) and then waits for you to call the tools client-side and pass back in the results.

This “agent” cognitive architecture has been evolving over the past year and a half. AI21 Labs released their [MRKL paper](https://www.ai21.com/blog/jurassic-x-crossing-the-neuro-symbolic-chasm-with-the-mrkl-system?ref=blog.langchain.com) over a year and half ago. The [ReAct prompting strategy](https://arxiv.org/abs/2210.03629?ref=blog.langchain.com) (released over a year ago) was a particular type of prompting strategy that enables this type of architecture. We incorporated ReAct in LangChain nearly a year ago, quickly expanding to a more general, zero-shot prompting strategy. [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT/tree/master?ref=blog.langchain.com) burst onto the scene about nine months ago, using this same cognitive architecture but giving it more tools, more persistent memory, and generally larger tasks to accomplish.

## The Bet OpenAI is Making

I was very interested to see how heavily OpenAI leaned into agents given that by all accounts this cognitive architecture is not reliable enough for serious applications. They are best positioned out of anyone to make this work - they control the underlying model, after all. But it is still a **bet**. They are betting that over time the issues that plague agents will go away.

Nearly all of the actually useful “autonomous agents” that we see differ in two key regards.

First, many are actually NOT this “agent” cognitive architecture, but rather either elaborate and complex chains, or more similar to “state machines”. Two great public examples of this are [GPT-Researcher](https://github.com/assafelovic/gpt-researcher?ref=blog.langchain.com) and [Sweep.dev](https://sweep.dev/?ref=blog.langchain.com).

We wrote at length about GPT-Researcher [multiple](https://blog.langchain.com/gpt-researcher-x-langchain/) [times](https://blog.langchain.com/exploring-uxs-besides-chat-with-research-assistant/), and worked with them last week to release a [LangChain template](https://github.com/langchain-ai/langchain/tree/master/templates/research-assistant?ref=blog.langchain.com). They are one of the few complex LLM powered applications that produce valuable results, but their cognitive architecture is more like a complex chain. If we look at the diagram below, we can see that it flows in one direction. It does a lot of complex steps, but in defined manner: it first generates sub questions, then gets links for each one, then summarizes each link, then combines the summaries into a research report.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0acc83ac7211fe5742c_68747470733a2f2f636f7772697465722d696d616765732e73332e616d617a6f6e6177732e636f6d2f6172636869746563747572652e706e67--2-.png)The GPT-Researcher cognitive architecture, taken from their GitHub repo.

[Sweep.dev](http://sweep.dev/?ref=blog.langchain.com) is another great example. They wrote a [blog](https://docs.sweep.dev/blogs/sweeps-core-algo?ref=blog.langchain.com) over the summer describing their cognitive architecture, including a fantastic diagram.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0acc83ac7211fe57426_flowchart.15fed92e--2-.svg)Sweep.dev cognitive architecture, taken from their blog.

There are clearly defined transitions and steps. First, a search is done. Then a plan is generated. Then the plan is executed on. There is then a validation step: if it passes, a PR is made and Sweep is done. If it fails, then it makes a new plan. This is a pretty clear state machine, where there are well defined transitions between different states.

Many other builders and teams that we work with have complex chains/state machines powering their applications.

💡

The benefits of these cognitive architectures are simple: **more control**. No two problems are alike and choosing the appropriate cognitive architecture that fits the problem space is critical to delivering a good experience.

For applications that do use something more similar to this agent architecture, they differ from GPTs in another way: how context is provided to the agent.

I was chatting with Flo Crivello about cognitive architectures and he brought up the point that one difference in the agent architecture is how context is provided to the agent. Remember, the way we describe most of the interesting LLM applications is “context-aware reasoning applications”.

💡

Context can either be provided via **pulling** or **pushing**. In most performant and reliable agents, we see a significant amount of context provided by pushing.

What does it mean for an agent to **pull** context? This means that the agent decides what context it needs, and then asks for it. This generally happens via a tool. As a concrete example, an agent created to interact with a SQL database may need to know what tables are present in the SQL database. So we may give it a tool that returns a list of tables in the database, and it can call that tool at the start.

In contrast, when context is **pushed** to the language model it is encoded in the logic of an application that a particular piece context should be fetched and pushed into the prompt. In the example of the SQL agent above, this would correspond to automatically fetching the SQL tables ahead of time and inserting them in the prompt.

Most applications that do use an agent architecture have a significant amount of pushed context. As one example, the [SQL](https://python.langchain.com/docs/integrations/toolkits/sql_database?ref=blog.langchain.com) and [Pandas](https://python.langchain.com/docs/integrations/toolkits/pandas?ref=blog.langchain.com) agents in LangChain have the table schemas as part of the system message. As another example, [the agent that the Rubrics team](https://blog.langchain.com/how-to-design-an-agent-for-production/) built for [Cal.com](http://cal.com/?ref=blog.langchain.com) has a [significant amount of user information pushed into the prompt](https://github.com/calcom/cal.com/blob/main/apps/ai/src/utils/agent.ts?ref=blog.langchain.com).

This **push vs pull** of context again gives developers **more control**. It allows us to enforce what context is relevant to the LLM when deciding what to do. Specifically, knowing what context is most relevant, how to fetch that context, and how to provide it are small decisions that can make a big impact on quality and performance.

GPTs - and to an extent, the Assistant API - largely empower applications with an unconstrained agent architecture that rely more on pulling context as needed. This can be great for getting started quickly or for simple tasks, but for more complex use cases, there’s no substitute for controlling the cognitive architecture that suits the problem at hand.

## Open vs Closed

Aside from the choice of cognitive architecture, another notable attribute of Assistants API and GPTs is that the cognitive architecture itself is **closed**. We do not know what is going on under the hood. We do not know the exact algorithm. We do not know what is being done to manage the context of the chat history. We do not know what is being done for retrieval.

Right now we can make guesses at both of those. However, as they add more and more, and it gets more and more complex, it will become more and more of a black box.

💡

Much of the [discourse around open-source vs closed-source](https://x.com/JosephJacks_/status/1728510229133119644?s=20&amp;ref=blog.langchain.com) revolves around the models themselves. But there is another element to consider: **open-source cognitive architectures vs closed-source cognitive architectures.**

Over time, I bet this will become a larger discussion topic than the models themselves. A year ago, most of the new features (and I would bet most of the focus internally) was on better models. Now, it seems to be a 50/50 split between core model improvements versus figuring out how best to hook them up in an agentic manner. As more evidence of the importance of this, [Karpathy’s Twitter feed](https://twitter.com/karpathy?ref=blog.langchain.com) (the definitive reading list for all things AGI) is shifting more and more towards this idea of the LLM as an OS. Over this past weekend, he released a [fantastic video](https://www.youtube.com/watch?v=zjkBMFhNj_g&amp;ref=blog.langchain.com) on exactly that.

I fully expect this trend to continue, and OpenAI (and perhaps other labs) to invest more in platform and tooling around models, rather than just models themselves. The way to AGI is not (just) in better models - it’s also in hooking them up to their surroundings. As the focus of these labs shift, I expect - and hope - the discourse around open vs closed will happen not just models but also for cognitive architectures.

## Do Cognitive Architectures Make Your Beer Taste Better?

There’s a great quote from Jeff Bezos that says to [only do what makes your beer taste better](https://blog.weaverse.io/make-your-beer-taste-better?ref=blog.langchain.com). This refers to early industrial revolution, when breweries were also making their own electricity. A breweries ability to make good beer doesn’t really depend on how differentiated their electricity was - so those that outsourced electricity generation and focused more on brewing jumped to an advantage.

Is the same true of cognitive architectures? Does having control over your cognitive architecture really make your beer taste better? At the moment, I would argue strongly the answer is yes, for two reasons. First: it’s very difficult to make complex agents actually function. If your application relies on agents working, and getting agents to work is challenging, then almost by definition if you can do that well you’ll have an advantage over your competition. The second reason is that we often see the value of GenAI applications being really closely tied to the performance of the cognitive architecture. A lot of current companies are selling agents for coding, agents for customer support. In those cases, the cognitive architecture IS the product.

That last reason is also the reason that I find it hard to believe that companies would be willing to lock into a cognitive architecture controlled by a single company. I think this is different form of lock-in than cloud or even LLMs. In those cases, you are using cloud resources and LLMs in order to build or power a particular application. But if a cognitive architecture moves closer and closer to being a full application by itself - you’re unlikely to want to have that locked in.

## How LangChain fits in

At LangChain, we believe in a world where LLMs power agent-like systems that are truly transformative. However, we believe the route to get there is one where companies have control over their cognitive architectures.

💡

From everything we’ve seen with working with teams shipping LLM-powered applications, it is really really hard to get agent-like systems working reliably. You can make demos with a general agent architecture, and maybe simple toy apps. But when it comes time to increase performance and run at scale, you NEED to customize it to your application and your use case.

This takes a lot of engineering work. We’re building tools to help with that. With [LCEL](https://python.langchain.com/docs/expression_language/?ref=blog.langchain.com) we have a flexible way to compose chains together. With LangChain we have [over 600 integrations](https://integrations.langchain.com/?ref=blog.langchain.com) allowing for full flexibility in what model/vectorstore/database you use. With [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) we’ve explicitly focused on having the best debugging experience possible (because that’s where most teams are) but we’ve also adding in management tools (regression testing, monitoring, data annotation, prompt hub) to help you manage these systems as you to go production.

We’ve also recently released [OpenGPTs](https://github.com/langchain-ai/opengpts?ref=blog.langchain.com). This is an attempt to recreate the same experience as the Assistants API as well as GPTs (our implementation of GPTs is just a simple UI over the Assistants API). This is open sourced, currently configurable with four different model providers, and the exact retrieval method used can be easily modified.

This is just the start.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd19c522dc1bc339c55041_image--9--1.webp)Harrison&#x27;s In the Loop

#### Your harness, your memory

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseApril 11, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/your-harness-your-memory)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b40927fd1d366828376_HFEylQUaIAAA88g.webp)Harrison&#x27;s In the Loop

#### Continual learning for AI agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseApril 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/continual-learning-for-ai-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)