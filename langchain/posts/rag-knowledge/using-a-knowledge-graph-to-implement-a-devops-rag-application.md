---
title: "Using a Knowledge Graph to implement a DevOps RAG application"
author: "LangChain Accounts"
date: "2023-10-04"
url: "https://www.langchain.com/blog/using-a-knowledge-graph-to-implement-a-devops-rag-application"
---

Company AnnouncementsLangChain

# Using a Knowledge Graph to implement a DevOps RAG application

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 4, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)8min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb133394beb695265e9ae_Twitter-post---12--1-.png)*Editor&#x27;s Note: This post was written in collaboration with the *[*Neo4J*](https://neo4j.com/?ref=blog.langchain.com)* team.*

RAG applications are all the rage at the moment. Everyone is building their company documentation chatbot or similar. Mostly, they all have in common that their source of knowledge is unstructured text, which gets chunked and embedded in one way or another. However, not all information arrives as unstructured text.

Say, for example, you wanted to create a chatbot that could answer questions about your microservice architecture, ongoing tasks, and more. Tasks are mostly defined as unstructured text, so there wouldn’t be anything different from the usual RAG workflow there. However, how could you prepare information about your microservices architecture so the chatbot can retrieve up-to-date information? One option would be to create daily snapshots of the architecture and transform them into text that the LLM would understand. However, what if there is a better approach? Meet knowledge graphs, which can store both structured and unstructured information in a single database.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea01_image-1.png)Knowledge graph schema representing microservice architecture and their tasks. Image by author.

Nodes and relationships are used to describe data in a knowledge graph. Typically, nodes are used to represent entities or concepts like people, organizations, and locations. In the microservice graph example, nodes describe people, teams, microservices, and tasks. On the other hand, relationships are used to define connections between these entities, like dependencies between microservices or task owners.

Both nodes and relationships can have property values stored as key-value pairs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea04_image-2.png)Node properties of a Microservice and Task nodes. Image by author.

The microservice nodes have two node properties describing their name and technology. On the other hand, task nodes are more complex. They have the the name, status, description, as well as embedding properties. By storing text embedding values as node properties, you can perform a vector similarity search of task descriptions identical to if you had the tasks stored in a vector database. Therefore, knowledge graphs allow you to store and retrieve both structured and unstructured information to power your RAG applications.

In this blog post, I’ll walk you through a scenario of implementing a knowledge graph based RAG application with LangChain to support your DevOps team. The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/devops_rag.ipynb?ref=blog.langchain.com).

## Neo4j Environment Setup

You need to set up a Neo4j 5.11 or greater to follow along with the examples in this blog post. The easiest way is to start a free instance on [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=blog.langchain.com), which offers cloud instances of Neo4j database. Alternatively, you can also set up a local instance of the Neo4j database by downloading the [Neo4j Desktop](https://neo4j.com/download/?ref=blog.langchain.com) application and creating a local database instance.from langchain.graphs import Neo4jGraph.

`from langchain.graphs import Neo4jGraph

url = &quot;neo4j+s://databases.neo4j.io&quot;
username =&quot;neo4j&quot;
password = &quot;&quot;

graph = Neo4jGraph(
    url=url,
    username=username,
    password=password
)`

## Dataset

Knowledge graphs are excellent at connecting information from multiple data sources. You could fetch information from cloud services, task management tools, and more when developing a DevOps RAG application.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265e9fe_image-3.png)Combining multiple data sources into a knowledge graph. Image by author.

`import requests

url = &quot;https://gist.githubusercontent.com/tomasonjo/08dc8ba0e19d592c4c3cde40dd6abcc3/raw/da8882249af3e819a80debf3160ebbb3513ee962/microservices.json&quot;
import_query = requests.get(url).json()[&#x27;query&#x27;]
graph.query(
    import_query
)`

If you inspect the graph in Neo4j Browser, you should get a similar visualization.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea07_image-4.png)Subset of the DevOps graph. Image by author.

Blue nodes describe microservices. These microservices may have dependencies on one another, implying that the functioning or the outcome of one might be reliant on another’s operation. On the other hand, the brown nodes represent tasks that are directly linked to these microservices. Besides showing how things are set up and their linked tasks, our graph also shows which teams are in charge of what.

