---
title: "Long Horizon Document Agents"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/long-horizon-document-agents"
category: "document-processing"
---

Content



- [ Current State  ](#current-state)
- [ Document Work is Multi-Step, Iterative, and Collaborative  ](#document-work-is-multi-step-iterative-and-collaborative)
- [ An Inbox for Long-Horizon Document Work  ](#an-inbox-for-long-horizon-document-work)
- [ Concrete Use Cases for Long-Running Document Work  ](#concrete-use-cases-for-long-running-document-work)
- [ 1. Living FAQ and knowledge base maintenance  ](#1-living-faq-and-knowledge-base-maintenance)
- [ 2. PRD generation and iteration from scattered inputs  ](#2-prd-generation-and-iteration-from-scattered-inputs)
- [ 3. Contract and redline collaboration loops  ](#3-contract-and-redline-collaboration-loops)
- [ 4. Due diligence and continuous memo updates  ](#4-due-diligence-and-continuous-memo-updates)
- [ A quick disclaimer, and looking ahead  ](#a-quick-disclaimer-and-looking-ahead)



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



 Recently Sequoia predicted that [2026 is the year of long-horizon agents](https://x.com/gradypb/status/2011491957730918510?s=20). Long horizon agents are “AI that can figure things out [and] has some baseline knowledge (pre-training), the ability to reason over that knowledge (inference-time compute), and the ability iterate its way to the answer.” At LlamaIndex, we’re especially excited about how this translates into more end-to-end knowledge work automation, particularly over documents.



 Existing document-based AI use cases have either been long-running but constrained (e.g. a batch invoice processing flow through RPA), or non-deterministic but ~short-horizon (e.g. having the user ask ChatGPT deep research over a collection of existing files). There’s a huge opportunity to build agents that are simultaneously long-running, perhaps eventually perpetually running, but also incredibly general purpose and unconstrained in the input/action/output space.



##  Current State



 Most “document AI” products today fall into two simple buckets: repetitive document extraction or agentic chatbots:


-  **Document Extraction:** The primary workflow is taking in an unstructured document like a PDF and extracting the data into a system of record, to help automate otherwise manual work. This industry is otherwise known as Intelligent Document Processing (IDP) and has existed for at least a decade pre-genAI. The broader process automation layer is/was known as Robotic Process Automation (RPA).
  -  **Agentic Chatbots:** This encompasses the category of all genAI products centered around a chat interface, whether it is ChatGPT, Microsoft Copilot, Manus, or even Claude Cowork. It is much more general than pure “document AI”, but these interfaces power the large majority of genAI-based document work today. Users can upload an arbitrary number of unstructured docs, perhaps index that data within a filesystem or vector database, and can surface information. By augmenting these agents with MCP tools and skills, these agents can start performing actions beyond simply reading information.



 Both of the existing buckets already provide a ton of value to users. There’s also plenty of “AI transformation” happening in each bucket already, which on its own will have many billions of dollars of impact:


-  Low-code interfaces for process automation are going away in favor of vibe-coding and defining procedures in natural language ala Claude Skills.
  -  Both foundation models and agent harnesses are getting ever-better, which means that agentic chatbots will be able to handle increasingly complex requests e2e - albeit in a synchronous manner.



 The issue with current agent interfaces is that they are synchronous; they cannot operate autonomously without user input, which blocks their ability to do longer-running knowledge work.



 I predict a step change in 2026 where agents go from “workflows” to “employees” - they are able to continuously monitor a wide range of incoming events, collaborate with other agents and humans, notify and ask the human when needed, but otherwise do work on their own. This lines up with how “e2e document work” is actually performed by humans within a company.



##  Document Work is Multi-Step, Iterative, and Collaborative



 Assume you’re a knowledge worker within any mid-to-large size organization and you’re tasked with “creating a document that’s a single-source of truth” (e.g. FAQ from SharePoint docs, a PRD from brainstorms, an investment memo from a data room, a launch checklist from a dozen scattered notes). First, you need to dig up the relevant set of documents for research. Next, you write an initial draft of the document, and share it with a set of reviewers. Then reviewers leave comments. Then someone responds to those comments. There are edits. There’s a second round. Sometimes a third. Then signoffs. Then the doc ships.



 After the doc is shipped, it remains as a living document. The human might add more files to the data room; there might be ongoing communications on email/Slack/Teams that changes the product requirements.



 If agents can only exist in a way that’s synchronously dependent on human input, then efficiency gains from agentic automation are bottlenecked by our own bandwidth in processing and re-prompting the agent. The human still acts as the scheduler, the orchestrator, and the reviewer.



 The next step is to unblock these agents from depending solely on human input, so they can start to reliably automate long-running human work.



##  An Inbox for Long-Horizon Document Work



 I define a “long-horizon” document agent as a **general agent loop** that can solve document tasks end-to-end with minimal human input, *and* can keep making progress over time because it can be triggered by events that are not a chat message.



 Three pieces matter here:


-  **Triggers (beyond chat).** The default trigger today is “user sends a prompt”. Long horizon agents need to retrigger when the world changes: a redline comes in, a doc is edited, someone comments, a template changes, a new folder appears in a repository, a deadline is approaching.
  -  **A persistent task backlog.** The agent needs a place to put work that it can’t finish right now. Not everything should interrupt a human. Not everything should be attempted immediately. Some tasks need batching. Some tasks need escalation. Some tasks need “wait for approval”.
  -  **A human interface that is not just a chat box.** Chat is fine for ad hoc work. It’s a terrible primitive for managing a queue of ongoing document tasks. The UX you want looks closer to an “agent inbox” than a conversation thread.



 The interface will likely be less of a chat interface and more like an inbox:


-  “Draft PRD v0 created, waiting for review”
  -  “3 new comments on the spec, proposed edits prepared”
  -  “Source doc changed, downstream FAQ is now stale”
  -  “New data room folder detected, memo updated with new risks”
  -  “I’m blocked on missing context: who is the approver for X?”



 Each item is a task with state, references, and artifacts. The agent can keep iterating on tasks in the background of your workday, but it knows when to pull you in. And when it pulls you in, it does not just say “here’s the answer”. It shows you what changed, why it changed, and where it got the information from.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Concrete Use Cases for Long-Running Document Work



 The architecture above will let agents solve a much wider class of human workflows over documents end-to-end, compared to synchronous chat loops or process automation. Here are some concrete examples.



###  1. Living FAQ and knowledge base maintenance



 A long horizon document agent can watch a set of source docs (policy docs, product docs, support macros, release notes), keep a derived FAQ up to date, and open a task when something breaks.



 It is easy to generate an FAQ once: the human hooks up the relevant MCP tools and submits a prompt to search across sources to generate a summary. But it is a lot harder to have an agent continuously responsible for updating the FAQ in a largely autonomous manner. Here’s what it would have to do:


-  Detect drift in the data sources (new Sharepoint files, Slack, call transcripts), and decide which data source changes would justify triggering an update.
  -  Propose edits with citations back to the source paragraphs
  -  Sends notifications to humans to spot-check edits.
  -  Publish updates
  -  Keep doing this forever



 Compared to a chat loop, the agent can update the FAQ without human prompting by paying attention to event streams from data sources. Compared to a deterministic workflow, the agent can more dynamically listen to events, perform updates, and update humans without massive human configuration.



###  2. PRD generation and iteration from scattered inputs



 Product scoping requires a lot of thinking. It requires the product owner to scope out something that adheres to customer asks, is feasible from an engineering standpoint, is consistent with the overall product vision, and makes the right tradeoff between hill-climbing an existing feature vs. a net new revamp.



 It is also inherently an iterative process. There is the initial step of data gathering: brainstorm doc in Box/Sharepoint/Confluence, customer calls, past PRDs, launch postmortems, competitor notes, random Slack threads. The human can use that to generate an initial draft.



 But afterwards, there’s a necessary back and forth process of conversation with engineers, product leads, cross-functional teams like sales/marketing. Stakeholders will leave comments and have debates on product scope. The product owner can decide to push back, or realize they need to some additional research (which would retrigger the data gathering step) and/or update the PRD.



 General agent loops are already quite good at data gathering, extended thinking, deep research. There are two main gaps in creating an autonomous PRD agent: the first is figuring out how to proactively pay attention to incoming feedback from different sources, and the second is continuing to push on extended-horizon reasoning and self-reflection.



 Creating a long-horizon PRD agent is likely equivalent to creating a junior PM employee.



###  3. Contract and redline collaboration loops



 Legacy contract review software tends to be rule-based and performs simple document extraction. More recently, legal AI tools like [Harvey](https://www.harvey.ai/platform/assistant) offer tailored chat assistants that let the user upload some documents, and specify the task at hand. This is already a big value-add, but is dependent on human input to trigger the task.



 A long horizon version of a contract/redlining agent can try to own more of the e2e lifecycle. It obviously would still require human in the loop, but it can also perform more tasks independently without the user having to supply more context at every turn. For example:


-  A redline ‘event’ arrives
  -  The agent summarizes changes, flags deltas that matter, and maps them to your internal playbook
  -  It drafts suggested responses and questions
  -  It escalates high-risk items to Legal
  -  It maintains a running “deal state” across versions, not just a one-off analysis



 In this instance, the agent can keep the process moving and update its context by paying attention to ongoing events (e.g. redlines), without a human re-explaining the situation every time.



###  4. Due diligence and continuous memo updates



 Anyone who has done diligence knows the pain: new documents appear late, someone changes a model, someone finds a buried risk factor, and the memo is already “final”.



 A long horizon diligence agent can treat the memo as a living artifact that gets updated as the data room evolves:


-  New docs show up, agent classifies and extracts key points
  -  It updates a risk register and links back to sources
  -  It updates the memo draft and highlights what changed
  -  It asks for signoff when changes are material



 This is basically “continuous integration”, but for document-heavy knowledge work.



##  A quick disclaimer, and looking ahead



 This is farther away than shorter-horizon agents. Enterprises are still getting used to the idea of even synchronously triggering a long-running agent loop - for example, the concept of using [Claude Code for non-coding tasks](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) is still a relatively fresh concept that requires greater adoption. The concept of having an agent manage an inbox of ongoing work in a continuous fashion may still feel a bit far out.



 That said, even coding agents are making rapid progress in tackling long-horizon tasks (from [Ralph Wiggum](https://ghuntley.com/ralph/) to [beads](https://github.com/steveyegge/beads)/[gastown](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)). The ability to have a semi-autonomous software engineer might be closer than we think. Being explicit about long-running agents for knowledge work clarifies what to build now.



 If the future looks like long horizon document agents, then the boring infrastructure becomes the important part: parsing, extraction, indexing, citations, and workflows that can be composed safely. Those are the building blocks that let an agent read messy documents and turn them into reliable actions.



 We’re focused on building that layer for both short-horizon and long-horizon agents: the stuff that unlocks context from PDFs, slides, spreadsheets, and everything else that companies actually run on. A lot of today’s use cases are still classic IDP (classify/extract). We’re committed to solving that. But the bigger opportunity, longer term, is higher-level document collaboration agents that can operate over weeks, not minutes.