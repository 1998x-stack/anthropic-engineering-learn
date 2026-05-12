---
title: "Skills vs MCP tools for agents: when to use what"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what"
category: "tools-integrations"
---

Content



- [ MCP  ](#mcp)
- [ Skills  ](#skills)
- [ When to use what: our experience with the LlamaAgents Builder  ](#when-to-use-what-our-experience-with-the-llamaagents-builder)



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

     **

   56



 A somewhat heated debate has been going on recently: whether you should use skills or MCPs to allow your agents to interact with certain tools or access domain-specific knowledge.



 While the two options have some partial overlap, there are several important differences around setup, execution and target audience. Let’s take a look at all of this in this blog, along with trying to understand how to chose (or whether to chose) amongst the two. To understand the tradeoffs, we&#39;ll first explore what each approach offers, then look at when to use each based on real-world experience.



##  MCP



 Model Context Protocol (MCP) is a protocol designed to expand the capabilities of LLMs by providing them with tools that come from third party services, as well as resources (extra context for the LLM exposed in a file-like interface) and prompts (parametrized, use-case specific prompts).



 Despite not being too difficult to set up, most MCPs are designed to be used by developers, since they are already familiar with concepts like authorization, transports and the command line interface (many MCP servers use the stdio communication).



 To use MCP tools or to setup MCP servers often needs at least some level of knowledge and practice in these topics (which might not be everyones cup of tea), but beyond this first hurdle, MCPs are quite effective at *predictable* and *precise* execution. For example, let’s imagine we have a simple web scraping tool that, given a URL, scrapes the content of the associated web page. A common interaction pattern with your agent might be:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/9c6bc90a56734fe7627bc11355d32800ddef7ada-1920x1080.png)

 The interaction is straightforward: the agent easily understands the required inputs for MCP tools, sends a request, receives a response and leverages that to fulfill the user’s request.



 The scope of each tool is generally narrow and produces a *precise* response that satisfies the agents needs, and each response is mostly *predictable*: given the same input conditions, we will receive always the same response.



 This makes MCPs a *functional* interface, which executes specific logic under specific conditions, and is highly effective to deliver exactly what the LLM needs.



 However, there are tjree downsides on MCP usage, which are:


-  scaling the number of tools is difficult, as each tool needs to be properly discovered through a name or description, and for each tool the agent needs to follow a specific input schema. This has prompted developers to come up with MCP gateways or MCP discovery middlewares that can help agents navigate tools.
  -  unoptimized tools can easily clutter the context of the agent, by returning large contents
  -  And finally, latency: MCP tools involve network calls to external services, which introduces network latency on each invocation. Skills run locally and don&#39;t have this overhead, making them faster for operations that don&#39;t inherently require external data.



##  Skills



 Skills are a set of specialized, (and most importantly) local instructions that are domain-specific: they are often contained in markdown documents, with links to other resources and code snippets, but they are essentially behavioural instructions in natural-language that the agent adopts while dealing with particular use cases.



 Skills act as *contextual modification*, by injecting custom instructions to the agent’s context: the agent matches the skill with the user’s request, validates that it has permissions to follow all instructions present in the skill, creates a fresh context window in which the prompt from the skill is loaded, and executes the user’s request in that context, retuning the answer to the main conversation.



 Skills have the clear advantage that they can easily steer the behavior of the agent with natural language, which requires minimal setup and almost no technical knowledge, and has endless customization possibilities. On top of that, skills are presented to the agent via local directories and files, rather than external services via third party servers.



 To better understand how skills work, let&#39;s look at a typical directory structure:



bash






```
.claude/skills
├── pdf-parsing
│   ├── script.py
│   └── SKILL.md
├── python-code-style
│   ├── REFERENCE.md
│   └── SKILL.md
└── web-scraping
    └── SKILL.md
```
    As you can see:


-  for each skill folder, we have a `SKILL.md`  file, which contains the main instructions, for example:



bash






```
---
name: web-scraping
description: Scrape web pages based on a provided URL using the scpr CLI app.
---

When asked to scrape a web page, use the `scpr` command line interface in this way:

```bash
scpr --url &#x3C;https://example.com>
```

-  This will allow you read the page content as markdown.
  -  for some skills, we can have scripts that the skill references and should be executed while the skill is active (e.g. `pdf-parsing/script.py`  )
  -  for some skills, we can have more comprehensive explanations, often contained in a `REFERENCE.md`  file that is mentioned within the main skill for the agent to consult while the skill is active

  Here is a potential interaction flow for the same use case as the one we saw for MCP:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/8518ed919c16e7ac2a4f2a59bf2b6956e4662edd-1920x1080.png)

 The overall user experience is similar, but there is a key difference in the core execution logic: being defined with natural language leaves skills open for misinterpretations and hallucinations by the LLM, and, more generally, does not provide only one deterministic way to execute a task.



 While it looks like the skill is providing the agent with an executable tool directly, in reality it simply gives precise instructions on what it can do, and how, which can equally lead to failure or success based on the capacity of the LLM to interpret and execute those instructions. This is in contrast to an MCP tool, which once an agent chooses to use, is a straight forward API call under the hood, with clear input and output schemas.



 All in all, for the agent, the challenge it faces with an MCP tool is *deciding which tool to run and when* only. Whereas the challenge it faces with a skill is to *decide which skill to use, when, and how.* The how is answered by the agent itself, and largely depends on how well the agent reasons about the instructions in the skill.



##  When to use what: our experience with the LlamaAgents Builder



 While building the core agentic coding capabilities of [LlamaAgents Builder](https://www.llamaindex.ai/blog/llamaagents-builder-idea-to-deployed-agent-in-minutes), we were faced with the decision of wether to use the [LlamaIndex Documentation MCP](https://www.llamaindex.ai/blog/adding-native-mcp-to-llamaindex-docs) or write custom skills (see an example [here](https://github.com/run-llama/vibe-llama/blob/main/documentation/skills/structured-data-extraction/SKILL.md)) to provide context to the agent about how to use our LlamaParse SDK and Agent Workflows.



 At first, we decided to combine both approaches, providing the agent with both, believing that MCP could provide access to a vaster knowledge base for planning, whereas the skills could’ve been useful when directly dealing with writing code.



 What we saw while testing was really interesting:


-  Often, the context from our documentation MCP was enough to get the agent started on generating code with correct patterns
  -  Skills were rarely invoked, and often did not yield substantially better results compared to when only our documentation MCP was used



 Here&#39;s how MCPs and Skills stack up across key dimensions:



        Aspect
        MCP
        Skills


        Setup complexity**
        Moderate (requires dev knowledge of auth, transports, CLI)
        Minimal (just markdown files)


        **Execution model**
        Deterministic API calls with fixed schemas
        LLM interprets natural language instructions


        **Performance**
        Network latency per call
        Local, no network overhead


        **Best for**
        Precise, predictable operations with clear inputs/outputs
        Behavioral guidance and contextual adaptation


        **Maintenance**
        Centralized (server updates propagate automatically)
        Manual (edit local markdown files)


        **Scalability challenges**
        Tool discovery becomes complex with many tools
        Easy to add, but LLM selection complexity grows


        **Failure modes**
        Wrong tool selection
        Misinterpretation of instructions + wrong tool selection


 However, we ultimately see that the choice of MCP vs skills is less about what each technology *can* do, but rather more about the use case in which you need the agent to operate in. For example, given the local nature of skills, and our use case of providing LlamaParse and LlamaIndex specific capabilities to our coding agent, we heavily rely on everything being up to date in terms of code examples etc (given both LlamaParse SDKs and LlamaIndex is constantly being updated). Skills needed to be constantly kept up to date to the latest best code practices, whereas the LlamaIndex Docs MCP was constantly updated by documentation changes pushed as new features were added and old ones deprecated.



 If an agent needs to operate in a fast evolving space, where context might change rapidly, a single-source of truth is a win. So in our case, that meant that MCP was the way to go. On the other hand, if that’s not the case, skills provide a super light weight, easy to set-up, easy to maintain solution.