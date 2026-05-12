---
title: "How ServiceNow uses LangSmith to get visibility into its customer success agents"
author: "LangChain Accounts"
date: "2025-11-17"
url: "https://www.langchain.com/blog/customers-servicenow"
---

Case StudiesLangSmithObservability &amp; Evals

# How ServiceNow uses LangSmith to get visibility into its customer success agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 17, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa3ce691fa7cd1fb06a2_6--1-.png)**Authors: ***Ganesh Srinivasan (ServiceNow), Linda Ye (LangChain), and Jake Broekhuizen (LangChain)*

ServiceNow is a leading digital workflow platform that helps enterprises transform service management across IT, customer service, and other departments. To improve their internal sales and customer success operations, ServiceNow&#x27;s AI team is using LangSmith and LangGraph to develop an intelligent multi-agent system that orchestrates the entire customer journey— from lead identification through post-sales adoption and expansion.

## **Tackling agent fragmentation **

At ServiceNow, agents were deployed across multiple parts of the platform without a single source of truth or unified orchestration layer. This fragmentation made it difficult to coordinate complex workflows that spanned the entire customer lifecycle.

To transform the sales and customer success operations, ServiceNow decided to build a comprehensive multi-agent system that could handle everything from lead qualification, closing deals through post-sales adoption, renewal, and customer advocacy. This ambitious project required both a robust orchestration framework and deep observability into agent behavior. ServiceNow needed a comprehensive framework to evaluate tool completion, accuracy, and path optimization, along with granular step-by-step tracing for agent debugging.

## **A multi-agent system for customer success workflows**

ServiceNow is developing an intelligent agent system that covers both pre-sales and post-sales workflows. In this case study, we’ll cover the pre and post-sales journey, which includes multiple critical stages:

- **Lead qualification: **Identify right leads and assist with email and meeting preparations
- **Opportunity discovery: **To identify cross-sell / up-sell opportunity
- **Economic Buyer Identification: **Identify the champion economic buyer
- **Onboarding and implementation**: Helping customers deploy ServiceNow platform applications
- **Adoption tracking**: Monitoring which licensed applications customers are actually using
- **Usage and value realization**: Ensuring customers extract real value from the platform
- **Renewal and expansion**: Identifying opportunities for contract renewals or additional licenses
- **Customer satisfaction and advocacy**: Tracking CSAT scores and developing customer champions

At each stage, specialized agents determine what actions an Account Executive (AE), seller, or Customer Success Manager (CSM) should take to meet customer requirements. For example, in the adoption stage, agents track application usage and proactively identify opportunities. If a customer isn&#x27;t realizing expected value, the system pushes the CSM to suggest additional applications that could increase ROI, automatically drafts personalized emails with relevant information, and schedules meetings between the CSM and customer.

The architecture uses a supervisor agent for orchestration, with multiple specialized subagents handling specific tasks. Different triggers activate the appropriate agents based on customer signals and lifecycle stage, enabling intelligent workflow automation across the customer journey.

## **Complex agent orchestration with LangGraph**

LangGraph provided the low-level tools and abstraction techniques ServiceNow needed for sophisticated multi-agent coordination. The ServiceNow team extensively used map-reduce style graphs with the Send API and subgraph calling throughout their system. These features enabled a modular approach: the team first built several smaller subgraphs using LangGraph&#x27;s lower-level techniques, then composed larger graphs that call the original graphs as modules.

The human-in-the-loop capabilities proved particularly valuable during development. Engineers can pause execution for testing, approve or rewind agent actions, and restart specific steps with different inputs without waiting for complete re-runs. This dramatically reduced development friction— especially important given the latency of waiting for model responses during testing.

ServiceNow has integrated their knowledge graph and Model Context Protocol (MCP) with LangGraph to create a comprehensive technology stack for agent orchestration across their platform.

## **LangSmith tracing: The standout feature for agent development**

LangSmith offers detailed tracing capabilities by providing the input, output, context used, latency, token counts at every step of agent orchestration and helps users to improve the agents performance. The intuitive structuring of trace data into inputs and outputs for each node makes debugging significantly easier than parsing through logs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa3de691fa7cd1fb06ce_data-src-image-540c2e86-95ce-46db-9d90-664b5b9c5238.png)*Lead qualification system: Drafting emails (note: this trace above does not contain real data)*

ServiceNow uses LangSmith&#x27;s tracing capabilities to:

- **Debug agent behavior step-by-step**: Understanding exactly how agents make decisions and where issues occur
- **Observe input/output at every stage**: Seeing the context, latency, and token generation for each step in the agent workflow
- **Build comprehensive datasets**: Creating golden datasets from successful agent runs to prevent regression

## **Rigorous evaluation strategy with custom metrics**

ServiceNow implemented a sophisticated evaluation framework in LangSmith tailored to their multi-agent system. Rather than one-size-fits-all metrics, they define custom scorers based on each agent&#x27;s specific task. Furthermore, they leverage LLM-as-a-judge evaluators to judge the agent responses.

For example, an agent that generates automated emails is evaluated on accuracy and content relevance. RAG-specific agents use chunk relevancy and groundedness as primary measures. Each metric has different thresholds to evaluate agent output. The LangSmith UI provides input, output and LLM generated score along with latency and token counts. The UI also helped ServiceNow to see the scores across different experiments.

The evaluation workflow includes:

- **Automated golden dataset creation**: When prompts meet score thresholds for specific agentic tasks, they&#x27;re automatically added to the golden dataset
- **Human feedback integration**: Leveraging LangSmith&#x27;s flexibility to collect human feedback and compare prompt versions
- **Regression prevention**: Using datasets to ensure new updates don&#x27;t degrade performance on previously successful scenarios
- **Multiple comparison modes**: Comparing prompts across different versions to identify and leverage the best prompting strategies

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa3de691fa7cd1fb06e5_data-src-image-86315380-bdad-417f-8727-c97197f3b220.png)*Lifecycle from traces to evaluation for an agent *

## **Testing and production roadmap**

ServiceNow is currently in the testing phase with QA engineers evaluating agent performance. They&#x27;re using this controlled environment as the ground source for building their datasets and evaluation framework. ServiceNow will continuously collect real user data and continue using LangSmith to monitor live agent performance. When production runs pass their thresholds, those prompts will automatically become part of the golden dataset for ongoing quality assurance. As a next step, ServiceNow will use the multi-turn evaluation, which was recently launched as a new feature in LangSmith, to evaluate the agent performance across an end-to-end user interaction. We will use the context of the entire thread for the evaluator instead of single conversation.

## **Conclusion**

ServiceNow is successfully addressing the challenges of agent orchestration and observability using LangChain&#x27;s platform. By leveraging LangGraph for multi-agent coordination and LangSmith for granular visibility into agent behavior, ServiceNow has built the foundation for intelligent customer success operations that span the entire customer journey.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)