---
title: "Villagers x LangSmith: Simulating multi-agent social networks with LangSmith"
author: "LangChain Accounts"
date: "2023-08-10"
url: "https://www.langchain.com/blog/villagers-x-langsmith-simulating-multi-agent-social-networks"
---

PartnerLangSmith

# Villagers x LangSmith: Simulating multi-agent social networks with LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 10, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9b244817b104fafff095_5-social--3-.webp)*Editor&#x27;s Note: This post was written in collaboration with Kevin Hu, Tae Hyoung Jo, John Kim, and Tejal Patwardhan from the Villagers team. Villagers came in second at a recent Anthropic hackathon. We really LOVED this project as it shows off complex prompt engineering with their multi-agent social network simulation that runs many agents in parallel. We were really excited to see how *[*LangSmith*](https://www.langchain.com/langsmith?ref=blog.langchain.com)* could help the team automate traces, quickly iterate on prompts, and efficiently debug for this complex use-case! *

We are excited to write about our experience building a proof-of-concept for [simulated multi-agent social networks](https://devpost.com/software/realistic-multi-agent-simulations?ref=blog.langchain.com) using LangSmith. Simulating language-based human interactions on social networks has shown potential across economics, politics, sociology, business, and policy applications (e.g., [[1](https://arxiv.org/pdf/2304.03442.pdf?ref=blog.langchain.com)], [[2](https://www.science.org/content/article/can-ai-chatbots-replace-human-subjects-behavioral-experiments?ref=blog.langchain.com)]). We use the example of a text-based online community (Twitter/X) with real user personas to demonstrate how LLMs can be used to create realistic multi-agent simulations.

Building a useful simulation requires mimicking what an actual user would do, ideally based on histories of past behavior. We built agents to simulate real Twitter users interacting online based on their tweet, retweet, quote tweet, comment, and like history. Each user is an agent with their own specific prompt based on their past history. We then tested the response of the community to various ad campaigns from brands, political statements from candidates, and social commentary from comedians. This served as a proof of concept for a new simulation platform to predict engagement, responses, and behavior modification for online social networks.

One of the major technical hurdles we encountered was debugging and prompt engineering given the number of agents that would be interacting at once. We were really excited by LangSmith, which allowed us to have automatic traces and to iterate effectively on prompts, helping build the foundation of the multi-agent network.

With LangSmith, we were able to significantly speed up development time and feel more confident about the quality of our prompts. We found it to be the easiest-to-use LLMops tool for a product that has a high magnitude of agents running in parallel.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

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