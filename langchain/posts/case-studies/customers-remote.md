---
title: "How Remote uses LangChain and LangGraph to onboard thousands of customers with AI"
author: "LangChain Accounts"
date: "2026-01-19"
url: "https://www.langchain.com/blog/customers-remote"
---

Case StudiesLangChainLangGraph

# How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)*Guest post written by José Mussa (Staff Software Engineer @ Remote)*

[Remote](https://remote.com/?ref=blog.langchain.com) is a fast-growing startup helping companies hire, manage, and pay employees globally from a single platform. Remote’s customers operate across many countries and regulatory environments, and they trust Remote as the system of record for their employee, payroll, and compliance data. Every new customer arrives with a unique set of HR and payroll data , with sometimes thousands of spreadsheets or large SQL exports. Migrating that data accurately and quickly is make-or-break for onboarding, but doing it manually simply doesn’t scale.

To solve this challenge, Remote built a Code Execution Agent inside its AI Service to automate these migrations. This agent brings together the reasoning power of large language models with the precision of deterministic code execution. Here&#x27;s how it works, why Remote chose LangChain and LangGraph to build it, and what they learned along the way.

## The Challenge: Context windows and hallucinations

LLMs are powerful, but they have hard limits. Every model has a context window: the maximum number of tokens it can process at once. Even state‑of‑the‑art models like GPT‑5 cap out around 400k tokens, far less than the millions of characters in a large payroll spreadsheet. Models also need part of that window to track instructions, system prompts, and conversation history.

Trying to feed a 50 MB Excel file directly into an LLM isn’t just expensive; it’s likely to produce hallucinations. As Anthropic engineers have pointed out, when agents call tools directly, every intermediate result flows through the model, which can add tens of thousands of tokens per call and even exceed the context limit.

For a global employment platform like Remote, where accuracy and compliance are non-negotiable, these constraints made it clear that a different approach to large-scale data migrations was necessary.

## The Solution: Let the models reason, let code execute

Remote’s Code Execution Agent separates the “thinking” from the “doing.” Instead of forcing the LLM to ingest all the data, it uses LangChain’s tool‑calling interface to decide what steps to take, then writes and runs real Python code to transform the data.

Anthropic&#x27;s research on code execution shows why this hybrid design works: by letting agents run code in a sandbox, tool definitions and intermediate results stay outside the context window. Only instructions and summaries pass through the model, dramatically cutting token usage and virtually eliminating hallucination risk.

Here&#x27;s how Remote’s agent works in practice:

- File ingestion. Customers upload their raw data (CSV, Excel or SQL exports) to Remote’s secure storage.
- Agent reasoning. Using LangChain’s tool‑calling, the agent receives a task like “Convert this file into Remote’s employee onboarding schema.” It maps out how to translate the input columns into the schema.
- Sandboxed execution. Behind the scenes, a Python sandbox (running in WebAssembly) executes the LLM‑generated code. Remote leans on libraries like Pandas because they&#x27;re fast and flexible for data analysis.
- Iterative refinement. The agent reviews the output, writes more code if needed, and repeats until the data meets the schema.
- Structured output. The final, validated JSON file is stored for ingestion. Large intermediate results never pass back to the model, keeping the context small.

This architecture started as a proof of concept where Remote fed a 5,000-row Excel file into the agent. The agent loaded the file in the sandbox, mapped each entry to the schema using Pandas, and could answer queries like &quot;What is the age of employee X?&quot; by running code instead of generating text. Remote also limits console output so the model doesn&#x27;t try to read entire datasets – a simple &quot;show the first N rows&quot; pattern borrowed straight from data science notebooks.

## Why LangChain and LangGraph

Remote chose LangChain because its ecosystem offers mature abstractions for prompt handling and tool invocation. Its modular design allowed the team to integrate multiple model providers and build on a standard interface instead of rolling out their own. The Remote AI Agent Toolkit (the open‑source package Remote publishes for partners) already uses LangChain to expose HR tasks as structured tools, so keeping the internal workflows consistent was a natural fit. LangChain gave Remote the foundation to focus on what matters most for them: safety, scalability, and developer experience.

Its node-and-edge model lets Remote represent complex workflows— ingestion, mapping, execution, validation— as a directed graph. Each step becomes a node with explicit transitions for success, failure, or retry. This makes the agent&#x27;s state transparent and recoverable, similar to how distributed systems engineers reason about pipelines. LangGraph&#x27;s focus on long-running, stateful agents was a perfect match for our multi-step migration process.

## Results and impact

By combining LLM reasoning with deterministic code execution, Remote has turned a manual process into an automated workflow. Their onboarding teams no longer write custom scripts for each customer – they simply plug data into the Code Execution Agent. The agent transforms diverse formats into a consistent JSON schema in hours instead of days.

Beyond speed, the system has made everything more reliable. Because the transformation logic runs as code in a sandbox, it&#x27;s repeatable and auditable, which is critical for a platform handling sensitive employment and payroll data across jurisdictions. The LLM guides the process, but the actual data manipulation happens with trusted Python libraries, completely sidestepping hallucination issues.

## Lessons learned

Building this AI agent taught Remote several lessons that now inform how its team builds AI systems across the company:

- LLMs are planners, not processors. Use them to reason about tasks and choose tools, but offload heavy data processing to code.
- Structure beats improvisation. Orchestrating workflows as graphs makes them much easier to debug and extend.
- Context tokens are precious. Large intermediate results should stay in the execution environment where they belong.
- Python remains the analytics workhorse. Libraries like Pandas offer fast, flexible data manipulation that&#x27;s hard to beat.

## What’s next

The Code Execution Agent is one building block in Remote’s broader AI platform. Whenever they spot a repetitive pattern across teams, like converting documents into structured records or extracting data from semi-structured forms, they abstract it into a reusable agent. A recent example is an Agentic OCR-to-JSON Schema prototype, which combines document parsing with an agentic workflow to outperform basic OCR by a wide margin.

As Remote refines these tools, the team is planning to contribute generic improvements back to LangChain&#x27;s open-source ecosystem and adopt new community innovations as they emerge.

## Final thoughts

Migrating HR data is one of the toughest parts of onboarding thousands of customers in a global employment platform. By pairing LangChain’s tool framework with LangGraph’s orchestration and a Python code‑execution layer, Remote built a system that handles complex transformations reliably and at scale. This hybrid approach of using LLMs for reasoning and code for execution reflects how Remote invests in AI as infrastructure: removing friction while enabling teams to focus on higher-level problems that help customers employ and pay anyone, anywhere.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)