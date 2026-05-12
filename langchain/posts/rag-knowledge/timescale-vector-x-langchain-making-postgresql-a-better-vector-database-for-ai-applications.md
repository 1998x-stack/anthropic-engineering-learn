---
title: "Timescale Vector x LangChain: Making PostgreSQL A Better Vector Database for AI Applications"
author: "LangChain Accounts"
date: "2023-09-24"
url: "https://www.langchain.com/blog/timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications"
---

Partner

# Timescale Vector x LangChain: Making PostgreSQL A Better Vector Database for AI Applications

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 24, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)15min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9ac6bd6891faf3ee3f00_image2.webp)*Editor&#x27;s Note: This post was written in collaboration with the Timescale Vector team. Their integration with LangChain supports PostgreSQL as your vector database for faster similarity search, time-based context retrieval for RAG, and self-querying capabilities. And they&#x27;re *[*offering a free 90 day trial!*](https://console.cloud.timescale.com/signup?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral)

Introducing the [Timescale Vector](https://www.timescale.com/ai?ref=blog.langchain.com) integration for LangChain. Timescale Vector enables LangChain developers to build better AI applications with PostgreSQL as their vector database: with faster vector similarity search, efficient time-based search filtering, and the operational simplicity of a single, easy-to-use cloud PostgreSQL database for not only vector embeddings, but an AI application’s relational and time-series data too.

PostgreSQL is the world’s most loved database, according to the [Stack Overflow 2023 Developer Survey](https://survey.stackoverflow.co/2023/?ref=blog.langchain.com#section-most-popular-technologies-databases). And for a good reason: it’s been battle-hardened by production use for over three decades, it’s robust and reliable, and it has a rich ecosystem of tools, drivers, and connectors.

And while pgvector, the open-source extension for vector data on PostgreSQL, is a wonderful extension (and is offered as part of Timescale Vector), it is just one piece of the puzzle in providing a production-grade experience for AI application developers on PostgreSQL. After speaking with numerous developers at nimble startups and established industry giants, we saw the need to enhance pgvector to cater to the performance and operational needs of developers building AI applications.

Here’s the TL;DR on how Timescale Vector helps you build better AI applications with LangChain:

- **Faster similarity search on millions of vectors: **Thanks to the introduction of a new search index inspired by the DiskANN algorithm, [Timescale Vector achieves 243% faster search speed at ~99 % recall than Weaviate, a specialized database,](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral) and outperforms all existing PostgreSQL search indexes by between 39.39% and 1,590.33% on a dataset of one million OpenAI embeddings. Plus, enabling product quantization yields a [10x index space savings compared to pgvector](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral). Timescale Vector also offers pgvector’s Hierarchical Navigable Small Worlds (HNSW) and Inverted File Flat (IVFFlat) indexing algorithms.
- **Similarity search with efficient time-based filtering: **Timescale Vector optimizes time-based vector search, leveraging the automatic time-based partitioning and indexing of [Timescale’s hypertables](https://docs.timescale.com/use-timescale/latest/hypertables/?ref=blog.langchain.com) to efficiently find recent embeddings, constrain vector search by a time range or document age, and store and retrieve large language model (LLM) response and chat history with ease. Time-based semantic search also enables you to use Retrieval Augmented Generation (RAG) with time-based context retrieval to give users more useful LLM responses.
- **Simplified AI infra stack:** By combining vector embeddings, relational data, and time-series data in one PostgreSQL database, Timescale Vector eliminates the operational complexity that comes with managing multiple database systems at scale.
- **Simplified metadata handling and multi-attribute filtering: **You can leverage all PostgreSQL data types to store and filter metadata, and JOIN vector search results with relational data for more contextually relevant responses. In future releases, Timescale Vector will also support rich multi-attribute filtering, enabling even faster similarity searches when filtering on metadata.

On top of these innovations for vector workloads, Timescale Vector provides a robust, production-ready PostgreSQL platform with flexible pricing, enterprise-grade security, and free expert support.

In the rest of this post, we’ll dive deeper (with code!) into the unique capabilities Timescale Vector enables for developers wanting to use PostgreSQL as their vector database with LangChain:

- Faster similarity search with DiskANN, HNSW and IVFFlat index types.
- Efficient similarity search when filtering vectors by time.
- Retrieval Augmented Generation (RAG) with time-based context retrieval.
- Advanced self-querying capabilities.

(If you’d prefer to jump into the code, explore [this tutorial](https://python.langchain.com/docs/integrations/vectorstores/timescalevector?ref=blog.langchain.com)).

**🎉 **[**LangChain Users Get 3 Months Free of Timescale Vector**](https://console.cloud.timescale.com/signup?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral)

Timescale is giving LangChain users an extended 90-day trial of Timescale Vector. This makes it easy to test and develop your applications with Timescale Vector, as you won’t be charged for any cloud PostgreSQL databases you spin up during your trial period. [Try Timescale Vector for free today](https://console.cloud.timescale.com/signup?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral).

# Faster Vector Similarity Search in PostgreSQL

Timescale Vector speeds up Approximate Nearest Neighbor (ANN) search on large scale vector datasets, enhancing pgvector with a state-of-the-art ANN index inspired by the[ DiskANN ](https://www.microsoft.com/en-us/research/publication/diskann-fast-accurate-billion-point-nearest-neighbor-search-on-a-single-node/?ref=blog.langchain.com)algorithm. Timescale Vector also offers pgvector’s HNSW and IVFFlat indexing algorithms as well, giving developers the flexibility to choose the right index for their use case.

Our performance benchmarks using the [ANN benchmarks](https://github.com/erikbern/ann-benchmarks/?ref=blog.langchain.com) suite show that Timescale Vector achieves between 39.43% and 1,590.33% faster search speed at ~99 % recall than all existing PostgreSQL search indexes and 243.77% faster search speed than specialized vector databases like Weaviate, on a dataset of one million OpenAI embeddings. You can [read more about the performance benchmark methodology and results here.](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral)

*Caption: Timescale Vector’s new index outperforms specialized vector database Weaviate by 243% and all existing PostgreSQL index types when performing approximate nearest neighbor searches at 99% recall on 1 million OpenAI embeddings.*

Using Timescale Vector’s DiskANN, HNSW, or IVFFLAT indexes in LangChain is incredibly straightforward.

Simply create a Timescale Vector vector store as shown below:

`from langchain.vectorstores.timescalevector import TimescaleVector

# Create a Timescale Vector instance from the collection of documents
db = TimescaleVector.from_documents(
   embedding=embeddings,
   documents=docs,
   collection_name=COLLECTION_NAME,
   service_url=SERVICE_URL,
)`

And then run:

`# create an index
# by default this will create a Timescale Vector (DiskANN) index
db.create_index()`

This will create a timescale-vector index with the default parameters.

We should point out that the term “index” is a bit overloaded. For many vector databases, an index is the thing that stores your data (in relational databases this is often called a table), but in the PostgreSQL world an index is something that speeds up search, and we are using the latter meaning here.

We can also specify the exact parameters for index creation in the `create_index` command as follows:

`# create an timescale vector index (DiskANN) with specified parameters
db.create_index(index_type=&quot;tsv&quot;, max_alpha=1.0, num_neighbors=50)`

Advantages to this Timescale Vector’s new DiskANN-inspired vector search index include the following:

- Faster vector search at high accuracy in PostgreSQL.
- Optimized for running on disks, not only in memory use.
- Quantization optimization compatible with PostgreSQL, reducing the vector size and consequently shrinking the index size ([by 10x in some cases](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=llamaindex&amp;utm_medium=referral)!) and expediting searches.
- Efficient hybrid search or filtering additional dimensions.

For more on DiskANN and how Timescale Vector’s new index works, [see this blog post](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral).

Pgvector is packaged as part of Timescale Vector, so you can also access pgvector’s HNSW and IVFFLAT indexing algorithms in your LangChain applications. The ability to conveniently create database indexes from your LangChain application code makes it easy to create different indexes and compare their performance.

`# Create an HNSW index.
# Note: you don&#x27;t need to specify m and ef_construction parameters as we set smart defaults.
db.create_index(index_type=&quot;hnsw&quot;, m=16, ef_construction=64)

# Create an IVFFLAT index
# Note:you don&#x27;t need to specify num_lists and num_records parameters as we set smart defaults.
db.create_index(index_type=&quot;ivfflat&quot;, num_lists=20, num_records=1000)`

# Add Efficient Time-Based Search Functionality to Your LangChain AI Application

Timescale Vector optimizes time-based vector search,** **leveraging the automatic time-based partitioning and indexing of [Timescale’s hypertables](https://docs.timescale.com/use-timescale/latest/hypertables/?ref=blog.langchain.com) to efficiently search vectors by time and similarity.

Time is often an important metadata component for vector embeddings. Sources of embeddings, like documents, images, and web pages, often have a timestamp associated with them, for example, their creation date, publishing date, or the date they were last updated, to name but a few.

We can take advantage of this time metadata in our collections of vector embeddings to enrich the quality and applicability of search results by retrieving vectors that are not just semantically similar but also pertinent to a specific time frame.

Here are some examples where time-based retrieval of vectors can improve your LangChain applications:

- **Chat history: **Storing and retrieving LLM response history. For example, chatbot chat history.
- **Finding recent embeddings: **Finding the most recent embeddings similar to a query vector. For example, finding the most recent news, documents, or social media posts related to elections.
- **Search within a time range: **Constraining similarity search to only vectors within a relevant time range. For example, asking time-based questions about a knowledge base (“What new features were added between January and March 2023?”).

Let’s look at an example of performing time-based searches on a [git log dataset](https://chat.openai.com/share/0612295b-a408-4e02-9ac2-3dc231fa89d1?ref=blog.langchain.com). In a git log, each entry has a timestamp, an author, and some information about the commit.

To illustrate how to use TimescaleVector&#x27;s time-based vector search functionality, we&#x27;ll ask questions about the git log history for TimescaleDB. Each git commit entry has a timestamp associated with it, as well as a message and other metadata (e.g., author).

### Load text and extract metadata

First, we load in the git log using LangChain’s [JSON Loader](https://python.langchain.com/docs/modules/data_connection/document_loaders/json?ref=blog.langchain.com).

`# Load data from JSON file and extract metadata
loader = JSONLoader(
   file_path=FILE_PATH,
   jq_schema=&#x27;.commit_history[]&#x27;,
   text_content=False,
   metadata_func=extract_metadata
)
documents = loader.load()`

Notice how we provide a function named `extract_metadata` as an argument to the JSONLoader. This function enables us to store not just the contents of the JSON in vectorized form but metadata about an embedding. It is in this function that we’ll specify the timestamp of the git log entry to be used in our time-based vector search.

### Create time-based identifiers for Documents

For time-based search in LangChain, Timescale Vector uses the ‘datetime’ portion of a UUID v1 to place vectors in the correct time partition. [Timescale Vector’s Python client library](https://github.com/timescale/python-vector?ref=blog.langchain.com) provides a simple-to-use function named `uuid_from_time` to create a UUID v1 from a Python `datetime` object, which you can then pass to the Timescale Vector vector store constructor as we’ll see in the code snippet further down. Here’s how we use the `uuid_from_time` helper functions:

`from timescale_vector import client
# Function to take in a date string in the past and return a uuid v1
def create_uuid(date_string: str):
   if date_string is None:
       return None
   time_format = &#x27;%a %b %d %H:%M:%S %Y %z&#x27;
   datetime_obj = datetime.strptime(date_string, time_format)
   uuid = client.uuid_from_time(datetime_obj)
   return str(uuid)`

Here’s the `extract_metdata()` function we pass to the JSONLoader specifying the fields we want in the metadata for each vector embedding in our vector collection:

`# Metadata extraction function to extract metadata from a JSON record
def extract_metadata(record: dict, metadata: dict) -&gt; dict:
   record_name, record_email = split_name(record[&quot;author&quot;])
   metadata[&quot;id&quot;] = create_uuid(record[&quot;date&quot;])
   metadata[&quot;date&quot;] = create_date(record[&quot;date&quot;])
   metadata[&quot;author_name&quot;] = record_name
   metadata[&quot;author_email&quot;] = record_email
   metadata[&quot;commit_hash&quot;] = record[&quot;commit&quot;]
   return metadata`

**Note:** The code above references two helper functions to get things in the right format (`split_name()` and `create_date()`) which we’ve omitted for brevity. The full code is included in the tutorial linked in the Resources section at the end of this post.

Next, we&#x27;ll create a Timescale Vector instance from the collection of documents we loaded into the JSONLoader above.

### Load vectors and metadata into Timescale Vector

Finally, we&#x27;ll create the Timescale Vector instance from the set of documents we loaded in.

To take advantage of Timescale Vector’s efficient time-based search, we need to specify the `time_partition_interval` argument when creating a Timescale Vector vector store. This argument represents the length of each interval for partitioning the data by time. Each partition will consist of data that falls within the specified length of time.

In the example below, we use seven days for simplicity, but you can pick whatever value makes sense for your use case—for example, if you query recent vectors frequently, you might want to use a smaller time delta (ike one day), or if you query vectors over a decade-long time period, then you might want to use a larger time delta like six months or one year.  As a rule of thumb, common queries should touch only a couple of partitions and at the same time your full dataset should fit within a 1000 partitions, but don’t stress too much – the system is not very sensitive to this value.

We specify the `ids` argument to be a list of the UUID v1s we created in the pre-processing step above and stored in the ID field of our metadata. We do this because we want the time part of our UUIDs to reflect past dates. If we want the current date and time to be associated with our document, we can remove the `id` argument, and UUIDs will be automatically created with the current date and time.

`# Define collection name
COLLECTION_NAME = &quot;timescale_commits&quot;
embeddings = OpenAIEmbeddings()

# Create a Timescale Vector instance from the collection of documents
db = TimescaleVector.from_documents(
     embedding=embeddings,
     ids = [doc.metadata[&quot;id&quot;] for doc in docs],
     documents=docs,
     collection_name=COLLECTION_NAME,
     service_url=SERVICE_URL,
     time_partition_interval=timedelta(days = 7),)`

### Efficient similarity search with time filters

Now that we’ve loaded our vector data and metadata into a Timescale Vector vector store, and enabled automatic time-based partitioning on the table our vectors and metadata are stored in, we can query our vector store with time-based filters as follows:

`start_dt = datetime(2023, 8, 1, 22, 10, 35)
end_dt = datetime(2023, 8, 30, 22, 10, 35)
query = &quot;What&#x27;s new with TimescaleDB functions?&quot;docs_with_score = db.similarity_search_with_score(query, start_date=start_dt, end_date=end_dt)--------------------------------------------------------------------------------
Score:  0.17487859725952148
Date:  Tue Aug 29 18:13:24 2023 +0200
{&quot;commit&quot;: &quot; e4facda540286b0affba47ccc63959fefe2a7b26&quot;, &quot;author&quot;: &quot;Sven Klemm&lt;sven@timescale.com&gt;&quot;, &quot;date&quot;: &quot;Tue Aug 29 18:13:24 2023 +0200&quot;, &quot;change summary&quot;: &quot;Add compatibility layer for _timescaledb_internal functions&quot;, &quot;change details&quot;: &quot;With timescaledb 2.12 ...&quot;}
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Score:  0.17487859725952148
Date:  Tue Aug 29 18:13:24 2023 +0200
{&quot;commit&quot;: &quot; e4facda540286b0affba47ccc63959fefe2a7b26&quot;, &quot;author&quot;: &quot;Sven Klemm&lt;sven@timescale.com&gt;&quot;, &quot;date&quot;: &quot;Tue Aug 29 18:13:24 2023 +0200&quot;, &quot;change summary&quot;: &quot;Add compatibility layer for _timescaledb_internal functions&quot;, &quot;change details&quot;: &quot;With timescaledb 2.12 all the functions... &quot;}
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Score:  0.18100780248641968
Date:  Sun Aug 20 22:47:10 2023 +0200
{&quot;commit&quot;: &quot; 0a66bdb8d36a1879246bd652e4c28500c4b951ab&quot;, &quot;author&quot;: &quot;Sven Klemm&lt;sven@timescale.com&gt;&quot;, &quot;date&quot;: &quot;Sun Aug 20 22:47:10 2023 +0200&quot;, &quot;change summary&quot;: &quot;Move functions to _timescaledb_functions schema&quot;, &quot;change details&quot;: &quot;To increase schema security we do ...&quot;}
--------------------------------------------------------------------------------`

Success! Notice how only vectors with timestamps within the specified start and end date ranges of 1 August 2023 and 30 August 2023 are included in the results.

We can also specify a time filter with a provided start date and time delta later:

`start_dt = datetime(2023, 8, 1, 22, 10, 35)
td = timedelta(days=7)
query = &quot;What&#x27;s new with TimescaleDB functions?&quot;

docs_with_score = db.similarity_search_with_score(query, start_date=start_dt, time_delta=td)
`

And specify a time filter within a provided end_date and time delta earlier:

`end_dt = datetime(2023, 8, 30, 22, 10, 35)
td = timedelta(days=7)
query = &quot;What&#x27;s new with TimescaleDB functions?&quot;

docs_with_score = db.similarity_search_with_score(query, end_date=end_dt, time_delta=td)

`

### What’s happening behind the scenes

Here’s some intuition for why Timescale Vector’s time-based partitioning speeds up ANN queries with time-based filters:

Timescale Vector partitions the data by time and creates ANN indexes on each partition individually. Then, during search, we perform a three-step process:

- Step 1: filter our partitions that don’t match the time predicate.
- Step 2: perform the similarity search on all matching partitions.
- Step 3: combine all the results from each partition in step 2, rerank, and filter out results by time.

Timescale Vector leverages [TimescaleDB’s hypertables](https://docs.timescale.com/use-timescale/latest/hypertables/?ref=blog.langchain.com), which automatically partition vectors and associated metadata by a timestamp. This enables efficient querying on vectors by both similarity to a query vector and time, as partitions not in the time window of the query are ignored, making the search a lot more efficient by filtering out whole swaths of data in one go.

# Powering Retrieval Augmented Generation With Time-Based Context Retrieval in LangChain Applications with Timescale Vector

Let’s put everything together and look at how to use the Timescale Vector to power Retrieval Augmented Generation (RAG) on the git log dataset we examined above.

Timescale Vector helps with time-based context retrieval, where we want to find the most relevant vectors within a specified time range to use as context for answering a user query. Let&#x27;s take a look at an example below, using Timescale Vector as a retriever.

First we create a retriever from the TimescaleVector store.

`# Set timescale vector as a retriever and specify start and end dates via kwargs
retriever = db.as_retriever(search_kwargs={&quot;start_date&quot;: start_dt, &quot;end_date&quot;: end_dt})

`

When creating the retriever, we can constrain the search to a relevant time range by passing our time filter parameters for Timescale Vector as `search_kwargs`.

Then we’ll create a [RetrievalQA chain](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa?ref=blog.langchain.com) from a [Stuff chain](https://python.langchain.com/docs/modules/chains/document/stuff?ref=blog.langchain.com), by passing our retriever and the LLM we want to use to generate a response:

`from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature = 0.1, model = &#x27;gpt-3.5-turbo-16k&#x27;)

from langchain.chains import RetrievalQA
qa_stuff = RetrievalQA.from_chain_type(
   llm=llm,
   chain_type=&quot;stuff&quot;,
   retriever=retriever,
   verbose=True,
)`

Then we can query the RetrievalQA chain and it will use the retriever backed by Timescale Vector to answer your the query with the most relevant documents within the time ranged specified:

`
query = &quot;What&#x27;s new with the timescaledb functions? Tell me when these changes were made.&quot;
response = qa_stuff.run(query)
print(response)`

**&gt; Entering new RetrievalQA chain...**

**&gt; Finished chain.**

> The following changes were made to the timescaledb functions:

> 1. &quot;Add compatibility layer for _timescaledb_internal functions&quot; - This change was made on Tue Aug 29 18:13:24 2023 +0200.

> 2. &quot;Move functions to _timescaledb_functions schema&quot; - This change was made on Sun Aug 20 22:47:10 2023 +0200.

> 3. &quot;Move utility functions to _timescaledb_functions schema&quot; - This change was made on Tue Aug 22 12:01:19 2023 +0200.

> 4. &quot;Move partitioning functions to _timescaledb_functions schema&quot; - This change was made on Tue Aug 29 10:49:47 2023 +0200.

Success! Note that the context the LLM uses to compose an answer are from retrieved documents only within the specified date range.

This is a simple example of a powerful concept – using time-based context retrieval in your RAG applications can help provide more relevant answers to your users. This time-based context retrieval can be helpful to any dataset with a natural language and time component. Timescale Vector uniquely enables this thanks to its efficient time-based similarity search capabilities and taking advantage of it in your LangChain applications is easy thanks to the Timescale Vector integration.

# Advanced LangChain Self-Querying Capabilities With Timescale Vector

Timescale Vector also supports one of LangChain’s coolest features: the [Self-Querying retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/self_query/?ref=blog.langchain.com).

Here’s how it works: We create a retriever from the Timescale Vector vector store and feed it a natural language query with a query statement and filters (single or composite). The retriever then uses a query constructing LLM chain to write a SQL query and applies it to the underlying PostgreSQL database in the Timescale Vector vector store.

With Timescale Vector, you can ask queries with limit, metadata, and time-based filters using the self-query retriever. Let’s take a look at an example of using self-querying on a git log dataset.

First, we instantiate our TimescaleVector vector store:

`COLLECTION_NAME = &quot;timescale_commits&quot;
vectorstore = TimescaleVector(
   embedding_function=OpenAIEmbeddings(),
   collection_name=COLLECTION_NAME,
   service_url=SERVICE_URL,
)`

Second, let’s create the self-query retriever from an LLM, passing the following parameters to it:

- `llm`: the LLM we want our self-query retriever to use to construct the queries.
- `vectorstore`: our TimescaleVector vectorstore, instantiated above.
- `document_content_description`: a description of the content associated with our vector embeddings. In this case, it is information about the git log entries.
- `metadata_field_info`: a list of AttributeInfo objects, which give the LLM information about the metadata fields in our collection of vectors.
- `enable_limit`: setting this to ‘true’ enables us to ask questions with an implied limit, which helps constrain the number of results returned.

`from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

# Give LLM info about the metadata fields
metadata_field_info = [
   AttributeInfo(
       name=&quot;id&quot;,
       description=&quot;A UUID v1 generated from the date of the commit&quot;,
       type=&quot;uuid&quot;,
   ),
   AttributeInfo(
       name=&quot;date&quot;,
       description=&quot;The date of the commit in timestamptz format&quot;,
       type=&quot;timestamptz&quot;,
   ),
   AttributeInfo(
       name=&quot;author_name&quot;,
       description=&quot;The name of the author of the commit&quot;,
       type=&quot;string&quot;,
   ),
   AttributeInfo(
       name=&quot;author_email&quot;,
       description=&quot;The email address of the author of the commit&quot;,
       type=&quot;string&quot;,
   )
]
document_content_description = &quot;The git log commit summary containing the commit hash, author, date of commit, change summary and change details&quot;

# Instantiate the self-query retriever from an LLM
llm = OpenAI(temperature=0)
retriever = SelfQueryRetriever.from_llm(
   llm, vectorstore, document_content_description, metadata_field_info, enable_limit=True, verbose=True
)`

Now for the fun part, let’s query our self-query retriever.

### Self-querying example: Query and metadata filter

Here’s an example of a simple metadata filter specified in natural language. In this case, we’re asking for commits added by a specific person:

`retriever.get_relevant_documents(&quot;What commits about timescaledb_functions did Sven Klemm add?&quot;)

`

Here’s the verbose output of the LLM chain, showing what query parameters the natural language query got translated into:

`query=&#x27;timescaledb_functions&#x27; filter=Comparison(comparator=&lt;Comparator.EQ: &#x27;eq&#x27;&gt;, attribute=&#x27;author_name&#x27;, value=&#x27;Sven Klemm&#x27;) limit=None

`

### Self-querying example:: Time-based filter

Here’s an example of a question that uses a time-based filter. The query to fetch the results to answer this question will take advantage of Timescale Vector’s efficient time-based partitioning.

`# This example specifies a time-based filter
retriever.get_relevant_documents(&quot;What commits were added in July 2023?&quot;)

`

Here’s the verbose explanation from LangChain’s self-query retriever about the SQL query parameters that the natural language query gets translated into:

`query=&#x27; &#x27; filter=Operation(operator=&lt;Operator.AND: &#x27;and&#x27;&gt;, arguments=[Comparison(comparator=&lt;Comparator.GTE: &#x27;gte&#x27;&gt;, attribute=&#x27;date&#x27;, value=&#x27;2023-07-01T00:00:00Z&#x27;), Comparison(comparator=&lt;Comparator.LTE: &#x27;lte&#x27;&gt;, attribute=&#x27;date&#x27;, value=&#x27;2023-07-31T23:59:59Z&#x27;)]) limit=None`

And here’s a snippet of the results:

`[Document(page_content=&#x27;{&quot;commit&quot;: &quot; 5cf354e2469ee7e43248bed382a4b49fc7ccfecd&quot;, &quot;author&quot;: &quot;Markus Engel&lt;engel@sero-systems.de&gt;&quot;, &quot;date&quot;: &quot;Mon Jul 31 11:28:25 2023 +0200&quot;,...

Document(page_content=&#x27;{&quot;commit&quot;: &quot; 88aaf23ae37fe7f47252b87325eb570aa417c607&quot;, &quot;author&quot;: &quot;noctarius aka Christoph Engelbert&lt;me@noctarius.com&gt;&quot;, &quot;date&quot;: &quot;Wed Jul 12 14:53:40 2023 +0200&quot;, . . .

Document(page_content=&#x27;{&quot;commit&quot;: &quot; d5268c36fbd23fa2a93c0371998286e8688247bb&quot;, &quot;author&quot;: &quot;Alexander Kuzmenkov&lt;36882414+akuzm@users.noreply.github.com&gt;&quot;, &quot;date&quot;: &quot;Fri Jul 28 13:35:05 2023 +0200&quot;,...`

Note how you can specify a query, filter, and composite filter (filters with AND, OR) in natural language and the self-query retriever will translate that query into SQL and perform the search on the Timescale Vector (PostgreSQL) vector store.

This illustrates the power of the self-query retriever. You can use it to perform complex searches over your vector store without you or your users having to write any SQL directly.

What’s more, you can combine the self-query retriever with the LangChain [RetrievalQA chain](https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa?ref=blog.langchain.com) to power an RAG application!

## Resources and next steps

Now that you’ve learned how Timescale Vector can help you power AI applications with PostgreSQL, it’s your turn to dive in. Take the next step in your learning journey by following one of the tutorials or reading one of the blog posts in the following resources set:

- [**Up and Running Tutorial**](https://python.langchain.com/docs/integrations/vectorstores/timescalevector?ref=blog.langchain.com)**: **learn how to use Timescale Vector as a LangChain vector store and perform time-based similarity search on vectors.
- [**Self-query retriever tutorial:**](https://python.langchain.com/docs/modules/data_connection/retrievers/self_query/timescalevector_self_query?ref=blog.langchain.com)** **learn how to use Timescale Vector as a self-query retriever.
- [**Timescale Vector explainer**](https://www.timescale.com/blog/how-we-made-postgresql-the-best-vector-database/?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral): learn more about the internals of Timescale Vector
- [**Timescale Vector website**](https://www.timescale.com/ai?ref=blog.langchain.com)**: learn more about Timescale Vector and Timescale’s AI Launch Week.**

**🎉 And a reminder:**[** LangChain Users get Timescale Vector free for 3 Months**](https://console.cloud.timescale.com/signup?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral)

Timescale is giving LangChain users an extended 90-day trial of Timescale Vector. This makes it easy to test and develop your applications with Timescale Vector, as you won’t be charged for any cloud PostgreSQL databases you spin up during your trial period. [Try Timescale Vector for free today](https://console.cloud.timescale.com/signup?utm_campaign=vectorlaunch&amp;utm_source=langchain&amp;utm_medium=referral).

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