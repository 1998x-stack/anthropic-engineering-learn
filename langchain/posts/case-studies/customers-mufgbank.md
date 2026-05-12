---
title: "How MUFG Bank increased sales efficiency by 10x with LangChain"
author: "LangChain Accounts"
date: "2025-02-27"
url: "https://www.langchain.com/blog/customers-mufgbank"
---

Case StudiesLangChain

# How MUFG Bank increased sales efficiency by 10x with LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 26, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbade707bc92c96efb9595_MUFG-Case-study.png)MUFG Bank is Japan’s largest bank and one of the world&#x27;s leading financial institutions. They provide capital market solutions to major corporate clients and promote economic growth around the world.

## **Problem: Solving data overload for corporate sales **

In MUFG Bank&#x27;s Global Capital Markets Division, the FX &amp; Derivative Sales team faced a key challenge. FX &amp; Derivative Sales team members needed to gather and analyze vast amounts of corporate data in order to create compelling client presentations – from 10k reports, to market data, to financial disclosures. This was a time-consuming process and skill-dependent (with junior members often needing additional guidance and assistance), which limited efficiency.

To address these challenges, MUFG’s AI/ML team leveraged Generative AI (GenAI) to streamline data digestion and automate the creation of presentation materials. Their goal was to empower sales teams with rapid insights, reducing manual burden and ensuring more effective client interactions.

## **Solution: Using LangChain for retrieval and summarization**

To improve the FX &amp; Derivative Sales team’s client research process, the MUFG AI/ML team implemented two key steps:

### **1) Data extraction &amp; summarization**

Annual reports often spanned 100-200 pages, with only a fraction containing relevant insights for the sales teams. Using LangChain, MUFG developed a system to extract critical financial data efficiently – and they implemented fine-tuned prompt engineering and retrieval-augmented generation (RAG) to surface the most relevant sections for sales teams.

### **2) Automatically generate presentations**

The FX &amp; Derivative Sales teams required tailored presentations based on the extracted insights. To ensure the insights were actionable, the AI/ML team implemented few-shot prompting techniques and step-by-step guidance that helped FX &amp; Derivative Sales professionals – even those with limited experience – quickly analyze financial opportunities and provide structured recommendations.

This enabled sales teams to assess interest rate risks, identify potential FX derivative purchases, and suggest regional currency positioning strategies.

The production RAG application now serves as a knowledge-sharing tool for corporate sales teams, simplifying the search for internal documents and deal-making ideas.

## **Impact: Improving efficiency 10x in sales processes**

The adoption of LangChain-powered GenAI has yielded substantial improvements for MUFG’s corporate sales team. Specifically, the process of analyzing corporate client data and generating presentation materials has been **reduced** from several hours to just **3-5 minutes**.

Previously, only limited experienced sales personnel could manually generate insightful presentations. With the new system, hundreds of sales professionals can now access the same level of intelligence, leading to a **10x increase** in the number of corporate clients receiving tailored financial recommendations.

These efficiency gains have also begun converting into tangible business outcomes, with deal execution timelines shortening over the past six months.

## **Behind the scenes: How LangChain enabled MUFG’s success**

The MUFG AI/ML team benefited from the LangChain programming library in the following two phases:

**R&amp;D / PoC phase**

The MUFG AI/ML team chose the Python version of LangChain and built a simple chat and RAG app. LangChain is well integrated with Streamlit, allowing them to easily manage conversation history and implement interactive apps. This enabled them to quickly start experiments, gather feedback from the sales, and iterate on improvements. Furthermore, thanks to the Retriever interface, they were able to switch between several specific vector databases and search engines, allowing them to compare and validate the accuracy at a low implementation cost.

**Development / Production phase**

The MUFG team switched to the TypeScript version of LangChain for a more sustainable and secure application via Next.js. The interface was nearly identical to the Python version, ensuring a smooth transition. In addition, Runnable Lambda allowed them to dynamically change the content filter and target index on demand and enabled them to invoke it in their custom RAG chain.

## **What’s Next**

MUFG Bank plans to refine its GenAI applications by enhancing its evaluation metrics, exploring graph-based AI architectures or AI agents for complex reasoning tasks, and expanding its RAG-driven retrieval system to incorporate broader financial data sources.

By leveraging LangChain, MUFG continues to advance AI-driven sales intelligence, improving efficiency, scalability, and strategic decision-making for its global clientele.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)