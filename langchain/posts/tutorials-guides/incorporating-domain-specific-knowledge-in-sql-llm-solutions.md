---
title: "Incorporating domain specific knowledge in SQL-LLM solutions"
author: "LangChain Accounts"
date: "2023-09-05"
url: "https://www.langchain.com/blog/incorporating-domain-specific-knowledge-in-sql-llm-solutions"
---

Partner

# Incorporating domain specific knowledge in SQL-LLM solutions

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 5, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb187f3571add5bcb596b_5-social--18-.png)*Editor&#x27;s Note: This post was written in collaboration with *[*Manuel*](https://twitter.com/manuelsoria_?ref=blog.langchain.com)* and *[*Francisco*](https://twitter.com/fpingham?ref=blog.langchain.com)* from the *[*Pampa Labs team*](https://www.pampa.ai/?ref=blog.langchain.com)*. We&#x27;re always excited to see new best practices emerge for more customizing/personalizing apps more thoroughly, and this post about extending the capabilities of the standard SQL toolkit by applying innovative RAG techniques is an awesome example. *

The LangChain library provides different tools to interact with SQL databases which can be used to build and run queries based on natural language inputs. For example, the standard SQL Toolkit draws from standard best practices that have been extensively covered in this[ blogpost](https://blog.langchain.com/llms-and-sql/). However, there is still room for improvement when it comes to building a custom solution and adjusting the generic tools to the specific use case. The advantage of having a *plug and play *toolkit contrasts with having a solution that is not flexible enough for the user to incorporate their domain-specific knowledge about the databases.

We can extend the out-of-the-box SQL Toolkit with extra custom tools which leverage domain specific knowledge. In this way, we get the best of both worlds: anyone can run the standard SQL Agent with minimal setup while at the same time being able to incorporate extra tools that add relevant information to the prompt at inference time. In this blogpost we will cover how to expand the standard SQL Toolkit with some very useful example extra tools.

# The Problems

Using the standard SQL Toolkit, an agent is able to construct and run queries to provide answers to user questions. Although this toolkit is robust enough for building a first out-of-the-box prototype by just connecting to a database, someone trying to use it with a complex enough database faces at least one of the following problems:

- Queries not generated correctly, leading to various retries until getting the right query.
- Excessive use of the tools, making the whole thinking process very inefficient in terms of time and tokens.
- Very extensive prompts with information that is not always relevant to the specific user question.

The underlying cause behind these problems is that we are trying to build a custom solution just using generic tools, without leveraging the fact that we *do *know the nuances of the use case. Therefore, we need to find a way of enhancing the agent with domain specific knowledge, without having to hardcode anything in the prompt template.

# Extending the SQL Toolkit

It has been [proven](https://arxiv.org/abs/2204.00498?ref=blog.langchain.com) that feeding the prompt with database information is crucial for constructing the right SQL query. This is why the toolkit enables the agent to get information about the table names, the schema, sample rows, etc. However, all these tools can do is retrieve information about the database, akin to how a data scientist would approach a new dataset during their initial interaction.

But what if it’s not the first interaction?

Anyone crafting an LLM-SQL solution brings a wealth of domain-specific knowledge to the table.  They know which questions are typically hard to translate into queries, as well as when and what supplementary information should be incorporated into the prompt. This becomes especially crucial in scenarios where simply using the standard toolkit falls short. Such insights can be dynamically included into the prompt using **Retrieval Augmented Generation, **which involves semantically searching in a vector database and retrieving relevant data.

## Including few shot examples

Feeding the prompt with *few-shot *examples of **question-query matches** [improves the query generation accuracy.](https://arxiv.org/abs/2204.00498?ref=blog.langchain.com) This can be achieved by simply appending standard static examples in the prompt to guide the agent on how it should build queries based on questions. However, a more powerful approach is to have a robust dataset of good examples, and *dynamically *include those which are relevant to the user question.

To achieve this, we need a custom Retriever Tool that handles the vector database in order to retrieve the examples that are semantically similar to the user’s question. The agent can even decide whether it needs to use other tools or not.

Let’s see an example!

`agent.run(&quot;How many employees do we have?&quot;)
&gt; Entering new AgentExecutor chain...
Invoking: `sql_get_similar_examples` with `How many employees do we have?`
[Document(page_content=&#x27;How many employees are there&#x27;, metadata={&#x27;sql_query&#x27;: &#x27;SELECT COUNT(*) FROM &quot;employee&quot;&#x27;}), Document(page_content=&#x27;Which employee has sold the most?&#x27;, metadata={&#x27;sql_query&#x27;: &quot;SELECT e.FirstName || &#x27; &#x27; || e.LastName AS EmployeeName, SUM(i.Total) AS TotalSales\n            FROM Employee e\n            JOIN Customer c ON e.EmployeeId = c.SupportRepId\n            JOIN Invoice i ON c.CustomerId = i.CustomerId\n            GROUP BY e.EmployeeId\n            ORDER BY TotalSales DESC\n            LIMIT 1;&quot;})]
Invoking: `sql_db_query` with `SELECT COUNT(*) FROM employee`
responded: {content}
[(8,)]We have 8 employees.
&gt; Finished chain.
`

## Finding misspellings in proper nouns

Another nice use case of applying RAG in LLM-SQL solutions is for making a system robust to misspellings. When querying for proper nouns like names or countries, a user may inadvertently write a proper noun wrongly and the system will not be able to find it in the database (e.g. ‘Franc Sinatra’).

How can we solve this problem?

One way to approach this problem is to create a vector store using all the distinct proper nouns that exist in the database. We can then have the agent query that vector store each time the user includes a proper noun in their question, to find the correct spelling for that word. In this way, the agent can make sure it understands which entity the user is referring to before building the target query.

Let’s see an example!

``
sql_agent(&quot;What is &#x27;Francis Trembling&#x27;s email address?&quot;)

Invoking: `name_search` with `Francis Trembling`

[Document(page_content=&#x27;François Tremblay&#x27;, metadata={}), Document(page_content=&#x27;Edward Francis&#x27;, metadata={}), Document(page_content=&#x27;Frank Ralston&#x27;, metadata={}), Document(page_content=&#x27;Frank Harris&#x27;, metadata={}), Document(page_content=&#x27;N. Frances Street&#x27;, metadata={})]
Invoking: `sql_db_query_checker` with `SELECT Email FROM Customer WHERE FirstName = &#x27;François&#x27; AND LastName = &#x27;Tremblay&#x27; LIMIT 1`
responded: {content}

SELECT Email FROM Customer WHERE FirstName = &#x27;François&#x27; AND LastName = &#x27;Tremblay&#x27; LIMIT 1
Invoking: `sql_db_query` with `SELECT Email FROM Customer WHERE FirstName = &#x27;François&#x27; AND LastName = &#x27;Tremblay&#x27; LIMIT 1`

[(&#x27;ftremblay@gmail.com&#x27;,)]The email address of &#x27;François Tremblay&#x27; is &#x27;ftremblay@gmail.com&#x27;.

&gt; Finished chain.

{&#x27;input&#x27;: &quot;What is &#x27;Francis Trembling&#x27; email address?&quot;,
 &#x27;output&#x27;: &quot;The email address of &#x27;François Tremblay&#x27; is &#x27;ftremblay@gmail.com&#x27;.&quot;}

`

*Implementation note: when instructing the LLM to use tools in one order or another, we found it was usually more effective to instruct this in the agent’s prompt rather than in the tool’s description - for more information please refer to the SQL use case in the docs.*

##
Going further

As well as these best practices improve the standard SQL Toolkit by leveraging the developer’s field-specific knowledge, there is still room for improvement in terms of accuracy and cost.

Some examples on enhancing the few-shot approach include:

- Applying a **similarity threshold** to decide whether the retrieved examples are related enough to be included in the prompt (e.g. a new question which is very different to other questions, shouldn’t retrieve any examples).
- Similarly, setting a threshold to decide if the **examples are *far too related****, *and no other tools should be used, thus saving a lot of time &amp; tokens (e.g. just adjusting a column filter, just having a related example is enough and no other tools should be necessary).
- Prioritizing **diversity of the few-shot examples** in order to cover a wider area of examples, as covered in the following [paper by Hongjin Su et al](https://arxiv.org/abs/2209.01975?ref=blog.langchain.com).

Also, some examples which aren’t strictly related to the few-shot examples but do involve using RAG include:

- Retrieving all values from a relevant categoric column if the user’s question involves filtering a column (e.g. a product name).
- Adjusting sample rows to show only the columns that are relevant to the user question.

If you want to help implementing any of these or have other best practices that you found helpful, don’t hesitate to join the discussion in the #sql [channel](https://discord.com/channels/1038097195422978059/1080206362669224027?ref=blog.langchain.com) in Discord!

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