---
title: "How Vizient empowers healthcare providers with reliable GenAI insights using LangGraph and LangSmith"
author: "LangChain Accounts"
date: "2025-02-10"
url: "https://www.langchain.com/blog/customers-vizient"
---

Case StudiesLangGraphLangSmith

# How Vizient empowers healthcare providers with reliable GenAI insights using LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 10, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadf7765e3cf29f5f7f0d_Vizient-case-study.png)[Vizient](https://www.vizientinc.com/?ref=blog.langchain.com), a leader in healthcare performance improvement, is revolutionizing how healthcare providers access and analyze data. Today, many healthcare providers rely on disparate data sources, needing to mine for data to produce actionable insights on patient care — a long, drawn-out process. Vizient&#x27;s GenAI platform empowers systems of all sizes to query and unify siloed datasets, driving better decisions in supply chain management and clinical outcomes.

Vizient&#x27;s GenAI platform helps answer questions like: &quot;Are my ambulatory investments effective?&quot; or &quot;Are we delivering the most cost-effective care?&quot; and get immediate, data-backed answers. The goal is to improve operational efficiency and democratize data analysis for resource-limited health facilities — all while maintaining strong trust and data privacy among their members.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadf8765e3cf29f5f7f17_AD_4nXfSQSqtuBymuSfDzhKcBFHUoGm8dRW63NusL-mdxMxIs87YZNEnz9dbly0DKeJ4ti_NRW2-r6D4HSIhI3n_iQqQ0bno994dx64eMqVvCQ1Z2tGqodmdM-33q9nugAYFoMGo6Sne.png)Scorecard performance for an example hospital system in Vizient’s GenAI platform

### **Reliable AI agent workflows with LangGraph **

Before adopting LangGraph, Vizient&#x27;s multi-agent system faced several challenges. Each agent had been designed to handle a specific task, such as analyzing historical data or generating visualizations. However, coordinating them was tricky. These agents worked in silos, leading to inconsistent responses and a lack of reliability. Some underlying API workflows also involved managing hundreds of parameters per call, making it difficult to maintain and update application logic.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadf8765e3cf29f5f7f13_AD_4nXezHA0afDB6ockYjhaKItF0Tvc2-WYS0ExC-hwMhd7X4twPT8WU1Ckw3bimhvgv0ueSi5fw6TZTCcI4rs54zwW_Ib8FVJkL1_e9BHGmYwRHtCdHQz_aSuLgiVX33-o5o1cQiM6Btg.png)Vizient’s AI user interface to chat with data and generate visualizations

To coordinate their multi-agent system and ensure their platform met high-reliability standards, Vizient chose [LangGraph](https://langchain.com/langgraph?ref=blog.langchain.com) to orchestrate their agentic system. With LangGraph&#x27;s graph structure and fully descriptive primitives, Vizient&#x27;s engineering team could control and plan their workflows and represent steps that an agent should perform as tools or nodes programmatically to improve reliability. Today, their hierarchical agent structure (with worker agents reporting to a supervisor agent) has greatly streamlined the process of routing requests to the appropriate APIs.

As Vizient continues to expand and enhance its GenAI platform, LangGraph remains a cornerstone of its strategy, enabling the team to adapt and scale its system confidently.

### **LLM observability and prompt management with LangSmith**

To ensure their GenAI platform runs smoothly, Vizient needed visibility into its performance. That&#x27;s where LangSmith came in. By leveraging LangSmith&#x27;s tracing capabilities, Vizient&#x27;s engineers could quickly pinpoint and resolve issues, even during high-stakes, real-time demos. For example, they easily navigated problems caused by Azure OpenAI&#x27;s content filters and external rate-limiting errors.

LangSmith&#x27;s Prompt Hub has also proved invaluable. By isolating prompt logic, Vizient&#x27;s teams gained the flexibility to version and iterate on prompts with ease— a much more flexible approach. As the number of GenAI development teams grows, having this logic separated out will help teams handle and iterate on prompts quickly.

### **Looking Forward**

Vizient is focused on refining evaluations to ensure output consistency and trust. Key initiatives include:

- **Evaluating consistency across data domains:** Aligning generated answers with established tools like Q&amp;A scorecards.
- **Rapid data onboarding**: The team aims to quickly onboard product data to fuel its agentic system using various existing product APIs and other data sources.

Vizient is building a transformative GenAI platform that empowers healthcare providers. It enables even non-experts to ask complex questions and get actionable insights while maintaining the highest trust, security, and innovation standards. With LangGraph and LangSmith as foundational technologies, Vizient is poised to continue raising the bar for healthcare performance improvement.

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