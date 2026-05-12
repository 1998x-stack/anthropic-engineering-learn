---
title: "Mixtral 8x7B Local Setup Guide With Ollama | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/running-mixtral-8x7-locally-with-llamaindex-e6cebeabe0ab"
category: "llamaindex-core"
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



   17



You may have heard the fuss about the latest release from European AI powerhouse [Mistral AI](https://mistral.ai/): it’s called Mixtral 8x7b, a “mixture of experts” model — eight of them, each trained with 7 billion parameters, hence the name. Released originally as a [mic-drop tweet](https://twitter.com/MistralAI/status/1733150512395038967) they followed up a few days later with a [blog post](https://mistral.ai/news/mixtral-of-experts/) that showed it matching or exceeding GPT-3.5 as well as the much larger Llama2 70b on a number of benchmarks.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



Here at LlamaIndex we’re naturally fans of open source software, so open models with permissive licenses like Mixtral are right up our alley. We’ve had a few questions about how to get Mixtral working with LlamaIndex, so this post is here to get you up and running with a totally local model.

# Step 1: Install Ollama

Previously getting a local model installed and working was a huge pain, but with the release of [Ollama](https://ollama.ai/), it’s suddenly a snap! Available for MacOS and Linux (and soon on Windows, though you can use it today on Windows via [Windows Subsystem For Linux](https://learn.microsoft.com/en-us/windows/wsl/install)), it is itself open source and a [free download](https://ollama.ai/download).

Once downloaded, you can get Mixtral with a single command:

ollama run mixtralThe first time you run this command it will have to download the model, which can take a long time, so go get a snack. Also note that it requires a hefty 48GB of RAM to run smoothly! If that’s too much for your machine, consider using its smaller but still very capable cousin **Mistral 7b**, which you install and run the same way:

ollama run mistralWe’ll assume you’re using Mixtral for the rest of this tutorial, but Mistral will also work.

Once the model is running Ollama will automatically let you chat with it. That’s fun, but what’s the point of having a model if it can’t work with your data? That’s where LlamaIndex comes in. The next few steps will take you through the code line by line, but if you’d prefer to save all the copying and pasting, all of this code is available in an [open-source repo](https://github.com/run-llama/mixtral_ollama) that you can clone to follow along there.

# Step 2: Install your dependencies

You’re going to need LlamaIndex installed, obviously! We’ll also get you going with a handful of other dependencies that are about to come in handy:

pip install llama-index qdrant_client torch transformers

# Step 3: Smoke test

If you’ve got Ollama running and LlamaIndex properly installed, the following quick script will make sure everything is in order by asking it a quick “smoke test” question in a script all by itself:

# Just runs .complete to make sure the LLM is listening
from llama_index.llms import Ollama

llm = Ollama(model="mixtral")
response = llm.complete("Who is Laurie Voss?")
print(response)

# Step 4: Load some data and index it

Now you’re ready to load in some real data! You can use any data you want; in this case I’m using a [small collection of my own tweets](https://www.dropbox.com/scl/fi/6sos49fluvfilj3sqcvoj/tinytweets.json?rlkey=qmxlaqp000kmx8zktvaj4u1vh&amp;dl=0) which you can download, or use your own! We’re going to be storing our data in the nifty, open source [Qdrant](https://github.com/qdrant/qdrant) vector database (which is why we got you to install it earlier). Create a new python file, and load in all our dependencies:

from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStoreThen load our tweets out of our JSON file using a nifty JSONReader from [LlamaHub](https://llamahub.ai/l/file-json?from=all), our convenient collection of open source data connectors. This will give you a pile of documents ready to be embedded and indexed:

JSONReader = download_loader("JSONReader")
loader = JSONReader()
documents = loader.load_data(Path('./data/tinytweets.json'))Get Qdrant ready for action by initializing it and passing it into a Storage Context we’ll be using later:

client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")
storage_context = StorageContext.from_defaults(vector_store=vector_store)Now set up our Service Context. We’ll be passing it Mixtral as the LLM so we can test that things are working once we’ve finished indexing; indexing itself doesn’t need Mixtral. By passing `embed_model="local"`we’re specifying that LlamaIndex will embed your data locally, which is why you needed `torch` and `transformers`.

llm = Ollama(model="mixtral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")Now bring it all together: build the index from the documents you loaded using the service and storage contexts you already set up, and give it a query:

index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What does the author think about Star Trek? Give details.")
print(response)Ollama will need to fire up Mixtral to answer the query, which can take a little while, so be patient! You should get output something like this (but with more details):

Based on the provided context information, the author has a mixed opinion about Star Trek.

# Verify our index

Now to prove it’s not all smoke and mirrors, let’s use our pre-built index. Start a new python file and load in dependencies again:

import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.llms import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStoreThis time we won’t need to load the data, that’s already done! We will need the Qdrant client and of course Mixtral again:

client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")

llm = Ollama(model="mixtral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")This time instead of creating our index from documents we load it directly from the vector store using `from_vector_store`. We’re also passing `similarity_top_k=20` to the query engine; this will mean it will fetch 20 tweets at a time (the default is 2) to get more context and better answer the question.

index = VectorStoreIndex.from_vector_store(vector_store=vector_store,service_context=service_context)
query_engine = index.as_query_engine(similarity_top_k=20)
response = query_engine.query("Does the author like SQL? Give details.")
print(response)

# Build a little web service

It’s no good having an index that just runs as a script! Let’s make an API out of this thing. We’ll need two new dependencies:

pip install flask flask-corsLoad in our dependencies as before into a new file:

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import qdrant_client
from llama_index.llms import Ollama
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
)
from llama_index.vector_stores.qdrant import QdrantVectorStoreGet the vector store, the LLM and the index loaded:

# re-initialize the vector store
client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)
vector_store = QdrantVectorStore(client=client, collection_name="tweets")

# get the LLM again
llm = Ollama(model="mixtral")
service_context = ServiceContext.from_defaults(llm=llm,embed_model="local")
# load the index from the vector store
index = VectorStoreIndex.from_vector_store(vector_store=vector_store,service_context=service_context)Set up a really basic Flask server:

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# This is just so you can easily tell the app is running
@app.route('/')
def hello_world():
    return 'Hello, World!'And add a route that accepts a query (as form data), queries the LLM and returns the response:

@app.route('/process_form', methods=['POST'])
@cross_origin()
def process_form():
    query = request.form.get('query')
    if query is not None:
        query_engine = index.as_query_engine(similarity_top_k=20)
        response = query_engine.query(query)
        return jsonify({"response": str(response)})
    else:
        return jsonify({"error": "query field is missing"}), 400

if __name__ == '__main__':
    app.run()Note those last two lines, they’re important! `flask run` is incompatible with the way LlamaIndex loads dependencies, so you will need to run this API directly like so (assuming your file is called `app.py`)

python app.pyWith your API up and running, you can use cURL to send a request and verify it:

curl --location '&amp;lt;http://127.0.0.1:5000/process_form&amp;gt;' \\
--form 'query="What does the author think about Star Trek?"'

# You’re done!

We covered a few things here:

- Getting Ollama to run Mixtral locally
- Using LlamaIndex to query Mixtral 8x7b
- Building and querying an index over your data using Qdrant vector store
- Wrapping your index into a very simple web API
- All open-source, free, and running locally!

I hope this was a fun, quick introduction to running local models with LlamaIndex!