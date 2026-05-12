---
title: "How Trellix cut log parsing time from days to minutes with LangGraph Studio and LangSmith"
author: "LangChain Accounts"
date: "2025-04-22"
url: "https://www.langchain.com/blog/customers-trellix"
---

Case StudiesLangGraphLangSmith

# How Trellix cut log parsing time from days to minutes with LangGraph Studio and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 21, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8e649e3ebd9d142435_Trellix-case-study.png)[Trellix](https://www.trellix.com/?ref=blog.langchain.com) is a leading cybersecurity firm with 40,000+ customers that prevents organizations from cybersecurity attacks and threats. To address challenges faced by customers, the Trellix Professional Services Team used LangSmith and LangGraph – including the visual LangGraph Studio – to develop Sidekick, their internal application that democratizes knowledge and automates tedious processes.

## **Problem: Customer request backlog and log parsing**

Trellix faced significant challenges with a growing backlog of requests for cybersecurity integrations and log parsing. Each request often required a developer to spend 2 to 3 days deciphering logs, coding integrations, and managing customer communications. This lengthy process frustrated customers and led to delays, as support tickets would bounce back and forth between customers and engineers.

To improve customer experience, Trellix decided to build Sidekick, an agentic platform to automate tasks for engineering teams at Trellix, including parsing and script writing. Specifically, they created a structured approach to intake and parse syslog data. Sidekick can automatically generate parsers for unknown log formats, **reducing the time required for manual parsing from days to minutes.** Additionally, they built agents that can speed up the development of plugins and integrations for their SaaS products. Traditionally, this required an engineer to read through 3rd-party API documentation and generate boilerplate code for each new plugin. Handing off this work to agents meant plugins, traditionally being written during the course of multiple days, could now be written during the better part of an afternoon. This quicker turn around time enabled engineers to make a dent in the integration backlog and increased customer satisfaction.

## **LangGraph’s advantages as a library**

[LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.com) provided the low-level tools and enhanced abstraction techniques needed for the Trellix AI engineering team to make the required customizations for their use cases. Specifically,  map-reduce style graphs using the Send API and subgraph calling are used throughout the Sidekick Agents. These features encouraged modularity and abstraction. The Trellix team started by making several smaller subgraphs, many of which relied on the Send API and other lower-level LangGraph techniques to work efficiently and at scale. Once multiple subgraphs could perform their individual roles successfully, larger graphs were made to call the original graphs as modules.

The Trellix team noted the ease of use; it was not that LangGraph had fundamentally reimagined how to develop agents. Instead, LangGraph offered several out-of-the-box features that made their lives as developers easier. Rather than spending their time figuring out the best way to create agents in code, their time was spent tweaking, refining, and combining a small assembly of easily-built agents.

LangGraph’s human-in-the-loop capabilities also provided reassurance that engineers could step in to approve or rewind the agent’s actions as needed. Having the ability to pause execution during development testing or restart a certain step with slightly different input without waiting for a whole new run led to efficiency gains. This was a big deal to the engineering team who has stressed that waiting for model responses to test code can become quite tedious.

## **Using Studio to visualize agent workflows for business stakeholders**

Not only did the open source libraries offer advantages, but LangChain tools were particularly useful. [LangGraph Studio](http://ncepts/langgraph_studio/?ref=blog.langchain.com) played a crucial role in the development of Sidekick by providing a framework to visualize and optimize the workflows involved in log parsing and integration tasks. The engineering team used LangGraph Studio to map out the manual processes and transition them into an agentic workflow.

The benefits of LangGraph Studio did not stop with development. Agent visualization was especially helpful for presenting the **thought process and reasoning** behind AI models to both technical and non-technical stakeholders, such as executives and business leaders at Trellix. The engineering team behind Sidekick found that getting buy-in and inter-team understanding drastically improved once LangGraph Studio came into use. It became a great way to show that agents are not a “black box” but are instead carefully engineered programs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8f649e3ebd9d142486_AD_4nXc1emegRr01gg2VIuyPoTomYYy6J9BtuJ25NUNfDshgH1iB829YN4e07dX01grZX-YSFRfqn9UeHSIK_1k9zCk39FEe0mbMnhl4wZUkg8TjWMn0Af3OFvygzpDSjYILA-nLfsRt.png)Trellix&#x27;s LangGraph Studio workflow

## **Monitoring agent performance over time with LangSmith **

To make data-driven decisions and to assess agent performance, Trellix used [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) for experimentation and to action upon performance metrics. The team was able to first design different architectures of their agent with LangGraph, then test multiple architectures of their Sidekick agents in LangSmith in order to see what performed best.

Using datasets and experiments in LangSmith was especially powerful, as the Trellix team could quickly compare performance across app versions. In particular, they monitored key metrics such as recursion rate (i.e., how often the agent has to restart or go back to a previous step) and the “must include” rate (i.e., how often the agent retrieves helpful additional documents). Having this data and seeing improvements grounded in data helped Trellix build confidence before shipping to production.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab8f649e3ebd9d14246e_AD_4nXcFwvtAeLGKcfAWOCvzf0ExNNlukGNrWrbI1YuPC7bM4mHdlUa0ngjK_0ieF3gB_eAimj3D2grOXOHCc8PPqHwTyEWZHgFJgh0H3lSBBZY-cCVhXhUwsGMy_eYVkMzKdqgjUbYb.png)Trellix&#x27;s Experiments view in LangSmith

In addition to their use of experiments and datasets, the engineers at Trellix found the traces to be especially useful for debugging both when in production and during development. The intuitive structuring of trace data into inputs and outputs of each node made debugging significantly easier than drudging through AWS logs. This led to quicker development and bug fixes which increased satisfaction from internal users.

## **Impact &amp; what’s next **

With Sidekick, Trellix has amplified time savings for both engineers on the team and customers. They have:

- **Reduced log parsing time from days to minutes**, drastically improving engineering efficiency.
- **Accelerated customer request resolution**, reducing backlog and improving time-to-value (TTV).
- **Improved AI agent performance** by testing multiple architectures and tracking key metrics in LangSmith.
- **Boosted stakeholder confidence** by providing clear, visual explanations of AI reasoning to non-technical leaders.

Looking ahead, Trellix plans to expand the capabilities of Sidekick to external partners, further democratizing access to AI-driven solutions in cybersecurity. The positive impact of LangSmith and LangGraph has set the stage for continued innovation in Trellix&#x27;s service delivery, with goals to extend automated parsing and cloud connectors to all customers in the next quarter.

## **Conclusion**

Trellix has successfully implemented generative AI to address operational challenges in the cybersecurity realm, including servicing customer needs. By using LangSmith, LangGraph, and LangGraph Studio to develop Sidekick, Trellix has not only improved internal efficiencies but also enhanced customer satisfaction – paving the way for future advancements in AI-driven cybersecurity solutions.

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