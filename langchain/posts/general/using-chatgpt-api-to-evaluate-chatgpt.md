---
title: "Using the ChatGPT API to evaluate the ChatGPT API"
author: "LangChain Accounts"
date: "2023-03-02"
url: "https://www.langchain.com/blog/using-chatgpt-api-to-evaluate-chatgpt"
---

Observability &amp; EvalsTutorials &amp; How-Tos

# Using the ChatGPT API to evaluate the ChatGPT API

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 2, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb255a83bd2fbf570ce1a_photo-1593115057322-e94b77572f20.jpeg)OpenAI released a new [ChatGPT API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis?ref=blog.langchain.com) yesterday. Lots of people were excited to try it. But how does it actually compare to the existing API? It will take some time before there is a definitive answer, but here are some initial thoughts. Because I&#x27;m lazy, I also enrolled the help of the ChatGPT API itself to help do this evaluation. Confused? Don&#x27;t be. Let&#x27;s dive in.

Relevant links:

- [Evaluation Notebook](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com)
- [ChatGPT PR](https://github.com/hwchase17/langchain/pull/1375?ref=blog.langchain.com)
- [ChatGPT PR Discussion](https://github.com/hwchase17/langchain/discussions/1376?ref=blog.langchain.com)

## What task are we evaluating?

In this article we will evaluate the performance of a chain on [question answering](https://python.langchain.com/docs/use_cases/question_answering/?ref=blog.langchain.com) over a particular dataset. This chain takes a query, does a &quot;retrieval&quot; step to look up relevant documents in a vector store, and then does a &quot;generation&quot; step to pass them, along with the original query, to a model to get back an answer. We will hold the &quot;retrieval&quot; step constant, so we are just evaluating the &quot;generation&quot; step of the chain.

## What models/prompts are we comparing?

First up, we&#x27;ve got the standard `text-davinci-003` model, with the standard [`VectorDBQAChain`](https://python.langchain.com/docs/modules/chains/popular/vector_db_qa?ref=blog.langchain.com) prompts.

We want to compare this to ChatGPT. There would be two potential ways to do this. One would be to use a wrapper that and treat ChatGPT has just another LLM. Another would be to try to use the ChatGPT API more natively.

What do I mean by that? The ChatGPT API differs from the GPT-3 API in that it takes in a list of messages (rather than a single string) and returns a message. These messages are essentially dicts that have two fields: `content` and `role`. Both are used in the prompt. The `content` field can be anything, while the `role` field should be one of `user`, `system`, or `assistant`. Presumably, the model is trained to treat the `user` messages as human messages, `system` messages as some system level configuration, and `assistant` messages as previous chat responses from the assistant.

So how can we use this to do question answering? Let&#x27;s think back to the information we need to pass in. There are three components:

- Instructions (about how it should answer, format, etc)
- The user question
- Retrieved pieces of content

Instructions seem like they should be the first message and have `role` of `system`. The user question seems like it should have `role` of `user`, but is a little bit less clear where it should go. It is extremely unclear what `role` or what position in the list of messages the retrieved pieces of content should go. Note that I say &quot;should&quot;, but our understanding might change in the near future.

Some ideas for how to combine the user question and retrieved pieces of content:

- Put the pieces of content in the system message and tell the model to only use that information.
- Put each piece of content as its own message (with either `assistant` or `user` roles) in the middle of the conversation
- Put the user question first, and then follow it with a message for each piece of content (with role `assistant`) and then another `user` message asking for it to answer given those pieces of content.

Lots of choices! For the purposes of this experiment I went with option 2, set role to be `user`, and instructed the model to only use pieces of information that the user had told it before when answering.

## How did we evaluate this?

We used the simple &quot;State of the Union Address&quot; that we commonly use as a toy example. We then generated a bunch of questions and corresponding answers from this dataset. This was done using GPT-3, using our [existing question/answering generation pipeline](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com). We then ran each question through the two chains (GPT3 and ChatGPT). We then evaluated the answers - using GPT3 and ChatGPT. Specifically, we have another chain called the [`QAEvalChain`](https://python.langchain.com/docs/guides/evaluation/data_augmented_question_answering?ref=blog.langchain.com#evaluate), which uses GPT3 to evaluate question answering responses. We created a corresponding [`QAEvalChatChain`](https://github.com/hwchase17/langchain/blob/harrison/memory-chat/langchain/evaluation/qa/chat_eval_chain.py?ref=blog.langchain.com) which uses the ChatGPT API to do a similar thing. To add a cherry on top, we then created a [`QACompChatChain`](https://github.com/hwchase17/langchain/blob/harrison/memory-chat/langchain/evaluation/qa/chat_comp_chain.py?ref=blog.langchain.com) which takes in the question, the true answer, and both predicted answers and compares them.

In this post, we will look mostly as the results of the evaluators. So in a meta way, we are using a language model to evaluate a language model, but then (for the time being) we are still the ones evaluating the evaluator model.

## So what were the results?

See our full results [here](https://langchain.readthedocs.io/en/harrison-memory-chat/use_cases/evaluation/data_augmented_question_answering_comparision.html?ref=blog.langchain.com). For speed/simplicity, we only evaluated 7 questions, so this suffers from incredibly small sample size issues.

Note that the imported code is still on a branch as we work to figure out the best abstractions for this new Chat paradigm.

First of all, how did GPT3 grade the two models?

- GPT3 grading GPT3: 4/7
- GPT3 grading ChatGPT: 4/7

And how did ChatGPT grade the two models?

- ChatGPT grading GPT3: 5/7
- ChatGPT grading ChatGPT: 4/7

It&#x27;s interesting to look where the differences lie. There was one example that GPT3 graded as incorrect for both GPT3 and ChatGPT, but ChatGPT graded as correct for both. And there was a separate example that GPT3 graded as correct for both, but ChatGPT graded as incorrect for ChatGPT. Let&#x27;s take a look.

First, the example that GPT3 graded as incorrect but ChatGPT as correct:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb256a83bd2fbf570ce5a_example0.png)

Here it looks like GPT3 may have graded it as incorrect due it the verbosity of the answers, but ChatGPT didn&#x27;t mind that. An alternative explanation could be that ChatGPT was more able to actually understand that &quot;praised her legal ability&quot; was consistent with the answers given.

Next, the example that GPT3 graded as correct for both, but ChatGPT graded as incorrect for ChatGPT.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb256a83bd2fbf570ce64_example4-1.png)

We can see in this example that the GPT3 is nearly exactly the same as the real answer. This is almost certainly due to the fact that we used GPT3 to generate the question/answer pairs. The ChatGPT answer is more verbose, and while not technically incorrectly it is not as specific and direct as the GPT3 answer. Again, this is likely due to using GPT3 to generate the question/answer pairs. Note for self: may want to manually curate a test set for the future.

## What about the direct comparison?

The final evaluation we did was give the question, the answer, and both predicted answers to ChatGPT and ask it to compare the answers. Synthesizing the results here:

- GPT3 is more succinct than ChatGPT
- ChatGPT is more detailed than GPT3
- ChatGPT is more polite than GPT3

Keep in mind, that this is not just the base model, but also the prompts used. So not truly a comparison between the two models, but rather the existing chains.

## Next steps

Still lots to be done in exploring the ChatGPT API! How can you best use the `role` parameter? What does the `system` role actually do? What are the right abstractions for this new type of API?

Only time will tell. Exciting times!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8a01c18c14b60cd4372_76.webp)LangSmithObservability &amp; Evals

#### Human judgment in the agent improvement loop

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2d3bf32d4fc06a289383_rahul-verma.png)Rahul VermaApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/human-judgment-in-the-agent-improvement-loop)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce9138b145f1419b6b38b_74--2-.webp)Observability &amp; Evals

#### Better Harness: A Recipe for Harness Hill-Climbing with Evals

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyApril 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)