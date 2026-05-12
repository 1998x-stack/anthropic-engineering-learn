---
title: "RAG-Powered Mechanic Assistant: How-To Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/oilyrags-building-a-rag-powered-mechanic-assistant-with-ai"
category: "rag"
---

Content



- [ The Concept  ](#the-concept)
- [ Focus Market: Marine Industry  ](#focus-market-marine-industry)
- [ The Problem  ](#the-problem)
- [ The Solution  ](#the-solution)
- [ How It Works  ](#how-it-works)
- [ Real World Impact  ](#real-world-impact)
- [ Technical Implementation  ](#technical-implementation)
- [ Observability &amp; Evaluation  ](#observability-and-evaluation)
- [ Next Steps  ](#next-steps)
- [ Takeaways  ](#takeaways)
- [ Where to Find Me  ](#where-to-find-me)



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







 *This is a guest post by Jeff Davis, one of the winners of our recent hackathon.*







 I recently participated in LlamaIndex&#39;s hackathon at 500 Global HQ in Palo Alto, California. This &quot;RAG-A-THON&quot; event focused on building agentic RAG systems. My project &quot;OilyRAGs&quot; ended up taking third place at the event, and I want to share some details about how I built this prototype.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  The Concept



 OilyRAGs is an AI mechanic assistant catalog for mechanics by mechanics. The aim is to accelerate customer service, mechanical maintenance, and repetitive operational tasks with artificial intelligence and machine learning. Essentially, OilyRAGs is a catalog of public, private, and manufacturer sponsored RAG applications.



 The market potential is massive: there are 1.4 billion autos (cars, trucks, buses) worldwide, billions of aircraft, billions of watercraft, and billions of appliances including refrigerators, washing machines, dryers, dishwashers, etc. There are also hundreds of millions of small engine devices, including tractors, loaders, forklifts and lawnmowers.



###  Focus Market: Marine Industry



 For the prototype, I focused on boats.



 This is a $50+ billion market alone. Recreational boating and fishing was the number one contributor to the $689 billion outdoor recreation industry in 2020, according to the US Department of Commerce&#39;s Bureau of Economics Analysis.



##  The Problem



 To understand the pain points, consider a boat mechanic&#39;s typical workflow when encountering an engine model number like &quot;P0006B051FW20A&quot; for a PCM engine:


-  Crawl into the engine compartment (requiring contortionist-level flexibility)
  -  Write down the number on scratch paper
  -  Climb down from the boat
  -  Walk to the computer room at the far side of the building
  -  Pull up a PDF
  -  Decipher the model number
  -  Look up corresponding parts for maintenance tasks



 This can take considerable time and isn’t the best use of a mechanic’s abilities.



##  The Solution



 OilyRAGs uses LlamaIndex to create a RAG-enabled chatbot with a multimodal hands-free interface. The mechanic can use their phone to decipher model numbers, diagnose problems and make simple queries without leaving the boat, such as:



 &quot;List all the parts and part numbers needed to perform a 50 hour service on a 2020 PCM 06.2 L DI, PEG 90A E, 2.0:1, return, A&quot;



 Using the application not only provides a standard output which is better all around, it is 6,000% faster - an order of magnitude of improvement rarely seen in innovation.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/6bd3eb7c0850a3ab8ae3f2b6ac2435841d74aa18-1920x1080.png)

##  How It Works



 The backend implementation uses LlamaIndex to build a RAG pipeline which is interfaced by a chatbot paired with a LlamaIndex workflow. This enables an AI agent to pass information to another AI agent which generates a report. The output is a digital form with checkboxes that allows mechanics to track their progress on their phone.



 The form includes:


-  Engine model number
  -  Deciphered characteristics
  -  Parts numbers associated with each required service item
  -  Space for notes (visible only to the marina)
  -  Digital signature and date
  -  PDF export capability



 All data is stored digitally and can be referenced by the RAG system for future queries. This eliminates 100% of carbon waste, removes issues with illegible handwriting and oily fingerprints, and creates easily shareable documentation.



##  Real World Impact

  ![](https://cdn.sanity.io/images/7m9jw85w/production/246f4a6fd36f475c35e56acb8092ca4501556824-1920x1080.png)

 As a Service Mechanic at a local marina noted: &quot;Using AI for repetitive tasks is a game changer. It makes completing time-sucking tasks exponentially faster.&quot;



 In the boat service industry, where oil changes cost $300 for customers and mechanics are paid $30 per hour, OilyRAGs creates benefits for everyone:


-  Mechanics become more efficient
  -  Marinas increase throughput
  -  Manufacturers/Suppliers sell more parts
  -  Customers receive faster service



 It&#39;s a win-win-win-win scenario where mechanics, marinas, manufacturers, and boat owners all benefit.



##  Technical Implementation



 The application was built using LlamaIndex for several key components:



python






```
# Storage
from pinecone import Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import SimpleDirectoryReader, StorageContext, Document, VectorStoreIndex, set_global_handler, Settings

# RAG
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore

# LLM
from llama_index.llms.openai import OpenAI

# Workflow
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    Event,
)

# Workflow Graph
from llama_index.utils.workflow import draw_all_possible_flows

# Embeddings
from llama_index.embeddings.openai import OpenAIEmbedding
```


##  Observability &amp; Evaluation

  The system includes observability using LlamaTrace with Arize Phoenix:



python






```
llama_index.core.set_global_handler(
    "arize_phoenix", project_name="oilyrags", endpoint="https://llamatrace.com/v1/traces"
)
```


##  Next Steps

  The validation of interest in OilyRAGs by the marine industry service providers demonstrates the potential for expansion into other mechanical sectors. Looking ahead, I plan to:


-  Implement a continuous feedback hands-free mode for the mechanics using the chatbot
  -  Expand offerings to cover even more niche vehicles and engines
  -  Develop predictive maintenance features using machine learning
  -  Scheduling and notification features for boat owners and service providers
  -  Partner with manufacturers for sponsored RAG applications
  -  Partner with suppliers for seamless ordering within the app



##  Takeaways



 This RAG-A-THON project demonstrates how LlamaIndex can be used to create practical, impactful solutions that transform traditional industries through the power of RAG and AI agents.The ability to implement so many key technical features using LlamaIndex is so powerful, fast, and reduces exposure to inconsistent code bases across multiple projects.



 If you have questions on implementation of an agentic RAG or are looking to develop one for your business, let’s talk!



##  Where to Find Me



 If you&#39;re interested in investing, partnering, or want to learn more about OilyRAGs development, [connect with me on LinkedIn](https://linkedin.com/in/tahoedesigner). I&#39;m particularly interested in connecting with:


-  Investors
  -  Marina Operators
  -  Boat Owners



 Let&#39;s work together to bring AI-powered efficiency to mechanical maintenance across industries!