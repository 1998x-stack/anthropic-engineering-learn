---
title: "Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith"
author: "LangChain Accounts"
date: "2025-09-11"
url: "https://www.langchain.com/blog/customers-monte-carlo"
---

Case StudiesLangGraphLangSmith

# Monte Carlo: Building Data + AI Observability Agents with LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 10, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa77bf847dfe35ef0fff_Monte-Carlo-case-study.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa78bf847dfe35ef103d_data-src-image-dd30ebdc-8c0a-4c5a-9060-1e2d8ccbf975.png)A high-level overview of Monte Carlo’s [Troubleshooting Agent](https://www.montecarlodata.com/platform/observability-agents?ref=blog.langchain.com) architecture[**Monte Carlo**](https://www.montecarlodata.com/?ref=blog.langchain.com) is a leading data + AI observability platform for enterprises, helping organizations monitor data and AI reliability issues, and trace them back to their root causes. After years of building sophisticated data monitoring and troubleshooting tools, Monte Carlo realized they had been unknowingly building the foundation for what would become their flagship AI agent— a system that can launch hundreds of sub-agents to investigate data issues and accelerate root cause analysis in a compelling, actionable way.

## **Automating data pipeline troubleshooting at enterprise scale**

Data engineers at enterprise organizations spend countless hours manually troubleshooting data alerts—investigating failed jobs, tracking down code changes, and determining whether issues require immediate resolution or can be deprioritized. This manual process forces engineers to follow single investigation paths sequentially, often missing parallel issues or taking too long to identify root causes in complex, interconnected data systems.

Monte Carlo&#x27;s customers are primarily large enterprises where data drives significant revenue. For these customers, **data that remains incorrect or unavailable can affect millions of dollars of business**. While Monte Carlo had built comprehensive troubleshooting tools, they identified an opportunity to further reduce this “data downtime:” have AI agents process and reason through hundreds of hypotheses concurrently to accelerate data + AI team’s ability to quickly spot and fix the root cause behind specific data quality incidents.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa78bf847dfe35ef1040_data-src-image-5f2b6d8f-dd02-4bc0-af6b-242a7289c03d.png)

## **Troubleshooting multi-paths with LangGraph**

Monte Carlo chose **LangGraph** as the foundation for their AI Troubleshooting Agent because their investigation process naturally mapped to a graph-based decision-making flow. When an alert is triggered, their system follows a structured troubleshooting methodology that mirrors how experienced data engineers approach problems, but at scale.

Alert → Check Code Changes → Analyze Timeline → Investigate Dependencies → Report Findings

Their LangGraph implementation starts with an alert and creates a dynamic graph of investigation nodes. Each node can spawn sub-nodes based on findings, allowing the agent to:

- Check for code changes in the past 7 days
- Narrow down to changes affecting the specific data pipeline
- Look at events occurring hours before the issue
- Investigate multiple potential root causes simultaneously

**The key advantage**: While human troubleshooters follow one path at a time, Monte Carlo&#x27;s agent can explore multiple investigation branches in parallel, checking significantly more scenarios than any individual data engineer could handle manually.

Monte Carlo&#x27;s Product Manager, Bryce Heltzel, notes that LangGraph&#x27;s value was in achieving speed to market. With a tight 4-week deadline ahead of major industry summits, the team felt confident demonstrating their agent to customers— something that wouldn&#x27;t have been possible with a custom-built solution.

## **Debugging with LangSmith**

Monte Carlo started debugging using LangSmith on day one of development. As Heltzel explains, &quot;LangSmith was a natural choice as we started building our agent in LangGraph. We wanted LangSmith to visualize what we were developing for our graph-based workflows.&quot;

As a product manager, Heltzel is very involved in the process of prompt engineering for their agents. With his deep context about customer use cases, he can now iterate quickly on prompts directly rather than going through engineering cycles.

The Monte Carlo team has been able to focus on agent logic and solving data issues for customers rather than tooling setup due to the minimal configuration LangSmith required to get up and running.

## **Monte Carlo&#x27;s architecture**

This architecture leverages several AWS services to build a scalable, secure, and decoupled system that connects Monte Carlo’s existing monolithic platform with its new AI Agent stack. We use **Amazon Bedrock** to empower our agents with the latest foundational models without the need to manage any infrastructure. The **Auth Gateway Lambda** handles authentication as a lightweight, serverless entry point, ensuring secure access without maintaining dedicated servers. The **Monolith Service **continues to serve core APIs (GraphQL and REST) and persists application data in **Amazon RDS**, a managed relational database that provides reliability and automated maintenance.

On the AI side, the **AI Agent Service** runs on **Amazon ECS Fargate**, which enables containerized microservices to scale automatically without managing underlying infrastructure. Incoming traffic to the AI Agent Service is distributed through a network load balancer (NLB), providing high-performance, low-latency routing across Fargate tasks. Together, these AWS components create a robust system where the legacy monolith and modern AI microservices interoperate efficiently, with secure authentication, resilient data storage, and elastic compute scaling.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa78bf847dfe35ef1033_monte-carlo-aws.png)

## **What&#x27;s next **

Monte Carlo is currently focused on visibility and validation — understanding where bugs occur in their traces and building robust feedback mechanisms to ensure their agent consistently delivers value to customers. They&#x27;re working on validation scenarios to measure whether the agent successfully identifies root causes in each investigation.

Looking ahead, Monte Carlo plans to expand their agent&#x27;s capabilities while maintaining the core value proposition: **enabling data teams to resolve issues faster and more comprehensively than ever before**. Their head start in building data + AI observability tools, combined with LangGraph&#x27;s flexible architecture and LangSmith&#x27;s debugging capabilities, positions them to continue leading the data + AI observability space.

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