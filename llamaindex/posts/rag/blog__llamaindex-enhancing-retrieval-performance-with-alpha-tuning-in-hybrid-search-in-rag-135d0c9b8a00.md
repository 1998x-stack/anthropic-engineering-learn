---
title: "Hybrid Search Alpha Tuning For RAG: How-To | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaindex-enhancing-retrieval-performance-with-alpha-tuning-in-hybrid-search-in-rag-135d0c9b8a00"
category: "rag"
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



   12



# Introduction

Retrieving the appropriate chunks, nodes, or context is a critical aspect of building an efficient Retrieval-Augmented Generation (RAG) application. However, a vector or embedding-based search may not be effective for all types of user queries.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



To address this, [Hybrid search](https://weaviate.io/blog/hybrid-search-explained) combines both keyword-based methods (BM25) and vector (embedding) search techniques. Hybrid search has a specific parameter, `Alpha` to balance the weightage between keyword (BM25) and vector search in retrieving the right context for your RAG application. (alpha=0.0 - keyword search (BM25) and alpha=1.0 - vector search)

But here’s where it gets interesting: fine-tuning Alpha isn’t just a task; it’s an art form. Achieving the ideal balance is crucial for unlocking the full potential of hybrid search. This involves adjusting different Alpha values for various types of user queries in your RAG system.

In this blog post, we will look into tuning Alpha within the Weaviate vector database using the `[**Retrieval Evaluation**](https://docs.llamaindex.ai/en/stable/examples/evaluation/retrieval/retriever_eval.html)` module of LlamaIndex with and without rerankers with the help of Hit Rate and MRR metrics.

Before diving into the implementation, let’s first understand the different query types and metrics we will be using in this article.

# Different User Query Types:

User queries in an RAG application vary based on individual intent. For these diverse query types, it’s essential to fine-tune the `**Alpha**` parameter. This process involves routing each user query to a specific `**Alpha**` value for effective retrieval and response synthesis. [Microsoft](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167) has identified various user query categories, and we have selected a few for tuning our hybrid search. Below are the different user query types we considered:

- **Web Search Queries:** Brief queries similar to those typically inputted into search engines.
- **Concept Seeking Queries:** Abstract questions that necessitate detailed, multi-sentence answers.
- **Fact Seeking Queries:** Queries that have a single, definitive answer.
- **Keyword Queries:** Concise queries composed solely of crucial identifier words.
- **Queries With Misspellings:** Queries containing typos, transpositions, and common misspellings.
- **Exact Sub-string Searches:** Queries that exactly match sub-strings from the original context.

Let’s look at sample examples in each of these different user query types:

- **Web Search Queries**

>

`*Transfer capabilities of LLaMA language model to non-English languages*`

**2. Concept Seeking Queries**

>

`*What is the dual-encoder architecture used in recent works on dense retrievers?*`

**3. Fact Seeking Queries**

>

`*What is the total number of propositions the English Wikipedia dump is segmented into in FACTOID WIKI?*`

**4. Keyword Queries**

>

`*GTR retriever recall rate*`

**5. Queries With Misspellings**

>

`*What is the advntage of prposition retrieval over sentnce or passage retrieval?*`

**6. Exact Sub-string Searches**

>

`*first kwords for the GTR retriever. Finer-grained*`

# Retrieval Evaluation Metrics:

We will utilize Hit Rate and MRR metrics for retrieval evaluation. Let’s get into understanding these metrics.

**Hit Rate:**

Hit Rate measures the proportion of queries for which the correct chunk/ context appears within the top-k results chunks/ contexts. Put simply, it evaluates how frequently our system correctly identifies the chunk within its top-k chunks.

**Mean Reciprocal Rank (MRR):**

MRR assesses a system’s accuracy by taking into account the position of the highest-ranking relevant chunk/ context for each query. It calculates the average of the inverse of these positions across all queries. For instance, if the first relevant chunk/ context is at the top of the list, its reciprocal rank is 1. If it’s the second item, the reciprocal rank becomes 1/2, and this pattern continues accordingly.

The remainder of this blog post is divided into two main sections:

- Implementing `**Alpha**` Tuning in Hybrid Search for Various Query Types.
- Analyzing the results of two different document datasets:

- **Indexing a Single Document:** The [LLM Compiler Paper](https://arxiv.org/pdf/2312.04511.pdf).
- **Indexing Three Documents:** The [LLM Compiler](https://arxiv.org/pdf/2312.04511.pdf), [Llama Beyond English](https://arxiv.org/abs/2401.01055), and [Dense X Retrieval](https://arxiv.org/abs/2312.06648) Papers.

You can also continue following along in the [Google Colab Notebook](https://colab.research.google.com/drive/1aiXqofZp7hSXuUdv2UGt_QoJa_liJDZ6?usp=sharing) from this point forward.

# Implementation

We will adopt a systematic approach to implement the experimental workflow, which involves the following steps:

- Data Download.
- Data Loading.
- Weaviate Client Setup.
- Index Creation and Node Insertion.
- Define LLM (GPT-4)
- Define CohereAI Reranker.
- Generation of Synthetic Queries for Various Query Types.
- Define CustomRetriever.
- Functions for Retrieval Evaluation and Metrics Calculation.
- Conducting Retrieval Evaluation for Different Query Types and Alpha Values.

Let’s begin by defining some essential functions for our implementation.

- `get_weaviate_client` - sets up weaviate client.
- `load_documents` - load the documents from the file path.
- `create_nodes` - create nodes by chunking the documents using a text splitter.
- `connect_index` - connect to weaviate index.
- `insert_nodes_index` - insert nodes into the index.

def get_weaviate_client(api_key, url):
  auth_config = weaviate.AuthApiKey(api_key=api_key)

  client = weaviate.Client(
    url=url,
    auth_client_secret=auth_config
  )
  return client

def load_documents(file_path, num_pages=None):
  if num_pages:
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()[:num_pages]
  else:
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
  return documents

def create_nodes(documents, chunk_size=512, chunk_overlap=0):
  node_parser = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  nodes = node_parser.get_nodes_from_documents(documents)
  return nodes

def connect_index(weaviate_client):
  vector_store = WeaviateVectorStore(weaviate_client=weaviate_client)
  storage_context = StorageContext.from_defaults(vector_store=vector_store)
  index = VectorStoreIndex([], storage_context=storage_context)
  return index

def insert_nodes_index(index, nodes):
  index.insert_nodes(nodes)
- **Download Data**

!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2312.04511.pdf" -O "llm_compiler.pdf"
!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2401.01055.pdf" -O "llama_beyond_english.pdf"
!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2312.06648.pdf" -O "dense_x_retrieval.pdf"2. **Load Data**

# load documents, we will skip references and appendices from the papers.
documents1 = load_documents("llm_compiler.pdf", 12)
documents2 = load_documents("dense_x_retrieval.pdf", 9)
documents3 = load_documents("llama_beyond_english.pdf", 7)

# create nodes
nodes1 = create_nodes(documents1)
nodes2 = create_nodes(documents2)
nodes3 = create_nodes(documents3)3. **Setup Weaviate Client**

url = 'cluster URL'
api_key = 'your api key'

client = get_weaviate_client(api_key, url)4. **Create an Index and Insert Nodes.**

index = connect_index(client)

insert_nodes_index(index, nodes1)5. **Define LLM**

# Deing LLM for query generation
llm = OpenAI(model='gpt-4', temperature=0.1)6. **Create Synthetic Queries**

We will create queries as discussed earlier, check prompts for each of the query types in the notebook, and code for each type of query. Showing code snippet for reference.

queries = generate_question_context_pairs(
    nodes,
  llm=llm,
  num_questions_per_chunk=2,
  qa_generate_prompt_tmpl = qa_template
)7. **Define reranker**

reranker = CohereRerank(api_key=os.environ['COHERE_API_KEY'], top_n=4)8. **Define CustomRetriever**

We will define `CustomRetriever` class to perform retrieval operations with and without a reranker.

class CustomRetriever(BaseRetriever):
    """Custom retriever that performs hybrid search with and without reranker"""

    def __init__(
        self,
        vector_retriever: VectorIndexRetriever,
        reranker: CohereRerank
    ) -&amp;gt; None:
        """Init params."""

        self._vector_retriever = vector_retriever
        self._reranker = reranker

    def _retrieve(self, query_bundle: QueryBundle) -&amp;gt; List[NodeWithScore]:
        """Retrieve nodes given query."""

        retrieved_nodes = self._vector_retriever.retrieve(query_bundle)

        if self._reranker != None:
            retrieved_nodes = self._reranker.postprocess_nodes(retrieved_nodes, query_bundle)
        else:
            retrieved_nodes = retrieved_nodes[:4]

        return retrieved_nodes

    async def _aretrieve(self, query_bundle: QueryBundle) -&amp;gt; List[NodeWithScore]:
        """Asynchronously retrieve nodes given query.

        Implemented by the user.

        """
        return self._retrieve(query_bundle)

    async def aretrieve(self, str_or_query_bundle: QueryType) -&amp;gt; List[NodeWithScore]:
        if isinstance(str_or_query_bundle, str):
            str_or_query_bundle = QueryBundle(str_or_query_bundle)
        return await self._aretrieve(str_or_query_bundle)9. **Define functions for retriever evaluation and metrics computation**

We will look into retriever performance for different `alpha` values with and without reranker.

# Alpha values and datasets to test
alpha_values = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Function to evaluate retriever and return results
async def evaluate_retriever(alpha, dataset, reranker=None):
    retriever = VectorIndexRetriever(index,
                                     vector_store_query_mode="hybrid",
                                     similarity_top_k=10,
                                     alpha=alpha)
    custom_retriever = CustomRetriever(retriever,
                                       reranker)

    retriever_evaluator = RetrieverEvaluator.from_metric_names(["mrr", "hit_rate"], retriever=custom_retriever)
    eval_results = await retriever_evaluator.aevaluate_dataset(dataset)
    return eval_results

# Function to calculate and store metrics
def calculate_metrics(eval_results):
    metric_dicts = []
    for eval_result in eval_results:
        metric_dict = eval_result.metric_vals_dict
        metric_dicts.append(metric_dict)

    full_df = pd.DataFrame(metric_dicts)

    hit_rate = full_df["hit_rate"].mean()
    mrr = full_df["mrr"].mean()
    return hit_rate, mrr**10. Retrieval Evaluation**

Here we do retrieval evaluation on different query types (datasets) and alpha values to understand which alpha will be suitable for which query type. You need to plug in the reranker accordingly to compute the retrieval evaluation with and without the reranker.

# Asynchronous function to loop over datasets and alpha values and evaluate
async def main():
    results_df = pd.DataFrame(columns=['Dataset', 'Alpha', 'Hit Rate', 'MRR'])

    for dataset in datasets_single_document.keys():
        for alpha in alpha_values:
            eval_results = await evaluate_retriever(alpha, datasets_single_document[dataset])
            hit_rate, mrr = calculate_metrics(eval_results)
            new_row = pd.DataFrame({'Dataset': [dataset], 'Alpha': [alpha], 'Hit Rate': [hit_rate], 'MRR': [mrr]})
            results_df = pd.concat([results_df, new_row], ignore_index=True)

    # Determine the grid size for subplots
    num_rows = len(datasets_single_document) // 2 + len(datasets_single_document) % 2
    num_cols = 2

    # Plotting the results in a grid
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, num_rows * 4), squeeze=False)  # Ensure axes is always 2D

    for i, dataset in enumerate(datasets_single_document):
        ax = axes[i // num_cols, i % num_cols]
        dataset_df = results_df[results_df['Dataset'] == dataset]
        ax.plot(dataset_df['Alpha'], dataset_df['Hit Rate'], marker='o', label='Hit Rate')
        ax.plot(dataset_df['Alpha'], dataset_df['MRR'], marker='o', linestyle='--', label='MRR')
        ax.set_xlabel('Alpha')
        ax.set_ylabel('Metric Value')
        ax.set_title(f'{dataset}')
        ax.legend()
        ax.grid(True)

    # If the number of datasets is odd, remove the last (empty) subplot
    if len(datasets_single_document) % num_cols != 0:
        fig.delaxes(axes[-1, -1])  # Remove the last subplot if not needed

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()

# Run the main function
asyncio.run(main())

# Analyze the results:

Having completed the implementation phase, we now turn our attention to analyzing the outcomes. We conducted two sets of experiments: one on a single document and another on multiple documents. These experiments varied in alpha values, types of user queries, and the inclusion or exclusion of a reranker. The accompanying graphs display the results, focusing on the Hit Rate and MRR (Mean Reciprocal Rank) as retrieval evaluation metrics.

>

Please keep in mind that following observations are specific to the datasets used in our study. We encourage you to conduct the experiment with your own documents and draw your relevant observations and conclusions.

## **With Single Document:**

**Without Reranker:**

![](/blog/images/1*MvCcrI782Hex9AEB51srpA.png)

**With Reranker:**

![](/blog/images/1*iAJP382Gm0I_cDN6CRQNxg.png)

## With Multiple Documents:

**Without Reranker:**

![](/blog/images/1*n5GtKtfgi5hI6-uznFgW8Q.png)

**With Reranker:**

![](/blog/images/1*gi7oiwJmZswrgWCE5ttoMg.png)

# Observations:

- There is a boost in Hit Rate and MRR in single and multiple documents indexing with the help of a reranker. Time and again it proves using reranker is pretty useful in your RAG application.
- Though most of the time hybrid search wins over keyword/ vector search, it should be carefully evaluated for different query types based on user queries in the RAG application.
- The behavior is different when you index a single document and multiple documents, which suggests it’s always better to tune alpha as you add documents into the index.
- Let’s look at a deeper analysis of different query types:

- **Web Search Queries:**

— MRR is higher with hybrid search with alpha=0.2/0.6 based on with/ without rerankers irrespective of single/ multiple documents indexing.

— The Hit rate is higher with alpha=1.0 for both single/ multiple documents indexing and with/ without rerankers.

- **Concept Seeking Queries:**

— MRR and Hit Rate are higher with hybrid search (with different alpha values) in Multiple documents indexing.

— MRR and Hit Rate are higher at Alpha=0.0 indicating keyword search works better in Single document indexing. Should be noted that MRR has different behavior with and without reranking.

- **Fact Seeking Queries**

— MRR and Hit Rate are higher with Hybrid search with/ without reranker in Multiple documents indexing.

— MRR and Hit Rate are higher with hybrid search with reranker and keyword search (alpha=0.0) is better without reranker in single documents indexing.

- **Keyword Queries**

— MRR and Hit Rate are higher with Hybrid search with/ without reranker in Multiple documents indexing.

— MRR and Hit Rate are higher with hybrid search with reranker and keyword search is better without reranker in single documents indexing. (though MRR is slightly higher with alpha=0.2)

- **Queries With Misspellings**

— MRR and Hit Rate are higher with Hybrid search with/ without reranker in single and multiple documents indexing. (Though in some cases hybrid search with alpha=1.0 wins).

— This also demonstrates that vector search performs better with misspelled queries, as keyword searches lose effectiveness in such cases.

- **Exact Sub-string Searches**

— MRR and Hit Rate are higher with Keyword search with/ without reranker in Single documents indexing and without reranker in multiple documents indexing.

— MRR and Hit Rate are higher with Hybrid search (alpha=0.4) with reranker in multiple documents indexing.

# What’s Next?

In this blog post, we looked into the tuning of Alpha in a hybrid search system for a range of query types. It was interesting to see how the results varied when indexing either a single document or multiple documents. Going forward, you might consider experimenting with documents from diverse domains, employing different query lengths for various query types. Should you come across any noteworthy observations, we encourage you to share them with us in the comments. It would certainly be interesting to discuss these findings with the wider community.

# References:

- [Hybrid Search Explained](https://weaviate.io/blog/hybrid-search-explained)
- [Azure AI Search: Outperforming vector search with hybrid retrieval and ranking capabilities](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167)