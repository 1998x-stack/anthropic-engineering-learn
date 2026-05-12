---
title: "LangSmith for the full product lifecycle: How Wordsmith quickly builds, debugs, and evaluates LLM performance in production"
author: "LangChain Accounts"
date: "2024-07-09"
url: "https://www.langchain.com/blog/customers-wordsmith"
---

Case StudiesLangSmithObservability &amp; Evals

# LangSmith for the full product lifecycle: How Wordsmith quickly builds, debugs, and evaluates LLM performance in production

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 8, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf96e51c6ccf78734fd0_WordSmith.png)[Wordsmith](https://link.wordsmith.ai/Rp33gza?ref=blog.langchain.com) is an AI assistant for in-house legal teams, reviewing legal docs, drafting emails, and generating contracts using LLMs powered by the customer’s knowledge base. Unlike other legal AI tools, Wordsmith has deep domain knowledge from leading law firms and is easy to install and use. It integrates seamlessly into email and messaging systems to automatically draft responses for the legal team, mimicking what it’s like to work with another person on the team.

Having experienced an exponential growth in LLM-powered features over the past few months, WordSmith’s engineering team needed better visibility into LLM performance and interactions. [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) has been vital to understanding what’s happening in production and measuring experiment impact on key parameters. Below, we’ll walk through how LangSmith has provided value at each stage of the product development life cycle.

## **Prototyping &amp; Development: Wrangling complexity through hierarchical tracing **

Wordsmith’s first feature was a configurable RAG pipeline for Slack. It has now evolved to support complex multistage inferences over a wide variety of data sources and objectives. Wordsmith ingests Slack messages, Zendesk tickets, pull requests, and legal documents, delivering accurate results over a heterogeneous set of domains and NLP tasks. Beyond just getting the right results, their team needed to optimize for cost and latency using LLMs from OpenAI, Anthropic, Google, and Mistral.

LangSmith has become crucial to Wordsmith&#x27;s growth, enabling engineers to work quickly and confidently. With its foundational value-add as a tracing service, LangSmith helps the Wordsmith team transparently assess *what the LLM is receiving and producing* at each step of their complex multi-stage inference chains. The hierarchical organization of inferences lets them quickly iterate during the development cycle, far faster than when they relied solely on Cloudwatch logs for debugging.

Consider the following snapshot of an agentic workflow in which GPT-4 crafts a bad Dynamo query:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf98e51c6ccf78734fef_AD_4nXcxgwuGhoEbGtGWMS72jVZNsJuTRvbyHNIILhpnkgRe80RQx3vq9RnLnpYvt2XuAKW-99hDEuvOOiEAfFbYzjcQ219Hg3ZVIZrWKqhFSssGSnjZmTxKA7svTKpG9jbeJuRZNQmSBW9RbNERtlyMrhUKwszE.png)Invalid Dynamo query in an agentic workflow

These workflows can contain up to 100 nested inferences, making it time-consuming and painful to sift through general logs to find the root cause of an errant response. With LangSmith’s out-of-the-box [tracing](https://docs.smith.langchain.com/concepts/tracing?ref=blog.langchain.com) interface, diagnosing poor performance at an intermediate step is seamless, enabling much faster feature development.

## **Performance Measurement: Establishing baselines with LangSmith datasets**

Reproducible measurement helps differentiate a promising GenAI demo from a production-ready product. Using LangSmith, Wordsmith has published a variety of evaluation sets for various tasks like RAG, agentic workloads, attribute extractions, and even XML-based changeset targeting — facilitating their deployment to production.

These static evaluation sets provide the following key benefits:

- Eval sets crystalize the requirements for Wordsmith’s feature. By forcing the team to write a set of correct questions and answers, they set clear expectations and requirements for the LLM.
- Eval sets enable the engineering team to iterate quickly and with confidence. For example, when Claude 3.5 was released, the Wordsmith team was able to compare its performance to GPT-4o within an hour and release it to production the same day. Without well-defined evaluation sets, they would have to rely on ad-hoc queries, lacking a standard baseline to confidently assess if a proposed change improved user outcomes.
- Eval sets let the Wordsmith team optimize on cost and latency with accuracy as the key constraint. Task complexities are not uniform, and using faster and cheaper models where possible has reduced cost on particular tasks by up to 10x. Similar to (2), this optimization would be time-consuming and error-prone without a predefined set of evaluation criteria.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf97e51c6ccf78734fdd_AD_4nXeSucMnovSrs1Naa3Unc8ETGBDvShbWn3i5yhibYRho5-OZDZ4HrHEv_MOu9SL58ipHOjahSUyr94E2CKoqWZ6uCqYrpupxDaXkAnwad1z2KFra18wnCZ7FI1N6SUFkrTc6lDLpif-EIcGcR9TLJDuV_UfH.png)Tracking the accuracy of an agentic workflow over time

