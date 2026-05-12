---
title: "The two patterns by which agents connect sandboxes"
author: "LangChain Accounts"
date: "2026-02-10"
url: "https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes"
---

Harrison&#x27;s In the LoopLangSmith

# The two patterns by which agents connect sandboxes

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseFebruary 10, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9f3eea3104c341cfdeb_Screenshot-2026-02-09-at-9.30.02---PM.png)*Thank you to Nuno Campos from Witan Labs, Tomas Beran and Mikayel Harutyunyan from E2B, Jonathan Wall from Runloop, and Ben Guo from Zo Computer for their review and comments.*

**TL;DR:**

- **More and more agents need a workspace: a computer where they can run code, install packages, and access files. Sandboxes provide this.**
- **There are two architecture patterns for integrating agents with sandboxes:**
**Pattern 1 (Agent IN Sandbox): Agent runs inside the sandbox, you communicate with it over the network. Benefits: mirrors local development, tight coupling between agent and environment.**
- **Pattern 2 (Sandbox as Tool): Agent runs locally/on your server, calls sandbox remotely for execution. Benefits: easy to update agent logic, API keys stay outside sandbox, cleaner separation of concerns.**

- [**deepagents**](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com)** supports both patterns with simple configuration**

An increasing number of agents need a workspace - a computer where they can run code, install packages, and access files. That workspace needs to be isolated so the agent can&#x27;t access your credentials, files, or network. Sandboxes provide this isolation by creating a boundary between the agent&#x27;s environment and your host system. The question teams building these agents face isn&#x27;t *whether* to use sandboxes - it&#x27;s *how to integrate them* with their agent architecture.

There are two common patterns based on where the agent runs: inside the sandbox or outside of it. Each pattern has different benefits and trade-offs.

Note: this post focuses on sandboxes that give agents a full &#x27;computer’ - complete execution environments like Docker containers or VMs. We won&#x27;t cover process-level sandboxes (like [bubblewrap](https://github.com/containers/bubblewrap?ref=blog.langchain.com)) or language-level sandboxes (like [Pyodide](https://pyodide.org/en/stable/?ref=blog.langchain.com)).

## Pattern 1: Agent Runs IN Sandbox

In this pattern, the agent runs inside the sandbox. You communicate with it over the network.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9f4eea3104c341cfe55_Screenshot-2026-02-09-at-9.52.12---PM.png)

**What this looks like in practice:**

You build a Docker or VM image with your agent framework pre-installed, run it inside the sandbox, and connect from outside to send messages. The agent exposes an API endpoint (typically HTTP or WebSocket), and your application communicates with it across the sandbox boundary.

**Benefits:**

This pattern mirrors local development closely—if you run `deepagents` in your terminal locally, you run the same command in the sandbox. The agent has direct filesystem access and can modify its environment. This is useful when the agent and execution environment are tightly coupled, such as when the agent needs to interact with specific libraries or maintain complex environment state.

**Trade-offs:**

Communication across the sandbox boundary requires infrastructure. Some providers handle this in their SDK—for example, agents like OpenCode run a server inside the sandbox, and providers like E2B can expose this through a clean API. If your provider doesn&#x27;t offer this, you&#x27;ll need to build the WebSocket or HTTP layer yourself, including session management and error handling.

API keys must live inside the sandbox to allow the agent to make inference calls. This creates a potential security risk if the sandbox is compromised, whether through a vulnerability in the isolation technology or through prompt injection attacks that exfiltrate credentials. Note: we see providers like E2B and Runloop working on secret vault capabilities, which addresses this.

Updates require rebuilding the container image and redeploying, which can slow iteration cycles during development.

Another downside is that the sandbox must be resumed before the agent becomes active, which often requires extra logic.

For those worried about protecting the IP of their agents, if your agent is running in the sandbox it becomes much easier to exfiltrate the entire code and prompts of the agent.

Nuno Campos from Witan Labs also points out another security risk: “I’d say another downside of agent in sandbox is that effectively no part of your agent can have more privileges than the bash tool does. E.g. imagine you want an agent that has a bash tool and a tool that can do web search or web fetch, then all the LLM generated code can do unlimited web fetches (which is a big security risk). If it’s sandbox as tool then you can have tools with more permissions than you give to llm generated code (which sounds very useful for many agents) trivially, as the security boundary is around the bash tool, not the whole agent.”

## Pattern 2: Sandbox as Tool

In this pattern, the agent runs on your machine or server. When it needs to execute code, it calls a remote sandbox via API.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9f3eea3104c341cfdeb_Screenshot-2026-02-09-at-9.30.02---PM.png)

