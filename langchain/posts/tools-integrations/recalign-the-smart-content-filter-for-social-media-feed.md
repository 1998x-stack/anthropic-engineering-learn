---
title: "RecAlign - The smart content filter for social media feed"
author: "LangChain Accounts"
date: "2023-04-22"
url: "https://www.langchain.com/blog/recalign-the-smart-content-filter-for-social-media-feed"
---

Partner

# RecAlign - The smart content filter for social media feed

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 22, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb236cbdf13f9a165cb06_photo-1583006977647-5d9e88d684d7.jpeg)**[Editor&#x27;s Note] This is a guest post by Tian Jin. We are highlighting this application as we think it is a novel use case. Specifically, we think recommendation systems are incredibly impactful in our everyday lives and there has not been a ton of discourse on how LLMs will impact these systems.**

We&#x27;ve all experienced the pains of using recommender systems: you signed up for Twitter to keep up with latest AI research, but a click on a funny meme will flood your timeline with similar distractions. These systems work to maximize their owner’s profit, not your welfare. Here, we outline the rationale behind our LangChain-powered solution to address this problem at its core.

**Transparency &amp; configurability.** In Brian Christian’s book the Alignment Problem, he shares an anecdote: his friend is recovering from alcohol addiction, but the recommender system knows, perhaps a little too well, about his love for alcohol and infests his feed with ads for alcohol. This episode is a vivid illustration of a recurring problem — recommender systems are skilled at catering to who we are today, but leaves little freedom for us to decide who we aspire to become. The current recommender systems lacks transparency and configurability. As a result, it is difficult for us to identify any problematic inferences that the recommender system made about our preferences, let alone modify them.

**Conflict of interest.** We cannot expect the owners of recommender systems (e.g., Twitter) to solve this lack of transparency and configurability due to a conflict of interest: system owners aim to maximize revenue, often prioritizing this objective over other desirable goals for users. This lead us to believe that to improve recommender systems, we must address the underlying conflict of interest. Users must have direct control over what they see as recommendations.

**A solution.** We propose to use large language models (LLMs) such as ChatGPT as smart content filters for social media feed, which are the outputs of recommendation systems on social media platforms. We developed an open source Chrome extension RecAlign ([https://github.com/tjingrant/RecAlign](https://github.com/tjingrant/RecAlign?ref=blog.langchain.com)) where you can specify your viewing preference in words such as *“I love reading about AI research”.* We then ask the LLM to intelligently determine whether each entry in the social media feed fits the user preference and remove all entries that violates it. We plan to develop other highly configurable augmentations such as feed re-ranking in the near future.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb237cbdf13f9a165cb0c_image.png)

A LLM-based smart content filter has the following benefits:

- **Configurable.** In the age of ChatGPT, English is the new programming language. We let users easily configure a smart content filter and see its effects immediately.
- **Transparent**. Your preference is right there, stated in words, in its entirety.
- **Flexible**. Our preference can be ephemeral. An easily configurable preference enables users to flexibly switch between different preferences.

**Join the cause**. Try RecAlign on Github at [https://github.com/recalign/RecAlign](https://github.com/recalign/RecAlign?ref=blog.langchain.com)! Consider watching/staring us for future development!

**LangChain**. LangChain plays a central role in our project. We use LangChain as an ergonomic interface to communicate with the OpenAI backend. We also rely on LangChain’s ability to easily format and parse the input to and output from LLMs. We highly recommend LangChain as it enables rapid prototyping and fast iteration on projects building with LLMs.

**Who we are**. We started as a team of two Ph.D. students in Computer Science from MIT and Harvard. This project kicked off when Xin was just 2 weeks away from his Ph.D. defense. Despite his otherwise good judgement he decides to work on this project. Thanks to LangChain, we released our first prototype with plenty of time for Xin to prepare for his defense!

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