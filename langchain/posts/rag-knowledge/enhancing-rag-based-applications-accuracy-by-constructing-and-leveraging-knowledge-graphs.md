---
title: "Enhancing RAG-based application accuracy by constructing and leveraging knowledge graphs"
author: "LangChain Accounts"
date: "2024-03-15"
url: "https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs"
---

Company AnnouncementsLangSmith

# Enhancing RAG-based application accuracy by constructing and leveraging knowledge graphs

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 15, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb003394beb6952654243_ragbased.webp)

### A practical guide to constructing and retrieving information from knowledge graphs in RAG applications with Neo4j and LangChain

*Editor&#x27;s Note: the following is a guest blog post from Tomaz Bratanic, who focuses on Graph ML and GenAI research at *[*Neo4j*](https://neo4j.com/?utm_source=Google&amp;utm_medium=PaidSearch&amp;utm_campaign=Evergreenutm_content%3DAMS-Search-SEMBrand-Evergreen-None-SEM-SEM-NonABM&amp;utm_term=neo4j&amp;utm_adgroup=core-brand&amp;gad_source=1&amp;gclid=CjwKCAjw48-vBhBbEiwAzqrZVOnH2D4WOkRLH78FtQAFitObkbJNs34kTFw4bbBX0VzwqSalQUV2UhoCrFcQAvD_BwE)*.* *Neo4j is a graph database and analytics company which helps organizations find hidden relationships and patterns across billions of data connections deeply, easily, and quickly.*

Graph retrieval augmented generation ([Graph RAG](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/?ref=blog.langchain.com)) is gaining momentum and emerging as a powerful addition to traditional vector search retrieval methods. This approach leverages the structured nature of graph databases, which organize data as nodes and relationships, to enhance the depth and contextuality of retrieved information.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb004394beb695265425e_0*rm_fRSPovV1wfTqH.jpeg)Example knowledge graph.

Graphs are great at representing and storing heterogeneous and interconnected information in a structured manner, effortlessly capturing complex relationships and attributes across diverse data types. In contrast, vector databases often struggle with such structured information, as their strength lies in handling unstructured data through high-dimensional vectors. In your RAG application, you can combine structured graph data with vector search through unstructured text to achieve the best of both worlds, which is exactly what we will do in this blog post.

**Knowledge graphs are great, but how do you create one?** Constructing a knowledge graph is typically the most challenging step in leveraging the power of graph-based data representation. It involves gathering and structuring the data, which requires a deep understanding of both the domain and graph modeling. To simplify this process, we have been experimenting with LLMs. LLMs, with their profound understanding of language and context, can automate significant parts of the knowledge graph creation process. By analyzing text data, these models can identify entities, understand the relationships between them, and suggest how they might be best represented in a graph structure. As a result of these experiments, we have added the first version of the graph construction module to LangChain, which we will demonstrate in this blog post.

The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/enhancing_rag_with_graph.ipynb?ref=blog.langchain.com).

### Neo4j Environment Setup

