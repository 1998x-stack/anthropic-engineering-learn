---
title: "Execute Code with Sandboxes for Deep Agents"
author: "LangChain Accounts"
date: "2025-11-13"
url: "https://www.langchain.com/blog/execute-code-with-sandboxes-for-deepagents"
---

Deep Agents

# Execute Code with Sandboxes for Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyNovember 13, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa406849b7969db84053_Blog-Header_02.png)By Vivek Trivedy

Today we&#x27;re excited to launch Sandboxes for Deep Agents, a new set of integrations that allow you to safely execute arbitrary Deep Agent code in remote sandboxes. We currently support sandboxes from 3 of our partners: [Runloop](https://www.runloop.ai/?ref=blog.langchain.com), [Daytona](https://www.daytona.io/?ref=blog.langchain.com), and [Modal](https://modal.com/?ref=blog.langchain.com). Below, we dive into what you can do with sandboxes and how to use them with with the Deep Agents CLI.

## Why Do We Need Sandboxes?

Sandboxes give us a simple, configurable environment to execute code and do work outside of our local machine. Here are some scenarios where this may be useful:

- **Safety**: Your agent is executing arbitrary code which could be harmful to your local machine (ex: `rm -rf`). Running in a sandbox means your machine is safe from potentially malicious code.
- **Clean Environments**: You need specific dependencies, languages, or OS configurations without polluting your local setup. Spin up a sandbox with exactly what you need, use it, then terminate it.
- **Parallel Execution**: Run multiple agents simultaneously, each in their own isolated environment, without resource conflicts or interference.
- **Long-Running Tasks**: Let agents work on time-intensive operations without blocking your local machine.
- **Reproducibility**: Guarantee consistent execution environments across your team.

## How It Works

The sandbox integration has three main steps:

- Setup the sandbox (with an optional setup script)
- The agent wants to execute a command
- The remote sandbox runs the command and sends it back to the user

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa406849b7969db84059_deepagents-sandbox.png)*Easily attach, configure, and use sandboxes with DeepAgents to safely execute code*

Your Deep Agent runs locally (or wherever you want), but when it needs to execute code, create files, or run commands, those operations happen in the remote sandbox. The agent maintains full visibility into the sandbox filesystem and command outputs, so it can iterate naturally. The setup script can be used to load in environment variables, clone git repos, prepare your environment, and more.

## How to Get Started

To use Daytona and Runloop sandboxes, simply create an account and store the API key as an environment variable (`DAYTONA_API_KEY` and `RUNLOOP_API_KEY`). To use Modal sandboxes, follow the setup instructions found [here](https://modal.com/docs/guide?ref=blog.langchain.com#getting-started) and run `modal setup`.

After completing the setup, the Deep Agents CLI provides simple commands to get started with sandboxes in minutes with convenient `sandbox` and `sandbox-setup` commands.

**Note:** we have context managers to automatically clean up sandboxes but we recommend checking your provider dashboard to be sure there’s no agent or sandbox that’s accidentally left running.

For example, the following command can be used to attach a runloop sandbox to your Deep Agent with a custom setup script located in your current directory: `uvx deepagents-cli --sandbox runloop --sandbox-setup ./setup.sh`

### Note: Using Sandboxes Securely

> While the sandbox is isolated, when working with untrusted inputs, agents are still prone to prompt injection. To mitigate the risks of having secrets present in the sandbox, we recommend running trusted setup scripts, using human-in-the-loop, and assigning short lived secrets. Sandbox APIs are evolving rapidly, and we expect more providers to support proxies that help mitigate prompt injection and secrets management concerns.

Here&#x27;s an example of a simple setup script that adds local environment variables like a GitHub token or OpenAI key into the sandbox, and pulls down a repository. The pre-requisites to run this script is that your local `.env` file contains the keys and tokens you need:

`#!/bin/bash
set -e  # Exit on any error

echo &quot;Configuring sandbox environment...&quot;

# 1. Clone your repository using GitHub token
echo &quot;Cloning repository...&quot;
git clone &lt;https://x-access-token:${GITHUB_TOKEN}@github.com/username/repo.git&gt; $$HOME/workspace
cd $$HOME/workspace
echo &quot;✓ Repository cloned&quot;

# 2. Make environment variables persistent for all future commands
echo &quot;Setting up environment variables...&quot;
cat &gt;&gt; ~/.bashrc &lt;&lt;&#x27;EOF&#x27;

# Add selected env variables to sandbox from local
export GITHUB_TOKEN=&quot;${GITHUB_TOKEN}&quot;
export FAL_API_KEY=&quot;${FAL_API_KEY}&quot;

# Auto-navigate to workspace
cd $$HOME/workspace
EOF

# 3. Activate the environment
source ~/.bashrc
echo &quot;✓ Environment configured&quot;
`

## What&#x27;s Next?

We&#x27;re excited to see how builders will use sandboxes with their Deep Agents. We&#x27;ll be adding more configuration options for sandboxes and sharing more examples on integrating sandboxes to do real work.

If you want to watch a tutorial on how to get started with sandboxes, get check our tutorial [here](https://youtu.be/CejntUP3muU?ref=blog.langchain.com).

Ready to start building? Get started with our [Deep Agents](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) documentation and [GitHub](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) repository today.

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