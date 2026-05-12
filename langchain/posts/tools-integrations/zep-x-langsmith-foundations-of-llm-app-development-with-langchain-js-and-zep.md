---
title: "Zep x LangSmith: Foundations of LLM app development with LangChain.js and Zep"
author: "LangChain Accounts"
date: "2023-08-17"
url: "https://www.langchain.com/blog/zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep"
---

PartnerLangSmith

# Zep x LangSmith: Foundations of LLM app development with LangChain.js and Zep

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 17, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)10min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b5504e43f6295a6c06_5-social--2-.png)Learn how to build three foundational LLM apps using TypeScript, LangChain.js, and Zep.

*Editor&#x27;s Note: This post was written in collaboration with the *[*Zep*](https://www.getzep.com/?ref=blog.langchain.com)* team.* *The post walks, step-by-step, through the process of building three foundational LLM apps using TypeScript, LangChain.js, and Zep. We think it&#x27;s a really compelling exploration of RAG and agents accessing to tools, combined with LangSmith for visibility into model behavior. And, we think–and hope–more developers will try these same approaches in their apps! *

Python gets much of the love in the LLM space. However, most web apps are built using TypeScript, JavaScript, and related technologies. Zep has first-class support for TypeScript and JavaScript, and this article explores using Zep and LangChain.js to build the foundation for various types of LLM apps.

Zep&#x27;s long-term memory store makes it simple for developers to add relevant documents, chat history memory &amp; rich user data to their prompts and without having to manage multiple pieces of infrastructure. Zep also automatically embeds chat history and documents, reducing reliance on 3rd-party embedding APIs.

💡

