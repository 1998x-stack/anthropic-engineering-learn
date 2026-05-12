---
title: "Constructing knowledge graphs from text using OpenAI functions: Leveraging knowledge graphs to power LangChain Applications"
author: "LangChain Accounts"
date: "2023-10-19"
url: "https://www.langchain.com/blog/constructing-knowledge-graphs-from-text-using-openai-functions"
---

PartnerTutorials &amp; How-Tos

# Constructing knowledge graphs from text using OpenAI functions: Leveraging knowledge graphs to power LangChain Applications

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 19, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)10min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1128232fce8d20f21c6_Twitter-post---17--1-.png)*Editor&#x27;s Note: This post was written by *[*Tomaz Bratanic*](https://twitter.com/tb_tomaz?ref=blog.langchain.com)* from the Neo4j team.*

Extracting structured information from unstructured data like text has been around for some time and is nothing new. However, LLMs brought a significant shift to the field of information extraction. If before you needed a team of machine learning experts to curate datasets and train custom models, you only need access to an LLM nowadays. The barrier to entry has dropped significantly, making what was just a couple of years ago reserved for domain experts more accessible to even non-technical people.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1128232fce8d20f21cc_1*RYCIqV1Gfp18VkXfY411Xg.jpeg)The goal of information extraction pipeline is to extract structured information from unstructured text. Image by the author.