You need to set up a Neo4j instance follow along with the examples in this blog post. The easiest way is to start a free instance on [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/?ref=blog.langchain.com), which offers cloud instances of Neo4j database. Alternatively, you can also set up a local instance of the Neo4j database by downloading the [Neo4j Desktop](https://neo4j.com/download/?ref=blog.langchain.com) application and creating a local database instance.

`os.environ[&quot;OPENAI_API_KEY&quot;] = &quot;sk-&quot;
os.environ[&quot;NEO4J_URI&quot;] = &quot;bolt://localhost:7687&quot;
os.environ[&quot;NEO4J_USERNAME&quot;] = &quot;neo4j&quot;
os.environ[&quot;NEO4J_PASSWORD&quot;] = &quot;password&quot;

graph = Neo4jGraph()`

Additionally, you must provide an [OpenAI key](https://openai.com/?ref=blog.langchain.com), as we will use their models in this blog post.

## Data ingestion

For this demonstration, we will use [Elizabeth I’s](https://en.wikipedia.org/wiki/Elizabeth_I?ref=blog.langchain.com) Wikipedia page. We can utilize [LangChain loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com) to fetch and split the documents from Wikipedia seamlessly.

`# Read the wikipedia article
raw_documents = WikipediaLoader(query=&quot;Elizabeth I&quot;).load()

# Define chunking strategy
text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=24)
documents = text_splitter.split_documents(raw_documents[:3])`

Now it’s time to construct a graph based on the retrieved documents. For this purpose, we have implemented an `LLMGraphTransformer`module that significantly simplifies constructing and storing a knowledge graph in a graph database.

`llm=ChatOpenAI(temperature=0, model_name=&quot;gpt-4-0125-preview&quot;)
llm_transformer = LLMGraphTransformer(llm=llm)

# Extract graph data
graph_documents = llm_transformer.convert_to_graph_documents(documents)

# Store to neo4j
graph.add_graph_documents(
  graph_documents,
  baseEntityLabel=True,
  include_source=True
)`

You can define which LLM you want the knowledge graph generation chain to use. At the moment, we support only function calling models from OpenAI and Mistral. However, we plan to expand the LLM selection in the future. In this example, we are using the latest GPT-4. Note that the quality of generated graph significantly depends on the model you are using. In theory, you always want to use the most capable one. The LLM graph transformers returns graph documents, which can be imported to Neo4j via the `add_graph_documents` method. The `baseEntityLabel` parameter assigns an additional `__Entity__` label to each node, enhancing indexing and query performance. The `include_source` parameter links nodes to their originating documents, facilitating data traceability and context understanding.

You can inspect the generated graph in Neo4j Browser.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb004394beb6952654262_1*ptr_F720ZRdxbA8ee-NvjQ.png)Part of the generated graph.

Note that this image represents only a part of the generated graph for clarity.

## Hybrid Retrieval for RAG

After the graph generation, we will use a hybrid retrieval approach that combines vector and keyword indexes with graph retrieval for RAG applications.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb004394beb6952654258_1*TJJBOZN9auUioEnqQo-Qdw.png)Combining hybrid (vector + keyword) and graph retrieval methods. Image by author.

The diagram illustrates a retrieval process beginning with a user posing a question, which is then directed to an RAG retriever. This retriever employs keyword and vector searches to search through unstructured text data and combines it with the information it collects from the knowledge graph. Since Neo4j features both keyword and vector indexes, you can implement all three retrieval options with a single database system. The collected data from these sources is fed into an LLM to generate and deliver the final answer.

### Unstructured data retriever

You can use the `Neo4jVector.from_existing_graph` method to add both keyword and vector retrieval to documents. This method configures keyword and vector search indexes for a hybrid search approach, targeting nodes labeled `Document`. Additionally, it calculates text embedding values if they are missing.

`vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(),
    search_type=&quot;hybrid&quot;,
    node_label=&quot;Document&quot;,
    text_node_properties=[&quot;text&quot;],
    embedding_node_property=&quot;embedding&quot;
)`

The vector index can then be called with the `similarity_search` method.

### Graph retriever

On the other hand, configuring a graph retrieval is more involved but offers more freedom. In this example, we will use a full-text index to identify relevant nodes and then return their direct neighborhood.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb004394beb695265425b_1*z0pYA_dSNG_yTYE6Rr7CQA.png)Graph retriever. Image by author.

The graph retriever starts by identifying relevant entities in the input. For simplicity, we instruct the LLM to identify people, organizations, and locations. To achieve this, we will use LCEL with the newly added `with_structured_output` method to achieve this.

`# Extract entities from text
class Entities(BaseModel):
    &quot;&quot;&quot;Identifying information about entities.&quot;&quot;&quot;

    names: List[str] = Field(
        ...,
        description=&quot;All the person, organization, or business entities
        that &quot; &quot;appear in the text&quot;,
    )

prompt = ChatPromptTemplate.from_messages(
    [
        (
            &quot;system&quot;,
            &quot;You are extracting organization and person entities from the
            text.&quot;,
        ),
        (
            &quot;human&quot;,
            &quot;Use the given format to extract information from the
             following&quot;
            &quot;input: {question}&quot;,
        ),
    ]
)

entity_chain = prompt | llm.with_structured_output(Entities)`

Let’s test it out:

`entity_chain.invoke({&quot;question&quot;: &quot;Where was Amelia Earhart born?&quot;}).names
# [&#x27;Amelia Earhart&#x27;]`

Great, now that we can detect entities in the question, let’s use a full-text index to map them to the knowledge graph. First, we need to define a full-text index and a function that will generate full-text queries that allow a bit of misspelling, which we won’t go into much detail here.

`graph.query(
    &quot;CREATE FULLTEXT INDEX entity IF NOT EXISTS FOR (e:__Entity__) ON EACH [e.id]&quot;)

def generate_full_text_query(input: str) -&gt; str:
    &quot;&quot;&quot;
    Generate a full-text search query for a given input string.

    This function constructs a query string suitable for a full-text
    search. It processes the input string by splitting it into words and
    appending a similarity threshold (~2 changed characters) to each
    word, then combines them using the AND operator. Useful for mapping
    entities from user questions to database values, and allows for some
    misspelings.
    &quot;&quot;&quot;
    full_text_query = &quot;&quot;
    words = [el for el in remove_lucene_chars(input).split() if el]
    for word in words[:-1]:
        full_text_query += f&quot; {word}~2 AND&quot;
    full_text_query += f&quot; {words[-1]}~2&quot;
    return full_text_query.strip()`

Let’s put it all together now.