## Neo4j Vector index

We will begin by implementing a vector index search for finding relevant tasks by their name and description. If you are unfamiliar with vector similarity search, let me give you a quick refresher. The key idea is to calculate the text embedding values for each task based on their description and name. Then, at query time, find the most similar tasks to the user input using a similarity metric like a cosine distance.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea15_image-5.png)Vector similarity search in a RAG application. Image by author.

The retrieved information from the vector index can then be used as context to the LLM so it can generate accurate and up-to-date answers.

The tasks are already in our knowledge graph. However, we need to calculate the embedding values and create the vector index. This can be achieved with the `from_existing_graph` method.

`import os
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings

os.environ[&#x27;OPENAI_API_KEY&#x27;] = &quot;OPENAI_API_KEY&quot;

vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(),
    url=url,
    username=username,
    password=password,
    index_name=&#x27;tasks&#x27;,
    node_label=&quot;Task&quot;,
    text_node_properties=[&#x27;name&#x27;, &#x27;description&#x27;, &#x27;status&#x27;],
    embedding_node_property=&#x27;embedding&#x27;,
)`

In this example, we used the following graph-specific parameters for the `from_existing_graph` method.

- index_name: name of the vector index
- node_label: node label of relevant nodes
- text_node_properties: properties to be used to calculate embeddings and retrieve from the vector index
- embedding_node_property: which property to store the embedding values to

Now that the vector index has been initiated, we can use it as any other vector index in LangChain.

`response = vector_index.similarity_search(
    &quot;How will RecommendationService be updated?&quot;
)
print(response[0].page_content)
# name: BugFix
# description: Add a new feature to RecommendationService to provide ...
# status: In Progress`

You can observe that we construct a response of a map or dictionary-like string with defined properties in the `text_node_properties` parameter.

Now we can easily create a chatbot response by wrapping the vector index into a `RetrievalQA` module.

`from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

vector_qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    chain_type=&quot;stuff&quot;,
    retriever=vector_index.as_retriever()
)
vector_qa.run(
    &quot;How will recommendation service be updated?&quot;
)
# The RecommendationService is currently being updated to include a new feature
# that will provide more personalized and accurate product recommendations to
# users. This update involves leveraging user behavior and preference data to
# enhance the recommendation algorithm. The status of this update is currently
# in progress.`

One limitation of vector indexes, in general, is that they don’t provide the ability to aggregate information like you would with a structured query language like Cypher. Take, for example, the following example:

`vector_qa.run(
    &quot;How many open tickets there are?&quot;
)
# There are 4 open tickets.`

The response seems valid, and the LLM uses assertive language, making you believe the result is correct. However, the problem is that the response directly correlates to the number of retrieved documents from the vector index, which is four by default. What actually happens is that the vector index retrieves four open tickets, and the LLM unquestioningly believes that those are all the open tickets. However, the truth is different, and we can validate it using a Cypher statement.

`graph.query(
    &quot;MATCH (t:Task {status:&#x27;Open&#x27;}) RETURN count(*)&quot;
)
# [{&#x27;count(*)&#x27;: 5}]`

There are five open tasks in our toy graph. While vector similarity search is excellent for sifting through relevant information in unstructured text, it lacks the capability to analyze and aggregate structured information. Using Neo4j, this problem can be easily solved by employing Cypher, which is a structured query language for graph databases.

## Graph Cypher search

Cypher is a structured query language designed to interact with graph databases and provides a visual way of matching patterns and relationships. It relies on the following **ascii**-**art** type of syntax:

`(:Person {name:&quot;Tomaz&quot;})-[:LIVES_IN]-&gt;(:Country {name:&quot;Slovenia&quot;})
`

This patterns describes a node with a label **Person** and the name property **Tomaz** that has a **LIVES_IN** relationship to the **Country** node of **Slovenia**.

