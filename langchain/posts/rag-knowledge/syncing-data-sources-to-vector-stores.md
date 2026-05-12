---
title: "Syncing data sources to vector stores"
author: "LangChain Accounts"
date: "2023-09-06"
url: "https://www.langchain.com/blog/syncing-data-sources-to-vector-stores"
---

Observability &amp; Evals

# Syncing data sources to vector stores

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 6, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)Most complex and knowledge-intensive LLM applications require runtime data retrieval for Retrieval Augmented Generation (RAG). A core component of the typical RAG stack is a vector store, which is used to power document retrieval.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1720463468b9830af32_data_connection-c42d68c3d092b85f50d08d4cc171fc25.jpeg)

Using a vector store requires setting up an indexing pipeline to load data from sources (a website, a file, etc.), transform the data into documents, embed those documents, and insert the embeddings and documents into the vector store.

If your data sources or processing steps change, the data needs to be re-indexed. If this happens regularly, and the changes are incremental, it becomes valuable to de-duplicate the content being indexed with the content already in the vector store. This avoids spending time and money on redundant work. It also becomes important to set up vector store cleanup processes to remove stale data from your vector store.

## LangChain Indexing API

The new LangChain Indexing API makes it easy to load and keep in sync documents from any source into a vector store. Specifically, it helps:

- Avoid writing duplicated content into the vector store
- Avoid re-writing unchanged content
- Avoid re-computing embeddings over unchanged content

Crucially, the indexing API will work even with documents that have gone through several transformation steps (e.g., via text chunking) with respect to the original source documents.

## How it works

LangChain indexing makes use of a record manager (`RecordManager`) that keeps track of document writes into a vector store.

When indexing content, hashes are computed for each document, and the following information is stored in the record manager:

- the document hash (hash of both page content and metadata)
- write time
- the source id -- each document should include information in its metadata to allow us to determine the ultimate source of this document

### Cleanup modes

When re-indexing documents into a vector store, it&#x27;s possible that some existing documents in the vector store should be deleted. If you’ve made changes to how documents are processed before insertion or source documents have changed, you’ll want to remove any existing documents that come from the same source as the new documents being indexed. If some source documents have been deleted, you’ll want to delete all existing documents in the vector store and replace them with the re-indexed documents.

The indexing API cleanup modes let you pick the behavior you want:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1720463468b9830af37_Screenshot-2023-09-06-at-8.36.55-AM.png)

For more detailed documentation of the API and its limitations, check out the docs: [https://python.langchain.com/docs/modules/data_connection/indexing](https://python.langchain.com/docs/modules/data_connection/indexing?ref=blog.langchain.com)

## Seeing it in action

First let’s initialize our vector store. We’ll demo with the `ElasticsearchStore`, since it satisfies the pre-requisites of supporting insertion and deletion. See the [Requirements](https://python.langchain.com/docs/modules/data_connection/indexing?ref=blog.langchain.com#requirements) docs section for more on vector store requirements.

`# !pip install openai elasticsearch

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import ElasticsearchStore

collection_name = &quot;test_index&quot;

# Set env var OPENAI_API_KEY
embedding = OpenAIEmbeddings()

# Run an Elasticsearch instance locally:
# !docker run -p 9200:9200 -e &quot;discovery.type=single-node&quot; -e &quot;xpack.security.enabled=false&quot; -e &quot;xpack.security.http.ssl.enabled=false&quot; docker.elastic.co/elasticsearch/elasticsearch:8.9.0
vector_store = ElasticsearchStore(
    collection_name,
    es_url=&quot;&lt;http://localhost:9200&gt;&quot;,
    embedding=embedding
)
`

And now we’ll initialize and create a schema for our record manager, for which we’ll just use a SQLite table:

`from langchain.indexes import SQLRecordManager

namespace = f&quot;elasticsearch/{collection_name}&quot;
record_manager = SQLRecordManager(
    namespace, db_url=&quot;sqlite:///record_manager_cache.sql&quot;
)
record_manager.create_schema()
`

Suppose we want to index the [reuters.com](http://reuters.com/?ref=blog.langchain.com) front page. We can load and split the url contents with:

`# !pip install beautifulsoup4 tiktoken

import bs4

from langchain.document_loaders import RecursiveUrlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

raw_docs = RecursiveUrlLoader(
    &quot;&lt;https://www.reuters.com&gt;&quot;,
    max_depth=0,
    extractor=lambda x: BeautifulSoup(x, &quot;lxml&quot;).text
).load()
processed_docs = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=200
).split_documents(raw_docs)
`

And now we’re ready to index! Suppose when we first index only the first 10 documents are on the front page:

`from langchain.indexes import index

index(
    processed_docs[:10],
    record_manager,
    vector_store,
    cleanup=&quot;full&quot;,
    source_id_key=&quot;source&quot;
)
{&#x27;num_added&#x27;: 10, &#x27;num_updated&#x27;: 0, &#x27;num_skipped&#x27;: 0, &#x27;num_deleted&#x27;: 0}
`

And if we index an hour later, maybe 2 of the documents have changed:

`index(
    process_docs[2:10] + processed_docs[-2:],
    record_manager,
    vector_store,
    cleanup=&quot;full&quot;,
    source_id_key=&quot;source&quot;,
)
{&#x27;num_added&#x27;: 2, &#x27;num_updated&#x27;: 0, &#x27;num_skipped&#x27;: 8, &#x27;num_deleted&#x27;: 2}
`

Looking at the output, we can see that while 10 documents were indexed the actual work we did was 2 additions and 2 deletions — we added the new documents, removed the old ones and skipped all the duplicate ones.

For more in-depth examples, head to: [https://python.langchain.com/docs/modules/data_connection/indexing](https://python.langchain.com/docs/modules/data_connection/indexing?ref=blog.langchain.com)

## ChatLangChain + Indexing API

We’ve recently revamped the [https://github.com/langchain-ai/chat-langchain](https://github.com/langchain-ai/chat-langchain?ref=blog.langchain.com) chatbot for questions about LangChain. As part of the revamp, we revived the hosted version [https://chat.langchain.com](https://chat.langchain.com/?ref=blog.langchain.com) and set up a daily indexing job using the new API to make sure the chatbot is up to date with the latest LangChain developments.

Doing this was very straightforward — all we had to do was:

- Set up a Supabase Postgres database to be used as a record manager,
- Update our ingestion script to use the indexing API instead of inserting documents to the vector store directly,
- Set up a scheduled Github Action to run the ingestion script daily. You can check out the GHA workflow [here](https://github.com/langchain-ai/chat-langchain/blob/master/.github/workflows/index.yml?ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1720463468b9830af3a_langchain-overview-5.png)

## Conclusion

As you move your apps from prototype to production, be able to re-indexing efficiently and keep documents in your vector in sync with their source becomes very important. LangChain&#x27;s new indexing API provides a clean and scalable way to do this.

Try it out and let us know what you think!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8a01c18c14b60cd4372_76.webp)LangSmithObservability &amp; Evals

#### Human judgment in the agent improvement loop

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2d3bf32d4fc06a289383_rahul-verma.png)Rahul VermaApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/human-judgment-in-the-agent-improvement-loop)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce9138b145f1419b6b38b_74--2-.webp)Observability &amp; Evals

#### Better Harness: A Recipe for Harness Hill-Climbing with Evals

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyApril 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)