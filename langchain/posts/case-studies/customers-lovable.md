---
title: "How Lovable uses LangSmith to debug &amp; monitor agents in production"
author: "LangChain Accounts"
date: "2025-03-25"
url: "https://www.langchain.com/blog/customers-lovable"
---

Case StudiesLangSmith

# How Lovable uses LangSmith to debug &amp; monitor agents in production

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 25, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbadd390227306de7d639d_Screenshot-2025-03-20-at-3.48.28-PM.png)[Lovable.dev](http://loveable.dev/?ref=blog.langchain.com) is an innovative AI-powered platform that lets users build and ship a high-quality v1 of their software without writing code. It offers seamless integration with tools like GitHub and Supabase, making it easy to create and deploy applications. Users can simply chat to rapidly build websites and web apps; for instance, they can build and deploy applications with features like authentication and data storage, achieving results 20x faster than conventional coding practices.

## **Using LangSmith for agent observability **

As Lovable experienced rapid growth and user adoption, the team needed to gain visibility into their agentic interactions. With an influx of users, understanding the intricacies of how various components of their agent interacted became crucial for the Lovable team to maintain efficiency and deliver a seamless user experience.

In order to solve their bottleneck of diagnosing agent issues and iterating on features quickly, Lovable turned to LangSmith to gain comprehensive insights into its agentic chain, which was essential. One of the key enhancements to their workflow was the addition of an admin-only button to &quot;open prompt in LangSmith,&quot; which enabled team members to access detailed agent traces. This feature empowered developers to quickly identify bottlenecks and optimize workflows, significantly enhancing operational efficiency.

By combining multiple requests in LangSmith with its low-level API, Lovable could pinpoint any session in production and instantly review the sequence of actions taken during the application&#x27;s development. Monitoring charts allowed Lovable to quickly see any spikes in metrics, and then double-click into any problematic traces to find the culprit. This not only improved debugging, but facilitated a deeper understanding of how each component interacted within the overall system, allowing the Lovable team to iterate and make continuous improvements to their agent.

## **Impact &amp; what’s next**

The integration of LangSmith has led to remarkable outcomes for Lovable.

- **Enhanced debugging**: LangSmith enabled Lovable to introspect anything in the agentic chain, reducing spent diagnosing issues and speeding up resolution time.
- **Improved collaboration**: With code stored in GitHub, team members can collaborate seamlessly, fostering a culture of teamwork and shared ownership.

Looking ahead, Lovable aims to further refine its agent development process and will explore additional LangSmith features that will enhance user experience and operational efficiency.

## **Conclusion**

Lovable&#x27;s strategic use of LangSmith has been instrumental in its rapid growth, enabling the company to achieve the milestone of $25M ARR in just four months. The integration of LangSmith has not only streamlined workflows but also set the stage for future advancements, showcasing the transformative potential of AI in the software development landscape.

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