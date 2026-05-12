---
title: "Recap of Interrupt 2025: The AI Agent Conference by LangChain"
author: "LangChain Accounts"
date: "2025-05-15"
url: "https://www.langchain.com/blog/interrupt-2025-recap"
---

Company Announcements

# Recap of Interrupt 2025: The AI Agent Conference by LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 14, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7ec303b901d2c2598e_Interrupt_Twitter_1200x675_V1.png)That&#x27;s a wrap on Interrupt 2025! This year, 800 folks from across the globe gathered in San Francisco for LangChain&#x27;s first industry conference to hear stories of teams building agents – and we’re still riding the high! Cisco, Uber, Replit, LinkedIn, Blackrock, JPMorgan, Harvey, and more shared lessons on architectures, evals, observability, and prompting strategies – both their challenges and their wins.

The main thing we felt leaving the day was that agents are here, and we’ve never been more bullish on the future of the industry. If you weren’t with us in person, we’ll be sharing content over the next few weeks, including recordings of all the talks. Sign up [here](https://interrupt.langchain.com/?ref=blog.langchain.com#tickets) to get the content as soon as it drops!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab80c303b901d2c259a4_AD_4nXdc7tPNPFHtqc9uU_t-DQvgbsbvTOVmHSgtu2Be7YeHabumtMFtLK8vbemBQvkZRe4r4X7upRnjl8Eh7hSCikhczHI6dUAAt-G3Qf1K33lozva9oLcD5hLwx6sSgXx2E1BF4LZ6qg.png)

Keep reading for big themes of the days and product launches!

## In Case You Missed It ✨

### **Keynote Themes:**

Harrison&#x27;s opening keynote at Interrupt highlighted a few key beliefs:

- **Agent Engineering is a new discipline** – Taking inspiration from the best of software engineering, prompting, product, and machine learning, we believe you need to code, engineer your prompts for the right context, understand the business workflows to turn them into agents, and understand likelihoods and distributions similar to in ML. Being good at all four disciplines is a tall task, and in pursuit of our mission to make agents ubiquitous, we want to make everyone an 100x agent engineer – no matter what your relative strengths are to start with.
- **LLM apps will rely on many different models. **The LangChain package today is mostly about giving companies model optionality. LangChain has had 3 stable releases, and we’re laser focused on depth and breadth of integrations. Developers want the choice and flexibility that LangChain provides, and as a result, LangChain has been downloaded over 70M times in the last month – even more than the OpenAI SDK 🤯.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab80c303b901d2c259a1_AD_4nXdmDc5VNW6JKK1PIzXO95mVl6Ioba8MhYuftyACKEDSPEiOyBioWDyxMr3cY3_Rsw1Wu1ewXzGVvYHmrhRTNwQwpKBXvysfkKU8E0tM0pbpr8aahIwKsgeebV_n9e1-oLAAX6NguQ.png)
- **LangGraph is how you build reliable agents. **One of the hardest parts about building agents is getting the right context to the LLM. LangGraph, our agent orchestration framework, gives you full authorship over the cognitive architecture so you can control the workflow and information flow. This low-level control makes LangGraph unique as an agent orchestration framework.
- **AI Observability is different. **With GenAI apps, you’re dealing with dense, unstructured information – often text, audio, or image. The agent engineer needs to understand what’s happening with the application, and is a totally different user with different needs than SREs that traditional observability tools serve. If LangSmith&#x27;s aggregate trace volume reflects broader industry trends, more agents are moving into production—making the need for an [AI observability](https://www.langchain.com/articles/ai-observability?ref=blog.langchain.com) stack more critical than ever.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7fc303b901d2c2599c_AD_4nXer65AMJE8RSyhmtrGWuRO0OJN_0Oba8WOPcUxzrEB1jR9GMIgBIvMkNhwmaHhs29YJLWsoFfEQEhABIkPexIkuNW-kXZDqpLdbFKFkVCefBnTyl_z0eXdb5rqSCVA1EQpqLEpF8Q.png)

## **Launches!**

We love to ship at LangChain, and we announced a LOT.

- **LangGraph Platform is Generally Available. **[LangGraph Platform](https://www.langchain.com/langgraph-platform?ref=blog.langchain.com) is a deployment and management platform for long-running, stateful agents, and you can 1-click deploy your agent today – available with Cloud, Hybrid, and fully self-hosted deployments. See the [docs](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com) for more information or check out our [4 min walk through](https://www.youtube.com/watch?v=pfAQxBS5z88&amp;t=8s&amp;ref=blog.langchain.com).

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7fc303b901d2c25999_AD_4nXdpp5mgm6EG88uuvin4o5JEsXPmXPYQkvBUXZzpl2eqGfIS5jLK1XMickg8NdwV7VFvwx1Pmlm37g2kw3C5yQeFd37mRkLIoDbJzYyoJiLwT_M-gKU-1tq4RbS8M9UwigcjG26i.png)
- **Open Agent Platform – an open source, no code agent builder. **You can now build agents without being a developer – select MCP tools, customize prompts, select models, connect to data source, and other agents all through the UI. Powered by LangGraph Platform. Sign up [here.](https://oap.langchain.com/signin?ref=blog.langchain.com)
- **LangGraph Studio v2. **LangGraph Studio can now be run locally without a desktop app. It’s an agent IDE that lets you visualize and debug agent interactions. In v2, we&#x27;re giving you the ability to pull down traces into the studio to investigate, add examples to a dataset for evals, and directly update prompts in a UI.
- **LangGraph Pre-Builts lowers the effort for building agents. **There are common architectures that we see repeatedly used when building agents – Swarm, Supervisor, tool-calling agent – so we want to lower the burden for implementing these architectures in your app. [LangGraph pre-builts](https://langchain-ai.github.io/langgraph/agents/prebuilt/?ref=blog.langchain.com#available-libraries) lets you leverage common architectures with less config code.
- **LangSmith Observability now includes agent specific metrics.** We’ve added support for tool calling and trajectory tracking so you can see the common paths your agent is taking and spot expensive, slow, or spotty calls.
- **Open Evals and Chat Simulations**. Authoring evaluators is tedious. While some evals are very application / use case specific, some are not – and that’s good news, because we can write those for you. We now have an open source catalog of evals, useful for code, extraction, RAG, agent trajectory testing, and more. We’re also excited to release chat simulation and evals for multi-turn conversation. Check it out [here](https://github.com/langchain-ai/openevals?ref=blog.langchain.com).
- **LLM-as-Judge: alignment and calibration (in Private Preview). **[LLM-as-judge](https://www.langchain.com/articles/llm-as-a-judge?ref=blog.langchain.com) is a fantastic technique for evaluating performance when more discretion or judgement is required. However, even the judge is subject to being faulty. We’re excited to launch, in private preview, a way to bootstrap LLM-as-a-judge evaluators with human feedback scores and constantly calibrate and audit scores to make sure the judge is performing well. If you’re interested, sign up [here](https://docs.google.com/forms/d/e/1FAIpQLSebD0knAtZjuN9VKbMmHmn6QL_8uZrMEfwqMi7pfIkhKYQH5Q/viewform?ref=blog.langchain.com) for access!

We’re so excited to be building alongside you all, and aim to make this an annual event. We’ll see you the C[ommunity slack](https://www.langchain.com/join-community?ref=blog.langchain.com), at our meetups, and **we’ll see you next year at Interrupt: The AI Agent Conference by LangChain. **

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7fc303b901d2c25994_Gq7QtdkaAAAmPNb.jpeg)Nothing beats the LangChain community in-person!

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