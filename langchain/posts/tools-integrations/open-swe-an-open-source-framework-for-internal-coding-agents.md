---
title: "Open SWE: An Open-Source Framework for Internal Coding Agents"
author: "LangChain Accounts"
date: "2026-03-17"
url: "https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents"
---

Deep AgentsOpen Source

# Open SWE: An Open-Source Framework for Internal Coding Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)10min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba99add151f0038d5bf22_OpenSWE.png)Over the past year, we&#x27;ve observed several engineering organizations building internal coding agents that operate alongside their development teams. Stripe developed [Minions](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents?ref=blog.langchain.com), Ramp built [Inspect](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal?ref=blog.langchain.com), and Coinbase created [Cloudbot](https://www.coinbase.com/blog/building-enterprise-AI-agents-at-Coinbase?ref=blog.langchain.com). These systems integrate into existing workflows (accessible through Slack, Linear, and GitHub) rather than requiring engineers to adopt new interfaces.

While these systems were developed independently, they&#x27;ve converged on similar architectural patterns: isolated cloud sandboxes, curated toolsets, subagent orchestration, and integration with developer workflows. This convergence suggests some common requirements for deploying AI agents in production engineering environments.

Today, we&#x27;re releasing **Open SWE**, an open-source framework that captures these patterns in a customizable form. Built on [Deep Agents](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) and [LangGraph](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com), Open SWE provides the core architectural components we&#x27;ve observed across these implementations. If your organization is exploring internal coding agents, this can serve as a starting point.

## Patterns from Production Deployments

