---
title: "Easier evaluations with LangSmith SDK v0.2"
author: "LangChain Accounts"
date: "2024-12-05"
url: "https://www.langchain.com/blog/easier-evaluations-with-langsmith-sdk-v0-2"
---

Tutorials &amp; How-TosLangSmith

# Easier evaluations with LangSmith SDK v0.2

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 5, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3307bc92c96efbbbff_Youtube-and-Blog-Self-Serve-Components--1-.png)We’ve recently released v0.2 of the LangSmith SDKs, which come with a number of improvements to the developer experience for evaluating applications. We have simplified usage of the `evaluate()` / `aevaluate()` methods, added an option to run evaluations locally without uploading any results, improved SDK performance, and expanded our documentation. These improvements have been made in both the Python and TypeScript SDKs.

The v0.2 release has 2 breaking changes in the Python SDK. These are listed at the bottom.

## Simplified usage of `evaluate()` / `aevaluate()`

### **Simpler evaluators**

The LangSmith SDK’s allow you to define [custom evaluators](https://docs.smith.langchain.com/evaluation/how_to_guides/custom_evaluator?ref=blog.langchain.com), which are functions that score your application’s outputs on a dataset. Before today, these evaluators had to take as arguments a Run and an Example object:

`from langsmith import evaluate
from langsmith.schemas import Run, Example

def correct(run: Run, example: Example) -&gt; dict:
  outputs = run.outputs
  inputs = example.inputs
  reference_outputs = example.outputs

	score = run.outputs[&#x27;answer&#x27;] == example.outputs[&#x27;answer&#x27;]
  return {&quot;key&quot;: &quot;correct&quot;, &quot;score&quot;: score}

results = evaluate(..., evaluators=[correct])
`

In v0.2, you can write this in Python as:

`from langsmith import evaluate

def correct(inputs: dict, outputs: dict, reference_outputs: dict) -&gt; bool:
  return outputs[&quot;answer&quot;] == reference_outputs[&quot;answer&quot;]

results = evaluate(..., evaluators=[correct])
`

And in TypeScript as:

`import type { EvaluationResult } from &quot;langsmith/evaluation&quot;;

const correct = async ({
  outputs,
  referenceOutputs,
}: {
  outputs: Record&lt;string, any&gt;;
  referenceOutputs?: Record&lt;string, any&gt;;
}): Promise&lt;EvaluationResult&gt; =&gt; {
  const score = outputs?.answer === referenceOutputs?.answer;
  return { key: &quot;correct&quot;, score };
};
`

The keys changes are as follows:

- You can write evaluator functions that accept the `inputs`, `outputs`, `reference_outputs` dicts as args. If needed, you can continue to pass in `run` and `example` to access run [intermediates steps or run/example metadata.](https://docs.smith.langchain.com/evaluation/how_to_guides/evaluate_on_intermediate_steps?ref=blog.langchain.com)
- (Python only) Yo can return primitives *(float, int, bool, str)* directly

Analogous simplifications have been made to [summary evaluators](https://docs.smith.langchain.com/evaluation/how_to_guides/summary?ref=blog.langchain.com) and [pairwise evaluators](https://docs.smith.langchain.com/evaluation/how_to_guides/evaluate_pairwise?ref=blog.langchain.com). For more on defining evaluators head to [this how-to guide](https://docs.smith.langchain.com/evaluation/how_to_guides/custom_evaluator?ref=blog.langchain.com).

### **Evaluate `langgraph` and `langchain` objects directly**

You can now pass your `langgraph` and `langchain` objects directly into `evaluate()` / `aevaluate()`:

`from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langsmith import evaluate

def check_weather(location: str) -&gt; str:
		&#x27;&#x27;&#x27;Return the weather forecast for the specified location.&#x27;&#x27;&#x27;
		return f&quot;It&#x27;s always sunny in {location}&quot;

tools = [check_weather]
model = init_chat_model(&quot;gpt-4o-mini&quot;)
graph = create_react_agent(model, tools=tools)

results = evaluate(graph, ...)
`

For more on evaluating `langgraph` and `langchain` objects, see these how-to guides: [langgraph](https://docs.smith.langchain.com/evaluation/how_to_guides/langgraph?ref=blog.langchain.com), [langchain](https://docs.smith.langchain.com/evaluation/how_to_guides/langchain_runnable?ref=blog.langchain.com).

### **Consolidated evaluation methods**

Previously, there were three different methods for running evaluations (not counting their async counterparts): `evaluate()`, `evaluate_existing()` and `evaluate_comparative()` / `evaluateComparative()` . The first was for running your application on a dataset and scoring the outputs, the second for just running evaluators on existing experiment results, and the third for running pairwise evaluators on two existing experiments.

In v0.2, you only need to know about the `evaluate()` method:

`from langsmith import evaluate

# Run the application and evaluate the results
def app(inputs: dict) -&gt; dict:
  return {&quot;answer&quot;: &quot;i&#x27;m not sure&quot;}

results = evaluate(app, data=&quot;dataset-name&quot;, evaluators=[correct])

# Run new evaluators on existing experimental results
def concise(outputs: dict) -&gt; bool:
	return len(outputs[&quot;answer&quot;]) &lt; 10

more_results = evaluate(
	results.experiment_name,  # Pass in an experiment name/ID instead of a function.
	evaluators=[concise].
)

# Run comparative evaluation
# First we need to run a second experiment
def app_v2(inputs: dict) -&gt; dict:
	return {&quot;answer&quot;: &quot;i dunno you tell me&quot;}

results_v2 = evaluate(app_v2, data=&quot;dataset-name&quot;, evaluators=[correct])

# Note: &#x27;outputs&#x27; is a two-item list for pairwise evaluators.
def more_concise(outputs: list[dict]) -&gt; bool:
	v1_len = len(outputs[0][&quot;answer&quot;])
	v2_len = len(outputs[1][&quot;answer&quot;])
	if v1_len &lt; v2_len:
		return [1, 0]
	elif v1_len &gt; v2_len:
		return [0, 1]
	else:
		return [0, 0]

comparative_results = evaluate(
	[results.experiment_name, results_v2.experiment_name],  # Pass in two experiment names/IDs instead of a function.
	evaluators=[more_concise],  # Pass in a pairwise evaluator(s).
)
`

For more see our how-to guides on [pairwise experiments](https://docs.smith.langchain.com/evaluation/how_to_guides/evaluate_pairwise?ref=blog.langchain.com) and [evaluating existing experiments](https://docs.smith.langchain.com/evaluation/how_to_guides/evaluate_existing_experiment?ref=blog.langchain.com).

## Beta: Run evaluations without uploading results

Sometimes it is helpful to run an evaluation locally without uploading any results to LangSmith. For example, if you&#x27;re quickly iterating on a prompt and want to smoke test it on a few examples, or if you&#x27;re validating that your target and evaluator functions are defined correctly, you may not want to record these evaluations.

In the v0.2 Python SDK, you can do this by simply setting:

`results = evaluate(..., upload_results=False)
`

The output of this will look exactly the same as it did before, but there will be no sign of this experiment in LangSmith. For more head to our [how-to guide on running evals locally](https://docs.smith.langchain.com/evaluation/how_to_guides/local?ref=blog.langchain.com).

**Note that this feature is still in beta and only supported in Python.**

## **Improved Python SDK performance**

We’ve also made several improvements to the Python SDK&#x27;s evaluation performance for large examples, resulting in approximately a 30% speedup in `aevaluate()` for examples ranging from 1 to 4MB .

## **Revamped documentation**

We’ve rewritten most of our [evaluation how-to guides](https://docs.smith.langchain.com/evaluation/how_to_guides?ref=blog.langchain.com), revamping existing guides and adding a number of new ones related to the improvements mentioned in this post. We’ve also updated the Python SDK API Reference and consolidated it with the main LangSmith docs: [https://docs.smith.langchain.com/reference/python](https://docs.smith.langchain.com/reference/python?ref=blog.langchain.com)

## Breaking changes

In the Python SDK,  two breaking changes have been made:

- In the Python SDK, `evaluate` / `aevaluate` now have a default `max_concurrency=0` instead of `None`. This makes it so that by default no concurrency is used instead of unlimited concurrency.
- In the Python SDK, if you pass in a string as the data arg to evaluate: `evaluate(..., data=&quot;...&quot;)` / `aevaluate(..., data=&quot;...&quot;)`, we will now check if that string corresponds to a UUID and should be treated as the dataset ID before treating it as the dataset name. Previously, it was always assumed that a string value corresponds to the dataset name.
- We’ve officially dropped support for Python 3.8, which reached its EOL in October 2024.

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