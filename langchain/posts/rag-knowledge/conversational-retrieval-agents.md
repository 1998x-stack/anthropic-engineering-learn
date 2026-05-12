---
title: "Conversational Retrieval Agents"
author: "LangChain Accounts"
date: "2023-08-03"
url: "https://www.langchain.com/blog/conversational-retrieval-agents"
---

LangChain

# Conversational Retrieval Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 3, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1ddc588d5fac7b9020a_photo-1625794084867-8ddd239946b1.jpeg)**TL;DR: There have been several emerging trends in LLM applications over the past few months: RAG, chat interfaces, agents. Our newest functionality - conversational retrieval agents - combines them all. This isn&#x27;t just a case of combining a lot of buzzwords - it provides real benefits and superior user experience.**

**Key Links:**

- [**Python Documentation**](https://python.langchain.com/docs/use_cases/question_answering/how_to/conversational_retrieval_agents?ref=blog.langchain.com)
- [**JavaScript Documentation**](https://js.langchain.com/docs/use_cases/question_answering/conversational_retrieval_agents?ref=blog.langchain.com)
- [**End-to-end example**](https://github.com/hwchase17/conversational-retrieval-agent?ref=blog.langchain.com)

As LLM applications are starting to make their way into more and more production use cases, a few common trends are starting emerge:

**Retrieval Augmented Generation**

LLMs only know what they are trained on. To combat this, a style of generation known as &quot;retrieval augmented generation&quot; has emerged. In this technique, documents are retrieved and then inserted into the prompt, and the language model is instructed to only respond based on those documents. This helps both in giving the language model additional context as well as in keeping it grounded.

**Chat Interfaces**

With the explosion of ChatGPT, chat interfaces have emerged as the dominant way with which to interact with language models. The ability to ask follow up questions about a previous response - especially as context windows grow longer and longer - proves invaluable.

**Agents**

The term agents may be overloaded by now. By &quot;agents&quot; we mean a system where the sequence of steps is NOT known ahead of time, but is rather determined by a language model. This can allow the system greater flexibility in dealing with edge cases. However, if unbounded it can become quite unreliable.

At LangChain, we have had components for these trends from the very beginning. One of our first applications built was a `RetrievalQA` system over a Notion database. We&#x27;ve experimented and pushed the boundary with many different forms of memory, enabling chatbots of all kinds. And - of course - we&#x27;ve got many types of agents, from the &quot;old&quot; ones that use ReAct style prompting, to newer ones powered by OpenAI Functions.

We&#x27;ve also combined these ideas before. `ConversationalRetrievalQA` - a chatbot that does a retrieval step to start - is one of our most popular chains. From almost the beginning we&#x27;ve added support for memory in agents.

Yet we&#x27;ve never really put all three of these concepts together. Until now. With our conversational retrieval agents we capture all three aspects. Let&#x27;s dive into what exactly this consists of, and why this is the superior retrieval system.

The basic outline of this system involves:

- An OpenAI Functions agent
- Tools that are themselves `retrievers` - they take in a string, and return a list of documents
- A new type of memory that not only remembers `human &lt;-&gt; ai` interactions, but also `ai &lt;-&gt; tool` interactions

The agent can then decide when to call the retrieval system if at all. If it does, the retrieved documents are returned and it can use them to reason about what to do next, whether it be respond directly or do a different retrieval step. Note that this relies upon a few things:

- Longer context windows: if context windows are short, then you can&#x27;t just return all the documents into the agent&#x27;s working memory
- Better language models: if language models aren&#x27;t good enough to reason about when they should retrieve documents, then this won&#x27;t work

Luckily, language models are getting better and getting longer context windows!

Here&#x27;s a LangSmith trace showing how it looks in action:
[https://smith.langchain.com/public/1e2b1887-ca44-4210-913b-a69c1b8a8e7e/r](https://smith.langchain.com/public/1e2b1887-ca44-4210-913b-a69c1b8a8e7e/r?ref=blog.langchain.com)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1dec588d5fac7b90216_screenshot-2023-08-02-at-10.29.17-pm.png)

Let&#x27;s compare this to the `ConversationalRetrievalQA` chain that most people use. The benefits that a conversational retrieval agent has are:

- Doesn&#x27;t always look up documents in the retrieval system. Sometimes, this isn&#x27;t needed! If the user is just saying &quot;hi&quot;, you shouldn&#x27;t have to look things up
- Can do multiple retrieval steps. In `ConversationalRetrievalQA`, one retrieval step is done ahead of time. If that retrieval step returns bad results, then you&#x27;re out of luck! But with an agent you can try a different search query to see if that yields better results
- With this new type of memory, you can maybe avoid retrieval steps! This is because it remembers `ai &lt;-&gt; tool` interactions, and therefore remembers previous retrieval results. If a follow-up question the user asks can be answered by those, there&#x27;s no need to do another retrieval step!
- Better support for meta-questions about the conversation - &quot;how many questions have I asked?&quot;, etc. Because the old chain dereferences questions to be &quot;standalone&quot; and independent of the conversation history in order to query the vector store effectively, it struggles with this type of question.

Note, that there are some downsides/dangers:

- With agents, they can occasionally spiral out of control. That&#x27;s why we&#x27;ve added controls to our AgentExecutor to cap them at a certain max amount of steps. It&#x27;s also worth noting that this is a VERY focused agent, in that it&#x27;s only given one tool (and a pretty simple tool at that). In general, the fewer (and simpler) tools an agent is given, the more likely it is to be reliable.
- By remembering `ai &lt;-&gt; tool` interactions, that can hog the context window occasionally. That&#x27;s why we&#x27;ve included a flag to disable that type of memory, and more generally have made memory pretty plug-and-play.

This new agent is in both Python and JS - you can use these guides to get started:

- [JS](https://js.langchain.com/docs/use_cases/question_answering/conversational_retrieval_agents?ref=blog.langchain.com)
- [Python](https://python.langchain.com/docs/use_cases/question_answering/how_to/conversational_retrieval_agents?ref=blog.langchain.com)

LLM applications are rapidly evolving. Our NotionQA demo was one of the first we did - and although it was only ~9 months ago the best practices have shifted dramatically since then. This currently represents our best guess at what a GenAI question-answering system should look like, combining the grounded-ness of RAG with the UX of chat and the flexibility of agents.

We&#x27;ve got a few more ideas on how this can be further improved - we&#x27;ll be rolling those out over the next few weeks. As always, we&#x27;d love to hear from you with any suggestions or ideas.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)