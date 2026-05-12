---
title: "Summarizing and Querying Data from Excel Spreadsheets Using eparse and a Large Language Model"
author: "LangChain Accounts"
date: "2023-08-24"
url: "https://www.langchain.com/blog/summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model"
---

Agent ArchitectureLangChain

# Summarizing and Querying Data from Excel Spreadsheets Using eparse and a Large Language Model

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 24, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)8min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb192f3571add5bcb5e35_1692661506294.png)*Editor&#x27;s Note: This post was written by *[*Chris Pappalardo*](https://www.linkedin.com/in/chris-a-pappalardo/?ref=blog.langchain.com)*, a Senior Director at Alvarez &amp; Marsal, a leading global professional services firm. The standard processes for building with LLM work well for documents that contain mostly text, but do not work as well for documents that contain tabular data (like spreadsheets). We wrote about our *[*latest thinking on Q&amp;A over csvs*](https://blog.langchain.com/benchmarking-question-answering-over-csv-data/)* on the blog a couple weeks ago, and we loved reading Chris&#x27;s exploration of working with csvs and *[*LangChain*](https://www.langchain.com/?ref=blog.langchain.com)* using agents, chains, RAG, and metadata. Lots of great learnings in here!*

When I first sat down to write [eparse](https://github.com/ChrisPappalardo/eparse?ref=blog.langchain.com), the objective was to create a library that could crawl and parse a large set of Excel files and extract information in context into storage for later consumption.  To this end, we were fairly successful – eparse can extract sub-tabular information using a rules-based search algorithm and store labeled cells as rows in a database.  Assuming the user has a good idea of what is contained in the source files, SQL queries or the eparse CLI can be used to retrieve specific data.

However, document Extraction, Transformation, and Loading (“ETL”) activities are becoming more generative AI-oriented to facilitate activities like document summarization and Retrieval-Augmented Generation (“RAG”).  Given that most documents in question mostly contain text, which Large Language Models (“LLMs”) are well suited for, many of the ETL tools were built for this case.  A typical “quickstart” workflow for these purposes is as follows:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e69_figure1.png)Figure 1 - Typical AI-oriented ETL Workflow (source: langchain.com).

The process begins with using an ETL tool set like [unstructured](https://github.com/Unstructured-IO/unstructured?ref=blog.langchain.com), which identifies the document type, extracts content as text, cleans the text, and returns one or more text elements.  A second library, in this case [langchain](https://github.com/langchain-ai/langchain?ref=blog.langchain.com), will then “chunk” the text elements into one or more documents that are then stored, usually in a vectorstore such as [Chroma](https://github.com/chroma-core/chroma?ref=blog.langchain.com).  Finally, an LLM can be used to query the vectorstore to answer questions or summarize the content of the document.

**This process works well for documents that contain mostly text.  It does not work well for documents that contain mostly tabular data, such as spreadsheets.**

To better understand this problem, let’s consider an example.  In the eparse code repository there is a unit test data file called [eparse_unit_test_data.xlsx](https://github.com/ChrisPappalardo/eparse?ref=blog.langchain.com) which contains the following sub-tables, each with different types of financial data:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e6c_figure2.png)Figure 2 - Financial Statement Data by Date with Duplicate Columns![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e93_figure3.png)Figure 3 - Principal Repayment Schedules for Multiple Unidentified Debt Instruments

For this demonstration, I wrote a Gradio app to display the extracted and chunked text data so it is easier to figure out what the libraries are doing behind the scenes.  If we use unstructured and langchain without any modifications, the ETL workflow would produce text chunks from this file that look as follows:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e6f_figure4-1.png)Figure 4 - Extracted Data from Figure 2 Spreadsheet Table in Gradio

Unstructured produces a single text element which LangChain chunks up into 14 pieces, with the 3rd piece (“3 – Document”) containing the first sub-table I depicted above.  Each cell in this table is a separate line, and the 3rd piece contains about 40 lines, which is not the entire table.

When I first tried to ask an LLM to summarize the document using the vectorstore, I received a context window overrun error due to the number of tokens (loosely words) exceeding the LLM’s context window size (in this case 2k tokens).  This is a common problem with working with LLMs, which I will touch on later in the article.  So, to handle that problem, I used a larger context window LLM running on a bigger server and extended the API timeout to 10 minutes.  This time we get a decent result:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e75_figure5-3.png)Figure 5 - Summarization Using a Large Context LLM with a Default Implementation

With default implementations, the LLM understood some aspects of the file but did not get a good general sense of the content.  Also, the amounts are off, the loan amount appears to be 10x higher than the amount in the file, ignores the other loans, and the LLM is misunderstanding the unformatted Excel date value (a 44,621 day maturity would be 122+ years).

**How does eparse perform on the same task?**

eparse does things a little differently.  Instead of passing entire sheets to LangChain, eparse will find and pass sub-tables, which appears to produce better segmentation in LangChain.  Using eparse, LangChain returns 9 document chunks, with the 2nd piece (“2 – Document”) containing the entire first sub-table.  Asking the LLM to summarize the spreadsheet using these vectors produces a more comprehensive view of what is contained in the spreadsheet, including the nuances of the sub-tables, and without any erroneous data.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e90_figure6.png)Figure 6 - Summarization Using eparse and Sub-table Chunking

