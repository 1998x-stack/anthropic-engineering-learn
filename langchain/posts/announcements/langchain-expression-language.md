---
title: "LangChain Expression Language"
author: "LangChain Accounts"
date: "2023-08-01"
url: "https://www.langchain.com/blog/langchain-expression-language"
---

Company Announcements

# LangChain Expression Language

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 1, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e2c83ac7211fe5d8c4_photo-1619431843665-54babc76ac8c.jpeg)**TL;DR:**

- **We’re excited to announce a new **[**syntax**](https://python.langchain.com/docs/guides/expression_language/?ref=blog.langchain.com)** to create chains with composition. This comes along with a new interface that supports batch, async, and streaming out of the box. We’re calling this syntax LangChain Expression Language (LCEL)**
- **We&#x27;ve created a &quot;**[**LangChain Teacher**](https://langchain-teacher-lcel.streamlit.app/?ref=blog.langchain.com)**&quot; to help teach you LCEL (assumes LangChain familiarity)**
- **We&#x27;ll be doing a **[**webinar**](https://www.crowdcast.io/c/ckw1tydg29er?ref=blog.langchain.com)** on 8/2 about this and how to use it**
- **This is aimed at making it easier to construct complex chains, and pairs nicely with **[**LangSmith**](https://blog.langchain.com/announcing-langsmith/)** - the platform we recently released aimed at making it easier to go from prototype to production.**

The idea of chaining has proven popular when building applications with language models. Chaining can come in a few different forms, each with their own benefits. Some examples of these are:

**Making Multiple LLM Calls**

Chaining can mean making multiple LLM calls in a sequence. Language models are often non deterministic and can make errors, so making multiple calls to check previous outputs or to break down larger tasks into bite-sized steps can improve results.

**Constructing the Input to LLMs**

Chaining can mean combining data transformation with a call to an LLM. For example, formatting a prompt template with user input or using retrieval to look up additional information to insert into the prompt template. This is necessary because you often need data from multiple sources to perform a task, which may be fetched at runtime conditional on the input.

**Using the Output of LLMs**

Another form of chaining refers to passing the output of an LLM call to a downstream application. For example, using the LLM to generate Python code and then running that code; using the LLM to generate SQL and then executing that against a SQL database.

There’s also something about working with language models that makes the idea of chaining appealing. Sure, all the above operations could be done with code, but people have gravitated towards the idea of chaining - as evidenced by the multitude of low-code/no-code platforms for building language model applications (some like [Flowwise](https://flowiseai.com/?ref=blog.langchain.com) and [LangFlow](https://github.com/logspace-ai/langflow?ref=blog.langchain.com) built on top of LangChain). Why? It’s become a bit of a meme, but if [text is the universal interface](https://scale.com/blog/text-universal-interface?ref=blog.langchain.com), and all of these operations involve manipulation of text, then this sets itself up incredibly naturally for an expression language to support this.

LangChain was born from the idea of making these types of operations easy. We saw people doing common patterns and factored them out into pre-built chains: LLMChain, ConversationalRetrievalChain, SQLQueryChain.

But these chains weren’t really composable. Sure - we had SequentialChain, but that wasn’t amazingly usable. And under the hood the other chains involved a lot of custom code, which made it tough to enforce a common interface for all chains, and ensure that all had equal levels of batch, streaming, and async support.

Today we’re excited to announce a new way of constructing chains. We’re calling this the LangChain Expression Language (in the same spirit as [SQLAlchemyExpressionLanguage](https://docs.sqlalchemy.org/en/14/core/tutorial.html?ref=blog.langchain.com)). This is a declarative way to truly compose chains - and get streaming, batch, and async support out of the box. You can use all the same existing LangChain constructs to create them.

We’ve included guides on [how to work with the interface](https://python.langchain.com/docs/guides/expression_language/interface?ref=blog.langchain.com) as well as [some examples of using it](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com). Let’s take a look at one of the more common ways below:

`from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template(&quot;tell me a joke about {foo}&quot;)
chain = prompt | model

chain.invoke({&quot;foo&quot;: &quot;bears&quot;})
&gt;&gt;&gt; AIMessage(content=&quot;Why don&#x27;t bears ever wear shoes?\n\nBecause they have bear feet!&quot;, additional_kwargs={}, example=False)
`

This uses a standard ChatOpenAI model and prompt template. You chain them together with the `|` operator, and then call it with `chain.invoke`. We can also get async, batch, and streaming support out of the box.

**Batch**

`batch` takes in a list of inputs. If optimizations can be done internally (like literally batching calls to LLM providers) those are done.

`chain.batch([{&quot;foo&quot;: &quot;bears&quot;}, {&quot;foo&quot;: &quot;cats&quot;}])
&gt;&gt;&gt; [AIMessage(content=&quot;Why don&#x27;t bears ever wear shoes?\n\nBecause they have bear feet!&quot;, additional_kwargs={}, example=False),
 AIMessage(content=&quot;Why don&#x27;t cats play poker in the wild?\n\nToo many cheetahs!&quot;, additional_kwargs={}, example=False)]`

**Stream**

`stream` returns an iterable that you can consume.

`for s in chain.stream({&quot;foo&quot;: &quot;bears&quot;}):
    print(s.content, end=&quot;&quot;)`

**Async**

All of `invoke`, `batch`, and `stream` expose async methods. We only show `ainvoke` here for simplicity, although you can check out our notebook that deep dives into the interface to see more.

`await chain.ainvoke({&quot;foo&quot;: &quot;bears&quot;})`

In our cookbook we’ve included examples of doing this with:

- [Multiple LLM calls](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#multiple-llm-chains)
- [Function calling](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#attaching-function-call-information)
- [Retrieval](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#llmchain--retriever)
- [Arbitrary Functions](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#arbitrary-functions)
- [SQL Database query](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#sql-database)
- [Python execution](https://python.langchain.com/docs/guides/expression_language/cookbook?ref=blog.langchain.com#code-writing)

We’ll be constantly beefing up support for this and adding more examples of functionality, so let us know what you’d like to see. We&#x27;ll also be incorporating this more into LangChain - already the [`create_sql_query_chain`](https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/chains/sql_database/query.py?ref=blog.langchain.com) uses this under the hood.

Besides the benefit of adding standard interfaces, another benefit is that this will make it easier for users to customize parts of the chain. Since the chain is expressed in such a declarative and composable nature, it will be much more clear how to swap certain components out. It also now brings the prompts front and center - making it more clear how to modify those. The prompts in LangChain are just defaults, and are largely intended to be modified for your particular use case if you are seriously trying to take an application into production. Previously, the prompts were a bit hidden and hard to change. With LCEL, they are more prominent and easily swappable.

LangChain Expression Language creates chains that integrate seamlessly with LangSmith. Here is a trace for the above:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e2c83ac7211fe5d8ca_screenshot-2023-07-28-at-6.16.58-pm.png)

You can inspect the trace [here](https://smith.langchain.com/public/779f432a-fa8c-4b85-bf7d-3dca9a8c569c/r?ref=blog.langchain.com). Previously, when creating a custom chain there was actually a good bit of work to be done to make sure callbacks were passed through correctly so that it could be traced correctly. With LangChain Expression Language that happens automatically.

We&#x27;ve also tried to make this as easy as possible for people to learn by creating a &quot;LangChain Teacher&quot; application that will walk you through the basics of getting started with LangChain Expression Language. You can access it [here](https://langchain-teacher-lcel.streamlit.app/?ref=blog.langchain.com). We&#x27;ll be open sourcing this soon.

We&#x27;ll also be doing a webinar on this tomorrow. We&#x27;ll cover the standard interface it exposes, how to use it, and why to use it. Register for that [here](https://www.crowdcast.io/c/ckw1tydg29er?ref=blog.langchain.com).

We&#x27;re incredibly excited about this being an easy and lightweight way to truly compose chains together. If you&#x27;re excited as well, we&#x27;re hiring for roles that would work directly on this. The best way to get our attention is to open a PR or two adding more functionality. There&#x27;s still a lot to build :)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)