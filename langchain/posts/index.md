# LangChain Blog Index

> Source: https://www.langchain.com/blog
> Archived: 2026-05-11
> Total: 409 articles

## File Structure

```
external/blog/langchain/posts/
├── langgraph-core/              # LangGraph framework: architecture, graphs, state, middleware
├── langsmith-observability/     # LangSmith: tracing, evals, monitoring, benchmarks
├── langsmith-deployment/        # LangSmith: deployment, LangServe, LangGraph Cloud/Platform
├── rag-knowledge/               # RAG: retrieval, chunking, embeddings, vector stores
├── deep-agents/                 # Deep Agents: agent builder, context engineering, memory
├── case-studies/                # Customer stories and real-world implementations
├── tools-integrations/          # Tools, SDKs, 3rd-party integrations
├── tutorials-guides/            # How-tos, tutorials, recipes, building guides
├── newsletters/                 # Weekly/monthly newsletters
├── announcements/               # Product launches, releases, funding, events
├── general/                     # Uncategorized
└── index.md                     # This file
```

## Category Summary

| Category | Articles |
| --- | --- |
| [Tools & Integrations](#tools-integrations) | 83 |
| [Case Studies](#case-studies) | 53 |
| [Announcements](#announcements) | 50 |
| [LangSmith Observability & Evals](#langsmith-observability) | 48 |
| [LangGraph Core](#langgraph-core) | 45 |
| [RAG & Knowledge](#rag-knowledge) | 38 |
| [LangSmith Deployment & Platform](#langsmith-deployment) | 28 |
| [Tutorials & Guides](#tutorials-guides) | 28 |
| [Deep Agents](#deep-agents) | 25 |
| [General](#general) | 7 |
| [Newsletters](#newsletters) | 4 |


## Announcements

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-28 | [Interrupt Preview: Meet the MC](https://www.langchain.com/blog/interrupt-preview-meet-the-mc) | [interrupt-preview-meet-the-mc.md](./announcements/interrupt-preview-meet-the-mc.md) |
| 2026-04-09 | [Previewing Interrupt 2026: Agents at Enterprise Scale](https://www.langchain.com/blog/previewing-interrupt-2026-agents-at-enterprise-scale) | [previewing-interrupt-2026-agents-at-enterprise-scale.md](./announcements/previewing-interrupt-2026-agents-at-enterprise-scale.md) |
| 2026-03-31 | [Announcing the LangChain + MongoDB Partnership: The AI Agent Stack That Runs On The Database You Already Trust](https://www.langchain.com/blog/announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust) | [announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust.md](./announcements/announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust.md) |
| 2026-03-23 | [Join LangChain at Google Cloud Next 2026](https://www.langchain.com/blog/join-langchain-at-google-cloud-next-2026) | [join-langchain-at-google-cloud-next-2026.md](./announcements/join-langchain-at-google-cloud-next-2026.md) |
| 2026-03-19 | [Introducing LangSmith Fleet](https://www.langchain.com/blog/introducing-langsmith-fleet) | [introducing-langsmith-fleet.md](./announcements/introducing-langsmith-fleet.md) |
| 2026-03-17 | [Introducing LangSmith Sandboxes: Secure Code Execution for Agents](https://www.langchain.com/blog/introducing-langsmith-sandboxes-secure-code-execution-for-agents) | [introducing-langsmith-sandboxes-secure-code-execution-for-agents.md](./announcements/introducing-langsmith-sandboxes-secure-code-execution-for-agents.md) |
| 2026-03-04 | [LangChain Skills](https://www.langchain.com/blog/langchain-skills) | [langchain-skills.md](./announcements/langchain-skills.md) |
| 2026-02-12 | [Join us for Interrupt: The Agent Conference](https://www.langchain.com/blog/join-us-for-interrupt-the-agent-conference) | [join-us-for-interrupt-the-agent-conference.md](./announcements/join-us-for-interrupt-the-agent-conference.md) |
| 2026-01-21 | [Deploy agents instantly with Agent Builder templates](https://www.langchain.com/blog/introducing-agent-builder-template-library) | [introducing-agent-builder-template-library.md](./announcements/introducing-agent-builder-template-library.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-12-10 | [Introducing Polly: Your AI Agent Engineer](https://www.langchain.com/blog/introducing-polly-your-ai-agent-engineer) | [introducing-polly-your-ai-agent-engineer.md](./announcements/introducing-polly-your-ai-agent-engineer.md) |
| 2025-12-10 | [Introducing LangSmith Fetch: Debug agents from your terminal](https://www.langchain.com/blog/introducing-langsmith-fetch) | [introducing-langsmith-fetch.md](./announcements/introducing-langsmith-fetch.md) |
| 2025-11-11 | [Join LangChain at AWS re:Invent 2025](https://www.langchain.com/blog/join-langchain-at-aws-re-invent-2025) | [join-langchain-at-aws-re-invent-2025.md](./announcements/join-langchain-at-aws-re-invent-2025.md) |
| 2025-10-30 | [Introducing Deep Agents CLI](https://www.langchain.com/blog/introducing-deepagents-cli) | [introducing-deepagents-cli.md](./announcements/introducing-deepagents-cli.md) |
| 2025-10-20 | [LangChain raises $125M to build the platform for agent engineering](https://www.langchain.com/blog/series-b) | [series-b.md](./announcements/series-b.md) |
| 2025-10-20 | [Reflections on Three Years of Building LangChain](https://www.langchain.com/blog/three-years-langchain) | [three-years-langchain.md](./announcements/three-years-langchain.md) |
| 2025-09-02 | [LangChain &amp; LangGraph 1.0 alpha releases](https://www.langchain.com/blog/langchain-langchain-1-0-alpha-releases) | [langchain-langchain-1-0-alpha-releases.md](./announcements/langchain-langchain-1-0-alpha-releases.md) |
| 2025-08-06 | [Introducing Open SWE: An Open-Source Asynchronous Coding Agent](https://www.langchain.com/blog/introducing-open-swe-an-open-source-asynchronous-coding-agent) | [introducing-open-swe-an-open-source-asynchronous-coding-agent.md](./announcements/introducing-open-swe-an-open-source-asynchronous-coding-agent.md) |
| 2025-07-29 | [Introducing Align Evals: Streamlining LLM Application Evaluation](https://www.langchain.com/blog/introducing-align-evals) | [introducing-align-evals.md](./announcements/introducing-align-evals.md) |
| 2025-07-16 | [LangSmith and LangGraph Platform are now available in AWS Marketplace](https://www.langchain.com/blog/aws-marketplace-july-2025-announce) | [aws-marketplace-july-2025-announce.md](./announcements/aws-marketplace-july-2025-announce.md) |
| 2025-05-15 | [Recap of Interrupt 2025: The AI Agent Conference by LangChain](https://www.langchain.com/blog/interrupt-2025-recap) | [interrupt-2025-recap.md](./announcements/interrupt-2025-recap.md) |
| 2025-02-18 | [LangMem SDK for agent long-term memory](https://www.langchain.com/blog/langmem-sdk-launch) | [langmem-sdk-launch.md](./announcements/langmem-sdk-launch.md) |
| 2025-02-03 | [Introducing Interrupt: The AI Agent Conference by LangChain](https://www.langchain.com/blog/introducing-interrupt-langchain-conference) | [introducing-interrupt-langchain-conference.md](./announcements/introducing-interrupt-langchain-conference.md) |
| 2025-01-29 | [Introducing the LangGraph Functional API](https://www.langchain.com/blog/introducing-the-langgraph-functional-api) | [introducing-the-langgraph-functional-api.md](./announcements/introducing-the-langgraph-functional-api.md) |
| 2025-01-14 | [Introducing ambient agents](https://www.langchain.com/blog/introducing-ambient-agents) | [introducing-ambient-agents.md](./announcements/introducing-ambient-agents.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-19 | [LangChain State of AI 2024 Report](https://www.langchain.com/blog/langchain-state-of-ai-2024) | [langchain-state-of-ai-2024.md](./announcements/langchain-state-of-ai-2024.md) |
| 2024-11-12 | [Introducing Prompt Canvas: a Novel UX for Developing Prompts](https://www.langchain.com/blog/introducing-prompt-canvas) | [introducing-prompt-canvas.md](./announcements/introducing-prompt-canvas.md) |
| 2024-10-24 | [LangChain&#x27;s Second Birthday](https://www.langchain.com/blog/langchain-second-birthday) | [langchain-second-birthday.md](./announcements/langchain-second-birthday.md) |
| 2024-09-16 | [Announcing LangChain v0.3](https://www.langchain.com/blog/announcing-langchain-v0-3) | [announcing-langchain-v0-3.md](./announcements/announcing-langchain-v0-3.md) |
| 2024-05-20 | [Documentation Refresh for LangChain v0.2](https://www.langchain.com/blog/documentation-refresh-for-langchain-v0-2) | [documentation-refresh-for-langchain-v0-2.md](./announcements/documentation-refresh-for-langchain-v0-2.md) |
| 2024-05-10 | [LangChain v0.2: A Leap Towards Stability](https://www.langchain.com/blog/langchain-v02-leap-to-stability) | [langchain-v02-leap-to-stability.md](./announcements/langchain-v02-leap-to-stability.md) |
| 2024-04-24 | [Announcing LangSmith is now a transactable offering in the Azure Marketplace](https://www.langchain.com/blog/announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace) | [announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace.md](./announcements/announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace.md) |
| 2024-04-05 | [Rethinking Our Documentation](https://www.langchain.com/blog/langchain-documentation-refresh) | [langchain-documentation-refresh.md](./announcements/langchain-documentation-refresh.md) |
| 2024-02-08 | [LangChain Partners with CommandBar on their Copilot User Assistant](https://www.langchain.com/blog/langchain-partners-with-commandbar-on-their-copilot-user-assistant) | [langchain-partners-with-commandbar-on-their-copilot-user-assistant.md](./announcements/langchain-partners-with-commandbar-on-their-copilot-user-assistant.md) |
| 2024-01-30 | [LangChain partners with Elastic to launch the Elastic AI Assistant](https://www.langchain.com/blog/langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant) | [langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant.md](./announcements/langchain-partners-with-elastic-to-launch-the-elastic-ai-assistant.md) |
| 2024-01-08 | [LangChain v0.1.0](https://www.langchain.com/blog/langchain-v0-1-0) | [langchain-v0-1-0.md](./announcements/langchain-v0-1-0.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-12-21 | [LangChain State of AI 2023](https://www.langchain.com/blog/langchain-state-of-ai-2023) | [langchain-state-of-ai-2023.md](./announcements/langchain-state-of-ai-2023.md) |
| 2023-12-12 | [Towards LangChain 0.1: LangChain-Core and LangChain-Community](https://www.langchain.com/blog/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1) | [the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1.md](./announcements/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1.md) |
| 2023-11-21 | [Introducing Tuna - A Tool for Rapidly Generating Synthetic Fine-Tuning Datasets](https://www.langchain.com/blog/introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets) | [introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets.md](./announcements/introducing-tuna-a-tool-for-rapidly-generating-synthetic-fine-tuning-datasets.md) |
| 2023-11-21 | [Introducing Dream – an AI no-code tool to build fully functional web apps and components with natural language](https://www.langchain.com/blog/introducing-dream) | [introducing-dream.md](./announcements/introducing-dream.md) |
| 2023-11-15 | [LangChain Expands Collaboration with Microsoft](https://www.langchain.com/blog/langchain-expands-collaboration-with-microsoft) | [langchain-expands-collaboration-with-microsoft.md](./announcements/langchain-expands-collaboration-with-microsoft.md) |
| 2023-10-31 | [LangChain Templates](https://www.langchain.com/blog/langchain-templates) | [langchain-templates.md](./announcements/langchain-templates.md) |
| 2023-10-26 | [Announcing Data Annotation Queues](https://www.langchain.com/blog/announcing-data-annotation-queue) | [announcing-data-annotation-queue.md](./announcements/announcing-data-annotation-queue.md) |
| 2023-10-24 | [LangChain&#x27;s First Birthday](https://www.langchain.com/blog/langchains-first-birthday) | [langchains-first-birthday.md](./announcements/langchains-first-birthday.md) |
| 2023-09-21 | [LangChain and Scrimba Partner to help Web Devs become AI Engineers](https://www.langchain.com/blog/langchain-and-scrimba-partner-to-help-web-devs-become-ai-engineers) | [langchain-and-scrimba-partner-to-help-web-devs-become-ai-engineers.md](./announcements/langchain-and-scrimba-partner-to-help-web-devs-become-ai-engineers.md) |
| 2023-09-05 | [Announcing LangChain Hub](https://www.langchain.com/blog/langchain-prompt-hub) | [langchain-prompt-hub.md](./announcements/langchain-prompt-hub.md) |
| 2023-08-01 | [LangChain Expression Language](https://www.langchain.com/blog/langchain-expression-language) | [langchain-expression-language.md](./announcements/langchain-expression-language.md) |
| 2023-07-31 | [Goodbye CVEs, Hello `langchain_experimental`](https://www.langchain.com/blog/goodbye-cves-hello-langchain-experimental) | [goodbye-cves-hello-langchain-experimental.md](./announcements/goodbye-cves-hello-langchain-experimental.md) |
| 2023-07-18 | [Announcing LangSmith, a unified platform for debugging, testing, evaluating, and monitoring your LLM applications](https://www.langchain.com/blog/announcing-langsmith) | [announcing-langsmith.md](./announcements/announcing-langsmith.md) |
| 2023-06-06 | [LangChain + Vectara: better together](https://www.langchain.com/blog/langchain-vectara-better-together) | [langchain-vectara-better-together.md](./announcements/langchain-vectara-better-together.md) |
| 2023-04-04 | [Announcing our $10M seed round led by Benchmark](https://www.langchain.com/blog/announcing-our-10m-seed-round-led-by-benchmark) | [announcing-our-10m-seed-round-led-by-benchmark.md](./announcements/announcing-our-10m-seed-round-led-by-benchmark.md) |


## Case Studies

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-29 | [How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith](https://www.langchain.com/blog/customers-madrigal) | [customers-madrigal.md](./case-studies/customers-madrigal.md) |
| 2026-04-20 | [How Credit Genie used Insights Agent to improve their AI financial assistant](https://www.langchain.com/blog/credit-genie-insights-agent-financial-assistant) | [credit-genie-insights-agent-financial-assistant.md](./case-studies/credit-genie-insights-agent-financial-assistant.md) |
| 2026-04-03 | [How My Agents Self-Heal in Production](https://www.langchain.com/blog/how-my-agents-self-heal-in-production) | [how-my-agents-self-heal-in-production.md](./case-studies/how-my-agents-self-heal-in-production.md) |
| 2026-03-26 | [How Kensho built a multi-agent framework with LangGraph to solve trusted financial data retrieval](https://www.langchain.com/blog/customers-kensho) | [customers-kensho.md](./case-studies/customers-kensho.md) |
| 2026-03-24 | [How Moda Builds Production-Grade AI Design Agents with Deep Agents](https://www.langchain.com/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents) | [how-moda-builds-production-grade-ai-design-agents-with-deep-agents.md](./case-studies/how-moda-builds-production-grade-ai-design-agents-with-deep-agents.md) |
| 2026-02-18 | [monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1](https://www.langchain.com/blog/customers-monday) | [customers-monday.md](./case-studies/customers-monday.md) |
| 2026-01-19 | [How Remote uses LangChain and LangGraph to onboard thousands of customers with AI](https://www.langchain.com/blog/customers-remote) | [customers-remote.md](./case-studies/customers-remote.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-12-16 | [Fastweb + Vodafone: Transforming Customer Experience with AI Agents using LangGraph and LangSmith](https://www.langchain.com/blog/customers-vodafone-italy) | [customers-vodafone-italy.md](./case-studies/customers-vodafone-italy.md) |
| 2025-11-20 | [How Jimdo empower solopreneurs with AI-powered business assistance](https://www.langchain.com/blog/customers-jimdo) | [customers-jimdo.md](./case-studies/customers-jimdo.md) |
| 2025-11-17 | [How ServiceNow uses LangSmith to get visibility into its customer success agents](https://www.langchain.com/blog/customers-servicenow) | [customers-servicenow.md](./case-studies/customers-servicenow.md) |
| 2025-09-11 | [Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith](https://www.langchain.com/blog/customers-monte-carlo) | [customers-monte-carlo.md](./case-studies/customers-monte-carlo.md) |
| 2025-07-29 | [How Bertelsmann Built a Multi-Agent System to Empower Creatives](https://www.langchain.com/blog/customer-bertelsmann) | [customer-bertelsmann.md](./case-studies/customer-bertelsmann.md) |
| 2025-05-19 | [How Webtoon Entertainment built agentic workflows with LangGraph to scale story understanding](https://www.langchain.com/blog/customers-webtoon) | [customers-webtoon.md](./case-studies/customers-webtoon.md) |
| 2025-04-29 | [How DocentPro Built a Multi-Agent Travel Companion with LangGraph](https://www.langchain.com/blog/customers-docentpro) | [customers-docentpro.md](./case-studies/customers-docentpro.md) |
| 2025-04-22 | [How Trellix cut log parsing time from days to minutes with LangGraph Studio and LangSmith](https://www.langchain.com/blog/customers-trellix) | [customers-trellix.md](./case-studies/customers-trellix.md) |
| 2025-04-15 | [TAMM AI Assistant: Transforming Government Services in Abu Dhabi with LangChain and LangGraph&quot;](https://www.langchain.com/blog/customers-abu-dhabi-government) | [customers-abu-dhabi-government.md](./case-studies/customers-abu-dhabi-government.md) |
| 2025-04-13 | [How Harmonic built an investment agent with LangGraph and LangSmith— so VCs can focus on founders](https://www.langchain.com/blog/customers-harmonic) | [customers-harmonic.md](./case-studies/customers-harmonic.md) |
| 2025-04-07 | [Why Definely chose LangGraph for building their multi-agent AI system](https://www.langchain.com/blog/customers-definely) | [customers-definely.md](./case-studies/customers-definely.md) |
| 2025-03-25 | [How Lovable uses LangSmith to debug &amp; monitor agents in production](https://www.langchain.com/blog/customers-lovable) | [customers-lovable.md](./case-studies/customers-lovable.md) |
| 2025-03-24 | [Vodafone transforms data operations with AI using LangChain and LangGraph](https://www.langchain.com/blog/customers-vodafone) | [customers-vodafone.md](./case-studies/customers-vodafone.md) |
| 2025-03-19 | [How Inconvo is improving customer-facing analytics with conversational AI built on LangGraph](https://www.langchain.com/blog/customers-inconvo) | [customers-inconvo.md](./case-studies/customers-inconvo.md) |
| 2025-03-10 | [How C.H. Robinson is transforming the logistics industry with LangChain](https://www.langchain.com/blog/customers-chrobinson) | [customers-chrobinson.md](./case-studies/customers-chrobinson.md) |
| 2025-03-05 | [How Build.inc used LangGraph to launch a Multi-Agent Architecture for automating critical CRE workflows for Data Center Development.](https://www.langchain.com/blog/how-build-inc-used-langgraph-to-launch-a-multi-agent-architecture-for-automating-critical-cre-workflows-for-data-center-development) | [how-build-inc-used-langgraph-to-launch-a-multi-agent-architecture-for-automating-critical-cre-workflows-for-data-center-development.md](./case-studies/how-build-inc-used-langgraph-to-launch-a-multi-agent-architecture-for-automating-critical-cre-workflows-for-data-center-development.md) |
| 2025-02-27 | [How MUFG Bank increased sales efficiency by 10x with LangChain](https://www.langchain.com/blog/customers-mufgbank) | [customers-mufgbank.md](./case-studies/customers-mufgbank.md) |
| 2025-02-12 | [How Klarna&#x27;s AI assistant redefined customer support at scale for 85 million active users](https://www.langchain.com/blog/customers-klarna) | [customers-klarna.md](./case-studies/customers-klarna.md) |
| 2025-02-10 | [How Vizient empowers healthcare providers with reliable GenAI insights using LangGraph and LangSmith](https://www.langchain.com/blog/customers-vizient) | [customers-vizient.md](./case-studies/customers-vizient.md) |
| 2025-02-06 | [How Infor is Transforming Enterprise AI using LangGraph and LangSmith](https://www.langchain.com/blog/customers-infor) | [customers-infor.md](./case-studies/customers-infor.md) |
| 2025-01-20 | [How Captide is redefining equity research with agentic workflows running on LangGraph Platform](https://www.langchain.com/blog/how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith) | [how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith.md](./case-studies/how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith.md) |
| 2025-01-20 | [How Minimal built a multi-agent customer support system with LangGraph &amp; LangSmith](https://www.langchain.com/blog/how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith) | [how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith.md](./case-studies/how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith.md) |
| 2025-01-13 | [Acxiom&#x27;s use of LangSmith for enhanced audience segmentation](https://www.langchain.com/blog/customers-acxiom) | [customers-acxiom.md](./case-studies/customers-acxiom.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-16 | [How AppFolio transformed property management workflows with Realm-X, built using LangGraph and LangSmith](https://www.langchain.com/blog/customers-appfolio) | [customers-appfolio.md](./case-studies/customers-appfolio.md) |
| 2024-12-03 | [How Cleric’s AI SRE leveled up with continuous learning through LangSmith](https://www.langchain.com/blog/customers-cleric) | [customers-cleric.md](./case-studies/customers-cleric.md) |
| 2024-11-26 | [How Airtop built web-automation for AI agents powered by the LangChain ecosystem](https://www.langchain.com/blog/customers-airtop) | [customers-airtop.md](./case-studies/customers-airtop.md) |
| 2024-11-18 | [How Dun &amp; Bradstreet’s ChatD&amp;B™ uses LangChain and LangSmith to deliver trusted, data-driven AI insights](https://www.langchain.com/blog/customers-dun-bradstreet) | [customers-dun-bradstreet.md](./case-studies/customers-dun-bradstreet.md) |
| 2024-11-06 | [How Chaos Labs built a multi-agent system for resolution in prediction markets](https://www.langchain.com/blog/how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets) | [how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets.md](./case-studies/how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets.md) |
| 2024-10-09 | [How Rexera’s AI agents drive quality control with LangGraph](https://www.langchain.com/blog/customers-rexera) | [customers-rexera.md](./case-studies/customers-rexera.md) |
| 2024-10-08 | [Unify Launches Agents for Account Qualification using LangGraph and LangSmith](https://www.langchain.com/blog/unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith) | [unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith.md](./case-studies/unify-launches-agents-for-account-qualification-using-langgraph-and-langsmith.md) |
| 2024-10-03 | [OpenRecovery: Transforming addiction recovery with LangGraph Platform](https://www.langchain.com/blog/customers-openrecovery) | [customers-openrecovery.md](./case-studies/customers-openrecovery.md) |
| 2024-09-26 | [Pushing LangSmith to new limits with Replit Agent&#x27;s complex workflows](https://www.langchain.com/blog/customers-replit) | [customers-replit.md](./case-studies/customers-replit.md) |
| 2024-09-25 | [How Tradestack launched their MVP in 6 weeks using LangGraph Cloud](https://www.langchain.com/blog/customers-tradestack) | [customers-tradestack.md](./case-studies/customers-tradestack.md) |
| 2024-09-04 | [How Paradigm runs and monitors thousands of agents in parallel with LangChain and LangSmith](https://www.langchain.com/blog/customers-paradigm) | [customers-paradigm.md](./case-studies/customers-paradigm.md) |
| 2024-08-15 | [How Podium optimized agent behavior and reduced engineering intervention by 90% with LangSmith](https://www.langchain.com/blog/customers-podium) | [customers-podium.md](./case-studies/customers-podium.md) |
| 2024-07-22 | [How Athena Intelligence optimized research reports with LangSmith, LangChain, and LangGraph](https://www.langchain.com/blog/customers-athena-intelligence) | [customers-athena-intelligence.md](./case-studies/customers-athena-intelligence.md) |
| 2024-07-09 | [LangSmith for the full product lifecycle: How Wordsmith quickly builds, debugs, and evaluates LLM performance in production](https://www.langchain.com/blog/customers-wordsmith) | [customers-wordsmith.md](./case-studies/customers-wordsmith.md) |
| 2024-07-02 | [Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith](https://www.langchain.com/blog/customers-new-computer) | [customers-new-computer.md](./case-studies/customers-new-computer.md) |
| 2024-06-19 | [How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x](https://www.langchain.com/blog/customers-factory) | [customers-factory.md](./case-studies/customers-factory.md) |
| 2024-02-14 | [Rakuten Group builds with LangChain and LangSmith to deliver premium products for its business clients and employees](https://www.langchain.com/blog/customers-rakuten) | [customers-rakuten.md](./case-studies/customers-rakuten.md) |
| 2024-01-25 | [How Mendable leverages LangSmith to debug Tools &amp; Actions](https://www.langchain.com/blog/how-mendable-leverages-langsmith-to-debug-tools-actions) | [how-mendable-leverages-langsmith-to-debug-tools-actions.md](./case-studies/how-mendable-leverages-langsmith-to-debug-tools-actions.md) |
| 2024-01-11 | [Ally Financial Collaborates with LangChain to Deliver Critical Coding Module to Mask Personal Identifying Information in a Compliant and Safe Manner](https://www.langchain.com/blog/ally-financial-collaborates-with-langchain-to-deliver-critical-coding-module-to-mask-personal-identifying-information-in-a-compliant-and-safe-manner) | [ally-financial-collaborates-with-langchain-to-deliver-critical-coding-module-to-mask-personal-identifying-information-in-a-compliant-and-safe-manner.md](./case-studies/ally-financial-collaborates-with-langchain-to-deliver-critical-coding-module-to-mask-personal-identifying-information-in-a-compliant-and-safe-manner.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-12-05 | [Transforming Mortgage Ops with LangChain &amp; LangSmith](https://www.langchain.com/blog/transforming-mortgage-ops-with-langchain-langsmith) | [transforming-mortgage-ops-with-langchain-langsmith.md](./case-studies/transforming-mortgage-ops-with-langchain-langsmith.md) |
| 2023-11-28 | [LLMs accelerate Adyen&#x27;s support team through smart-ticket routing and support agent copilot](https://www.langchain.com/blog/llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot) | [llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot.md](./case-studies/llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot.md) |
| 2023-11-14 | [Morningstar Intelligence Engine puts personalized investment insights at analysts&#x27; fingertips](https://www.langchain.com/blog/morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips) | [morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips.md](./case-studies/morningstar-intelligence-engine-puts-personalized-investment-insights-at-analysts-fingertips.md) |
| 2023-10-22 | [Robocorp’s code generation assistant makes building Python automation easy for developers](https://www.langchain.com/blog/robocorps-code-gen-assistant-makes-building-python-automation-easy-for-developers) | [robocorps-code-gen-assistant-makes-building-python-automation-easy-for-developers.md](./case-studies/robocorps-code-gen-assistant-makes-building-python-automation-easy-for-developers.md) |


## Deep Agents

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-05-08 | [building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel](https://www.langchain.com/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel) | [building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel.md](./deep-agents/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel.md) |
| 2026-04-29 | [Tuning Deep Agents to Work Well with Different Models](https://www.langchain.com/blog/tuning-deep-agents-different-models) | [tuning-deep-agents-different-models.md](./deep-agents/tuning-deep-agents-different-models.md) |
| 2026-04-20 | [The Runtime Behind Production Deep Agents](https://www.langchain.com/blog/runtime-behind-production-deep-agents) | [runtime-behind-production-deep-agents.md](./deep-agents/runtime-behind-production-deep-agents.md) |
| 2026-04-16 | [Running Subagents in the Background](https://www.langchain.com/blog/running-subagents-in-the-background) | [running-subagents-in-the-background.md](./deep-agents/running-subagents-in-the-background.md) |
| 2026-04-09 | [Deep Agents Deploy: an open alternative to Claude Managed Agents](https://www.langchain.com/blog/deep-agents-deploy-an-open-alternative-to-claude-managed-agents) | [deep-agents-deploy-an-open-alternative-to-claude-managed-agents.md](./deep-agents/deep-agents-deploy-an-open-alternative-to-claude-managed-agents.md) |
| 2026-04-07 | [Deep Agents v0.5](https://www.langchain.com/blog/deep-agents-v0-5) | [deep-agents-v0-5.md](./deep-agents/deep-agents-v0-5.md) |
| 2026-04-05 | [Continual learning for AI agents](https://www.langchain.com/blog/continual-learning-for-ai-agents) | [continual-learning-for-ai-agents.md](./deep-agents/continual-learning-for-ai-agents.md) |
| 2026-02-22 | [How we built Agent Builder’s memory system](https://www.langchain.com/blog/how-we-built-agent-builders-memory-system) | [how-we-built-agent-builders-memory-system.md](./deep-agents/how-we-built-agent-builders-memory-system.md) |
| 2026-02-19 | [How to Use Memory in Agent Builder](https://www.langchain.com/blog/how-to-use-memory-in-agent-builder) | [how-to-use-memory-in-agent-builder.md](./deep-agents/how-to-use-memory-in-agent-builder.md) |
| 2026-02-18 | [New in Agent Builder: all new agent chat, file uploads + tool registry](https://www.langchain.com/blog/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry) | [new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry.md](./deep-agents/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry.md) |
| 2026-02-17 | [Improving Deep Agents with harness engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) | [improving-deep-agents-with-harness-engineering.md](./deep-agents/improving-deep-agents-with-harness-engineering.md) |
| 2026-02-10 | [The two patterns by which agents connect sandboxes](https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes) | [the-two-patterns-by-which-agents-connect-sandboxes.md](./deep-agents/the-two-patterns-by-which-agents-connect-sandboxes.md) |
| 2026-01-28 | [Context Management for Deep Agents](https://www.langchain.com/blog/context-management-for-deepagents) | [context-management-for-deepagents.md](./deep-agents/context-management-for-deepagents.md) |
| 2026-01-21 | [Building Multi-Agent Applications with Deep Agents](https://www.langchain.com/blog/building-multi-agent-applications-with-deep-agents) | [building-multi-agent-applications-with-deep-agents.md](./deep-agents/building-multi-agent-applications-with-deep-agents.md) |
| 2026-01-16 | [How we built Agent Builder’s memory \| Building memory into your agents](https://www.langchain.com/blog/how-we-built-agent-builders-memory) | [how-we-built-agent-builders-memory.md](./deep-agents/how-we-built-agent-builders-memory.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-11-25 | [Using skills with Deep Agents](https://www.langchain.com/blog/using-skills-with-deep-agents) | [using-skills-with-deep-agents.md](./deep-agents/using-skills-with-deep-agents.md) |
| 2025-11-21 | [How agents can use filesystems for context engineering](https://www.langchain.com/blog/how-agents-can-use-filesystems-for-context-engineering) | [how-agents-can-use-filesystems-for-context-engineering.md](./deep-agents/how-agents-can-use-filesystems-for-context-engineering.md) |
| 2025-11-13 | [Execute Code with Sandboxes for Deep Agents](https://www.langchain.com/blog/execute-code-with-sandboxes-for-deepagents) | [execute-code-with-sandboxes-for-deepagents.md](./deep-agents/execute-code-with-sandboxes-for-deepagents.md) |
| 2025-10-28 | [Doubling down on Deep Agents](https://www.langchain.com/blog/doubling-down-on-deepagents) | [doubling-down-on-deepagents.md](./deep-agents/doubling-down-on-deepagents.md) |
| 2025-07-30 | [Deep Agents](https://www.langchain.com/blog/deep-agents) | [deep-agents.md](./deep-agents/deep-agents.md) |
| 2025-07-16 | [Open Deep Research](https://www.langchain.com/blog/open-deep-research) | [open-deep-research.md](./deep-agents/open-deep-research.md) |
| 2025-07-02 | [Context Engineering](https://www.langchain.com/blog/context-engineering-for-agents) | [context-engineering-for-agents.md](./deep-agents/context-engineering-for-agents.md) |
| 2025-06-23 | [The rise of &quot;context engineering&quot;](https://www.langchain.com/blog/the-rise-of-context-engineering) | [the-rise-of-context-engineering.md](./deep-agents/the-rise-of-context-engineering.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-05 | [Semantic Search for LangGraph Memory](https://www.langchain.com/blog/semantic-search-for-langgraph-memory) | [semantic-search-for-langgraph-memory.md](./deep-agents/semantic-search-for-langgraph-memory.md) |
| 2024-10-19 | [Memory for agents](https://www.langchain.com/blog/memory-for-agents) | [memory-for-agents.md](./deep-agents/memory-for-agents.md) |


## General

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-10-23 | [Beyond Text: Making GenAI Applications Accessible to All](https://www.langchain.com/blog/beyond-text-making-genai-applications-accessible-to-all) | [beyond-text-making-genai-applications-accessible-to-all.md](./general/beyond-text-making-genai-applications-accessible-to-all.md) |
| 2023-09-20 | [LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith](https://www.langchain.com/blog/langchain-docugami-webinar-lessons-from-deploying-llms-with-langsmith) | [langchain-docugami-webinar-lessons-from-deploying-llms-with-langsmith.md](./general/langchain-docugami-webinar-lessons-from-deploying-llms-with-langsmith.md) |
| 2023-08-17 | [Langchain x Predibase: The easiest way to fine-tune and productionize OSS LLMs](https://www.langchain.com/blog/langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms) | [langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms.md](./general/langchain-predibase-the-easiest-way-to-fine-tune-and-productionize-oss-llms.md) |
| 2023-07-13 | [LangChain x Context: Building Better Chat Products With User Analytics](https://www.langchain.com/blog/langchain-x-context-building-better-chat-products-with-user-analytics) | [langchain-x-context-building-better-chat-products-with-user-analytics.md](./general/langchain-x-context-building-better-chat-products-with-user-analytics.md) |
| 2023-04-17 | [AI-Powered Medical Knowledge: Revolutionizing Care for Rare Conditions](https://www.langchain.com/blog/ai-powered-medical-knowledge) | [ai-powered-medical-knowledge.md](./general/ai-powered-medical-knowledge.md) |
| 2023-03-02 | [Using the ChatGPT API to evaluate the ChatGPT API](https://www.langchain.com/blog/using-chatgpt-api-to-evaluate-chatgpt) | [using-chatgpt-api-to-evaluate-chatgpt.md](./general/using-chatgpt-api-to-evaluate-chatgpt.md) |
| 2023-01-16 | [LangChain Chat](https://www.langchain.com/blog/langchain-chat) | [langchain-chat.md](./general/langchain-chat.md) |


## LangGraph Core

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-17 | [Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering](https://www.langchain.com/blog/agentic-engineering-redefining-software-engineering) | [agentic-engineering-redefining-software-engineering.md](./langgraph-core/agentic-engineering-redefining-software-engineering.md) |
| 2026-04-15 | [How We Made Our Docs Test Themselves](https://www.langchain.com/blog/our-docs-test-themselves) | [our-docs-test-themselves.md](./langgraph-core/our-docs-test-themselves.md) |
| 2026-04-11 | [Your harness, your memory](https://www.langchain.com/blog/your-harness-your-memory) | [your-harness-your-memory.md](./langgraph-core/your-harness-your-memory.md) |
| 2026-04-08 | [Better Harness: A Recipe for Harness Hill-Climbing with Evals](https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals) | [better-harness-a-recipe-for-harness-hill-climbing-with-evals.md](./langgraph-core/better-harness-a-recipe-for-harness-hill-climbing-with-evals.md) |
| 2026-03-26 | [How Middleware Lets You Customize Your Agent Harness](https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness) | [how-middleware-lets-you-customize-your-agent-harness.md](./langgraph-core/how-middleware-lets-you-customize-your-agent-harness.md) |
| 2026-03-23 | [Two different types of agent authorization](https://www.langchain.com/blog/two-different-types-of-agent-authorization) | [two-different-types-of-agent-authorization.md](./langgraph-core/two-different-types-of-agent-authorization.md) |
| 2026-03-11 | [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) | [the-anatomy-of-an-agent-harness.md](./langgraph-core/the-anatomy-of-an-agent-harness.md) |
| 2026-03-09 | [How we built LangChain’s GTM Agent](https://www.langchain.com/blog/how-we-built-langchains-gtm-agent) | [how-we-built-langchains-gtm-agent.md](./langgraph-core/how-we-built-langchains-gtm-agent.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-12-09 | [Agent Engineering: A New Discipline](https://www.langchain.com/blog/agent-engineering-a-new-discipline) | [agent-engineering-a-new-discipline.md](./langgraph-core/agent-engineering-a-new-discipline.md) |
| 2025-10-25 | [Agent Frameworks, Runtimes, and Harnesses- oh my!](https://www.langchain.com/blog/agent-frameworks-runtimes-and-harnesses-oh-my) | [agent-frameworks-runtimes-and-harnesses-oh-my.md](./langgraph-core/agent-frameworks-runtimes-and-harnesses-oh-my.md) |
| 2025-10-22 | [LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones](https://www.langchain.com/blog/langchain-langgraph-1dot0) | [langchain-langgraph-1dot0.md](./langgraph-core/langchain-langgraph-1dot0.md) |
| 2025-10-13 | [Securing your agents with authentication and authorization](https://www.langchain.com/blog/agent-authorization-explainer) | [agent-authorization-explainer.md](./langgraph-core/agent-authorization-explainer.md) |
| 2025-10-07 | [Not Another Workflow Builder](https://www.langchain.com/blog/not-another-workflow-builder) | [not-another-workflow-builder.md](./langgraph-core/not-another-workflow-builder.md) |
| 2025-09-08 | [Agent Middleware](https://www.langchain.com/blog/agent-middleware) | [agent-middleware.md](./langgraph-core/agent-middleware.md) |
| 2025-09-04 | [Building LangGraph: Designing an Agent Runtime from first principles](https://www.langchain.com/blog/building-langgraph) | [building-langgraph.md](./langgraph-core/building-langgraph.md) |
| 2025-09-03 | [Standard message content](https://www.langchain.com/blog/standard-message-content) | [standard-message-content.md](./langgraph-core/standard-message-content.md) |
| 2025-07-10 | [How to Build an Agent](https://www.langchain.com/blog/how-to-build-an-agent) | [how-to-build-an-agent.md](./langgraph-core/how-to-build-an-agent.md) |
| 2025-06-09 | [LangGraph Release Week Recap](https://www.langchain.com/blog/langgraph-release-week-recap) | [langgraph-release-week-recap.md](./langgraph-core/langgraph-release-week-recap.md) |
| 2025-02-27 | [LangGraph 0.3 Release: Prebuilt Agents](https://www.langchain.com/blog/langgraph-0-3-release-prebuilt-agents) | [langgraph-0-3-release-prebuilt-agents.md](./langgraph-core/langgraph-0-3-release-prebuilt-agents.md) |
| 2025-02-22 | [Beyond RAG: Implementing Agent Search with LangGraph for Smarter Knowledge Retrieval](https://www.langchain.com/blog/beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval) | [beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval.md](./langgraph-core/beyond-rag-implementing-agent-search-with-langgraph-for-smarter-knowledge-retrieval.md) |
| 2025-02-05 | [Is LangGraph Used In Production?](https://www.langchain.com/blog/is-langgraph-used-in-production) | [is-langgraph-used-in-production.md](./langgraph-core/is-langgraph-used-in-production.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-31 | [Top 5 LangGraph Agents in Production 2024](https://www.langchain.com/blog/top-5-langgraph-agents-in-production-2024) | [top-5-langgraph-agents-in-production-2024.md](./langgraph-core/top-5-langgraph-agents-in-production-2024.md) |
| 2024-12-19 | [Custom Authentication and Access Control for LangGraph Platform](https://www.langchain.com/blog/custom-authentication-and-access-control-in-langgraph) | [custom-authentication-and-access-control-in-langgraph.md](./langgraph-core/custom-authentication-and-access-control-in-langgraph.md) |
| 2024-12-10 | [Command: A new tool for building multi-agent architectures in LangGraph](https://www.langchain.com/blog/command-a-new-tool-for-multi-agent-architectures-in-langgraph) | [command-a-new-tool-for-multi-agent-architectures-in-langgraph.md](./langgraph-core/command-a-new-tool-for-multi-agent-architectures-in-langgraph.md) |
| 2024-11-19 | [Agent Protocol: Interoperability for LLM agents](https://www.langchain.com/blog/agent-protocol-interoperability-for-llm-agents) | [agent-protocol-interoperability-for-llm-agents.md](./langgraph-core/agent-protocol-interoperability-for-llm-agents.md) |
| 2024-10-31 | [LangGraph Platform in beta: New deployment options for scalable agent infrastructure](https://www.langchain.com/blog/langgraph-platform-announce) | [langgraph-platform-announce.md](./langgraph-core/langgraph-platform-announce.md) |
| 2024-09-25 | [Introducing Assistant Editor for configuring agents in LangGraph Studio](https://www.langchain.com/blog/asssistant-editor) | [asssistant-editor.md](./langgraph-core/asssistant-editor.md) |
| 2024-09-11 | [Build stateful conversational AI agents with LangGraph and assistant-ui](https://www.langchain.com/blog/assistant-ui) | [assistant-ui.md](./langgraph-core/assistant-ui.md) |
| 2024-09-03 | [Build reliable agents in JavaScript with LangGraph.js v0.2: Now supporting Cloud and Studio](https://www.langchain.com/blog/javascript-langgraph-v02-cloud-studio) | [javascript-langgraph-v02-cloud-studio.md](./langgraph-core/javascript-langgraph-v02-cloud-studio.md) |
| 2024-08-10 | [UX for Agents, Part 3: Spreadsheet, Generative, and Collaborative UI/UX](https://www.langchain.com/blog/ux-for-agents-part-3) | [ux-for-agents-part-3.md](./langgraph-core/ux-for-agents-part-3.md) |
| 2024-08-07 | [LangGraph v0.2: Increased customization with new checkpointer libraries](https://www.langchain.com/blog/langgraph-v0-2) | [langgraph-v0-2.md](./langgraph-core/langgraph-v0-2.md) |
| 2024-08-03 | [UX for Agents, Part 2: Ambient](https://www.langchain.com/blog/ux-for-agents-part-2-ambient) | [ux-for-agents-part-2-ambient.md](./langgraph-core/ux-for-agents-part-2-ambient.md) |
| 2024-08-01 | [LangGraph Studio: The first agent IDE](https://www.langchain.com/blog/langgraph-studio-the-first-agent-ide) | [langgraph-studio-the-first-agent-ide.md](./langgraph-core/langgraph-studio-the-first-agent-ide.md) |
| 2024-07-27 | [UX for Agents, Part 1: Chat](https://www.langchain.com/blog/ux-for-agents-part-1-chat-2) | [ux-for-agents-part-1-chat-2.md](./langgraph-core/ux-for-agents-part-1-chat-2.md) |
| 2024-07-03 | [Jockey: A Conversational Video Agent Powered by Twelve Labs APIs and LangGraph](https://www.langchain.com/blog/jockey-twelvelabs-langgraph) | [jockey-twelvelabs-langgraph.md](./langgraph-core/jockey-twelvelabs-langgraph.md) |
| 2024-06-29 | [What is an AI agent?](https://www.langchain.com/blog/what-is-an-agent) | [what-is-an-agent.md](./langgraph-core/what-is-an-agent.md) |
| 2024-02-27 | [LangGraph for Code Generation](https://www.langchain.com/blog/code-execution-with-langgraph) | [code-execution-with-langgraph.md](./langgraph-core/code-execution-with-langgraph.md) |
| 2024-02-07 | [Meet Connery: An Open-Source Plugin Infrastructure for OpenGPTs and LLM apps](https://www.langchain.com/blog/meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps) | [meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps.md](./langgraph-core/meet-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps.md) |
| 2024-02-07 | [Self-Reflective RAG with LangGraph](https://www.langchain.com/blog/agentic-rag-with-langgraph) | [agentic-rag-with-langgraph.md](./langgraph-core/agentic-rag-with-langgraph.md) |
| 2024-01-31 | [OpenGPTs](https://www.langchain.com/blog/opengpts) | [opengpts.md](./langgraph-core/opengpts.md) |
| 2024-01-23 | [LangGraph: Multi-Agent Workflows](https://www.langchain.com/blog/langgraph-multi-agent-workflows) | [langgraph-multi-agent-workflows.md](./langgraph-core/langgraph-multi-agent-workflows.md) |
| 2024-01-17 | [LangGraph](https://www.langchain.com/blog/langgraph) | [langgraph.md](./langgraph-core/langgraph.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-11-29 | [Adding Long Term Memory to OpenGPTs](https://www.langchain.com/blog/adding-long-term-memory-to-opengpts) | [adding-long-term-memory-to-opengpts.md](./langgraph-core/adding-long-term-memory-to-opengpts.md) |
| 2023-04-03 | [Custom Agents](https://www.langchain.com/blog/custom-agents) | [custom-agents.md](./langgraph-core/custom-agents.md) |
| 2023-03-01 | [Agent Toolkits](https://www.langchain.com/blog/agent-toolkits) | [agent-toolkits.md](./langgraph-core/agent-toolkits.md) |


## LangSmith Deployment & Platform

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-27 | [How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements](https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act) | [langsmith-langchain-oss-eu-ai-act.md](./langsmith-deployment/langsmith-langchain-oss-eu-ai-act.md) |
| 2026-04-07 | [Arcade.dev tools now in LangSmith Fleet](https://www.langchain.com/blog/arcade-dev-tools-now-in-langsmith-fleet) | [arcade-dev-tools-now-in-langsmith-fleet.md](./langsmith-deployment/arcade-dev-tools-now-in-langsmith-fleet.md) |
| 2026-03-18 | [Polly is generally available everywhere you work in LangSmith](https://www.langchain.com/blog/polly-langsmith-ga) | [polly-langsmith-ga.md](./langsmith-deployment/polly-langsmith-ga.md) |
| 2026-03-16 | [Introducing deploy cli](https://www.langchain.com/blog/introducing-deploy-cli) | [introducing-deploy-cli.md](./langsmith-deployment/introducing-deploy-cli.md) |
| 2026-03-04 | [LangSmith CLI &amp; Skills](https://www.langchain.com/blog/langsmith-cli-skills) | [langsmith-cli-skills.md](./langsmith-deployment/langsmith-cli-skills.md) |
| 2026-02-10 | [LangSmith is Now Available in Google Cloud Marketplace](https://www.langchain.com/blog/langsmith-is-now-available-in-google-cloud-marketplace) | [langsmith-is-now-available-in-google-cloud-marketplace.md](./langsmith-deployment/langsmith-is-now-available-in-google-cloud-marketplace.md) |
| 2026-01-13 | [Now GA: LangSmith Agent Builder](https://www.langchain.com/blog/langsmith-agent-builder-generally-available) | [langsmith-agent-builder-generally-available.md](./langsmith-deployment/langsmith-agent-builder-generally-available.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-12-02 | [LangSmith Agent Builder now in Public Beta](https://www.langchain.com/blog/langsmith-agent-builder-now-in-public-beta) | [langsmith-agent-builder-now-in-public-beta.md](./langsmith-deployment/langsmith-agent-builder-now-in-public-beta.md) |
| 2025-10-29 | [Introducing LangSmith’s No Code Agent Builder](https://www.langchain.com/blog/langsmith-agent-builder) | [langsmith-agent-builder.md](./langsmith-deployment/langsmith-agent-builder.md) |
| 2025-07-28 | [Why agent infrastructure matters](https://www.langchain.com/blog/why-agent-infrastructure) | [why-agent-infrastructure.md](./langsmith-deployment/why-agent-infrastructure.md) |
| 2025-05-22 | [Why do I need LangGraph Platform for agent deployment?](https://www.langchain.com/blog/why-langgraph-platform) | [why-langgraph-platform.md](./langsmith-deployment/why-langgraph-platform.md) |
| 2025-05-14 | [LangGraph Platform is now Generally Available: Deploy &amp; manage long-running, stateful Agents](https://www.langchain.com/blog/langgraph-platform-ga) | [langgraph-platform-ga.md](./langsmith-deployment/langgraph-platform-ga.md) |
| 2025-05-07 | [LangSmith Incident on May 1, 2025](https://www.langchain.com/blog/langsmith-incident-on-may-1-2025) | [langsmith-incident-on-may-1-2025.md](./langsmith-deployment/langsmith-incident-on-may-1-2025.md) |
| 2025-04-22 | [Catch production failures early with LangSmith Alerts](https://www.langchain.com/blog/langsmith-alerts) | [langsmith-alerts.md](./langsmith-deployment/langsmith-alerts.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-11-19 | [LangSmith: Redesigned product homepage and Resource Tags for better organization](https://www.langchain.com/blog/langsmith-homepage-redesign-and-resource-tags) | [langsmith-homepage-redesign-and-resource-tags.md](./langsmith-deployment/langsmith-homepage-redesign-and-resource-tags.md) |
| 2024-10-08 | [Launching Long-Term Memory Support in LangGraph](https://www.langchain.com/blog/launching-long-term-memory-support-in-langgraph) | [launching-long-term-memory-support-in-langgraph.md](./langsmith-deployment/launching-long-term-memory-support-in-langgraph.md) |
| 2024-09-19 | [Launching LangGraph Templates](https://www.langchain.com/blog/launching-langgraph-templates) | [launching-langgraph-templates.md](./langsmith-deployment/launching-langgraph-templates.md) |
| 2024-07-15 | [How We Deployed our Multi-Agent Flow to LangGraph Cloud](https://www.langchain.com/blog/how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2) | [how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2.md](./langsmith-deployment/how-we-deployed-our-multi-agent-flow-to-langgraph-cloud-2.md) |
| 2024-07-13 | [Why you should outsource your agentic infrastructure, but own your cognitive architecture](https://www.langchain.com/blog/why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture) | [why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture.md](./langsmith-deployment/why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture.md) |
| 2024-07-06 | [What is a &quot;cognitive architecture&quot;?](https://www.langchain.com/blog/what-is-a-cognitive-architecture) | [what-is-a-cognitive-architecture.md](./langsmith-deployment/what-is-a-cognitive-architecture.md) |
| 2024-06-27 | [Announcing LangGraph v0.1 &amp; LangGraph Cloud: Running agents at scale, reliably](https://www.langchain.com/blog/langgraph-cloud) | [langgraph-cloud.md](./langsmith-deployment/langgraph-cloud.md) |
| 2024-06-13 | [Workspaces in LangSmith for improved collaboration and organization](https://www.langchain.com/blog/workspaces-in-langsmith) | [workspaces-in-langsmith.md](./langsmith-deployment/workspaces-in-langsmith.md) |
| 2024-05-08 | [Role Based Access Control (RBAC) for LangSmith](https://www.langchain.com/blog/access-control-updates-for-langsmith) | [access-control-updates-for-langsmith.md](./langsmith-deployment/access-control-updates-for-langsmith.md) |
| 2024-04-02 | [LangSmith: Production Monitoring &amp; Automations](https://www.langchain.com/blog/langsmith-production-logging-automations) | [langsmith-production-logging-automations.md](./langsmith-deployment/langsmith-production-logging-automations.md) |
| 2024-02-15 | [Announcing the General Availability of LangSmith and Our Series A Led By Sequoia Capital](https://www.langchain.com/blog/langsmith-ga) | [langsmith-ga.md](./langsmith-deployment/langsmith-ga.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-11-28 | [OpenAI&#x27;s Bet on a Cognitive Architecture](https://www.langchain.com/blog/openais-bet-on-a-cognitive-architecture) | [openais-bet-on-a-cognitive-architecture.md](./langsmith-deployment/openais-bet-on-a-cognitive-architecture.md) |
| 2023-10-19 | [LangServe Playground and Configurability](https://www.langchain.com/blog/langserve-playground-and-configurability) | [langserve-playground-and-configurability.md](./langsmith-deployment/langserve-playground-and-configurability.md) |
| 2023-10-12 | [Introducing LangServe, the best way to deploy your LangChains](https://www.langchain.com/blog/introducing-langserve) | [introducing-langserve.md](./langsmith-deployment/introducing-langserve.md) |


## LangSmith Observability & Evals

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-05-05 | [agent-observability-needs-feedback-to-power-learning](https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning) | [agent-observability-needs-feedback-to-power-learning.md](./langsmith-observability/agent-observability-needs-feedback-to-power-learning.md) |
| 2026-04-16 | [Reusable Evaluators and Evaluator Templates in LangSmith](https://www.langchain.com/blog/reusable-langsmith-evaluator-templates) | [reusable-langsmith-evaluator-templates.md](./langsmith-observability/reusable-langsmith-evaluator-templates.md) |
| 2026-04-09 | [Human judgment in the agent improvement loop](https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop) | [human-judgment-in-the-agent-improvement-loop.md](./langsmith-observability/human-judgment-in-the-agent-improvement-loop.md) |
| 2026-03-31 | [The Agent Improvement Loop Starts with a Trace](https://www.langchain.com/blog/traces-start-agent-improvement-loop) | [traces-start-agent-improvement-loop.md](./langsmith-observability/traces-start-agent-improvement-loop.md) |
| 2026-03-27 | [Agent Evaluation Readiness Checklist](https://www.langchain.com/blog/agent-evaluation-readiness-checklist) | [agent-evaluation-readiness-checklist.md](./langsmith-observability/agent-evaluation-readiness-checklist.md) |
| 2026-03-26 | [How we build evals for Deep Agents](https://www.langchain.com/blog/how-we-build-evals-for-deep-agents) | [how-we-build-evals-for-deep-agents.md](./langsmith-observability/how-we-build-evals-for-deep-agents.md) |
| 2026-03-05 | [Evaluating Skills](https://www.langchain.com/blog/evaluating-skills) | [evaluating-skills.md](./langsmith-observability/evaluating-skills.md) |
| 2026-02-26 | [Agent Observability: How to Monitor and Evaluate LLM Agents in Production](https://www.langchain.com/blog/production-monitoring) | [production-monitoring.md](./langsmith-observability/production-monitoring.md) |
| 2026-02-13 | [On Agent Frameworks and Agent Observability](https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability) | [on-agent-frameworks-and-agent-observability.md](./langsmith-observability/on-agent-frameworks-and-agent-observability.md) |
| 2026-01-28 | [How to Debug &amp; Evaluate AI Agents with Observability — LangChain Guide](https://www.langchain.com/blog/agent-observability-powers-agent-evaluation) | [agent-observability-powers-agent-evaluation.md](./langsmith-observability/agent-observability-powers-agent-evaluation.md) |
| 2026-01-20 | [From Traces to Insights: Understanding Agent Behavior at Scale](https://www.langchain.com/blog/from-traces-to-insights-understanding-agent-behavior-at-scale) | [from-traces-to-insights-understanding-agent-behavior-at-scale.md](./langsmith-observability/from-traces-to-insights-understanding-agent-behavior-at-scale.md) |
| 2026-01-10 | [In software, the code documents the app. In AI, the traces do.](https://www.langchain.com/blog/in-software-the-code-documents-the-app-in-ai-the-traces-do) | [in-software-the-code-documents-the-app-in-ai-the-traces-do.md](./langsmith-observability/in-software-the-code-documents-the-app-in-ai-the-traces-do.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-12-10 | [Debugging Deep Agents with LangSmith](https://www.langchain.com/blog/debugging-deep-agents-with-langsmith) | [debugging-deep-agents-with-langsmith.md](./langsmith-observability/debugging-deep-agents-with-langsmith.md) |
| 2025-12-05 | [Evaluating Deep Agents CLI on Terminal Bench 2.0](https://www.langchain.com/blog/evaluating-deepagents-cli-on-terminal-bench-2-0) | [evaluating-deepagents-cli-on-terminal-bench-2-0.md](./langsmith-observability/evaluating-deepagents-cli-on-terminal-bench-2-0.md) |
| 2025-12-03 | [Evaluating Deep Agents: Our Learnings](https://www.langchain.com/blog/evaluating-deep-agents-our-learnings) | [evaluating-deep-agents-our-learnings.md](./langsmith-observability/evaluating-deep-agents-our-learnings.md) |
| 2025-10-23 | [Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith](https://www.langchain.com/blog/insights-agent-multiturn-evals-langsmith) | [insights-agent-multiturn-evals-langsmith.md](./langsmith-observability/insights-agent-multiturn-evals-langsmith.md) |
| 2025-06-11 | [Benchmarking Multi-Agent Architectures](https://www.langchain.com/blog/benchmarking-multi-agent-architectures) | [benchmarking-multi-agent-architectures.md](./langsmith-observability/benchmarking-multi-agent-architectures.md) |
| 2025-02-26 | [Quickly Start Evaluating LLMs With OpenEvals](https://www.langchain.com/blog/evaluating-llms-with-openevals) | [evaluating-llms-with-openevals.md](./langsmith-observability/evaluating-llms-with-openevals.md) |
| 2025-02-10 | [Benchmarking Single Agent Performance](https://www.langchain.com/blog/react-agent-benchmarking) | [react-agent-benchmarking.md](./langsmith-observability/react-agent-benchmarking.md) |
| 2025-01-22 | [Introducing Pytest and Vitest integrations for LangSmith Evaluations](https://www.langchain.com/blog/pytest-and-vitest-for-langsmith-evals) | [pytest-and-vitest-for-langsmith-evals.md](./langsmith-observability/pytest-and-vitest-for-langsmith-evals.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-14 | [Making it easier to build human-in-the-loop agents with interrupt](https://www.langchain.com/blog/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt) | [making-it-easier-to-build-human-in-the-loop-agents-with-interrupt.md](./langsmith-observability/making-it-easier-to-build-human-in-the-loop-agents-with-interrupt.md) |
| 2024-12-05 | [Easier evaluations with LangSmith SDK v0.2](https://www.langchain.com/blog/easier-evaluations-with-langsmith-sdk-v0-2) | [easier-evaluations-with-langsmith-sdk-v0-2.md](./langsmith-observability/easier-evaluations-with-langsmith-sdk-v0-2.md) |
| 2024-11-07 | [SCIPE - Systematic Chain Improvement and Problem Evaluation](https://www.langchain.com/blog/scipe-systematic-chain-improvement-and-problem-evaluation) | [scipe-systematic-chain-improvement-and-problem-evaluation.md](./langsmith-observability/scipe-systematic-chain-improvement-and-problem-evaluation.md) |
| 2024-07-31 | [Dataset schemas for fast and iterative data curation in LangSmith](https://www.langchain.com/blog/dataset-schemas) | [dataset-schemas.md](./langsmith-observability/dataset-schemas.md) |
| 2024-06-26 | [Aligning LLM-as-a-Judge with Human Preferences](https://www.langchain.com/blog/aligning-llm-as-a-judge-with-human-preferences) | [aligning-llm-as-a-judge-with-human-preferences.md](./langsmith-observability/aligning-llm-as-a-judge-with-human-preferences.md) |
| 2024-05-15 | [Pairwise Evaluations with LangSmith](https://www.langchain.com/blog/pairwise-evaluations-with-langsmith) | [pairwise-evaluations-with-langsmith.md](./langsmith-observability/pairwise-evaluations-with-langsmith.md) |
| 2024-05-02 | [How Dosu Used LangSmith to Achieve a 30% Accuracy Improvement with No Prompt Engineering](https://www.langchain.com/blog/dosu-langsmith-no-prompt-eng) | [dosu-langsmith-no-prompt-eng.md](./langsmith-observability/dosu-langsmith-no-prompt-eng.md) |
| 2024-05-01 | [Regression Testing with LangSmith](https://www.langchain.com/blog/regression-testing) | [regression-testing.md](./langsmith-observability/regression-testing.md) |
| 2024-03-20 | [Using Feedback to Improve Your Application: Self Learning GPTs](https://www.langchain.com/blog/self-learning-gpts) | [self-learning-gpts.md](./langsmith-observability/self-learning-gpts.md) |
| 2024-03-15 | [Benchmarking Query Analysis in High Cardinality Situations](https://www.langchain.com/blog/high-cardinality) | [high-cardinality.md](./langsmith-observability/high-cardinality.md) |
| 2024-03-11 | [Iterating Towards LLM Reliability with Evaluation Driven Development](https://www.langchain.com/blog/iterating-towards-llm-reliability-with-evaluation-driven-development) | [iterating-towards-llm-reliability-with-evaluation-driven-development.md](./langsmith-observability/iterating-towards-llm-reliability-with-evaluation-driven-development.md) |
| 2024-02-08 | [Human-in-the-loop with OpenGPTs and LangGraph](https://www.langchain.com/blog/human-in-the-loop-with-opengpts-and-langgraph) | [human-in-the-loop-with-opengpts-and-langgraph.md](./langsmith-observability/human-in-the-loop-with-opengpts-and-langgraph.md) |
| 2024-01-30 | [LangSmith&#x27;s Latest Feature: Grouped Monitoring Charts](https://www.langchain.com/blog/grouped-monitoring-charts) | [grouped-monitoring-charts.md](./langsmith-observability/grouped-monitoring-charts.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-12-20 | [Benchmarking Agent Tool Use](https://www.langchain.com/blog/benchmarking-agent-tool-use) | [benchmarking-agent-tool-use.md](./langsmith-observability/benchmarking-agent-tool-use.md) |
| 2023-12-13 | [Benchmarking RAG on tables](https://www.langchain.com/blog/benchmarking-rag-on-tables) | [benchmarking-rag-on-tables.md](./langsmith-observability/benchmarking-rag-on-tables.md) |
| 2023-12-05 | [Extraction Benchmarking](https://www.langchain.com/blog/extraction-benchmarking) | [extraction-benchmarking.md](./langsmith-observability/extraction-benchmarking.md) |
| 2023-11-22 | [Sharing LangSmith Benchmarks](https://www.langchain.com/blog/public-langsmith-benchmarks) | [public-langsmith-benchmarks.md](./langsmith-observability/public-langsmith-benchmarks.md) |
| 2023-11-08 | [♠️ SPADE: Automatically Digging up Evals based on Prompt Refinements](https://www.langchain.com/blog/spade-automatically-digging-up-evals-based-on-prompt-refinements) | [spade-automatically-digging-up-evals-based-on-prompt-refinements.md](./langsmith-observability/spade-automatically-digging-up-evals-based-on-prompt-refinements.md) |
| 2023-10-17 | [Test Run Comparisons](https://www.langchain.com/blog/test-run-comparisons) | [test-run-comparisons.md](./langsmith-observability/test-run-comparisons.md) |
| 2023-10-16 | [Testing Fine Tuned Open Source Models in LangSmith](https://www.langchain.com/blog/testing-fine-tuned-open-source-models-in-langsmith) | [testing-fine-tuned-open-source-models-in-langsmith.md](./langsmith-observability/testing-fine-tuned-open-source-models-in-langsmith.md) |
| 2023-09-28 | [How &quot;Correct&quot; are LLM Evaluators?](https://www.langchain.com/blog/how-correct-are-llm-evaluators) | [how-correct-are-llm-evaluators.md](./langsmith-observability/how-correct-are-llm-evaluators.md) |
| 2023-09-20 | [Peering Into the Soul of AI Decision-Making with LangSmith](https://www.langchain.com/blog/peering-into-the-soul-of-ai-decision-making-with-langsmith) | [peering-into-the-soul-of-ai-decision-making-with-langsmith.md](./langsmith-observability/peering-into-the-soul-of-ai-decision-making-with-langsmith.md) |
| 2023-08-23 | [Using LangSmith to Support Fine-tuning](https://www.langchain.com/blog/using-langsmith-to-support-fine-tuning-of-open-source-llms) | [using-langsmith-to-support-fine-tuning-of-open-source-llms.md](./langsmith-observability/using-langsmith-to-support-fine-tuning-of-open-source-llms.md) |
| 2023-08-15 | [Benchmarking Question/Answering Over CSV Data](https://www.langchain.com/blog/benchmarking-question-answering-over-csv-data) | [benchmarking-question-answering-over-csv-data.md](./langsmith-observability/benchmarking-question-answering-over-csv-data.md) |
| 2023-05-16 | [Auto-Evaluation of Anthropic 100k Context Window](https://www.langchain.com/blog/auto-evaluation-of-anthropic-100k-context-window) | [auto-evaluation-of-anthropic-100k-context-window.md](./langsmith-observability/auto-evaluation-of-anthropic-100k-context-window.md) |
| 2023-05-01 | [Auto-Evaluator Opportunities](https://www.langchain.com/blog/auto-evaluator-opportunities) | [auto-evaluator-opportunities.md](./langsmith-observability/auto-evaluator-opportunities.md) |
| 2023-04-16 | [Auto-Eval of Question-Answering Tasks](https://www.langchain.com/blog/auto-eval-of-question-answering-tasks) | [auto-eval-of-question-answering-tasks.md](./langsmith-observability/auto-eval-of-question-answering-tasks.md) |
| 2023-01-30 | [Tracing](https://www.langchain.com/blog/tracing) | [tracing.md](./langsmith-observability/tracing.md) |


## Newsletters

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-27 | [April 2026: LangChain Newsletter](https://www.langchain.com/blog/april-2026-langchain-newsletter) | [april-2026-langchain-newsletter.md](./newsletters/april-2026-langchain-newsletter.md) |
| 2026-04-01 | [March 2026: LangChain Newsletter](https://www.langchain.com/blog/march-2026-langchain-newsletter) | [march-2026-langchain-newsletter.md](./newsletters/march-2026-langchain-newsletter.md) |
| 2026-03-04 | [February 2026: LangChain Newsletter](https://www.langchain.com/blog/febraury-2026-langchain-newsletter) | [febraury-2026-langchain-newsletter.md](./newsletters/febraury-2026-langchain-newsletter.md) |
| 2026-01-30 | [January 2026: LangChain Newsletter](https://www.langchain.com/blog/january-2026-langchain-newsletter) | [january-2026-langchain-newsletter.md](./newsletters/january-2026-langchain-newsletter.md) |


## RAG & Knowledge

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-03-11 | [Autonomous context compression](https://www.langchain.com/blog/autonomous-context-compression) | [autonomous-context-compression.md](./rag-knowledge/autonomous-context-compression.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-11-05 | [Why We Rebuilt LangChain’s Chatbot and What We Learned](https://www.langchain.com/blog/rebuilding-chat-langchain) | [rebuilding-chat-langchain.md](./rag-knowledge/rebuilding-chat-langchain.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-04-25 | [Graph-based metadata filtering for improving vector search in RAG applications](https://www.langchain.com/blog/graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications) | [graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications.md](./rag-knowledge/graph-based-metadata-filtering-for-improving-vector-search-in-rag-applications.md) |
| 2024-03-15 | [Enhancing RAG-based application accuracy by constructing and leveraging knowledge graphs](https://www.langchain.com/blog/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs) | [enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs.md](./rag-knowledge/enhancing-rag-based-applications-accuracy-by-constructing-and-leveraging-knowledge-graphs.md) |
| 2024-03-13 | [Multi Needle in a Haystack](https://www.langchain.com/blog/multi-needle-in-a-haystack) | [multi-needle-in-a-haystack.md](./rag-knowledge/multi-needle-in-a-haystack.md) |
| 2024-01-16 | [Build and deploy a RAG app with Pinecone Serverless](https://www.langchain.com/blog/pinecone-serverless) | [pinecone-serverless.md](./rag-knowledge/pinecone-serverless.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-12-06 | [Multi-modal RAG on slide decks](https://www.langchain.com/blog/multi-modal-rag-template) | [multi-modal-rag-template.md](./rag-knowledge/multi-modal-rag-template.md) |
| 2023-11-30 | [Deconstructing RAG](https://www.langchain.com/blog/deconstructing-rag) | [deconstructing-rag.md](./rag-knowledge/deconstructing-rag.md) |
| 2023-11-17 | [Applying OpenAI&#x27;s RAG Strategies](https://www.langchain.com/blog/applying-openai-rag) | [applying-openai-rag.md](./rag-knowledge/applying-openai-rag.md) |
| 2023-11-14 | [Query Construction](https://www.langchain.com/blog/query-construction) | [query-construction.md](./rag-knowledge/query-construction.md) |
| 2023-11-09 | [Parallel Function Calling for Structured Data Extraction](https://www.langchain.com/blog/parallel-function-calling-extraction) | [parallel-function-calling-extraction.md](./rag-knowledge/parallel-function-calling-extraction.md) |
| 2023-11-07 | [Implementing advanced RAG strategies with Neo4j](https://www.langchain.com/blog/implementing-advanced-retrieval-rag-strategies-with-neo4j) | [implementing-advanced-retrieval-rag-strategies-with-neo4j.md](./rag-knowledge/implementing-advanced-retrieval-rag-strategies-with-neo4j.md) |
| 2023-11-02 | [Embeddings Drive the Quality of RAG: Voyage AI in Chat LangChain](https://www.langchain.com/blog/voyage-embeddings-in-langchain-and-chat-langchain) | [voyage-embeddings-in-langchain-and-chat-langchain.md](./rag-knowledge/voyage-embeddings-in-langchain-and-chat-langchain.md) |
| 2023-10-20 | [Multi-Vector Retriever for RAG on tables, text, and images](https://www.langchain.com/blog/semi-structured-multi-modal-rag) | [semi-structured-multi-modal-rag.md](./rag-knowledge/semi-structured-multi-modal-rag.md) |
| 2023-10-19 | [Constructing knowledge graphs from text using OpenAI functions: Leveraging knowledge graphs to power LangChain Applications](https://www.langchain.com/blog/constructing-knowledge-graphs-from-text-using-openai-functions) | [constructing-knowledge-graphs-from-text-using-openai-functions.md](./rag-knowledge/constructing-knowledge-graphs-from-text-using-openai-functions.md) |
| 2023-10-18 | [A Chunk by Any Other Name: Structured Text Splitting and Metadata-enhanced RAG](https://www.langchain.com/blog/a-chunk-by-any-other-name) | [a-chunk-by-any-other-name.md](./rag-knowledge/a-chunk-by-any-other-name.md) |
| 2023-10-04 | [Building (and Breaking) WebLangChain](https://www.langchain.com/blog/weblangchain) | [weblangchain.md](./rag-knowledge/weblangchain.md) |
| 2023-10-04 | [Using a Knowledge Graph to implement a DevOps RAG application](https://www.langchain.com/blog/using-a-knowledge-graph-to-implement-a-devops-rag-application) | [using-a-knowledge-graph-to-implement-a-devops-rag-application.md](./rag-knowledge/using-a-knowledge-graph-to-implement-a-devops-rag-application.md) |
| 2023-09-27 | [Building Chat LangChain](https://www.langchain.com/blog/building-chat-langchain-2) | [building-chat-langchain-2.md](./rag-knowledge/building-chat-langchain-2.md) |
| 2023-09-24 | [Timescale Vector x LangChain: Making PostgreSQL A Better Vector Database for AI Applications](https://www.langchain.com/blog/timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications) | [timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications.md](./rag-knowledge/timescale-vector-x-langchain-making-postgresql-a-better-vector-database-for-ai-applications.md) |
| 2023-09-07 | [Neo4j x LangChain: Deep dive into the new Vector index implementation](https://www.langchain.com/blog/neo4j-x-langchain-new-vector-index) | [neo4j-x-langchain-new-vector-index.md](./rag-knowledge/neo4j-x-langchain-new-vector-index.md) |
| 2023-09-06 | [Syncing data sources to vector stores](https://www.langchain.com/blog/syncing-data-sources-to-vector-stores) | [syncing-data-sources-to-vector-stores.md](./rag-knowledge/syncing-data-sources-to-vector-stores.md) |
| 2023-08-29 | [Xata x LangChain: new vector store and memory store integrations](https://www.langchain.com/blog/xata-x-langchain-new-vector-store-and-memory-store-integrations) | [xata-x-langchain-new-vector-store-and-memory-store-integrations.md](./rag-knowledge/xata-x-langchain-new-vector-store-and-memory-store-integrations.md) |
| 2023-08-29 | [Boost Your Bottom Line and Performance: OpenAI’s 3.5T Fine-Tuning with LangSmith](https://www.langchain.com/blog/chatopensource-x-langchain-the-future-is-fine-tuning-2) | [chatopensource-x-langchain-the-future-is-fine-tuning-2.md](./rag-knowledge/chatopensource-x-langchain-the-future-is-fine-tuning-2.md) |
| 2023-08-25 | [Chat Loaders: Fine-tune a ChatModel in your Voice](https://www.langchain.com/blog/chat-loaders-finetune-a-chatmodel-in-your-voice) | [chat-loaders-finetune-a-chatmodel-in-your-voice.md](./rag-knowledge/chat-loaders-finetune-a-chatmodel-in-your-voice.md) |
| 2023-08-24 | [Evaluating RAG pipelines with Ragas + LangSmith](https://www.langchain.com/blog/evaluating-rag-pipelines-with-ragas-langsmith) | [evaluating-rag-pipelines-with-ragas-langsmith.md](./rag-knowledge/evaluating-rag-pipelines-with-ragas-langsmith.md) |
| 2023-08-23 | [Epsilla x LangChain: Retrieval Augmented Generation (RAG) in LLM-Powered Question-Answering Pipelines](https://www.langchain.com/blog/espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines) | [espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines.md](./rag-knowledge/espilla-x-langchain-retrieval-augmented-generation-rag-in-llm-powered-question-answering-pipelines.md) |
| 2023-08-16 | [Qdrant x LangChain: Endgame Performance](https://www.langchain.com/blog/qdrant-x-langchain-endgame-performance) | [qdrant-x-langchain-endgame-performance.md](./rag-knowledge/qdrant-x-langchain-endgame-performance.md) |
| 2023-08-08 | [Chat with your data using OpenAI, Pinecone, Airbyte and Langchain](https://www.langchain.com/blog/chat-with-your-data-using-openai-pinecone-airbyte-langchain) | [chat-with-your-data-using-openai-pinecone-airbyte-langchain.md](./rag-knowledge/chat-with-your-data-using-openai-pinecone-airbyte-langchain.md) |
| 2023-08-03 | [Conversational Retrieval Agents](https://www.langchain.com/blog/conversational-retrieval-agents) | [conversational-retrieval-agents.md](./rag-knowledge/conversational-retrieval-agents.md) |
| 2023-07-12 | [Neon x LangChain: HNSW in Postgres with pg_embedding](https://www.langchain.com/blog/neon-x-langchainhnsw-in-postgres-with-pg-embedding) | [neon-x-langchainhnsw-in-postgres-with-pg-embedding.md](./rag-knowledge/neon-x-langchainhnsw-in-postgres-with-pg-embedding.md) |
| 2023-04-21 | [Improving Document Retrieval with Contextual Compression](https://www.langchain.com/blog/improving-document-retrieval-with-contextual-compression) | [improving-document-retrieval-with-contextual-compression.md](./rag-knowledge/improving-document-retrieval-with-contextual-compression.md) |
| 2023-04-08 | [LangChain x Supabase](https://www.langchain.com/blog/langchain-x-supabase) | [langchain-x-supabase.md](./rag-knowledge/langchain-x-supabase.md) |
| 2023-03-24 | [Retrieval](https://www.langchain.com/blog/retrieval) | [retrieval.md](./rag-knowledge/retrieval.md) |
| 2023-03-06 | [Chat Models](https://www.langchain.com/blog/chat-models) | [chat-models.md](./rag-knowledge/chat-models.md) |
| 2023-02-13 | [Chat-Your-Data Submissions](https://www.langchain.com/blog/chat-your-data-submissions) | [chat-your-data-submissions.md](./rag-knowledge/chat-your-data-submissions.md) |
| 2023-02-13 | [LangChain + Chroma](https://www.langchain.com/blog/langchain-chroma) | [langchain-chroma.md](./rag-knowledge/langchain-chroma.md) |
| 2023-02-06 | [Chat-Your-Data Challenge](https://www.langchain.com/blog/chat-your-data-challenge) | [chat-your-data-challenge.md](./rag-knowledge/chat-your-data-challenge.md) |


## Tools & Integrations

### 2026

| Date | Title | File |
| --- | --- | --- |
| 2026-04-16 | [A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense](https://www.langchain.com/blog/secure-agents-cisco-ai-defense) | [secure-agents-cisco-ai-defense.md](./tools-integrations/secure-agents-cisco-ai-defense.md) |
| 2026-04-02 | [Open Models have crossed a threshold](https://www.langchain.com/blog/open-models-have-crossed-a-threshold) | [open-models-have-crossed-a-threshold.md](./tools-integrations/open-models-have-crossed-a-threshold.md) |
| 2026-03-17 | [Open SWE: An Open-Source Framework for Internal Coding Agents](https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents) | [open-swe-an-open-source-framework-for-internal-coding-agents.md](./tools-integrations/open-swe-an-open-source-framework-for-internal-coding-agents.md) |
| 2026-03-16 | [LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA](https://www.langchain.com/blog/nvidia-enterprise) | [nvidia-enterprise.md](./tools-integrations/nvidia-enterprise.md) |
| 2026-03-10 | [How Coding Agents Are Reshaping Engineering, Product and Design](https://www.langchain.com/blog/how-coding-agents-are-reshaping-engineering-product-and-design) | [how-coding-agents-are-reshaping-engineering-product-and-design.md](./tools-integrations/how-coding-agents-are-reshaping-engineering-product-and-design.md) |
| 2026-01-14 | [Choosing the Right Multi-Agent Architecture](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture) | [choosing-the-right-multi-agent-architecture.md](./tools-integrations/choosing-the-right-multi-agent-architecture.md) |

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-07-01 | [How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith](https://www.langchain.com/blog/exa) | [exa.md](./tools-integrations/exa.md) |
| 2025-06-24 | [How Captide agents running on LangGraph Platform compress investment research from days to seconds](https://www.langchain.com/blog/captide) | [captide.md](./tools-integrations/captide.md) |
| 2025-06-12 | [The Hidden Metric That Determines AI Product Success](https://www.langchain.com/blog/the-hidden-metric-that-determines-ai-product-success) | [the-hidden-metric-that-determines-ai-product-success.md](./tools-integrations/the-hidden-metric-that-determines-ai-product-success.md) |
| 2025-05-04 | [How Outshift by Cisco achieved a 10x productivity boost with their Agentic AI Platform Engineer](https://www.langchain.com/blog/cisco-outshift) | [cisco-outshift.md](./tools-integrations/cisco-outshift.md) |
| 2025-03-27 | [Introducing End-to-End OpenTelemetry Support in LangSmith](https://www.langchain.com/blog/end-to-end-opentelemetry-langsmith) | [end-to-end-opentelemetry-langsmith.md](./tools-integrations/end-to-end-opentelemetry-langsmith.md) |
| 2025-03-08 | [MCP: Flash in the Pan or Future Standard?](https://www.langchain.com/blog/mcp-fad-or-fixture) | [mcp-fad-or-fixture.md](./tools-integrations/mcp-fad-or-fixture.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-12-09 | [Introducing OpenTelemetry support for LangSmith](https://www.langchain.com/blog/opentelemetry-langsmith) | [opentelemetry-langsmith.md](./tools-integrations/opentelemetry-langsmith.md) |
| 2024-11-13 | [Promptim: an experimental library for prompt optimization](https://www.langchain.com/blog/promptim) | [promptim.md](./tools-integrations/promptim.md) |
| 2024-11-11 | [Composio’s SWE agent advances open-source on SweBench with a 48.6% score using LangGraph and LangSmith](https://www.langchain.com/blog/composio-swekit) | [composio-swekit.md](./tools-integrations/composio-swekit.md) |
| 2024-10-26 | [Communication is all you need](https://www.langchain.com/blog/communication-is-all-you-need) | [communication-is-all-you-need.md](./tools-integrations/communication-is-all-you-need.md) |
| 2024-09-12 | [Building a Data Visualization Agent with LangGraph Cloud](https://www.langchain.com/blog/data-viz-agent) | [data-viz-agent.md](./tools-integrations/data-viz-agent.md) |
| 2024-08-14 | [LangChain Integration Docs: Find information faster with revamped pages &amp; API references](https://www.langchain.com/blog/langchain-integration-docs-revamped) | [langchain-integration-docs-revamped.md](./tools-integrations/langchain-integration-docs-revamped.md) |
| 2024-07-24 | [Few-shot prompting to improve tool-calling performance](https://www.langchain.com/blog/few-shot-prompting-to-improve-tool-calling-performance) | [few-shot-prompting-to-improve-tool-calling-performance.md](./tools-integrations/few-shot-prompting-to-improve-tool-calling-performance.md) |
| 2024-05-16 | [Integrating LangChain with Azure Container Apps dynamic sessions](https://www.langchain.com/blog/integrating-langchain-with-azure-container-apps-dynamic-sessions) | [integrating-langchain-with-azure-container-apps-dynamic-sessions.md](./tools-integrations/integrating-langchain-with-azure-container-apps-dynamic-sessions.md) |
| 2024-04-22 | [Empowering Development with FlowTestAI: Bridging APIs and LLMs for Enhanced Testing and Privacy](https://www.langchain.com/blog/empowering-development-with-flowtestai) | [empowering-development-with-flowtestai.md](./tools-integrations/empowering-development-with-flowtestai.md) |
| 2024-04-11 | [Tool Calling with LangChain](https://www.langchain.com/blog/tool-calling-with-langchain) | [tool-calling-with-langchain.md](./tools-integrations/tool-calling-with-langchain.md) |
| 2024-03-28 | [LangFriend: a Journal with Long-Term Memory](https://www.langchain.com/blog/langfriend) | [langfriend.md](./tools-integrations/langfriend.md) |
| 2024-03-26 | [Open Source Extraction Service](https://www.langchain.com/blog/open-source-extraction-service) | [open-source-extraction-service.md](./tools-integrations/open-source-extraction-service.md) |
| 2024-03-18 | [LangChain Integrates NVIDIA NIM for GPU-optimized LLM Inference in RAG](https://www.langchain.com/blog/nvidia-nim) | [nvidia-nim.md](./tools-integrations/nvidia-nim.md) |
| 2024-02-20 | [JSON agents with Ollama &amp; LangChain](https://www.langchain.com/blog/json-based-agents-with-ollama-and-langchain) | [json-based-agents-with-ollama-and-langchain.md](./tools-integrations/json-based-agents-with-ollama-and-langchain.md) |
| 2024-02-19 | [Supercharging If-Statements With Prompt Classification Using Ollama and LangChain](https://www.langchain.com/blog/supercharging-if-statements-with-prompt-classification-using-ollama-and-langchain) | [supercharging-if-statements-with-prompt-classification-using-ollama-and-langchain.md](./tools-integrations/supercharging-if-statements-with-prompt-classification-using-ollama-and-langchain.md) |
| 2024-02-14 | [How Dataherald Makes Natural Language to SQL Easy](https://www.langchain.com/blog/dataherald) | [dataherald.md](./tools-integrations/dataherald.md) |
| 2024-02-12 | [BCG X Releases AgentKit, a Full-Stack Starter Kit for Building Constrained Agents](https://www.langchain.com/blog/bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents) | [bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents.md](./tools-integrations/bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents.md) |
| 2024-02-05 | [Generating Usable Text with AI](https://www.langchain.com/blog/generating-usable-text-with-ai) | [generating-usable-text-with-ai.md](./tools-integrations/generating-usable-text-with-ai.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-12-19 | [How Rubric Labs and Graphite leveraged LLMs to create personalized videos at scale](https://www.langchain.com/blog/rubric-labs-graphite-personalized-video-at-scale) | [rubric-labs-graphite-personalized-video-at-scale.md](./tools-integrations/rubric-labs-graphite-personalized-video-at-scale.md) |
| 2023-10-18 | [The Prompt Landscape](https://www.langchain.com/blog/the-prompt-landscape) | [the-prompt-landscape.md](./tools-integrations/the-prompt-landscape.md) |
| 2023-10-18 | [You.com x LangChain](https://www.langchain.com/blog/you-com-x-langchain) | [you-com-x-langchain.md](./tools-integrations/you-com-x-langchain.md) |
| 2023-10-10 | [Fine-tuning ChatGPT: Surpassing GPT-4 Summarization Performance–A 63% Cost Reduction and 11x Speed Enhancement using Synthetic Data and LangSmith](https://www.langchain.com/blog/fine-tuning-chatgpt-surpassing-gpt-4-summarization) | [fine-tuning-chatgpt-surpassing-gpt-4-summarization.md](./tools-integrations/fine-tuning-chatgpt-surpassing-gpt-4-summarization.md) |
| 2023-10-03 | [Kay x Cybersyn x LangChain: Embedding SEC Filings for RAG](https://www.langchain.com/blog/kay-x-cybersyn-x-langchain) | [kay-x-cybersyn-x-langchain.md](./tools-integrations/kay-x-cybersyn-x-langchain.md) |
| 2023-10-02 | [Bringing Free OSS Models to the Playground with Fireworks AI](https://www.langchain.com/blog/bringing-free-oss-models-to-the-playground-with-fireworks-ai) | [bringing-free-oss-models-to-the-playground-with-fireworks-ai.md](./tools-integrations/bringing-free-oss-models-to-the-playground-with-fireworks-ai.md) |
| 2023-09-26 | [Fine-tune your LLMs with LangSmith and Lilac](https://www.langchain.com/blog/fine-tune-your-llms-with-langsmith-and-lilac) | [fine-tune-your-llms-with-langsmith-and-lilac.md](./tools-integrations/fine-tune-your-llms-with-langsmith-and-lilac.md) |
| 2023-09-21 | [Eden AI x LangChain: Harnessing LLMs, Embeddings, and AI](https://www.langchain.com/blog/eden-ai-x-langchain) | [eden-ai-x-langchain.md](./tools-integrations/eden-ai-x-langchain.md) |
| 2023-09-19 | [TED AI Hackathon Kickoff (and projects we’d love to see)](https://www.langchain.com/blog/ted-ai-hackathon-kickoff) | [ted-ai-hackathon-kickoff.md](./tools-integrations/ted-ai-hackathon-kickoff.md) |
| 2023-09-12 | [How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel](https://www.langchain.com/blog/how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel) | [how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel.md](./tools-integrations/how-to-safely-query-enterprise-data-with-langchain-agents-sql-openai-gretel.md) |
| 2023-09-12 | [OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change](https://www.langchain.com/blog/opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change) | [opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change.md](./tools-integrations/opaqueprompts-x-langchain-enhance-the-privacy-of-your-langchain-application-with-just-one-code-change.md) |
| 2023-09-06 | [Announcing our Student Hacker in Residence Program, Fall &#x27;23 Semester](https://www.langchain.com/blog/student-hacker-in-residence-fall-23) | [student-hacker-in-residence-fall-23.md](./tools-integrations/student-hacker-in-residence-fall-23.md) |
| 2023-09-05 | [Streamlit LLM Hackathon Kickoff (and projects we’d love to see)](https://www.langchain.com/blog/streamlit-llm-hackathon-kickoff-and-projects-wed-love-to-see-2) | [streamlit-llm-hackathon-kickoff-and-projects-wed-love-to-see-2.md](./tools-integrations/streamlit-llm-hackathon-kickoff-and-projects-wed-love-to-see-2.md) |
| 2023-08-30 | [TitanTakeoff x LangChain: Supercharged Local Inference for LLMs](https://www.langchain.com/blog/titantakeoff-x-langchain-supercharged-local-inference-for-llms-2) | [titantakeoff-x-langchain-supercharged-local-inference-for-llms-2.md](./tools-integrations/titantakeoff-x-langchain-supercharged-local-inference-for-llms-2.md) |
| 2023-08-24 | [Summarizing and Querying Data from Excel Spreadsheets Using eparse and a Large Language Model](https://www.langchain.com/blog/summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model) | [summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model.md](./tools-integrations/summarizing-and-querying-data-from-excel-spreadsheets-using-eparse-and-a-large-language-model.md) |
| 2023-08-23 | [Tavrn x LangChain: Integrating Noah: ChatGPT with Google Drive and Notion data](https://www.langchain.com/blog/integrating-chatgpt-with-google-drive-and-notion-data) | [integrating-chatgpt-with-google-drive-and-notion-data.md](./tools-integrations/integrating-chatgpt-with-google-drive-and-notion-data.md) |
| 2023-08-23 | [Cube x LangChain: Building AI experiences with LLMs and the semantic layer](https://www.langchain.com/blog/cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer) | [cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer.md](./tools-integrations/cube-x-langchain-building-ai-experiences-with-llms-and-the-semantic-layer.md) |
| 2023-08-22 | [Introducing Airbyte sources within LangChain](https://www.langchain.com/blog/introducing-airbyte-sources-within-langchain) | [introducing-airbyte-sources-within-langchain.md](./tools-integrations/introducing-airbyte-sources-within-langchain.md) |
| 2023-08-21 | [LangChain 🤝 DemoGPT: New Era for Gen-AI Applications](https://www.langchain.com/blog/langchain-demogpt-new-era-for-gen-ai-applications) | [langchain-demogpt-new-era-for-gen-ai-applications.md](./tools-integrations/langchain-demogpt-new-era-for-gen-ai-applications.md) |
| 2023-08-17 | [Zep x LangSmith: Foundations of LLM app development with LangChain.js and Zep](https://www.langchain.com/blog/zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep) | [zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep.md](./tools-integrations/zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-and-zep.md) |
| 2023-08-15 | [MultiOn x LangChain: Powering Next-Gen Web Automation &amp; Navigation with AI](https://www.langchain.com/blog/multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai) | [multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai.md](./tools-integrations/multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai.md) |
| 2023-08-14 | [Label Studio x LangChain: From Foundation Models to Fine-Tuned Applications Using Label Studio](https://www.langchain.com/blog/from-foundation-models-to-fine-tuned-applications-using-label-studio) | [from-foundation-models-to-fine-tuned-applications-using-label-studio.md](./tools-integrations/from-foundation-models-to-fine-tuned-applications-using-label-studio.md) |
| 2023-08-13 | [GPT Researcher x LangChain](https://www.langchain.com/blog/gpt-researcher-x-langchain) | [gpt-researcher-x-langchain.md](./tools-integrations/gpt-researcher-x-langchain.md) |
| 2023-08-10 | [Villagers x LangSmith: Simulating multi-agent social networks with LangSmith](https://www.langchain.com/blog/villagers-x-langsmith-simulating-multi-agent-social-networks) | [villagers-x-langsmith-simulating-multi-agent-social-networks.md](./tools-integrations/villagers-x-langsmith-simulating-multi-agent-social-networks.md) |
| 2023-08-09 | [NeumAI x LangChain: Efficiently maintaining context in sync for AI applications](https://www.langchain.com/blog/neum-x-langchain) | [neum-x-langchain.md](./tools-integrations/neum-x-langchain.md) |
| 2023-08-08 | [Making Data Ingestion Production Ready: a LangChain-Powered Airbyte Destination](https://www.langchain.com/blog/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination) | [making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination.md](./tools-integrations/making-data-ingestion-production-ready-a-langchain-powered-airbyte-destination.md) |
| 2023-07-26 | [Zep x LangChain: Diagnosing and Fixing Slow Chatbots](https://www.langchain.com/blog/zep-x-langchain-slow-chatbots) | [zep-x-langchain-slow-chatbots.md](./tools-integrations/zep-x-langchain-slow-chatbots.md) |
| 2023-07-24 | [Lepton x LangChain: Earning Sage, How to Transform AI into a Savvy CFO](https://www.langchain.com/blog/lepton-x-langchain-earning-sage) | [lepton-x-langchain-earning-sage.md](./tools-integrations/lepton-x-langchain-earning-sage.md) |
| 2023-07-24 | [RealChar x LangSmith: Using Open Source tools to create an AI companion](https://www.langchain.com/blog/realchar-x-langsmith-ai-companions) | [realchar-x-langsmith-ai-companions.md](./tools-integrations/realchar-x-langsmith-ai-companions.md) |
| 2023-07-16 | [Code Interpreter API](https://www.langchain.com/blog/code-interpreter-api) | [code-interpreter-api.md](./tools-integrations/code-interpreter-api.md) |
| 2023-07-13 | [Analyzing User Interactions with LLMs to Improve our Documentation](https://www.langchain.com/blog/llms-to-improve-documentation) | [llms-to-improve-documentation.md](./tools-integrations/llms-to-improve-documentation.md) |
| 2023-07-11 | [LangChain 🤝 Streamlit](https://www.langchain.com/blog/langchain-streamlit) | [langchain-streamlit.md](./tools-integrations/langchain-streamlit.md) |
| 2023-06-26 | [🎉 Prem Challenge🎉](https://www.langchain.com/blog/prem-challenge-with-langchain) | [prem-challenge-with-langchain.md](./tools-integrations/prem-challenge-with-langchain.md) |
| 2023-06-22 | [LangChain &lt;&gt; MongoDB Atlas](https://www.langchain.com/blog/langchain-x-mongodb-atlas) | [langchain-x-mongodb-atlas.md](./tools-integrations/langchain-x-mongodb-atlas.md) |
| 2023-06-19 | [Data-Driven Characters](https://www.langchain.com/blog/data-driven-characters) | [data-driven-characters.md](./tools-integrations/data-driven-characters.md) |
| 2023-06-05 | [GPTeam: A multi-agent simulation](https://www.langchain.com/blog/gpteam-a-multi-agent-simulation) | [gpteam-a-multi-agent-simulation.md](./tools-integrations/gpteam-a-multi-agent-simulation.md) |
| 2023-05-22 | [Going Beyond Chatbots: How to Make GPT-4 Output Structured Data Using LangChain](https://www.langchain.com/blog/going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain) | [going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain.md](./tools-integrations/going-beyond-chatbots-how-to-make-gpt-4-output-structured-data-using-langchain.md) |
| 2023-05-15 | [Rebuff: Detecting Prompt Injection Attacks](https://www.langchain.com/blog/rebuff) | [rebuff.md](./tools-integrations/rebuff.md) |
| 2023-05-09 | [Feature Stores and LLMs](https://www.langchain.com/blog/feature-stores-and-llms) | [feature-stores-and-llms.md](./tools-integrations/feature-stores-and-llms.md) |
| 2023-05-01 | [Callbacks Improvements](https://www.langchain.com/blog/callbacks) | [callbacks.md](./tools-integrations/callbacks.md) |
| 2023-04-24 | [Gradio &amp; LLM Agents](https://www.langchain.com/blog/gradio-llm-agents) | [gradio-llm-agents.md](./tools-integrations/gradio-llm-agents.md) |
| 2023-04-22 | [RecAlign - The smart content filter for social media feed](https://www.langchain.com/blog/recalign-the-smart-content-filter-for-social-media-feed) | [recalign-the-smart-content-filter-for-social-media-feed.md](./tools-integrations/recalign-the-smart-content-filter-for-social-media-feed.md) |
| 2023-04-19 | [Autonomous Agents &amp; Agent Simulations](https://www.langchain.com/blog/agents-round) | [agents-round.md](./tools-integrations/agents-round.md) |
| 2023-04-11 | [Announcing LangChainJS Support for Multiple JS Environments](https://www.langchain.com/blog/js-envs) | [js-envs.md](./tools-integrations/js-envs.md) |
| 2023-03-16 | [LangChain + Zapier Natural Language Actions (NLA)](https://www.langchain.com/blog/langchain-zapier-nla) | [langchain-zapier-nla.md](./tools-integrations/langchain-zapier-nla.md) |
| 2023-03-13 | [LLMs and SQL](https://www.langchain.com/blog/llms-and-sql) | [llms-and-sql.md](./tools-integrations/llms-and-sql.md) |
| 2023-03-08 | [Origin Web Browser](https://www.langchain.com/blog/origin-web-browser) | [origin-web-browser.md](./tools-integrations/origin-web-browser.md) |
| 2023-03-08 | [Prompt Selectors](https://www.langchain.com/blog/prompt-selectors) | [prompt-selectors.md](./tools-integrations/prompt-selectors.md) |
| 2023-02-15 | [Streaming Support in LangChain](https://www.langchain.com/blog/streaming-support-in-langchain) | [streaming-support-in-langchain.md](./tools-integrations/streaming-support-in-langchain.md) |
| 2023-02-08 | [Async Support in LangChain](https://www.langchain.com/blog/async-api) | [async-api.md](./tools-integrations/async-api.md) |
| 2023-02-06 | [LangChain &lt;&gt; Unstructured](https://www.langchain.com/blog/langchain-unstructured) | [langchain-unstructured.md](./tools-integrations/langchain-unstructured.md) |
| 2023-02-01 | [GPTwitter](https://www.langchain.com/blog/gptwitter) | [gptwitter.md](./tools-integrations/gptwitter.md) |
| 2023-01-24 | [LangChainHub](https://www.langchain.com/blog/langchainhub) | [langchainhub.md](./tools-integrations/langchainhub.md) |


## Tutorials & Guides

### 2025

| Date | Title | File |
| --- | --- | --- |
| 2025-09-11 | [How to turn Claude Code into a domain specific coding agent](https://www.langchain.com/blog/how-to-turn-claude-code-into-a-domain-specific-coding-agent) | [how-to-turn-claude-code-into-a-domain-specific-coding-agent.md](./tutorials-guides/how-to-turn-claude-code-into-a-domain-specific-coding-agent.md) |
| 2025-06-16 | [How and when to build multi-agent systems](https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems) | [how-and-when-to-build-multi-agent-systems.md](./tutorials-guides/how-and-when-to-build-multi-agent-systems.md) |
| 2025-04-20 | [How to think about agent frameworks](https://www.langchain.com/blog/how-to-think-about-agent-frameworks) | [how-to-think-about-agent-frameworks.md](./tutorials-guides/how-to-think-about-agent-frameworks.md) |
| 2025-03-15 | [AI Agent Latency 101: How do I speed up my AI agent?](https://www.langchain.com/blog/how-do-i-speed-up-my-agent) | [how-do-i-speed-up-my-agent.md](./tutorials-guides/how-do-i-speed-up-my-agent.md) |
| 2025-01-28 | [Exploring Prompt Optimization](https://www.langchain.com/blog/exploring-prompt-optimization) | [exploring-prompt-optimization.md](./tutorials-guides/exploring-prompt-optimization.md) |
| 2025-01-06 | [Structured Report Generation Blueprint with NVIDIA AI](https://www.langchain.com/blog/structured-report-generation-blueprint) | [structured-report-generation-blueprint.md](./tutorials-guides/structured-report-generation-blueprint.md) |

### 2024

| Date | Title | File |
| --- | --- | --- |
| 2024-07-20 | [Planning for Agents](https://www.langchain.com/blog/planning-for-agents) | [planning-for-agents.md](./tutorials-guides/planning-for-agents.md) |
| 2024-07-18 | [Improving core tool interfaces and docs in LangChain](https://www.langchain.com/blog/improving-core-tool-interfaces-and-docs-in-langchain) | [improving-core-tool-interfaces-and-docs-in-langchain.md](./tutorials-guides/improving-core-tool-interfaces-and-docs-in-langchain.md) |
| 2024-07-12 | [[Week of 7/8] LangChain Release Notes](https://www.langchain.com/blog/week-of-7-8-langchain-release-notes) | [week-of-7-8-langchain-release-notes.md](./tutorials-guides/week-of-7-8-langchain-release-notes.md) |
| 2024-05-09 | [How to Build the Ultimate AI Automation with Multi-Agent Collaboration](https://www.langchain.com/blog/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration) | [how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration.md](./tutorials-guides/how-to-build-the-ultimate-ai-automation-with-multi-agent-collaboration.md) |
| 2024-03-06 | [Use Case Accelerant: Extraction Service](https://www.langchain.com/blog/use-case-accelerant-extraction-service) | [use-case-accelerant-extraction-service.md](./tutorials-guides/use-case-accelerant-extraction-service.md) |
| 2024-02-21 | [Reflection Agents](https://www.langchain.com/blog/reflection-agents) | [reflection-agents.md](./tutorials-guides/reflection-agents.md) |
| 2024-02-16 | [Winning in AI means mastering the new stack](https://www.langchain.com/blog/winning-in-ai-means-mastering-the-new-stack) | [winning-in-ai-means-mastering-the-new-stack.md](./tutorials-guides/winning-in-ai-means-mastering-the-new-stack.md) |
| 2024-02-13 | [Plan-and-Execute Agents](https://www.langchain.com/blog/planning-agents) | [planning-agents.md](./tutorials-guides/planning-agents.md) |
| 2024-01-26 | [Mental Health Therapy as an LLM State Machine](https://www.langchain.com/blog/mental-health-therapy-as-an-llm-state-machine) | [mental-health-therapy-as-an-llm-state-machine.md](./tutorials-guides/mental-health-therapy-as-an-llm-state-machine.md) |

### 2023

| Date | Title | File |
| --- | --- | --- |
| 2023-11-16 | [&quot;Research Assistant&quot;: Exploring UXs Besides Chat](https://www.langchain.com/blog/exploring-uxs-besides-chat-with-research-assistant) | [exploring-uxs-besides-chat-with-research-assistant.md](./tutorials-guides/exploring-uxs-besides-chat-with-research-assistant.md) |
| 2023-10-24 | [Query Transformations](https://www.langchain.com/blog/query-transformations) | [query-transformations.md](./tutorials-guides/query-transformations.md) |
| 2023-10-13 | [Building LLM-Powered Web Apps with Client-Side Technology](https://www.langchain.com/blog/building-llm-powered-web-apps-with-client-side-technology) | [building-llm-powered-web-apps-with-client-side-technology.md](./tutorials-guides/building-llm-powered-web-apps-with-client-side-technology.md) |
| 2023-10-03 | [Handling PII data in LangChain](https://www.langchain.com/blog/handling-pii-data-in-langchain) | [handling-pii-data-in-langchain.md](./tutorials-guides/handling-pii-data-in-langchain.md) |
| 2023-09-05 | [Incorporating domain specific knowledge in SQL-LLM solutions](https://www.langchain.com/blog/incorporating-domain-specific-knowledge-in-sql-llm-solutions) | [incorporating-domain-specific-knowledge-in-sql-llm-solutions.md](./tutorials-guides/incorporating-domain-specific-knowledge-in-sql-llm-solutions.md) |
| 2023-08-04 | [Yeager.ai x LangChain: Exploring GenWorlds a Framework for Coordinating AI Agents](https://www.langchain.com/blog/exploring-genworlds) | [exploring-genworlds.md](./tutorials-guides/exploring-genworlds.md) |
| 2023-08-02 | [Unifying AI endpoints with Genoss, powered by LangChain](https://www.langchain.com/blog/unifying-ai-endpoints-with-genoss) | [unifying-ai-endpoints-with-genoss.md](./tutorials-guides/unifying-ai-endpoints-with-genoss.md) |
| 2023-07-26 | [Automating Web Research](https://www.langchain.com/blog/automating-web-research) | [automating-web-research.md](./tutorials-guides/automating-web-research.md) |
| 2023-05-10 | [Plan-and-Execute Agents](https://www.langchain.com/blog/plan-and-execute-agents) | [plan-and-execute-agents.md](./tutorials-guides/plan-and-execute-agents.md) |
| 2023-05-03 | [Structured Tools](https://www.langchain.com/blog/structured-tools) | [structured-tools.md](./tutorials-guides/structured-tools.md) |
| 2023-04-28 | [Unleashing the power of AI Collaboration with Parallelized LLM Agent Actor Trees](https://www.langchain.com/blog/unleashing-the-power-of-ai-collaboration-with-parallelized-llm-agent-actor-trees) | [unleashing-the-power-of-ai-collaboration-with-parallelized-llm-agent-actor-trees.md](./tutorials-guides/unleashing-the-power-of-ai-collaboration-with-parallelized-llm-agent-actor-trees.md) |
| 2023-02-17 | [TypeScript Support](https://www.langchain.com/blog/typescript-support) | [typescript-support.md](./tutorials-guides/typescript-support.md) |
| 2023-02-06 | [Tutorial: ChatGPT Over Your Data](https://www.langchain.com/blog/tutorial-chatgpt-over-your-data) | [tutorial-chatgpt-over-your-data.md](./tutorials-guides/tutorial-chatgpt-over-your-data.md) |

---

## Stats

- **Total articles:** 409
- **Date range:** 2023-01-16 → 2026-05-08
- **Categories:** 11
