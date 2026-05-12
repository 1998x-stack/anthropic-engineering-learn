---
title: "Chat with your data using OpenAI, Pinecone, Airbyte and Langchain"
author: "LangChain Accounts"
date: "2023-08-08"
url: "https://www.langchain.com/blog/chat-with-your-data-using-openai-pinecone-airbyte-langchain"
---

Tutorials &amp; How-Tos

# Chat with your data using OpenAI, Pinecone, Airbyte and Langchain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 8, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)18min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d53fe3e9a95a560821_image20.jpeg)***Editor’s Note: This blog post was written in collaboration with ***[***Airbyte***](https://airbyte.com/?ref=blog.langchain.com)***. Their ***[***new vector database destination***](https://docs.airbyte.com/integrations/destinations/langchain/?ref=blog.langchain.com)*** makes it really easy for data to retrieve relevant context for question answering use cases via LangChain.  We&#x27;re seeing more and more teams seek ways to  integrate diverse data sources–and keep them up-to-date automatically–and this is a fantastic way to do it! ***

***Aside from the specific use case highlighted here, we&#x27;re also very excited about this integration in general. It combines the hundreds of sources in AirByte with their robust scheduling and orchestration framework, and leverages the advanced transformation logic in LangChain along with LangChain&#x27;s 50+ embedding provider integrations and 50+ vectorstore integrations.***

*Learn how to build a connector development support bot for Slack that knows all your APIs, open feature requests and previous Slack conversations by heart*

In [a previous article](https://airbyte.com/tutorials/implement-ai-data-pipelines-with-langchain-airbyte-and-dagster?ref=blog.langchain.com), we explained how Dagster and Airbyte can be leveraged to power LLM-supported use cases. Our newly introduced [vector database destination](https://docs.airbyte.com/integrations/destinations/langchain/?ref=blog.langchain.com) makes this even easier as it removes the need to orchestrate chunking and embedding manually - instead the sources can be directly connected to the vector database through an Airbyte connection.

This tutorial walks you through a real-world use case of how to leverage vector databases and LLMs to make sense out of your unstructured data. By the end of this, you will:

- Know how to extract unstructured data from a variety of sources using Airbyte
- Know how to use Airbyte to efficiently load data into a vector database, preparing the data for LLM usage along the way
- Know how to integrate a vector database into your LLM to ask questions about your proprietary data

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560836_ujinpxejz-b8du5crn_1zqtbkvcztsixopalvmqjunbxtfu4cfc9anzdnchj3hb6j5nvee6lfapxzfom30vfyo-foivbsyccjlvionrs9-ro-mnggyf2dhguski06nmup_9o-pajsfkym4bazntgvce.png)

## What we will build

To better illustrate how this can look in practice, let’s use something that’s relevant for Airbyte itself.

Airbyte is a highly extensible system that allows users to develop their own connectors to extract data from any API or internal systems. Helpful information for connector developers can be found in different places:

- The official connector development documentation website
- Github issues documenting existing feature requests, known bugs and work in progress
- The community Slack help channel

This article describes how to tie together all of these diverse sources to offer a single chat interface to access information about connector development - a bot that can answer questions in plain english about the code base, documentation and reference previous conversations:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560850_ehpvmfqp7yzadohhebtgnt0i0byubze-nevc6uxbwdcgmkwa80srkq-9wgidol8jw5irhwdmcmhjwzahut_m9k1p3xej-urkiu3fqcmbgrj2p5zq3jukli0gwx4mgnpvyvbwxjipxeazr1lus4l-ray.png)

In these examples, information from the documentation website and existing Github issues is combined in a single answer.

## Prerequisites

For following through the whole process, you will need the following accounts. However, you can also work with your own custom sources and use a local vector store to avoid all but the OpenAI account:

