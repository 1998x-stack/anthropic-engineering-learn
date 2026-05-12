---
title: "LLMs and SQL"
author: "LangChain Accounts"
date: "2023-03-13"
url: "https://www.langchain.com/blog/llms-and-sql"
---

Tutorials &amp; How-TosLangChainOpen Source

# LLMs and SQL

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 13, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)8min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb24cba9d0fc7237831f8_photo-1532619675605-1ede6c2ed2b0.jpeg)[Francisco Ingham](https://twitter.com/fpingham?ref=blog.langchain.com) and [Jon Luo](https://twitter.com/JonZluo?ref=blog.langchain.com) are two of the community members leading the change on the SQL integrations. We’re really excited to write this blog post with them going over all the tips and tricks they’ve learned doing so. We’re even more excited to announce that we’ll be doing an hour long webinar with them to discuss these learnings and field other related questions. This webinar will be on March 22nd - sign up at the below link:

- [Webinar Link](https://www.crowdcast.io/c/fgxa65bugxk4?ref=blog.langchain.com)

The LangChain library has multiple SQL chains and even an SQL agent aimed at making interacting with data stored in SQL as easy as possible. Here are some relevant links:

- [Python SQL Chains](https://python.langchain.com/docs/modules/chains/popular/sqlite?ref=blog.langchain.com)
- [Python SQL Agents](https://python.langchain.com/docs/modules/agents/toolkits/sql_database?ref=blog.langchain.com)
- [Javascript SQL Chains](https://hwchase17.github.io/langchainjs/docs/modules/chains/sql_db?ref=blog.langchain.com)
- [Javascript SQL Agents](https://hwchase17.github.io/langchainjs/docs/modules/agents/agent_toolkits/sql?ref=blog.langchain.com)

## Introduction

Most of an enterprise’s data is traditionally stored in SQL databases. With the amount of valuable data stored there, business intelligence (BI) tools that make it easy to query and understand the data present there have risen in popularity. But what if you could just interact with a SQL database in natural language? With LLMs today, that is possible. LLMs have an understanding of SQL and are able to write it pretty well. However, there are several issues that make this a non-trivial task.

## The Problems

So LLMs can write SQL - what more is needed?

Unfortunately, a few things.

The main issue that exists is hallucination. LLMs can write SQL, but they are often prone to making up tables, making up fields, and generally just writing SQL that if executed against your database would not actually be valid. So one of the big challenges we face is how to ground the LLM in reality so that it produces valid SQL.

The main idea to fix this (we will go into more detail below) is to provide the LLM with knowledge about what actually exists in the database and tell it to write a SQL query consistent with that. However, this runs into a second issue - the context window length. LLMs have some context window which limits the amount of text they can operate over. This is relevant because SQL databases often contain a lot of information. So if we were to naively pass in all the data to ground the LLM in reality, we would likely run into this issue.

A third issue is a more basic one: sometimes the LLM just messes up. The SQL it writes may be incorrect for whatever reason, or it could be correct but just return an unexpected result. What do we do then? Do we give up?

## The (High Level) Solutions

When thinking about how to tackle these issues, it’s informative to think about how we as humans tackle these issues. If we can then replicate the steps that we would take to solve those problems, we can help the LLM do so as well. So let’s think about what a data analyst would do if they were asked to answer a BI question.

When data analysts query SQL databases, there’s a few things they normally do that help them make the right queries. For example, they usually make a sample query beforehand to understand what the data looks like. They can look at the schema of the tables, or even certain rows. This can be thought of as the data analyst learning what the data looks like so that when they write a SQL query in the future it is grounded in what actually exists. Data analysts also don’t usually just look at all the data (or thousands of rows) at the same time - they may limit any exploratory queries to the top K rows, or look at summary stats instead. This can yield some hints at how to get around the context window limitations. And finally, if a data analyst hits an error, they don’t just give up - they learn from the error and write a new query.

We discuss each of these solutions in a separate section below.

## Describing your database

To provide the LLM with enough information for it to generate reasonable queries for a given database, we need to effectively describe the database in the prompt. This can include describing table structure, examples of what the data looks like, and even examples of good queries for the database. The examples below come from the Chinook database.

### Describing the schema

In older versions of LangChain, we simply provided the table names, columns, and their types:

`Table &#x27;Track&#x27; has columns: TrackId (INTEGER), Name (NVARCHAR(200)), AlbumId (INTEGER), MediaTypeId (INTEGER), GenreId (INTEGER), Composer (NVARCHAR(220)), Milliseconds (INTEGER), Bytes (INTEGER), UnitPrice (NUMERIC(10, 2))`

[Rajkumar et al](https://blog.langchain.com/content/files/abs/2204.xml) performed a study evaluating the Text-to-SQL performance of OpenAI Codex given a variety of different prompting structures. They achieved the best performance when prompting Codex with the `CREATE TABLE` commands, which include column names, their types, column references, and keys. For the `Track` table, this looks like:

`CREATE TABLE &quot;Track&quot; (
&quot;TrackId&quot; INTEGER NOT NULL,
&quot;Name&quot; NVARCHAR(200) NOT NULL,
&quot;AlbumId&quot; INTEGER,
&quot;MediaTypeId&quot; INTEGER NOT NULL,
&quot;GenreId&quot; INTEGER,
&quot;Composer&quot; NVARCHAR(220),
&quot;Milliseconds&quot; INTEGER NOT NULL,
&quot;Bytes&quot; INTEGER,
&quot;UnitPrice&quot; NUMERIC(10, 2) NOT NULL,
PRIMARY KEY (&quot;TrackId&quot;),
FOREIGN KEY(&quot;MediaTypeId&quot;) REFERENCES &quot;MediaType&quot; (&quot;MediaTypeId&quot;),
FOREIGN KEY(&quot;GenreId&quot;) REFERENCES &quot;Genre&quot; (&quot;GenreId&quot;),
FOREIGN KEY(&quot;AlbumId&quot;) REFERENCES &quot;Album&quot; (&quot;AlbumId&quot;)
)`

### Describing the data

We can further improve the LLM’s ability to create optimal queries by additionally providing examples of [what the data looks like](https://python.langchain.com/docs/modules/chains/popular/sqlite?ref=blog.langchain.com#adding-example-rows-from-each-table). For example, if we are searching for composers in the `Track` table, it will be quite useful to know if the `Composer` column consists of full names, abbreviated names, both, or perhaps even other representation. [Rajkumar et al](https://blog.langchain.com/content/files/abs/2204.xml) found that providing example rows in a `SELECT` statement following the `CREATE TABLE` description resulted in consistent performance improvements. Interestingly, they found that providing 3 rows was optimal, and that providing more database content can even decrease performance.

We’ve adopted the best practice findings from their paper as the default settings. Together, our database description in the prompt looks like this:

`db = SQLDatabase.from_uri(
	&quot;sqlite:///../../../../notebooks/Chinook.db&quot;,
	include_tables=[&#x27;Track&#x27;], # including only one table for illustration
	sample_rows_in_table_info=3
)
print(db.table_info)`

Which outputs:

`CREATE TABLE &quot;Track&quot; (
&quot;TrackId&quot; INTEGER NOT NULL,
&quot;Name&quot; NVARCHAR(200) NOT NULL,
&quot;AlbumId&quot; INTEGER,
&quot;MediaTypeId&quot; INTEGER NOT NULL,
&quot;GenreId&quot; INTEGER,
&quot;Composer&quot; NVARCHAR(220),
&quot;Milliseconds&quot; INTEGER NOT NULL,
&quot;Bytes&quot; INTEGER,
&quot;UnitPrice&quot; NUMERIC(10, 2) NOT NULL,
PRIMARY KEY (&quot;TrackId&quot;),
FOREIGN KEY(&quot;MediaTypeId&quot;) REFERENCES &quot;MediaType&quot; (&quot;MediaTypeId&quot;),
FOREIGN KEY(&quot;GenreId&quot;) REFERENCES &quot;Genre&quot; (&quot;GenreId&quot;),
FOREIGN KEY(&quot;AlbumId&quot;) REFERENCES &quot;Album&quot; (&quot;AlbumId&quot;)
)
SELECT * FROM &#x27;Track&#x27; LIMIT 3;
TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
2	Balls to the Wall	2	2	1	None	342562	5510424	0.99
3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Hoffman	230619	3990994	0.99`

### Using custom table information

Although LangChain conveniently assembles the schema and sample row descriptions automatically, there are a few cases in which it is preferable to override the automatic info with hand-crafted descriptions. For example, if you know that the first few rows of a table are uninformative, it is best to manually provide example rows that provide the LLM with more information. As an example, in the `Track` table, sometimes multiple composers are separated by slashes instead of commas. This first appears in row 111 of the table, well beyond our limit of 3 rows. We can provide this custom information such that the example rows contain this new information. [Here’s](https://python.langchain.com/docs/modules/chains/popular/sqlite?ref=blog.langchain.com#adding-example-rows-from-each-table) an example of doing this in practice.

It is also possible to use a custom description to limit the columns of a table that are visible to the LLM. An example of these two uses applied to the `Track` table might look like:

`CREATE TABLE &quot;Track&quot; (
&quot;TrackId&quot; INTEGER NOT NULL,
&quot;Name&quot; NVARCHAR(200) NOT NULL,
&quot;Composer&quot; NVARCHAR(220),
PRIMARY KEY (&quot;TrackId&quot;),
)
SELECT * FROM &#x27;Track&#x27; LIMIT 4;
TrackId	Name	Composer
1	For Those About To Rock (We Salute You)	Angus Young, Malcolm Young, Brian Johnson
2	Balls to the Wall	None
3	Fast As a Shark	F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Hoffman
4	Money	Berry Gordy, Jr./Janie Bradford`

If you have sensitive data that you do not wish to send to an API, you can use this feature to provide mock data instead of your actual database.

## Constraining the size of the output

When we make queries with LLMs within a chain or agent, the result from our query will be used as the input for another LLM. If the query result is too big this will max out our model’s input size. So it is usually a good practice to sensibly limit the size of the output of our query. We can do this by instructing our LLM to use as few columns as possible and limit the number of returned rows.

As we can in the following example, if we ask for the list of total sales per country without specifying a number of countries, the query will be capped to 10. You can manage this limit with the `top_k` parameter.

`agent_executor.run(&quot;List the total sales per country. Which country&#x27;s customers spent the most?&quot;)`

&gt;&gt;

`…
Action Input: SELECT c.Country, SUM(i.Total) AS TotalSales FROM Invoice i INNER JOIN Customer c ON i.CustomerId = c.CustomerId GROUP BY c.Country ORDER BY TotalSales DESC LIMIT 10
Observation: [(&#x27;USA&#x27;, 523.0600000000003), (&#x27;Canada&#x27;, 303.9599999999999), (&#x27;France&#x27;, 195.09999999999994), (&#x27;Brazil&#x27;, 190.09999999999997), (&#x27;Germany&#x27;, 156.48), (&#x27;United Kingdom&#x27;, 112.85999999999999), (&#x27;Czech Republic&#x27;, 90.24000000000001), (&#x27;Portugal&#x27;, 77.23999999999998), (&#x27;India&#x27;, 75.25999999999999), (&#x27;Chile&#x27;, 46.62)]
…
`

### Checking syntax

If our LLM generated query is syntactically broken we will find that we will get a traceback when running our chain or agent. This is highly problematic if we want to use this for productive purposes. How could we help the LLM correct the query? We can replicate exactly what we would have done if we had made the mistake ourselves. We send the original query with the traceback log to the LLM and ask it to make it right, by understanding exactly what went wrong. This concept is inspired by [this blogpost](https://www.patterns.app/blog/2023/01/18/crunchbot-sql-analyst-gpt/?ref=blog.langchain.com) where you can find a more detailed explanation.

In the following example from the docs, you can see that the model was trying to query for an unexisting column and when it finds the query is wrong it promptly corrects it with the `query_checker_sql_db` tool:

*Observation: Error: (sqlite3.OperationalError) no such column: Track.ArtistId
[SQL: SELECT Artist.Name, SUM(InvoiceLine.Quantity) AS TotalQuantity FROM Artist INNER JOIN Track ON Artist.ArtistId = Track.ArtistId INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.Name ORDER BY TotalQuantity DESC LIMIT 3]
(Background on this error at: *[*https://sqlalche.me/e/14/e3q8*](https://sqlalche.me/e/14/e3q8?ref=blog.langchain.com)*)*
**Thought:** I should double check my query before executing it.
**Action:** query_checker_sql_db
**Action Input:** *SELECT Artist.Name, SUM(InvoiceLine.Quantity) AS TotalQuantity FROM Artist INNER JOIN Track ON Artist.ArtistId = Track.ArtistId INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.Name ORDER BY TotalQuantity DESC LIMIT 3*
**Observation:**
*SELECT Artist.Name, SUM(InvoiceLine.Quantity) AS TotalQuantity
FROM Artist
INNER JOIN Track ON Artist.ArtistId = Track.ArtistId
INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
GROUP BY Artist.Name
ORDER BY TotalQuantity DESC
LIMIT 3;*
**Thought:** I now know the final answer.
**Action:** query_sql_db
**Action Input:** *SELECT Artist.Name, SUM(InvoiceLine.Quantity) AS TotalQuantity FROM Artist INNER JOIN Album ON Artist.ArtistId = Album.ArtistId INNER JOIN Track ON Album.AlbumId = Track.AlbumId INNER JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.Name ORDER BY TotalQuantity DESC LIMIT 3*

## Future work

As you know, the field is moving fast and we are collectively finding out the best ways for achieving optimal LLM-SQL interaction. Here is the backlog going forward:

#### Few-shot examples

[Rajkumar et al](https://blog.langchain.com/content/files/abs/2204.xml) also found that Codex’s SQL generation accuracy improved in benchmarks with few-shot learning, where question-query examples are appended to the prompt (see Figure 2).

#### Use subqueries

Some users have found that telling the agent to break down the problem into multiple subqueries, including comments on what each subquery does, helps the agent get to the correct answer. Thinking in subqueries forces the agent to think in logical steps and thus reduces the probability of making structural mistakes in the query. This is analogous to adding CoT type phrases to the prompt like ‘think this problem step by step” for non-sql problems.

If you want to help implementing any of these or have other best practices that you found helpful, please do share your thoughts in the discussion in the #sql channel in [Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) or directly take a stab at a PR!

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