## **Operational Monitoring: Rapid debugging via LangSmith filters**

The same visibility features that make LangSmith ideal for development also make it a core part of Wordsmith’s online monitoring suite. The team can immediately link a production error to its LangSmith trace, reducing time to debug an inference from minutes to seconds by simply following a LangSmith URL instead of perusing logs.

LangSmith’s indexed queries also make it easy to isolate production errors related to inference issues:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf97e51c6ccf78734fe2_AD_4nXd48xCJw3Prd6P4UBKdywx1UcBrQn2SxLrJAFR9Z7hxIBGmistmdbFfvHqVIZsTtvsaT3onPNvBlNHxlz89IlCUcjOF8jtmnn0TPsZr-pe9QT4dUu0mxu-MiCw2_pBwdgyQqlCcL0cnmMxSuJlZkt5JyBFU.png)What’s breaking in prod? LangSmith makes it easy to isolate issues

## **Online Experimentation: Enabling experiment analyses via tags**

Wordsmith uses [Statsig](https://www.statsig.com/?ref=blog.langchain.com) as their feature flag / experiment exposure library. Leveraging LangSmith tags, it’s simple to map each exposure to the appropriate tag in LangSmith for simplified experiment analyses.

A few lines of code are all it takes for us to associate each experiment exposure to an appropriate LangSmith tag:

def get_runnable_config() -&gt; RunnableConfig:
        llm_flags = get_all_llm_features() # fetch experiments from Statsig
        return {
            &quot;metadata&quot;: {
                &quot;env&quot;: ENV,
            },
            &quot;tags&quot;: [f&quot;{flag}:{value}&quot; for (flag, value) in llm_flags.items()] + [ENV], # associate experiments with inferences
        }

In LangSmith, these exposures are queryable via tags, allowing for seamless analysis and comparison between experiment groups:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf98e51c6ccf78734ff8_AD_4nXe8WKf5764pEUlI14Q5xLxvxjN_K_aCZ11c7B4qIdF9fKvEvHudYBzxyaMnwvpiPjFNG-WX8U7_VQxNaD6aO026_jo-VdGkYFqiIu95osCh9uRbgY4h6c_r6pstXMicxJNeEPRRCn0tLld71xFRr0DgNZE.png)Test![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf98e51c6ccf78734ff3_AD_4nXeBoB_p8H7GMmin9F7gY_yfNqcnojn9Qeh9cvhW_FNLkQMtss1-_XpBtQ_6fYJ7qzaNRITYkcaAub3bbg5JLKsVeCJnrTjQA4B6rY0R3ttvopUBKvh2b2xpboLF5Ea3g2heIwwSOLF2InIvw3q2L_2X_T_F.png)Comparison

Using basic filters, they can fetch all experiment exposures in LangSmith, save them to a new dataset, and export the dataset for downstream analysis. LangSmith thus plays a crucial role in the Wordsmith product’s iterative experimentation and improvement.

## **What’s Next: Customer-specific hyperparameter optimization**

At each stage of the product life cycle, LangSmith has enhanced the Wordsmith team’s speed and visibility into the quality of their product. Moving forward, they plan to integrate LangSmith even more deeply into the product life cycle and tackle more complex optimization challenges.

Wordsmith’s RAG pipelines contain a broad and ever-increasing set of parameters that govern how the pipelines work. These include embedding models, chunk sizes, ranking and re-ranking configurations, etc. By mapping these hyperparameters to LangSmith tag (using a similar technique to their online experimentation), Wordsmith aims to create online datasets to optimize these parameters for each customer and use case. As datasets grow, they envision a world in which each customer’s RAG experience is automatically optimized based on their datasets and query patterns.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

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