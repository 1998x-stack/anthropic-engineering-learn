---
title: "LangChain &lt;&gt; Unstructured"
author: "LangChain Accounts"
date: "2023-02-06"
url: "https://www.langchain.com/blog/langchain-unstructured"
---

PartnerLangChain

# LangChain &lt;&gt; Unstructured

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 5, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)1min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb269adb40d0919239f96_screen-shot-2023-02-05-at-11.32.11-pm.png)One of the core value props of LangChain is the ability to combine Large Language Models with your own text data. There are multiple ([four!](https://python.langchain.com/docs/modules/chains/document/?ref=blog.langchain.com)) different methods of doing so, and [many](https://langchain.readthedocs.io/en/latest/use_cases/question_answering.html?ref=blog.langchain.com) [different](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) applications this can power.

A step that sits upstream of using text data is the ability to get your data into a text form. This can be rather tricky due to the multitude of different formats that exist out there.

Enter... [unstructured.io](https://www.unstructured.io/?ref=blog.langchain.com).

Unstructured is a company with a mission of transforming natural language data from raw to machine ready. One of the main ways they do this is with an [open source Python package](https://github.com/Unstructured-IO/unstructured?ref=blog.langchain.com). This package as support for [MANY](https://github.com/Unstructured-IO/unstructured?ref=blog.langchain.com#document-parsing) different types of file extensions: `.txt`, `.docx`, `.pptx`, `.jpg`, `.png`, `.eml`, `.html`, and `.pdf` documents.

After playing around with Unstructured, we realized that by integrating with it we could easily start to build out first class support for loading documents of all types into a format that LangChains could work with. So we created the [Document Loaders module](https://python.langchain.com/docs/modules/data_connection/document_loaders/?ref=blog.langchain.com), a large part of which is powered by Unstructured.

There are currently two loaders that are powered by Unstructured. Both seem rather simple, but are quite powerful.

The first is the [UnstructuredFileLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/unstructured_file?ref=blog.langchain.com). This has a simple interface (you just pass it a file path) but under the hood Unstructured is doing a lot of smart logic to infer which data type it is (PDF, PowerPoint, image, etc) and extract text.

The second is the [DirectoryLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/how_to/file_directory?ref=blog.langchain.com). Again, this has a pretty simple interface: it takes only a path to a directory and an optional regex to glob for files against. But under the hood it is looping over all files and using the above UnstructuredFileLoader to load them. This makes it possible to load files of all types in a single call.

We&#x27;re incredibly excited to have made this integration with Unstructured. With their focus on transforming raw data into clean text, it makes it incredibly easy to combine language models with your data, no matter what form it is in.

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