The image depicts the transformation of unstructured text into structured information. This process, labeled as the information extraction pipeline, results in a graph representation of information. The nodes represent key entities, while the connecting lines denote the relationships between these entities. Knowledge graphs are useful for [multi-hop question-answering](https://medium.com/neo4j/knowledge-graphs-llms-multi-hop-question-answering-322113f53f51?ref=blog.langchain.com), [real-time analytics](https://medium.com/neo4j/knowledge-graphs-llms-real-time-graph-analytics-89b392eaaa95?ref=blog.langchain.com), or when you want to [combine structured and unstructured data in a single database](https://blog.langchain.com/using-a-knowledge-graph-to-implement-a-devops-rag-application/).

While extracting structured information from text has been made more accessible due to LLMs, it is by no means a solved problem. In this blog post, we will use [OpenAI functions in combination with LangChain](https://python.langchain.com/docs/modules/chains/how_to/openai_functions?ref=blog.langchain.com) to construct a knowledge graph from a sample Wikipedia page. Along the way, we will discuss best practices as well as some limitations of current LLMs.

tldr; The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/openaifunction_constructing_graph.ipynb?ref=blog.langchain.com).

# Neo4j Environment setup

You need to setup a Neo4j to follow along with the examples in this blog post. The easiest way is to start a free instance on [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=blog.langchain.com), which offers cloud instances of Neo4j database. Alternatively, you can also setup a local instance of the Neo4j database by downloading the [Neo4j Desktop](https://neo4j.com/download/?ref=blog.langchain.com) application and creating a local database instance.

The following code will instantiate a LangChain wrapper to connect to Neo4j Database.

`from langchain.graphs import Neo4jGraph

url = &quot;neo4j+s://databases.neo4j.io&quot;
username =&quot;neo4j&quot;
password = &quot;&quot;
graph = Neo4jGraph(
    url=url,
    username=username,
    password=password
)`

# Information extraction pipeline

A typical information extraction pipeline contains the following steps.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1138232fce8d20f21da_1*93ZK9-74dYv4eXY-Oe_bkA.png)Multiple steps of information extraction pipeline. Image by author.

In the first step, we run the input text through a coreference resolution model. The coreference resolution is the task of finding all expressions that refer to a specific entity. Simply put, it links all the pronouns to the referred entity. In the named entity recognition part of the pipeline, we try to extract all the mentioned entities. The above example contains three entities: Tomaz, Blog, and Diagram. The next step is the entity disambiguation step, an essential but often overlooked part of an information extraction pipeline. Entity disambiguation is the process of accurately identifying and distinguishing between entities with similar names or references to ensure the correct entity is recognized in a given context. In the last step, the model tried to identify various relationships between entities. For example, it could locate the **LIKES** relationship between **Tomaz** and **Blog** entities.

## Extracting structured information with OpenAI functions

[OpenAI functions](https://openai.com/blog/function-calling-and-other-api-updates?ref=blog.langchain.com) are a great fit to extract structured information from natural language. The idea behind OpenAI functions is to have an LLM output a predefined JSON object with populated values. The predefined JSON object can be used as input to other functions in so-called RAG applications, or it can be used to extract predefined structured information from text.

In LangChain, you can[ pass a Pydantic class as description](https://python.langchain.com/docs/modules/chains/how_to/openai_functions?ref=blog.langchain.com) of the desired JSON object of the OpenAI functions feature. Therefore, we will start by defining the desired structure of information we want to extract from text. LangChain already has [definitions of nodes and relationship as Pydantic classes that we can reuse](https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/graphs/graph_document.py?ref=blog.langchain.com).

`class Node(Serializable):
    &quot;&quot;&quot;Represents a node in a graph with associated properties.

    Attributes:
        id (Union[str, int]): A unique identifier for the node.
        type (str): The type or label of the node, default is &quot;Node&quot;.
        properties (dict): Additional properties and metadata associated with the node.
    &quot;&quot;&quot;

    id: Union[str, int]
    type: str = &quot;Node&quot;
    properties: dict = Field(default_factory=dict)

class Relationship(Serializable):
    &quot;&quot;&quot;Represents a directed relationship between two nodes in a graph.

    Attributes:
        source (Node): The source node of the relationship.
        target (Node): The target node of the relationship.
        type (str): The type of the relationship.
        properties (dict): Additional properties associated with the relationship.
    &quot;&quot;&quot;

    source: Node
    target: Node
    type: str
    properties: dict = Field(default_factory=dict)`

Unfortunately, it turns out that OpenAI functions don’t currently support a dictionary object as a value. Therefore, we have to overwrite the **properties** definition to adhere to the limitations of the functions’ endpoint.

`from langchain.graphs.graph_document import (
    Node as BaseNode,
    Relationship as BaseRelationship
)
from typing import List, Dict, Any, Optional
from langchain.pydantic_v1 import Field, BaseModel

class Property(BaseModel):
  &quot;&quot;&quot;A single property consisting of key and value&quot;&quot;&quot;
  key: str = Field(..., description=&quot;key&quot;)
  value: str = Field(..., description=&quot;value&quot;)

class Node(BaseNode):
    properties: Optional[List[Property]] = Field(
        None, description=&quot;List of node properties&quot;)

class Relationship(BaseRelationship):
    properties: Optional[List[Property]] = Field(
        None, description=&quot;List of relationship properties&quot;
    )`

Here, we have overwritten the properties value to be a list of **Property** classes instead of a dictionary to overcome the limitations of the API. Because you can only pass a single object to the API, we can to combine the nodes and relationships in a single class called **KnowledgeGraph**.

`class KnowledgeGraph(BaseModel):
    &quot;&quot;&quot;Generate a knowledge graph with entities and relationships.&quot;&quot;&quot;
    nodes: List[Node] = Field(
        ..., description=&quot;List of nodes in the knowledge graph&quot;)
    rels: List[Relationship] = Field(
        ..., description=&quot;List of relationships in the knowledge graph&quot;
    )`

The only thing left is to do a bit of prompt engineering and we are good to go. How I usually go about prompt engineering is the following:

- Iterate over prompt and improve results using natural language
- If something doesn’t work as intended, ask ChatGPT to make it clearer for an LLM to understand the task
- Finally, when the prompt has all the instructions needed, ask ChatGPT to summarize the instructions in a markdown format, saving on tokens and perhaps having more clear instructions

I specifically chose the markdown format as I have seen somewhere that OpenAI models respond better to markdown syntax in prompts, and it seems to be at least plausible from my experience.

Iterating over prompt engineering, I came up with the following system prompt for an information extraction pipeline.

`llm = ChatOpenAI(model=&quot;gpt-3.5-turbo-16k&quot;, temperature=0)

def get_extraction_chain(
    allowed_nodes: Optional[List[str]] = None,
    allowed_rels: Optional[List[str]] = None
    ):
    prompt = ChatPromptTemplate.from_messages(
    [(
      &quot;system&quot;,
      f&quot;&quot;&quot;# Knowledge Graph Instructions for GPT-4
## 1. Overview
You are a top-tier algorithm designed for extracting information in structured formats to build a knowledge graph.
- **Nodes** represent entities and concepts. They&#x27;re akin to Wikipedia nodes.
- The aim is to achieve simplicity and clarity in the knowledge graph, making it accessible for a vast audience.
## 2. Labeling Nodes
- **Consistency**: Ensure you use basic or elementary types for node labels.
  - For example, when you identify an entity representing a person, always label it as **&quot;person&quot;**. Avoid using more specific terms like &quot;mathematician&quot; or &quot;scientist&quot;.
- **Node IDs**: Never utilize integers as node IDs. Node IDs should be names or human-readable identifiers found in the text.
{&#x27;- **Allowed Node Labels:**&#x27; + &quot;, &quot;.join(allowed_nodes) if allowed_nodes else &quot;&quot;}
{&#x27;- **Allowed Relationship Types**:&#x27; + &quot;, &quot;.join(allowed_rels) if allowed_rels else &quot;&quot;}
## 3. Handling Numerical Data and Dates
- Numerical data, like age or other related information, should be incorporated as attributes or properties of the respective nodes.
- **No Separate Nodes for Dates/Numbers**: Do not create separate nodes for dates or numerical values. Always attach them as attributes or properties of nodes.
- **Property Format**: Properties must be in a key-value format.
- **Quotation Marks**: Never use escaped single or double quotes within property values.
- **Naming Convention**: Use camelCase for property keys, e.g., `birthDate`.
## 4. Coreference Resolution
- **Maintain Entity Consistency**: When extracting entities, it&#x27;s vital to ensure consistency.
If an entity, such as &quot;John Doe&quot;, is mentioned multiple times in the text but is referred to by different names or pronouns (e.g., &quot;Joe&quot;, &quot;he&quot;),
always use the most complete identifier for that entity throughout the knowledge graph. In this example, use &quot;John Doe&quot; as the entity ID.
Remember, the knowledge graph should be coherent and easily understandable, so maintaining consistency in entity references is crucial.
## 5. Strict Compliance
Adhere to the rules strictly. Non-compliance will result in termination.&quot;&quot;&quot;),
        (&quot;human&quot;, &quot;Use the given format to extract information from the following input: {input}&quot;),
        (&quot;human&quot;, &quot;Tip: Make sure to answer in the correct format&quot;),
    ])
    return create_structured_output_chain(KnowledgeGraph, llm, prompt, verbose=False)`

You can see that we are using the 16k version of the GPT-3.5 model. The main reason is that the OpenAI function output is a structured JSON object, and structured JSON syntax adds a lot of token overhead to the result. Essentially, you are paying for the convenience of structured output in increased token space.

Besides the general instructions, I have also added the option to limit which node or relationship types should be extracted from text. You’ll see through examples why this might come in handy.

We have the Neo4j connection and LLM prompt ready, which means we can define the information extraction pipeline as a single function.

`def extract_and_store_graph(
    document: Document,
    nodes:Optional[List[str]] = None,
    rels:Optional[List[str]]=None) -&gt; None:
    # Extract graph data using OpenAI functions
    extract_chain = get_extraction_chain(nodes, rels)
    data = extract_chain.run(document.page_content)
    # Construct a graph document
    graph_document = GraphDocument(
      nodes = [map_to_base_node(node) for node in data.nodes],
      relationships = [map_to_base_relationship(rel) for rel in data.rels],
      source = document
    )
    # Store information into a graph
    graph.add_graph_documents([graph_document])`

The function takes in a LangChain document as well as optional nodes and relationship parameters, which are used to limit the types of objects we want the LLM to identify and extract. A month or so ago, we added the `add_graph_documents` method the Neo4j graph object, which we can utilize here to seamlessly import the graph.

## Evaluation

We will extract information from the Walt Disney Wikipedia page and construct a knowledge graph to test the pipeline. Here, we will utilize the Wikipedia loader and text chunking modules provided by LangChain.

`from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import TokenTextSplitter

# Read the wikipedia article
raw_documents = WikipediaLoader(query=&quot;Walt Disney&quot;).load()
# Define chunking strategy
text_splitter = TokenTextSplitter(chunk_size=2048, chunk_overlap=24)

# Only take the first the raw_documents
documents = text_splitter.split_documents(raw_documents[:3])`

You might have noticed that we use a relatively large `chunk_size` value. The reason is that we want to provide as much context as possible around a single sentence in order for the coreference resolution part to work as best as possible. Remember, the coreference step will only work if the entity and its reference appear in the same chunk; otherwise, the LLM doesn’t have enough information to link the two.

Now we can go ahead and run the documents through the information extraction pipeline.

`from tqdm import tqdm

for i, d in tqdm(enumerate(documents), total=len(documents)):
    extract_and_store_graph(d)`

The process takes around 5 minutes, which is relatively slow. Therefore, you would probably want parallel API calls in production to deal with this problem and achieve some sort of scalability.

Let’s first look at the types of nodes and relationships the LLM identified.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1138232fce8d20f21d4_1*OCjG5oY6DyOnLuo1_N4OlA.png)

Since the graph schema is not provided, the LLM decides on the fly what types of node labels and relationship types it will use. For example, we can observe that there are **Company** and **Organization** node labels. Those two things are probably semantically similar or identical, so we would want to have only a single node label representing the two. This problem is more obvious with relationship types. For example, we have **CO-FOUNDER** and **COFOUNDEROF** relationships as well as **DEVELOPER** and **DEVELOPEDBY**.

For any more serious project, you should define the node labels and relationship types the LLM should extract. Luckily, we have added the option to limit the types in the prompt by passing additional parameters.

`# Specify which node labels should be extracted by the LLM
allowed_nodes = [&quot;Person&quot;, &quot;Company&quot;, &quot;Location&quot;, &quot;Event&quot;, &quot;Movie&quot;, &quot;Service&quot;, &quot;Award&quot;]

for i, d in tqdm(enumerate(documents), total=len(documents)):
    extract_and_store_graph(d, allowed_nodes)`

In this example, I have only limited the node labels, but you can easily limit the relationship types by passing another parameter to the `extract_and_store_graph` function.

The visualization of the extracted subgraph has the following structure.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1138232fce8d20f21e0_1*mEipkYmePMYvX4t5tU8u2w.png)

The graph turned out better than expected (after five iterations :) ). I couldn’t catch the whole graph nicely in the visualization, but you can explore it on your own in Neo4j Browser other tools.

