---
title: "Neo4j x LangChain: Deep dive into the new Vector index implementation"
author: "LangChain Accounts"
date: "2023-09-07"
url: "https://www.langchain.com/blog/neo4j-x-langchain-new-vector-index"
---

PartnerLangChain

# Neo4j x LangChain: Deep dive into the new Vector index implementation

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 7, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb16f4b4a669566a4c531_5-social--20-.png)

### Learn how to customize LangChain’s wrapper of Neo4j vector index

*Editor&#x27;s Note: This post was written in collaboration with the *[*Neo4j*](https://neo4j.com/?ref=blog.langchain.com)* team. We&#x27;ve been working closely with them on their new vector index and we&#x27;re really impressed with its ability to efficiently perform semantic search over unstructured text or other embedded data modalities, unlocking support for RAG applications and more customization.*

[Neo4j](https://neo4j.com/?ref=blog.langchain.com) was and is an excellent fit for [handling structured information](https://towardsdatascience.com/langchain-has-added-cypher-search-cb9d821120d5?ref=blog.langchain.com), but it struggled a bit with semantic search due to its brute-force approach. However, the struggle is in the past as Neo4j has[ introduced a new vector index in version 5.11](https://neo4j.com/blog/vector-search-deeper-insights/?ref=blog.langchain.com) designed to efficiently perform semantic search over unstructured text or other embedded data modalities. The newly added vector index makes Neo4j a great fit for most RAG applications as it now works great with both structured and unstructured data.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1704b4a669566a4c53a_1*AH05dvGA_7db_EMySc9AAw.png)Image by author.

This blog post is designed to walk you through all the customization options available in the Neo4j Vector Index implementation in LangChain.

The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/neo4jvector_langchain_deepdive.ipynb?ref=blog.langchain.com).

## Neo4j Environment setup

You need to setup a Neo4j 5.11 or greater to follow along with the examples in this blog post. The easiest way is to start a free instance on [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=blog.langchain.com), which offers cloud instances of Neo4j database. Alternatively, you can also setup a local instance of the Neo4j database by downloading the [Neo4j Desktop](https://neo4j.com/download/?ref=blog.langchain.com) application and creating a local database instance.

## Example dataset

For the purpose of this blog post, we will use the `WikipediaLoader` to fetch text from the Witcher page.

`from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import CharacterTextSplitter

# Read the wikipedia article
raw_documents = WikipediaLoader(query=&quot;The Witcher&quot;).load()
# Define chunking strategy
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=20
)
# Chunk the document
documents = text_splitter.split_documents(raw_documents)
# Remove the summary
for d in documents:
    del d.metadata[&quot;summary&quot;]`

### Neo4j Vector index customization

Each text chunk is stored in Neo4j as a single isolated node.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1704b4a669566a4c53d_1*ykWpIYVgxZqs-On7qXkRtg.png)Graph schema of imported documents.

By default, Neo4j vector index implementation in LangChain represents the documents using the `Chunk` node label, where the `text` property stores the text of the document, and the `embedding` property holds the vector representation of the text. The implementation allows you to customize the node label, text and embedding property names.

`neo4j_db = Neo4jVector.from_documents(
    documents,
    OpenAIEmbeddings(),
    url=url,
    username=username,
    password=password,
    database=&quot;neo4j&quot;,  # neo4j by default
    index_name=&quot;wikipedia&quot;,  # vector by default
    node_label=&quot;WikipediaArticle&quot;,  # Chunk by default
    text_node_property=&quot;info&quot;,  # text by default
    embedding_node_property=&quot;vector&quot;,  # embedding by default
    create_id_index=True,  # True by default
)`

In this example, we have specified that we want to store text chunks under the `WikipediaArticle` node label, where the `info` property is used to store text, and the `vector` property holds the text embedding representation. If you run the above examples, you should see the following information in the database.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1704b4a669566a4c543_1*2RB0omgeJyyHFF7LqHicQA.png)Node information.

As mentioned, we define the `info` property to contain the text information, while the `vector` property is used to store the embedding. Any other properties like the `source` and `title` are treated as document metadata.

By default, we also create a [unique node property constraint](https://neo4j.com/docs/cypher-manual/current/constraints/?ref=blog.langchain.com) on the id property of the specified node label for faster imports. If you don’t want to create a unique constraint, you can set the `create_id_index` to false. You can verify that the constraint has been created by using the following Cypher statement:

`neo4j_db.query(&quot;SHOW CONSTRAINTS&quot;)
#[{&#x27;id&#x27;: 4,
#  &#x27;name&#x27;: &#x27;constraint_e5da4d45&#x27;,
#  &#x27;type&#x27;: &#x27;UNIQUENESS&#x27;,
#  &#x27;entityType&#x27;: &#x27;NODE&#x27;,
#  &#x27;labelsOrTypes&#x27;: [&#x27;WikipediaArticle&#x27;],
#  &#x27;properties&#x27;: [&#x27;id&#x27;],
#  &#x27;ownedIndex&#x27;: &#x27;constraint_e5da4d45&#x27;,
#  &#x27;propertyType&#x27;: None}]`

As you would expect, we also create a vector index that will allow us to perform fast ANN searches.

`neo4j_db.query(
    &quot;&quot;&quot;SHOW INDEXES
       YIELD name, type, labelsOrTypes, properties, options
       WHERE type = &#x27;VECTOR&#x27;
    &quot;&quot;&quot;
)
#[{&#x27;name&#x27;: &#x27;wikipedia&#x27;,
#  &#x27;type&#x27;: &#x27;VECTOR&#x27;,
#  &#x27;labelsOrTypes&#x27;: [&#x27;WikipediaArticle&#x27;],
#  &#x27;properties&#x27;: [&#x27;vector&#x27;],
#  &#x27;options&#x27;: {&#x27;indexProvider&#x27;: &#x27;vector-1.0&#x27;,
#   &#x27;indexConfig&#x27;: {&#x27;vector.dimensions&#x27;: 1536,
#    &#x27;vector.similarity_function&#x27;: &#x27;cosine&#x27;}}}]`

The LangChain implementation created a vector index named `wikipedia` , which indexes the `vector` property of `WikipediaArticle` nodes. Additionally, the provided configuration informs us that the vector embedding dimension is `1536` and uses the `cosine` similarity function.

## Loading additional documents

You can use the `add_documents` method to load additional documents into an instantiated vector index.

`neo4j_db.add_documents(
    [
        Document(
            page_content=&quot;LangChain is the coolest library since the Library of Alexandria&quot;,
            metadata={&quot;author&quot;: &quot;Tomaz&quot;, &quot;confidence&quot;: 1.0}
        )
    ],
    ids=[&quot;langchain&quot;],
)`

LangChain allows you to provide document ids to the `add_document` method, which can be used to sync information across different system and make it easier to update or delete relevant text chunks.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1704b4a669566a4c540_1*fjn0sNiGglVtojnGFr3Qtg.png)

