---
title: "Automating spreadsheet workflows with AI (Manaflow)"
author: "Tereza Tizkova"
date: "2024-09-11"
url: "https://e2b.dev/blog/automating-spreadsheet-workflows-with-ai"
category: "case-studies"
site: "e2b"
---

[Manaflow](https://manaflow.ai/) is a YC startup that uses AI to automate repetitive office work often done in spreadsheets. Using natural language, you can program AI agents via Notion-like UI, create & call custom tools, populate Manasheet columns, and execute your repetitive workflows on a cron schedule. 

#### What was your journey to building Manaflow? What problem does it solve?

The idea for Manaflow emerged from our conversations with over 200 business managers, directors, and operators across various industries. We noticed that small-to-mid-sized businesses (SMBs) are constantly overwhelmed with numerous manual workflows and heavily underutilized technology.

Throughout America, there are millions of white-collar workers with spreadsheets open, where each column represents a step of a task and each row represents a case of the task. At SMBs, these processes are traditionally manual, time-consuming, and tedious, hindering scalability. 

We knew that we wanted to build something that could even the automation playing field for these underdog businesses against the larger, tech-savvy corporations with teams of engineers. At first, it started as one of the many side projects that we hacked together, but it eventually grew into a startup as we kept talking to businesses about our idea, who were impressed by the technology and wanted to use our product.

Manaflow solves the pain by automating manual, repetitive office work that businesses do on a daily basis, especially those involving data analysis, calling APIs, and business actions. With automation, Manaflow enables more efficient scalability and frees up human resources for more strategic work while reducing errors.

#### How does the product work under the hood? What is the role of AI agents and "tools"?

Manaflow’s primary interface is a spreadsheet called a Manasheet where each column represents a step in the workflow and each row corresponds to an instance of a task. The workflow powering each spreadsheet is programmed using natural language, allowing non-technical users to describe tasks and steps in plain English, eliminating the need for coding skills. 

We have a list of custom tools that our users can call or create themselves that AI agents can call to execute different steps of the task. Each spreadsheet has an internal dependency graph to determine the execution order for each column. This also enables checkpoints, which allow for human intervention and audits. 

In addition, Manaflow has integrations with various external services, authenticated platforms, and APIs, enabling seamless automation of diverse business operations, from retrieving data from Google searches to processing Stripe invoices. Real-time monitoring and updates on the spreadsheets that serve as admin dashboards provide transparency and allow human operators to effectively manage workflow progress.

Lastly, operation managers can program AI agents to populate data into the cells and execute Manasheets for you. These AI agents are essentially managers that handle data entry and execution of the task for you if need be – they can be programmed to run on a cron schedule or via a button.

#### What are your techstack choices and why?

Manaflow is built primarily with TypeScript, Next.js, Postgres, and PartyKit. Each Manasheet is backed by a Postgres table. Manasheet executions spawn Durable Objects that execute code on [E2B sandboxes](/docs/sandbox/overview). We made these technical decisions in order to unify user-facing code interpreter sessions with every Manasheet cell execution. This made it easy to observe individual Manasheet cells’ code interpreter runs within a chat/notebook interface.

#### How and why are you using E2B? What other alternatives have you considered?

We are using [E2B](/docs) sandboxes to provide a [code interpreter](https://github.com/e2b-dev/code-interpreter) environment. When we started building, we relied on Pyodide to evaluate Python and StackBlitz to evaluate JS/TS in the user’s browser. However, some people wanted to install dependencies, execute compute-intensive code, run tasks on a schedule, and make requests to services that had CORS. At this point, we knew we had to move code execution out of the user’s browser. 

> "We found that E2B’s startup times were significantly faster than everything else we tried."

‍* *‍

We considered using Fly.io Machines, Modal, and Google Cloud Run, and implementing our own Jupyter clusters on basic cloud compute primitives. However, when evaluating these options, we found that E2B’s startup times were significantly faster than everything else we tried. And with the ease of use of the @e2b/code-interpreter package, choosing E2B was a no-brainer.

#### What is your vision for the future? What is next on your roadmap?

Automation will transform office work. But, rather than relying on third parties to build automations, we believe knowledge workers themselves will be empowered to automate their own tasks without needing to code. Today, operations managers are essentially expert workflow programmers at heart, orchestrating manual human tasks to achieve broader objectives. In the future, these managers will shift to directing AI agents instead.

Internal tools and software are widespread across companies of all sizes today. We believe that in the future, AI agents will take over the operation of these internal tools, which is a manual process traditionally done by humans. AI agents will automatically update new states on admin dashboards, with humans overseeing the process. The concept of internal tools will change forever with AI agents – instead of building physical internal tools, AI agents will automate processes end-to-end on one consolidated platform.

We hope to be the infrastructure layer above the foundation models so that businesses can seamlessly integrate state-of-the-art AI models into their current workflows.

#### See Manaflow in action

#### Learn more

- [Manaflow - website](https://manaflow.ai/)
- [Manaflow - LinkedIn page](https://www.linkedin.com/company/manaflow-ai/)
- [Manaflow - X page](https://x.com/manaflowai)
- [Lawrence Chen - website](https://lawrencecchen.com/)
- [Lawrence Chen - LinkedIn profile](https://www.linkedin.com/in/lawrencecchen/)
- [Lawrence Chen - X profile](https://x.com/lawrencecchen)