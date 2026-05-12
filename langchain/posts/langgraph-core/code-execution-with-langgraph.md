---
title: "LangGraph for Code Generation"
author: "LangChain Accounts"
date: "2024-02-27"
url: "https://www.langchain.com/blog/code-execution-with-langgraph"
---

LangGraph

# LangGraph for Code Generation

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaFebruary 27, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01303935dbc92df8dd2_Screenshot-2024-02-22-at-2.41.55-PM.png)

### Key Links

- [LangGraph cookbook](https://github.com/langchain-ai/langgraph/blob/main/examples/code_assistant/langgraph_code_assistant.ipynb?ref=blog.langchain.com)
- [Video](https://www.youtube.com/watch?v=MvNdgmM7uyc&amp;ref=blog.langchain.com)

### Motivation

Code generation and analysis are two of most important applications of LLMs, as shown by the ubiquity of products like [GitHub co-pilot](https://github.com/features/copilot?ref=blog.langchain.com) and popularity of projects like [GPT-engineer](https://github.com/gpt-engineer-org/gpt-engineer?ref=blog.langchain.com). The recent [AlphaCodium](https://arxiv.org/pdf/2401.08500.pdf?ref=blog.langchain.com) work showed that code generation can be [improved by using a `flow` paradigm](https://x.com/karpathy/status/1748043513156272416?s=20&amp;ref=blog.langchain.com) rather than a naive `prompt:answer` paradigm: answers can be **iteratively** constructed by (1) testing answers and (2) [reflecting](https://blog.langchain.com/reflection-agents/) on the results of these tests in order to improve the solution.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01403935dbc92df8de7_image-20.png)Flow for AlphaCodium

We recently launched [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) to support flow engineering, giving the user the ability to represent flows as a graph. Inspired by the [AlphaCodium](https://arxiv.org/pdf/2401.08500.pdf?ref=blog.langchain.com) and [Reflexion](https://blog.langchain.com/reflection-agents/) work, we wanted to demonstrate that LangGraph can be used to implement code generation with the same types of cycles and decisions points as shown above.

Specifically we wanted to build and compare two different architectures:

- Code generation via prompting and context stuffing
- Code generation flow that involved checking and running the code, and then if there was some error passing it back to correct itself

This would attempt to answer: how much can these code checks improve performance of a code generation system?

The answer?

💡

The system that checks the code and attempts to fix it yielded a sizable improvement over the baseline of a single generation (81% vs 55%)

### Problem

To demonstrate code generation on a narrow corpus of documentation, we chose a sub-set of LangChain docs focused on [LangChain Expression Language](https://python.langchain.com/docs/expression_language/?ref=blog.langchain.com) (LCEL), which is both  bounded (~60k token) and a topic of high interest. We mined 30 days of [`chat-langchain`](https://chat.langchain.com/?ref=blog.langchain.com) for LCEL related questions (code [here](https://github.com/langchain-ai/lcel-teacher/blob/main/eval/build_eval_set.ipynb?ref=blog.langchain.com)). We filtered for those that mentioned LCEL, from `&gt;60k chats` to `~500`. We clustered the ~500 and had an LLM (GPT-4, 128k) summarize clusters to give us representative questions in each. We manually reviewed and generated a ground truth answer for each question (eval set of 20 questions [here](https://github.com/langchain-ai/lcel-teacher/blob/main/eval/eval.csv?ref=blog.langchain.com)). We added [this dataset](https://smith.langchain.com/public/ea1f6ca5-de52-4d36-bd7b-fde3faa74a70/d?ref=blog.langchain.com) to LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01403935dbc92df8de2_image-1.png)Workflow to generate the eval set for LCEL teacher

### Code generation with reflection using LangGraph

We implement a code generation flow with the following components:

- Inspired by recent [trends](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/?ref=blog.langchain.com) in long-context LLMs, we context stuff the 60k token LCEL docs using GPT-4 with a 128k token context window. We pass a question about LCEL to our context-stuffed LCEL chain for initial answer generation.
- We use OpenAI tools to [parse the output](https://python.langchain.com/docs/modules/model_io/output_parsers/types/pydantic?ref=blog.langchain.com) to a [Pydantic](https://docs.pydantic.dev/latest/?ref=blog.langchain.com) object with three parts: (1) a preamble describing the problem, (2) the import block, (3) the code.
- We first check **import** execution, because we have [found](https://docs.google.com/spreadsheets/d/1SkHHw52AHFFBnmljKW3Vq_YvnPpAhhBVhd1SF9mPFUk/edit?ref=blog.langchain.com#gid=0) that hallucinations can creep into import statements during code generation.
- If the **import** check passes, we then check that the code itself can be executed. In the generation prompt, we instruct the LLM not to use pseudo-code or undefined variables in the code solution, which should yield executable code.
- Importantly, if either check fails, we pass back the stack trace along with the prior answer to the generation node to [reflect](https://blog.langchain.com/reflection-agents/) We allow this to re-try 3 times (simply as a default value), but this can of course be extended as desired.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01403935dbc92df8ddf_image-21.png)LangGraph for code execution with error checking, feedback, and reflection

### Evaluation with LangSmith

As a baseline, we  implement `context stuffing` without LangGraph, which is the first node in our graph without any of the checks or feedback: we context stuff the 60k token LCEL docs using GPT-4 with a 128k token context window. We pass a question about LCEL to our context-stuffed LCEL chain for answer generation.

We implement [LangSmith custom evaluators](https://docs.smith.langchain.com/evaluation/faq/custom-evaluators?ref=blog.langchain.com) for both (1) import evaluation and (2) code execution. We run evaluation on `context stuffing` with our 20 question eval set four times. [Here](https://smith.langchain.com/public/ea1f6ca5-de52-4d36-bd7b-fde3faa74a70/d?ref=blog.langchain.com) is our eval result. With `context stuffing` we see `~98%` of the import tests are correct and `~55%` of the code execution tests  (`N=79` successful trials). We use LangSmith to look at our failures: [here](https://smith.langchain.com/public/b04f4258-173f-4b79-a935-1e7c8bc4526c/r?ref=blog.langchain.com) is one example, which fails to see that the `RunnableLambda` function input will be a `dict` and thinks that it is a `string`: `AttributeError: &#x27;dict&#x27; object has no attribute &#x27;upper&#x27;`

We then tested `context stuffing + LangGraph` to (1) perform checks for errors like this in both imports and code execution and (2) [reflect](https://blog.langchain.com/reflection-agents/) on any errors when performing updated answer generation. On the same eval set, we see `100%` of the import tests are correct along with `~81%` of the code execution tests  (`N=78` trials).

We can revisit the above failure to demonstrate why: the full [trace](https://smith.langchain.com/public/b595525e-59fe-4cb6-905b-2bad8e0e9165/r?ref=blog.langchain.com) shows that we **do** hit that same error [here](https://smith.langchain.com/public/0a1c33fa-c947-42ab-9dae-16fc7868ad53/r?ref=blog.langchain.com), in our second attempt at answering the question. We include this error in our [reflection](https://blog.langchain.com/reflection-agents/) step in which both the prior solution and the resulting error are provided within the prompt for the final (correct) answer:

`You previously tried to solve this problem.
...
--- Most recent run error ---
Execution error: &#x27;dict&#x27; object has no attribute &#x27;upper&#x27;
...
Please re-try to answer this.
...`

The [final generation](https://smith.langchain.com/public/b595525e-59fe-4cb6-905b-2bad8e0e9165/r?ref=blog.langchain.com) then correctly handles the input dict in the `RunnableLambda` function, bypassing the error observed in the  `context stuffing` base case. Overall, adding this simple reflection step and re-try using LangGraph results in a substantial improvement on code execution, `~47%` improvement:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb01403935dbc92df8dea_Screenshot-2024-02-22-at-1.07.33-PM.png)LangSmith evaluation for imports and code execution with and without LangGraph

### Conclusion

LangGraph makes it easy to engineer flows with various cycles and decision points. [Recent work](https://arxiv.org/pdf/2401.08500.pdf?ref=blog.langchain.com) has shown that this is powerful for code generation, where answers to coding questions can be constructed iteratively using using tests to check answers, [reflect](https://blog.langchain.com/reflection-agents/) on failures, and iteratively improve the answer. We show that this can be implemented in LangGraph and test it on 20 questions related to LCEL for both code imports and execution. We find that `context stuffing + LangGraph` with reflection results in `~47%` improvement in code execution relative `context stuffing`. The notebook is [here](https://github.com/langchain-ai/langgraph/blob/main/examples/code_assistant/lcel-teacher-langgraph.ipynb?ref=blog.langchain.com) and be extended to other codebases trivially.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b0ec45aa6d7bc39a91_KEnsho.png)Case StudiesLangGraphObservability &amp; Evals

#### How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 26, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/customers-kensho)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa18703c727fd28ab4de_Vodafone-Italy---Oct-2025--1-.png)Case StudiesLangGraphLangSmith

#### Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 16, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/customers-vodafone-italy)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)