The neat thing about LangChain is that it provides a [GraphCypherQAChain](https://python.langchain.com/docs/use_cases/more/graph/graph_cypher_qa?ref=blog.langchain.com), which generates the Cypher queries for you, so you don’t have to learn Cypher syntax in order to retrieve information from a graph database like Neo4j.

The following code will refresh the graph schema and instantiate the Cypher chain.

`from langchain.chains import GraphCypherQAChain

graph.refresh_schema()

cypher_chain = GraphCypherQAChain.from_llm(
    cypher_llm = ChatOpenAI(temperature=0, model_name=&#x27;gpt-4&#x27;),
    qa_llm = ChatOpenAI(temperature=0), graph=graph, verbose=True,
)`

Generating valid Cypher statements is a complex task. Therefore, it is recommended to use state-of-the-art LLMs like gpt-4 to generate Cypher statements, while generating answers using the database context can be left to gpt-3.5-turbo.

Now, you can ask the same question about how many tickets are open.

`cypher_chain.run(
    &quot;How many open tickets there are?&quot;
)`

*Result is the following*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265e9f5_image-6.png)

You can also ask the chain to aggregate the data using various grouping keys, like the following example.

`cypher_chain.run(
    &quot;Which team has the most open tasks?&quot;
)`

*Result is the following
*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265e9f2_image-7.png)

You might say these aggregations are not graph-based operations, and you will be correct. We can, of course, perform more graph-based operations like traversing the dependency graph of microservices.

`cypher_chain.run(
    &quot;Which services depend on Database directly?&quot;
)`

*Result is the following
*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea0a_image-8.png)

Of course, you can also ask the chain to produce [variable-length path traversals](https://graphaware.com/graphaware/2015/05/19/neo4j-cypher-variable-length-relationships-by-example.html?ref=blog.langchain.com) by asking questions like:

`cypher_chain.run(
    &quot;Which services depend on Database indirectly?&quot;
)`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265e9f8_image-9.png)

Some of the mentioned services are the same as in the directly dependent question. The reason is the structure of the dependency graph and not the invalid Cypher statement.

## Knowledge graph agent

Since we have implemented separate tools for the structured and unstructured parts of the knowledge graph, we can add an agent that can use these two tools to explore the knowledge graph.

`from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

tools = [
    Tool(
        name=&quot;Tasks&quot;,
        func=vector_qa.run,
        description=&quot;&quot;&quot;Useful when you need to answer questions about descriptions of tasks.
        Not useful for counting the number of tasks.
        Use full question as input.
        &quot;&quot;&quot;,
    ),
    Tool(
        name=&quot;Graph&quot;,
        func=cypher_chain.run,
        description=&quot;&quot;&quot;Useful when you need to answer questions about microservices,
        their dependencies or assigned people. Also useful for any sort of
        aggregation like counting the number of tasks, etc.
        Use full question as input.
        &quot;&quot;&quot;,
    ),
]

mrkl = initialize_agent(
    tools,
    ChatOpenAI(temperature=0, model_name=&#x27;gpt-4&#x27;),
    agent=AgentType.OPENAI_FUNCTIONS, verbose=True
)`

Let’s try out how well does the agent works.

`response = mrkl.run(&quot;Which team is assigned to maintain PaymentService?&quot;)
print(response)`

*Result is the following*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea0d_image-10.png)

Let’s now try to invoke the **Tasks** tool.

`response = mrkl.run(&quot;Which tasks have optimization in their description?&quot;)
print(response)`

*Result is the following
*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb135394beb695265ea12_image-11.png)

One thing is certain. I have to work on my agent prompt engineering skills. There is definitely room for improvement in tools description. Additionally, you can also customize the agent prompt.

## Conclusion

Knowledge graphs are an excellent fit when you require structured and unstructured data to power your RAG applications. With the approach shown in this blog post, you can avoid polyglot architectures, where you must maintain and sync multiple types of databases. Learn more about graph-based search in LangChain [here](https://medium.com/neo4j/langchain-cypher-search-tips-tricks-f7c9e9abca4d?ref=blog.langchain.com).

The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/devops_rag.ipynb?ref=blog.langchain.com).

If you are eager to learn more about building AI applications with graphs, join us at the [NODES, online, 24h conference](https://neo4j.registration.goldcast.io/events/6fb85147-ca27-4310-9dec-cb345c53bd6f?ref=blog.langchain.com) organized by Neo4j on October 26th, 2023.

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