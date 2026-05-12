---
title: "How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x"
author: "LangChain Accounts"
date: "2024-06-19"
url: "https://www.langchain.com/blog/customers-factory"
---

Case StudiesLangSmithObservability &amp; Evals

# How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 19, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafc6a83bd2fbf5700d46_Factory.ai-case-study--1--1.png)In today’s fast-paced software development, streamlined Software Development Lifecycle (SDLC) capabilities are essential. Factory is building the secure AI platform for SDLC automation. Factory’s fleet of Droids automate different stages of the SDLC, boosting engineering velocity for large organizations — and their [Code Droid](https://www.factory.ai/news/code-droid-technical-report?ref=blog.langchain.com) has achieved state-of-the-art performance in complex software development tasks. By leveraging Self-hosted [LangSmith](http://www.langchain.com/langsmith?ref=blog.langchain.com), Factory meets complex observability requirements for autonomous LLM systems while maintaining enterprise-level security and privacy.

## **Leveraging LangSmith for Secure and Reliable AI Operations**

Self-hosted LangSmith provides the necessary observability infrastructure needed to manage complex LLM workflows while ensuring data privacy and security. Factory can deploy LangSmith into environments where tight data controls prevent most LLM infrastructure from operating successfully.

One primary challenge Factory faced was ensuring robust observability in their customers&#x27; environments. Traditional methods for tracking data flow across LLM pipelines and debugging context-awareness issues were cumbersome. Additionally, Factory’s custom LLM tooling made most LLM observability tools challenging to set-up. LangSmith offered a complete solution with custom tracing via a first-party API.

Factory integrated LangSmith to export traces to AWS CloudWatch logs, which allowed the team to precisely track data flow through various stages of the LLM pipeline. By linking LangSmith events and steps with CloudWatch logs, Factory’s engineers could pinpoint their position in the agentic stage. This integration helped maintain a single source of truth for data flow in LLM from one step to the next, which is mission-critical for debugging and optimization.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafc7a83bd2fbf5700d50_AD_4nXeE4KjVcMsmiygiDPyzAkguSgnsrwSxQYVj44ldEksgCPNLNXBnafVZCIA6uarpqR3mme9NOmHaWe0SPKlM3AckUANqH-8g7uksPaWNU_zt4Dx0LE2i8MiA2tEcxvums1NSnT56_f8PIzE9uDokW06ztQnk.png)Main UI in LangSmith that Factory reviews in development.

Another challenge was debugging context-awareness issues in generated responses. Factory used LangSmith to link feedback directly to each LLM call, providing immediate insights into potential problems. This integration helped the team quickly identify and resolve issues like hallucinations without a proprietary logging system. With feedback available next to every LLM call, Factory could ensure that the AI’s outputs were contextually accurate and relevant based on real customer input.

## **Closing the Product Feedback Loop with LangSmith**

In addition to observability, Factory used LangSmith to optimize product feedback loops, focusing on prompt optimization and feedback API utilization. Traditional methods of manual prompt optimization were time-consuming and often inaccurate. LangSmith’s Feedback API streamlined the process, enabling Factory to collect and analyze feedback, then refine their prompts based on real-time data.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafc7a83bd2fbf5700d4c_AD_4nXeaZ7wx4MoP0lLjYHQxrMlC7ASQwML_ObX1gVA2oJj5O6C2E-IdwJPVQbc0trRTmrZtKshbc3Zch9XXOj10JBAbcRjK30u-9vMACje_pxsXvMyeDjOUu79T0jyqdLtPN_F20r4YbOg5E8TCeXySvd1vEuZo.png)*Factory&#x27;s feedback loop starts with the Droid posting a comment and collecting positive/negative feedback. LangSmith analyzes the data, then Factory&#x27;s engineers use custom LangChain tooling to optimize the prompt, re-prompt the LLM, and improve accuracy and reduce errors.*

Factory used the Feedback API to append feedback to various stages of their workflows. The feedback was then exported to datasets, and analyzed for patterns and areas for improvement.

By benchmarking examples and automating the optimization process, Factory increased their control over accuracy and enhanced the overall performance of their AI models. For example, with examples of comments on code with good or bad feedback, they had the LLM look at a prompt and make a claim as to why the prompt may have caused a bad example (and not a good example). This streamlined feedback collecting and processing not only improved prompt optimization but also reduced mental overhead and infrastructure requirements for analyzing feedback.

The ability to automate feedback collection and processing was particularly valuable for pipeline steps that required human feedback. With LangSmith, Factory could focus on the final stages of feedback collection, ensuring that the most critical aspects of their Droid’s performance were continually refined and optimized.

This approach led to significant improvements in accuracy and efficiency across their workflows. Compared to their previous method of manual data collection and human-driven prompt iteration, Factory was able to 2x their iteration speed. Factory also reports their average customer experienced a ~20% reduction in open-to-merge time, and a 3x reduction in code churn on code impacted by Droids in the first 90 days.

## **Looking Forward: Expanding AI Autonomy in the SDLC**

As Factory continues to innovate, their focus remains on enhancing AI capabilities across the entire SDLC. Partnering with LangChain and using LangSmith have been pivotal in this journey, providing the tools and infrastructure needed to achieve unprecedented levels of efficiency and quality in software development.

Factory’s [Droids](https://www.factory.ai/news/code-droid-technical-report?ref=blog.langchain.com) have already led to remarkable improvements in engineering operations. Clients report an average reduction in cycle time by up to 20%, with over 550,000 hours of development time saved across various organizations. These substantial time savings allow engineering teams to focus on innovative, value-added tasks, enhancing overall productivity and reducing operational costs.

The future looks bright for Factory as they continue to push the boundaries of AI in software development. With the recent public launch of their AI Droids and $15 million in Series A funding led by Sequoia Capital, Factory is poised for significant growth and innovation. The ongoing collaboration with LangChain is a cornerstone of this strategy, ensuring that Factory remains at the cutting edge of AI-driven software development.

> *“Our collaboration with LangChain has been critical to successfully deploying enterprise LLM-based systems. We are significantly more confident in our decision making and operational capabilities thanks to the observability and orchestration-layer tooling that we get from the LangChain team.” – Eno Reyes, CTO of Factory*

**About Factory**

Factory is an enterprise AI company dedicated to automating the software development lifecycle. By integrating advanced autonomous Droids, Factory helps businesses achieve faster, more reliable, and cost-effective software delivery.

For more insights and updates, visit[ Factory’s website](https://factory.ai/?ref=blog.langchain.com).

**About LangChain**

LangChain, Inc. was founded in early 2023 to help developers build context-aware reasoning applications. The company’s popular open-source framework gives developers the building blocks to create production-ready applications with LLMs. LangSmith complements this as an all-in-one SaaS platform that enables a full, end-to-end development workflow for building and monitoring LangChain and LLM-powered apps.

For more information, visit[ LangChain’s website](https://langchain.com/?ref=blog.langchain.com).

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