## Entity disambiguation

One thing I should mention is that we partly skipped entity disambiguation part. We used a large chunk size and added a specific instruction for coreference resolution and entity disambiguation in the system prompt. However, since each chunk is processed separately, there is no way to ensure consistency of entities between different text chunks. For example, you could end up with two nodes representing the same person.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1138232fce8d20f21dd_1*PHsfndcMjOMoAdUAx8IJrw.png)Multiple nodes representing the same entity.

In this example, Walt Disney and Walter Elias Disney refer to the same real-world person. The entity disambiguation problem is nothing new and there has been various solution proposed to solve it:

- Using [entity linking](https://wikifier.org/about.html?ref=blog.langchain.com) or [entity disambiguation](https://github.com/SapienzaNLP/extend?ref=blog.langchain.com) NLP models
- Doing a [second pass through an LLM](https://medium.com/neo4j/creating-a-knowledge-graph-from-video-transcripts-with-gpt-4-52d7c7b9f32c?ref=blog.langchain.com) and asking it to perform entity disambiguation
- [Graph-based approaches](https://neo4j.com/developer-blog/exploring-supervised-entity-resolution-in-neo4j/?ref=blog.langchain.com)

Which solution you should use depends on your domain and use case. However, have in mind that entity disambiguation step should not be overlooked as it can have a significant impact on the accuracy and effectiveness of your RAG applications.

## Rag Application

The last thing we will do is show you how you can browse information in a knowledge graph by constructing Cypher statements. Cypher is a structured query language used to work with graph databases, similar to how SQL is used for relational databases. LangChain has a [GraphCypherQAChain](https://medium.com/neo4j/langchain-cypher-search-tips-tricks-f7c9e9abca4d?ref=blog.langchain.com) that reads the schema of the graph and constructs appropriate Cypher statements based on the user input.

`# Query the knowledge graph in a RAG application
from langchain.chains import GraphCypherQAChain

graph.refresh_schema()

cypher_chain = GraphCypherQAChain.from_llm(
    graph=graph,
    cypher_llm=ChatOpenAI(temperature=0, model=&quot;gpt-4&quot;),
    qa_llm=ChatOpenAI(temperature=0, model=&quot;gpt-3.5-turbo&quot;),
    validate_cypher=True, # Validate relationship directions
    verbose=True
)
cypher_chain.run(&quot;When was Walter Elias Disney born?&quot;)
`

*Result is the following*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1138232fce8d20f21d7_1*CTF2gfNwx4v7V-0qM4s6uw.png)

## Summary

Knowledge graphs are a great fit when you need a combination of structured and structured data to power your RAG applications. In this blog post, you have learned how to construct a knowledge graph in Neo4j on an arbitrary text using OpenAI functions. OpenAI functions provide the convenience of neatly structured outputs, making them an ideal fit for extracting structured information. To have a great experience constructing graphs with LLMs, make sure to define the graph schema as detailed as possible and make sure you add an entity disambiguation step after the extraction.

If you are eager to learn more about building AI applications with graphs, join us at the [NODES, online, 24h conference](https://neo4j.registration.goldcast.io/events/6fb85147-ca27-4310-9dec-cb345c53bd6f?ref=blog.langchain.dev) organized by Neo4j on October 26th, 2023.

The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/openaifunction_constructing_graph.ipynb?ref=blog.langchain.com).

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