However, the LLM gets sidetracked by pedantic things like row structure on a single table, and still gets basic questions about amounts incorrect:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e78_figure_between_6_and_7---1_of_2.png)

And the dates are still in the wrong format:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e72_figure_between_6_and_7---2_of_2.png)

**A better way.**

To recap, these are the issues with feeding Excel files to an LLM using default implementations of unstructured, eparse, and LangChain and the current state of those tools:

- Excel sheets are passed as a single table and default chunking schemes break up logical collections
- Larger chunks strain constraints such as context window size, GPU memory, and timeout settings
- Broken logical collections and default retrieval schemes produce incomplete summaries
- Discrete value lookup performance by the LLM on vectorized data is poor
- Default data cleaning does not handle certain things like Excel numeric date encoding

The basic problem with summarization is that it is a reduction from many things to one statement.  The default configuration for a single document retrieval Q&amp;A application is to find 4 similar parts of the document and “stuff” them into the context window before asking for a summary.

To improve retrieval and summarization performance on spreadsheets, we need to consider other retrieval strategies.  Damien Benveniste recently posted the following graphic on LinkedIn that addresses handling summaries of multiple documents that are too large to fit into the context window:

Adding options for chain type, search type, and k-documents settings to my Gradio app, I am now able to test each of these strategies in different configurations against different LLMs:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e87_figure8.png)Figure 8 - Adding Options for Chain Type, Search Type, and K-documents

Setting chain type to “map reduce” (the second strategy in Figure 7) and increasing the number of retrieved documents produces a much better result:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e81_figure9.png)Figure 9 - Map-reduced Summarization with 10 Table Elements

The LLM hits on all major themes in the various extracted sub-tables, acknowledges the instrument type in the document (debt), and even mentions the amortization schedule.  All sans nonsensical data elements.

Turning on chain verbosity, we can get an idea of what is happening behind the scenes (apologies for the small text):

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e84_figure10.png)Figure 10 – The Final Prompt in the Map Reduce Chain

Each extracted sub-table is being summarized by the LLM before it is injected into a final prompt for a collective summary at the end, just like the map-reduce diagram depicts.  Expanding the K-document size ensures that smaller nuances of the file are considered.

You may be wondering about the “refine” strategy and perhaps wonder what happened to the small context model we started with.  I tried various strategies and combinations with the smaller model including refine and, while I was able to eventually deal with the context window limitation, that model with and without the refine strategy just did not deliver quality responses.  I believe this result is the combination of a worse foundational model and 8-bit quantization.  Bottom line is that it pays to have at least one LLM running on outsized hardware with a solid foundation to test against.

**What about specific data retrieval?**

The solution to the problem of extracting specific data from spreadsheet tables using an LLM will involve the Agent design pattern, where LLMs are taught to use functions that they can call.  The demonstration of agents is beyond the scope of this article.  However, we recently added something to eparse that will assist in this effort that I am excited to share.

In version 0.7.0 of eparse we introduced utility functions and a new interface to seamlessly transition from HTML tables to an eparse data interface backed by Sqlite.  What this means is that users can interface their LLMs to structured table data captured by the ETL process, which is stored as metadata in the objects that are uploaded to vector storage.  For example, the following HTML table was generated as a by-product from eparsing the unit test spreadsheet:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5ea1_figure11.png)Figure 11 - HTML Tabular Metadata

To facilitate an ETL pipeline powered by eparse, a drop-in replacement of the unstructured auto partitioner and the Excel partitioner are provided starting with v0.7.1 (see the README for more details on how to incorporate these functions into your project):

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e8d_figure12.png)Figure 12 - Custom Excel Partitioner for Unstructured Using eparse

Using HTML tabular data in an LLM chain with agent tools is as easy as instantiating the following new HTML interface and then using it like any other database ORM:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb195f3571add5bcb5e8a_figure13.png)Figure 13 - eparse HTML Tabular Data Interface

**And handling conversion of numeric Excel formatting data?**

The solution to the problem of handling things like recasting Excel numeric date information into the proper format would best be handled by a custom cleaning or staging brick using the unstructured library.  A discussion of cleaning bricks and how to apply them is [here](https://unstructured-io.github.io/unstructured/bricks.html?ref=blog.langchain.com#cleaning).

**Conclusion**

In conclusion, extracting information from Excel spreadsheets presents unique problems not contemplated by many ETL systems and the typical LLM tool sets.  Key points to consider when designing your own solutions include:

- Spreadsheets present unique problems on both the ingestion / chunking side and in retrieval
- Chain selection is important, default settings may (and often) do not work well
- LLMs are good at text, not great at data, so you will likely need an agent solution to get accurate information from queries
- Not all LLMs are the same when it comes to summarization performance
- Metadata is valuable and you may have underutilized data in your vectorstore

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)