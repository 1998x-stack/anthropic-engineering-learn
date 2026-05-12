---
title: "Running Subagents in the Background"
author: "LangChain Accounts"
date: "2026-04-16"
url: "https://www.langchain.com/blog/running-subagents-in-the-background"
---

Agent ArchitectureDeep AgentsOpen Source

# Running Subagents in the Background

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)Hunter LovellColin FrancisApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)

## Key Takeaways

- **Inline subagents block the supervisor agent for the duration of the task.** Because tool calls in an agent loop are synchronous, the supervisor can&#x27;t respond to users, coordinate other work, or course-correct until the subagent finishes, a real problem when a task takes an hour or more.
- **Async subagents return a task ID immediately, so supervisors stay in control.** The supervisor can launch multiple subagents in parallel, keep talking to the user, send mid-task updates, or cancel work that&#x27;s no longer needed, more like &quot;fire-and-steer&quot; than &quot;fire-and-forget.&quot;
- **Async subagents are built on Agent Protocol, so you&#x27;re not locked into one deployment.** They run as fully separate agents with their own process and state, and can be hosted on LangSmith deployments or self-hosted on your own infrastructure, the supervisor manages them through the same standard interface either way.

We&#x27;re starting to ask more of our agents — we want them to take on longer and more complex tasks. As we&#x27;ve done that, the typical way that we&#x27;ve orchestrated agents has started to show some cracks.

