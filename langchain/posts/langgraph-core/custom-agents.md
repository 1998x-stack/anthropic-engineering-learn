---
title: "Custom Agents"
author: "LangChain Accounts"
date: "2023-04-03"
url: "https://www.langchain.com/blog/custom-agents"
---

Agent ArchitectureLangChain

# Custom Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 3, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb246c588d5fac7b931bc_photo-1589254065878-42c9da997008.jpeg)One of the most common requests we&#x27;ve heard is better functionality and documentation for creating custom agents. This has always been a bit tricky - because in our mind it&#x27;s actually still very unclear what an &quot;agent&quot; actually is, and therefor what the &quot;right&quot; abstractions for them may be. Recently, we&#x27;ve felt some of the abstractions starting to come together, so we did a big push across both our [Python](https://github.com/hwchase17/langchain?ref=blog.langchain.com) and [TypeScript](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com) modules to better enforce and document these abstractions. Please see below for links to those technical docs, and then a description of the abstractions we&#x27;ve introduced and future directions.

- [Python Custom Agent Docs](https://python.langchain.com/docs/modules/agents/how_to/custom_llm_agent?ref=blog.langchain.com)
- [TypeScript Custom Agent Docs](https://js.langchain.com/docs/modules/agents/agents/custom_llm?ref=blog.langchain.com)

**TL;DR:** we&#x27;ve introduced a `BaseSingleActionAgent` as the highest level abstraction for an agent that can be used in our current `AgentExecutor`. We&#x27;ve added a more practical `LLMSingleActionAgent` that implements this interface in a simple and extensible way (PromptTemplate + LLM + OutputParser).

## BaseSingleActionAgent

The most base abstraction we&#x27;ve introduced is a `BaseSingleActionAgent`. As you can tell by the name, we don&#x27;t consider this a base abstraction for all agents. Rather, we consider this the base abstraction for a family of agents that predicts a single action at a time.

A `SingleActionAgent` is used in an our current `AgentExecutor`. This `AgentExecutor` can largely be thought of as a loop that:

- Passes user input and any previous steps to the Agent
- If the Agent returns an `AgentFinish`, then return that directly to the user
- If the Agent returns an `AgentAction`, then use that to call a tool and get an `Observation`
- Repeat, passing the `AgentAction` and `Observation` back to the Agent until an `AgentFinish` is emitted.

`AgentAction` is a response that consists of `action` and `action_input`. `action` refers to which tool to use, and `action_input` refers to the input to that tool.

`AgentFinish` is a response that contains the final message to be sent back to the user. This should be used to end an agent run.

If you are interested in this level of customizability, check out [this walkthrough](https://python.langchain.com/docs/modules/agents/how_to/custom_agent?ref=blog.langchain.com). For most use cases, however, we would recommend using the abstraction below.

## LLMSingleActionAgent

Another class we&#x27;ve introduced is the `LLMSingleActionAgent`. This is a concrete implementation of the `BaseSingleActionAgent`, but is highly modular so therefor is highly customizable.

The `LLMSingleActionAgent` consists of four parts:

- `PromptTemplate`: This is the prompt template that can be used to instruct the language model on what to do
- `LLM`: This is the language model that powers the agent
- `stop` sequence: Instructs the `LLM` to stop generating as soon as this string is found
- `OutputParser`: This determines how to parse the output of an `LLM` into an `AgentAction` or `AgentFinish` object

The logic for combining these is:

- Use the `PromptTemplate` to turn the input variables (inlcuding user input and any previous `AgentAction`, `Observation` pairs) into a prompt
- Pass the prompt to the `LLM`, with a specific `stop` sequence
- Parse the output of the `LLM` into an `AgentAction` or `AgentFinish` object

These abstraction can be used to customize your agent in a lot of ways. For example:

- Want to give your agent some personality? Use the `PromptTemplate`!
- Want to format the previous `AgentAction`, `Observation` pairs in a specific way? Use the `PromptTemplate`!
- Want to use a custom or local model? Write a custom LLM wrapper and pass that in as the LLM!
- **Is the output parsing too brittle, or you want to handle errors in a different way? Use a custom OutputParser!**

(The last one is in bold, because that&#x27;s the one we&#x27;v maybe heard the most)

We imagine this being the most practically useful abstraction. Please see the documentation links at the beginning of the blog for links to concrete Python/TypeScripts guides for getting started here.

## Future Directions

We hope these abstractions have clarified some of our thinking around agents, as well as open up places where we hope the community can contribute. In particular:

We are very excited about other examples of `SingleActionAgents`, like:

- Using embeddings to do tool selection before calling an `LLM`
- Using a `ConstitutionalChain` instead of an `LLMChain` to improve reliability

We are also excited about other types of agents (which will require new `AgentExecutors`), like:

- Multi-action agents
- Plan-execute agents

If any of those sound interesting, we are always willing to work with folks to implement their ideas! The best way is probably to do some initial work, open a RFC pull request, and we&#x27;re happy to go from there :)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)