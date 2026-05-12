---
title: "How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel"
author: "LangChain Accounts"
date: "2023-09-12"
url: "https://www.langchain.com/blog/how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel"
---

PartnerTutorials &amp; How-Tos

# How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 12, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1694cf06727c05dca33_64ff5e36ac4b999af4a08f05_image-20230911-155918.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Gretel*](https://gretel.ai/?ref=blog.langchain.com)* team. We&#x27;re really excited by their approach to combining agent-based methods, LLMs, and synthetic data to enable natural language queries for databases and data warehouses, sans SQL. The post has a really helpful walkthrough (with code!) to bring the ideas to life.*

Agent-based approaches coupled with large language models (LLMs) are quickly transforming how we interact with databases and data warehouses. Combined, these technologies enable natural language queries to data in your application or business, eliminating the need for SQL expertise to interact with data and even facilitating seamless queries across diverse systems.

In this post, we’ll walk through an example of how LangChain, LLMs (whether open-source models like Llama-2, Falcon, or API-based models from OpenAI, Google, Anthropic), and synthetic data from Gretel combine to create a powerful, privacy-preserving solution for natural language data interaction with data in databases and warehouses. We&#x27;ll introduce key concepts such as Agents, LLM Chains, and synthetic data, then delve into a practical code example to bring these ideas to life.

## **Key technologies**

- **LLM Chains**: Frameworks such as LangChain for developing applications powered by language models by chaining them together.
- **Agents: **Agents use an LLM to decide what actions to take and the order to take them in, making future decisions by iteratively observing the outcome of prior actions.
- **Function Aware LLMs: **Certain newer LLMs (like OpenAI’s GPT-3.5-turbo-0613 and Google’s PaLM text-bison) have been fine-tuned to detect when a function should be called and respond with the inputs that should be passed to the function.
- **Synthetic data:** An artificial version of the real-world created by data-aware generative models that can offer strong privacy guarantees to data. Gretel offers generative models for working with tabular data based on Transformer, GAN, and graph-based architectures.
- **SQL Databases: **The backbone holding the data you&#x27;ll be querying. For today, we’ll use a SQLite database.

## **What is an Agent in LangChain?**

Some applications will require not just a predetermined chain of calls to LLMs/other tools, but potentially an unknown chain that depends on the user&#x27;s input, too. In these types of chains, there is an “agent” that has access to a suite of tools — for example math, or the ability to query a SQL database. Depending on the user input, the agent can then decide which, if any, of these tools to call.

