---
title: "Catch production failures early with LangSmith Alerts"
author: "LangChain Accounts"
date: "2025-04-22"
url: "https://www.langchain.com/blog/langsmith-alerts"
---

LangSmithTutorials &amp; How-Tos

# Catch production failures early with LangSmith Alerts

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 22, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8cdd151f0038d5f492_Alerting-LangSmith.png)Great user experiences start with reliable applications. That’s why catching failures *before* they reach your users is key. To help you stay ahead, we’ve launched** Alerts in LangSmith— **making it easier to monitor your LLM apps and agents in real time.

We now support setting alerts based on key metrics like **error rate**, **run latency**, and **feedback scores**.

If you’re already sending production traces to LangSmith, you can [set up your first alert](https://docs.smith.langchain.com/observability/how_to_guides/alerts?ref=blog.langchain.com) today. New to tracing? [Get started with tracing](https://docs.smith.langchain.com/observability?ref=blog.langchain.com) in LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8ddd151f0038d5f49c_image.png)LangSmith Alerts Configuration

## Why proactive monitoring matters

Monitoring and alerting are critical for any production app— but LLM-powered applications bring unique challenges, which primarily fall into two categories:

### **Dependence on External Services:**

Agentic apps inherently rely on numerous dependencies — you might use one (or many) model providers and have a number of tools such as APIs, web search services, and databases available to your agent. Outages, rate limits, or increased latency from these dependencies can significantly degrade user experience. Proactive monitoring helps you identify these issues quickly.

### **Quality &amp; Correctness**

User experience isn&#x27;t just about speed; it&#x27;s also about the *quality* of the LLM&#x27;s output. LLMs don&#x27;t always behave predictably— small changes in prompts, models, or inputs can unexpectedly impact results.

Prompts that perform well in controlled evaluations can also sometimes regress in real-world scenarios due to differences in user interactions. Alerts based on feedback scores (from [user input](https://docs.smith.langchain.com/evaluation/how_to_guides/attach_user_feedback?ref=blog.langchain.com) or [online evaluations](https://docs.smith.langchain.com/observability/how_to_guides/online_evaluations?ref=blog.langchain.com#configure-llm-as-judge-evaluators)) provide an early warning system for these quality dips.

## LangSmith Alerts Overview

LangSmith supports alerting on the following metrics:

- **Error Count and Rate**
- **Average Latency**
- **Average Feedback Score**

For each alert metric, you can leverage a robust set of filters to focus on specific subsets of runs (e.g., filtering by model, tool call or run type).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8cdd151f0038d5f498_image-1.png)

You can then set an aggregation windows (5 or 15 minutes) and a threshold to tune the sensitivity of alerts.

The last step is integrating the alert into your existing workflows. We support alerts via PagerDuty or setting up a custom webhook (e.g., to send notifications directly to a Slack channel).

And thats it! [Check out our docs](https://docs.smith.langchain.com/observability/how_to_guides/alerts?ref=blog.langchain.com) to learn more and get started today with alerting in LangSmith.

## What&#x27;s Next?

Alerting is a key piece to any observability product. In the future, we will be adding:

- More types of alerts: run count and LLM token usage
- Change alerts that allow you to set a relative value to alert over (e.g. alert when latency spikes 25%)
- Alerts over custom time windows

If you have feedback or feature requests, let us know what you think by getting in touch with us through the [LangChain Slack Community](https://langchaincommunity.slack.com/?ref=blog.langchain.dev). If you’re not part of the Slack community yet, sign up [here](https://www.langchain.com/join-community?ref=blog.langchain.dev).

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