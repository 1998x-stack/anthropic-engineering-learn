---
title: "Gumloop: Building AI workflow automation for enterprises"
author: "Tereza Tizkova"
date: "2024-06-03"
url: "https://e2b.dev/blog/building-ai-workflow-automation-for-enterprises"
category: "case-studies"
site: "e2b"
---

[Max Brodeur-Urbas](https://www.linkedin.com/in/max-brodeur-urbas-1a4b25172/?originalSubdomain=ca) is the founder of [Gumloop](https://www.gumloop.com/) - a platform for automating any workflow without needing to code, using movable building blocks. Gumloop has customers from banks and big corporations to individuals running their whole businesses on the platform. What are the secrets behind their success?

We talked about:

- How they started as an AutoGPT wrapper
- Why Max thinks AI products would sometimes be better off with less AI
- Views on security, generative UI, future of agents, and AI code execution with [E2B](/)
- Why they rebranded AgentHub to Gumloop.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638477_6797b599a3f13d7cbcd4e577_ZLlmiiWGpPFJk2f03v5nvIKlEU8.avif)

## From AutoGPT wrapper to a successful company

**Tell me about the beginnings of Gumloop. When and how did you start?**

It all started last year when [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) came out in March 2023. At that time, I was using ChatGPT daily and already understood its limitations. AutoGPT convinced me, at least for a few days, that agents were going to be something crazy, so we started building on top of the AutoGPT GitHub repository as a side project.
**So Gumloop started as a wrapper around AutoGPT… Among all the agentic experiments at that time, how did you get your first users?**

Spending time on the [AutoGPT Discord server](https://discord.com/invite/autogpt), we noticed thousands of people were joining the server each day, but most of these were nontechnical. They didn’t even know what GitHub was, or how to clone a repo or install dependencies, but they wanted to use AutoGPT.

So we just took the most recent version of AutoGPT, hosted it in the cloud, and made a simple GUI for it in a browser. People were writing to the Support channel with problems like “What command do I use to run this repo”, so we just pasted a link to Gumloop (at that time AgentHub) as an answer and people often checked that.**‍**
**How did the first version of the product look?**

We shipped the first version in approximately 48 hours. It was my first time using React. This is how the first version looked like on day one:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a63846e_6797b5e5721ce5e2686c2de2_dgNnkcYcllhtax6wYw9ShSWas.avif)

This all happened within a few weeks of the launch of the AutoGPT GitHub repo.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638471_6797b5fa5c5e8ccf8c9d0c97_78LyqSHERBuLbFFS5e9yMHmMs.avif)
**At that time your company was called AgentHub and you just recently rebranded to Gumloop. Where did the original name come from?**

And the domain for AgentHub was cheap.

## Building an app with reliable AI agents

**What happened after you launched the first version?**

I was getting dozens of messages on Discord. People were complaining about the agents. Especially non-technical people didn’t understand that I wasn’t the person building AutoGPT itself, but just the UI. And at that time, AutoGPT was failing in many tasks, so people blamed me for that. They wanted me to debug their agents constantly.
**Did you consider building on alternatives to AutoGPT?**

I was watching the AI agents community and quickly moved on from the super autonomous agents and didn’t even try other alternatives. I remember [BabyAGI](https://github.com/yoheinakajima/babyagi) was one of the other popular projects at the time but we never experimented with it.
**How did you overcome this stage and move towards an enterprise-grade product?**

It started with one important realization. I noticed people demanded simple tasks like “Scrape this website and analyze it.” or “Get information from this website and summarize it.” There was a desperate need from non-technical people for AI to do something useful, even if their tasks often weren’t that sophisticated.

These automations could very feasibly be built with a few scripts and working directly with different APIs but for these users, learning how to code was completely out of the question. They were looking for a simple solution, not a new career path.

Agents felt like an exciting possible solution but they were a bandaid on the problem. Throwing AI at every step of the way will only make things expensive and unreliable. We wanted a simpler way for people to reliably convert their tasks to valuable automation. This is how our automation framework was born.
**So your strategy is to take part of the responsibilities from agents if they are better done with deterministic software? **

Yes, exactly. The approach we are taking is using less AI in the workflow and creating something more reliable.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a63847a_6797b6384a877bc1f91d4914_dJ50j1s3FSlG6IxiDOqPCKoy5w.avif)

‍
**Do you think the future of AI agents lies in focusing on narrow tasks, like with Gumloop, or do generic agents still have a chance?**

I think what we’re building is the shortest path to reliable, affordable AI being leveraged in businesses.

Until true AGI arrives, the only people able to utilize AI to its full potential are engineers building with it. We’re lowering that technical bar so anyone can build complex flows with AI and see immediate business value.

