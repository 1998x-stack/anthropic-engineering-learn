---
title: "Plan-and-Execute Agents"
author: "LangChain Accounts"
date: "2024-02-13"
url: "https://www.langchain.com/blog/planning-agents"
---

LangGraphAgent Architecture

# Plan-and-Execute Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 13, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb02fc588d5fac7b85a83_Will---agents---2-1-1.png)

### **Links **

- Plan-and-execute ([Python](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb?ref=blog.langchain.com), [JS](https://github.com/langchain-ai/langgraphjs/blob/main/examples/plan-and-execute/plan-and-execute.ipynb?ref=blog.langchain.com))
- LLMCompiler ([Python](https://github.com/langchain-ai/langgraph/blob/main/examples/llm-compiler/LLMCompiler.ipynb?ref=blog.langchain.com))
- ReWOO ([Python](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb?ref=blog.langchain.com))
- [Youtube](https://youtu.be/uRya4zRrRx4?ref=blog.langchain.com)

We’re releasing three agent architectures in LangGraph showcasing the “plan-and-execute” style agent design. These agents promise a number of improvements over traditional Reasoning and Action (ReAct)-style agents.

⏰ First of all, they can execute multi-step workflow ***faster****,* since the larger agent doesn’t need to be consulted after each action. Each sub-task can be performed without an additional LLM call (or with a call to a lighter-weight LLM).

💸 Second, they offer **cost savings** over ReAct agents. If LLM calls are used for sub-tasks, they typically can be made to smaller, domain-specific models. The larger model then is only called for (re-)planning steps and to generate the final response.

🏆 Third, they can **perform better** overall (in terms of task completions rate and quality) by forcing the planner to explicitly “think through” all the steps required to accomplish the entire task. Generating the full reasoning steps is a tried-and-true prompting technique to improve outcomes. Subdividing the problem also permits more focused task execution.

## Background

Over the past year, language model-powered agents and state machines have emerged as a promising design pattern for creating flexible and effective ai-powered products.

At their core, agents use LLMs as general-purpose problem-solvers, connecting them with external resources to answer questions or accomplish tasks.

LLM agents typically have the following main steps:

- Propose action: the LLM generates text to respond directly to a user or to pass to a function.
- Execute action: your code invokes other software to do things like query a database or call an API.
- Observe: react to the response of the tool call by either calling another function or responding to the user.

The [ReAct](https://arxiv.org/abs/2210.03629?ref=blog.langchain.com) agent is a great prototypical design for this, as it prompts the language model using a repeated thought, act, observation loop:

`Thought: I should call Search() to see the current score of the game.
Act: Search(&quot;What is the current score of game X?&quot;)
Observation: The current score is 24-21
... (repeat N times)`

A typical ReAct-style agent trajectory.

This takes advantage of [Chain-of-thought](https://arxiv.org/abs/2201.11903?ref=blog.langchain.com) prompting to make a single action choice per step. While this can be effect for simple tasks, it has a couple main downsides:

- It requires an LLM call for each tool invocation.
- The LLM only plans for 1 sub-problem at a time. This may lead to sub-optimal trajectories, since it isn&#x27;t forced to &quot;reason&quot; about the whole task.

One way to overcome these two shortcomings is through an explicit planning step. Below are two such designs we have implemented in LangGraph.

## **Plan-And-Execute**

🔗 [Python Link](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb?ref=blog.langchain.com)

🔗 [JS Link](https://github.com/langchain-ai/langgraphjs/blob/main/examples/plan-and-execute/plan-and-execute.ipynb?ref=blog.langchain.com)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb030c588d5fac7b85a9b_plan-and-execute.png)Plan-and-execute Agent

Based loosely on Wang, et. al.’s paper on [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091?ref=blog.langchain.com), and Yohei Nakajima’s [BabyAGI](https://github.com/yoheinakajima/babyagi?ref=blog.langchain.com) project, this simple architecture is emblematic of the planning agent architecture. It consists of two basic components:

- A **planner**, which prompts an LLM to generate a multi-step plan to complete a large task.
- **Executor**(s), which accept the user query and a step in the plan and invoke 1 or more tools to complete that task.

Once execution is completed, the agent is called again with a re-planning prompt, letting it decide whether to finish with a response or whether to generate a follow-up plan (if the first plan didn’t have the desired effect).

This agent design lets us avoid having to call the large planner LLM for each tool invocation. It still is restricted by serial tool calling and uses an LLM for each task since it doesn&#x27;t support variable assignment.

## Reasoning WithOut Observations

🔗 [Python Link ](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb?ref=blog.langchain.com)

In [ReWOO](https://arxiv.org/abs/2305.18323?ref=blog.langchain.com), Xu, et. al, propose an agent that removes the need to always use an LLM for each task while still allowing tasks to depend on previous task results. They do so by permitting variable assignment in the planner&#x27;s output. Below is a diagram of the agent design.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb030c588d5fac7b85aaa_rewoo.png)ReWOO Agent

Its **planner** generates a plan list consisting of interleaving &quot;Plan&quot; (reasoning) and &quot;E#&quot; lines. As an example, given the user query &quot;What are the stats for the quarterbacks of the super bowl contenders this year&quot;, the planner may generate the following plan:

`Plan: I need to know the teams playing in the superbowl this year
E1: Search[Who is competing in the superbowl?]
Plan: I need to know the quarterbacks for each team
E2: LLM[Quarterback for the first team of #E1]
Plan: I need to know the quarterbacks for each team
E3: LLM[Quarter back for the second team of #E1]
Plan: I need to look up stats for the first quarterback
E4: Search[Stats for #E2]
Plan: I need to look up stats for the second quarterback
E5: Search[Stats for #E3]`

Notice how the planner can reference previous outputs using syntax like `#E2` . This means it can execute a task list without having to re-plan every time.

The **worker** node loops through each task and assigns the task output to the corresponding variable. It also replaces variables with their results when calling subsequent calls.

Finally, the **Solver** integrates all these outputs into a final answer.

This agent design can be more effective than a naive plan-and-execute agent since each task can have only the required context (its input and variable values).

It still relies on sequential task execution, however, which can create a longer runtime.

## **LLMCompiler**

🔗 [Python Link ](https://github.com/langchain-ai/langgraph/blob/main/examples/llm-compiler/LLMCompiler.ipynb?ref=blog.langchain.com)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb030c588d5fac7b85a9e_llm-compiler-1.png)LLMCompiler Agent

The **LLMCompiler**, by [Kim, et. al.,](https://arxiv.org/abs/2312.04511?ref=blog.langchain.com) is an agent architecture designed to further increase the **speed** of task execution beyond the plan-and-execute and ReWOO agents described above, and even beyond OpenAI’s parallel tool calling.

The LLMCompiler has the following main components:

- **Planner**: streams a DAG of tasks. Each task contains a tool, arguments, and list of dependencies.
- **Task Fetching Unit** schedules and executes the tasks. This accepts a stream of tasks. This unit schedules tasks once their dependencies are met. Since many tools involve other calls to search engines or LLMs, the extra parallelism can grant a significant speed boost (the paper claims 3.6x).
- **Joiner**: dynamically replan or finish based on the entire graph history (including task execution results) is an LLM step that decides whether to respond with the final answer or whether to pass the progress back to the (re-)planning agent to continue work.

The key runtime-boosting ideas here are:

- **Planner** outputs are ***streamed;*** the output parser eagerly yields task parameters and their dependencies.
- The **task fetching unit **receives the parsed task stream and schedules tasks once all their dependencies are satisfied.
- Task arguments can be *variables,* which are the outputs of previous tasks in the DAG. For instance, the model can call `search(&quot;${1}&quot;)` to search for queries generated by the output of task 1. This lets the agent work even faster than the &quot;embarrassingly parallel&quot; tool calling in OpenAI.

By formatting tasks as a DAG, the agent can save precious time while invoking tools, leading to an overall better user experience.

## Conclusion

These three agent architectures are prototypical of the &quot;plan-and-execute&quot; design pattern, which separates an LLM-powered &quot;planner&quot; from the tool execution runtime. If your application requires multiple tool invocations or API calls, these types of approaches can reduce the time it takes to return a final result and help you save costs by reducing the frequency of calls to more powerful LLMs.

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