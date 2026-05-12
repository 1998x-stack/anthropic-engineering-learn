---
title: "How Cleric’s AI SRE leveled up with continuous learning through LangSmith"
author: "LangChain Accounts"
date: "2024-12-03"
url: "https://www.langchain.com/blog/customers-cleric"
---

Case StudiesLangSmith

# How Cleric’s AI SRE leveled up with continuous learning through LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 2, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3807bc92c96efbbd2b_Cleric-case-study.png)Cleric is an AI agent designed to help engineering teams debug production issues, focusing on the complex, time consuming investigations that often drain engineering productivity.

When an alert fires, Cleric automatically begins investigating using existing observability tools and infrastructure. Like a human engineer, Cleric examines multiple systems simultaneously - checking database metrics, network traffic, application logs, and system resources through read-only access to production systems. This parallel investigation approach helps quickly identify complex issues, like cascading failures across microservices.

Cleric communicates with teams through Slack, sharing its findings and asking for guidance when needed. There&#x27;s no new tooling to learn – Cleric works with existing observability stacks, accessing logs, metrics, and traces just like a human engineer would.

## **Conducting concurrent investigations of production issues in LangSmith**

Production issues present unique learning opportunities that can&#x27;t be reproduced later. Unlike code generation, production environments are stateful and dynamic. Once an issue is resolved, that exact system state is gone, along with the opportunity to learn from it.

The Cleric team needed to test different investigation approaches simultaneously. For instance, one investigation path might prioritize checking database connection pools and query patterns, while another focuses first on network traffic and system resources. This setup creates a complex matrix of concurrent investigations, as Cleric examines multiple systems using different investigation strategies.

This approach introduced a new challenge. How could the Cleric team monitor and compare the performance of different investigation strategies running simultaneously? And how could they determine which investigation approaches would work best for different types of issues?

LangSmith helped to address this problem by providing clear visibility into these parallel investigations and experiments. With LangSmith, the Cleric system can now:

- Compare different investigation strategies side-by-side
- Track investigation paths across all systems
- Aggregate performance metrics for different investigation approaches
- Tie user feedback directly to specific investigation strategies
- Perform direct comparisons of different approaches handling the same incident

LangSmith&#x27;s tracing capabilities enabled the Cleric team to analyze investigation patterns across thousands of concurrent traces, measuring which approaches consistently lead to faster resolutions. This data-driven validation is crucial for building reliable autonomous systems, as relying on an approach that worked once isn’t enough to ensure it will be generalizable.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3907bc92c96efbbd31_AD_4nXc7bXzy6SJAIQbH_W_YQusa9K5IlM8wQ2g_uzSxkkJ9p6YbHBHQqGh-vZOEz_nLIkwz9iVDof-zjXfvwT60J0efkZIqtiCqov8hMi11F54FRPJf9Dm8mA3eK6YEQ_14rXmq0yLJVQ.png)

## **Tracking feedback &amp; performance metrics to generalize insights across deployments**

Cleric learns continuously from interactions within each customer environment. When an engineering team provides feedback on an investigation - whether positive or negative - this creates an opportunity to improve future investigations. While learning within a single team or company is valuable, Cleric  also recognized the potential to generalize successful investigation strategies across all of our deployments.

The challenge is determining which learnings are specific to a team or company, and which represent broader patterns that could help all users. For example, a solution that works in one environment might depend on specific internal tools or processes that don&#x27;t exist elsewhere.

Before generalizing any learnings, Cleric employs strict privacy controls and data anonymization. All customer specific details, proprietary information, and identifying data are stripped before any patterns are analyzed or shared.

Cleric uses LangSmith to manage this continuous learning process:

- When Cleric completes an investigation, engineers provide feedback through their normal interactions with Cleric (Slack, ticketing systems, etc.)
- This feedback is captured through LangSmith&#x27;s feedback API and tied directly to the investigation trace. Cleric stores both the specific details of the investigation and the key patterns that led to its resolution.
- The system analyzes these patterns to create generalized memories that strip away environment specific details while preserving the core problem-solving approach.
- These generalized memories are then made available selectively during new investigations across all deployments. LangSmith helps track when and how these memories are used, and whether they improve investigation outcomes.
- By comparing performance metrics across different teams, companies, and industries, Cleric can determine the appropriate scope for each learning. Some memories might only be useful within a specific team, while others provide value across all customer deployments.

LangSmith&#x27;s tracing and metrics capabilities allow the Cleric team to measure the impact of these shared learnings. The system can compare investigation success rates, resolution times, and other key metrics before and after introducing new memories. This data-driven approach helps validate which learnings truly generalize across environments and which should remain local to specific customers.

This system allows Cleric to maintain separate knowledge spaces - customer specific context for unique environments and procedures, alongside a growing library of generalized problem solving patterns that benefit all users.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3907bc92c96efbbd35_AD_4nXfBeaYkak1lGtBhqwAHPmGQYj0uZ5brnJsaz_Obuosvni4zdh_47a-3xvzhtZzJu8RKq8-4pS7OTJQjE9xJuH1wAIctxlBhlz1uyA-TRzloZ-mGmXVM8bLuICMbrZgd79Yffoi6GQ.png)**Knowledge Hierarchy:** How Cleric Organizes Operational Learning

## **The path to autonomous,  self-healing systems**

Production systems are becoming more autonomous. The future of engineering is building products, not operating them. Every incident Cleric resolves advances this shift, systematically moving operations from human engineers to AI systems, letting teams focus on strategic work and product development.

Cleric is building this future systematically, expanding autonomous capabilities while maintaining the safety and control that production systems demand. Each investigation helps Cleric learn and improve, moving their customers toward truly self-healing infrastructure. To see how Cleric can help your team today, [reach out](https://cleric.io/?ref=blog.langchain.com).

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