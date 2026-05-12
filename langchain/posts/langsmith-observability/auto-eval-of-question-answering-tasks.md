---
title: "Auto-Eval of Question-Answering Tasks"
author: "LangChain Accounts"
date: "2023-04-16"
url: "https://www.langchain.com/blog/auto-eval-of-question-answering-tasks"
---

LangChain

# Auto-Eval of Question-Answering Tasks

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 15, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23ec7d72dc333a9d09a_photo-1516771317026-14d76f5396e5.jpeg)By [Lance Martin](https://twitter.com/RLanceMartin?ref=blog.langchain.com)

**Context**

LLM ops platforms, such as [LangChain](https://python.langchain.com/docs/get_started/introduction?ref=blog.langchain.com), make it easy to assemble LLM components (e.g., models, document retrievers, data loaders) into chains. [Question-Answering](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) is one of the most popular applications of these chains. But it is often not always obvious to determine what parameters (e.g., chunk size) or components (e.g., model choice, VectorDB) yield the best QA performance.

Here, we introduce a simple tool for evaluating QA chains ([see the code here](https://github.com/PineappleExpress808/auto-evaluator?ref=blog.langchain.com)) called `auto-evaluator`

- Ask the user to input a set of documents of interest
- Use an LLM (`GPT-3.5-turbo`) to auto-generate `question-answer` pairs from these docs
- Generate a question-answering chain with a specified set of UI-chosen configurations
- Use the chain to generate a response to each `question`
- Use an LLM (`GPT-3.5-turbo`) to score the response relative to the `answer`
- Explore scoring across various chain configurations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23fc7d72dc333a9d0a8_auto-eval.png)

**User Inputs**

This is implemented as a  [Streamlit](https://streamlit.io/?ref=blog.langchain.com) app where a user can supply a set of documents. Optionally, the user can also supply a corresponding set of question-answer pairs (see example [here](https://github.com/PineappleExpress808/auto-evaluator/tree/main/docs/karpathy-lex-pod?ref=blog.langchain.com)). If the user does not supply this, the app with auto-generate an eval set using [`QAGenerationChain`](https://python.langchain.com/docs/guides/evaluation/qa_generation?ref=blog.langchain.com). You can see the prompt used for this [here](https://github.com/hwchase17/langchain/blob/master/langchain/evaluation/qa/generate_prompt.py?ref=blog.langchain.com), which selects question-answer pairs from random chunks for the input.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23fc7d72dc333a9d0a5_auto-eval-ui.png)

**Chain**

The UI has various [knobs](https://github.com/PineappleExpress808/auto-evaluator?ref=blog.langchain.com) that can be used to create a QA chain. For example, you can pick from newer document retrievers (e.g., an [SVM](https://twitter.com/hwchase17/status/1647328542529843200?s=20&amp;ref=blog.langchain.com)) or you can use similarity search on a vectorstore. You can select various document split methods, split sizes, and split overlap. You can also select the LLM used for final summarization of the answer to the question from the retrieved docs. These different pieces can be quickly and easily assembled using Langchain into a chain for evaluation.

**Scoring**

We use an LLM (`GPT-3.5-turbo`) to score the quality of the retrieved docs, which is an idea inspired by discussion with Jerry Liu at LLama-Index ([here](https://github.com/jerryjliu/llama_index/blob/main/examples/test_wiki/TestNYC-Benchmark-GPT4.ipynb?ref=blog.langchain.com)). We also use an LLM to score the quality of the answers relative to the evaluation set. In both cases, we expose the [prompts](https://github.com/PineappleExpress808/auto-evaluator/blob/main/text_utils.py?ref=blog.langchain.com). Users can easily engineer them. We also expose the results for human inspection; the `Descriptive` prompt can be used to ask the LLM grader for a detailed explanation of its assessment.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23fc7d72dc333a9d0a2_auto-eval-results.png)

**Comparison**

We accumulate experimental results for easy comparison across the various tests, with a table and a scatter plot of the mean score (answer and retrieval) versus the model latency (in sec).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23fc7d72dc333a9d0ac_comparison.png)

**Future directions**

Feedback and contributions are welcome; for example, we would like to include other retrievers (such as LLama-Index) and other models (e.g., various HuggingFace models). We’d like to improve the performance (e.g., in particular, the latency) of various stages in the eval process and offer this as a free hosted tool (since some users will not have access to GPT-4 or Claude today). Finally, we’d like to extend this to other tasks (e.g., chat) and automate the process of best chain assembly (e.g., using agents) given a user-specified objective (e.g., chat or QA goals).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)