We shipped [async subagents](https://docs.langchain.com/oss/javascript/deepagents/async-subagents) to Deep Agents recently to help address that! It&#x27;s a pattern that lets agents run delegated work in the background, and is something we&#x27;re excited about since it remedies some of the shortcomings of traditional agent architectures.

## Where traditional subagents break down

A subagent is an agent that a supervisor agent delegates scoped work to. The subagent gets instructions from the supervisor, access to relevant tools, and returns a summary when it’s done. It’s a context engineering pattern that we’ve been adopting in practically all of the agents we build for a couple of important reasons:

- **Agents perform better when work is broken up into smaller tasks** - a supervisor agent gets an understanding of the problem, organizes the tasks, then coordinates workers that execute on them.
- **Not all information about a small task is important for the large objective** - by splitting things out into focused, independent agent runs, we hide away unnecessary context from the supervisor.

This pattern works. But as we’ve given agents longer and more complex tasks, inline subagents have started to break down.

## Agent are put in a deadlock while subagents are working

Subagents are called via a tool that&#x27;s given to the supervisor agent, and because of the way that tool calling works inside of an agent, the supervisor can&#x27;t reason about anything else until the tool call has been answered with the subagent response.

This wasn&#x27;t that big of an issue when subagents were tasked with smaller, low-stakes tasks. But now that we&#x27;ve given agents more complicated tasks and tooling (and with models that take longer to run), this becomes more strongly felt. If a subagent takes an hour, you have to wait an hour before you can interact with the agent again.

## New information is hard to coordinate

There are a couple of channels of information that are important to an agent as it&#x27;s working:

- **User input** — the user might want to steer the agent, add context, or change priorities while a task is in flight.
- **Results from other work** — one subagent&#x27;s output might inform what another subagent should do next.
- **Partial progress** — sometimes you want to course-correct a task that&#x27;s heading in the wrong direction before it finishes.

With inline subagents, none of these channels are available. The supervisor is blocked, so the user can&#x27;t talk to it. Subagents can&#x27;t run concurrently, so there&#x27;s no cross-pollination of results. And subagent turns are all-or-nothing  meaning there&#x27;s no way to send a mid-task update or gracefully handle a partial failure. The supervisor fires off a subagent and hopes for the best.

## Enter: Async Subagents

A simple way to think about async subagents are as subagents that run in the background instead of sequentially. Instead of waiting for the subagent to finish before moving on, the supervisor launches a task, gets a task ID back immediately, and continues working. It can talk to the user, kick off more subagents, or make progress on other parts of the problem while work is happening in the background.

Because subagents are stateful and maintain their own conversation thread, the supervisor can send follow-up instructions, course-correct mid-task, or cancel work that&#x27;s no longer needed. Think of it less like &quot;fire-and-forget&quot; and more like &quot;fire-and-steer.&quot;

### How they work

Instead of giving the supervisor a single blocking tool call per subagent, async subagents give the supervisor a set of management tools that work more like a task queue:




        Tool
        Purpose




        `start_async_task`
        Launch a task on a remote agent. Returns a task ID immediately.


        `check_async_task`
        Poll a task's status and retrieve its result when complete.


        `update_async_task`
        Send follow-up instructions to a running task.


        `cancel_async_task`
        Cancel a running task.


        `list_async_tasks`
        List all tracked tasks with their current statuses.




The supervisor uses these tools naturally as part of its reasoning loop — it can start a few tasks, go back to talking with the user, check in on progress, and course-correct as needed.

Traditional subagents are really just a function of the parent agent — they share a process, they share state, and they only exist inside the supervisor&#x27;s execution loop. Async subagents treat them as separate, individually addressable agents entirely. They can run in their own process, maintain their own state, and scale to runs that might call hundreds or thousands of subagents.

### **Built on Agent Protocol**

That kind of separation requires more than in-process function calls. Async subagents are built on [Agent Protocol](https://github.com/langchain-ai/agent-protocol), a framework-agnostic API specification for managing remote agents. It defines standard endpoints for creating threads, launching runs, polling status, sending updates, and managing long-term memory. Everything the supervisor needs to manage async work through a consistent interface.

The key benefit is deployment flexibility. You aren&#x27;t locked into any single hosting platform. Run your async subagents on [LangSmith deployments](https://docs.langchain.com/langsmith) for a managed experience, or host them yourself on your own infrastructure. The supervisor doesn&#x27;t care where the subagent lives. It sends a task, gets a task ID, and manages the lifecycle through the same standard interface either way.

To learn more about Agent Protocol, see the [specification](https://github.com/langchain-ai/agent-protocol) and [API reference](https://langchain-ai.github.io/agent-protocol/api.html).

## **How to use async subagents in Deep Agents**

[Deep Agents](https://docs.langchain.com/oss/python/deepagents) is our general purpose agent harness that [we talk a lot about](https://blog.langchain.com/). Adding async subagents to DeepAgents is as simple as swapping an async subagent spec into the `subagents` list — you can mix and match them freely with inline subagents.

### **With LangSmith Deployment**

Define your agents and register them in `langgraph.json`. Because the researcher is a separate agent, the supervisor gets the async management tools automatically:

```
// agents.ts
import { createAgent } from &quot;langchain&quot;;
import { createDeepAgent } from &quot;deepagents&quot;;

export const researcher = createAgent({
  model: &quot;anthropic:claude-sonnet-4-6&quot;,
  instructions: &quot;Perform deep research on the given topic.&quot;,
  tools: [searchWeb, readUrl],
});

export const agent = createDeepAgent({
  model: &quot;anthropic:claude-opus-4-6&quot;,
  subagents: [{
    name: &quot;researcher&quot;,
    description: &quot;Performs deep research on a topic.&quot;,
    graphId: &quot;researcher&quot;,
  }],
});
```

```
// langgraph.json
{
  &quot;dependencies&quot;: [&quot;.&quot;],
  &quot;graphs&quot;: {
    &quot;researcher&quot;: &quot;./agents.ts:researcher&quot;,
    &quot;agent&quot;: &quot;./agents.ts:agent&quot;
  }
}
```

The subagent runs in its own process with its own state and the supervisor just delegates and checks back.

## Self-hosted

If you want full control over where your subagents run, you can host them yourself. The subagent just needs to implement the Agent Protocol endpoints and the supervisor connects to it via a URL instead of a graph ID.

```
export const agent = createDeepAgent({
  model: &quot;anthropic:claude-opus-4-6&quot;,
  subagents: [{
    name: &quot;researcher&quot;,
    description: &quot;Performs deep research on a topic.&quot;,
    graphId: &quot;researcher&quot;,
    url: &quot;http://localhost:2024&quot;,  // points to your self-hosted server
  }],
});
```

The self-hosted server implements the Agent Protocol endpoints (creating threads, launching runs, polling status, cancelling tasks) and can run anywhere — a Docker container, a VM, your own Kubernetes cluster. We have a [complete self-hosted example](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/async-subagent-server) that includes a Hono server, Postgres-backed state, and Docker Compose setup you can use as a starting point.

## Learn more

For a complete walkthrough — including deployment configuration, tracing, and troubleshooting — see the [async subagents documentation](https://docs.langchain.com/oss/javascript/deepagents/async-subagents).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

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