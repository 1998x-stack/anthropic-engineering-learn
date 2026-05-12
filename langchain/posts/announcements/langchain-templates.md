---
title: "LangChain Templates"
author: "LangChain Accounts"
date: "2023-10-31"
url: "https://www.langchain.com/blog/langchain-templates"
---

Agent ArchitectureTutorials &amp; How-Tos

# LangChain Templates

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 31, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0f9394beb695265cded_Screenshot-2023-10-29-at-2.40.54-PM.png)Today we&#x27;re excited to announce the release of LangChain Templates. LangChain Templates offers a collection of easily deployable reference architectures that anyone can use. We&#x27;ve worked with some of our partners to create a set of easy-to-use templates to help developers get to production more quickly. We will continue to add to this over time. This is a new way to create, share, maintain, download, and customize chains and agents. They are all in a standard format with allows them to easily be deployed with [LangServe](https://github.com/langchain-ai/langserve?ref=blog.langchain.com), allowing you to easily get production-ready APIs and a playground for free.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0fa394beb695265ce0f_Screenshot-2023-10-29-at-2.38.36-PM.png)

## **Key Links**

[**Quick Start**](https://github.com/langchain-ai/langchain/blob/master/templates/README.md?ref=blog.langchain.com)**: Go here for a guide on how to get started with LangChain Templates.**

[**YouTube Walkthrough**](https://youtu.be/aA6KZ4L_ono?ref=blog.langchain.com)**: We filmed a quick walkthrough of how to use LangChain Templates.**

[**LangSmith**](https://smith.langchain.com/?ref=blog.langchain.com)**: LangChain Templates seamlessly integrate with LangSmith - our logging and debugging tool. **[**Sign up here**](https://smith.langchain.com/?ref=blog.langchain.com)**.**

[**Hosted LangServe**](https://airtable.com/app0hN6sd93QcKubv/shrAjst60xXa6quV2?ref=blog.langchain.com)**: We will be releasing a hosted version of LangServe for one-click deployments of LangChain applications. **[**Sign up here**](https://airtable.com/app0hN6sd93QcKubv/shrAjst60xXa6quV2?ref=blog.langchain.com)**.**

## Additional Resources

[**Featured Templates**](https://github.com/langchain-ai/langchain/blob/master/templates/docs/INDEX.md?ref=blog.langchain.com)**: Explore the many templates available to use - from advanced RAG to agents.**

[**All Templates**](https://github.com/langchain-ai/langchain/tree/master/templates?ref=blog.langchain.com)**: Explore all templates available.**

[**Contributing**](https://github.com/langchain-ai/langchain/blob/master/templates/docs/CONTRIBUTING.md?ref=blog.langchain.com)**: Want to contribute your own template? It&#x27;s pretty easy! These instructions walk through how to do that.**

[**LangServe**](https://github.com/langchain-ai/langserve?ref=blog.langchain.com)**: Learn more about the best way to deploy LangChain chains and agents.**

[**LangServe Webinar**](https://www.crowdcast.io/c/zcl2p0y0wrvd?ref=blog.langchain.com)**: We will be doing a webinar this Thursday to discuss more about LangServe and LangChain Templates. Register **[**here**](https://www.crowdcast.io/c/zcl2p0y0wrvd?ref=blog.langchain.com)**.**

## Motivation

What was our motivation LangChain Templates? These templates can be either chains or agents, and represent a full-features *context-aware reasoning applications*. Over time we&#x27;ve seen:

- Developers want to create **many different types** of applications
- Developers want to better **understand** internals of applications
- Developers want to **modify** internal of applications
- Developers want an **easy way to deploy** application

### Developers want to create many different types of applications

We&#x27;ve recently seen a proliferation of chains and agents being added to LangChain. There are a few different flavors:

- Tool specific chains
- Language model specific chains
- New architectures

It&#x27;s natural that all these types of chains are added, and says something about the current state of the field.

**Tool Specific Chains**

We are seeing a lot of chains/agents aimed at best interacting with particular tools. This is consistent with what we know about language models: they are fantastic generalists, so of course it makes sense that we would want to use with different tools. The exact chain/agent that makes the most sense for one particular tool may actually differ subtly from another

**Language Model Specific Chains**

We are seeing that not all language models are interchangeable for all tasks. At the most obvious level, they may require different prompts. But they may also require different output parsing, maybe even slightly different context to be provided.

**New Architectures**

We are seeing new architectures emerge for how best to build applications. We will discuss this in a future post. This implies the field is still very early and people are trying to figure out how best to work with language models.

This had lead to a proliferation of chains and agents getting contributed to LangChain. We realized a while ago we couldn&#x27;t accept every possible variation (or LangChain would become incredibly bloated). We started moving more and more to cookbooks, but those aren&#x27;t as discoverable or as usable.

### Developers want to understand internals of applications

While it&#x27;s convenient to have an entire chain wrapped up in a class, it does obfuscate what exactly is going on inside. We&#x27;ve introduced [LangSmith](https://smith.langchain.com/o/ebbaf2eb-769b-4505-aca2-d11de10372a4/?ref=blog.langchain.com) to help with debugging and observability, and while that helps it&#x27;s not the same as being able to easily see that code.

### Developers want to modify internals of applications

We&#x27;ve seen a lot of developers wanting to modify the internals of chains. This could be changing some of the orchestration, changing some of the context loading, changing some of the prompts. This is extremely related to the first point.

As such we&#x27;ve seen a lot of people fork LangChain and modify the code internally. Some of them open up a PR with more minor changes for prompts/output parsers. This raises an interesting challenge for us though: it&#x27;s extremely tough to evaluate language model applications, so even though these prompt/output parser changes may be helpful for one person&#x27;s application, we&#x27;re hesitant to merge these in for fear that it may affect some other unsuspecting user.

### Developers want an easy way to deploy chains

There are two drivers here.

One driver: we see that one of the things that successful teams do is deploy an application quickly, to gather user interaction data. This user interaction data is useful for many purposes.

- First: are people even interacting with it? If no, then that may imply this particular product/feature does not have product market fit and you&#x27;d want to investigate that.
- Second: how are people using? If they are using it in unexpected ways, that may change some of the focus for development.
- Third: where is the chain not performing well? It&#x27;s often tough to now how exactly to improve the chain without seeing concrete datapoints on where is performing well.

Therefore, the faster we can allow teams to deploy their applications, the quicker they can iterate.

A second driver: a lot of organizations typically have not deployed Python applications in their infrastructure, and are looking for a battle-tested way to do so.

## What are LangChain Templates

In response to the above, we began working on LangChain Templates. LangChain Templates offers a collection of easily deployable reference architectures that anyone can use. We have created a collection of end-to-end templates for creating different types of applications. These templates are in a standard format that makes them easy to deploy with LangServe. We&#x27;ve also exposed an easy way to create new projects and load templates in.

How you consume these modules? You can first create a project, which contains a folder for chains. You can then easily download a module into a that application project. You can easily inspect and modify a chain (since it is being downloaded, rather than `pip` installed). You can then deploy the whole project using `langserve`.

## What is in LangChain Templates

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0fa394beb695265ce15_Screenshot-2023-10-29-at-2.42.18-PM.png)

One of the things that we are most excited about with LangChain Templates is that it enables us to much more easily add a variety of chains and agents. Some of the ones we&#x27;re particularly excited by:

**OSS Models**

We&#x27;ve heard a lot that LangChain seems OpenAI-centric. That is not our intention, but it is true that the default prompts for most chains are designed to work will with OpenAI. With LangChain Templates, we&#x27;re incredibly excited to be able to add templates that work best for other models - especially open source. We&#x27;ve already added some for [RAG](https://github.com/langchain-ai/langchain/tree/master/templates/rag-chroma-private?ref=blog.langchain.com) and [SQL-question-answering](https://github.com/langchain-ai/langchain/tree/master/templates/sql-ollama?ref=blog.langchain.com), and we&#x27;re excited to add more.

**Advanced RAG**

There are a lot of different methods and algorithms for advanced RAG, and we&#x27;re excited to be able to highlight them more properly. We&#x27;ve added templates for all the papers we highlighted last week in our blog post on [Query Transformations](https://blog.langchain.com/query-transformations/). We&#x27;ve also worked with partners to take some of the heuristics we&#x27;ve developed (like [Parent Document Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/parent_document_retriever?ref=blog.langchain.com)) and get them to work with their database - see the [Neo4J Parent Document Retriever](https://github.com/langchain-ai/langchain/tree/master/templates/neo4j-parent?ref=blog.langchain.com) template.

**Use Case Specific Chains**

We hope this opens the path for highlighting more and more use case specific chains. For example, we worked with [Sphinx Bio](https://www.sphinxbio.com/?ref=blog.langchain.com) to add a [template](https://github.com/langchain-ai/langchain/tree/master/templates/plate-chain?ref=blog.langchain.com) aimed at identifying coordinates of plate data within a messy Excel file. Something like this would have been too specific to include in the core LangChain package, but fits perfectly here.

## How does LangChain Templates solve the earlier problems?

Above we had listed out a few different problems we were observing. We think LangChain Templates goes a long way in addressing these problems.

**Developers want to create many different types of applications**

By adding templates for chains and agents in this format, we are no longer putting them in LangChain which should prevent bloat. This is also more organized and easier to work with than cookbooks.

**Developers want to better understand internals of applications**

By downloading chains (rather than `pip` - installing) the source code for chains and agents is right in your application. That makes it easy to inspect it.

**Developers want to modify internal of applications**

Again, by downloading chains (rather than `pip` - installing) the source code for chains and agents is right in your application. That makes it easy to modify it.

**Developers want an easy way to deploy applications**

All templates are in a standard format which makes it easy to deploy them with LangServe.

## Conclusion

The goal of LangChain is to make it as easy as possible for developers to build context-aware reasoning applications. We believe this is a big step in that direction. We&#x27;re incredibly grateful to our partners who have helped provide initial templates, and we look forward to working with the community to add more!

Big thank you to:

- All our ecosystem partners who contributed templates
- Jason Liu for suggesting this method of adding templates
- Rajtilak Bhattacharjee for helping us with the `langchain-cli` package name
- All our community members who helped test this: Greg Kamradt, Ryan Brandt, Misbah Syed, Hai, Lucas Hänke de Cansino, Hamel Husain

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)