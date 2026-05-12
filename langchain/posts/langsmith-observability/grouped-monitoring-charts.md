---
title: "LangSmith&#x27;s Latest Feature: Grouped Monitoring Charts"
author: "LangChain Accounts"
date: "2024-01-30"
url: "https://www.langchain.com/blog/grouped-monitoring-charts"
---

LangSmithObservability &amp; Evals

# LangSmith&#x27;s Latest Feature: Grouped Monitoring Charts

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaJanuary 30, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb04d2c7f205b929b9bde_Screenshot-2024-01-28-at-5.03.55-PM.png)

## Tag and Metadata Grouping

LangSmith has long supported monitoring charts to showcase important performance and feedback metrics overtime for your LLM applications (see the **`Monitoring`** section in any project details page). However, until now, it wasn&#x27;t possible to compare metrics of logged traces containing different tags or metadata. In LLM applications, there can often be many knobs at your disposal (model params, prompt, chunking strategy, look-back window), each having a potentially huge impact on your application.

With tag and metadata grouping, users of LangSmith can now mark different versions of their applications with different identifiers and view how they are performing side-by-side using the new monitoring features.

## Sending Traces With Tags and Metadata

LangSmith now supports grouping by both tags and metadata in monitoring charts. Here&#x27;s a quick refresher on how you can log traces with tags and metadata. For more information, check out our [docs](https://docs.smith.langchain.com/tracing/tracing-faq?ref=blog.langchain.com#how-do-i-add-metadata-to-runs).

### LangChain

If using LangChain, you can send a dictionary with tags and/or metadata in `invoke` to any Runnable. The same concept works in TypeScript as well.

`chain.invoke({&quot;input&quot;: &quot;What is the meaning of life?&quot;}, {&quot;metadata&quot;: {&quot;my_key&quot;: &quot;My Value&quot;}})  # sending custom metadata

chain.invoke({&quot;input&quot;: &quot;Hello, World!&quot;}, {&quot;tags&quot;: [&quot;shared-tags&quot;]})  # sending custom tags`

LangChain Python

### LangSmith SDK / API

If you&#x27;re not using LangChain, you can either use the SDK or API to log traces with custom tags and/or metadata.

`# Using the Python SDK
import openai
from langsmith.run_helpers import traceable

@traceable(
    run_type=&quot;llm&quot;
    name=&quot;My LLM Call&quot;,
    tags=[&quot;tutorial&quot;],
    metadata={&quot;githash&quot;: &quot;e38f04c83&quot;},
)
def call_openai(
    messages: List[dict], model: str = &quot;gpt-3.5-turbo&quot;, temperature: float = 0.0
) -&gt; str:
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )`

Python SDK

`// Using the TypeScript SDK
import { RunTree, RunTreeConfig } from &quot;langsmith&quot;;

const parentRunConfig: RunTreeConfig = {
    name: &quot;My Chat Bot&quot;,
    run_type: &quot;chain&quot;,
    inputs: {
        text: &quot;Summarize this morning&#x27;s meetings.&quot;,
    },
    extra: {
        metadata: {&quot;githash&quot;: &quot;e38f04c83&quot;}
    },
    tags=[&quot;tutorial&quot;]
};

const parentRun = new RunTree(parentRunConfig);
await parentRun.postRun();`

TypeScript SDK

`# Using the REST API (in Python)
requests.post(
    &quot;https://api.smith.langchain.com/runs&quot;,
    json={
        &quot;id&quot;: run_id,
        &quot;name&quot;: &quot;My Run&quot;,
        &quot;run_type&quot;: &quot;chain&quot;,
        &quot;inputs&quot;: {&quot;text&quot;: &quot;Foo&quot;},
        &quot;start_time&quot;: datetime.datetime.utcnow().isoformat(),
        &quot;session_name&quot;: project_name,
        &quot;tags&quot;: [&quot;langsmith&quot;, &quot;rest&quot;, &quot;my-example&quot;],
        &quot;extra&quot;: {
            &quot;metadata&quot;: {&quot;my_key&quot;: &quot;My value&quot;},
        },
    },
    headers={&quot;x-api-key&quot;: _LANGSMITH_API_KEY},
)`

REST API (in Python)

## Case Study: Testing Different LLM Providers in Chat LangChain

[Chat LangChain](https://blog.langchain.com/building-chat-langchain-2/) is an LLM-powered chatbot designed to answer questions about LangChain’s python documentation. We’ve deployed the chatbot to production using LangServe, and have enabled [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) tracing for best-in-class observability. We’ve allowed the user to pick one out of four LLM providers  (Claude 2.1, Mixtral hosted on Fireworks, Google Gemini Pro, and OpenAI GPT 3.5 Turbo) to power the chat experience and are sending up the model type using the key `&quot;llm&quot;` in `metadata`.

Let’s say we’re interested in analyzing how each model is performing w.r.t important metrics, such as latency and time-to-first-token.

We can see here that we have grouped the monitoring charts by the `llm` metadata key. By analyzing the charts, we can identify any variations or discrepancies between the models and make data-driven decisions about our application.

### LLM Latency

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb04d2c7f205b929b9c37_Screenshot-2024-01-28-at-4.34.18-PM.png)Chart in LangSmith showing LLM latency over time

Here, we see that responses powered by Mixtral on Fireworks complete a lot faster than other providers.

### Time to First Token

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb04d2c7f205b929b9c34_Screenshot-2024-01-28-at-4.35.02-PM-1.png)Chart in LangSmith showing time-to-first-token over time

This chart shows time-to-first-token over time across the different LLM providers. Interestingly, while Google Gemini provides faster overall completion times than Claude 2.1, time-to-first-token is is trending slower.

### Feedback

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb04d2c7f205b929b9c3a_Screenshot-2024-01-28-at-5.29.03-PM.png)Chart in LangSmith showing User Score (binary) over time

The monitoring section also shows you charts for feedback across different criteria over time. While our feedback data was noisy during this time period, you can imagine that seeing clear trends in user satisfaction in chatbot response across the different model providers would allow for assessing tradeoffs of model latency vs quality of response.

## Other Use-Cases

Here, we’ve shown you can use metadata and tagging in LangSmith to group your data into different categories, one category per model-type, then analyze performance metrics for each category alongside each other. This paradigm can be easily applied to other use-cases:

- **A/B Testing with Revisions**: Imagine you&#x27;re rolling out different feature revisions or versions in your application and want to test them side-by-side. By sending up a `revision` identifier in the metadata and grouping by this revision in your charts, you can clearly see how each version performs with respect to each other.
- **Enhancing User Experience**: By grouping data using `user_id` or `conversation_id` in metadata, you gain an in-depth understanding of how different users are experiencing the application and identify any user-specific issues or trends.

These examples just scratch the surface of what&#x27;s possible with LangSmith&#x27;s new grouping feature.

You can sign up for LangSmith [here](https://smith.langchain.com/?ref=blog.langchain.com), as well as check out the LangSmith [docs](https://docs.smith.langchain.com/?ref=blog.langchain.com) and a helpful guided LangSmith [walkthrough](https://python.langchain.com/docs/langsmith/walkthrough?ref=blog.langchain.com) too.

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