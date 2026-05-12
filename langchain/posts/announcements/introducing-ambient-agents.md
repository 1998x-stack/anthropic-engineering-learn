---
title: "Introducing ambient agents"
author: "LangChain Accounts"
date: "2025-01-14"
url: "https://www.langchain.com/blog/introducing-ambient-agents"
---

Harrison&#x27;s In the LoopLangGraph

# Introducing ambient agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseJanuary 14, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae13cbdf13f9a16535fc_Theme-Digital-Nebula--Format-Blog--Colour-Blue--Text-Alignment-Centred--With-Image-Text-Only.png)Most AI apps today follow a familiar chat pattern ([&quot;chat&quot; UX](https://blog.langchain.com/ux-for-agents-part-1-chat-2/)). Though easy to implement, they create unnecessary interaction overhead, limit the ability of us humans to scale ourselves, and fail to use the full potential of LLMs.

Over the past six months, we&#x27;ve been exploring a different approach at LangChain: agents that respond to ambient signals and demand user input only when they detect important opportunities or require feedback. Rather than forcing users into new chat windows, these agents help save your attention for when it matters most.

We built [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) to make these patterns easy to implement. Today we&#x27;re sharing our first reference implementation: an [email assistant](https://github.com/langchain-ai/executive-ai-assistant?ref=blog.langchain.com) that demonstrates key ambient agent patterns. Over the next few days, we&#x27;ll release additional examples and tooling to help you build your own ambient workflows.

## What is an ambient agent?

When using ChatGPT (or any other chatbot), they rely on you to initiate the conversation. The agent is kicked off by the human sending a message.

This is great for some use cases, but also severely limiting for others. It requires the user to go into the chat interface and send a message every time they want the agent to do work. There is a lot of overhead in having the agent start work.

An additional limitation is you can only have one conversation at a time. This makes it hard for us humans to scale ourselves - an agent can only be doing one thing for us at a time.

If we think about a UX paradigm that allows us to overcome these limitations, it should exhibit two key characteristics:

- It should not (solely) be triggered by human messages
- It should allow for multiple agents running simultaneously

The characteristics define what we call *ambient agents*.

💡

Ambient agents listen to an event stream and act on it accordingly, potentially acting on multiple events at a time

Notably, however, we do not think that ambient agents are necessarily completely autonomous. In fact, we think a key part of bringing ambient agents to the public will be thoughtful consideration as to *when* and *how *these agents interact with humans.

## Human-in-the-loop

We use human-in-the-loop to refer to *when* and *how* these agents interact with humans. We&#x27;ll talk about *how* later, but for now let&#x27;s discuss the *when*.

We typically see three common human-in-the-loop patterns for ambient agents: notify, question, and review.

**Notify:** let the user know some event is important, but not take any actions. This is useful in flagging events that user should see, but where the agent is not empowered to act them. In the context of an email assistant, this could be the agent flagging a Docusign in my inbox - it&#x27;s not able to sign that Docusign, but I should know it exists.

**Question:** ask the user a question to help unblock the agent. The agent may be trying to take some actions, but unclear on how best to do so because it&#x27;s lacking some relevant information. Rather than hallucinate or guess, you just have the agent ask the human what to do. In the context of an email assistant, this could be an agent asking me whether I want to go to a conference. Unless something was in the prompt to instruct the agent on my conference preferences, there&#x27;s no way it should know that. A human EA would ask me, and so should an agentic one.

**Review:** review an action the agent wants to take. Some actions are &quot;dangerous&quot; enough that it may be worth hard coding a review for any action the agent wants to take. The human can either approve the action, edit it directly, or give direct feedback to the agent on how to change it. In the context of an email assistant, this could be an outbound email. It might write a draft, but I would have to approve it, edit the message content directly, or tell the agent to fix it in a certain way.

## The importance of human-in-the-loop

We think this human-in-the-loop component brings three key benefits to ambient agents:

- It lowers the stakes, making it easier to ship agents to production
- It mimics how humans communicate, building user trust and adoption
- It empowers long term memory and learning

**Human-in-the-loop lowers the stakes. **If an agent is running fully autonomously in the background, then it really can&#x27;t make a mistake. You would have to trust the agent immensely before letting it take certain actions (like updating a database, sending an email to an important client, etc). With human-in-the-loop, you can easily gate those actions and require explicit human approval. This way you can be sure that no errant email will get sent.

**Human-in-the-loop mimics how humans communicate. **A big part of working with someone else is communicating with them. Asking them questions when you&#x27;re unsure, running ideas by them. If we have &quot;co-workers&quot; that are agents, having them communicate in similar patterns builds user trust and therefor adoption. Consider something like [Devin](https://devin.ai/?ref=blog.langchain.com). One of the primary interfaces they chose for users to interact with Devin is in Slack. That&#x27;s where we interact with human developers, why shouldn&#x27;t we interact with AI developers in that way? Communication is important.

