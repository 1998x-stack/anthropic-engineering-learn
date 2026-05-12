---
title: "Autonomous Agents &amp; Agent Simulations"
author: "LangChain Accounts"
date: "2023-04-19"
url: "https://www.langchain.com/blog/agents-round"
---

Observability &amp; Evals

# Autonomous Agents &amp; Agent Simulations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 18, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb23bc588d5fac7b92956_photo-1569087682520-45253cc2e0ee.jpeg)Over the past two weeks, there has been a massive increase in using LLMs in an agentic manner. Specifically, projects like [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT?ref=blog.langchain.com), [BabyAGI](https://github.com/yoheinakajima/babyagi?ref=blog.langchain.com), [CAMEL](https://github.com/lightaime/camel?ref=blog.langchain.com), and [Generative Agents](https://blog.langchain.com/content/files/abs/2304.xml) have popped up. The LangChain community has now implemented some parts of all of those projects in the LangChain framework. While researching and implementing these projects, we’ve tried to best understand what the differences between them are and what the novel features of each are. This blog is an explanation of what we’ve learned.

Note: this is a fairly technical blog. It assumes some familiarity with LangChain and these related projects. If you are not familiar with these projects, it may be helpful to read a more introductory piece (like [this fantastic one](https://t.co/vgZhvKhscG?ref=blog.langchain.com) by Sophia Yang).

**TL;DR:**

- **The “**[**autonomous agents**](https://python.langchain.com/en/latest/use_cases/autonomous_agents.html?ref=blog.langchain.com)**” projects (BabyAGI, AutoGPT) are largely novel in their long-term objectives, which necessitate new types of planning techniques and a different use of memory.**
- **The “**[**agent simulation**](https://python.langchain.com/en/latest/use_cases/agent_simulations.html?ref=blog.langchain.com)**” projects (CAMEL, Generative Agents) are largely novel for their simulation environments and long-term memory that reflects and adapts based on events.**

We also discuss what parts of each project we’ve replicated in the LangChain framework, and why we chose those parts. Implementing these in the LangChain framework has the benefits of:

- Allowing easy switching between [LLM providers](https://python.langchain.com/docs/modules/model_io/models/?ref=blog.langchain.com)
- Allowing easy switching of [VectorStore providers](https://python.langchain.com/docs/modules/data_connection/vectorstores/?ref=blog.langchain.com) (or, [alternative retrieval methods](https://python.langchain.com/docs/modules/data_connection/retrievers/?ref=blog.langchain.com))
- Allowing connectivity to LangChain’s collection of [tools](https://python.langchain.com/docs/modules/agents/tools/?ref=blog.langchain.com)
- Allowing connectivity to the LangChain ecosystem in general

## Background

First, let’s start with some background context. What are “agents” and why are they important? For this discussion, we will use LangChain nomenclature, although it’s worth noting that this field is so new there’s no super standard terminology.

Agents generally refer to the idea of using a language model as a reasoning engine and connecting it to two key components: tools and memory.

Tools help connect the LLM to other sources of data or computation. Examples of tools include search engines, APIs, and other datastores. Tools are useful because LLMs only have knowledge of what they were trained on. This knowledge can quickly get out-of-date. In order to overcome this limitations, tools can fetch up-to-date data and insert it as context into the prompt. Tools can also be used to take actions (e.g. run code, modify files, etc), and the outcome of that action can then be observed by the LLM and factored into their decision on what to do next.

Memory helps the agent remember previous interactions. These interactions can either be with other entities (humans or other agents) or with tools. These memories can either be short term (e.g. a list of the previous 5 tool usages) or long term (tool usages from the past that seem most similar to the current situation).

Within LangChain, we refer to an “Agent” as the LLM that decides what actions to take; “Tools” as the actions an Agent can take; “Memory” the act of pulling in previous events, and an AgentExecutor as the logic for running an Agent in a while-loop until some stopping criteria is met.

The stereotypical LangChain Agent is based on the [Reasoning and Acting (ReAct) framework](https://blog.langchain.com/content/files/abs/2210.xml) proposed by Yao et all in November of 2022. This approach is characterized by the following algorithm:

- User gives an agent a task
- **Thought**: The agent “thinks” about what to do
- **Action/Action Input**: The agent decides what action to take (aka what tool to use) and what the input to that tool should be
- **Observation**: The output of the tool
- Repeat steps 2-4 until the Agent “thinks” it is done

When discussing other implementations and frameworks we will compare them to this algorithm.

## AutoGPT

**Links:**

- [Original Repo](https://github.com/Significant-Gravitas/Auto-GPT?ref=blog.langchain.com)
- [LangChain Implementation](https://python.langchain.com/docs/use_cases/autonomous_agents/autogpt?ref=blog.langchain.com)

**What is novel about this project?**

The main differences between the AutoGPT project and traditional LangChain agents can be attributed to different objectives. In AutoGPT, the goals are often more open ended and long running. This means that AutoGPT has a different AgentExecutor and different way of doing memory (both of which are more optimized for long running tasks). Previously, memory of agents in LangChain had two forms:

- Memory of agent steps: this was done by keeping a list of intermediate agent steps relevant for that task, and passing the full list to the LLM calls
- Memory of system: this remembered the final inputs and outputs (but forgot the intermediate agent steps)

Because AutoGPT is more long running, passing the full list of agent steps to the LLM call is no longer feasible. Instead, AutoGPT added a retrieval-based memory over the intermediate agent steps. Under the hood, this retrieval-based memory is doing doing semantic search over embeddings, using a VectorStore. Note that LangChain has this type of retrieval-based memory, but it was previously applied to **user-agent** interactions, not [agent-tool](https://python.langchain.com/docs/use_cases/autonomous_agents/autogpt?ref=blog.langchain.com) interations.

**How did we incorporate this into LangChain?**

We added a version of this to `langchain.experimental` - a place where we are putting more experimental and newer code while we figure out the proper abstractions. Specifically, we’ve implemented the prompt templating logic used, as well as `while` loop used to run the agent. We’ve made it compatible with LangChain LLM wrappers, LangChain VectorStores, and LangChain tools.

We’ve also created [this](https://python.langchain.com/docs/use_cases/autonomous_agents/autogpt?ref=blog.langchain.com) notebook showing how to use it.

## BabyAGI

**Links:**

- [Original Repo](https://github.com/yoheinakajima/babyagi?ref=blog.langchain.com)
- [LangChain Implementation](https://python.langchain.com/docs/use_cases/autonomous_agents/baby_agi?ref=blog.langchain.com)
- [LangChain Implementation with Tools](https://python.langchain.com/docs/use_cases/autonomous_agents/baby_agi_with_agent?ref=blog.langchain.com)

**What is novel about this project?**

The BabyAGI project differs from traditional LangChain Agents in the following regards:

- Similar to AutoGPT, it applies retrieval-based memory to intermediate agent-tool steps.
- It has separate planning and execution steps, where it plans a sequence of actions all at once (rather than just the next one)

Similar to AutoGPT, BabyAGI is designed for more long running tasks, which lead to both of these differences.

Let’s expand on the second point, since that is one of the more important and substantial differences. In the traditional LangChain Agent framework (and the AutoGPT framework), the agent thinks one step ahead at a time. For a given state of the world it think about what its next immediate action should be, and then does that action.

BabyAGI differs in that it explicitly plans out a sequence of actions. It then executes on the first one, and then uses the result of that to do another planning step and update it’s task list. Our intuition is that this enables it to execute better on more complex and involved tasks, by using the planning steps essentially as a state tracking system.. We’ve observed (anecdotally) that for tasks that require many steps, the traditional LangChain Agent can sometimes forget its original objective after a few steps, so planning all the steps ahead of time could be beneficial.

**How did we incorporate this into LangChain?**

Similar to AutoGPT, we added this to `langchain.experimental`. Specifically, we’ve implemented the prompt templating logic used, as well as `while` loop used to run the agent. We’ve made it compatible with LangChain LLM wrappers, LangChain vectorstores, and LangChain tools.

## Camel

**Links:**

- [Original Paper](https://blog.langchain.com/content/files/camel.pdf)
- [Original Repo](https://github.com/lightaime/camel?ref=blog.langchain.com)
- [LangChain Implementation](https://python.langchain.com/docs/use_cases/agent_simulations/camel_role_playing?ref=blog.langchain.com)

**What is novel about this project?**

The main novelty in this project comes from taking two agents, each with their own personality, and having them chat with each other. In this sense there are two novel components: the idea of having two agents interact with each other in a collaborative manner, and the specific simulation environment.

The idea of two agents interacting is not entirely new. Given the modular nature of LangChain, we have long been proponents of having agents use other agents as tools. However, what is novel about this type of interaction is that the two agents are poised as equals - in previous LangChain implementations there has always been one agent which calls the other as a tool, in a [&quot;stacking&quot;](https://twitter.com/mathemagic1an/status/1645096275392745477?s=20&amp;ref=blog.langchain.com) approach. This idea of putting both agents on equal footing, rather than having one use the other as a tool strikes a chord of being particularly interesting to see evolving behavior emerge.

Note that these agents can have different tools available to them and could be specialized around that. For example, you could have one agent that is armed with tools needed for coding, another with tools needed for interacting with linear, etc. So it is still possible to achieve a &quot;stacking&quot; effect (where you have different agents responsible for different things).

The second novel component was the particular simulation environment. This is a two sided conversation, and is not terribly complex but still the first implementation of this in a research setting we have seen.

**How did we incorporate this into LangChain?**

We added a notebook, largely reflecting the simulation environment (having two agents chatting with each other). We may look into making this simulation environment more available off-the-shelf in the future.

## Generative Agents

**Links:**

- [Original Paper](https://blog.langchain.com/content/files/abs/2304.xml)
- [Retriever Implementation](https://python.langchain.com/docs/modules/data_connection/retrievers/how_to/time_weighted_vectorstore?ref=blog.langchain.com)
- [LangChain Memory Implementation](https://python.langchain.com/docs/use_cases/agent_simulations/characters?ref=blog.langchain.com)

**What is novel about this project?**

There are two novel (and fairly complex) aspects to this project. The first is the simulation environment, which consists of 25 different agents. This seems fairly specific, and very complex, so we did not dive into this too much. The other aspect that is novel is the **long-term memory** they created for these agents.

We did a deep dive on this [earlier this week](https://twitter.com/hwchase17/status/1647987713449263106?s=20&amp;ref=blog.langchain.com). The agents’ memory is made up of:

- Importance reflection steps, to give each observation an importance score. This score can be used in retrieval down the line to fetch particularly important memories and ignore basic ones
- Reflection steps, to “pause” and think about what generalizations the agent has learned. These reflections can then be retrieved alongside normal memories. This reflection step can serve to condense information and observe patterns in recent memories
- A retriever that combines recency, relevancy to the situation, and importance. This can allow for surfacing of memories that similar to the situation at hand, happened a short while ago, and particularly important. All of these seem to be attributes that naturally reflect how we as human “retrieve” memories

All of these memory components are fairly novel, and extremely exciting to us.

**How did we incorporate this into LangChain?**

The retriever logic seemed generalizable so we added it as a [`TimeWeightedVectorStoreRetriever`](https://python.langchain.com/docs/modules/data_connection/retrievers/how_to/time_weighted_vectorstore?ref=blog.langchain.com).

We added a [notebook](https://python.langchain.com/docs/use_cases/agent_simulations/characters?ref=blog.langchain.com) showing off how to use the reflection steps + the new retriever to replicate part of the setup the paper described.

The simulation environment seemed complex and not super generalizable so we did not do any thing there.

## Conclusion

All of these projects rightfully garnered a lot of attention. We view them as two separate categories:

- [Autonomous Agents](https://python.langchain.com/docs/use_cases/autonomous_agents/?ref=blog.langchain.com), which have improved planning abilities
- [Agent Simulations](https://python.langchain.com/docs/use_cases/agent_simulations/?ref=blog.langchain.com), which have novel simulation environments and complex, evolving memory

We’re excited to have started implementing parts of these projects in the LangChain ecosystem, and look forward to seeing how the community uses these, adds to these, and combines these 🙂

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