The source code for this post may be found in the [Zep By Example Repo](https://github.com/getzep/zep-by-example/tree/main/langchain/js?ref=blog.langchain.com).

### An overview of the LangChain features we&#x27;ll use

We&#x27;re going to build the foundations for three types of applications, all using LangChain&#x27;s `ZepMemory` and `ZepVectorStore` classes.

- A simple conversational bot using a `ConversationChain`. We&#x27;ll use this to demonstrate the ability to recall past conversations.
- A *Retrieval Augmented Generation* app using a `ConversationalRetrievalQAChain`. We&#x27;ll demonstrate how to populate Zep&#x27;s VectorStore with several books, and ask the LLM questions about the books.
- Lastly, we&#x27;ll build a REACT-type *agent* that has access to two tools. The first, a `peopleRetriever` tool, provides search access to historical chat messages but filtered by entity for people&#x27;s names. The second, the `bookSearch` tool, provides search access over our book collection.

We&#x27;ll use LangChain&#x27;s new [LangSmith platform](https://www.langchain.com/langsmith?ref=blog.langchain.com) for observability, providing insight into what our chains and agent are doing under the hood.

### A simple conversational bot recalling past conversations

This somewhat trivial example demonstrates preloading historical conversation into Zep and passing an instance of `ZepMemory` to the chain.

Let&#x27;s start off by [initializing Zep in our app](https://docs.getzep.com/sdk/?ref=blog.langchain.com) and creating a `sessionId`, a unique key representing the user or a user&#x27;s chat session. We&#x27;ll then [load some test data](https://docs.getzep.com/sdk/chat_history/?ref=blog.langchain.com#persisting-a-memory-to-a-session) into the chat history for this session.

`// Create a new ZepClient instance
const client = await ZepClient.init(ZEP_API_URL, ZEP_API_KEY);

// Create a session ID for our conversation. This ID could represent our user, or a
// conversation thread with a user. i.e. You can map multiple sessions to a single user
// in your data model.
const sessionId = randomUUID();

// add the sample chat history to the Zep memory
const messages = history.map(
  ({ role, content }: { role: string; content: string }) =&gt;
    new Message({ role, content }),
);
const zepMemory = new Memory({ messages });
await client.memory.addMemory(sessionId, zepMemory);
`

Let&#x27;s now create an instance of `ZepMemory` initialized for the above session, and create our chain. We&#x27;ll ask the LLM what we&#x27;ve discussed so far, giving it the opportunity review the chat history provided by Zep.

`// Create a new ChatOpenAI model instance. We&#x27;ll use this for both oru chain and agent.
const model = new ChatOpenAI({
  modelName: &quot;gpt-3.5-turbo&quot;,
  temperature: 0,
});

// Let&#x27;s create a new ZepMemory instance with very simple configuration.
// We&#x27;ll use this in our first chain to demonstrate the basics by recalling the
// chat history we&#x27;ve just added to Zep.
const memorySimple = new ZepMemory({
  sessionId,
  baseURL: ZEP_API_URL,
  apiKey: ZEP_API_KEY,
});

// Let&#x27;s start with a simple chain and ask the LLM what we&#x27;ve discussed so far.
const conversationChain = new ConversationChain({
  llm: model,
  memory: memorySimple,
});
const res1 = await conversationChain.run(&quot;What have we discussed so far?&quot;);
console.log(res1);`

Thanks to LangSmith, we have visibility into the data sent to the LLM. You&#x27;ll note below that Zep has automatically summarized the long chat history and provided it to our chain as a *system message*. Zep does this asynchronously on the server in order to avoid impacting the user experience.

LangSmith has the nifty ability to share traces and you can [find the trace for this chain here.](https://smith.langchain.com/public/0fac6325-b58a-4f74-89e2-57f8985ced28/r?ref=blog.langchain.com)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b5504e43f6295a6c19_image.png)

For each subsequent turn of the conversation, LangChain will persist AI and human messages to Zep. These messages will be automatically added to later prompts.

Alongside summarization, Zep also enriches memories with named entities, an intent analysis, and token counts. We&#x27;ll use some of this metadata later when we build our agent.

`    {
      &quot;uuid&quot;: &quot;d02a90a7-0981-43ae-92bf-95e448f6fff4&quot;,
      &quot;created_at&quot;: &quot;2023-08-17T04:11:43.520994Z&quot;,
      &quot;role&quot;: &quot;AI&quot;,
      &quot;content&quot;: &quot;So far, we have discussed the authors Kurt Vonnegut, Jules Verne, and Philip K. Dick. We talked about their most famous books, some other notable works, the genres they wrote in, the awards they won, and the influences on their writing styles. We also mentioned the common themes in their works, such as critiques of society, exploration of the human condition, and speculations about future technologies.&quot;,
      &quot;token_count&quot;: 88,
      &quot;metadata&quot;: {
        &quot;system&quot;: {
          &quot;entities&quot;: [
            {
              &quot;Label&quot;: &quot;PERSON&quot;,
              &quot;Matches&quot;: [
                {
                  &quot;End&quot;: 51,
                  &quot;Start&quot;: 38,
                  &quot;Text&quot;: &quot;Kurt Vonnegut&quot;
                }
              ],
              &quot;Name&quot;: &quot;Kurt Vonnegut&quot;
            },
            {
              &quot;Label&quot;: &quot;PERSON&quot;,
              &quot;Matches&quot;: [
                {
                  &quot;End&quot;: 64,
                  &quot;Start&quot;: 53,
                  &quot;Text&quot;: &quot;Jules Verne&quot;
                }
              ],
              &quot;Name&quot;: &quot;Jules Verne&quot;
            },
            {
              &quot;Label&quot;: &quot;PERSON&quot;,
              &quot;Matches&quot;: [
                {
                  &quot;End&quot;: 84,
                  &quot;Start&quot;: 70,
                  &quot;Text&quot;: &quot;Philip K. Dick&quot;
                }
              ],
              &quot;Name&quot;: &quot;Philip K. Dick&quot;
            }
          ]
        }
      }
    }
`

### Building a Q&amp;A over Docs / RAG-type app

Next, we&#x27;ll use Zep&#x27;s VectorStore to support a `ConversationalRetrievalQAChain` searching over a Zep document Collection. We&#x27;ve downloaded three public domain scifi books and will be using these for our demo.

How we approach chunking can significantly effect the performance of our app. Since we have multiple books and will be chunking each of these, we&#x27;ve included the file name as a prefix to each chunk. This ensures the LLM can relate a chunk to its source.

`async function loadDocs(path: string): Promise&lt;Document[]&gt; {
  return new DirectoryLoader(path, {
    &quot;.txt&quot;: (path) =&gt; new TextLoader(path),
  }).load();
}

async function loadDocsIntoVectorStore(
  config: IZepConfig,
): Promise&lt;ZepVectorStore&gt; {
  const docs = await loadDocs(&quot;./books&quot;);
  console.log(`Loaded ${docs.length} documents`);

  // Split the documents into chunks
  const splitter = new RecursiveCharacterTextSplitter({
    chunkSize: 1000,
    chunkOverlap: 200,
    separators: [&quot;\n\n&quot;, &quot;\n&quot;, &quot; &quot;, &quot;&quot;, &quot;\r&quot;, &quot;\r\n&quot;], // add carriage returns to the list of separators
  });

  // Split the documents into chunks. We also add the source of the document as a header to each chunk.
  const chunks = (
    await Promise.all(
      docs.map((doc) =&gt;
        splitter.splitDocuments([doc], {
          chunkHeader: doc.metadata.source
            ? &quot;SOURCE: &quot; + doc.metadata.source.split(&quot;/&quot;).pop() + &quot;\n\n&quot;
            : &quot;&quot;,
          appendChunkOverlapHeader: true,
        }),
      ),
    )
  ).flat();

  return ZepVectorStore.fromDocuments(chunks, new FakeEmbeddings(), config);
}`

We&#x27;re creating a new Zep Collection, and so the config we pass into the `loadDocsIntoStore` function includes mandatory `embeddingDimensions` and `isAutoEmbedded` fields. The first specifies the width of the vectors generated by the embedding model we&#x27;ll use, and the second tells Zep whether it should embed the documents for us. We can alternatively pass in embedding vectors.

`const config: IZepConfig = {
  apiUrl: ZEP_API_URL,
  apiKey: ZEP_API_KEY,
  collectionName: ZEP_COLLECTION_NAME,
  embeddingDimensions: 768, // Set to the width of the model configured in Zep. Use 1536 for OpenAI
  isAutoEmbedded: true,
};`

Let&#x27;s populate our collection with documents and wait for Zep to embed them. Zep Collections have a `status` field that we can poll to determine whether all present documents have been embedded.

`  // Create a new ZepVectorStore instance and load a document collection into it
  const vectorStore = await loadDocsIntoVectorStore(ZEP_COLLECTION_CONFIG);

  // Wait for the ZepVectorStore to finish embedding the documents
  console.log(&quot;Waiting for Zep to finish embedding documents...&quot;);
  while (true) {
    const c = await client.document.getCollection(ZEP_COLLECTION_NAME);
    console.log(
      `Embedding status: ${c.document_embedded_count}/${c.document_count} documents embedded`,
    );
    await new Promise((resolve) =&gt; setTimeout(resolve, 1000));
    if (c.status === &quot;ready&quot;) {
      break;
    }
  }`

Next, we&#x27;ll configure our memory and chain classes and question the LLM about the books. We&#x27;ve configured the `ZepMemory` with a `memoryKey` and other fields. These need to be aligned with the prompts a chain uses and are dependent on the chain class.

`// Let&#x27;s create a new ZepMemory instance. This will be used to store the current state of the conversation.
// Zep will also auto-summarize and enrich memories for you.
const memory = new ZepMemory({
  sessionId,
  baseURL: ZEP_API_URL,
  apiKey: ZEP_API_KEY,
  memoryKey: &quot;chat_history&quot;,
  inputKey: &quot;question&quot;, // The key for the input to the chain
  outputKey: &quot;text&quot;, // The key for the final conversational output of the chain
});

// Create a new ConversationalRetrievalQAChain instance
// Initialize the chain with the model, the vector store, and the memory
// We&#x27;ll configure the VectorStore&#x27;s Retriever to use Maximal Marginal Relevance reranking.
// This will re-rank the search results to ensure that the results are diverse.
const chain = ConversationalRetrievalQAChain.fromLLM(
  model,
  vectorStore.asRetriever({
    searchType: &quot;mmr&quot;,
    k: 4,
  }),
  { memory: memory },
);`

In the code above, we&#x27;re passing in the `ZepVectorStore` class as a LangChain `Retriever. `Under the hood, Zep uses cosine similarity normalized to [0,1] to order search results. Here, we&#x27;re configuring the Zep retriever to use [*Maximal Marginal Relevance*](https://python.langchain.com/docs/modules/model_io/prompts/example_selectors/mmr?ref=blog.langchain.com) to re-rank search results for diversity. This is useful for RAG apps but domain-dependent, and you should explore how helpful it is for your use case.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c2c_image-1.png)

The [trace for a call to the chain is above](https://smith.langchain.com/public/9f799057-81c4-4d7e-86f9-dd0508ac00c1/r?ref=blog.langchain.com). With the `ConversationalRetrievalQAChain`, multiple calls are made to the LLM. First, depicted above, the LLM is provided with the user&#x27;s question and the chat history and is asked to rephrase the question given this context. The rephrased question is then used to search over the document collection.

This approach is helpful when a user&#x27;s question alone does not convey enough context to search the vector database.

I mentioned above how a thoughtful approach to chunking is essential to how well our app works. Well, so is data preparation. In looking at the search results from the vector store, I see that the first result is the Project Gutenberg preface to the book, as it is close in the vector space to our *book*-related query.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c2f_image-2.png)

We&#x27;d probably want to remove the preface when loading the files and before chunking to improve our results. The other three results are, however, relevant.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c28_image-4.png)

Next, the search results are added to the prompt, along with the rephrased question. The LLM&#x27;s response is highlighted in green below. It does a pretty good job of making sense of the document chunks we&#x27;ve provided it. The &quot;source&quot; header we added to each chunk has ensured that results relevant to *Philip K. Dick* are returned.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c25_image-5.png)

There [are alternative approaches](https://js.langchain.com/docs/modules/chains/document/?ref=blog.langchain.com) to summarizing and refining search results before populating them into a prompt. These do come at the cost of additional LLM calls, so it&#x27;s worth exploring the value trade-off for your app.

### Building a REACT-type agent with Zep Memory Retrieval and Search as Tools

The last type of app we&#x27;ll build is an agent that uses Zep&#x27;s conversational history and vector store as tools. We&#x27;ll take a quick look at the set up below, but will spend time on the tools themselves.

We&#x27;re using the `initializeAgentExecutorWithOptions` helper function to initialize the agent, passing in our tool list and LLM. Passing in a ZepMemory class is also possible, but we&#x27;ll keep it simple for this demonstration.

Each tool has a description that the LLM uses to determine which tool will most likely help it with its task. Note that the agent and tool setup below is fairly primitive. You can build far more [sophisticated ones using Zod](https://js.langchain.com/docs/modules/agents/agent_types/structured_chat?ref=blog.langchain.com) and [OpenAI Functions](https://js.langchain.com/docs/modules/agents/agent_types/openai_functions_agent?ref=blog.langchain.com).

`// Let&#x27;s build an agent!
const zepMemoryRetriever = await new ZepRetriever({
    url: ZEP_API_URL,
    apiKey: ZEP_API_KEY,
    sessionId: sessionId,
});

// Create some tools.
const tools = [
  new DynamicTool({
    name: &quot;peopleRetriever&quot;,
    description: `call this if you want to search for authors, characters, or people we may have discussed in the
past. input should be a search string`,
    func: async (query) =&gt;
      await getPeopleFromMemoryTool(query, zepMemoryRetriever),
  }),
  new DynamicTool({
    name: &quot;bookSearch&quot;,
    description:
      &quot;call this if to search for passages in sci-fi books. input should be a search string&quot;,
    func: async (query) =&gt; await getBookSearchTool(query, vectorStore),
  }),
];

const executor = await initializeAgentExecutorWithOptions(tools, model, {
  agentType: &quot;zero-shot-react-description&quot;,
});`

Zep has a special LangChain Retriever, the aptly named `ZepRetriever`, for searching over a session&#x27;s chat history. We&#x27;re using this above in our first tool, the `peopleRetriever`. As the description implies, this tool searches over historical chat messages for a person. The tool also filters chat message results using Zep&#x27;s entity metadata for `PERSON` entities.

`async function getPeopleFromMemoryTool(
  query: string,
  retriever: ZepRetriever,
): Promise&lt;string&gt; {
  return retriever
    .getRelevantDocuments(query, {
      metadata: {
        where: { jsonpath: &#x27;$.system.entities[*] ? (@.Label == &quot;PERSON&quot;)&#x27; },
      },
    })
    .then((docs) =&gt; {
      const filteredDocs = docs.filter((doc) =&gt; doc.metadata.dist &gt;= 0.8);
      return (
        filteredDocs.length &gt; 0
          ? filteredDocs.map((doc) =&gt; doc.pageContent)
          : [&quot;No results&quot;]
      ).join(&quot;\n\n&quot;);
    });
}`

The function also filters for a cosine similarity above 0.8 to ensure that irrelevant chat messages are not returned to the LLM.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c32_image-6.png)

In the trace above, we can see that we&#x27;ve asked the agent whether we&#x27;ve previously discussed *Kurt Vonnegut*. The agent has correctly determined that it should use the `peopleRetriever` tool with input `Kurt Vonnegut`.

Next, the search results are returned from the tool, passed to the LLM, and it has determined that we have indeed mentioned *Kurt Vonnegut* in our prior conversations.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c35_image-7.png)

Finally, let&#x27;s take a look at the agent&#x27;s use of the `bookSearch` tool. We&#x27;ve asked it the following question: *Which sci-fi novel featured a gun club headquartered in Baltimore?*

Viewing [the trace below](https://smith.langchain.com/public/3db03218-8486-4048-94d8-230401696c98/r?ref=blog.langchain.com), we see the agent chose the correct tool and searched the book collection for *gun club Baltimore*. The vector database returned book chunks relevant to the query, and the agent responds with *From the Earth to the Moon* by Jules Verne.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1b6504e43f6295a6c3d_image-8.png)

### Summing it up

We&#x27;ve explored how to build three foundational LLM app types using LangChain.js and Zep, and, using LangSmith, took a look under the hood as to how things worked.

As mentioned above, the chains, agents, and tools we used are quite primitive. The [LangChain docs](https://python.langchain.com/docs/get_started/introduction.html?ref=blog.langchain.com) are worth exploring as you consider how to solve different problems when building your app. You&#x27;ll see most value from Zep&#x27;s features, including message metadata, when you start to customize or build your own agents and tools.

### Next Steps

- Sign up for the [LangSmith beta](https://smith.langchain.com/?ref=blog.langchain.com)
- Get setup with Zep using the [Quick Start Guide](https://docs.getzep.com/deployment/quickstart?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)