Stripe, Ramp, and Coinbase have all built their own internal coding agents. Kishan Dahya [wrote a great post](https://x.com/kishan_dahya/status/2028971339974099317?ref=blog.langchain.com) on the different architectural decisions these coding agents made. We summarize them below and then dive into how OpenSWE compares on those dimensions.

**Isolated execution environments**: Tasks run in dedicated cloud sandboxes with full permissions inside strict boundaries. This isolates the blast radius of any mistake from production systems while allowing agents to execute commands without approval prompts for each action.

**Curated toolsets**: According to [Stripe&#x27;s engineering team](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents?ref=blog.langchain.com), their agents have access to around 500 tools, but these are carefully selected and maintained rather than accumulated over time. Tool curation appears to matter more than tool quantity.

**Slack-first invocation**: All three systems integrate with Slack as a primary interface, meeting developers in their existing communication workflows rather than requiring context switches to new applications.

**Rich context at startup**: These agents pull full context from Linear issues, Slack threads, or GitHub PRs before beginning work, reducing the overhead of discovering requirements through tool calls.

**Subagent orchestration**: Complex tasks get decomposed and delegated to specialized child agents, each with isolated context and focused responsibilities.

These architectural choices have proven effective across multiple production deployments, though organizations will likely need to adapt specific components to their own environments and requirements.

## Open SWE&#x27;s Architecture

Open SWE provides an open-source implementation of similar architectural patterns. Here&#x27;s how the framework maps to what we&#x27;ve observed:

### 1. Agent Harness: Composed on Deep Agents

Rather than forking an existing agent or building from scratch, Open SWE composes on the [Deep Agents](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) framework. This approach is similar to how [Ramp&#x27;s team built Inspect](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal?ref=blog.langchain.com) on top of OpenCode.

Composition provides two advantages:

**Upgrade path**: When Deep Agents improves (better context management, more efficient planning, optimized token usage), you can incorporate those improvements without rebuilding your customizations.

**Customization without forking**: You can maintain org-specific tools, prompts, and workflows as configuration rather than as modifications to core agent logic.

`create_deep_agent(
    model=&quot;anthropic:claude-opus-4-6&quot;,
    system_prompt=construct_system_prompt(repo_dir, ...),
    tools=[
        http_request,
        fetch_url,
        commit_and_open_pr,
        linear_comment,
        slack_thread_reply
    ],
    backend=sandbox_backend,
    middleware=[
        ToolErrorMiddleware(),
        check_message_queue_before_model,
        ...
    ],
)
`

Deep Agents provides infrastructure that can support these patterns: built-in planning via `write_todos`, file-based context management, native subagent spawning via the `task` tool, and middleware hooks for deterministic orchestration.

### 2. Sandbox: Isolated Cloud Environments

Each task runs in its own isolated cloud sandbox, a remote Linux environment with full shell access. The repository is cloned in, the agent receives complete permissions, and any errors are contained within that environment.

Open SWE supports multiple sandbox providers out of the box:

- [Modal](https://modal.com/?ref=blog.langchain.com)
- [Daytona](https://www.daytona.io/?ref=blog.langchain.com)
- [Runloop](https://www.runloop.ai/?ref=blog.langchain.com)
- [LangSmith](https://blog.langchain.com/introducing-langsmith-sandboxes-secure-code-execution-for-agents/)

You can also implement your own sandbox backend.

This follows a pattern we&#x27;ve observed: isolate first, then grant full permissions inside the boundary.

Key behaviors:

- Each conversation thread gets a persistent sandbox, reused across follow-up messages
- Sandboxes automatically recreate if they become unreachable
- Multiple tasks run in parallel, each in its own sandbox

### 3. Tools: Curated, Not Accumulated

Open SWE ships with a focused toolset:




        Tool
        Purpose




        execute
        Shell commands in the sandbox


        fetch_url
        Fetch web pages as markdown


        http_request
        API calls (GET, POST, etc.)


        commit_and_open_pr
        Git commit and open a GitHub draft PR


        linear_comment
        Post updates to Linear tickets


        slack_thread_reply
        Reply in Slack threads




Plus the built-in Deep Agents tools: `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep`, `write_todos`, and `task` (subagent spawning).

A smaller, curated toolset can be easier to test, maintain, and reason about. When you need additional tools for your organization (internal APIs, custom deployment systems, specialized testing frameworks), you can add them explicitly.

### 4. Context Engineering: [AGENTS.md](http://agents.md/?ref=blog.langchain.com) + Source Context

Open SWE gathers context from two sources:

**`AGENTS.md` file**: If your repository contains an `AGENTS.md` file at the root, it&#x27;s read from the sandbox and injected into the system prompt. This file can encode conventions, testing requirements, architectural decisions, and team-specific patterns that every agent run should follow.

**Source context**: The full Linear issue (title, description, comments) or Slack thread history is assembled and passed to the agent before it starts, providing task-specific context without additional tool calls.

This two-layer approach balances repository-wide knowledge with task-specific information.

### 5. Orchestration: Subagents + Middleware

Open SWE&#x27;s orchestration combines two mechanisms:

**Subagents**: The Deep Agents framework supports spawning child agents via the `task` tool. The main agent can delegate independent subtasks to isolated subagents, each with its own middleware stack, todo list, and file operations.

**Middleware**: Deterministic middleware hooks run around the agent loop:

- `check_message_queue_before_model`: Injects follow-up messages (Linear comments or Slack messages that arrive mid-run) before the next model call. This allows users to provide additional input while the agent is working.
- `open_pr_if_needed`: Acts as a safety net that commits and opens a PR if the agent didn&#x27;t complete this step. This ensures critical steps happen reliably.
- `ToolErrorMiddleware`: Catches and handles tool errors gracefully.

This separation between agentic (model-driven) and deterministic (middleware-driven) orchestration can help balance reliability with flexibility.

### 6. Invocation: Slack, Linear, and GitHub

We&#x27;ve observed that many teams converge on Slack as a primary invocation surface. Open SWE follows a similar pattern:

**Slack**: Mention the bot in any thread. Supports `repo:owner/name` syntax to specify which repository to work on. The agent replies in-thread with status updates and PR links.

**Linear**: Comment `@openswe` on any issue. The agent reads the full issue context, reacts with 👀 to acknowledge, and posts results back as comments.

**GitHub**: Tag `@openswe` in PR comments on agent-created PRs to have it address review feedback and push fixes to the same branch.

Each invocation creates a deterministic thread ID, so follow-up messages on the same issue or thread route to the same running agent.

### 7. Validation: Prompt-Driven + Safety Nets

The agent is instructed to run linters, formatters, and tests before committing. The `open_pr_if_needed` middleware acts as a backstop—if the agent finishes without opening a PR, the middleware handles it automatically.

You can extend this validation layer by adding deterministic CI checks, visual verification, or review gates as additional middleware.

## Why Deep Agents

Deep Agents provides the foundation that makes this architecture composable and maintainable.

**Context management**: Long-running coding tasks can produce large amounts of intermediate data (file contents, command outputs, search results). Deep Agents handles this through file-based memory, offloading large results instead of keeping everything in the conversation history. This can help prevent context overflow when working on larger codebases.

**Planning primitives**: The built-in `write_todos` tool provides a structured way to break down complex work, track progress, and adapt plans as new information emerges. We&#x27;ve found this particularly helpful for multi-step tasks that span extended periods.

**Subagent isolation**: When the main agent spawns a child agent via the `task` tool, that subagent gets its own isolated context. Different subtasks don&#x27;t pollute each other&#x27;s conversation history, which can lead to clearer reasoning on complex, multi-faceted work.

**Middleware hooks**: Deep Agents&#x27; middleware system allows you to inject deterministic logic at specific points in the agent loop. This is how Open SWE implements message injection and automatic PR creation—behaviors that need to happen reliably.

**Upgrade path**: Because Deep Agents is actively developed as a standalone library, improvements to context compression, prompt caching, planning efficiency, and subagent orchestration can flow to Open SWE without requiring you to rebuild your customizations.

This composability offers similar advantages to what [Ramp&#x27;s team described](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal?ref=blog.langchain.com) when building on OpenCode: you get the benefits of a maintained, improving foundation while retaining control over your org-specific layer.

## Customization for Your Organization

Open SWE is intended as a customizable foundation rather than a finished product. Every major component is pluggable:

**Sandbox provider**: Swap between Modal, Daytona, Runloop, or LangSmith. Implement your own sandbox backend if you have internal infrastructure requirements.

**Model**: Use any LLM provider. The default is Claude Opus 4, but you can configure different models for different subtasks.

**Tools**: Add tools for your internal APIs, deployment systems, testing frameworks, or monitoring platforms. Remove tools you don&#x27;t need.

**Triggers**: Modify the Slack, Linear, and GitHub integration logic. Add new trigger surfaces like email, webhooks, or custom UIs.

**System prompt**: Customize the base prompt and the logic for incorporating `AGENTS.md` files. Add org-specific instructions, constraints, or conventions.

**Middleware**: Add your own middleware hooks for validation, approval gates, logging, or safety checks.

The [Customization Guide](https://github.com/langchain-ai/open-swe/blob/main/CUSTOMIZATION.md?ref=blog.langchain.com) walks through each of these extension points with examples.

## Comparison to Internal Implementations

Here&#x27;s how Open SWE compares to the internal systems at Stripe, Ramp, and Coinbase based on [publicly](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents?ref=blog.langchain.com) [available](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal?ref=blog.langchain.com) [information](https://www.coinbase.com/blog/building-enterprise-AI-agents-at-Coinbase?ref=blog.langchain.com):




        Decision
        Open SWE
        Stripe (Minions)
        Ramp (Inspect)
        Coinbase (Cloudbot)




        Harness
        Composed (Deep Agents/LangGraph)
        Forked (Goose)
        Composed (OpenCode)
        Built from scratch


        Sandbox
        Pluggable (Modal, Daytona, Runloop, etc.)
        AWS EC2 devboxes (pre-warmed)
        Modal containers (pre-warmed)
        In-house


        Tools
        ~15, curated
        ~500, curated per-agent
        OpenCode SDK + extensions
        MCPs + custom Skills


        Context
        Agents.md + issue/thread
        Rule files + pre-hydration
        OpenCode built-in
        Linear-fear + MCPs


        Orchestration
        Subagents + middleware
        Blueprints (deterministic + agentic)
        Sessions + child sessions
        Three modes


        Invocation
        Slack, Linear, GitHub
        Slack + embedded buttons
        Slack + web + Chrome extension
        Slack-native


        Validation
        Prompt-driven + PR safety net
        3-layer (local + CI + 1 retry)
        Visual DOM verification
        Agent councils + auto-merge




The core patterns are similar. The differences lie in implementation details, internal integrations, and org-specific tooling—which is exactly what you&#x27;d expect when adapting a framework to different environments.

## Getting Started

Open SWE is available now on [GitHub](https://github.com/langchain-ai/open-swe?ref=blog.langchain.com).

[**Installation Guide**](https://github.com/langchain-ai/open-swe/blob/main/INSTALLATION.md?ref=blog.langchain.com): Walks through GitHub App creation, LangSmith setup, Linear/Slack/GitHub triggers, and production deployment.

[**Customization Guide**](https://github.com/langchain-ai/open-swe/blob/main/CUSTOMIZATION.md?ref=blog.langchain.com): Shows how to swap the sandbox, model, tools, triggers, system prompt, and middleware for your organization.

The framework is MIT-licensed. You can fork it, customize it, and deploy it internally. If you build something interesting on top of it, we&#x27;d be interested to hear about it.

Several engineering organizations have successfully deployed internal coding agents in production. Open SWE provides an open-source implementation of similar architectural patterns, designed to be customized for different codebases and workflows. While we&#x27;re still learning what works across different contexts, this framework offers a starting point for teams exploring this approach.

**Try Open SWE**: [github.com/langchain-ai/open-swe](https://github.com/langchain-ai/open-swe?ref=blog.langchain.com)

**Learn about Deep Agents**: [docs.langchain.com/oss/python/deepagents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com)

**Sign up for the LangSmith Sandboxes Waitlist:** [https://www.langchain.com/langsmith-sandboxes-waitlist](https://www.langchain.com/langsmith-sandboxes-waitlist?ref=blog.langchain.com)

**Read the docs**: [Open SWE Documentation](https://github.com/langchain-ai/open-swe/tree/main/apps/docs?ref=blog.langchain.com)

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