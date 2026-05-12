---
title: "How Airtop built web-automation for AI agents powered by the LangChain ecosystem"
author: "LangChain Accounts"
date: "2024-11-26"
url: "https://www.langchain.com/blog/customers-airtop"
---

Case StudiesLangChain

# How Airtop built web-automation for AI agents powered by the LangChain ecosystem

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 26, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3ba657ab2a6d2fddf9_Airtop-case-study.png)[Airtop](https://www.airtop.ai/?ref=blog.langchain.com) is a powerful platform that empowers developers to create scalable, production-ready web automations with simplicity and precision. Airtop is at the forefront of enabling agents to interact intelligently with the web, it empowers agents to perform actions such as logging in, extracting information, filling forms, and interacting with web interfaces—all through natural language commands.

AI agents are only as functional as the data they can access. Navigating websites at scale introduces challenges like authentication and Captchas. Airtop bridges this gap by providing developers with a reliable way to control browsers via natural language APIs, eliminating the need for complex CSS selector hacks or Puppeteer scripts.

Leveraging the full LangChain ecosystem (LangChain, LangSmith, and LangGraph), Airtop has built a number of browser solutions, including:

- **Extract API**: Enables **extraction of structured information** from web pages, like lists of speakers, LinkedIn URLs, or monitoring flight prices. Also works with authenticated sites for use cases like social listening and e-commerce.
- **Act API: **Adds the** ability to take actions on websites,** such as entering search queries or interacting with UI elements in real-time.

## **Simplifying model integration with LangChain**

As Airtop set out to build its cloud-based browsers for AI agents, they needed a platform that could flexibly integrate various LLM models. [LangChain](https://www.langchain.com/langchain?ref=blog.langchain.com) quickly stood out because of its &quot;batteries-included&quot; approach. With built-in integrations for the GPT-4 series, Claude, Fireworks, and Gemini, LangChain saved Airtop countless hours of development time.

“The standardized interface LangChain provides has been a game-changer,” shared Kyle, Airtop’s AI Engineer. “We can switch between models effortlessly, which has been critical as we optimize for different use cases.”

## **Building a flexible agent architecture in LangGraph**

As Airtop looked to add more browser automations, their engineering team turned to [LangGraph](https://www.langchain.com/langgraph?ref=blog.langchain.com) to leverage its flexible architecture to build their agent system. With LangGraph, Airtop constructed individual browser automations as subgraphs. This also helped future-proof their application, as it would be easy to add in additional subgraphs as they expanded their automations — giving the team more dynamic control without needing to redesign their control flow.

As Airtop designed their agents, the team decided to start small with micro-capabilities for their agents, then building out their system with more sophisticated agents that could click on elements on the site and perform keystrokes. As their agents evolved, reliability was top-of-mind. LangGraph helped Airtop validate the accuracy of their agent steps as it took actions on a website.

## **Debugging and refining prompts in LangSmith**

While Airtop originally began using LangSmith to debug issues that would come in through customer support tickets, they quickly also discovered that [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) could speed up multiple parts of their development process.

During development, Airtop used LangSmith for prompt engineering and dynamic testing. When nebulous error messages arose from AI models like OpenAI or Claude, LangSmith’s multimodal debugging features offered clarity, allowing the team to identify whether issues stemmed from formatting problems or misplaced prompt components.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3ca657ab2a6d2fde69_AD_4nXcvDbsPbROHACbFfRsacnLzsa7g7_iyAhXDJ4HiIkdcuEzgRZehrn4WIiFRWp8fot9dfjKJ8pQhVJomAP3AUvV6Rn-bC3mEE8Vta_MtrHsQOYQYqxbj4_9g6ZuD36OKwMrqW5WIFQ.png)

In addition, it was important for the Airtop team to empower their users with reliable web automation capabilities. They utilized LangSmith’s playground to iterate on prompts and run parallel model requests, simulating real-world use cases on the fly. This sped up Airtop’s internal workflows and enhanced their ability to deliver more accurate, tailored responses to users.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae3ca657ab2a6d2fde65_AD_4nXe_qrfH5P_jpLmorKSUfIw6liKx69hk3QqwmqNeo-okU1O-CST5Pf0JBMR_m3l8Pti-eRcj9gHzwK9jTlEY1X5PsdYHl_8r0VWKYfeqxBXzaw35xMkQQs7t1lb3YBqbPX1qiaXTFg.png)

## **What’s next**

Airtop has significantly accelerated its time-to-market for AI agent-powered web automation solutions. With LangGraph’s controllable agent framework and LangSmith for testing in development, the team ensures robust agent performance.

*“Each innovation becomes a foundation for what&#x27;s next,”* said Daniel Shteremberg, Airtop’s CTO. *“With LangChain and LangSmith, we can create solutions that are adaptable, reliable, and future-proof.”*

In the future, the Airtop team aims to:

- **Build even more sophisticated agents**, with advanced LangGraph agents capable of performing multi-step, high-value tasks, such as stock market analysis or enterprise-level automation.
- **Adding additional **micro-capabilities to the platform, enabling AI agents to perform an unlimited range of actions across the web.
- **Enhanced benchmarking**: Further refining their benchmarking system to evaluate performance across a wider array of model configurations and use cases.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)