---
title: "MultiOn x LangChain: Powering Next-Gen Web Automation &amp; Navigation with AI"
author: "LangChain Accounts"
date: "2023-08-15"
url: "https://www.langchain.com/blog/multion-x-langchain-powering-next-gen-web-automation-navigation-with-ai"
---

Partner

# MultiOn x LangChain: Powering Next-Gen Web Automation &amp; Navigation with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 15, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1bec588d5fac7b8ed6c_5-social--5-.png)*Editor&#x27;s Note: This post was written in collaboration with *[*MultiOn*](https://www.multion.ai/?ref=blog.langchain.com)*. We&#x27;re really excited about the way they&#x27;re using Agents to* *automate and streamline online interactions. They are one of the first real world, production agent applications that we know of. Their integration with LangChain as a Toolkit makes it quick and easy to personalize and automate everyday web tasks.*

## MultiOn: Your Personal AI Agent Now on LangChain

Whether it&#x27;s searching for information, filling out forms, or navigating complex websites, daily web tasks can often be tedious and time-consuming. That&#x27;s why we&#x27;re thrilled to introduce MultiOn, a next-generation personal AI assistant designed to interact with the web, to handle these tasks on your behalf.

Operating much like the sci-fi concept of JARVIS, MultiOn leverages cutting-edge AI technology to interact with your browser to perform tasks for you in real-time, from [ordering you dinner](https://youtu.be/2pF5SNhduTc?ref=blog.langchain.com), [booking flights](https://youtu.be/Lh6c8Evo-kY?ref=blog.langchain.com), [scheduling](https://youtu.be/KgH7I7Y59G8?ref=blog.langchain.com), finding information online, [to even filling out forms](https://youtu.be/zP0Ug9BVvhk?ref=blog.langchain.com). And the best part? MultiOn is now integrated directly within LangChain as a Toolkit, making it even easier to automate your everyday web tasks &amp; build custom agents and applications that can take actions on the web.

## Seamless Integration with LangChain

With MultiOn directly integrated into LangChain, the power of Autonomous Web AI Agents is now at the fingertips of all users.

The integration unlocks numerous advantages. It provides LangChain users with an AI-powered tool that can automate a variety of everyday web tasks, from information retrieval to interaction with web services on their behalf. This integration not only enhances the functionality of LangChain but also takes the Action ability of agents to the next level - to now interact with any website!

Here is a glimpse of how you can use MultiOn within LangChain to interact with the website in just **3 Lines of Code 🔥:**

Import MultiOn as a LangChain Toolkit to add it to any custom Agent:

`# IMPORTS
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import MultionToolkit
import multion
multion.login() # MultiOn -&gt; Login to the MultiOn Website
# Initialize Agent
agent = initialize_agent(
    tools=MultionToolkit().get_tools(),
    llm=OpenAI(temperature=0),
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)
print(agent.run(&quot;Show Beautiful Pictures of New York&quot;))
`

Get more samples at the [MultiOn API repository](https://www.google.com/url?q=https://github.com/MULTI-ON/api&amp;sa=D&amp;source=docs&amp;ust=1692134001253806&amp;usg=AOvVaw0xFKlpwYs8u8vulVJ77IvW).

LangChain Agent Demo:

Other

- [MultiOn Scheduler App](https://github.com/MULTI-ON/api/tree/main/examples/task_scheduler?ref=blog.langchain.com): Schedule recurring tasks that run periodically, such as “wishing happy birthday to friends on fb” everyday.
- [Group Dinner reservation Agent](https://github.com/MULTI-ON/api/tree/main/examples/restaurant-bot?ref=blog.langchain.com): Add MultiOn to a sms group chat and ask it to help book a group dinner on Opentable

## **Join the MultiOn Community!**

We’re very enthusiastic about the potential for Autonomous Web AI Agents, and more broadly, exploring new ways to harness the power of AI to improve online experiences. We believe that Actions are key to building powerful AI applications, and we want to empower developers &amp; the open source community to build AI that can interact with the Web by building on top of MultiOn. Please check [our documentation](https://docs.multion.ai/?ref=blog.langchain.com),  [contribute to adding examples](https://github.com/MULTI-ON/api/tree/main/examples?ref=blog.langchain.com), and join our Discord to experience the future of web task automation!

Stay tuned for more updates on our journey, and don&#x27;t hesitate to reach us out at [info@multion.ai](mailto:info@multion.ai) if you have any questions or suggestions. We&#x27;re always looking to hear from users and improve MultiOn to best serve your needs 🚀

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)