## Is Gumloop a Zapier on steroids?

**Now we are getting more into the question of how Gumloop works. Can you talk about the product and how it is built?**

We are using Tailwind, CSS, React, and Typescript for the frontend, and Python for the backend.

The frontend provides a hyper-flexible canvas where the user can define their custom flows, we then run them in the cloud in a scalable way so that even workflows can be looped thousands of times to hyper-scale operations. 
**My first thought was that Gumloop reminds me of Zapier and I have seen your users call Gumloop “Zapier on steroids” too. What are the differences?**

Gumloop as the framework is very flexible, it’s almost like a visual programming language. There is always the tradeoff between how steep the learning curve is, versus what you can achieve with it.

You can have a ‘low floor’ which makes getting started simple, or a high ceiling which allows power users to build extremely complex automations. Our ceiling is extremely high compared to competitors. So high in fact that users are building entire businesses on Gumloop. We’re now working on lowering that floor next so that absolutely anyone can get started with ease.
**How are your customers utilizing the wide range of possibilities? What are some examples of what people are building with Gumloop?**

We have some very large startups and corporations as enterprise customers but the most impressive use cases are people who have built entire businesses on our app. For example, one of our enterprise users is using Gumloop to process academic papers for universities. His whole data pipeline and the service he provides is built on our platform.

He provides the expertise on how to build the automation and then sends it back to his customers at a much higher markup. He was able to build it all without hiring any AI engineer, so the value is equivalent to the salaries of several engineers.
**On your website, you have a lot of different templates for use cases from Sales to Hiring and Education. How customizable are the workflows in Gumloop?**

That’s our biggest strength. We are completely horizontal so we can really automate anything. The only missing part might be a particular integration, but we can quickly implement that for our customers.

On the other hand, it can do anything, but it’s hard to market. A lot of time we see the failure in creativity. People don’t really know what to do with Gumploop, so they need to see the examples to get the idea.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a63847d_6797b66c36af122d38b7f73a_0ypGCKhFx0NJ3sZD1DjAn9Fu3Jw.avif)
**We talked about removing responsibilities from AI agents. Are there still any autonomous parts within your platform?**

Almost none of our features are Agentic anymore on Gumloop. The closest to agentic decision-making is when you have an AI step, and set up conditional flows based on the response. E.g. “If the agent responds with this, let’s do this”. This happens for example with categorization and data extraction flows.

If you add more decisions like this in a row, it might seem autonomous, but even this is a deterministic process that depends on the previous output.

We do have some experimental web browsing agents built into the platform which are our take on the web voyager project. These are more proofs of concept however than something people should use in production.

## About security and code execution in the cloud

**We talked about removing responsibilities from AI agents. Are there still any autonomous parts within your platform?**

We have a big library of nodes. Nodes are building blocks that you drag onto the canvas to provide functionality, and each of the nodes has its specific purpose.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638483_6797b69a82aa06e6412d7e16_XD6F269dTFgTZCEHusOVeXGQ6s.avif)

We have a “run code” node that a lot of users choose when the existing nodes library doesn’t suffice for their use case. That is, once you want something very custom, e.g. your own way to manipulate and format data, we have to run code for that.

That’s why we use [E2B](/), which we see as the only way to do safe code execution within our automation. The E2B sandbox environment is the solution we are sure won’t destroy our servers with malicious code. The E2B runtime lets users code in Python or JavaScript, define dynamic inputs and outputs, and run code in the node, so it gives customers the flexibility to go the extra mile.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638480_6797b6c3425373f1b04b7f24_L5iVtQl6v9ssWQYUs6R54vQumw%2520(1).webp)](/docs/sandbox/overview)

‍
**What’s the most popular use case today?**

There are some patterns, but the most exciting ones are so niche that they seem useless to the general population. The bigger the business, the more boring and niche the work becomes. A lot of companies are just doing the same specific thing thousands of times a month, so giving someone else the same template wouldn’t bring much value.

