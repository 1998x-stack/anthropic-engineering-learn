---
title: "Human-in-the-loop with OpenGPTs and LangGraph"
author: "LangChain Accounts"
date: "2024-02-08"
url: "https://www.langchain.com/blog/human-in-the-loop-with-opengpts-and-langgraph"
---

Company AnnouncementsLangChain

# Human-in-the-loop with OpenGPTs and LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 8, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0374cf06727c05d6a53_opengpts-authorize-1.png)**TLDR; Today we’re launching two “human in the loop” features in OpenGPTs, Interrupt and Authorize, both powered by LangGraph.**

We&#x27;ve recently launched LangGraph, a library to help developers build multi-actor, multi-step, stateful LLM applications. That&#x27;s a lot words packed into a short sentence, let&#x27;s take it one at a time

## Multi-actor

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0384cf06727c05d6a81_opengpts-multi-actor.png)

A team of specialists can build something together that none of them could build alone. The same is true of LLM applications: an LLM (great at answer generation and task planning) is much more powerful when paired up with a search engine (best at finding current facts). We have seen folks build some amazing applications, like perplexity or arc search, when they combine those two building blocks (and others) in novel ways.

And just as a human team needs more coordination than one person working by themselves, an application with multiple actors needs a coordination layer to

- define the actors involved (the nodes in a graph) and how they handoff work to each other (the edges in that graph)
- schedule execution of each actor at the appropriate time, in parallel if needed, with deterministic results

## Multi-step

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0384cf06727c05d6a84_opengpts-multi-step.png)

As each actor hands off work to another (eg. an LLM prompt asking a search tool for results on a query) we need to make sense of the back-and-forth between multiple actors – what order does it happen in, how many times is each actor called, etc. To do this we can model the interaction between the actors as happening across multiple discrete steps, when one actor hands off work to another actor, that results in the scheduling of the next step of the computation, and so on, until no more actors hand off work to others, and we’ve reached the final result.

## Stateful

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0384cf06727c05d6a8a_opengpts-stateful.png)

Communication across steps implies updating of some state, otherwise when you call the LLM actor the 2nd time you’d get the same result as the first time. Turns out it’s very helpful to pull this state out of each of the actors, so that all actors collaborate on updating a single central state. With a single central state we can also easily snapshot it and store during or after each computation.

# Human-in-the-loop

A single shared state makes the process easier to observe, interrupt and modify. Which is very important for complex LLM applications, where some amount of human supervision/approval/editing can be the difference between a toy and a deployment useful in the real world. We’re introducing support for two forms of Human in the Loop in OpenGPTs, powered by LangGraph – Interrupt and Authorize.

### Interrupt

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0384cf06727c05d6a87_opengpts-interrupt.png)

The first mode, Interrupt, is the simplest form of control – the user is looking at streaming output of the application as it is produced, and manually interrupts it when he sees fit. The state is saved as of the last complete step prior to the user hitting the interrupt button. From there the user can choose to

- resume from that point onwards, and the computation will proceed as if it hadn’t been interrupted, or
- send new input into the application (eg. a new message in a chatbot), which will cancel any future steps that were pending, and start dealing with the new input, or
- do nothing, and nothing else will run.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0384cf06727c05d6a9e_Screenshot-2024-02-07-at-8.38.09-AM.png)

### Authorize

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0374cf06727c05d6a53_opengpts-authorize-1.png)

A 2nd control mode is Authorize, where the user defines ahead of time that they want the application to hand off control to them every time a particular actor is about to be called. In OpenGPTs we’ve implemented this mode for Tool Confirmation – when this mode is turned on, before any tool is called the application will pause and ask for confirmation, at which point the user can, again

- resume computation, accepting the tool call
- send a new message to guide the bot in a different direction, in which case the tool will not be called
- or, do nothing.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0394cf06727c05d6aac_Screenshot-2024-02-07-at-8.38.52-AM.png)

### Where to find this

You can go here to [demo](https://opengpts-example-vz4y4ooboq-uc.a.run.app/?ref=blog.langchain.com) OpenGPTs and here to [fork](https://github.com/langchain-ai/opengpts?ref=blog.langchain.com) it.

You can find an example notebook [here](https://github.com/langchain-ai/langgraph/blob/main/examples/human-in-the-loop.ipynb?ref=blog.langchain.com) for building your own LangGraph application with Human-in-the-loop controls.

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