## Loading existing index

If you have an existing vector index in Neo4j with populated data, you can use the `from_existing_method` to connect to it.

`existing_index = Neo4jVector.from_existing_index(
    OpenAIEmbeddings(),
    url=url,
    username=username,
    password=password,
    index_name=&quot;wikipedia&quot;,
    text_node_property=&quot;info&quot;,  # Need to define if it is not default
)`

First, the `from_existing_method` checks if the index with the provided name actually exists in the database. If it exists, it can retrieve the node label and embedding node property from index configuration map, which means that you don’t have to manually set those.

`print(existing_index.node_label) # WikipediaArticle
print(existing_index.embedding_node_property) # vector`

However, the index information does not contain the text node property information. Therefore, if you use any property besides the default one (`text`), specify it using the `text_node_property` parameter.

## Custom retrieval queries

Since Neo4j is a native graph database, the vector index implementation in LangChain allows customization and enrichment of the returned information. However, this feature is intended for more advanced users as you are responsible for custom data loading as well as retrieval.

The `retrieval_query` parameter allows you to collect, transform, or calculate any additional graph information you want to return from the similarity search. To better understand it, we can look at the actual implementation in the code.

`read_query = (
    &quot;CALL db.index.vector.queryNodes($index, $k, $embedding) &quot;
    &quot;YIELD node, score &quot;
) + retrieval_query`

From the code, we can observe that the vector similarity search is hardcoded. However, we then have the option to add any intermediate steps and return additional information. The retrieval query must return the following three columns:

- text (String): This is usually the textual data that is associated with the node that has been retrieved. This could be the main content of the node, a name, a description, or any other text-based information.
- score (Float): This represents the similarity score between the query vector and the vector associated with the returned node. The score quantifies how similar the query is to the returned nodes, often on a scale from 0 to 1
- metadata (Dictionary): This is a more flexible column that can contain additional information about the node or the search. It can be a dictionary (or map) that includes various attributes or properties that give more context to the returned node.

We will add a relationship to a `WikipediaArticle`node to demonstrate this functionality.

`existing_index.query(
    &quot;&quot;&quot;MATCH (w:WikipediaArticle {id:&#x27;langchain&#x27;})
       MERGE (w)&lt;-[:EDITED_BY]-(:Person {name:&quot;Galileo&quot;})
    &quot;&quot;&quot;
)`

We have added an `EDITED_BY` relationship to the `WikipediaArticle` node with the given id. Let’s now test out a custom retrieval option.

`retrieval_query = &quot;&quot;&quot;
OPTIONAL MATCH (node)&lt;-[:EDITED_BY]-(p)
WITH node, score, collect(p) AS editors
RETURN node.info AS text,
       score,
       node {.*, vector: Null, info: Null, editors: editors} AS metadata
&quot;&quot;&quot;

existing_index_return = Neo4jVector.from_existing_index(
    OpenAIEmbeddings(),
    url=url,
    username=username,
    password=password,
    database=&quot;neo4j&quot;,
    index_name=&quot;wikipedia&quot;,
    text_node_property=&quot;info&quot;,
    retrieval_query=retrieval_query,
)`

I won’t go too much into the specifics of Cypher. You can use many resources to learn the basic syntax and more like the [Neo4j Graph Academy](https://graphacademy.neo4j.com/?ref=blog.langchain.com). To construct a valid retrieval query, you must know that the relevant node from the vector similarity search is available under the `node` reference variable, while the similarity metric value is available under the `score` reference.

Let’s try it out.

`existing_index_return.similarity_search(
    &quot;What do you know about LangChain?&quot;, k=1)

#[
#   Document(&quot;page_content=&quot;&quot;LangChain is the coolest library since the Library of Alexandria&quot;,
#   &quot;metadata=&quot;{
#      &quot;author&quot;:&quot;Tomaz&quot;,
#      &quot;confidence&quot;:1.0,
#      &quot;id&quot;:&quot;langchain&quot;,
#      &quot;editors&quot;:[
#         {
#            &quot;name&quot;:&quot;Galileo&quot;
#         }
#      ]
#   }&quot;)&quot;
#]`

You can observe that the metadata information contains the `editor` property, which was calculated from graph information.

## Summary

The newly added vector index implementation in Neo4j allows it to support RAG applications that rely on both structured and unstructured data, making it a perfect fit for highly-complex and connected datasets.

The code is available on GitHub.

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