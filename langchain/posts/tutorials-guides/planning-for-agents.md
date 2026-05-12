---
title: "Planning for Agents"
author: "LangChain Accounts"
date: "2024-07-20"
url: "https://www.langchain.com/blog/planning-for-agents"
---

Harrison&#x27;s In the LoopDeploymentAgent Architecture

# Planning for Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseJuly 20, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf87394beb695264f3ee_Planning-for-agents.png)*At Sequoia’s AI Ascent conference in March, I talked about three limitations for agents: planning, UX, and memory. Check out that talk *[*here*](https://www.youtube.com/watch?v=pBBe1pk8hf4&amp;ref=blog.langchain.com)*. In this post, I will dive more into planning for agents.*

If you ask any developer building agents with LLMs, he or she will probably cite the inability for agents to plan and reason well as a big pain point for agent reliability. What does planning mean for an agent, and how do we see people currently overcoming this shortcoming? What is (our best guess at what) the future of planning and reasoning for agents will look like? We’ll cover all of this below.

## What exactly is meant by planning and reasoning?

Planning and reasoning by an agent involves the LLM’s ability to think about what actions to take. This involves both short-term and long term steps. The LLM evaluates all available information and then decides: what are the series of steps that I need to take, and which is the first one I should take right now?

Most of the time, developers use [function calling](https://platform.openai.com/docs/guides/function-calling?ref=blog.langchain.com) (also known as tool calling) to let LLMs choose what actions to take. Function calling is a capability [first added to LLM APIs by OpenAI in June of 2023](https://openai.com/index/function-calling-and-other-api-updates/?ref=blog.langchain.com) and then [by others in late 2023/early 2024](https://python.langchain.com/v0.2/docs/integrations/chat/?ref=blog.langchain.com#advanced-features). With function calling, you can provide JSON schemas for different functions and have the LLM output object match one (or more) of those schemas. For more information on how to do this, see our guide [here](https://python.langchain.com/v0.2/docs/how_to/tool_calling/?ref=blog.langchain.com).

Function calling is used to let the agent choose what to do as an immediate action. Often times though, to successfully accomplish a complex task you need to take a number of actions in sequence. This long-term planning and reasoning is a tougher task for LLMs for a few reasons. First, the LLM must think about a longer time-horizon goal, but then jump back into a short-term action to take. Second, as the agent takes more and more actions, the results of those actions are fed back to the LLM; this lead to the context window growing, which can cause the LLM to get “distracted” and perform poorly.

Like most things in the LLM world, it is tough to measure exactly how well current models do at planning and reasoning. There are reasonable benchmarks like the [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html?ref=blog.langchain.com) for evaluating function calling. We’ve done [a little research](https://blog.langchain.com/benchmarking-agent-tool-use/) on evaluating multi-step applications. But the best way to get a sense for this is build up an evaluation set for **your specific problem** and attempt to evaluate on that yourself.

💡

Anecdotally, it&#x27;s a common conclusion that planning and reasoning is still not at the level it’s needed to be for real-world tasks.

## What are current fixes to improve planning by agents?

The lowest hanging fix for improving planning is to ensuring the LLM has all the information required to reason/plan appropriately. As basic as this sounds, oftentimes the prompt being passed into the LLM simply does not contain enough information for the LLM to make a reasonable decision. Adding a retrieval step, or clarifying the prompt instructions, can be an easy improvement. That’s why its crucial to actually [look at the data](https://x.com/HamelHusain/status/1717582026537312519?ref=blog.langchain.com) and see what the LLM is actually seeing.

After that, I’d recommend you try changing the [cognitive architecture](https://blog.langchain.com/what-is-a-cognitive-architecture/) of your application. By “cognitive architecture”, I mean the data engineering logic your application uses to reason. There are two categories of cognitive architectures you can look towards to improve reasoning: general purpose cognitive architectures and domain specific cognitive architectures.

## General purpose cognitive architectures vs domain specific cognitive architectures

General purpose cognitive architectures attempt to achieve better reasoning generically. They can be applied to any task. One good example of this is the “plan and solve” architecture. [This paper](https://arxiv.org/abs/2305.04091?ref=blog.langchain.com) explores an architecture where first you come up with a plan, and then execute on each step in that plan. Another general purpose architecture is the Reflexion architecture. [This paper](https://arxiv.org/abs/2303.11366?ref=blog.langchain.com) explores putting an explicit “reflection” step after the agent does a task to reflect on whether it did it correctly or not.

Though these ideas show improvement, they are often too general for practical use by agents in production. Rather, we see agents being built with domain-specific cognitive architectures. This often manifests in domain-specific classification/routing steps, domain specific verification steps. Some of the general ideas of planning and reflection can be applied here, but they are often applied in a domain specific way.

As a concrete example, let’s look at the [AlphaCodium paper](https://www.codium.ai/products/alpha-codium/?ref=blog.langchain.com). This achieved state-of-the-art performance by using what they called “flow engineering” (another way to talk about cognitive architectures). See a diagram of the flow they use below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf88394beb695264f417_1.png)

The flow is VERY specific to the problem they are trying to solve. They are telling the agent what to do in steps - come up with tests, then come up with a solution, then iterate on more tests, etc. This cognitive architecture is highly domain specific - it wouldn’t help you write essays, for example.

## Why are domain specific cognitive architectures so helpful?

There are two ways I like to think about this.

First: you can view this as just another method of communicating to the agent what it should do. You can communicate instructions in prompt instructions, or you can hardcode specific transitions in code. Either one is valid! Code is **fantastic** way of communicating what you want to have happen.

Second: this is essentially removing the planning responsibilities from the LLM to us as engineers. We are are basically saying: “don’t worry about planning, LLM, I’ll do it for you!” Of course, we’re not removing ALL planning from the LLM, as we still ask it do some planning in some instances.

For example, let’s look back at the AlphaCodium example above. The steps in the flow are basically us doing planning for the LLM! We’re telling it to first write tests, then code, then run the tests, etc. This is presumably what the authors thought a good plan for writing software was. If they were planning how to do a problem, this is how they would do it. And rather than tell the LLM to do in the prompt - where it may ignore it, not understand it, not have all the details - they told the system to do it by constructing a domain specific cognitive architecture.

💡

Nearly all the advanced “agents” we see in production actually have a very domain specific and custom cognitive architecture.

We’re making building these custom cognitive architectures easier with [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com). One of the big focus points of LangGraph is on controllability. We’ve designed LangGraph to very low level and highly controllable - this is because we’ve seen that level of controllability is 100% needed to create a reliable custom cognitive architecture.

## What does the future of planning and reasoning look like?

The LLM space has been changing and evolving rapidly, and we should keep that in mind when building applications, and especially when building tools.

My current take is that general purpose reasoning will get more and more absorbed into the model layer. The models will get more and more intelligent, whether through scale or research breakthroughs - it seems foolish to bet against that. Models will get faster and cheaper as well, so it will become more and more feasible to pass a large amount of context to them.

However, I believe that no matter how powerful the model becomes, you will always need to communicate to the agent, in some form, what it should do. As a result, I believe prompting and custom architectures are here to stay. For simple tasks, prompting may suffice. For more complex tasks, you may want to put the logic of how it should behave in code. Code-first approaches may be faster, more reliable, more debuggable, and oftentimes easier/more logical to express.

I went on a [podcast recently](https://podcasts.apple.com/us/podcast/langchains-harrison-chase-on-building-the/id1750736528?i=1000659385691&amp;ref=blog.langchain.com) with Sonya and Pat from Sequoia and talked about this topic. They drew a fantastic diagram showing how the role / importance of prompting, cognitive architectures, and the model may evolve over time.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf88394beb695264f41a_Screenshot-2024-07-20-at-8.00.15-AM.png)

So while the planning and reasoning of LLMs will certainly get better, we also strongly believe that if you are building a task-specific agent then you will need to build a custom cognitive architecture. That’s why we’re so bullish on the future of [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)