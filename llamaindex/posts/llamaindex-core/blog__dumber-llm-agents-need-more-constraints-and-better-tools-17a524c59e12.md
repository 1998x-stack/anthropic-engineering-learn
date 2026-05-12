---
title: "LLM Agents: Constraints And Better Tools Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/dumber-llm-agents-need-more-constraints-and-better-tools-17a524c59e12"
category: "llamaindex-core"
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







# Summary

In this article, we compare how well LLM-powered agents with different degrees of complexity perform over practical data tasks (financial analysis). We compare the performance of agents with more *complex, unrestrained *interaction behavior (ReAct) with agents that contain *simpler, more constrained *interactions (routing). We specifically analyze how much complexity can be added to the agent layer vs. the tool layer.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



We find that the choice of the language model matters a lot. ReAct agents that are powered by “dumber” models (in a tongue-in-cheek fashion we are referring to any non GPT-4 model as “dumb”) struggle to return relevant results over data. We find that constraining agent interaction behavior, and giving them access to more tools that can more explicitly perform complex actions, can help improve query performance over these less sophisticated LLMs. In contrast, more sophisticated models (GPT-4) can more reliably utilize the ReAct loop to execute a variety of complex data queries.

This blog post is quite detailed; we provide a *lot *of experiments and results below. Best of all, you can run this all yourself with our [example notebook](https://colab.research.google.com/drive/1uP38k4nr8OPmXbY4dLoKKQW0F29WtNuY?usp=sharing)!

# Overview of Agents

Building LLM-powered agents have gotten increasingly popular in the past few months. Frameworks like [LangChain](https://github.com/hwchase17/langchain) have made it much easier to create these agents according to a set of common abstractions.

At a high-level, an “agent” is essentially an automated decision engine, that can be used to interact with an external environment. The core agent loop looks something like the following:

- The agent has access to a set of “tools”, which are generic functions that it can perform. It has an awareness of each tool through some attached metadata, and it can call each tool (either as a function call or structured API).
- User feeds in a natural language input to the agent.
- Given the input, the agent **interacts with the set of tools **in some fashion and returns the response.

There’s a variety of ways to perform **agent-tool interaction.**

- The most popular is probably [ReAct](https://arxiv.org/abs/2210.03629): the agent reasons over the next action, constructs an action command, executes the action. It repeats these steps in an iterative loop until the task is complete.
- There are other interaction modes too. Recently there was a paper on [Plan-and-solve Prompting](https://arxiv.org/pdf/2305.04091.pdf), which generates a plan beforehand (to decompose a complex task into simpler ones). Before ReAct there have also been related techniques on [Self-Ask](https://arxiv.org/abs/2210.03350) and [Chain of Thought Prompting](https://arxiv.org/abs/2201.11903).

## “Complex” vs. “Simple” Agent Interaction Techniques

We classify techniques like ReAct are more *complex and unconstrained: *this is because they perform iterative reasoning and also break the input into smaller steps. Complicated agent interaction loops allow for more *freedom of behavior, *and* *create an increased burden on the LLM being used. The pro of complex interaction frameworks is that they can be more general and handle a broader class of queries over simple tools. The con is that if the LLM is not up to par, then these frameworks are prone to making mistakes; unconstrained behavior can lead to unexpected results.

On the other end of the spectrum, you can imagine a *simple and constrained *agent interaction mechanism, where the agent does one-step selection of the underlying tool to use, and returns the response from the tool. The agent essentially just acts as a router from the query to Tool. There are no steps to break down the question into smaller ones, and no iterative chain-of-thought loops. The pro here is that the model will likely make fewer errors. The con here is that the interaction technique allows for less freedom and imposes more constraints on behavior.

## Investigating Agent Interaction Techniques for Data Querying

We at LlamaIndex are interested in how agents can help augment data tasks. More specifically, we are interested in how agents can help perform complex user queries over a diverse range of data sources. This includes not only asking questions over a single document, but being able to synthesize insights across multiple documents and return that to the user.

LlamaIndex query engines can be used as Tools within an agent construct to query your data (we provide [seamless integrations with LangChain](https://gpt-index.readthedocs.io/en/latest/how_to/integrations/using_with_langchain.html)). These Tools can vary in complexity. For instance, a *simple *Tool could be our [vector store query engine](https://gpt-index.readthedocs.io/en/latest/how_to/integrations/vector_stores.html), which does top-k embedding retrieval from a vector store. A more *advanced* tool could be a query engine over our graph data structure, which can be setup to [explicitly provide compare/contrast capabilities](https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html#compare-contrast-queries) over any subset of documents. The tool itself can contain “agent-like” decision-making capabilities under the hood. LlamaIndex provides a variety of modules around [routing](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/RouterQueryEngine.html), [query decomposition](https://gpt-index.readthedocs.io/en/latest/how_to/query/query_transformations.html#single-step-query-decomposition), and [multi-part query planning](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/sub_question_query_engine.html).

In this blog post, we are interested in comparing the following approaches to designing agents and tools to see which approach can provide good answers to different user queries in a robust fashion:

- more *complex and unconstrained *agent interaction (ReAct) over a set of *simple *Tools
- more *simple and constrained *agent interaction (simple routing) that uses more *complex *Tools

Complex Agents with Simple Tools, Simple Agents with Complex Tools![](/blog/images/1*R4zNJYl_k47ZvAbapWe70Q.png)

Essentially what we are interested in is how much complexity can be pushed to the agent interaction layer vs. being left in the Tool layer. We explore the following concrete example: let’s say the user query is to compare/contrast two different documents (a relatively complex query). If the set of Tools are all just vector indices over different documents, could the agent interaction loop figure out how to execute that query reliably against the vector indices? On the other hand, if we push the complexity down to the Tool layer, then we could *explicitly *have a Tool that can perform “compare/contrast” over your Documents. Then the burden on the agent is to simply call this Tool instead of interacting with a set of other tools in a more complex fashion.

## High-Level Findings

The high-level finding is that **less sophisticated agents need more constraints. **More specifically, we found that using a GPT-3 powered agent in a ReAct loop did not provide good results over complex queries; it was not able to figure out the proper interaction pattern over the provided set of Tools in order to surface the results. Instead, by adding more constraints to the agent behavior and providing more sophistication in the Tool itself, we were able to get a GPT-3 agent to produce better results.

**Smarter agents require fewer constraints. **We did find that GPT-4 agents with ReAct were able to provide better query results than GPT-3 agents when presented with a set of simple Tools over the data. This implies that more powerful agents may not need as many tools to “explicitly” perform tasks when much of that logic can be handled in the agent interaction loop.

# Setup

Our data consists of three Uber 10-Q filings (quarterly financial reports) in 2022: March, June, and September. We wish to execute different queries over this data; the bulk of these queries are around comparing different bits of information between these documents.

march_2022 = SimpleDirectoryReader(input_files=["../data/10q/uber_10q_march_2022.pdf"]).load_data()
june_2022 = SimpleDirectoryReader(input_files=["../data/10q/uber_10q_june_2022.pdf"]).load_data()
sept_2022 = SimpleDirectoryReader(input_files=["../data/10q/uber_10q_sept_2022.pdf"]).load_data()We use LlamaIndex to define a vector index over each document, which just stores the document chunks + embeddings in a vector store. We can then query each vector index using a simple`QueryEngine` . We create a tool for each of these`QueryEngine` objects.

# define indices
march_index = GPTVectorStoreIndex.from_documents(march_2022)
june_index = GPTVectorStoreIndex.from_documents(june_2022)
sept_index = GPTVectorStoreIndex.from_documents(sept_2022)

# define query engine
march_engine = march_index.as_query_engine(similarity_top_k=3)
june_engine = june_index.as_query_engine(similarity_top_k=3)
sept_engine = sept_index.as_query_engine(similarity_top_k=3)We also define a `ComposableGraph` over these three documents. The composable graph roughly follows the [guide described here](https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html#compare-contrast-queries). This graph is explicitly setup to perform compare/contrast queries over these three documents.

graph = ComposableGraph.from_indices(
    GPTListIndex,
    children_indices=[march_index, june_index, sept_index],
    index_summaries=[
        "Provides information about Uber quarterly financials ending March 2022",
        "Provides information about Uber quarterly financials ending June 2022",
        "Provides information about Uber quarterly financials ending September 2022"
    ]
)The graph can be queried with a `ComposableGraphQueryEngine` :

# define decompose_transform
decompose_transform = DecomposeQueryTransform(verbose=True)

# define custom query engines
custom_query_engines = {}
for index in [march_index, june_index, sept_index]:
    query_engine = index.as_query_engine(service_context=service_context)
    query_engine = TransformQueryEngine(
        query_engine,
        query_transform=decompose_transform,
        transform_extra_info={'index_summary': index.index_struct.summary},
    )
    custom_query_engines[index.index_id] = query_engine

custom_query_engines[graph.root_id] = graph.root_index.as_query_engine(
    service_context=service_context,
    streaming=True,
)

# define graph
g_engine = graph.as_query_engine(
    custom_query_engines=custom_query_engines
)We try the following agent setups:

- **GPT-3 ReAct agent: **A zero-shot GPT-3 ReAct agent with three Tools: each Tool corresponds to the vector index over a 10-Q filing.
- **GPT-4 ReAct agent: **Same as above but using GPT-4 instead.
- **Simple Router agent: **A simple router “agent” with four Tools: the three Tools listed above + the `ComposableGraphQueryEngine` explicitly setup to perform compare/contrast queries.

The code snippets for initializing these agents are below. For the simple router agent, we use the native `RouterQueryEngine` within LlamaIndex, though you should also be able to achieve similar results in LangChain through either the zero-shot agent (with tweaked settings) or the router chain.

## **GPT-3/GPT-4 ReAct Agent Setup**

# initializing zero-shot ReAct agent

uber_config_sept = IndexToolConfig(
    query_engine=sept_engine,
    name=f"Uber 10Q September 2022",
    description=f"Provides information about Uber quarterly financials ending September 2022",
    tool_kwargs={"return_direct": False}
)
uber_config_june = IndexToolConfig(
    query_engine=june_engine,
    name=f"Uber 10Q June 2022",
    description=f"Provides information about Uber quarterly financials ending June 2022",
    tool_kwargs={"return_direct": False}
)
uber_config_march = IndexToolConfig(
    query_engine=march_engine,
    name=f"Uber 10Q March 2022",
    description=f"Provides information about Uber quarterly financials ending March 2022",
    tool_kwargs={"return_direct": False}
)

toolkit = LlamaToolkit(
    index_configs=[uber_config_sept, uber_config_june, uber_config_march],
)

# this is a light wrapper around `initialize_agent` in langchain (which defaults to zero-shot)
agent_chain = create_llama_agent(
    toolkit,
    llm, # can be GPT-3 or GPT-4
    verbose=True
)

## Simple Router Agent Setup

query_tool_sept = QueryEngineTool.from_defaults(
    query_engine=sept_engine,
    description=f"Provides information about Uber quarterly financials ending September 2022",
)
query_tool_june = QueryEngineTool.from_defaults(
    query_engine=june_engine,
    description=f"Provides information about Uber quarterly financials ending June 2022",
)
query_tool_march = QueryEngineTool.from_defaults(
    query_engine=march_engine,
    description=f"Provides information about Uber quarterly financials ending March 2022",
)
query_tool_graph = QueryEngineTool.from_defaults(
    query_engine=g_engine,
    description=f"Provides comparisons between Uber financials across quarters in 2022. Can be used to answer "
                 "any questions that require analysis across multiple quarters.",
)

# our "router" query engine is effectively a simple agent that can only perform routing
query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        query_tool_sept,
        query_tool_june,
        query_tool_march,
        query_tool_graph
    ]
)Now that we’ve described the setup, let’s take a look at the results below!

# Findings and Experiments

At a high-level, we find using GPT-3 in ReAct agents produces suboptimal results over these queries. They tend to exhibit the following characteristics:

- **Unpredictability in the set of chosen tools: **The set of tools chosen can differ even if the questions are semantically similar, leading to variability in the responses.
- **Lack of coverage in the set of chosen tools: **Oftentimes we expect that a given question is able to make use of all three 10-Q statements, but only a subset of them are picked.
- **Erroneous chain-of-thought processing: **Sometimes the agent uses tools throughout the CoT process that are irrelevant to the question.

In contrast, we find that GPT-4 ReAct agents provide answers that are more relevant, predictable, and exhibit fewer errors in intermediate results.

Finally, we find that using a simpler routing-only GPT-3 agent with access to an explicit “compare/contrast” tool allows the agent to perform better.

As a reminder, full results are in the notebook: [https://colab.research.google.com/drive/1uP38k4nr8OPmXbY4dLoKKQW0F29WtNuY?usp=sharing](https://colab.research.google.com/drive/1uP38k4nr8OPmXbY4dLoKKQW0F29WtNuY?usp=sharing)

## GPT-3 ReAct Agent Results

**Query 1**

agent_chain.run(input="Analyze Uber revenue growth over the last few quarters")Response:

![](/blog/images/1*Rwh0f3D-D-KhpiG3hAoSkw.png)

We see that only the September 10-Q filing is chosen to answer the question. The September 10-Q does contain some information about revenue growth compared to the same period in 2021, but that doesn’t explicitly answer the question, which is about revenue growth the past few quarters.

**Query 2**

agent_chain.run(input="Analyze changes in risk factors for Uber")Response:

![](/blog/images/1*R7zJfetsc8mXhG4kW8_Siw.png)

The September and June 10-Q filings are chosen, but not March. Moreover, the answer is vague and doesn’t provide much detail regarding concrete risk factors for Uber (and also mentions that the risk factors “have changed over the past three quarters” even though it’s only using two Tools).

**Query 3**

In this query, we more explicitly showcase how slight changes in prompts can induce different chain-of-thought paths through different Tools, and as a result produce different answers.

# Prompt variation 1
agent_chain.run(input="Analyze Uber revenue growth and risk factors over time")Response:

![](/blog/images/1*AbOFy6vaAQ3vijwhV5V1ug.png)

# Prompt variation 2
agent_chain.run(input="Analyze Uber revenue growth and risk factors over quarters")![](/blog/images/1*LgCbvrqwEGROw_vma0l4QA.png)The main difference between these two queries is “over time” versus “over quarters.” As we can see, not only are the selected Tools different between the two variations, but the inputs are different as well — in the first it’s “financials”, and in the second it’s “Revenue growth and risk factors.”

Since the Tool input in the first variant is unrelated to the question, the answer is similarly vague: “Uber’s revenue growth and risk factors can be analyzed by comparing the financials…”

**Query 4:**

Here instead of asking a compare/contrast question let’s just ask a question about a given statement.

agent_chain.run(input="How much cash did Uber have in sept 2022?")![](/blog/images/1*A7bhWOv5Z3HdTp2iafR3sA.png)We see that the agent makes two errors 1) it is not able to supply an action input to each Tool, and 2) ends up looking through the June and March filings which are irrelevant to the question.

## GPT-4 ReAct Agent Results

GPT-4 ReAct agents perform a lot better than GPT-3 agents. They comprehensively go through the set of available Tools, and provide much more detailed observation extraction and response synthesis.

We won’t go through all of these examples, but they can be found in the example notebook!

**Query 1:**

agent_chain_gpt4.run(input="Analyze Uber revenue growth over the last few quarters")Response:

![](/blog/images/1*PJDOtqVHKJ9I_l6rICp6dQ.png)

Unlike the GPT-3 agent, here the GPT-4 agent at least goes through every filing and synthesizes the result.

**Query 2**

agent_chain_gpt4.run(input="Analyze changes in risk factors for Uber")Response:

![](/blog/images/1*VBPGlCvcyjaRYEpXChGm2w.png)

Here the GPT-4 agent still only looks at September and June (and skips March), but the response is way more detailed, and references concrete facts within the report.

## GPT-3 Router Agent Results

Reminder: the router agent doesn’t do any CoT and has additional access to our ComposableGraph query engine, which can explicitly perform compare/contrast queries. Let’s take a look at how this agent does.

**Query 1**

response = query_engine.query("Analyze Uber revenue growth over the last few quarters")Response (intermediate steps):

Selecting query engine 3: Provides comparisons between Uber financials across quarters in 2022. Can be used to answer any questions that require analysis across multiple quarters..
&gt; Current query: Analyze Uber revenue growth over the last few quarters
&gt; New query:  What was Uber's revenue growth from the last quarter ending March 2022 compared to the previous quarter?
&gt; Current query: Analyze Uber revenue growth over the last few quarters
&gt; New query:  What was Uber's revenue growth from the last quarter ending June 2022 compared to the previous quarter?
&gt; Current query: Analyze Uber revenue growth over the last few quarters
&gt; New query:  What was Uber's revenue growth from the last few quarters ending September 2022?
Final Response

Based on the limited context information provided, we can only analyze Uber's revenue growth for two specific quarters:

1. For the quarter ending March 2022, Uber's revenue growth increased compared to the first quarter of 2021. However, the exact percentage of growth is not provided.

2. For the quarter ending September 2022, Uber's revenue growth was 72%.

Unfortunately, we do not have enough data to analyze the revenue growth for the quarters ending June 2022 or to compare it to the previous quarter. To provide a more comprehensive analysis, additional data on Uber's revenue growth for other quarters would be needed.To be fair, this response does not cover the month of June. But the fault of that lies with the implementation of the Tool itself rather than the agent interaction step. The agent’s only job is to pick the right Tool to solve the task at hand, and it does that job correctly; it decides to choose the Tool corresponding to our `ComposableGraphQueryEngine` abstraction (which can perform compare/contrast queries).

**Query 2**

response = query_engine.query("Analyze changes in risk factors for Uber")Response (intermediate steps):

INFO:llama_index.query_engine.router_query_engine:Selecting query engine 3: Provides comparisons between Uber financials across quarters in 2022. Can be used to answer any questions that require analysis across multiple quarters..
Selecting query engine 3: Provides comparisons between Uber financials across quarters in 2022. Can be used to answer any questions that require analysis across multiple quarters..
&amp;gt; Current query: Analyze changes in risk factors for Uber
&amp;gt; New query:  What are the risk factors for Uber in the quarter ending March 2022?
&amp;gt; Current query: Analyze changes in risk factors for Uber
&amp;gt; New query:  What are the risk factors for Uber in the quarter ending June 2022?
&amp;gt; Current query: Analyze changes in risk factors for Uber
&amp;gt; New query:  What are the risk factors for Uber in the quarter ending September 2022?Final Response

From the context information provided, we can analyze the changes in risk factors for Uber across the three quarters as follows:

1. COVID-19 pandemic: The ongoing pandemic remains a constant risk factor across all quarters, with its impact on driver and courier supply constraints, consumer demand, and government restrictions. However, the specific concerns related to the pandemic may evolve, such as the emergence of new virus variants or changes in vaccination rates.

2. Driver and courier supply constraints: This risk factor is present in the quarter ending March 2022 but is not explicitly mentioned in the subsequent quarters. However, it may still be an underlying concern, especially if the pandemic continues to impact driver availability.

3. Changes in consumer demand: This risk factor is mentioned in the quarter ending March 2022, with an imbalance between Mobility and Delivery services. It is not explicitly mentioned in the subsequent quarters, but fluctuations in revenue due to changes in Gross Bookings and Mobility Trip volumes in the quarter ending June 2022 could be related to changes in consumer demand.

4. Government restrictions and regulations: This risk factor is present in the quarter ending March 2022, with the impact of restrictions on Mobility offerings. In the quarter ending June 2022, the focus shifts to the potential impact of regulatory changes and legal claims, such as driver classification in the UK. In the quarter ending September 2022, the risk factor of driver classification as employees, workers, or quasi-employees becomes more prominent.

5. Uncertainty around future developments: This risk factor is mentioned in the quarter ending March 2022 but is not explicitly mentioned in the subsequent quarters. However, it may still be an underlying concern, especially with the ongoing impact of COVID-19 and potential permanent changes to end-users' behavior.

6. Accounting pronouncements: This risk factor is introduced in the quarter ending June 2022, with the adoption and impact of recently issued accounting pronouncements potentially affecting Uber's consolidated financial statements.

7. Integration and performance of acquired businesses: This risk factor is introduced in the quarter ending June 2022, with the acquisition of Transplace contributing to the increase in Freight revenue.

8. Competition: This risk factor is introduced in the quarter ending September 2022, highlighting the highly competitive nature of the mobility, delivery, and logistics industries, and the need to lower fares, offer incentives, and promotions to remain competitive.

9. Significant losses and increasing operating expenses: This risk factor is introduced in the quarter ending September 2022, emphasizing the financial challenges Uber faces in achieving profitability.The job of the agent is once again simple: it chooses the graph query engine that is optimized to perform “compare/contrast” queries. The result is much more detailed than the result obtained from the GPT-3 ReAct agent (and is comparable to the GPT-4 ReAct agent). It contains a detailed analysis of all risk factors in bullet points, and offers a comparison across time for all bullet points.

**Query 3**

response = query_engine.query("Analyze Uber revenue growth and risk factors over the last few quarters")Response (intermediate steps):

&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What is Uber's revenue growth and risk factors for the quarter ending March 2022?
&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What is Uber's revenue growth and risk factors for the quarter ending March 2022?
&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What is Uber's revenue growth and risk factors for the quarter ending June 2022?
&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What is Uber's revenue growth and risk factors for the quarter ending June 2022?
&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What were Uber's total revenues for the quarter ending September 2022?
&gt; Current query: Analyze Uber revenue growth and risk factors over quarters
&gt; New query:  What were Uber's total revenues for the quarter ending September 2022?Final Response

Uber's revenue growth has been impressive over the past few quarters, with the quarter ending March 2022 showing a 136% year-over-year growth and the quarter ending June 2022 showing a 105% year-over-year growth. The revenue for the quarter ending June 2022 was $8,343 million.

The risk factors for Uber's business have been largely related to the ongoing impacts of the COVID-19 pandemic, including reduced global demand for Mobility rides, supply constraints, and potential permanent changes to end-user behavior. These risk factors have been present in both the quarter ending March 2022 and the quarter ending June 2022, though the specific risks have varied slightly.

# Concluding Thoughts

ReAct-based agents offer a powerful, general reasoning loop, and have the potential to solve complex tasks over your data. But they tend to only work reliably with more powerful language models such as GPT-4. Less sophisticated models (e.g. GPT-3) will make more unpredictable and erroneous decisions, leading to subpar query performance over your data sources.

Agents implemented with “dumber” models need more interaction constraints in order to make more reliable, less erroneous decisions. We find that if we explicitly constrain the agent interface and push the complexity down to the Tool layer, we can still create agents that offer good performance over your data.

Of course, this is just an initial analysis and there’s a few caveats/limitations:

- You may be able to “prompt hack” the default ReAct loop to get more consistent results, and we did not try that.
- We only tested this over a set of three financial documents. There’s a lot more work that needs to be done if we want to test this out on thousands of docs.
- We only compared GPT-3 and GPT-4, there’s so many more models to compare/benchmark, e.g ChatGPT, any open-source model, Anthropic Claude, etc.
- We did not test out other agent interaction patterns besides ReAct: “plan and solve” agents (though we do have similar formulations in LlamaIndex), AutoGPT-like task management, and more.

Whether you’ve run into similar findings or you disagree with our analysis, let us know! We’d love to facilitate this discussion on our [Discord](https://discord.gg/dGcwcsnxhU).

## Notebook Walkthrough

You can find the full notebook walkthrough here: [https://colab.research.google.com/drive/1uP38k4nr8OPmXbY4dLoKKQW0F29WtNuY?usp=sharing](https://colab.research.google.com/drive/1uP38k4nr8OPmXbY4dLoKKQW0F29WtNuY?usp=sharing)