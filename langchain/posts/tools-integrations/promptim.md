---
title: "Promptim: an experimental library for prompt optimization"
author: "LangChain Accounts"
date: "2024-11-13"
url: "https://www.langchain.com/blog/promptim"
---

LangSmithTutorials &amp; How-Tos

# Promptim: an experimental library for prompt optimization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 13, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae45f4d459ecdf5f3e13_Screenshot-2024-11-13-at-7.39.25-AM.png)[Promptim](https://github.com/hinthornw/promptimizer?ref=blog.langchain.com) is an experimental **prompt** **optimization** library to help you systematically improve your AI systems.

[Promptim](https://github.com/hinthornw/promptimizer?ref=blog.langchain.com) automates the process of improving prompts on specific tasks. You provide initial prompt, a dataset, and custom evaluators (and optional human feedback), and `promptim` runs an optimization loop to produce a refined prompt that aims to outperform the original.

## From evaluation-driven development to prompt optimization

A core responsibility of AI engineers is prompt engineering. This involves manually tweaking the prompt to produce better results.

A useful way to approach this is through **evaluation-driven development**. This involves first creating a dataset of inputs (and optionally, expected outputs) and then defining a number of [evaluation metrics](https://www.langchain.com/articles/llm-evaluation-metrics). Every time you make a change to the prompt, you can run it over the dataset and then score the outputs. In this way, you can measure the performance of your prompt and make sure its improving, or at the very least not regressing. Tools like [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) help with dataset curation and evaluation.

The idea behind prompt optimization is to use these well-defined datasets and evaluation metrics to automatically improve the prompt. You can suggest changes to the prompt in an automated way, and then score the new prompt with this evaluation method. Tools like [DSPy](https://github.com/stanfordnlp/dspy?ref=blog.langchain.com) have been pioneering efforts like this for a while.

## Why do prompt optimization?

There are several motivations for prompt optimization:

**Save time**: Manual prompt engineering can often be a time-intensive process. Automated prompt optimization can speed up prompt engineering efforts and save engineering time.

**Bring rigor**: Prompt engineering is sometimes more of an art than a science – so this brings some rigor to the process. Note that evaluation-driven development in general can help accomplish this.

**Facilitate swapping between models:** Different models often require different prompting strategies. Switching model providers isn&#x27;t as simple as changing the URL you are calling; you also often need to change the prompt. Prompt optimization can speed up that process, as you focus most of your effort on developing evals (which are model agnostic) as opposed to prompting (which is not model agnostic).

## How Promptim works

We&#x27;re excited to release our first attempt at prompt optimization. It is an open source library ([promptim](https://github.com/hinthornw/promptimizer?ref=blog.langchain.com)) that integrates with LangSmith (which we use for dataset management, prompt management, tracking results, and (optionally) human labeling.

The core algorithm is as follows:

- Specify a LangSmith dataset, a prompt in LangSmith, and evaluators defined locally. Optionally, you can specify `train`/`dev`/`test` dataset splits.
- We run the initial prompt over the `dev` (or full) dataset to get a baseline score.
- We then loop over all examples in the `train` (or full) dataset. We run the prompt over all examples, then score them. We then pass the results (inputs, outputs, expected outputs, scores) to a **metaprompt **and ask it to suggest changes to the current prompt
- We then use the new updated prompt to compute metrics again on the `dev` split.
- If the metrics show improvement, the the updated prompt is retained. If no improvement, then the original prompt is kept.
- This is repeated `N` times

Optionally, you can add a step where you leave human feedback. This is useful when you don&#x27;t have good automated metrics, or want to optimize the prompt based on feedback beyond what the automated metrics can provide. This uses [LangSmith&#x27;s Annotation Queues](https://docs.smith.langchain.com/evaluation/how_to_guides/human_feedback/annotation_queues?ref=blog.langchain.com).

## Limitations of prompt optimization

Although we are excited by prompt optimization, we don&#x27;t think this is a silver bullet. It&#x27;s still worthwhile to have a human-in-the-loop in this process - even if it&#x27;s just to provide a sanity check for the final result. That&#x27;s part of the reason why we use [LangSmith&#x27;s Prompt Hub](https://docs.smith.langchain.com/prompt_engineering/concepts?ref=blog.langchain.com) to store prompts — so you can easily review the prompts afterwards.

## Comparing Promptim to DSPy

DSPy is the leading tool in the optimization space. It&#x27;s worth comparing our approach to theirs.

First, this initial effort is focused on just optimizing a single prompt. DSPy focuses on optimizing your whole &quot;compound AI system&quot;. We chose to focus on a single prompt for now as we think it is a more tractable problem at the moment.

Second, we focus more on still having the human in-the-loop, while DSPy removes the human a bit more. One example of this through hooking this up to annotation queues for human feedback as part of the optimization process. Another example is storing these prompts in LangSmith for easy review after the fact. A final example is tracking evaluation results in LangSmith.

Third, we focus solely on rewriting the prompt and aim to be really good at that, while DSPy offers a wider breadth of solutions to optimize your system (finetuning, few shot prompting).

💡

Because of these differences, we view `promptim` and `dspy` as different tools for different problems.

## Future work

As the foundation models stabilize, we are getting more and more excited about prompt optimization. Things we are looking forward to:

- Pushing more on [dynamic few shot prompting](https://docs.langchain.com/langsmith/manage-datasets)
- Integrating `promptim` into the LangSmith UI
- Adding more optimization methods to `promptim`
- Optimizing LangGraph graphs as a whole, not just prompts (ideally through an integration with DSPy)

You can [try out Promptim](https://github.com/hinthornw/promptimizer?ref=blog.langchain.com) today: `pip install promptim`. Check out [this YouTube video](https://youtu.be/18ltU1hJ7Dw?ref=blog.langchain.com) for a walkthrough, and drop us a line on [GitHub](https://github.com/langchain-ai/langchain/discussions?ref=blog.langchain.com) or [Twitter](https://x.com/LangChainAI?ref=blog.langchain.com) with any feedback.

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