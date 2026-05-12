---
title: "How Outshift by Cisco achieved a 10x productivity boost with their Agentic AI Platform Engineer"
author: "LangChain Accounts"
date: "2025-05-04"
url: "https://www.langchain.com/blog/cisco-outshift"
---

LangSmithObservability &amp; EvalsDeployment

# How Outshift by Cisco achieved a 10x productivity boost with their Agentic AI Platform Engineer

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 4, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf96b87e1201d9d100434c_Cisco-Outshift-case-study.webp)[Outshift](https://outshift.cisco.com/?ref=blog.langchain.com) is the incubation engine at Cisco, driving innovation in emerging technologies such as the Internet of Agents, Quantum, and next-generation infrastructure. The Platform Engineering team at Outshift offers foundational platform services to accelerate various incubation projects.

Platform Engineers manage complex, distributed cloud-native SaaS environments involving multiple heterogeneous systems. Monitoring and diagnosing issues in these systems often requires rapidly locating information across these runtime environments, telemetry systems, and documentation sites.

The small and mighty team of Platform engineers at Outshift had to context-switch and service frequent developer requests, ranging from access management to infrastructure provisioning, while developing new features to advance the platform. This led to:

- **Long wait times** for request fulfillment of simple and frequent requests, often taking days to complete.
- **Increased cognitive load** due to constant context switching between tools and workflows.
- **Operational inefficiencies**, where high-value engineering tasks were deprioritized in favor of routine platform maintenance.

# JARVIS: The AI Platform Engineer

To unlock a **10x productivity boost**, the Cisco Outshift Platform Engineering team developed [JARVIS](https://outshift.cisco.com/blog/jarvis-agentic-platform-engineering-outshift?ref=blog.langchain.com), an AI Platform Engineer designed as a **distributed Multi-Agent System (MAS)**.

JARVIS is orchestrated using [LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.com) for scalable and deterministic agent workflows and connected through the [AGNTCY Agent Connect Protocol (ACP),](https://docs.agntcy.org/pages/syntactic_sdk/connect.html?ref=blog.langchain.com) an open source standard protocol, to enable seamless agent-to-agent collaboration across systems.

### Key Features of JARVIS

**Knowledge Management**

JARVIS integrates with platform knowledge bases — including documentation, policies, Jira, and code repositories — using **Retrieval-Augmented Generation (RAG)** for unstructured data and **GraphRAG** for structured data to extract actionable insights from platform information.

**Self-Service Capabilities**

JARVIS automates many commonly requested developer tasks such as CI/CD onboarding, cloud resource provisioning, and developer sandbox environment setup — dramatically reducing turnaround times.

**Code Generation**

JARVIS simplifies Kubernetes deployments by translating natural language inputs into K8s manifests and infrastructure templates through a hybrid machine learning approach.

**Seamless UX Integration**

JARVIS surfaces agentic AI capabilities directly into familiar developer interfaces — including Jira, Backstage, Webex, and CLI — allowing developers to interact with autonomous workflows without changing their existing tools or habits.

## Agentic Blueprint Behind JARVIS

The development of JARVIS was grounded in [AGNTCY’s Four-Phase approach](https://outshift.cisco.com/blog/four-phases-for-development-of-multi-agent-apps?ref=blog.langchain.com) to building resilient multi-agent systems on the Internet of Agents, an open, interoperable platform for agent-to-agent collaboration:

**1. Discover**

We mapped critical platform workflows with specialized first- and third-party agents, laying the foundation for multi-agentic system.

**2. Compose**

Using LangGraph and the AGNTCY Agent Connect Protocol, we designed flexible, modular workflows where agents collaborate seamlessly across distributed environments.

**3. Deploy**

JARVIS was operationalized across our cloud-native ecosystem, powered by the AGNTCY Workflow Server for scalable execution and coordination.

**4. Evaluate**

Through continuous tracing, benchmarking, and feedback loops with LangSmith and agentevals, we refined agent behavior to drive consistent improvements over time.

This approach made JARVIS modular, scalable, and ready to evolve with our growing platform needs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab87b02f04cb69c45f59_AD_4nXdzbx8S7Y84Cw859AdD9J9vWRFHji0WNLcarZQOlSj_fqb1PePs6dfKRUKTuXqWlQH7-uQ5ErqJzobHJd6SIQSYR4jocSKYTFa0QrMxqLbx6BI8mzET4nTE_hURWiGAbJhV1Ql2Te6-DuJkONt_TQ.png)

‍

# How Developers Use JARVIS: Real Interfaces in Action

To maximize accessibility and adoption, JARVIS was integrated across multiple developer interfaces:

- **Jira**: Developers can assign tasks directly to the JARVIS AI Platform Engineer via Jira tickets. JARVIS autonomously executes the request and reaches out for additional input if needed.
- **Backstage**: A chat-based assistant embedded within our internal developer portal allows developers to trigger workflows and retrieve platform services seamlessly.
- **Webex**: A secure, conversational interface that delivers real-time notifications, task updates, and direct messaging interactions with JARVIS.
- **CLI**: Developers interact with JARVIS via the command line to provision sandbox applications, deploy infrastructure, and automate repetitive tasks with ease.

By meeting developers where they already work, JARVIS drives adoption while enhancing platform usability and responsiveness.

Below are some examples of JARVIS in action:

### *Assigning Jira task to JARVIS AI Engineer*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf97c04202ac24d36ab2a9_gif1-ezgif.com-resize.gif)

#### *Internal Developer Portal Chat Interface: User requesting an LLM Key using JARIVS*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf984cfa0bbcafe7bc7746_gif2-ezgif.com-resize.gif)

#### *LangGraph Studio Demonstration of multi-agent tool calling*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf989affabe444bda85131_gif3-ezgif.com-resize.gif)

## Impact of JARVIS at Outshift

JARVIS is  delivering significant productivity gains for Platform Engineering at Outshift:

- Tasks that previously took a week, such as setting up CI/CD pipelines, can now be completed **in under an hour**.
- **Provisioning resources** (e.g., S3 buckets, EC2 instances, LLM access keys) is now **instantaneous**, reducing what used to be half-day tasks to just **seconds**.
- Back-and-forth communication between developers and Platform Engineering for routine tasks has been **eliminated**, thanks to JARVIS’s ability to autonomously guide developers and retrieve needed information.
- **The organization now handles a significantly higher volume of requests** with the same team size, while also reducing burnout and improving overall efficiency.

## Key Learnings in Building JARVIS AI Platform Engineer

- [Internet of Agents](https://outshift.cisco.com/the-internet-of-agents?ref=blog.langchain.com)** **(IoA) unlocks the true potential of Multi-Agent Systems: The future of platform engineering lies in multi-agent systems, where the seamless integration of first-party and third-party distributed agents automate complex platform workflows.
- Open standards like the [AGNTCY Agent Connect Protocol (ACP)](https://docs.agntcy.org/pages/syntactic_sdk/connect.html?ref=blog.langchain.com) enable reliable agent-to-agent communication across heterogeneous systems, while frameworks like **LangGraph** provide scalable, deterministic workflow orchestration
- Structuring multi-agent systems around the [Four Phases](https://outshift.cisco.com/blog/four-phases-for-development-of-multi-agent-apps?ref=blog.langchain.com) — Discover, Compose, Deploy, and Evaluate — enables agent discoverability, promotes agent-to-agent collaboration, drives reuse, and simplifies the creation of complex, deterministic multi-agent systems.
- **Seamless UX Integration is essential for agentic workflows. **Embedding agentic capabilities directly into existing developer tools — Jira, CLI, developer portals — is critical for adoption. Combining GenAI-driven agent outputs with traditional interfaces ensures users can interact intuitively with complex workflows without changing their daily routines.
- **Continuous evaluation and benchmarking ensure reliability, **Delivering trustworthy agentic systems requires continuous tracing, monitoring, and performance evaluation. Using tracing solutions like **LangSmith** and evaluation frameworks like **agentevals** allows teams to analyze agent reasoning patterns, detect inconsistencies, and refine system performance to ensure high accuracy at scale.

**The Future of Agentic AI in Platform Engineering**

Outshift is pioneering the integration of agentic AI into platform engineering — building ecosystems where AI agents amplify human potential, enhance collaboration, and accelerate innovation. Their work with **JARVIS** is just the beginning. They&#x27;re pushing the boundaries of what’s possible with AI-powered platforms, creating new foundations for the Internet of Agents.

To see how the broader ecosystem is evolving, visit [**agntcy.org**](https://agntcy.org/?ref=blog.langchain.com) — where the Outshift team is helping to build the collaboration layer that will let AI agents work together seamlessly.

[*Explore how Outshift is driving the future of AI in platform engineering.*](https://outshift.cisco.com/blog/topic/platform-engineering?ref=blog.langchain.com)

[*Learn more about Outshift Incubations*](https://outshift.cisco.com/?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)