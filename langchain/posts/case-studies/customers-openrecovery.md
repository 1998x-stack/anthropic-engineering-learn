---
title: "OpenRecovery: Transforming addiction recovery with LangGraph Platform"
author: "LangChain Accounts"
date: "2024-10-03"
url: "https://www.langchain.com/blog/customers-openrecovery"
---

Company AnnouncementsLangGraph

# OpenRecovery: Transforming addiction recovery with LangGraph Platform

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 3, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4757c432b84a7356aa_Case-study---openrecovery--2-.png)[OpenRecovery](http://openrecovery.com/?ref=blog.langchain.com) is transforming addiction recovery with their AI-powered assistant that provides personalized, 24/7 support via text and voice. Bridging the gap between costly inpatient care and generic self-help programs, it makes expert-level guidance accessible to those struggling with addiction. Using tools like LangGraph and LangSmith, and deploying the final application to LangGraph Platform, the OpenRecovery team has built a sophisticated mobile application that adapts to individual users’ recovery journey.

## **Building a multi-agent architecture with LangGraph**

OpenRecovery chose to build a multi-agent system atop LangGraph for several reasons. First, the team specialized nodes in LangGraph, each with tailored prompts for specific stages of the recovery process, such as step work or fear inventory. This ensures that each workflow is precisely tuned for its intended purpose.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4957c432b84a73572e_AD_4nXeQvWC0PW6A7tuZUE-9brGQ5ba0bU97CLBSj-cBpVlocJ4gftlVmKJyffeCWbFb78pjIqtTBWlCADVq_IP99sq18lhkeOy0B1G065ZdNR3HR9FaBd9ryago_ByceYADjrrVWbBNvY1KD49YG0YqHUgflyQ.png)Visualization of OpenRecovery’s agent architecture using LangGraph Studio (part of LangGraph Platform)

The graph structure of LangGraph supports the reuse of key components across agents, including shared-state memory, dynamic few-shot expert prompts, and search tools. This maintains consistency and efficiency across the system.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4857c432b84a73571c_AD_4nXc66KzHTO3eagXQehy0qEH6RHrSu7Kl4aOApxmB26QDvisu2AUU6NHU1usLz7POGmTlA1ncRRUQNkzxypg2u_euYbmsUj7iKSjFjRXoFEuBD2dQEQ8QrxZODAolOWrb9lDEzawivAsrVOEo8pLqpw4Jl0Zw.png)Using LangGraph Studio (part of LangGraph Platform), the OpenRecovery team can visually inspect state in the graph and agent interactions in the recovery journey

LangGraph also enables smooth context switching between different agents within the same conversation. Users can transition from general chat to specific recovery work without disruption, creating a more natural and guided experience.

Finally, the architecture is highly scalable. By leveraging LangGraph Platform, OpenRecovery ensures that their multi-agent system can scale effortlessly as new agents are added for various recovery stages and mental health support, as they expand beyond 12-step programs.

## **Deploying to LangGraph Platform for rapid iteration**

OpenRecovery opted to deploy their app on LangGraph Platform&#x27;s robust infrastructure, integrating smoothly with their mobile app frontend.  LangGraph Platform&#x27;s easy-to-use API also reduced the complexity of managing agent conversations and state, making it a great fit for OpenRecovery&#x27;s lean engineering team.

A key benefit of LangGraph Platform is its support for rapid iteration. The OpenRecovery team could quickly debug their agent interactions in the out-of-the-box visual studio, LangGraph Studio, then make updates and revisions to meet the evolving needs of their users and incorporate new recovery methodologies.

## **Human-in-the-Loop to enhance trust and accuracy**

Recognizing the sensitive nature of addiction recovery, OpenRecovery incorporated crucial human-in-the-loop features into its mobile app. First, the AI encourages deeper introspection by prompting users, much like a sponsor or therapist would. It gauges when enough information has been collected and requests human confirmation when needed for better accuracy and understanding.

Additionally, users can edit AI-generated summaries or tables, allowing them to verify the accuracy of their personal information and maintain control over their data. Users can also provide feedback to the agent in natural language, which helps build trust throughout the recovery process.

## **Collaborative development and improvement with LangSmith**

Layering on LangSmith for observability has accelerated OpenRecovery&#x27;s development process and added robustness to their testing.

First, the platform enables collaborative prompt engineering. The non-technical content team and addiction recovery experts can easily modify prompts in the LangSmith prompt hub, test them in the playground, and deploy new revisions on LangGraph Platform. The OpenRecovery team can also test changes in LangGraph Studio, using trace logs to ensure everything functions as expected.

LangSmith helps the OpenRecovery team identify failure points, such as when the language model lacks the proper empathy needed for addiction recovery support. This allows a human to come in and make the critical corrections.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf4857c432b84a735708_image4.png)

When the OpenRecovery team identifies an unsatisfactory response when debugging traces, they can quickly add new few-shot examples to the dataset in LangSmith, re-index it, and test

the same question to verify the improvement. This enforces a cycle of continuous improvement.

## **Conclusion**

By harnessing LangChain&#x27;s ecosystem, OpenRecovery has developed a dynamic, personalized AI assistant for addiction recovery. Their multi-agent architecture, combined with human-in-the-loop features, lets the team adapt to individual needs while providing the empathy essential for recovery support. As they expand their offerings and introduce new modalities like voice interactions, OpenRecovery is set to make a meaningful impact in providing expert-level addiction recovery guidance.

To try out the beta version of their new Recovery Assistant, visit their [website](https://www.openrecovery.com/?ref=blog.langchain.com) or download on your [iPhone](https://apps.apple.com/us/app/12-steps-addiction-recovery/id6446251140?ref=blog.langchain.com) or [Android](https://play.google.com/store/apps/details?id=com.twelve_steps.twelve_steps&amp;hl=en_US&amp;ref=blog.langchain.com) device – and keep an eye out for their public launch later this month.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)