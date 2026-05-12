---
title: "LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA"
author: "LangChain Accounts"
date: "2026-03-16"
url: "https://www.langchain.com/blog/nvidia-enterprise"
---

Company AnnouncementsPartner

# LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba99ee691fa7cd1fa8176_bg-2--1-.png)*Comprehensive agent engineering platform combined with NVIDIA AI enables enterprises to build, deploy, and monitor production-grade AI agents at scale*

[*Press Release*](https://www.prnewswire.com/news-releases/langchain-announces-enterprise-agentic-ai-platform-built-with-nvidia-302714006.html?ref=blog.langchain.com)

**SAN FRANCISCO, March 16, 2026 /PRNewswire/ **— LangChain, the agent engineering company behind LangSmith and open-source frameworks that have surpassed 1 billion downloads, today announced a comprehensive integration with NVIDIA to deliver an enterprise-grade agentic AI development platform. As part of this collaboration, LangChain is also joining the[ *Nemotron Coalition*](https://nvidianews.nvidia.com/news/nvidia-launches-nemotron-coalition-of-leading-global-ai-labs-to-advance-open-frontier-models?ref=blog.langchain.com), NVIDIA&#x27;s global initiative to advance frontier open AI models through shared expertise, data, and compute.

The collaboration combines LangChain&#x27;s LangSmith agent engineering platform and its open-source frameworks (Deep Agents, LangGraph, and LangChain)with NVIDIA Agent Toolkit, including[ NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/?ref=blog.langchain.com) models,[ NVIDIA NeMo Agent Toolkit](https://developer.nvidia.com/nemo-agent-toolkit?ref=blog.langchain.com) profiling and optimization,[ NVIDIA NIM microservices](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/?ref=blog.langchain.com), and[ NVIDIA Dynamo](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/?ncid=partn-748028&amp;ref=blog.langchain.com) giving developers a complete stack to build, deploy, and continuously improve AI agents in production. The platform also incorporates[ NVIDIA OpenShell](https://nvidianews.nvidia.com/news/ai-agents?ref=blog.langchain.com), a secure runtime that sandboxes autonomous, self-evolving agents with policy‑based guardrails. Development teams often spend months building custom infrastructure rather than delivering business value. The LangChain-NVIDIA platform is designed to close that gap.

## **What the Platform Delivers**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9a1a2e29eee5bae3426_data-src-image-a75d6965-c150-4a16-a951-7b885807be19.png)

**Build with LangGraph, Deep Agents, and AI-Q: **The combined LangChain-NVIDIA stack enables developers to build agents at increasing levels of complexity. LangGraph provides a runtime for stateful multi-agent orchestration with complex control flows and human-in-the-loop patterns. Deep Agents, LangChain&#x27;s agent harness, goes further with built-in task planning, sub-agent spawning, long-term memory, and context management, enabling agents that run for minutes or hours across dozens of steps. Building on top of Deep Agents, NVIDIA AI-Q Blueprint is the flagship result of this collaboration: a full production enterprise deep research system that ranks #1 on deep research benchmarks. NeMo Agent Toolkit lets teams onboard existing LangGraph agents with minimal code changes and immediately access advanced profiling, evaluation, and MCP/A2A protocol support for composing multi-agent systems.

**Accelerate LangGraph with NVIDIA: **The LangChain NVIDIA software package provides NVIDIA-optimized execution strategies applied at compile time with no changes to node logic or graph edges. Parallel execution automatically identifies independent nodes and runs them concurrently, eliminating sequential bottlenecks. Speculative execution runs both branches of conditional edges simultaneously, discarding the wrong branch once the routing condition resolves. Together, these optimizations significantly reduce end-to-end latency for complex multi-step agent workflows.

**Deploy with NVIDIA NIM: **NIM microservices deliver up to 2.6x higher throughput compared to standard deployments across cloud, on-premise, and hybrid environments. Nemotron 3 Super&#x27;s MoE architecture enables cost-efficient deployment on a single GPU. NVIDIA NeMo Agent Toolkit adds production-readiness features including authentication, rate limiting, and a built-in UI for debugging deployed workflows. The toolkit&#x27;s GPU cluster sizing calculator lets teams profile their LangGraph workflows under load and forecast exact hardware requirements for scaling from a single user to thousands of concurrent sessions.

**Monitor with LangSmith and NeMo Agent Toolkit: **LangSmith, which has processed over 15 billion traces and 100 trillion tokens, provides application-level observability: distributed tracing, cost and latency monitoring, Insights Agent for automatically detecting usage patterns and failure modes on a recurring schedule, Polly for natural-language debugging and prompt engineering, and LangSmith CLI for working with trace data. The NeMo Agent Toolkit observability system natively exports telemetry to LangSmith, creating a unified view where infrastructure-level profiling (token usage, timing, throughput down to individual tokens) combines with LangSmith&#x27;s application-level tracing and AI-powered analysis in a single platform. To ensure enterprises have the right tools to embrace responsible AI practices, NVIDIA NeMo Guardrails integrates out of the box with LangChain, enabling teams to enforce content safety and policy compliance while customizing guardrails per use case.

**Evaluate across the Nemotron model family: **LangSmith and NeMo Agent Toolkit together provide comprehensive evaluation across the full agent lifecycle. LangSmith supports offline evaluation (human review, LLM-as-judge, pairwise comparison, CI/CD integration via pytest/Vitest/GitHub workflows) and online evaluation including multi-turn evals that score entire conversation trajectories for task completion and decision quality. NeMo Agent Toolkit complements this with RAG-specific evaluators, agent trajectory analysis, and a hyper-parameter and prompt optimizer. These capabilities are especially powerful when applied across the Nemotron model family: teams can benchmark the same agent across Nemotron 3 Nano (30B/3B active), Super (~100B/10B active), and Ultra (~500B/50B active), measuring tradeoffs between accuracy, latency, and cost to right-size model selection per task, then use NeMo Agent Toolkit&#x27;s automatic reinforcement learning to fine-tune the chosen Nemotron model for their specific workflows.

## **Looking Ahead**

### Deep Agents with GPU-Accelerated Compute

The collaboration also lays the groundwork for Deep Agents, LangChain&#x27;s framework for long-running, complex tasks requiring planning, persistent memory, and sub-agent coordination, to operate within GPU-accelerated compute sandboxes powered by[ NVIDIA CUDA-X libraries](https://developer.nvidia.com/cuda/cuda-x-libraries?ref=blog.langchain.com). This would enable agents to perform computationally intensive data processing using tools like[ NVIDIA cuDF](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf?ref=blog.langchain.com) for large-scale structured data manipulation and NVIDIA NeMo Curator for petabyte-scale data curation, opening new possibilities in industries like financial services and healthcare.

### Joining the Nemotron Coalition

LangChain is joining the Nemotron Coalition, a global collaboration of model builders and AI developers working together to build frontier-level open foundation models. The Coalition allows participants to contribute data, evaluation frameworks, and post-training innovation toward a shared foundation, while independently specializing and building differentiated AI systems for their own industries and use cases.

By joining the Coalition, LangChain aims to help shape the capabilities of frontier open models with the needs of agent developers in mind, ensuring that the models powering production agents are built with input from the teams deploying them at scale. The partnership reflects a shared commitment to open, transparent AI development and to jointly delivering tools and infrastructure that help customers move faster from prototype to production.

> *“With over 100 million monthly downloads of LangChain’s frameworks, we’ve seen that frontier models must go beyond raw intelligence to enable reliable tool use, long-horizon reasoning and agent coordination,” ****said Harrison Chase, Cofounder and CEO of LangChain.**** “Through the NVIDIA Nemotron Coalition, we will build the best agent harness for these models, rigorously evaluate their capabilities and provide comprehensive observability into agent behavior, helping make Nemotron models the best foundation for the next generation of AI agents.”*

> *&quot;Enterprises need open, flexible tooling to build AI agents customized for their workflows and deployed securely at scale. LangChain&#x27;s framework and LangSmith&#x27;s observability, combined with NVIDIA Nemotron models, Agent Toolkit and NIM microservices, give developers the complete foundation to move from prototype to production,&quot; said Justin Boitano, Vice President of Enterprise AI at NVIDIA.*

## **Availability**

The[ LangChain-NVIDIA integration](https://docs.langchain.com/oss/python/integrations/providers/nvidia?ref=blog.langchain.com) is available today. LangGraph and the LangChain framework are open-source at[ github.com/langchain-ai](http://github.com/langchain-ai?ref=blog.langchain.com). LangSmith is available at[ smith.langchain.com](http://smith.langchain.com/?ref=blog.langchain.com). NVIDIA Nemotron 3 Nano and Super are available on Hugging Face through NVIDIA NIM microservices with updated integrations with LangChain ecosystem, with Nemotron 3 Ultra expected in the first half of 2026. The NVIDIA NeMo Agent Toolkit is available at[ github.com/NVIDIA/NeMo-Agent-Toolkit](http://github.com/NVIDIA/NeMo-Agent-Toolkit?ref=blog.langchain.com).

## **About LangChain**

LangChain is the agent engineering platform powering top engineering teams, from AI startups to global enterprises. Its open-source frameworks, including LangChain, LangGraph, and Deep Agents, have surpassed 1 billion cumulative downloads and are used by over one million practitioners. LangSmith, the observability and evaluation platform, serves over 300 enterprise customers and has processed more than 15 billion traces and 100 trillion tokens. LangChain is backed by Sequoia Capital, Benchmark, and IVP. For more information, visit[ langchain.com](https://langchain.com/?ref=blog.langchain.com).

**Media Contacts:** [press@langchain.dev](mailto: press@langchain.dev)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)