Under the hood, the LangChain SQL Agent uses a [MRKL](https://arxiv.org/abs/2205.00445?ref=blog.langchain.com) (pronounced Miracle)-based approach, and queries the database schema and example rows and uses these to generate SQL queries, which it then executes to pull back the results you&#x27;re asking for.

## **Generating synthetic tabular data**

Before diving into the example, let&#x27;s talk about synthetic data. With Gretel&#x27;s models, you can make an artificial but statistically similar version of your sensitive data. This synthetic data is safe to use, thanks to math-backed privacy features like [differential privacy](https://gretel.ai/blog/introducing-gretel-tabular-dp?ref=blog.langchain.com). In our example, we&#x27;ll use both real and synthetic data to show why this privacy is crucial when letting language models access sensitive info.

To generate your own synthetic data for this example, grab the [IBM HR Employee Attrition dataset](https://gretel-public-website.s3.us-west-2.amazonaws.com/datasets/ibm_hr_attrition/ibm-hr-employee-attrition.csv?ref=blog.langchain.com) (or your own) and an API key from [https://console.gretel.ai](https://console.gretel.ai/?ref=blog.langchain.com). You can run Gretel&#x27;s [quickstart notebook](https://docs.gretel.ai/examples/synthesize-tabular-data?ref=blog.langchain.com) or console-based workflow to create a synthetic version of the data.

For this example, I used the Gretel Tabular DP model ([notebook](https://github.com/gretelai/gretel-blueprints/blob/main/docs/notebooks/create_synthetic_data_with_tabular_dp.ipynb?ref=blog.langchain.com), [docs](https://docs.gretel.ai/reference/synthetics/models/gretel-tabular-dp?ref=blog.langchain.com)) with an epsilon value of 5 for strong privacy guarantees that are great for regulated environments. For maximum accuracy while still maintaining privacy, you can also try the Gretel ACTGAN model ([docs](https://docs.gretel.ai/reference/synthetics/models/gretel-actgan?ref=blog.langchain.com)), which excels at working with highly dimensional tabular data to enable machine learning and analytics use cases.

### **Getting started: Installation**

Follow along with our complete [notebook in Colab](https://colab.research.google.com/gist/zredlined/f84c50771245ec15993b44f846c9cd0e/safely-query-enterprise-databases-with-langchain-openai-and-gretel-ai.ipynb?ref=blog.langchain.com#scrollTo=ySD3ANEsCLw-) or [GitHub](https://gist.github.com/zredlined/f84c50771245ec15993b44f846c9cd0e?ref=blog.langchain.com).

First, install dependencies.

`!pip install -Uqq langchain openai gretel-client
!pip install -Uqq smart_open tabulate`

### **Initializing the LangChain Agent**

Note: Please use your OpenAI key for this, which should be kept private.

Here&#x27;s the code to initialize the LangChain Agent and connect it to your SQL database.

`from langchain.agents import AgentExecutor, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms.openai import OpenAI
from langchain.sql_database import SQLDatabase




def create_agent(
    db_uri,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=VERBOSE_LANGCHAIN,
    temperature=0,
    model=&quot;gpt-3.5-turbo-0613&quot;,
 ):
    db = SQLDatabase.from_uri(db_uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=temperature))


    return create_sql_agent(
        llm=ChatOpenAI(temperature=temperature, model=model),
        toolkit=toolkit,
        verbose=verbose,
        agent_type=agent_type,
    )`

Here, we are also importing some sample datasets. We&#x27;ll use both a real and a synthetic version of the IBM attrition HR dataset. The synthetic version is generated using Gretel&#x27;s Tabular DP model with an (ε) Epsilon of 5.

`# Create SQLite databases from CSV datasets
create_sqlite_db_from_csv(
    SYNTHETIC_DATA, db_name=&quot;synthetic-sqlite.db&quot;, table_name=&quot;synthetic_ibm_attrition&quot;
)
create_sqlite_db_from_csv(
    REAL_DATA, db_name=&quot;real-sqlite.db&quot;, table_name=&quot;real_ibm_attrition&quot;
)


# Create SQL agent to interact with synthetic IBM attrition data
agent_synthetic_db = create_agent(&quot;sqlite:////content/synthetic-sqlite.db&quot;)


# Create SQL agent to interact with real-world IBM attrition data
agent_real_db = create_agent(&quot;sqlite:////content/real-sqlite.db&quot;)`

### **Querying the data**

First, we&#x27;ll create a helper function to compare the outputs of real data and synthetic data.

`def run_and_compare_queries(synthetic, real, query: str):
    &quot;&quot;&quot;Compare outputs of Langchain Agents running on real vs. synthetic data&quot;&quot;&quot;
    query_template = f&quot;{query} Execute all necessary queries, and always return results to the query, no explanations or apologies please. Word wrap output every 50 characters.&quot;


    result1 = synthetic.run(query_template)
    result2 = real.run(query_template)


    print(&quot;=== Comparing Results for Query ===&quot;)
    print(f&quot;Query: {query}&quot;)


    table_data = [
        {&quot;From Agent on Synthetic DB&quot;: result1, &quot;From Agent on Real DB&quot;: result2}
    ]


    print(tabulate(table_data, headers=&quot;keys&quot;, tablefmt=&quot;pretty&quot;))`

### **Sample queries**

**Which three departments have the highest attrition rates?**

`prompt = &quot;Which 3 departments have the highest attrition rates? Return a list please.&quot;
run_and_compare_queries(synthetic=agent_synthetic_db, real=agent_real_db, query=prompt)`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16a4cf06727c05dca4c_64ff603f80ed4f6db766bed7_Screenshot%25202023-09-11%2520at%25202.43.37%2520PM.png)*Figure 1. Comparing real and synthetic results for query #1.*

The results were quite similar between the synthetic and real datasets, giving us confidence in the synthetic data&#x27;s reliability.

**What is the distribution of ages by 10-year increments across the entire dataset?**

`prompt = &quot;Show me a distribution of ages by 10 year increments. Return in list format please.&quot;
run_and_compare_queries(synthetic=agent_synthetic_db, real=agent_real_db, query=prompt)`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16a4cf06727c05dca51_Image-from-iOS.jpeg)

Again, the distributions were notably similar between the synthetic and real data sets.

**Which department travels the furthest from home?**

`prompt = &quot;Which department travels the furthest from home?&quot;
run_and_compare_queries(synthetic=agent_synthetic_db, real=agent_real_db, query=prompt)`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16a4cf06727c05dca43_64ff73f91aab5c89289e368c_Screenshot%25202023-09-11%2520at%25204.09.07%2520PM.png)*Figure 3. Comparing real and synthetic results for query #3.*

In this case, we get a perfect match.

## **Importance of privacy: Re-identification attack example**

Here, we illustrate a &quot;re-identification attack&quot; where vulnerabilities in even de-identified datasets can allow an attacker to re-identify individuals by combining known attributes. Such risks emphasize the danger of sharing data stripped of direct identifiers yet containing attributes that, when combined, can lead to identification — such as the combination of an attacker who knew someone’s age, gender, and department in the example below.

Synthetic data prevents direct linking of individual information as no record in the output is based on a single user’s data, effectively thwarting re-identification attacks and upholding privacy.

`prompt = &quot;Is there an employee who is Age 46, Female, and who works in Human Resources. If so, what is their monthly income, performance rating, and years since their last promotion?&quot;
run_and_compare_queries(synthetic=agent_synthetic_db, real=agent_real_db, query=prompt)
`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16a4cf06727c05dca57_Screenshot-2023-09-12-at-4.02.18-PM--2-.png)

## **Conclusion**

By using synthetic data, you not only protect privacy but also gain actionable insights—essential for any data-driven organization. When you blend this with agent-based approaches and large language models, you open the door for more and better stakeholder collaborations. No SQL expertise needed; simply use natural language to engage with your data across all levels of your organization.

This scalable solution democratizes data access and ushers in a new era of smart, privacy-conscious data interaction. For businesses eager to maintain a competitive edge in today&#x27;s data-centric world, adopting these technologies isn&#x27;t just an option; it&#x27;s a must.

If you&#x27;re ready to up your data game, [sign up for Gretel today](https://gretel.ai/signup?ref=blog.langchain.com) and start synthesizing.

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