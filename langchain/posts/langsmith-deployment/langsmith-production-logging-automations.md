---
title: "LangSmith: Production Monitoring &amp; Automations"
author: "LangChain Accounts"
date: "2024-04-02"
url: "https://www.langchain.com/blog/langsmith-production-logging-automations"
---

LangSmithTutorials &amp; How-TosObservability &amp; Evals

# LangSmith: Production Monitoring &amp; Automations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaApril 2, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff68232fce8d20e1f85_Production-Monitoring-and-Automations---Blog---without-graphic.png)**Key Links:**

- [**YouTube Walkthrough**](https://www.youtube.com/playlist?list=PLfaIDFEXuae0bYV1_60f0aiM0qI7e1zSf&amp;ref=blog.langchain.com)
- [**Sign up for LangSmith here**](https://smith.langchain.com/?ref=blog.langchain.com)

If 2023 was a [breakthrough year for LLMs](https://simonwillison.net/2023/Dec/31/ai-in-2023/?ref=blog.langchain.com), then 2024 is shaping up to be the year that a significant amount of LLM-powered applications make their way into production. From the [Elastic AI Assistant](https://blog.langchain.com/langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant/) to [CommandBar&#x27;s Copilot User Assistant](https://blog.langchain.com/langchain-partners-with-commandbar-on-their-copilot-user-assistant/) - more and more complex applications are shipping to production and providing real business value. Many of these applications use LangSmith to [test](https://docs.smith.langchain.com/evaluation?ref=blog.langchain.com) and [debug](https://docs.smith.langchain.com/tracing?ref=blog.langchain.com) their applications, and today we&#x27;re announcing a set of new features aimed at helping applications post production-deployment.

As an [AI Engineer](https://www.ai.engineer/worldsfair?ref=blog.langchain.com), your job doesn&#x27;t stop once an application is launched to production. Once it&#x27;s in production you start getting real user data flowing through the system, allowing you to try to answer all sorts of questions. How are people using it? Where is the application messing up? Where is it performing well? How can I improve my application based on this data? How can I start to build a [data flywheel](https://www.ai.engineer/worldsfair?ref=blog.langchain.com)?

In order to make it as easy as possible to address these questions, we&#x27;re releasing a new set of features around production logging and automations. *Production monitoring* allows you to more easily manually explore and identify your data, while *automations* allow you to start acting on this data in an automated way. Like all LangSmith features, these work whether you are using LangChain or not. In the rest of this blog, we will walk through what these features are. You can also check out our [YouTube Playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae0bYV1_60f0aiM0qI7e1zSf&amp;ref=blog.langchain.com) for video walkthroughs.

## Filtering

We&#x27;ve revamped our infrastructure and invested a lot in being able to support advanced filters. These advanced filters are **crucial** for being able to efficiently and thoroughly inspect your data. As a starting point, we support basic filtering of runs based on:

- **Latency:** can be used to identify runs that took an inordinate amount of time
- **Errors:** can be used to identify runs that hit a breaking error
- **Feedback:** can be used to identify runs that users identified as particularly good or bad
- **Metadata/Tags:** can be used to filter into subsets of runs based on their configuration
- **Full Text Search:** can be used to search for keywords

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1fa5_filter.png)

We also have added in a few more advanced forms of filtering. These include

**By Trace Attributes**: sometimes you may want to filter for runs based on attributes of the root run of the trace they are a part of. This is especially common when working with chains or agents, where there are multiple sub-runs that make up a larger trace. Oftentimes, you are only collecting feedback on the high level trace. You may want to look for particular types of sub-runs whose parent trace has positive or negative feedback. An example of this might be filtering for runs with name `&quot;ChatOpenAI&quot;` that in which the root run of the trace has a`user_score` equal to `0`.

**By Tree Attributes**: The reverse of the above. You may want to filter for root runs of traces that have a particular type of sub-run. This can be useful in identifying high level traces that called a particular tool, for example.

**AI Query**: Don&#x27;t know how to construct your trace in the UI? Type in what you want to search for in natural language and we will use an LLM to convert it to our filtering language! (Yes, we monitor this with LangSmith)

## Monitoring

Filtering is useful to be able to identify and look at individual datapoints. Oftentimes, you may want an even more birds eye view of what is happening. In the `Monitoring` tab you can view aggregate statistics over time. These statistics include LLM specific metrics like latency, time-to-first-token, cost, tokens, feedback, etc.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1fa2_monitoring.png)

One of the more advanced features here is that you can group runs by metadata attributes. What this means is that you add a metadata tag to runs representing a particular configuration. A concrete example of this is with [ChatLangChain](https://chat.langchain.com/?ref=blog.langchain.com), where we rotate between five different LLM providers. We insert as metadata a key tracking which LLM we chose. In LangSmith, you can then group the monitoring dashboards by this metadata key. This allows us to easily compare all those same stats (latency, feedback, etc) across the five different model providers.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1fae_subsets_monitor.png)

Another incredibly useful feature of these charts is that they are all interactive. What this means is that you can click into any particular point in the chart and that will bring you to the `Runs` page automatically filtered to only show datapoints in the timebin you just clicked on.

## Threads

The dominant UX for LLM applications is still chat. In chat applications, there is a back and forth between human messages and an AI response. Each AI response is a trace (and can consist of many sub-runs). With `Threads`, we&#x27;ve now introduced a way to view the whole back-and-forth of a conversation in a single view. This can be done by attaching a special metadata key to each trace with the unique identifier for that conversation. This makes it much easier to debug conversations as you can see the whole thread in one place.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1fab_convo.png)

## Automations

The previous features all make it easy to manually inspect datapoints. With `Automations`, you can now act upon datapoints of interest in an automated fashion.

Automations consist of three points: a filter, a sampling rate, and an action. The filter determines which subset of datapoints you want to act on. We talked about filters above, and we can reuse the same UI components to create an automation. After constructing the desired filter, you can then click on the `Add Rule` button to create an automation.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1f9c_filter_rule.png)

The sampling rate is the next thing to set. This is a rate between 0 and 1 which represents the fraction of the datapoints that meet the filter that you want want to take action on.

There are three actions you can choose from: `Add to Dataset`, `Add to Annotation Queue`, and `Online Evaluation`.

### Add to Dataset

The `Add to Dataset` action does exactly what the name suggests: it automatically adds all selected runs to a dataset. The inputs of the run become the inputs of the datapoints, the outputs the outputs, and any metadata or feedback is also copied over.

This can be used to automatically construct datasets that you can use for testing, few-shot examples, or finetuning. A typical workflow here involves filtering for datapoints that received positive feedback and moving those into a dataset.

### Add to Annotation Queue

The `Add to Annotation Queue` action is also self explanatory. It moves all selected datapoints into an annotation queue. An annotation queue is a user-friendly way to easily inspect datapoints. You can leave feedback, notes, or add to a dataset manually from this queue.

A common workflow is to send any datapoints with negative feedback into an annotation queue. This allows a reviewer to inspect all datapoints and optionally annotate them with the correct answer and move them to a dataset.

### Online Evaluation

Online evaluation is a brand new feature we&#x27;re adding, and one we&#x27;re very excited about. While it may be tough for a human to look at a large number of datapoints - it&#x27;s quite easy for a language model to do!

The basic idea of `Online Evaluation` is that each run is sent to an LLM to evaluate it according to some criteria. This criteria can be things like &quot;rudeness&quot; (checking if the LLM responded in a rude way) or something completely different like &quot;topic&quot; (classifying the user input into a variety of topics). The criteria is completely configurable.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaff78232fce8d20e1f96_evaluator.png)

## Use Case: Optimization

We&#x27;ve also added an example use case showing how to combine all these features into a relatively advanced use case. The use case we put together shows how to create an app that can learn over time how to tweet in a style that you like. It does this using a few technologies:

- Log all traces to LangSmith
- Log all feedback to LangSmith, associated with the particular trace
- For all traces with positive feedback, move into a dataset
- For all traces with negative feedback, move into an annotation queue
- Use the aforementioned dataset as few-shot examples in the application

You can see a detailed walkthrough [here](https://docs.smith.langchain.com/monitoring/use_cases/optimization?ref=blog.langchain.com).

## Conclusion

Launching an LLM application to production is just the first step. With that, you have the gift of beginning to get real user interactions and feedback. It is crucial to capture this information and then also take advantage of it. The more easily you can do that, the more quickly your application can improve. With these &quot;Production Logging &amp; Automations&quot; features, we&#x27;re making it as easy as possible for you to do that.

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