**Human-in-the-loop empowers long term memory and learning. **We strongly believe that a key part of AI agents is their ability to learn over time and better align themselves with their human users. In order for this alignment to happen, they need some form of user feedback. This human-in-the-loop component provides this feedback.

## Agent Inbox

So we talked about *when* agents should communicate with humans (**notify**, **question**, **review**), but we didn&#x27;t talk about *how* they should.

When experimenting with ambient agents we initially started with Slack. The main benefit of this is that we&#x27;re all already in Slack for our day-to-day work, so its an efficient way to get our attention and centralized with our human &lt;&gt; human communication.

The downside of Slack is that it&#x27;s easy to lose track of all the notifications. If you don&#x27;t respond to a few, the a backlog of slack notifications grows. A slack channel (or DM) isn&#x27;t the easiest to navigate. It is also constrictive in how you can communicate with agents - you can message them easily, but anything else is a bit tricker.

We moved onto what we dubbed an &quot;Agent Inbox&quot;. This is new UX for interacting with ambient agents. It&#x27;s modeled after some combination of an email inbox and a customer support ticketing system. It displays all open lines of communication between you and an agent - making it easy to track any outstanding actions. It&#x27;s a standalone UI, making it easy to add any panels, buttons, or other UI features that allow you to more easily capture user feedback. Right now items are sorted just by time, but in the future you&#x27;ll be able to sort it based on priority. Right now this inbox is single player, but in the future you&#x27;ll be able to see which items are assigned to you versus others.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae13cbdf13f9a1653602_Screenshot-2025-01-09-at-4.42.45-PM.png)

*Note: an open source implementation of the agent inbox will be released Thursday.*

## Why LangGraph is great for ambient agents

As we&#x27;ve been building ambient agents, we&#x27;ve made sure that [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) is equipped to support these types of agents. There are a few key characteristics that LangGraph (and [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/?ref=blog.langchain.com#langgraph-platform)) have that you probably don&#x27;t want to build yourself:

**Built in **[**persistence layer**](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com)**. **LangGraph is backed by a persistence layer that saves the state of the agent between each action (or node of the graph). This allows the agent to essentially &quot;pause&quot; and wait for user feedback. This is important for enabling human-in-the-loop interaction patterns as well as short term conversational memory.

**Built in **[**human-in-the-loop support**](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?ref=blog.langchain.com)**. **LangGraph supports human-in-the-loop patterns natively. The built in persistence layer is a big part, but we also recently added [&quot;interrupt&quot;](https://langchain-ai.github.io/langgraph/reference/types/?ref=blog.langchain.com#langgraph.types.interrupt), a new built-in method for communicating with the end user.

**Built in **[**long-term memory**](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#long-term-memory)**. **LangGraph comes with built in long-term memory (essentially a namespaced, key-value store that supports semantic search). This makes it easy for agents to update their &quot;memory&quot; after human-in-the-loop interactions.

[**Cron jobs**](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/?ref=blog.langchain.com#cron-jobs)**. **Many ambient agents run on a schedule to check for new events. LangGraph Platform comes with built in cron jobs to support this.

## Building an AI email assistant

We&#x27;ve made LangGraph great for building ambient agents by building ambient agents that we use every day. One of the main ones is an [email assistant](https://github.com/langchain-ai/executive-ai-assistant?ref=blog.langchain.com). If you&#x27;ve corresponded with me in the past six months, there&#x27;s a good chance an AI agent drafted that email (and if I&#x27;ve ignored you - it&#x27;s definitely the AI agent&#x27;s fault).

Today we&#x27;re launching that email assistant, both as a free-to-use hosted email agent, but also an [open source project](https://github.com/langchain-ai/executive-ai-assistant?ref=blog.langchain.com). We&#x27;re hopeful the hosted email agent makes it easy to try out and experience ambient agents, and the open source version serves as a reference implementation for this new design paradigm.

Hosted Email Assistant

- [Platform](https://www.agentinbox.ai/?ref=blog.langchain.com)
- [Instructions](https://mirror-feeling-d80.notion.site/AI-Email-Assistant-How-to-hire-and-communicate-with-an-AI-Email-Assistant-17b808527b178019a42af932bb64badd?pvs=4&amp;ref=blog.langchain.com)
- [YouTube Walkthrough](https://youtu.be/-SZkNdmtZ7k?ref=blog.langchain.com)

OSS Email Assistant

- [Code](https://github.com/langchain-ai/executive-ai-assistant?ref=blog.langchain.com)
- [YouTube Walkthrough](https://youtu.be/1A79eYjiBvo?ref=blog.langchain.com)

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