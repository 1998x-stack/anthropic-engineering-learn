---
title: "Reusable Evaluators and Evaluator Templates in LangSmith"
author: "LangChain Accounts"
date: "2026-04-16"
url: "https://www.langchain.com/blog/reusable-langsmith-evaluator-templates"
---

Observability &amp; EvalsLangSmith

# Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)

## Key Takeaways

- **Evaluator templates give you a running start.** LangSmith now includes 30+ templates covering safety, response quality, trajectory, user behavior, and multimodal evaluation. Use them as-is or customize them — they work for both online monitoring and offline experiment runs.
- **Build an evaluator once, apply it everywhere.** A new Evaluators tab centralizes every evaluator in your workspace. You can attach an existing evaluator to a new tracing project in seconds, so your safety checks and quality metrics stay consistent across the org without maintaining duplicate copies.
- **Good evals require coverage at multiple levels.** A single evaluator checking the final answer won&#x27;t catch whether your retrieval agent pulled the right documents or your planning agent delegated correctly. Effective agent evaluation means testing individual steps, full trajectories, multi-turn conversations, and specific tool calls within a trace.

Today, we&#x27;re releasing two updates to LangSmith Evaluation: **reusable evaluators** and an **evaluator template library**.

Reusable evaluators give you a single place to view, manage, and apply evaluators across multiple tracing projects. Evaluator templates give teams a running start on testing and monitoring agents without building everything from scratch.

[Try LangSmith Evaluation](https://www.langchain.com/langsmith/evaluation)

## Where evaluations get stuck

Figuring out what &quot;good&quot; looks like is one of the hardest problems when building agents. Your agent might call the right tool but format the response poorly. It might handle single-turn interactions well but fall apart over a multi-turn conversation. And a single evaluator that checks the final answer won&#x27;t tell you whether your retrieval agent pulled the right documents or whether your planning agent chose the right subagent to delegate to. You need evals at different levels: individual steps, full trajectories, entire conversations, and sometimes specific tool calls within a trace.

Building evaluators across those levels can take weeks. You write a prompt, check the scores against real data, tune it, and repeat. That iteration is important, but when you&#x27;re starting from scratch every time, it&#x27;s time spent on the basics instead of improving your agent. And once you&#x27;ve built a good evaluator, you’ll want to apply it across tracing projects without maintaining separate copies.

We&#x27;ve been building evaluation tooling in LangSmith for over a year, from [openevals](https://blog.langchain.com/evaluating-llms-with-openevals/) evaluator framework to [Align Evals](https://blog.langchain.com/introducing-align-evals/) for evaluator calibration to [multimodal evaluator support](https://www.youtube.com/watch?v=QZjjVMhjEcY). Today&#x27;s release adds two features we&#x27;ve heard the most demand for.

## Evaluator templates

We&#x27;ve worked with a lot of teams running agents in production, and the same evaluation questions keep coming up: is the agent safe? Is the response actually good? Did it take the right steps to get there?

Templates cover the categories we see come up most often:

- **Safety and security**: prompt injection detection, PII checks, bias and toxicity
- **Response quality**: correctness, helpfulness, tone
- **Trajectory**: did the agent take the right steps?
- **User behavior analysis**: language distribution, satisfaction signals
- **Multimodal:** voice and image review

These are a few of the 30+ evaluator templates available. Templates include LLM-as-judge evaluators with tuned prompts and rule-based code evaluators. Use them as-is or customize for your agent.

They work for both online and offline evaluation. For online evaluation, templates help you categorize production traffic: detecting prompt injections, flagging unexpected user behavior, or surfacing traces that need human review. You can use your corrections to tune the evaluator prompt so it performs better next time

For offline evaluation, templates give you a starting point for running experiments across your datasets. Run the evaluator, check scores, filter down to failures, and understand what went wrong.

These templates are also available in [openevals v0.2.0](https://github.com/langchain-ai/openevals), released today, with new multimodal support for evaluating voice and image outputs. You can use them directly in code or through the LangSmith UI.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e00162a04500053fdbcfd0_evals-library-1.png)

## Reusable evaluators

Once you&#x27;ve built evaluators that work well, you need a way to manage them centrally. A new **Evaluators tab** surfaces every evaluator in your workspace, regardless of which project it&#x27;s attached to. You can filter by tracing project and attach an existing evaluator to a new project in seconds.

If your team owns evaluation quality across the org (defining safety checks, standardizing quality metrics), you can build evaluators once and apply them everywhere. No more maintaining separate copies of the same safety evaluator across every tracing project.

For individual engineers working in a specific tracing project, the experience stays simple: you can quickly add and configure evaluators scoped to your project from the tracing view.

As an example, say you build a prompt injection evaluator from a template. You tune the prompt, validate it against sample data, and it works well. With reusable evaluators, you attach it to every production tracing project from one place. When you improve the prompt, the update applies everywhere.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e001b3ee6d1cf734174f5f_evals-library-2.png)

## What&#x27;s coming next

If you try out the new features, let us know how they&#x27;re working for you. Next up, we&#x27;re adding spend visibility so you can track what evaluations are costing you and set budgets accordingly.

## Get started

Evaluator templates and reusable evaluators are available now in LangSmith.

[Try LangSmith Evaluation](https://smith.langchain.com/) | [Read the docs](https://docs.langchain.com/langsmith/evaluators)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8a01c18c14b60cd4372_76.webp)LangSmithObservability &amp; Evals

#### Human judgment in the agent improvement loop

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2d3bf32d4fc06a289383_rahul-verma.png)Rahul VermaApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/human-judgment-in-the-agent-improvement-loop)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)