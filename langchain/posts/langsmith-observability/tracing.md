---
title: "Tracing"
author: "LangChain Accounts"
date: "2023-01-30"
url: "https://www.langchain.com/blog/tracing"
---

LangSmithObservability &amp; Evals

# Tracing

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 29, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb26fba9d0fc723784452_photo-1644088379091-d574269d422f.jpeg)We’re excited to announce native tracing support in LangChain! By enabling tracing in your LangChain runs, you’ll be able to more effectively visualize, step through, and debug your chains and agents.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb26fba9d0fc723784461_explore.png)A view of a more complicated trace at a high level

## Motivation

Reasoning about your chain and agent executions is important for troubleshooting and debugging. However, it can be difficult for complex chains and agents, for a number of reasons:

- There could be a high number of steps, making it hard to keep track of all of them
- The sequence of steps could not be fixed, and could vary based on user input
- The inputs/outputs at each stage may not be long and deserve more detailed inspection

Each step of a chain or agent might also involve nesting — for example, an agent might invoke a tool, which uses an `LLMMathChain`, which uses an `LLMChain`, which then invokes an `LLM`. If you notice strange or incorrect output from a top-level agent run, it is difficult to determine exactly where in the execution it was introduced.

Tracing solves this by allowing you to clearly see the inputs and outputs of each LangChain primitive involved in a particular chain or agent run, in the order in which they were invoked.

There has been some great work already for tracing and visualization for LLM compositions (see [ICE](https://github.com/oughtinc/ice?ref=blog.langchain.com) and [langchain-visualizer](https://github.com/amosjyng/langchain-visualizer?ref=blog.langchain.com)), and we’re now excited to incorporate tracing natively in LangChain. We hope to release new and exciting features that build upon tracing in the near future.

## Usage

As a starting point, we’re allowing everyone to leverage tracing in their LangChain compositions by using a locally hosted setup spun up by docker-compose. We’re also rolling out a hosted version to a small initial group of users. If you are interested in getting access to this, please fill out [this form](https://docs.google.com/forms/u/5/d/e/1FAIpQLScoDu0bJ5cGrlSJvbMW-LgPkq70ewiuBBpMCZgmwtJ3Iz-NLw/viewform?usp=send_form&amp;ref=blog.langchain.com).

For full technical documentation on how to get started, please see [here](https://langchain.readthedocs.io/en/latest/tracing.html?ref=blog.langchain.com).

We hope to continuously iterate on this to make it as useful as possible. Please reach out with any feedback!

## Up Next

We’re just getting started with tracing and additional features. In the future we hope to add:

- UI improvements
- Better filtering and grouping of traces
- Logging the full serialized `LLM` and `Chain` for each run
- Other exciting features we’re still fleshing out ;)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)