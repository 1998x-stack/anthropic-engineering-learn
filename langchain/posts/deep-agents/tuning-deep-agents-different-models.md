---
title: "Tuning Deep Agents to Work Well with Different Models"
author: "LangChain Accounts"
date: "2026-04-29"
url: "https://www.langchain.com/blog/tuning-deep-agents-different-models"
---

Deep AgentsAgent ArchitectureOpen Source

# Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)

## Key Takeaways

‍💡**TL;DR: **[Deep Agents](https://github.com/langchain-ai/deepagents) was previously designed in a generic way to work well across model families. Today we’re adding model-specific profiles to adjust prompts, tools, and middleware. This allows us to better conform to prompting guides specific to model families. We ship profiles for OpenAI, Anthropic, and Google models out of the box, which we see leads to a 10–20 point jump on a subset of tau2-bench over the default harness.

Until today, `deepagents` shipped with a single set of prompts, tools, and middleware aimed to work well across *all* Large Language Models. Builders could swap in different models or extend the harness with additional tools extensions to the system prompt. But the base prompts, tools, and middleware were fixed and not optimized per model.

As of today, we’re excited to launch **harness profiles** as a way to control these parameters on a per-model basis. This matters because:

- **Prompting guides differ per model.** OpenAI&#x27;s [Codex Prompting Guide](https://developers.openai.com/codex/prompting) prescribes specific tool implementations and names (`apply_patch`, `shell_command`) that move the needle on Codex models. Anthropic&#x27;s [Claude prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) emphasizes a different set of conventions. Even within a family, the Opus 4.6 → 4.7 migration guide flags prompt-level changes worth making.
- **Eval leaderboards show that the same model in a different harness can yield much different performance.** [Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0) is the cleanest public example. The [Claude Code harness ranks last](https://www.tbench.ai/leaderboard/terminal-bench/2.0?models=Claude+Opus+4.6) among Opus 4.6 submissions.  We saw similar effects of careful harness engineering in previous work: [Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering). Here we took `gpt-5.2-codex` from 52.8% to 66.5% on Terminal-Bench 2.0 (Top 30 → Top 5 at the time of publishing) *just by applying harness layer changes* like prompts and middleware hooks.

A single harness can&#x27;t be optimal for every model. So we make it easy to support varying the harness per model.

How much does this matter?

## Results on measuring the effect of profiles

In order to judge how much this matters, we measured performance on a subset of [tau2-bench](https://github.com/sierra-research/tau2-bench) (multi-turn tool use + instruction following). We use a curated subset of more difficult tasks that frontier models haven’t yet saturated so we can better measure the impacts of harness level changes on agents.




        Model
        Base Deep Agents Harness
        With Custom Profile




        GPT 5.3 Codex
        33%
        53%


        Claude Opus 4.7
        43%
        53%




### What changed per model

We use the [Codex](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) and [Claude](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) prompting guides as the source for what changes we applied per profile.

For Codex the main changes included:

- **Tool changes:** overriding the default `file_edit` implementation in `deepagents` with the recommended `apply_patch` tool, and aliasing the `execute` tool name in `deepagents` as `shell_command`
- **Prompt changes:** largely around tool calling and planning using details from the prompting guide

> Before any tool call, decide ALL files and resources you will need. Batch reads, searches, and other independent operations into parallel tool calls instead of issuing them one at a time.

For Opus the main changes were all prompting focused on tool usage and planning. For example, below are two snippets that were added to the prompt.

> &lt;tool_result_reflection&gt;
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
&lt;/tool_result_reflection&gt;

> &lt;tool_usage&gt;
When a task depends on the state of files, tests, or system output, use tools to observe that state directly rather than reasoning from memory about what it probably contains. Read files before describing them. Run tests before claiming they pass. Search the codebase before asserting a symbol does or does not exist. Active investigation with tools is the default mode of working, not a fallback.
&lt;/tool_usage&gt;

Our takeaway is that exposing an interface for customizing the harness per model is a helpful primitive for builders to manage profiles per agent, version them, and easily test differences in configurations.

## Try it today

To use this today, simply start using:

```
deepagents: uv add deepagents
```

```
agent = create_deep_agent(
    model=&quot;google_genai:gemini-3.1-pro-preview&quot;,
    tools=[internet_search],
    system_prompt=research_instructions,
)
```

The profiles will be automatically applied for supported models. If you want to look into the details of what each default profile looks like today, you can inspect the code in the [repo](https://github.com/langchain-ai/deepagents). To learn how to register your own profile, keep reading.

### How profiles work under the hood

A harness profile is a declarative override layer for the parts of the harness that vary per model: system prompt prefix/suffix, tool inclusion and naming, middleware selection, subagent configuration, and skills. You register a profile for a model or provider (or load a preexisting one from YAML), and `create_deep_agent` adapts when you swap the model. Importantly, your call site doesn&#x27;t change.

We ship defaults for OpenAI, Anthropic, and Google models. You can override them, layer your own on top, or distribute profiles as plugins.

```
from deepagents import (
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    &quot;openai:gpt-5.4&quot;,
    HarnessProfile(
        system_prompt_suffix=&quot;Respond in under 100 words.&quot;,
        excluded_tools={&quot;execute&quot;},
        excluded_middleware={&quot;SummarizationMiddleware&quot;},
    ),
)
```

Or declare a profile in YAML:

```
# openai.yaml
base_system_prompt: You are helpful.
system_prompt_suffix: Respond briefly.
excluded_tools:
  - execute
  - grep
excluded_middleware:
  - SummarizationMiddleware
  - my_pkg.middleware:TelemetryMiddleware
general_purpose_subagent:
  enabled: false
```

For more custom details read the [Profiles docs](https://docs.langchain.com/oss/python/deepagents/profiles) for the full field surface, merge semantics, and plugin packaging. Register a profile at startup for the models you use, or rely on the built-in profiles we ship.

If you&#x27;re building on Deep Agents and want to share a profile, [open a PR](https://github.com/langchain-ai/deepagents) or [distribute it as a plugin](https://docs.langchain.com/oss/python/deepagents/profiles#ship-a-profile-as-a-plugin) via entry points. We&#x27;ll keep extending the profile surface across models. The goal is that whichever model you reach choose, Deep Agents gives you the tools and defaults to create the best harness for your task. We’ll be releasing more information and walkthroughs showing how builders can customize their agent harness for their tasks.

*Note: This is currently only available in Python but is coming soon to TypeScript*

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ea236ce872ec8be413bd2f_runtime-behind-production-deep-agents-thumbnail.png)Conceptual GuideDeep Agents

#### The runtime behind production deep agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Sydney RunkleVivek TrivedyApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)24min[](/blog/runtime-behind-production-deep-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)