Among more generic use cases, web scraping is very popular, e.g., using external data from the internet to enrich flows, scrapping subreddits, summarizing reports of what customers are complaining about… A lot of people have businesses that aggregate information, like databases or directories of sources. These are the kinds of users approaching us. Keeping information up to date is important and often requires automation.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638489_6797b6e1732ca69275156bb8_W63vSby6QuF96Gp1toZcFFhJ6Y4.avif)](https://x.com/MaxBrodeurUrbas/status/1793336019263320199)

‍

Another big use case is document processing. We found out that a lot of companies, especially those interacting with the government, have to deal with a lot of annoying forms and documents. More old-aged businesses like lawyers or people working in shipping and logistics have to fill in tons of annoying paperwork, so they get pretty excited about the ability to process documents in a smart way. Whether it is categorizing data, or processing it for their CRM. This is the boring paperwork to automate with Gumloop.
**In the beginning, you talked about the benefit of no-code UI. What do you offer for more technical users, like developers, apart from customizing the “run code” node?**

We have the more “advanced” category of nodes, where you can call your own arbitrary API in the automation. For example, people make get requests to their own servers to receive the product information. You can use the code execution, you can script in Selenium without using code. We have a “web agent scraper” with discrete actions like “scroll”, “click” “hover”, or “screenshot” allowing you to automate your browser in a selenium-like way.
**How can people integrate Gumloop into their existing products?**

We can trigger the automations with Webhook. This is how people integrate the Gumloop automations into their own products. Generally, all automations have one or a few input nodes with input data, but with Webhook, you can pass in values as input nodes. For example, you put in the first and last name via the Webhook, trigger it via API, and in turn, it researches the person and pings you on Slack about it.
**How agnostic is Gumloop? Are there any techstack limitations or lock-ins?**

Yes, it works with anything. We are completely model-agnostic too, so every time a new LLM comes out, users can just run the automations with a new model easily without changing anything.

Any integration we don’t have now is possible to add as long as they have a public-facing API for us to integrate with. We can ship features like this within days when customers need them.

The only “lock-in” is that the Gumloop automations stay in the Gumloop platform since they’re a totally custom format that is executed in quite a uniquely scalable way on our backend.
**You are building an enterprise-grade product and your customers are often companies. Are there any security and compliance challenges you had to overcome?**

We have had several requests for different certifications, e.g. a request for SOC 2. These typically come from bigger companies like banks, that require a lot of certifications or even on-prem hosting. Some companies want to run Gumloop in their own locally hosted LLM such that no data would leave. This is on our roadmap, but at this moment we haven’t had an urgent need to focus on this yet..
**Apart from security, what are other important aspects of building a product for enterprises?**

## Why AgentHub rebranded to Gumloop

**What else is on your roadmap recently?**

We recently released parallel node execution that really sped up some automations. Let’s say you are processing a thousand websites and performing the same tasks on them. That might take a day. However, since we added the parallel batch mode, you can process many websites at once, which makes these processes take not a day, but just an hour.

We are also adding a lot of AI features that allow users to build more easily. We are trying to lower the floor starting with Gumloop. The complexity is what can make new-coming people leave before using the platform in a meaningful way, so we are solving this problem.
**What is your approach to generative UI?**

I think if you nail generative UI, you get the ultimate personalization and onboarding experience. We are trying to let users describe what they want to build, the same way they would describe it to a human, and encode our understanding of how to approach it to an LLM that is able to do it at scale and help out.

I think it is done well and allows us to completely change the journey of some users.  The ability to demonstrate to people what they can build, instead of hoping that some content on your page will speak to them or some example you published will address their needs. That is, I see generative UI as a problem of execution and user experience problem more than a technical problem. At least with regard to generating automation on our platform, we know that it’s possible, but the question is how to make it enjoyable for users.
**What are the biggest challenges for you at this moment?**

I think the biggest thing is not having enough engineering hours in a day. We are a team of two full-time engineers, plus doing a lot of sales, marketing, and hiring. It’s hard to increase velocity when you’re working 14-hour days every day. 
**My last question is about your recent rebranding. Why did you go from AgentHub to Gumloop?**

We rebranded to Gumloop, because instead of “AgentHub”, people were hearing “AsianHub”, and that’s not something you want to google. Another reason was some points from Paul Graham's essay “[Change Your Name](https://paulgraham.com/name.html?ref=blog.gumloop.com)”. And finally, we are not technically building agents (which non-technical people often don’t know anyway), and the original direction of a hub for agents isn’t relevant anymore.

The name Gumloop suggests connecting things with some sticky substance and looping one instance of 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c398949703945a638474_6797b70bc69fb3935d2d3d19_oReUFZn2SkH3JAt16us9n3vY0.avif)

### Discover more

- [Gumloop.com](https://www.gumloop.com/)
- [Gumloop - X (Twitter) profile](https://x.com/gumloop_ai)
- [Max Brodeur-Urbas - X (Twitter) profile](https://x.com/MaxBrodeurUrbas)
- [Gumloop - LinkedIn profile](https://www.linkedin.com/company/gumloop/posts/?feedView=all)
- [Gumloop - video tutorials](https://www.youtube.com/@Gumloop_Ai)
- [Gumloop - Discord server](https://discord.com/invite/xtbrafmzC7)