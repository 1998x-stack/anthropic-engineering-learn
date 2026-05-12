---
title: "Multi Needle in a Haystack"
author: "LangChain Accounts"
date: "2024-03-13"
url: "https://www.langchain.com/blog/multi-needle-in-a-haystack"
---

Tutorials &amp; How-Tos

# Multi Needle in a Haystack

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaMarch 13, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00af4d459ecdf5fca6d_multi-needle-figure-2-1.png)

## Key Links

- [Video](https://youtu.be/UlmyyYQGhzc?ref=blog.langchain.com)
- [Code](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/tree/main?ref=blog.langchain.com)

## Overview

Interest in long context LLMs is surging as context windows expand to [1M](https://www.anthropic.com/news/claude-3-family?ref=blog.langchain.com) [tokens](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/?ref=blog.langchain.com). One of the most popular and cited benchmarks for long context LLM retrieval is [Greg Kamradt&#x27;s](https://twitter.com/GregKamradt?ref=blog.langchain.com) [Needle in A Haystack](https://twitter.com/GregKamradt/status/1722386725635580292?lang=en&amp;ref=blog.langchain.com): a fact (needle) is injected into a (haystack) of context (e.g., Paul Graham [essays](https://www.ycombinator.com/library/carousel/Essays%20by%20Paul%20Graham?ref=blog.langchain.com)) and the LLM is asked a question related to this fact. This explores retrieval across context length and document placement.

But, this isn&#x27;t fully reflective of many [retrieval augmented generation (RAG)](https://github.com/langchain-ai/rag-from-scratch?ref=blog.langchain.com) applications; RAG is often focused on retrieving multiple facts (from an index) and then reasoning over them. We present a new benchmark that tests exactly this. In our `Multi-Needle + Reasoning` benchmark we show two new results:

- Performance degrades as you ask LLMs to retrieve more facts
- Performance degrades when the LLM has to reason about retrieved facts

See below plot for a summary of the results: as the number of needles increases, retrieval decreases; and *reasoning* over those needles is worse than just retrieval.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00af4d459ecdf5fca6d_multi-needle-figure-2-1.png)

We also show (similar to [previous benchmarks](https://twitter.com/GregKamradt/status/1722386725635580292?lang=en&amp;ref=blog.langchain.com)) that performance decreases as more and more context is passed in. However, we additionally investigate not just overall performance but **why** performance drops when retrieving multiple needles. Looking at the heatmap of results below, we can see that when retrieving multiple needles GPT-4 consistently retrieves needles towards the end while ignoring needles at the beginning, similar to the [single needle studies](https://twitter.com/GregKamradt/status/1722386725635580292?lang=en&amp;ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00bf4d459ecdf5fca7b_image-13-1.png)

Below we&#x27;ll walk through benchmark usage and discuss results on GPT-4.

## Usage

To perform a `Multi-Needle + Reasoning` evaluation, a user only needs three things: (1) A `question` that requires multiple needles to answer, (2) an `answer` derived from the needles, and (3) `list of needles` to be inserted into the context.

We extended Greg Kamradt&#x27;s [`LLMTest_NeedleInAHaystack`](https://github.com/gkamradt/LLMTest_NeedleInAHaystack?ref=blog.langchain.com) repo to support multi-needle evaluation and [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) as an valuator. Using LangSmith for evaluation, we [create](https://docs.smith.langchain.com/evaluation/faq/datasets-webapp?ref=blog.langchain.com) a LangSmith eval set with items (1) `question` and (2) `answer` above.

As an example, lets use [this](https://twitter.com/alexalbert__/status/1764722513014329620?ref=blog.langchain.com) case study where the needle was a combination of pizza ingredients. We create a new LangSmith eval set ([here](https://smith.langchain.com/public/d6b47e6e-8279-4452-bd22-d6c8b839f1a0/d?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D&amp;chartedColumn=latency_p50&amp;ref=blog.langchain.com)) named `multi-needle-eval-pizza-3` with our `question` and `answer`:

`question:
What are the secret ingredients needed to build the perfect pizza?

answer:
The secret ingredients needed to build the perfect pizza are figs, prosciutto, and goat cheese.`

Question, Answer pairs for LangSmith `multi-needle-eval-pizza-3` eval set

Once we&#x27;ve created a dataset, we with few flags:

- `document_depth_percent_min` - the depth of the first needle. The remaining needles are inserted at roughly equally spaced intervals after the first.
- `multi_needle` -  flag to run multi-needle evaluation
- `needles` - the full list of needles to inject into the context
- `evaluator` - choose `langsmith`
- `eval_set` - choose the eval set we created `multi-needle-eval-pizza-3`
- `context_lengths_num_intervals` - number of context lengths to test
- `context_lengths_min` (and max) - context length bounds to test

We can run this to execute the evaluation:

`python main.py --evaluator langsmith --context_lengths_num_intervals 6 --document_depth_percent_min 5 --document_depth_percent_intervals 1 --provider openai --model_name &quot;gpt-4-0125-preview&quot; --multi_needle True --eval_set multi-needle-eval-pizza-3 --needles &#x27;[ &quot; Figs are one of the secret ingredients needed to build the perfect pizza. &quot;, &quot; Prosciutto is one of the secret ingredients needed to build the perfect pizza. &quot;,  &quot; Goat cheese is one of the secret ingredients needed to build the perfect pizza. &quot;]&#x27;  --context_lengths_min 1000 --context_lengths_max 120000   `

Command to run multi-needle evaluation using LangSmith

This will kick off a workflow below. It will insert the needles into the haystack, prompt the LLM to generate a response to the `question` using the context with the inserted needles, and evaluate whether the generation correctly retrieved the needles using the ground truth `answer` and the logged needles that were inserted.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00bf4d459ecdf5fca81_image-4.png)Workflow for Multi-Needle + Reasoning evaluation

## GPT-4 Retrieval Results

To test multi-needle retrieval for GPT-4, we built three LangSmith eval sets:

- `multi-needle-eval-pizza-1` [here](https://smith.langchain.com/public/af0f1c89-3993-4ded-91c2-29eebef67582/d?ref=blog.langchain.com) - Insert a single needle
- `multi-needle-eval-pizza-3` [here](https://smith.langchain.com/public/d6b47e6e-8279-4452-bd22-d6c8b839f1a0/d?ref=blog.langchain.com) - Insert three needles
- `multi-needle-eval-pizza-10` [here ](https://smith.langchain.com/public/74d2af1c-333d-4a73-87bc-a837f8f0f65c/d?ref=blog.langchain.com)- Insert ten needles

We evaluate the ability of [GPT4](https://openai.com/blog/new-models-and-developer-products-announced-at-devday?ref=blog.langchain.com) (128k token context length) to retrieve 1, 3, or 10 needles in a single turn for small (1000 token) and large (120,000 token) context lengths. All commands run are [here](https://mirror-feeling-d80.notion.site/Multi-Needle-Evaluation-528e8e976a264ef3be2b145003c010e0?pvs=4&amp;ref=blog.langchain.com). All resulting generations with public links to LangSmith traces are [here](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/viz/multi-needle-datasets/gpt4_retrieval.csv?ref=blog.langchain.com). Here is a summary figure of our results:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00bf4d459ecdf5fca7e_image-12.png)

There are clear observations:

- Performance degrades at the number of needles increases from 1 to 10
- Performance degrades as the context increases from 1000 to 120,000 tokens

To explore and validate these results, we can drill into LangSmith traces: [here](https://smith.langchain.com/public/dddfcdc1-bc9a-4299-a5a6-55ba13d54a77/r/ca6e02a2-b472-49ff-af12-b70f44c0de1f?ref=blog.langchain.com) is one LangSmith trace where we inserted 10 needles. Here is the `GPT-4` generation:

`The secret ingredients needed to build the perfect pizza include espresso-soaked dates, gorgonzola dolce, candied walnuts, and pear slices.`

GPT-4 generation for replicate 1 for 10 needles, 24,800 token context

Only **four** of the `secret ingredients` are in the generation. Based on the [trace](https://smith.langchain.com/public/dddfcdc1-bc9a-4299-a5a6-55ba13d54a77/r/5c8da4fe-9294-456f-9620-7d59dde0809f?ref=blog.langchain.com), we verify that all 10 needles are in the context and we [log](https://docs.google.com/spreadsheets/d/1FAxyJHi2CyrfYoupFz46xvT4AgyI2akBVxQ_ykFtZKo/edit?usp=sharing&amp;ref=blog.langchain.com) the inserted needle order:

`* Figs
* Prosciutto
* Smoked applewood bacon
* Lemon
* Goat cheese
* Truffle honey
* Pear slices
* Espresso-soaked dates
* Gorgonzola dolce
* Candied walnuts `

Order of the 10 needles placed in the context

From this we can confirm that the four `secret ingredients` in the generation are the **last four** needles placed in our context. This provokes an interesting point about **where** retrieval fails. Greg&#x27;s [single needle](https://twitter.com/GregKamradt/status/1722386725635580292?lang=en&amp;ref=blog.langchain.com) analysis showed GPT-4 retrieval failure when the needle is place towards the start of the document.

Because we log the placement of each needle, we can explore this too: the below heatmap shows 10 needle retrieval with respect to context length. Each column is a single experiment when we ask GPT-4 to retrieve 10 needles in the context.

As the context length grows, we also see retrieval failure towards the start of the document. The effect appears to start earlier in the multi-needle case (around 25k tokens) than the single needle case (which started around 73k tokens for GPT-4).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00bf4d459ecdf5fca7b_image-13-1.png)

## GPT-4 Retrieval &amp; Reasoning

RAG is often focused on retrieving multiple facts (from an indexed corpus of documents) and then reasoning over them. To test this, we build 3 datasets that build on the above by asking for the **first letter** of all secret ingredients. This requires retrieval of ingredients and reasoning about them to answer the question.

- `multi-needle-eval-pizza-reasoning-1` - [here](https://smith.langchain.com/public/a85db85f-ee45-4a39-a1ac-52f7279134ac/d?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D&amp;chartedColumn=latency_p50&amp;ref=blog.langchain.com)
- `multi-needle-eval-pizza-reasoning-3` - [here](https://smith.langchain.com/public/270cd9cd-154d-4ba9-8b34-7b6537007867/d?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D&amp;chartedColumn=latency_p50&amp;ref=blog.langchain.com)
- `multi-needle-eval-pizza-reasoning-10`- [here](https://smith.langchain.com/public/00658b64-6199-48fc-9443-1478aadbe19a/d?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D&amp;chartedColumn=latency_p50&amp;ref=blog.langchain.com)

Note that this is an extremely simple form of reasoning. For future benchmarks, we want to include different levels of reasoning.

We compared the fraction of correct answers for 3 replicates between retrieval and **retrieval + reasoning**. All data with traces is [here](https://github.com/gkamradt/LLMTest_NeedleInAHaystack/blob/main/viz/multi-needle-datasets/gpt4_reasoning.csv?ref=blog.langchain.com). Retrieval and reasoning both degrade as the context length increases, reasoning lags retrieval. This suggests that retrieval may set an upper bound on reasoning performance, as expected.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb00af4d459ecdf5fca6d_multi-needle-figure-2-1.png)

## Conclusion

The emergence of long context LLMs is extremely promising. In order to use them with or in place of external retrieval systems, it is critical to understand their limitations. The `Multi-Needle + Reasoning` benchmark can characterize the performance of long context retrieval relative to using a traditional RAG approach.

We can draw a few general insights, but further testing is needed:

- `No retrieval guarantees` -  Multiple facts are not guaranteed to be retrieved, especially as the number of needles and context size increases.
- `Different patterns of retrieval failure ` -   GPT-4 fails to retrieve needles towards the start of documents as context length increases.
- `Prompting matters` - Following insights mentioned [here](https://www.youtube.com/watch?v=aswbFKE_0Dg&amp;ref=blog.langchain.com) and [here](https://www.anthropic.com/news/claude-2-1-prompting?ref=blog.langchain.com), specific prompt formulations may be needed to improve recall with certain LLMs.
-  `Retrieval vs reasoning` - Performance degrades when the LLM is asked to reason about the retrieved facts.

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