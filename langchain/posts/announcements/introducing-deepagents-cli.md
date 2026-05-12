---
title: "Introducing Deep Agents CLI"
author: "LangChain Accounts"
date: "2025-10-30"
url: "https://www.langchain.com/blog/introducing-deepagents-cli"
---

Company AnnouncementsDeep Agents

# Introducing Deep Agents CLI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyOctober 30, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa4ce7ec0692a2d0dc06_Deep-Agents-CLI-blog.png)*By *[*Vivek Trivedy*](https://www.linkedin.com/in/vivek-trivedy-433509134/?ref=blog.langchain.com)

We&#x27;re excited to introduce **Deep Agents CLI** for coding, research, and building agents with persistent memory. Now you can easily create and run custom Deep Agents directly from the terminal. It supports:

- **Read, write, and edit files** in your project
- **Execute shell commands** with human approval
- **Search the web** for current information
- **Make HTTP requests** to APIs
- **Learn and remember** information across sessions
- **Plan tasks** with visual todo lists

## Installation

`
uv tool install deepagents-cli

`

## Quick Start

### 1. Set Up Your API Keys

Deep Agents CLI supports any Large Language Model that supports tool calling. See [the docs](https://docs.langchain.com/oss/python/deepagents/cli/providers?ref=blog.langchain.com) for details.

### 2. Launch the CLI

Start Deep Agents in your project directory:

`
deepagents

`

### 3. Your First Task

Try asking the agent to help with a simple task:

`
You: Add type hints to all functions in src/utils.py

`

The agent will:

- Read the file
- Analyze the functions
- Show you a diff of proposed changes
- Ask for your approval before writing

There&#x27;s also an option to Auto-Accept Edits to speed up development

## Learning Through Memory

One of Deep Agents&#x27; most powerful features is its **persistent memory system**. The agent can learn information and recall it across sessions. Each agent stores its knowledge in `~/.deepagents/AGENT_NAME/memories/`:

By default, if you spin up Deep Agents it will create an agent with the name `agent` and use that by default. You can change the agent used (and therefor what memories are used) by specifying an agent name, eg `deepagents --agent foo`. See next section for more details.

The agent automatically follows a **Memory-First Protocol**:

- **During Research** - Checks `/memories/` for relevant knowledge
- **Before answering** - Searches memory files in case of uncertainty
- **When learning** - Saves new information to `/memories/`

### Example: Teaching API Patterns

`
You: Remember that our API endpoints follow this pattern:
- Use /api/v1/ prefix
- All POST requests return 201 on success
- Error responses include a &quot;code&quot; and &quot;message&quot; field

Save this as our API conventions.

Agent: I&#x27;ll save these API conventions to memory.
⚙ write_file(/memories/api-conventions.md)

`

Because this memory is persistent, the agent can use this information across future conversations.

`You: Create a new endpoint for user registration
Agent: Based on our API conventions, I&#x27;ll create an endpoint at
/api/v1/users that returns 201 on success and follows
our error format.
⚙ read_file(/memories/api-conventions.md)
⚙ write_file(src/routes/users.py)

`

### Memory Best Practices

**1. Use descriptive filenames** ✓ /memories/deployment-checklist.md ✗ /memories/notes.md

**2. Organize by topic**

`/memories/
├── backend/

│ ├── tools_to_use.md

│ └── api-design.md

├── frontend/

│ ├── component-patterns.md

└── security-setup.md

`

**3. Verify saved knowledge** Because memory is just a set of files, you can always inspect and validate its content manually or with the agent.

`You: Check what you know about our database

Agent: Let me check my memories...
⚙ ls /memories/
⚙ read_file(/memories/backend/database-schema.md)

Based on my memory, we use PostgreSQL with these tables...

`

You can also inspect the memory files manually by just looking at `~/.deepagents/AGENT_NAME/memories/`

### Managing Multiple Agents

You can create specialized agents for different projects or roles: From the Deep Agents CLI you can list existing agents, create new agents, or reset an agent to its default state (system prompts, memories, etc).

`deepagents list

deepagents --agent backend-dev

deepagents reset backend-dev

`

## Get Started Today

Get started with Deep Agents and the Deep Agent CLI today! We&#x27;re excited to see what you build.

Join the community and contribute:

- **GitHub**: [https://github.com/langchain-ai/deepagents](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com)
- **Documentation**: [https://docs.langchain.com/oss/python/deepagents/cli/overview](https://docs.langchain.com/oss/python/deepagents/cli/overview?ref=blog.langchain.com)
- **YouTube:** [https://youtu.be/IrnacLa9PJc](https://youtu.be/IrnacLa9PJc?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)