- Source-specific accounts
- Apify account
- Github account
- Slack account
- Destination-specific accounts
- OpenAI account
- Pinecone account
- Airbyte instance ([local](https://docs.airbyte.com/deploying-airbyte/local-deployment/?ref=blog.langchain.com) or [cloud](https://cloud.airbyte.com/?ref=blog.langchain.com))

## Step 1 - Fetch Github issues

Airbyte’s feature and bug tracking is handled by the [Github issue tracker](https://github.com/airbytehq/airbyte/issues?ref=blog.langchain.com) of the Airbyte open source repository. These issues contain important information people need to look up regularly.

To fetch Github issues, create a new source using the Github connector.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560839_cop1kxjzzqotadep56svn5_nowva7fo6vv1d51l1iy2tyzug1foftepic6kysu5mlymzdk9ug8etslp_ttzvbq_nuhawrskl9as_so9opmmjfrwjnbn55xc5gp5bgxn0uuagluuuqawagpcw1gieyym.png)

If you are using Airbyte Cloud , you can easily authenticate using the “Authenticate your GitHub account”, otherwise follow the instructions in the documentation on the right side of how to set up a [personal access token](https://github.com/settings/tokens?ref=blog.langchain.com) in the Github UI.

Next, configure a cutoff date for issues and specify the repositories that should be synced. In this case I’m going with “2023-07-01T00:00:00Z” and “airbytehq/airbyte” to sync recent issues from the main Airbyte repository:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a56083c_0p_tzc0jyt4slno24bmop1g_kz0pc1cdlxbbnc0au37vqne3gxjak4gw2_pbsnxx59ha1dxfdnsy33weuwpo9_7jo3qf2hvr2so1byt0ebnbt8gbyvnpqiudjaztoh1zgnn0sn2hurnslxm1uyn8zgq.png)

## Step 2 - Load into vector database

Now we have our first source ready, but Airbyte doesn’t know yet where to put the data. The next step is to configure the destination. To do so, pick the “Pinecone” connector. There is some preprocessing that Airbyte is doing for you so that the data is vector ready:

- Separating text and metadata fields and splitting up records into multiple documents to keep each document focused on a single topic and to make sure the text fits into the context window of the LLM that’s going to be used for question answering
- Embedding the text of every document using the configured embedding service, turning the text into a vector to do similarity search on
- Indexing the documents into the vector database (uploading the vector from the embedding service along with the metadata object)

Besides Pinecone, Airbyte supports loading data into Weaviate, Milvus, Qdrant and Chroma.

For using Pinecone, sign up for a [free trial account](https://app.pinecone.io/?sessionType=signup&amp;ref=blog.langchain.com) and create an index using a starter pod. Set the dimensions to **1536** as that’s the size of the OpenAI embeddings we will be using

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560853_zuimpcckdmq7kqzfngo9zjymo1epgxistffs8jgebwgsrdub0dtxyf5ipbdc7vcvs6u873y69egz5dkysda6-3jbynqkhgtk4hd8vlbwsdohojua8psrq3jntoslygdwbyoripjzv8ry23rmvkh4pso.png)

Once the index is ready, configure the vector database destination in Airbyte:

- Set chunk size to **1000** (the size refers to number of tokens, not characters, so this is roughly 4KB of text. The best chunking is dependent on the data you are dealing with)
- Configure the records fields to treat as text fields which will be embedded. All other fields will be handled as metadata. For now, set it “**title**” and “**body**” as these are the relevant feels in the issue stream of the Github source
- Set your OpenAI api key for powering the embedding service. You can find your API key in the API keys section of the [platform.openai.com/account](https://platform.openai.com/account?ref=blog.langchain.com) page
- For the indexing step, copy over index, environment and api key from the Pinecone UI. You can find the API key and the environment in the “API Keys” section in the UI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a56083f_xh7oqwnygqrap798u3-epoo9puftswjsyd3cunxeahs8r06qetxzftb4s_qvubtfx-xmr5rdxzpua2kjabyzxwfla44c9xy6gmdqtmpshldtobq3xi2opyxsuyoqxds-7m1xkrqruqynxkvcjemfpks.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560856_8w3pjoulh-bzswowq8buou7dh0asmh0oh6knzq3he2hc6bcclsevd7wo_ccxuhloodokuyhx6qqymgmlkwxhzmotyzbjrkudvo0yisiloylritd4pvpy-idt75dklbcsj1wibdufjuj8vsy0flyvw7c.png)

## Step 3 - Create a connection

Once the destination is set up successfully, set up a connection from the Github source to the vector database destination. In the configuration flow, pick the existing source and destination. When configuring the connection, make sure to only use the “issues” stream, as this is the one we are interested in.

Side note: Airbyte allows to make this sync more efficient in a production environment:

- To keep the metadata focused, you can click on the stream name to select the individual fields you want to sync. For example if the “assignee” or the “milestone” field is never relevant to you, you can uncheck it and it won’t be synced to the destination.
- The sync mode can be used to sync issues incrementally while deduplicating the records in the vector database so no stale data will show up in searches

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560859_oowbc1f63est1tbtzzrmusfrt4qpymlvmoaukmbhsgrxqmdoxxrgnvxc1xt107giujalfa8telc2vwemnajuwy13cizsppmnyhjihn2ty81z8rixjgxt-bbpybe_t2qutgk_kqxjj5d-9uwnf9z5c2a.png)

If everything went well, there should be a connection now syncing data from Github to Pinecone via the vector store destination. Give the sync a few minutes to run. Once the first run has completed, you can check the [Pinecone index management page](https://app.pinecone.io/?ref=blog.langchain.com) to see a bunch of indexed vectors ready to be queried.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560842_yeal8oklviscdc7ffziet9ggcnq-cl2jokvsnmlbs2llcxl93cjw_dzoemn1phecfaprgrxjmhao_m2gxqnlec3or8n8gaf2n_ewqro4z7mjmn0dzmukhyqoy1k-ehwy1hmhx8veuwhsb_psru6iitq.png)

Each vector is associated with a metadata object that’s filled with the fields that were not mentioned as “text fields” in the destination configuration. These fields will be retrieved along with the embedded text and can be leveraged by our chatbot in later sections. This is how a vector with metadata looks like when retrieved from Pinecone:

`{
      &quot;id&quot;: &quot;599d75c8-517c-4f37-88df-ff16576bd607&quot;,
      &quot;values&quot;: [0.0076571689, ..., 0.0138477711],
      &quot;metadata&quot;: {
        &quot;_ab_stream&quot;: &quot;issues&quot;,
        &quot;_ab_record_id&quot;: 1556650122,
        &quot;author_association&quot;: &quot;CONTRIBUTOR&quot;,
        &quot;comments&quot;: 3,
        &quot;created_at&quot;: &quot;2023-01-25T13:21:50Z&quot;,
        // ...
        &quot;text&quot;: &quot;...The acceptance-test-config.yml file is in a legacy format. Please migrate to the latest format...&quot;,
        &quot;updated_at&quot;: &quot;2023-07-17T09:20:56Z&quot;,
      }
}`

On subsequent runs, Airbyte will only re-embed and update the vectors for the issues that changed since the last sync - this will speed up subsequent runs while making sure your data is always up-to-date and available.

##
Step 4 - Chat interface

The data is ready, now let’s wire it up with our LLM to answer questions in natural language. As we already used OpenAI for the embedding, the easiest approach is to use it as well for the question answering.

We will use Langchain as an orchestration framework to tie all the bits together.

First, install a few pip packages locally:

`pip install pinecone-client langchain openai`

The basic functionality here works the following way:

- User asks a question
- The question is embedded using the same model used for generating the vectors in the vector database (OpenAI in this case)
- The question vector is sent to the vector database and documents with similar vectors are returned - as the vectors represent the meaning of the text, the question and the answer to the question will have very similar vectors and relevant documents will be returned
- The text of all documents with the relevant metadata are put together into a single string and sent to the LLM together with the question the user asked and the instruction to answer the user’s question based on the provided context
- The LLM answers the question based on the provided context
- The answer is presented to the user

This flow is often referred to as [retrieval augmented generation](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html?ref=blog.langchain.com). The RetrievalQA class from the Langchain framework already implements the basic interaction. The simplest version of our question answering bot only has to provide the vector store and the used LLM:

`# chatbot.py
import os
import pinecone
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone

embeddings = OpenAIEmbeddings()
pinecone.init(api_key=os.environ[&quot;PINECONE_KEY&quot;], environment=os.environ[&quot;PINECONE_ENV&quot;])
index = pinecone.Index(os.environ[&quot;PINECONE_INDEX&quot;])
vector_store = Pinecone(index, embeddings.embed_query, &quot;text&quot;)

qa = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), chain_type=&quot;stuff&quot;, retriever=vector_store.as_retriever())

print(&quot;Connector development help bot. What do you want to know?&quot;)
while True:
    query = input(&quot;&quot;)
    answer = qa.run(query)
    print(answer)
    print(&quot;\nWhat else can I help you with:&quot;)`

To run this script, you need to set OpenAI and Pinecone credentials as environment variables:

`export OPENAI_API_KEY=...
export PINECONE_KEY=...
export PINECONE_ENV=...
export PINECONE_INDEX=...
python chatbot.py`

This works in general, but it has some limitations. By default, only the text fields are passed into the prompt of the LLM, so it doesn’t know what the context of a text is and it also can’t give a reference back to where it found its information:

`Connector development help bot. What do you want to know?
&gt; Can you give me information about how to authenticate via a login endpoint that returns a session token?

Yes, the GenericSessionTokenAuthenticator should be supported in the UI[...]`

From here, there’s lots of fine tuning to do to optimize our chat bot. For example we can improve the prompt to contain more information based on the metadata fields and be more specific for our use case:

`prompt_template = &quot;&quot;&quot;You are a question-answering bot operating on Github issues and documentation pages for a product called connector builder. The documentation pages document what can be done, the issues document future plans and bugs. Use the following pieces of context to answer the question at the end. If you don&#x27;t know the answer, just say that you don&#x27;t know, don&#x27;t try to make up an answer. Always state were you got this information from (and the github issue number if applicable).
If the answer is based on a Github issue that&#x27;s not closed yet, add &#x27;This issue is not closed yet - the feature might not be shipped yet&#x27; to the answer.

{context}

Question: {question}
Helpful Answer:&quot;&quot;&quot;

prompt = PromptTemplate(
    template=prompt_template, input_variables=[&quot;context&quot;, &quot;question&quot;]
)

class ConnectorDevelopmentPrompt(PromptTemplate):
    def format_document(doc: Document, prompt: PromptTemplate) -&gt; str:
        if doc.metadata[&quot;_ab_stream&quot;] == &quot;issues&quot;:
            return f&quot;Excerpt from Github issue: {doc.page_content}, issue number: {doc.metadata[&#x27;number&#x27;]}, issue state: {doc.metadata[&#x27;state&#x27;]}&quot;
        else:
            return super().format_document(doc, prompt)

document_prompt = ConnectorDevelopmentPrompt(input_variables=[&quot;page_content&quot;], template=&quot;{page_content}&quot;)
qa = RetrievalQA.from_chain_type(llm=OpenAI(temperature=0), chain_type=&quot;stuff&quot;, retriever=vector_store.as_retriever(), chain_type_kwargs={&quot;prompt&quot;: prompt, &quot;document_prompt&quot;: document_prompt})`

The full script also be found [on Github](https://github.com/airbytehq/tutorial-connector-dev-bot/blob/main/localbot_adapted.py?ref=blog.langchain.com)

This revised version of the RetrievalQA chain customizes the prompts that are sent to the LLM after the context has been retrieved:

- The basic prompt template sets the broader context what this question is about (previously the LLM had to guess from the documents)
- It also changes the way documents are added to the prompt - by default, only the text is added, but the ConnectorDevelopmentPrompt implementation sets the context where the data is coming from and also adds relevant metadata to the prompt so the LLM can base its answer on more than just the text

`Connector development help bot. What do you want to know?
&gt; Can you give me information about how to authenticate via a login endpoint that returns a session token?

You can use the GenericSessionTokenAuthenticator to authenticate via a login endpoint that returns a session token. This is documented in the Connector Builder documentation with an example of how the request flow functions (e.g. metabase). This issue is not closed yet - the feature might not be shipped yet (Github issue #26341).`

##
Step 5 - Put it on Slack

So far this helper can only be used locally. However, using the python slack sdk it’s easy to turn this into a Slack bot itself.

To do so, we need to set up a Slack “App” first. Go to [https://api.slack.com/apps](https://api.slack.com/apps?ref=blog.langchain.com) and create a new app based on the manifest [here](https://raw.githubusercontent.com/airbytehq/tutorial-connector-dev-bot/main/slack_manifest.json?ref=blog.langchain.com) (this saves you some work configuring permissions by hand). After you set up your app, install it to the workspace you want to integrate with. This will generate a “Bot User OAuth Access Token” you need to note down. Afterwards, go to the “Basic information” page of your app, scroll down to “App-Level Tokens” and create a new token. Note down this “app level token” as well.

Within the regular Slack client, your app can be added to a slack channel by clicking the channel name and going to the “Integrations” tab:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a56085c_i9gwhcsnmnodfaoxxp_6qgk8zw3ek_jj-oaolxok3itmoxl_gdxnew6eglbsbmmkc9vg5vsced6kbzmfayhoca44ylj2j1fd5ekbvw9qcp0vadmbic8yzuuoon5t7puqqg4kbhnb7vgrejzzm96yi70.png)

After this, your Slack app is ready to receive pings from users to answer questions - the next step is to call Slack from within python code, so we need to install the python client library:

`pip install slack_sdk`

Afterwards, we can extend our existing chatbot script with a Slack integration:

`from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse

slack_web_client = WebClient(token=os.environ[&quot;SLACK_BOT_TOKEN&quot;])

handled_messages = {}

def process(client: SocketModeClient, socket_mode_request: SocketModeRequest):
    if socket_mode_request.type == &quot;events_api&quot;:
        event = socket_mode_request.payload.get(&quot;event&quot;, {})
        client_msg_id = event.get(&quot;client_msg_id&quot;)
        if event.get(&quot;type&quot;) == &quot;app_mention&quot; and not handled_messages.get(client_msg_id):
            handled_messages[client_msg_id] = True
            channel_id = event.get(&quot;channel&quot;)
            text = event.get(&quot;text&quot;)
            result = qa.answer(text)
            slack_web_client.chat_postMessage(channel=channel_id, text=result)

    return SocketModeResponse(envelope_id=socket_mode_request.envelope_id)

socket_mode_client = SocketModeClient(
    app_token=os.environ[&quot;SLACK_APP_TOKEN&quot;],
    web_client=slack_web_client
)
socket_mode_client.socket_mode_request_listeners.append(process)

socket_mode_client.connect()
print(&quot;listening&quot;)
from threading import Event
Event().wait()`

The full script also be found [on Github](https://github.com/airbytehq/tutorial-connector-dev-bot/blob/main/slackbot.py?ref=blog.langchain.com)

To run the script, the environment variables for the slack bot token and app token need to be added as environment variables as well:

`export SLACK_BOT_TOKEN=...
export SLACK_APP_TOKEN=...
python chatbot.py`

Running this, you should be able to ping the development bot application in the channel you added it to like a user and it will respond to questions by running the RetrievalQA chain that loads relevant context from the vector database and uses an LLM to formulate a nice answer:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a56086e_ctzxwdwa6d3fwqtshhujsjkaum8d9gzrpxc_wbydyakqvvpkfuiqqe4t2gxqyf54eromz6bzk6uwbmx_dbrhumnvrwmkol5lwz7du7jf7uahtlilclyfdet-ig7xyqppckdvo2zel9wn8afycdclhua.png)

All the code can also be found [on Github](https://github.com/airbytehq/tutorial-connector-dev-bot?ref=blog.langchain.com)

##
Step 6 - Additional data source: Scrape documentation website

Github issues are helpful, but there is more information we want our development bot to know.

The [documentation page](https://docs.airbyte.com/connector-development/connector-builder-ui/overview/?ref=blog.langchain.com) for connector development is a very important source of information to answer questions, so it definitely needs to be included. The easiest way to make sure the bot has the same information as what’s published, is to scrape the website. For this case, we are going to use the [Apify](https://docs.airbyte.com/integrations/destinations/langchain/?ref=blog.langchain.com) service to take care of the scraping and turning the website into a nicely structured dataset. This dataset can be extracted using the Airbyte Apify Dataset source connector.

First, log into Apify and navigate to the store. Choose the “Web Scraper” actor as a basis - it already implements most of the functionality we need

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a56084c_yn_ghtzznpizcjkm9otesdqf6o71oifzrdoodmajdwlaivpt2nf3rzh64ixyrkjls2djm6-grwe5k_ucgkxtcetrapvhrh1w8yvpy95qtmx6imo6gh-tjd7qfipdg4kihef-kgwuxhmumpsog49edfw.png)

Next, create a new task and configure it to scrape all pages of the documentation, extracting the page title and all of the content:

- Set Start URLs to [https://docs.airbyte.com/connector-development/connector-builder-ui/overview/](https://docs.airbyte.com/connector-development/connector-builder-ui/overview/?ref=blog.langchain.com) , the intro page of the documentation linking to other pages
- Set Link selector to a[href] to follow all links from every page
- Set Glob Patterns to [https://docs.airbyte.com/connector-development/connector-builder-ui/*](https://docs.airbyte.com/connector-development/connector-builder-ui/*?ref=blog.langchain.com) to limit the scraper to stick to the documentation and not crawl the whole internet
- Configure the Page function to extract the page title and the content - in this case the content element can be found using the CSS class name

`async function pageFunction(context) {
    const $ = context.jQuery;
    const pageTitle = $(&#x27;title&#x27;).first().text();
    const content = $(&#x27;.markdown&#x27;).first().text();

    return {
        url: context.request.url,
        pageTitle,
        content
    };
}`

Running this actor will complete quickly and give us a nicely consumable dataset with a column for the page title and the content:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a560871_mzmg-g22lwbjjllhlowcwmofdc9v31bsouv6rqbg3mbswxwjf3f68tzmyh02pnlaftzmfvmknjvjzddzsjjdrzmpiezidmbtt0iy1cvravkjm9enwnkbff-ri8dhzgkau1dg63ogzkawofqxhkwqmy.png)

Now it’s time to connect Airbyte to the Apify data set - go to the Airbyte web UI and add your second Source - pick “Apify Dataset”

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a560864_brfn45rtehx8ozpkp4sk_2vq3elapuw5sl85hu8ea0qoogzj54iqokp6_4og6wwwo_xuauuud8vaigjkws-olx19jfnwyc9gvynixkvfywfqxyxvn_ejwg1aa8cvm--pjf9l8xankx9_spmzyyuvysg.png)

To set up the Source, you only need to copy the dataset ID that’s shown in the “Storage” tap of the “Run” in the Apify UI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a560861_iv4cxlty6vgkmvsf4iv9omohom26zuffm8nunfu76up1ankx23xqugrt5s0dxczfwar17ynqnhsv1tigqd_8xmj4opcggiumtfqrz1hqkldltwv7fw97uo_i--5zt5isiyz5suj1uhb-ktrdbmdigzk.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d83fe3e9a95a560849_y_v0up-8vnbmvb0xbbuzlii6_mn4fhtm7hgkzntoycotxc-y0u0ktt2i3bgzpstdq9gmnnichfskejqqfl_ghhe-r0elcauaozqqc7jahemozyt0dxfknawsg_bsw2suowinikcs98tcnaajqeev_ow.png)

Once the source is set up, follow the same steps as for the Github source to set up a connection moving data from the Apify dataset to the vector store. As the relevant text content is sitting in different fields, you also need to update the vector store destination - add **data.pageTitle** and **data.content** to the “text fields” of the destination and save.

## Step 7 - Additional data source: Fetch Slack messages

Another valuable source of information relevant to connector development are Slack messages from the public help channel. These can be loaded in a very similar fashion. Create a new source using the Slack connector. When using cloud, you can authenticate using the “Authenticate your Slack account” button for simple setup, otherwise follow the instructions in the documentation on the right hand side how to create a Slack “App” with the required permissions and add it to your workspace. To avoid fetching messages from all channels, set the channel name filter to the correct channel.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a56086b_grhgkswfarigc_esbq4qtvh-q29n_qstyjchtlbqms-erl2uf2-ekqacxfl0uobwjcrsmndmzlrgfafu9cpcn-qztubfccwcegtm08__w9eu8xif1xcdjcbkm0l_n4dwqgqp-aeoiml6tfmfuc5pk2e.png)

As for Apify and Github, a new connection needs to be created to move data from Slack to Pinecone. Also add **text** to the “text fields” of the destination to make sure the relevant data gets embedded properly so similarity searches will yield the right results.

If everything went well, there should be three connections now, all syncing data from their respective sources to the centralized vector store destination using a Pinecone index.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1d93fe3e9a95a560867_5bqr308nnav3n4wxjnh2p-chwj_g_zevior07kno61pfppd78pivjz9qh42fzakmt9sucswaw8kgkcgostzia_4nxsob7t15ybcotmydhvy8somfylw1patgosxx90gijqxnrpwenik9vt97fabzami.png)

By adjusting the frequency of the connections, you can control how often Airbyte will rerun the connection to make sure the knowledge base of our chat bot stays up to date. As Github and Slack are frequently updated and support efficient incremental updates, it makes sense to set them to a daily frequency or higher. The documentation pages don’t change as often, so they can be kept at a lower frequency or even just be triggered on demand when there are changes.

As we have more sources now, let’s improve our prompt to make sure the LLM has all necessary information to formulate a good answer:

`class ContextualRetriever(VectorStoreRetriever):
    def _get_relevant_documents(self, query: str, *, run_manager):
        docs = super()._get_relevant_documents(query, run_manager=run_manager)
        return [self.format_doc(doc) for doc in docs]

    def format_doc(self, doc: Document) -&gt; Document:
        if doc.metadata[&quot;_ab_stream&quot;] == &quot;item_collection&quot;:
            doc.page_content = f&quot;Excerpt from documentation page: {doc.page_content}&quot;
        elif doc.metadata[&quot;_ab_stream&quot;] == &quot;issues&quot;:
            doc.page_content =  f&quot;Excerpt from Github issue: {doc.page_content}, issue number: {int(doc.metadata[&#x27;number&#x27;]):d}, issue state: {doc.metadata[&#x27;state&#x27;]}&quot;
        elif doc.metadata[&quot;_ab_stream&quot;] == &quot;threads&quot; or doc.metadata[&quot;_ab_stream&quot;] == &quot;channel_messages&quot;:
            doc.page_content =  f&quot;Excerpt from Slack thread: {doc.page_content}&quot;
        return doc`

By default the RetrievalQA chain retrieves the top 5 matching documents, so if it’s applicable the answer will be based on multiple sources at the same time:

`Connector development help bot. What do you want to know?
&gt; What different authentication methods are supported by the builder? Can I authenticate a login endpoint that returns a session token?

The authentication methods supported by the builder are Basic HTTP, Bearer Token, API Key, and OAuth. The builder does not currently support authenticating a login endpoint that returns a session token, but this feature is planned and can be tracked in the Github issue #26341. This issue is not closed yet - the feature might not be shipped yet.`

The first sentence about Basic HTTP, Bearer Token, API Key and OAuth is retrieved from the [documentation page about authentication](https://docs.airbyte.com/connector-development/connector-builder-ui/authentication/?ref=blog.langchain.com), while the second sentence is referring to the same Github issue as before.

## Wrapping up

We covered a lot of ground here - stepping back a bit, we accomplished the following parts:

- Set up a pipeline that loads unstructured data from multiple sources into a vector database
- Implement an application that can answer plain text questions about the unstructured data in a general way
- Expose this application as a Slack bot

With data flowing through this system, Airbyte will make sure the data in your vector database will always be up-to-date while only syncing records that changed in the connected source, minimizing the load on embedding and vector database services while also providing an overview over the current state of running pipelines.

This setup isn’t using a single black box service that encapsulates all the details and leaves us with limited options for tweaking behavior and controlling data processing - instead it’s composed out of multiple components that be easily extended in various places:

- The large catalog of Airbyte sources and the connector builder for integrating specialized sources allow to easily load just about any data into a vector db using a single tool
- Langchain is very extensible and allows you to leverage LLMs in different ways beyond this simple application, including enriching data from other sources, keeping a chat history to be able to have full conversations and more

If you are interested in leveraging Airbyte to ship data to your LLM-based applications, take a moment to [fill out our survey](https://docs.google.com/forms/d/e/1FAIpQLSduobMZwbqiFlPxsWDG-hrBw6NLYMDu_7zRfo4j7AsaO1QtfQ/viewform?usp=sf_link&amp;ref=blog.langchain.com) so we can make sure to prioritize the most important features.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)