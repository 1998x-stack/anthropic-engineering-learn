---
title: "LangChain &lt;&gt; MongoDB Atlas"
author: "LangChain Accounts"
date: "2023-06-22"
url: "https://www.langchain.com/blog/langchain-x-mongodb-atlas"
---

Partner

# LangChain &lt;&gt; MongoDB Atlas

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 22, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb2112c87c962360d6df8_mongo.webp)Today we’re announcing LangChain’s integration with MongoDB Atlas, adding support for one of the most popular developer data platforms in the world. This is an integration so anticipated that a few developers added the integration before we were ready to announce it :)

### Overview

One of the key components of AI powered applications is semantic search powered by embeddings and vector stores. Semantic Search is a capability that allows you to query your data based on its meaning rather than the data itself.  This is made possible by being able to represent any form of data numerically as a Vector which can then be compared to one another through sophisticated algorithms.

While building semantic search capabilities in your production application, vector stores will need to work in conjunction with an application database. One of the largest pain points associated with having a separate vector search engine from your application database is the added complexity around syncing the data between these systems and managing the additional infrastructure. And this doesn’t even include the challenges around security and compliance as you get ready for selling to enterprises.  All of this adds friction to both the process of building applications as well as the work to manage and maintain them in production.

### **MongoDB Atlas - The Developer Data Platform**

MongoDB Atlas was released in 2016 to provide a cloud native, fully managed database service offering, helping developers build applications faster than ever before.  Over the years, Atlas has grown into a full fledged developer data platform, satisfying workloads from transactional to search to analytical and streaming.  MongoDB Atlas is a battle-tested platform that provides for high availability, horizontal and vertical scale out, and world class security.  And now it is thrilled to add native support for vectors in the form of Atlas Vector Search to streamline building the next generation of applications.

### **Introducing Atlas Vector Search**

Atlas Vector Search is natively built into MongoDB Atlas, so you don’t need to copy and transform your data, learn some new stack and syntax, or manage a whole new set of infrastructure.  Atlas Vector Search allows you to store your vector embeddings right alongside your operational data, dynamically update your vector entries when your data changes using Atlas Triggers, and your application only needs to interact with a single query interface. This drastically reduces the overhead of adding support for vector search and you can utilize these powerful new capabilities all within a world class and battle tested platform to build applications faster than ever before.

Sign up for Atlas [here](https://www.mongodb.com/pricing?ref=blog.langchain.com) with our Free Forever Tier

### **LangChain and MongoDB Atlas**

LangChain and MongoDB Atlas are a natural fit, and it’s been demonstrated by the organic community enthusiasm which has led to several integrations in LangChain for MongoDB.  In addition to now supporting Atlas Vector Search as a Vector Store there is already support to utilize MongoDB as a chat log history.

Both LangChain and MongoDB are keenly focused on developer productivity with both our core missions centralized around ensuring an amazing developer experience.

With today’s announcement you can head over to MongoDB Atlas, setup Vector Search, and then connect LangChain and start prompting!  To simplify your first time setup, we’ve added some pre-embedded data (using text-embedding-ada-002 from Open AI) to our [MongoDB Atlas sample data](https://www.mongodb.com/developer/products/atlas/atlas-sample-datasets/?ref=blog.langchain.com) (sample_mflix.embedded_movies), so it’s as easy as loading the sample data, defining a vector index, and start finding those neighbors with our approximate nearest neighbors algorithm.

### **The Future**

We are extremely excited about this new capability, but it is just the beginning!  The MongoDB team is going to be moving fast in this space and we’ll be making some additional announcements in the coming months to further evolve this capability.  Most importantly though we are extremely excited to stay engaged with the community to ensure we’re providing the capabilities you need, so don’t be a stranger!

A big thank you and shout out to @P-E-B who kicked off the Python implementation and @floomby who started the JavaScript support!

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