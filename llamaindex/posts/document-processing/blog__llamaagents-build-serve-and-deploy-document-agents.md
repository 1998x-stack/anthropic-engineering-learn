---
title: "LlamaAgents Open Preview: Build Document Agents | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/llamaagents-build-serve-and-deploy-document-agents"
category: "document-processing"
---

Content



- [ LlamaAgents: Bringing Together the Best of LlamaParse and Agent Workflows  ](#llamaagents-bringing-together-the-best-of-llamaparse-and-agent-workflows)
- [ The CLI Tool for Serving and Deploying Agent Workflows: llamactl  ](#the-cli-tool-for-serving-and-deploying-agent-workflows-llamactl)
- [ Build an SEC Insights Agent  ](#build-an-sec-insights-agent)
- [ Serve the Agent Locally  ](#serve-the-agent-locally)
- [ Deploy the Agent to LlamaParse  ](#deploy-the-agent-to-llamaparse)
- [ Deploy the Agent to LlamaParse  ](#deploy-the-agent-to-llamaparse)
- [ How to Get Started  ](#how-to-get-started)
- [ What’s Next  ](#whats-next)



 Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)



   2



 A few weeks ago we announced the early alpha waitlist for LlamaAgents. It’s the fastest way to build multi-step workflows over your documents, by complementing the core document processing capabilities of [LlamaParse](https://www.llamaindex.ai/llamacloud) with the orchestration flexibility of [Agent Workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/), enabling you to solve end-to-end tasks. Together, they empower you to:


-  jumpstart development with customizable, pro-code agent templates
  -  create a local server for your agent workflow with a single command
  -  deploy an agent to the cloud as a headless API or in the LlamaParse UI with a single command



 Today, we’re excited to open LlamaAgents for **open preview**, where we are especially doubling down on *document extraction agents*. In this article, we’ll give you an overview of what’s available now and what you can expect in the coming weeks and months. In this article, we&#39;ll give you an overview of what we have so far, and what you can expect in the coming weeks and months.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  **LlamaAgents: Bringing Together the Best of LlamaParse and Agent Workflows**



 At LlamaIndex, building powerful document-processing solutions is central to our mission with LlamaParse. Along the way, we’ve learned a great deal about the challenges of integrating documents into AI workflows. No two documents look alike: layouts vary widely, tables can be long or split across pages with merged cells, and charts and images often contain essential context. In short, bringing rich, complex documents into AI workflows is a unique and meaningful challenge, and critical to solve in order to enable any type of downstream automation with AI agents.



 That’s exactly why we’ve spent the past two-plus years investing in agent frameworks that make these workflows predictable and steerable. Early agent systems often relied on unrestricted LLMs to make every decision, but real production use cases demand more control. You need to dictate how the agent operates, what it can and can’t do, and how it handles the complexity inherent in real documents. Our [Agent Workflows](https://www.llamaindex.ai/workflows) enable this with an event-driven architecture that spans the [full spectrum of development patterns](https://www.anthropic.com/engineering/building-effective-agents) ,from free-form LLM behavior to tightly orchestrated flows, so you can precisely manage decision steps, reasoning loops, LLM invocation points, and everything in between.



 LlamaAgents brings together the best of [LlamaParse](https://www.llamaindex.ai/llamacloud)’s advanced document processing capabilities and the easy of workflow orchestration with Agent Workflows. It enables developers to build advanced document agents that are completely customizable to specific business needs. We simplify building with LlamaAgents through our CLI (`llamactl` ) for agent templates and deployment assistance, as well as our emerging vibe-coding capabilities to ease the development process from idea to production.



 Whether you&#39;re building an agent that triages incoming documents, one that extracts structured data from unstructured PDFs, or a complex pipeline that does both and more, LlamaAgents gives you the tools to take it from prototype to production.



 In the following section, let’s walk through how you can get started, using `llamactl` , our CLI tool for getting started with LlamaAgents.







###  The CLI Tool for Serving and Deploying Agent Workflows: `llamactl`



 To ease the process of getting started, building, serving and deploying Agent Workflows, we’ve released a CLI tool (`llamactl` ) alongside LlamaAgents. It&#39;s designed to make the journey from local development to production deployment as straightforward as possible. `llamactl`  bootstraps an application server that manages running and persisting your workflows, and a control plane for managing cloud deployments of applications.



###  Build an SEC Insights Agent



 In this example, let’s initialize and deploy the “SEC Insights” agent starting with the template. This is a multi-step agent that will:


-  Classify SEC filings by type using LlamaClassify: filings will be classified as 10K, 10Q, 8K or other
  -  Depending on the result of the classification, the document will be sent off to the relevant extraction agent, with specific schemas defined for each filing type
  -  Finally, the UI will allow you to review the extraction result for approval.



 To get started, all you have to do is run `llamactl init`  and select the SEC Insights template




 The rest of the `llamactl`  templates include:


-  An Extraction Agent with a Review UI that you can configure with your custom extraction schema
  -  An Invoice Extraction Agent
  -  Document Q&amp;A with a UI that allows you to have a chat interface over a set of documents that you upload
  -  A Showcase Agent, demonstrating capabilities of Agent Workflows and how to integrate a UI, such as streaming, human in the loop, and fan out.
  -  A Document Parser
  -  A Human in the Loop Agent
  -  Basic templates for both UI and API that you can use as a blank slate for your agent.



 and more.



 Once you select a template, `llamactl`  pulls a template repository which you can access and modify in your local environment. Each template repository will include a few things:


-  A set of Python files with the agent workflow(s) that contain the core of your agent orchestration.
  -  UI elements that comes with your agent template (if any).
  -  A [`pyproject.toml` ](https://developers.llamaindex.ai/python/llamaagents/llamactl/configuration-reference#pyprojecttoml) where your agent configuration is managed, including the list of agent workflows and.or UI elements in your application.
  -  A `README.md`  with instructions (such as the required API keys for model providers and/or LlamaParse).
  -  As well as As well as built in configuration and documentation for coding agents (Cursor, Claude, etc.)



 You are free to modify everything about this repository, push it to a remote repository and collaborate with others on your final code.



###  Serve the Agent Locally



 When you’re ready, `llamactl`  also helps you serve your agent locally by running `llamactl serve` .



 Here, we’re serving the SEC Insights agent. You’ll see us uploading an NVIDIA 10K filing. The agent then classifies it as a 10K filing and extracts the relevant fields. We then get the option to review and approve the output of the extraction step.




 The `llamactl serve`  command installs all required dependencies, reads the workflows configured in your app&#39;s `pyproject.toml`  and serves them as an API.



 The development server will detect changes as you save files and will even resume in-progress workflows. This means you can iterate quickly without losing state or having to restart long-running processes. For example, if you configure a workflow in your `pyproject.toml` , it&#39;ll be automatically served at an endpoint like `/deployments/my-package/workflows/my-workflow/run`  where you can trigger it with a POST request.



>  Serving Agent Workflows locally is available to all Agent Workflow users. To deploy an agent to LlamaParse, sign up [here](https://landing.llamaindex.ai/llamaagents).



###  Deploy the Agent to LlamaParse



 When you&#39;re ready to move to production, deploying your agent is remarkably straightforward. LlamaAgents applications can be deployed to LlamaParse just by pointing to a source git repository. With the provided repository configuration, LlamaParse will clone, build, and serve your app. It even supports private GitHub repositories through the LlamaAgents GitHub app.



 The deployment process is simple: push your code to a git repository, then run `llamactl deploy create` . This opens an interactive Terminal UI where you can configure your deployment details including name, git repository, branch, and secrets. All required fields are automatically detected from your environment but can be customized.



 The `llamactl serve`  command installs all required dependencies, reads the workflows configured in your app&#39;s `pyproject.toml`  and serves them as an API.



 The development server will detect changes as you save files and will even resume in-progress workflows. This means you can iterate quickly without losing state or having to restart long-running processes. For example, if you configure a workflow in your `pyproject.toml` , it&#39;ll be automatically served at an endpoint like `/deployments/my-package/workflows/my-workflow/run`  where you can trigger it with a POST request.



>  Serving Agent Workflows locally is available to all Agent Workflow users. To deploy an agent to LlamaParse, sign up [here](https://landing.llamaindex.ai/llamaagents).



###  Deploy the Agent to LlamaParse



 When you&#39;re ready to move to production, deploying your agent is remarkably straightforward. LlamaAgents applications can be deployed to LlamaParse just by pointing to a source git repository. With the provided repository configuration, LlamaParse will clone, build, and serve your app. It even supports private GitHub repositories through the LlamaAgents GitHub app.



 The deployment process is simple: push your code to a git repository, then run `llamactl deploy create` . This opens an interactive Terminal UI where you can configure your deployment details including name, git repository, branch, and secrets. All required fields are automatically detected from your environment but can be customized.



 Below, you’ll see us deploying the SEC Insights Agent to LlamaParse, this time uploading and extracting the NVIDIA 10Q filing.




 After creation, the TUI will show deployment status and logs. You can later use `llamactl deployments get`  to view again, add secrets or change branches with `llamactl deployments edit` , and if you update your source repo, run `llamactl deployments update`  to roll a new version.



##  How to Get Started



 You can start building and serving document agents with LlamaAgents today. If you&#39;re already using Agent Workflows, you can immediately begin serving your workflows locally as APIs using llamactl. Simply install the CLI tool and run `llamactl serve`  to get your agent up and running on your machine.



 When you&#39;re ready to deploy to production, we&#39;re onboarding users in batches - [sign up](https://landing.llamaindex.ai/llamaagents) and you&#39;ll get access without a lengthy waitlist. Once you have deployment access, pushing your agents to production is as simple as pointing `llamactl`  to your git repository.



 **Resources to get started:**


-  [**Getting Started with llamactl**](https://developers.llamaindex.ai/python/llamaagents/llamactl/getting-started/) - Install the CLI and initialize your first project
  -  [**Agent Workflows Documentation**](https://developers.llamaindex.ai/python/llamaagents/workflows/) - Learn how to build custom agent workflows
  -  [**Serve your Agent Worklflow**](https://developers.llamaindex.ai/python/llamaagents/workflows/) - Detailed guide on defining and exposing workflows
  -  [**llamactl Command Reference**](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-serve) - Complete CLI documentation for serving and deploying
  -  [**Deployment Configuration Reference**](https://developers.llamaindex.ai/python/llamaagents/llamactl/configuration-reference) - Configure your deployment settings



 Sign up for deployment access [here](https://landing.llamaindex.ai/llamaagents) and start building your production document agents today.



##  What’s Next



 In the coming weeks, we’ll be pushing updates and new features to LlamaAgents as a whole. For example, you’ll slowly start to see pre-made templates in LlamaParse which you can click and deploy from within the UI.