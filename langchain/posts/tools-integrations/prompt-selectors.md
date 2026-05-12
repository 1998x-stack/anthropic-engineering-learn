---
title: "Prompt Selectors"
author: "LangChain Accounts"
date: "2023-03-08"
url: "https://www.langchain.com/blog/prompt-selectors"
---

LangChainOpen Source

# Prompt Selectors

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 8, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb2522c7f205b929c99a4_photo-1483213097419-365e22f0f258.jpeg)One common complaint we&#x27;ve heard is that the default prompt templates do not work equally well for all models. This became especially pronounced this past week when OpenAI released a ChatGPT API. This new API had a completely new interface ([which required new abstractions](https://blog.langchain.com/chat-models/)) and as a result many users noticed issues with old prompts no longer working. Although we quickly added support for this model, many users noticed that prompt templates that worked well for GPT-3 did not work well in the chat setting.

All chains expose ways to customize these prompt templates, so there&#x27;s always the option to let users pass in prompts that work better. But we want to do better than that. One goal of having chains with default prompt templates is to offer functionality that &quot;Just Works&quot; out of the box. If different models expect different types of prompts, this breaks down.

Our solution for this is to introduce a concept of a `PromptSelector`. Rather than define a default `PromptTemplate` for each chain, we will move towards defining a `PromptSelector` for each chain. If no prompt is specified by the user, the `PromptSelector` will select a `PromptTemplate` to use based on the model that is passed in.

For an example of this in action, check out the following examples:

### Python

[Code Definition](https://github.com/hwchase17/langchain/blob/master/langchain/chains/prompt_selector.py?ref=blog.langchain.com)

[Full Example](https://github.com/hwchase17/langchain/blob/master/langchain/chains/question_answering/stuff_prompt.py?ref=blog.langchain.com)

Snippet:

`PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=PROMPT, conditionals=[(is_chat_model, CHAT_PROMPT)]
)`

### In JS/TS:

[Code Definition](https://github.com/hwchase17/langchainjs/blob/main/langchain/src/chains/prompt_selector.ts?ref=blog.langchain.com)

[Full Example](https://github.com/hwchase17/langchainjs/blob/main/langchain/src/chains/question_answering/stuff_prompts.ts?ref=blog.langchain.com)

Snippet:

`export const QA_PROMPT_SELECTOR = new ConditionalPromptSelector(
  DEFAULT_QA_PROMPT,
  [[isChatModel, CHAT_PROMPT]]
);`

Both these examples show the same thing. We define a default prompt, but then if a condition (`isChatModel`) is met we switch to a different prompt. This is also extendable to an arbitrary list of &quot;conditions&quot; and corresponding prompts&quot;

This is a very simple concept, but we hope it gives us (and other developers) the flexibility to define chains that &quot;Just Work&quot; out of the box for any model. Although the immediate use case is for switching between prompts for ChatModels (like ChatGPT) vs more traditional models (like GPT-3), we also envision this allow switching between different model providers (eg OpenAI vs Cohere) and even model versions (eg GPT-3 vs GPT-4) down the road.

It will take some time to transition over to these selectors, but we started with some of the more popular chains and intend to transition over as fast we can. As always, feedback and help from the community is greatly appreciated!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)Agent ArchitectureDeep AgentsOpen Source

#### Running Subagents in the Background

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)Hunter LovellColin FrancisApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/running-subagents-in-the-background)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)