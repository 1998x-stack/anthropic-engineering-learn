---
title: "How We Made Our Docs Test Themselves"
author: "LangChain Accounts"
date: "2026-04-15"
url: "https://www.langchain.com/blog/our-docs-test-themselves"
---

Deep AgentsEngineering

# How We Made Our Docs Test Themselves

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc520e7b284e657a1faba_naomi-pentrel.png)Naomi PentrelApril 15, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc55eabcedb7ed1755cf9_79.png)

## Key Takeaways

- It is possible to test code samples in docs because most teams don’t do this, resulting in outdated content
- It doesn’t have to be a lot of manual work
- Give the Deep Agents CLI a try to make this happen

Stale code samples are a universal documentation problem. Every team that ships tutorials, API guides, or integration examples eventually sees examples break as dependencies change and APIs evolve. The problem is not unique to us, but it is exacerbated by how quickly our product—and the AI and LLM space more broadly—moves. New models, updated SDKs, and shifting best practices mean that what worked last month may not work today.

Making code samples *testable *solves this. That means running them in CI, asserting they execute correctly, and failing the build when they break. But setting up code samples to be testable is not trivial and requires some upfront investment. This setup cost can feel so daunting that the project never happens.

Delegating that work to agents is the perfect solution.

## The problem: incomplete inline code that can’t be tested

Inline code samples are convenient to write. You test the code, copy the relevant snippet, paste it into your markdown files (or other docs files) and you ship. The problem is they&#x27;re static and when an API changes you might forget to update the code sample if it uses that API.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc7716452e907f1c96691_deep_agents_docs_1_dark%201.png)

Ideally you want to know when code samples stop working. You want continuous integration tests. The same principle that applies to application code—automate checks, catch changes and regressions, fail the build when something breaks—applies to docs: treat code samples as code that must pass tests. To make code samples in docs testable the manual process looks like this:

- Extract inline code into standalone files.
- Add setup and teardown code.
- Add markup to designate what is the code snippet.
- Use tooling to extract the code snippet.
- Include the extracted code snippets as reusable [snippets](https://www.mintlify.com/docs/create/reusable-snippets) in the docs.
- Use CI to run the standalone code snippets regularly and when the samples change.

At LangChain, we used the Deep Agents CLI to offload the migration workflow. No coding required.

## The Solution: Deep Agents + Skills: Write instructions once, delegate the rest

The Deep Agents CLI is a command line agent that you can chat with. One of its capabilities is using information from skills to perform tasks. Skills are reusable instructions that the agent loads when a task matches the skill description. These skills can be written just like step-by-step instructions to a coworker who might do these tasks. That’s exactly what we did. We wrote each step for the agent to perform:

- **Move code into standalone files** under `src/code-samples/{product}`, organized by product area.
- **Add setup and teardown** to make code snippets complete runnable examples.
- **Lint the code** using the configured linters.
- **Add markup** to define the code snippet using `:snippet-start:` and `:snippet-end:` tags. If there is code that needs to be removed in the snippet it can be excluded with `:remove-start:` and `:remove-end:`.
- **Run the code samples** to test them.
- **Generate the snippets** based on the markup and include the generated files in the docs.

This is the agentic part of the flow, on top of that we need a GitHub action that regularly runs the tests and creates tickets if a test fails. 

This skill is in a hidden folder in our docs repo at [.deepagents/skills/docs-code-samples/SKILL.md](https://github.com/langchain-ai/docs/blob/main/.deepagents/skills/docs-code-samples/SKILL.md). With this set up, anyone can open the Deep Agents CLI from within the docs repo and ask the agent to make one or more code samples in the docs testable. When you ask a Deep Agent to &quot;migrate the inline code in `streaming.mdx` to testable code samples,&quot; it uses this skill. The agent creates the right files, adds the right tags, runs the right commands, and includes the code snippets in the docs files.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dfc7e57eea87677a369f63_deep_agents_docs_2_dark%201.png)

## SKILL.md

The `docs-code-samples` skill lives in [.deepagents/skills/docs-code-samples/SKILL.md](https://github.com/langchain-ai/docs/blob/main/.deepagents/skills/docs-code-samples/SKILL.md). Its frontmatter includes a `description` that tells the agent when to use it:

```
---
name: docs-code-samples
description: Use this skill when migrating inline code samples from LangChain docs (MDX files) into external, testable code files that are extracted with Bluehawk and used as Mintlify snippets. Applies when extracting code blocks from documentation, creating runnable code samples, using snippet delineators, or wiring Bluehawk output into MDX includes.
---
```

The body of the skill contains the full context for the agent:

- When to use the skill
- Directory structure and file layout
- Step-by-step migration instructions
- Commands to run and in what order
- Conventions (naming, tagging, imports)

You can view the full `SKILL.md` file in our [GitHub repository](https://github.com/langchain-ai/docs/blob/main/.deepagents/skills/docs-code-samples/SKILL.md).

## Getting Started

This is only one example of how you can use [skills](https://docs.langchain.com/oss/python/deepagents/skills) with deep agents in your repository.

To get started with the Deep Agents CLI, check out the [CLI docs](https://docs.langchain.com/oss/python/deepagents/cli/overview).

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