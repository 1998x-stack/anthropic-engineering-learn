---
title: "How &quot;Correct&quot; are LLM Evaluators?"
author: "LangChain Accounts"
date: "2023-09-28"
url: "https://www.langchain.com/blog/how-correct-are-llm-evaluators"
---

Tutorials &amp; How-Tos

# How &quot;Correct&quot; are LLM Evaluators?

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 28, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1433d7d286a58faa0db_5-social--33-.png)

## Summary:

- We tested LangChain&#x27;s LLM-assisted evaluators on common tasks to provide guidelines on how to best use them in your practice.
- GPT-4 excels in accuracy across various tasks, while GPT-3.5 and Claude-2 lag for tasks requiring complex &quot;reasoning&quot; (when used in a zero-shot setting).

## Context

Evaluating language model applications is a challenge. Evaluating by hand can be costly and time-consuming, and classic automated metrics like ROUGE or BLEU can often [miss the point](https://aclanthology.org/2022.wmt-1.2.pdf?ref=blog.langchain.com) of what makes a &quot;good&quot; response. LLM-based evaluation methods are promising, but they aren&#x27;t without issues. For instance, they can prefer their own output to human-written text, as revealed in [recent research](https://arxiv.org/abs/2303.16634?ref=blog.langchain.com).

Another challenge is reliability. If an evaluation model operates in the same context as the model being assessed, its feedback might lack the depth needed for meaningful insights. This [isn&#x27;t a solved problem](https://www.aclweb.org/portal/content/second-call-papers-4th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp-2023?ref=blog.langchain.com), and it&#x27;s why we&#x27;re committed to developing robust, flexible evaluation tools at LangChain.

In tasks such as question-answering and information extraction, &#x27;correctness&#x27; is often the key metric. We&#x27;ve run experiments to measure the quality of LLM-based evaluators in determining &quot;correctness&quot; of outputs relative to a label, so we can share better guidelines and best practices for achieving reliable results.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0f7_image-43.png)

## What we tested

We investigated three of LangChain&#x27;s evaluators designed to grade whether a predicted output is &quot;correct&quot; relative to a label.

- QAEvalChain ([link](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.qa.eval_chain.QAEvalChain.html?ref=blog.langchain.com#langchain.evaluation.qa.eval_chain.QAEvalChain) + [prompt](https://smith.langchain.com/hub/wfh/qa?ref=blog.langchain.com)): prompts a model to grade the prediction as a teacher grading a quiz, ignoring spacing and wording.
- CoT evaluator ([link](https://api.python.langchain.com/en/latest/evaluation/langchain.evaluation.qa.eval_chain.CotQAEvalChain.html?ref=blog.langchain.com#langchain.evaluation.qa.eval_chain.CotQAEvalChain) + [prompt](https://smith.langchain.com/hub/wfh/cot_qa?ref=blog.langchain.com)): similar to the QA example above, but it instructs step-by-step reasoning using the provided context.
- LangChain also provides a “Criteria” evaluator ([link](https://python.langchain.com/docs/guides/evaluation/string/criteria_eval_chain?ref=blog.langchain.com)), for testing whether a prediction meets the custom criterion provided (in this case, &quot;correctness&quot; relative to the reference). The  [prompt](https://smith.langchain.com/hub/wfh/criteria_candidates?ref=blog.langchain.com) is similar to OpenAI&#x27;s [model graded ](https://github.com/openai/evals/blob/e49868e550babb7b1c5b4223c9b7a14511bf114d/evals/registry/modelgraded/closedqa.yaml?ref=blog.langchain.com#L1)evaluator prompt.

We tested all three evaluators using a binary &#x27;right or wrong&#x27; scale, without giving them any few-shot examples for each task. Tests using additional prompting techniques or a continuous grading scale are saved for a future post. You can find the code for these experiments here ([link](https://github.com/langchain-ai/langchain-benchmarks/tree/main/meta-evals/correctness?ref=blog.langchain.com)) and the full summary table of these experiments here ([link](https://drive.google.com/file/d/16zCLnJlxxuAjb12SH5AmZOuGr72uyB-a/view?usp=sharing&amp;ref=blog.langchain.com)).

## Creating the datasets

To grade the reliability of these evaluators, we created benchmark datasets for three common tasks. For each source dataset, we transformed the answers using [techniques](https://aclanthology.org/2020.acl-main.442/?ref=blog.langchain.com) to generate data splits where the predictions are known to be “Correct” or “Incorrect”, assuming the original labels are reliable. Below is an overview for each dataset.

**Q&amp;A:** sampled from the  [WebQuestions](https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a?ref=blog.langchain.com) dataset.

- The &quot;*Correct*&quot; split was made by altering the true answers without changing their meaning. We swapped in synonyms, padded answers like, &quot;The answer to &#x27;What is X&#x27; is Y,&quot; where &quot;Y&quot; is the correct answer, and we added small typos,
- The “*Incorrect*” split was generated by selecting outputs from other rows in the dataset.

**Translation**: sampled from the [Opus-100 dataset](https://opus.nlpl.eu/opus-100.php?ref=blog.langchain.com) .

- The “Correct” split was made by padding with chit chat and inserting additional spaces where it wouldn&#x27;t impact the way the sentence was read.
- The “Incorrect” split was generated by selecting negative examples from other rows in the dataset or adding content not in the source phrase.

**Extraction**: sampled from the [CarbIE benchmark ](https://aclanthology.org/D19-1651/?ref=blog.langchain.com)

- The “Correct” split was generated by shuffling the order of rows in the extracted triplets, keeping the content the same.
- The “Incorrect” split was generated by inserting a new triple into each example.

## Results

For a full table of results, see the [data](https://drive.google.com/file/d/16zCLnJlxxuAjb12SH5AmZOuGr72uyB-a/view?usp=sharing&amp;ref=blog.langchain.com) in the link. We will answer some key questions in the sections below:

### Which models should I use in evaluators?

When selecting LLM&#x27;s to use as a judge in our evaluators, we have traditionally recommended starting with GPT-4 since &quot;less capable&quot; models can give spurious results. Our experiments sought to validate this recommendation and provide more context on when a smaller model can be substituted in.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1433d7d286a58faa0e1_image-38.png)Evaluator accuracy based on the eval LLM, for each dataset

Table of Results

 The following results contain the accuracy/null rate of the evaluation outputs each model, selecting the *best* performing evaluator for each model.

DatasetClaude-2GPT-3.5-turboGPT-3.5-turbo-instructGPT-4Carb-IE Correct1.00 / 0.001.00 / 0.001.00 / 0.001.00 / 0.00Carb-IE Incorrect0.65 / 0.000.21 / 0.350.42 / 0.270.99 / 0.00Opus100 - Correct1.00 / 0.001.00 / 0.001.00 / 0.000.98 / 0.00Opus100 - Incorrect0.98 / 0.000.59 / 0.050.57 / 0.001.00 / 0.00WebQ&amp;A - Correct1.00 / 0.001.00 / 0.001.00 / 0.001.00 / 0.00WebQ&amp;A - Incorrect1.00 / 0.001.00 / 0.001.00 / 0.001.00 / 0.00

The results indicate GPT-4 indeed outperforms the others in structured &quot;reasoning&quot; tasks, such as when evaluating on the Carb-IE extraction dataset. On the other hand, Claude-2 and GPT-3.5 show reliability in simpler tasks like translation and Web Q&amp;A but falter when additional reasoning is needed. Notably, the results table above shows that GPT-3.5-turbo struggled with false positives and had high null rates, meaning it often provided unusable responses.

This error analysis suggests that while prompt-tuning might improve performance, GPT-4 remains the most dependable general-purpose model for tasks requiring structured data reasoning. The instruct variant of GPT-3.5-turbo offers no significant advantage in response quality over its predecessor.

### How reliable is a single evaluator across tasks?

We next wanted to see how well a single evaluator (which encapsulates a configurable prompt) generalizes across the different tasks. We used GPT-4 for prompt comparisons to ensure the evaluation was based on prompt effectiveness rather than model capability.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0fa_image-37.png)Evaluator accuracy over each dataset

Table of Results

 The following results contain the accuracy/null rate of the evaluation outputs using each evaluator, when using GPT-4 as the judge.

Datasetcot_qalabeled_criteriaqaCarb-IE Correct1.00 / 0.000.98 / 0.011.00 / 0.00Carb-IE Incorrect0.76 / 0.000.98 / 0.010.98 / 0.00Opus100 - Correct0.98 / 0.000.87 / 0.000.98 / 0.00Opus100 - Incorrect0.99 / 0.011.00 / 0.000.99 / 0.00Web Q&amp;A - Correct1.00 / 0.000.95 / 0.001.00 / 0.00Web Q&amp;A - Incorrect1.00 / 0.001.00 / 0.001.00 / 0.00

The default &quot;qa&quot; prompt most consistently produced the expected answers, especially when compared to the chain-of-thought QA evaluator and the general criteria evaluator. In the Carb-IE Incorrect split, which tests the correctness of extracted knowledge triplets,  the chain-of-thought QA evaluator underperformed significantly. It failed to penalize for extra, irrelevant triplets, revealing the limitation of applying a general &quot;quiz-style&quot; prompt to specialized tasks if without providing additional information.

Below are some examples to illustrate the relative behavior of the three evaluators on the same extraction data point:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0f4_cot_qa.png)Chain-of-thought QA evaluator (left), QA Evaluator (middle), and Criteria evaluator (right) outputs for a single dataset example.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0f1_qa.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0eb_labeled_criteria.png)

The links in the images show how the chain-of-thought QA evaluator ([link](https://smith.langchain.com/public/5951139f-8f0d-46cb-8d4e-2e1d2634e83d/r?ref=blog.langchain.com) to run) disregards the extra information in its final grade, whereas both the standard QA ([link](https://smith.langchain.com/public/5847c001-e519-4b57-94ec-680760b3a0f9/r?ref=blog.langchain.com))  and labeled criteria ([link](https://smith.langchain.com/public/cea1d2f8-66eb-4eb9-9508-444a8497759d/r?ref=blog.langchain.com)) evaluators appropriately mark the prediction as &quot;incorrect&quot; for including spurious information.

## Additional Insights

Two important observations also emerged from our tests:

- **At the time of testing, Claude-2 was sometimes prone to inconsistencies**:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0ee_image-46.png)

In [test](https://smith.langchain.com/public/ab0cbb96-e359-4efc-9843-c11dc61a15a7/r?ref=blog.langchain.com) above, Claude-2 wrongly included &quot;Texas&quot; in its reference answer. Similarly, when [using a different prompt](https://smith.langchain.com/public/ab0cbb96-e359-4efc-9843-c11dc61a15a7/r?ref=blog.langchain.com), the model gets the chain of thought &quot;reasoning&quot; correct while still printing out the wrong answer.

2. **Zero-shot language models, like GPT-4 and Claude-2, carry inherent biases.** These models can over-rely on their pre-trained knowledge, even when it conflicts with the actual data. For instance, when evaluating the example input &quot;who is the CEO of Twitter&quot; in [the linked run](https://smith.langchain.com/public/99c6fb34-6138-4dc7-8e4d-7c897ffe4ea1/r?ref=blog.langchain.com),

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1443d7d286a58faa0fd_image-39.png)

The GPT-4 based model marked the prediction of &quot;Elon Musk&quot; as incorrect, despite the reference answer providing the same information.

This problem can often be mitigated by refining the prompt or providing more context to the model. It is important to spot check your evaluation results to make sure they correspond with your intuition, especially if your task involves names or concepts where the model may have a &quot;high confidence&quot; in its trained knowledge.

### What&#x27;s Next?

While tweaks in prompt and output parsing have improved reliability, there are further enhancements that could further  implement:

- Offer more default flexibility in grading scales, backed by reliable prompts to interpret each grade.
- Further examine the impact of using few-shot examples in the prompts.
- Incorporate function calling for GPT-3.5 models to generate more reliable

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)