`# Fulltext index query
def structured_retriever(question: str) -&gt; str:
    &quot;&quot;&quot;
    Collects the neighborhood of entities mentioned
    in the question
    &quot;&quot;&quot;
    result = &quot;&quot;
    entities = entity_chain.invoke({&quot;question&quot;: question})
    for entity in entities.names:
        response = graph.query(
            &quot;&quot;&quot;CALL db.index.fulltext.queryNodes(&#x27;entity&#x27;, $query,
            {limit:2})
            YIELD node,score
            CALL {
              MATCH (node)-[r:!MENTIONS]-&gt;(neighbor)
              RETURN node.id + &#x27; - &#x27; + type(r) + &#x27; -&gt; &#x27; + neighbor.id AS
              output
              UNION
              MATCH (node)&lt;-[r:!MENTIONS]-(neighbor)
              RETURN neighbor.id + &#x27; - &#x27; + type(r) + &#x27; -&gt; &#x27; +  node.id AS
              output
            }
            RETURN output LIMIT 50
            &quot;&quot;&quot;,
            {&quot;query&quot;: generate_full_text_query(entity)},
        )
        result += &quot;\n&quot;.join([el[&#x27;output&#x27;] for el in response])
    return result`

The `structured_retriever` function starts by detecting entities in the user question. Next, it iterates over the detected entities and uses a Cypher template to retrieve the neighborhood of relevant nodes. Let’s test it out!

`print(structured_retriever(&quot;Who is Elizabeth I?&quot;))
# Elizabeth I - BORN_ON -&gt; 7 September 1533
# Elizabeth I - DIED_ON -&gt; 24 March 1603
# Elizabeth I - TITLE_HELD_FROM -&gt; Queen Of England And Ireland
# Elizabeth I - TITLE_HELD_UNTIL -&gt; 17 November 1558
# Elizabeth I - MEMBER_OF -&gt; House Of Tudor
# Elizabeth I - CHILD_OF -&gt; Henry Viii
# and more...`

### Final retriever

As we mentioned at the start, we’ll combine the unstructured and graph retriever to create the final context that will be passed to an LLM.

`def retriever(question: str):
    print(f&quot;Search query: {question}&quot;)
    structured_data = structured_retriever(question)
    unstructured_data = [el.page_content for el in vector_index.similarity_search(question)]
    final_data = f&quot;&quot;&quot;Structured data:
{structured_data}
Unstructured data:
{&quot;#Document &quot;. join(unstructured_data)}
    &quot;&quot;&quot;
    return final_data`

As we are dealing with Python, we can simply concatenate the outputs using the f-string.

## Defining the RAG chain

We have successfully implemented the retrieval component of the RAG. Next, we introduce a prompt that leverages the context provided by the integrated hybrid retriever to produce the response, completing the implementation of the RAG chain.

`template = &quot;&quot;&quot;Answer the question based only on the following context:
{context}

Question: {question}
&quot;&quot;&quot;
prompt = ChatPromptTemplate.from_template(template)

chain = (
    RunnableParallel(
        {
            &quot;context&quot;: _search_query | retriever,
            &quot;question&quot;: RunnablePassthrough(),
        }
    )
    | prompt
    | llm
    | StrOutputParser()
)`

Finally, we can go ahead and test our hybrid RAG implementation.

`chain.invoke({&quot;question&quot;: &quot;Which house did Elizabeth I belong to?&quot;})
# Search query: Which house did Elizabeth I belong to?
# &#x27;Elizabeth I belonged to the House of Tudor.&#x27;`

I’ve also incorporated a query rewriting feature, enabling the RAG chain to adapt to conversational settings that allow follow-up questions. Given that we use vector and keyword search methods, we must rewrite follow-up questions to optimize our search process.

`chain.invoke(
    {
        &quot;question&quot;: &quot;When was she born?&quot;,
        &quot;chat_history&quot;: [(&quot;Which house did Elizabeth I belong to?&quot;,
        &quot;House Of Tudor&quot;)],
    }
)
# Search query: When was Elizabeth I born?
# &#x27;Elizabeth I was born on 7 September 1533.&#x27;`

You can observe that `When was she born?` was first rewritten to `When was Elizabeth I born?` . The rewritten query was then used to retrieve relevant context and answer the question.

## Summary

With the introduction of the `LLMGraphTransformer`, the process of generating knowledge graphs should now be smoother and more accessible, making it easier for anyone looking to enhance their RAG-based applications with the depth and context that knowledge graphs provide. This is just a start as we have a lot of improvements planned.

If you have insights, suggestions, or questions about our generating graphs with LLMs, please don’t hesitate to reach out.

The code is available on [GitHub](https://github.com/tomasonjo/blogs/blob/master/llm/enhancing_rag_with_graph.ipynb?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)