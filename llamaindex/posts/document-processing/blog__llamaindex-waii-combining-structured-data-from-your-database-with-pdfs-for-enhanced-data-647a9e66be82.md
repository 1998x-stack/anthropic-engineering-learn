---
title: "LlamaIndex + Waii: Text-to-SQL + PDF RAG Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-waii-combining-structured-data-from-your-database-with-pdfs-for-enhanced-data-647a9e66be82"
category: "document-processing"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







# Introduction

In many enterprises, data primarily resides in databases and generally, it’s very difficult to combine database data with other forms of data, such as PDFs, when trying to generate actionable insights.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We envision the development of an agent that empowers anyone to leverage data from all of these data sources for informed decision-making. Imagine an agent proficient in creating documents by merging data from diverse sources, including JIRA and databases, further enriched with the latest internet-sourced information.

At [waii.ai](http://waii.ai/), we are committed to delivering an enterprise text-to-SQL API with the most complete and accurate translation of plain English to SQL available. Waii allows companies to build text-to-SQL right into their products as well as enable no-code analytics for their internal data/business teams. Waii works out of the box and can be self-hosted/on-prem.

LlamaIndex introduces a remarkable RAG framework, facilitating the connection of various customer data sources, such as PDFs, Notion, and internal knowledge bases, to large language models (LLMs). This advancement simplifies the creation of data-augmented chatbots and analysis agents.

This opens up a prime opportunity to develop an enterprise agent that can access data from multiple sources, including your preferred database. We will explore this further in the rest of the blog.

# Why a New Text-to-SQL LlamaIndex Plugin?

To enable the Llama Index agent to utilize text-to-SQL APIs, a plugin is essential. LlamaIndex already has a built-in text-to-SQL plugin, but why did we decide to create a new LlamaHub plugin?

The existing text-to-SQL plugin in LlamaIndex has been suitable for handling simple databases (less than 10 tables, 100 columns) with straightforward SQL queries. However, managing medium to large databases, which can include 100s of tables and 1000s of columns, presents a complex challenge. Limitations arise due to the restricted context windows of LLMs, and even those with large context windows, like GPT-4-turbo with its 128K tokens, can suffer from inaccuracies and regression in task retrieval when overloaded with content. This issue is discussed in a [LlamaIndex study](https://x.com/jerryjliu0/status/1722657583331491860?s=20).

In contrast, Waii focuses on making query generation more efficient. We have developed a built-in compiler to deal with compilation errors from LLMs to support multiple dialects. Our internal knowledge graph, created from database metadata, constraints, and query history, aids in table/schema selection. Users can also apply semantic rules to schema/table/column, or integrate with their data catalog services, ensuring the semantic correctness of generated queries, in addition to syntactic correctness.

To utilize our service, users simply need to connect their database to Waii and copy a Waii API key to create a LlamaIndex agent.

# LlamaIndex + Waii Agent

We are thrilled to showcase the integration of Waii with LlamaIndex to create an agent capable of executing various text-to-SQL tasks and validating the data based on a PDF.

We’ll be analyzing customers’ top-purchased categories during Christmas time, and compare it with [Deloitte’s holiday retail survey](https://www2.deloitte.com/content/dam/insights/articles/us176694_cic_holiday-retail-survey/DI_2023-Deloitte-holiday-retail-survey.pdf) report.

# Architecture of LlamaIndex + Waii

Before diving into the code example, let’s look at the architecture first:

  ![](/blog/images/1*erCvltYEvXnNi3tkj9IPCA.png)

  The LlamaIndex agent operates on the client side, accompanied by a number of
  tools: Each tool provides function specifications and allows functions to be
  selected based on context and the user’s input to
  `**chat("…")**`. For example, if the question indicates information needs to be retrieved
  from the “internet”, the Google search tool will be chosen. Internally it uses
  LLM which returns selected functions with parameters for a given context.

  When the Waii tool is chosen, whether for describing a dataset, generating a
  query, or running a query, it sends the API request to the Waii Service.

  The Waii Service can be deployed as a hosted SaaS or as Docker containers
  running in your on-premises environment. The components of the Waii Service
  include:

  -
    **The Query Generator: **coordinates the entire workflow of
    query generation and communicates with the LLM for this purpose.


  -
    **Knowledge Graph / Metadata Management**: connects to
    databases, extracting metadata and query history as a knowledge graph to
    assist the Query Generator in choosing the right tables and schemas.


  -
    **Semantic Rules**: These aid the Query Generator in producing
    semantically correct queries.


  -
    **Waii Compiler**: After a query is generated by the LLM, the
    Waii Compiler patches identified issues in the query. If a compilation issue
    is not fixable, it regenerates the query with an articulated error message.


# Create LlamaIndex agent with Waii + PDF Loader

  Let’s first create two LlamaHub tools — Waii and PDF Loader. LlamaHub tools
  include specs to identify available functions along with their parameters, the
  agent will select and execute which function to use based on available
  functions and context.

Let’s start with creating an agent which includes the Waii tool:

from llama_hub.tools.google_search import GoogleSearchToolSpec
from llama_hub.tools.waii import WaiiToolSpec
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI

waii_tool = WaiiToolSpec(
    api_key='waii_api_key',
    # Connection key of WAII connected database, see
    # https://github.com/waii-ai/waii-sdk-py#get-connections
    database_key='database_to_use',
    verbose=True
)
And then create a PDF tool:

from pathlib import Path
from llama_index import download_loader
from llama_index import VectorStoreIndex

PDFReader = download_loader("PDFReader")
loader = PDFReader()
documents = loader.load_data(file=Path('DI_2023-Deloitte-holiday-retail-survey.pdf'))
index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine(similarity_top_k=5)
deloitte_retail_survey_tool = QueryEngineTool(
        query_engine=engine,
        metadata=ToolMetadata(
            name="deloitte_retail_survey",
            description=(
                "Provides retail survey report for holiday sales based on Deloitte's data"
                "Use a detailed plain text question as input to the tool, and output using plain text based on pdf data"
            ),
        ),
    )
And at last, create an agent which combines Waii and PDF tools:

agent = OpenAIAgent.from_tools(
  [deloitte_retail_survey_tool] + waii_tool.to_tool_list(),
  llm=OpenAI(model='gpt-4-1106-preview', temperature=0),
  verbose=True)

  `[deloitte_retail_survey_tool] + waii_tool.to_tool_list()`
  indicate using all functions (such as getting answers from the database,
  generating a query, executing a query, describing datasets, etc.) provided by
  Waii and PDF Search.

# Understand your dataset

  The first step in doing data analysis is to get a better understanding of your
  dataset.

You can start asking questions to your agent:

agent.chat("Describe my database")
The output of which is:

STARTING TURN 1
---------------

=== Calling Function ===
Calling function: describe_dataset with args:
  {"ask":"Can you describe the whole database?"}
...

========================

STARTING TURN 2
---------------

The database I have access to consists of several schemas, each with its
own set of tables and domains:

1. **CRUNCHBASE_2016**: This schema includes tables related to acquisitions,
   companies, investments, and funding rounds in the Crunchbase database for
   the year 2016. It's useful for analyzing acquisition trends, company
   information, investment activity, and funding trends.

2. **RETAIL_DATA**: This schema contains tables related to retail operations,
   such as call centers, customers, addresses, demographics, inventory,
   items, promotions, stores, returns, sales, and warehouses. It can be used
   to analyze call center performance, customer demographics, inventory
   management, sales performance, and other retail operations.

3. ...

  As you can see, the agent understood the request, called
  `describe_dataset` function provided by Waii, and generated a
  summary of the dataset.

  I’m interested in the
  `RETAIL_DATA` schema, so let me ask more of the schema -

agent.chat("What can i do with the retail_data schema")
And I get this:

The RETAIL_DATA schema in the TWEAKIT_PLAYGROUND database is designed
to support a wide range of analyses related to retail operations. Here
are some of the capabilities and types of analyses you can perform with
this schema:

1. **Call Center Analysis**: Evaluate the performance of call centers,
   understand call volumes, and assess customer service efficiency.

2. **Customer Demographics**: Analyze customer profiles, including
   demographics, purchasing behaviors, and preferences. This can help
   in targeted marketing and customer segmentation.

Specific questions that can be addressed using the RETAIL_DATA schema include:
- What is the total number of call centers?
- How many customers have a preferred customer flag?
- What is the average price of items?
Let me do some more data analysis.

# Generate an SQL query and run it

  Let’s generate a SQL query (asking top 10 item categories sold during
  Christmas time):

agent.chat("Top 10 item category sold during christmas time across all years")
Now it calls `get_answer` function from Waii tool:

=== Calling Function ===
Calling function: get_answer with args:
  {"ask":"What are the top 10 item categories sold during
          Christmas time across all years?"}
And got a SQL like:

WITH christmas_sales AS (
    SELECT
        ss_item_sk,
        SUM(ss_quantity) AS total_quantity
    FROM tweakit_playground.retail_data.store_sales AS ss
    INNER JOIN tweakit_playground.retail_data.date_dim AS dd
        ON ss_sold_date_sk = d_date_sk
    WHERE
        d_holiday = 'Y' AND d_date ILIKE '%-12-25'
    GROUP BY
        ss_item_sk
),
ranked_categories AS (
    SELECT
        i_category,
        SUM(total_quantity) AS category_quantity
    FROM christmas_sales AS cs
    INNER JOIN tweakit_playground.retail_data.item AS i
        ON ss_item_sk = i_item_sk
    GROUP BY
        i_category
    ORDER BY
        category_quantity DESC
    LIMIT 10
)
SELECT
    i_category AS category,
    category_quantity
FROM ranked_categories
Let me ask it to run the query:

agent.chat("Run it")
I got a Dataframe along with its summary:

  ![](/blog/images/1*WRPeDfQJBuVmNtU40OVLjA.png)

The top 10 item categories sold during Christmas time across all years,
based on the total quantity of items, are:

1. Women: 1,487,891
2. Sports: 1,486,644
3. Children: 1,483,531
4. Electronics: 1,478,463
5. Music: 1,476,045
6. Books: 1,472,911
7. Home: 1,471,348
8. Jewelry: 1,459,025
9. Shoes: 1,456,296
10. Men: 1,451,285

# Use with a PDF report

  Let’s try to cross-check the result with the[
    holiday retailer report (in PDF form) from Deloitte](https://www2.deloitte.com/content/dam/insights/articles/us176694_cic_holiday-retail-survey/DI_2023-Deloitte-holiday-retail-survey.pdf)
  — Are Deloitte’s top-purchased gift categories the same as what we saw from
  the database?

  ![](/blog/images/1*SEaHOPtWQD9fE6isn2aTTQ.png)

  Top gift categories during the holiday

  There’s one page from the pdf we are interested in — let’s see if we can
  retrieve this page

agent.chat("""Give me top holiday gift categories based on Deloitte's
holiday retail survey, and how it is different from the top
10 item category sold during christmas time across all years
from my database""")

  The output looks like the following, which indicates it uses the
  `deloitte_retail_survey` tool to obtain insights from the PDF.

STARTING TURN 1
---------------
=== Calling Function ===
Calling function: deloitte_retail_survey with args: {"input": "What are the top holiday gift categories based on Deloitte's holiday retail survey?"}
...
It gives the following summary:

Based on Deloitte's holiday retail survey, the top holiday gift
categories are:

1. Clothing &amp; Accessories
2. Gift Cards &amp; Other
3. Food &amp; Beverage
...

From your database, the top 10 item categories sold during Christmas
time across all years are:

1. Women
2. Sports
3. Children
...

Comparing the two lists, we can see some differences and similarities:

- "Clothing &amp; Accessories" from Deloitte's survey could correspond to
  "Women," "Men," and possibly "Children" from your database.
- "Electronics &amp; Accessories" is a common category in both lists.
- "Gift Cards &amp; Other" and "Food &amp; Beverage" from Deloitte's survey do
  not have a direct match in the top categories from your database.
...

  Bingo! Now we can compare the results from our database with PDFs. And I love
  seeing how the agent can correlate the two lists and tell me that my store
  doesn’t have the “Gift Cards &amp; Other” and “Food &amp; Beverage”
  categories!

  You can find the code from the Colab notebook
  [link](https://colab.research.google.com/drive/1hL_Ztb1DRcdyeO2JZwsc9osW0Y3chP9c#scrollTo=fvye9sqAcn5j)

# Wrapping up

  The integration of Waii’s text-to-SQL API with LlamaIndex’s RAG framework
  marks a significant advancement in enterprise data analytics. This powerful
  combination enables companies to effortlessly merge and analyze data from
  various sources, including databases, PDFs, and the Internet. We demonstrated
  the agent’s capability to generate SQL queries, understand complex datasets,
  and correlate findings with external reports. This innovation not only
  simplifies data analysis but also opens new avenues for informed
  decision-making in the digital era.

  To learn more about Waii, please contact us here:
  [https://www.waii.ai/#request-demo](https://www.waii.ai/#request-demo)