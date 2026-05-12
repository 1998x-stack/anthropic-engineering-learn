---
title: "Knowledge Graph Guide: Build With Memgraph | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/constructing-a-knowledge-graph-with-llamaindex-and-memgraph"
category: "llamaindex-core"
---

Content



- [
Step 1: Install and Set Up Memgraph  ](#step-1-install-and-set-up-memgraph)
- [ Step 2: Install LlamaIndex and Memgraph Integration  ](#step-2-install-llamaindex-and-memgraph-integration)
- [
Step 3: Configure Your Environment  ](#step-3-configure-your-environment)
- [ Database Credentials  ](#database-credentials)
- [ Set up OpenAI API Key  ](#set-up-openai-api-key)
- [ Step 4: Load and Prepare Your Data  ](#step-4-load-and-prepare-your-data)
- [ Step 5: Build the Knowledge Graph  ](#step-5-build-the-knowledge-graph)
- [ Construct the Graph  ](#construct-the-graph)
- [ Step 6: Query the Knowledge Graph  ](#step-6-query-the-knowledge-graph)
- [ Why Natural Language Queries Matter  ](#why-natural-language-queries-matter)
- [ Visualizing Your Knowledge Graph  ](#visualizing-your-knowledge-graph)
- [
Transform Raw Data Into Actionable Knowledge  ](#transform-raw-data-into-actionable-knowledge)
- [ Next Steps  ](#next-steps)



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







 *This is a guest post from our friends at [Memgraph](https://memgraph.com/).*







 In this blog post, we’ll share how Memgraph [integrates](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/memgraph/) with [LlamaIndex](https://www.llamaindex.ai/). You can use LlamaIndex to transform raw data into a structured knowledge graph, which can then be queried using natural language.







 Here’s a step-by-step guide to get you started, complete with installation instructions, environment setup, and a sample knowledge graph created from Charles Darwin’s biography.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##
Step 1: Install and Set Up Memgraph



 The quickest way to get started with Memgraph (Memgraph db + MAGE library + Lab) is by running the following command:







 For Linux/macOS:



sh






```
curl https://install.memgraph.com | sh
```
    For Windows:



sh






```
iwr https://windows.memgraph.com | iex
```
    Once installed, launch [**Memgraph Lab**](https://memgraph.com/docs/data-visualization), a visual tool for interacting with your database. Access it through:


-  **Web**: [http://localhost:3000](http://localhost:3000/)
  -  **Desktop App**: Download [here](https://memgraph.com/download).



 If you need further details, check out the [Getting Started with Memgraph](https://memgraph.com/docs/getting-started#install-memgraph-platform) docs.







##  Step 2: Install LlamaIndex and Memgraph Integration



 Run the following command to install LlamaIndex and Memgraph’s graph integration package:



sh






```
%pip install llama-index llama-index-graph-stores-memgraph
```
    This package integrates LlamaIndex with Memgraph, allowing you to transform unstructured data into a structured knowledge graph that can be easily constructed, visualized, and queried.



##
Step 3: Configure Your Environment



###  Database Credentials



 Configure LlamaIndex to connect to your Memgraph database by setting up the following parameters:



python






```
from llama_index.graph_stores.memgraph import MemgraphPropertyGraphStore

username = ""  # Your Memgraph username, default is ""
password = ""  # Your Memgraph password, default is ""
url = "bolt://localhost:7687"  # Connection URL for Memgraph

graph_store = MemgraphPropertyGraphStore(
    username=username,
    password=password,
    url=url,
)
```


###  Set up OpenAI API Key

  Add your OpenAI API key to your environment for embedding and query processing.



python






```
import os
os.environ["OPENAI_API_KEY"] = "&#x3C;YOUR_API_KEY>"  # Replace with your OpenAI API key
```


##  Step 4: Load and Prepare Your Data

  Use a sample text file about **Charles Darwin** as your dataset, stored in `./data/charles_darwin/charles.txt` :



text






```
Charles Robert Darwin was an English naturalist, geologist, and biologist, widely known for his contributions to evolutionary biology. His proposition that all species of life have descended from a common ancestor is now generally accepted and considered a fundamental scientific concept. In a joint publication with Alfred Russel Wallace, he introduced his scientific theory that this branching pattern of evolution resulted from a process he called natural selection, in which the struggle for existence has a similar effect to the artificial selection involved in selective breeding. Darwin has been described as one of the most influential figures in human history and was honoured by burial in Westminster Abbey.
```
    Load this unstructured text data using LlamaIndex’s `SimpleDirectoryReader` :



python






```
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data/charles_darwin/").load_data()
```
    The data is now loaded in the documents variable and will be used as an argument in the next steps: index creation and graph construction.



##  Step 5: Build the Knowledge Graph



 LlamaIndex offers several [graph constructors](https://docs.llamaindex.ai/en/latest/module_guides/indexing/lpg_index_guide/#construction). For this tutorial, we’ll use the [SchemaLLMPathExtractor](https://docs.llamaindex.ai/en/latest/module_guides/indexing/lpg_index_guide/#schemallmpathextractor) to extract entities and relationships from the text automatically.



###  Construct the Graph



python






```
from llama_index.core import PropertyGraphIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor

index = PropertyGraphIndex.from_documents(
    documents,
    embed_model=OpenAIEmbedding(model_name="text-embedding-ada-002"),
    kg_extractors=[
        SchemaLLMPathExtractor(
            llm=OpenAI(model="gpt-4", temperature=0.0),
        )
    ],
    property_graph_store=graph_store,
    show_progress=True,
)
```
    This step creates a knowledge graph in Memgraph by identifying key concepts and their relationships from the Charles Darwin dataset. The graph is now queryable!







 In the image below, you can see how the text was transformed into a knowledge graph and stored into Memgraph.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/9c496e451841627addd5e7afd5428e907bb9e5e4-1256x634.png)

##  Step 6: Query the Knowledge Graph







 After constructing your knowledge graph, querying becomes straightforward. LlamaIndex offers various methods to retrieve nodes and paths from the graph. If no specific retrievers are configured, the system defaults to using the [LLMSynonymRetriever](https://docs.llamaindex.ai/en/latest/module_guides/indexing/lpg_index_guide/#default-llmsynonymretriever).







###  Why Natural Language Queries Matter



 Using natural language, you can ask questions that would typically require complex query languages. Here, the model fetches relevant information from the graph and returns it in a human-readable format, leveraging the connections and entities captured during graph construction.







 **Example query:**



python






```
query_engine = index.as_query_engine(include_text=True)

response = query_engine.query("Who did Charles Robert Darwin collaborate with?")
print(str(response))
```
    **Query**: &quot;Who did Charles Robert Darwin collaborate with?&quot;**Response**: The system identifies **Alfred Russel Wallace** as a collaborator.



 This allows even non-technical users to extract insights easily using natural language.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/39d09d007ec5698a5888a844ffb05960086b3b82-968x1040.png)

##  Visualizing Your Knowledge Graph



 Use **Memgraph Lab** to explore your graph visually. You’ll see entities like &quot;Charles Darwin&quot; and &quot;Alfred Russel Wallace,&quot; along with their relationships. This helps in understanding how data points connect, making your insights more actionable.



 Read more: [Memgraph Lab 101: Simplify Graph Data Exploration with Visualization and Querying](https://memgraph.com/blog/lab-guide-graph-data-visualization-querying)



##
Transform Raw Data Into Actionable Knowledge



 With LlamaIndex and Memgraph, you can bridge unstructured data and advanced analytics.







 This integration offers:


-  Effortless data transformation - build knowledge graphs from raw text.
  -  Intuitive querying - extract insights in natural language without technical barriers.
  -  Scalable insights - use Memgraph’s property graph for various advanced applications, including GenAI.



##  Next Steps



 Now that you successfully built your knowledge graph, it’s time to unlock the full potential with Memgraph’s algorithms to further analyze your data. Dive into algorithms such as [PageRank](https://memgraph.com/docs/advanced-algorithms/available-algorithms/pagerank), [community detection](https://memgraph.com/docs/advanced-algorithms/available-algorithms/community_detection) and [Leiden](https://memgraph.com/docs/advanced-algorithms/available-algorithms/leiden_community_detection) to take your graph analysis to the next level.