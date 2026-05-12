---
title: "Deep Agents v0.5"
author: "LangChain Accounts"
date: "2026-04-07"
url: "https://www.langchain.com/blog/deep-agents-v0-5"
---

Deep Agents

# Deep Agents v0.5

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 7, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77a23b90087fe7b1e06e0_73--5-.webp)

## Key Takeaways

**TL;DR:** We’ve released new minor versions of `deepagents `&amp; `deepagentsjs`, featuring async (non-blocking) subagents, expanded multi-modal filesystem support, and more.

See the [**changelog**](https://docs.langchain.com/oss/python/releases/changelog?ref=blog.langchain.com) for details.

## Async subagents

Deep Agents can now delegate work to remote agents that run in the background. As opposed to the existing inline [**subagents**](https://docs.langchain.com/oss/python/deepagents/subagents?ref=blog.langchain.com), which block the main agent until they complete, async subagents return a task ID immediately and execute independently on a remote server.

See the [**Deep Agents docs**](https://docs.langchain.com/oss/python/deepagents/async-subagents?ref=blog.langchain.com) for more detail.

### Motivation

Inline subagents are effective for short, focused tasks, but they block the supervisor&#x27;s execution loop while they run. For work that takes minutes rather than seconds—deep research, large-scale code analysis, multi-step data pipelines—this becomes a bottleneck. The supervisor can&#x27;t respond to the user or make progress on other work until the subagent returns. This was less of an issue when most agents and subagents were short-lived, but as the addressable task length has grown, blocking has become a more serious issue.

Async subagents remove this constraint. The supervisor can launch several subagents in parallel, continue a conversation with the user, and collect results as they become available. Unlike inline subagents, async subagents are also stateful: they maintain their own thread across interactions, so the supervisor can send follow-up instructions or course-correct mid-task.

This also opens the door to heterogeneous deployments, where a lightweight orchestrator delegates to specialized remote agents running on different hardware, using different models, or maintaining their own tool sets.

### Usage

The `subagents` parameter has been widened to accept an `AsyncSubAgent` spec, which points to a remote agent:

```
from deepagents import AsyncSubAgent, create_deep_agent

agent = create_deep_agent(
    model=&quot;anthropic:claude-sonnet-4-6&quot;,
    subagents=[
        AsyncSubAgent(
            name=&quot;researcher&quot;,
            description=&quot;Performs deep research on a topic.&quot;,
            url=&quot;&lt;https://my-agent-server.dev&gt;&quot;,
            graph_id=&quot;research_agent&quot;,
        ),
    ],
)
```

`AsyncSubAgent` specs can be mixed freely with the existing `SubAgent` and `CompiledSubAgent` specs—`create_deep_agent` routes each to the appropriate middleware based on its type.

Once configured, the main agent gains five tools for managing background work:




        Tool
        Purpose




        start_async_task
        Launch a task on a remote agent. Returns a task ID immediately.


        check_async_task
        Poll a task's status and retrieve its result when complete.


        update_async_task
        Send follow-up instructions to a running task.


        cancel_async_task
        Cancel a running task.


        list_async_tasks
        List all tracked tasks with their current statuses.




The interaction model is fire-and-forget: the main agent launches a task, continues working or talking to the user, and checks back for results when needed. Multiple async subagents can run concurrently.

### Server protocol

Any remote agent that implements the [**Agent Protocol**](https://github.com/langchain-ai/agent-protocol?ref=blog.langchain.com) is a valid target for async subagents. This means you can point a Deep Agent at any Agent Protocol-compliant server, including any agent [**deployed with LangSmith**](https://docs.langchain.com/langsmith/deployment?ref=blog.langchain.com), a custom FastAPI service using the [**server stubs**](https://github.com/langchain-ai/agent-protocol/tree/main/server?ref=blog.langchain.com), or any other implementation. We’ve added example server implementations for Deep Agents for [**Python**](https://github.com/langchain-ai/deepagents/tree/main/examples/async-subagent-server?ref=blog.langchain.com) and [**JS**](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/async-subagent-server?ref=blog.langchain.com).

If the `url` field is omitted, Deep Agents will use ASGI transport to communicate with the sub-agent. This allows supervisor and sub-agents to be co-deployed and communicate in the same process.

For a complete walkthrough—including deployment configuration, tracing, troubleshooting, and a reference implementation—see the [**async subagents documentation**](https://docs.langchain.com/oss/python/deepagents/async-subagents?ref=blog.langchain.com).

### **Why Agent Protocol**

Async subagents need a standard server protocol, one that any remote agent can implement regardless of how or where it’s deployed. Before landing on Agent Protocol, we looked at what other options were available.

[**ACP**](https://agentcommunicationprotocol.dev/introduction/welcome?ref=blog.langchain.com) (Agent Client Protocol) is purpose built for editor-to-agent communication and has growing adoption in the tooling space. ACP has two problems for our use case. First, it&#x27;s built around a synchronous session model where the client sends a prompt and waits for a response, which doesn&#x27;t map cleanly to async subagents. Second, it currently only supports stdio transport, which means the remote agent has to run as a local subprocess. HTTP support is on the roadmap but hasn&#x27;t shipped, so ACP isn&#x27;t viable for remote deployments today.

[**A2A**](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/?ref=blog.langchain.com) (Agent-to-Agent Protocol) is a closer fit and is technically compatible. It has full HTTP support and a native async task model. It’s a strong protocol and is designed to solve broad agent interoperability challenges across the industry covering things like push/pull subscriptions, agent discovery, and capability negotiation. However, since async subagents are still evolving, we prioritized a protocol that allows for faster iteration. Support for A2A may be added in a future release.

[**Agent Protocol**](https://github.com/langchain-ai/agent-protocol?ref=blog.langchain.com) is LangChain&#x27;s own open specification for serving LLM agents and is already the protocol underlying LangGraph Platform. It fits well here for a few reasons.

The model lines up cleanly. Agent Protocol is built around threads and runs. You create a thread to hold conversation context, start a run to kick off work, and check on it when you need the result. That maps directly onto how async subagents work. It also means subagents are stateful across interactions. When you send a mid-task update, the remote agent picks up in context because the thread history is preserved, rather than starting from scratch.

The result is a protocol that fits the async task model naturally, works across managed and self-hosted deployments, and stays nimble enough to evolve alongside the feature.

## Expanded multi-modal support

Deep Agents previously supported reading images from its [**virtual filesystem**](https://docs.langchain.com/oss/python/deepagents/backends?ref=blog.langchain.com). This release extends multimodal support to PDFs, audio, video, and other file types. The agent uses the same `read_file` tool; no API change is required. File type is detected automatically from the extension, and the content is passed to the model as a native content block with the appropriate MIME type. See [**Deep Agents docs**](https://docs.langchain.com/oss/python/deepagents/harness?ref=blog.langchain.com#supported-multimodal-file-extensions) for details.

Importantly, which modalities are supported depends on the underlying model. You can check supported modalities programmatically via [**model profiles**](https://docs.langchain.com/oss/python/langchain/models?ref=blog.langchain.com#model-profiles)—each LangChain chat model exposes a profile that declares which input types it accepts.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ea236ce872ec8be413bd2f_runtime-behind-production-deep-agents-thumbnail.png)Conceptual GuideDeep Agents

#### The runtime behind production deep agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Sydney RunkleVivek TrivedyApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)24min[](/blog/runtime-behind-production-deep-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)