**What this looks like in practice:**

Your agent runs locally (or on your server), and when it generates code that needs to execute, it calls out to a sandbox provider&#x27;s API (like [E2B](https://e2b.dev/?ref=blog.langchain.com), [Modal](https://modal.com/?ref=blog.langchain.com), [Daytona](https://www.daytona.io/?ref=blog.langchain.com), or [Runloop](https://runloop.ai/?ref=blog.langchain.com)). The provider&#x27;s SDK handles all the communication details. From your agent&#x27;s perspective, the sandbox is just another tool.

**Benefits:**

You can update agent code instantly without rebuilding container images, which speeds up iteration during development. API keys stay outside the sandbox—only execution happens in isolation. This provides cleaner separation of concerns: agent state (conversation history, reasoning chains, memory) lives where your agent runs, separate from the sandbox. This means sandbox failures don&#x27;t lose your agent&#x27;s state, and you can switch sandbox backends without affecting your agent&#x27;s core logic.

Two other benefits of this option, as pointed out by Tomas Beran of E2B:

- Having the option to run tasks in multiple remote sandboxes in parallel
- Paying for sandboxes only when executing code, rather than for the whole process runtime.

Ben Guo adds a final point about the benefits of separating agent runtime from sandbox runtime: “We chose Pattern 2 for the reasons you mention, but also in preparation for a future where it makes sense to run the agent harness in a GPU machine – generally feels like the environment requirements will diverge between the persistent sandbox and the inference harness”

**Trade-offs:**

Network latency is the main downside. Each execution call crosses the network boundary. For workloads with many small executions, this can add up.

Many sandbox providers offer stateful sessions where variables, files, and installed packages persist across invocations within the same session. This can mitigate some of the latency concerns by reducing the number of round trips needed.

## Choosing Between Patterns

**Choose Pattern 1 when:**

- The agent and execution environment are tightly coupled (for example, the agent needs persistent access to specific libraries or complex environment state)
- You want production to mirror local development closely
- Your provider&#x27;s SDK handles the communication layer for you

**Choose Pattern 2 when:**

- You need to iterate quickly on agent logic during development
- You want to keep API keys outside the sandbox
- You prefer cleaner separation between agent state and execution environment

## Implementation Example

To make these patterns concrete, we&#x27;ll show examples using [deepagents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com), an open-source agent framework with built-in sandbox support. Similar patterns apply to other agent frameworks.

### Pattern 1: Agent IN Sandbox

For Pattern 1, first you build an image with your agent pre-installed:

`FROM python:3.11
RUN pip install deepagents-cli

`

Then run it inside the sandbox. A complete implementation requires additional infrastructure to handle communication between your application and the agent inside the sandbox (WebSocket or HTTP server, session management, error handling). This is beyond the scope of this post, but we will have some follow up posts diving into this in more detail.

### Pattern 2: Sandbox as Tool

`from daytona import Daytona
from langchain_anthropic import ChatAnthropic

from deepagents import create_deep_agent
from langchain_daytona import DaytonaSandbox

# Can also do this with E2B, Runloop, Modal
sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model=&quot;claude-sonnet-4-20250514&quot;),
    system_prompt=&quot;You are a Python coding assistant with sandbox access.&quot;,
    backend=backend,
)

result = agent.invoke(
    {
        &quot;messages&quot;: [
            {
                &quot;role&quot;: &quot;user&quot;,
                &quot;content&quot;: &quot;Run a small python script&quot;,
            }
        ]
    }
)

sandbox.stop()

`

Here&#x27;s what happens when this code runs:

- The agent plans locally on your machine
- It generates Python code to solve the problem
- It calls the Runloop API, which executes the code in a remote sandbox
- The sandbox returns the result
- The agent sees the output and continues reasoning locally

## Conclusion

Agents need to execute code in isolated environments for security. There are two architecture patterns: running the agent inside the sandbox (mirrors local development, tight coupling) or running it outside with the sandbox as a tool (easy updates, API keys stay secure). Each has different benefits and trade-offs depending on your needs.

deepagents supports both patterns with simple configuration. [Try it out](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) to see which pattern works best for your use case.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f93289bc64d34828c3f815_Screenshot%202026-05-04%20at%2010.12.00%E2%80%AFAM.png)Harrison&#x27;s In the Loop

#### Agent observability needs feedback to power learning

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMay 5, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/agent-observability-needs-feedback-to-power-learning)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)