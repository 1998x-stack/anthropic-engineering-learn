---
title: "David Zhang from Aomni gives his view agents' reliability, debugging and orchestration"
author: "Tereza Tizkova"
date: "2023-08-23"
url: "https://e2b.dev/blog/david-zhang-from-aomni-gives-his-view-agents-reliability-debugging-and-orchestration"
category: "case-studies"
site: "e2b"
---

[**David Zhang**](https://twitter.com/dzhng) is the founder of [**Aomni**](https://www.aomni.com/) - one of not so many agents in the **business intelligence** category. We asked David about [Aomni](https://www.aomni.com/) users, the challenges he has been working on recently, and his view on the agents’ journey toward reliability.

### Intro

[Aomni](https://www.aomni.com/) is an AI agent that **crawls the web and ingests a vast amount of unstructured data**. It takes user's research goal, creates a research plan, completes it one by one, and sends user the result over email. This process takes 15-20 minutes to complete, and you can use it **3 times a day for free**.

## Users and Use Cases

The primary use of [Aomni](https://www.aomni.com/) is **sales market research and account planning**. It trains a personalized AI agent to handle account planning busywork, **saving sales reps 10+ hours every week** by researching their prospects and doing the legwork needed to help reps with outreach and relationship building, allowing reps to focus on building relationships and closing deals. Most [Aomni](https://www.aomni.com/) users are not in the AI field and are completely unaware of agent technology.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67979e80bdc3c8a8da6566a6_67979dd2cdd90fa506d8a1b9_dWawFmxvGaGc3ok1f7J0kzgY.webp)Dashboard of the Aomni Agent.** **Source: [*Aomni*](https://www.aomni.com/)

## Enterprise-level reliability

We discussed the readiness of agents for widespread adoption.

“One thing that I noticed recently is that **many builders are still not fully focusing on enterprise-level reliability**,” thinks David. “For enterprise customers, we are talking at least ~99.9% reliability. That’s what people expect and what agent developers need to aim for.”

David points out that the end users of Aomni (and many other agent-powered companies) are not in the AI field. They just see the product as any other software and put their **high-reliability standards **on it.

“There is a **tradeoff between generality versus reliability of the agent technology**. As a proxy, we can say that more general agent projects get less reliable. Take some of the popular [open-source agents](https://github.com/e2b-dev/awesome-ai-agents#open_hands-open-source-projects) as examples. You sure can ask a very multi-purpose agent to plan your wedding or to code for you. But it's going to **cost a lot of tokens** and these agents are not known as the perfectly reliable ones.” Usage - e.g. how expensive the agent gets - is another important variable to include in this tradeoff.

David predicts that new agents coming to the market in the next 1-2 years will be** very specific in certain niches** and that’s why he focuses on **narrowing down the focus of **[**Aomni**](https://www.aomni.com/).

“I **limit the number of tools** that [Aomni](https://www.aomni.com/) uses,” David adds, “and the number of decisions the agent needs to make to reach the final result.”

## Solving agents’ challenges

We asked David about [SDKs and tools](https://github.com/e2b-dev/awesome-sdks-for-ai-agents) he has been using for overcoming challenges, such as debugging, monitoring, and orchestration.

On the left of the image below, we can see all the agent runs, both successful and unsuccessful. On the right, there are all different steps that the agent took in a certain run, including reasons for failures that have happened.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67979e80bdc3c8a8da6566a3_67979ded106b56d8b6b7570f_npWRrj15i7UcYkwmDGjDvH6A8Yc.webp)Runs and steps of the Aomni Agent.  Source: [*Aomni*](https://www.aomni.com/)

However, David points out the **limitations of **[**Inngest**](https://www.inngest.com/)**.** “It doesn't let you get in the middle of the process and **retry the agent from a certain step**. Such tasks are very agents-specific.”

David’s take on the agents' debugging is that he is noticing a lot of agent developers **trying to reinvent the wheel with new frameworks and SDKs**. Instead, they should build on top of existing technology.

“However, there is still a space for innovation, for example for having one **platform for monitoring token usage and measuring prompt effectiveness**.”

David enhances the necessity of **time-travel debugging**, e.g., resuming the execution of an agent in a certain step.

“It is a pretty common concept in SW engineering, so for me, it is a matter of time before someone adds the agent logic on the top of one of the existing engines,” David predicts. 

## Communication with users

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67979e80bdc3c8a8da656691_67979e208cf6ddbcc644e524_yRDfcMmaGXdNOywDdGJSN3FPAVs.webp)Error message that an Aomni user sees.  Source: [*Aomni*](https://www.aomni.com/)

“**The Aomni agents are relatively reliable** and don’t fail that much, so I didn’t need anything complicated for the error messages,” says David. “I am in the middle of **adding a **[**PostHog**](https://posthog.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-Campaign-OtherEU&utm_content=pure-brand&gclid=Cj0KCQjw3JanBhCPARIsAJpXTx4sK2SHsgHRJl0MlLqpnzAY1UQnZUGYy0r7OYam-8B3bFoKgoyBCo8aAuMyEALw_wcB)** integration **for product analytics.”

In David’s opinion, agent developers need to find a good way to **collect human feedback** and sort and manage examples of agents’ use cases.

“Creating something like a repository of agents’ use cases with good examples could be very useful.” 

Try the Aomni agent [here](https://www.aomni.com/?auth=signin), and join their [Discord community](https://discord.com/invite/a367ncqEsm/?utm_source=awesome-ai-agents) to stay updated.