---
title: "Semantic Search for LangGraph Memory"
author: "LangChain Accounts"
date: "2024-12-05"
url: "https://www.langchain.com/blog/semantic-search-for-langgraph-memory"
---

LangGraph

# Semantic Search for LangGraph Memory

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaDecember 5, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae363fe3e9a95a53b022_semsearch-1.png)Following our [launch of long-term memory support](https://blog.langchain.com/launching-long-term-memory-support-in-langgraph/), we&#x27;re adding semantic search to LangGraph&#x27;s BaseStore. Available today in the open source `PostgresStore` and `InMemoryStore`&#x27;s, in LangGraph studio, as well as in production in all LangGraph Platform deployments.

**Quick Links:**

- [Video tutorial](https://youtu.be/HfJ4h380J_U?ref=blog.langchain.com) on adding semantic search to the memory agent template
- [How to guide](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/?ref=blog.langchain.com) on adding semantic search in LangGraph
- [How to guide ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/?ref=blog.langchain.com)on adding semantic search in your LangGraph Platform deployment

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae373fe3e9a95a53b028_image-3.png)

## Why semantic search?

While our base memory implementation provides document storage and filtering, many users requested primitives for more sophisticated retrieval of unstructured information. Simple filtering works when you keep things well-organized, but agents often need to find relevant information based on meaning, not just exact matches.

For example, an agent might need to:

- Recall user preferences and past interactions for personalized responses
- Learn from past mistakes by retrieving similar failed approaches
- Maintain consistent knowledge by recalling important facts learned in previous interactions

Semantic search addresses these challenges by matching on meaning rather than exact content, making agents more effective at using their stored knowledge.

## Implementation

The `BaseStore` &#x27;s  `search`  (and asynchronous `asearch` ) methods now support a natural language `query` term. If the store you are using has added support, documents will be scored and returned based on semantic similarity. Support has been added to both the `InMemoryStore` for development and `PostgresStore` for production. An example usage is below:

`def search_memory(state: State, *, store: BaseStore):
    results = store.search(
        (&quot;user_123&quot;, &quot;interactions&quot;),
        query=state[&quot;messages&quot;][-1].content,
        filter={&quot;type&quot;: &quot;conversation&quot;},
        limit=3
    )
    return {
        &quot;context&quot;: [
            f&quot;Previous interaction ({r.score:.2f} relevance):\n{r.value}&quot;
            for r in results
        ]
    }
Example search node to lookup relevant memories.`

Example node querying for related content

To use in the LangGraph Platform, you can configure your server to embed new items through a `store` configuration in your `langgraph.json` file:

`{
  &quot;store&quot;: {
    &quot;index&quot;: {
      &quot;embed&quot;: &quot;openai:text-embeddings-3-small&quot;,
      &quot;dims&quot;: 1536,
      &quot;fields&quot;: [&quot;text&quot;, &quot;summary&quot;]
    }
  }
}
`

The main configuration options:

- `embed`: Embedding provider (e.g., &quot;openai:text-embedding-3-small&quot;) or path to custom function ([doc](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/?ref=blog.langchain.com#custom-embeddings)).  `provider:model` support depends on LangChain to use.
- `dims`: Dimension size of the chosen embedding model (1536 for OpenAI&#x27;s text-embedding-3-small)
- `fields`: List of fields to index. Use `[&quot;$&quot;]` to index entire documents, or specify json paths like `[&quot;text&quot;, &quot;summary&quot;, &quot;messages[-1]&quot;]`

If you&#x27;re not a LangChain user, or if you want to define custom embedding logic, define your own function:

`async def aembed_texts(texts: list[str]) -&gt; list[list[float]]:
    response = await client.embeddings.create(
        model=&quot;text-embedding-3-small&quot;,
        input=texts
    )
    return [e.embedding for e in response.data]
`

Then reference your function in the config:

`{
  &quot;store&quot;: {
    &quot;index&quot;: {
      &quot;embed&quot;: &quot;path/to/embedding_function.py:embed_texts&quot;,
      &quot;dims&quot;: 1536
    }
  }
}
`

If you want to customize which fields to embed for a given item, or if you want to omit an item from being indexed, pass the `index` arg to `store.put`

`# embed the configured default &quot;text&quot; field &quot;Python tutorial&quot;
store.put((&quot;docs&quot;,), &quot;doc1&quot;, {&quot;text&quot;: &quot;Python tutorial&quot;})
# Override default field to embed &quot;other_field&quot; instead
store.put(
    (&quot;docs&quot;,),
    &quot;doc2&quot;,
    {&quot;text&quot;: &quot;TypeScript guide&quot;, &quot;other_field&quot;: &quot;value&quot;},
    index=[&quot;other_field&quot;],
)
# Do not embed this item
store.put((&quot;docs&quot;,), &quot;doc2&quot;, {&quot;text&quot;: &quot;Other guide&quot;}, index=False)`

See the [docs](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/?ref=blog.langchain.com#custom-embeddings) for more information.

## Migration

If you&#x27;re already using LangGraph&#x27;s memory store, adding semantic search is non-breaking. All operations work the same as before. LangGraph OSS users can start using by constructing their `PostGresStore` with an index configuration ([sync](https://langchain-ai.github.io/langgraph/reference/store/?ref=blog.langchain.com#langgraph.store.postgres.PostgresStore) &amp; [async](https://langchain-ai.github.io/langgraph/reference/store/?ref=blog.langchain.com#langgraph.store.postgres.AsyncPostgresStore) docs):

`from langchain.embeddings import init_embeddings
from langgraph.store.postgres import PostgresStore

store = PostgresStore(
    connection_string=&quot;postgresql://user:pass@localhost:5432/dbname&quot;,
    index={
        &quot;dims&quot;: 1536,
        &quot;embed&quot;: init_embeddings(&quot;openai:text-embedding-3-small&quot;),
        # specify which fields to embed. Default is the whole serialized value
        &quot;fields&quot;: [&quot;text&quot;],
    },
)
store.setup()  # Do this once to run migrations
`

For LangGraph platform users, once you add an `index` configuration to your deployment, new documents that are `put` into the store can be indexed for search, and you can add a natural language `query` string to return documents sorted by semantic similarity.

## Next Steps

We&#x27;ve updated our documentation &amp; templates to demonstrate semantic search in action. Check them out at the links below:

- [Memory Template](https://github.com/langchain-ai/memory-template?ref=blog.langchain.com) uses search over memories saved &quot;in the background&quot;
- [Memory Agent](https://github.com/langchain-ai/memory-agent?ref=blog.langchain.com) searches over memories saved as a tool
- [Video tutorial ](https://youtu.be/HfJ4h380J_U?ref=blog.langchain.com)on adding semantic search to the memory agent template
- [How to guide ](https://langchain-ai.github.io/langgraph/how-tos/memory/semantic-search/?ref=blog.langchain.com)on adding semantic search in LangGraph
- [How to guide ](https://langchain-ai.github.io/langgraph/cloud/deployment/semantic_search/?ref=blog.langchain.com)on adding semantic search in your LangGraph Platform deployment
- [Reference docs](https://langchain-ai.github.io/langgraph/reference/store/?ref=blog.langchain.com#langgraph.store.base.BaseStore.search) on the BaseStore

Try it out and share your feedback on [GitHub](https://github.com/langchain-ai/langgraph/discussions?ref=blog.langchain.com).

And finally, for more conceptual information on AI memory, check out our  [memory conceptual documentation](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa18703c727fd28ab4de_Vodafone-Italy---Oct-2025--1-.png)Case StudiesLangGraphLangSmith

#### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/customers-vodafone-italy)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)