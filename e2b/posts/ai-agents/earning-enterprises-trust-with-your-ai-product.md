---
title: "Athena Intelligence: Earning enterprises' trust with your AI product"
author: "Tereza Tizkova"
date: "2024-07-09"
url: "https://e2b.dev/blog/earning-enterprises-trust-with-your-ai-product"
category: "ai-agents"
site: "e2b"
---

When people talk about AI agents, one particular thing they ask very often is the option to analyze their own data, like PDF, Web, or Excel. That’s exactly what [Athena Intelligence](https://www.athenaintelligence.ai/) is great at. Athena is the first artificial data analyst, which automates time-consuming tasks so that analysts can focus on strategic work.

Recently, they announced the code execution feature. This is a major next step for code generation - you can now let the AI assistant write code to enable complex analytics without leaving the chat interface.

I talked to [Ben Reilly](https://www.linkedin.com/in/patrickbenreilly/), the founding platform engineer about building a trustworthy AI product, what is going on “behind the scenes” of Athena, and what enterprises care about the most.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797cc5f7270aefbda5d12df_6797cbb9d9e65f810402db97_hz4buhNcZoY3hiqY5FTVqura8g.webp)](https://www.athenaintelligence.ai/)
**You are building Athena intelligence. How did you start, and what were the beginnings like?**

The story starts with the founder [Brendan Geils](https://www.linkedin.com/in/brendongeils/). The idea behind Athena is a one-stop shop for enterprise data analytics. We aim to be the place where enterprise data teams, whether that means analysts or engineers, go to help understand their data. 

As LLMs have gotten better and better, we've seen a very obvious use case in our platform. Athena harnesses LLMs to provide enterprise analytics teams with everything they need out of the box to move fast and get productive answers to the business as fast as possible.
**For readers who haven't tried the product, can you describe the basic building blocks and features of Athena?**

Athena offers many interfaces. The original is chat, but we now offer AI-powered reports, spreadsheets, and other interfaces.

Currently, users can leverage a variety of tools within the chat, including accessing information from PDFs and spreadsheets in your workspace. Athena can use this information to answer questions about your business in real-time. Athena also enables an auto-pilot mode to do this, where workflows you previously had Athena help you with become fully automated.

I find the roadmap really exciting as it aligns with our future goals and takes advantage of advancements in the field. I believe our platform will only become more useful as the models improve. 

> "The vision is to build a platform that brings value to the most technical person in the room but is also immediately useful for the least technical one."
**How is the experience with Athena different for technical versus non-technical people and teams?**

A data analyst can work without having to deal with any complexity, while a technical person can get more specific and have greater control by writing custom components.

The vision is to build a platform that brings value to the most technical person in the room but is also immediately useful for the least technical one. That is, for someone who doesn’t know Python or SQL, but still has some basic understanding of data analytics and has a question to answer with data.

These workflows are enabled by [E2B](/), which enables trust in our platform for clients building a microVM and handling the code processes there.
**Regardless of technical skills of the user, what are your favorite examples of workflows done with Athena?**

Some examples include preparing complex reports, for example of a competitive landscape, synthesizing information across hundreds of documents, or researching important metrics.

Teams can even include Athena in their email and let it handle their tasks without needing to log in and initiate a conversation. Plus, any attachments or rich media in the email are automatically uploaded to your Olympus Drive.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797cc5f7270aefbda5d12e2_6797cbe0655304be4ba11617_JrlBxYOJGXvmJcOIRKDVodsk.webp)](https://www.athenaintelligence.ai/)
**There are a lot of security questions when building with AI. How do you make users trust the product?**

Imagine you hire a brilliant team of PhDs who have already worked on groundbreaking research. You bring them onto your team and give them all your Slack messages and all the context that they would theoretically need. You ask them to solve a tough problem, and they come back and they say 42. Would you believe them just like that?

The idea of observability and customizability is an integral part of how we will work with LLMs in the future. Even if GPT-7 was a genius, we need the AI products to be observable and tweakable.

If the Athena agent performs a complex task, the user can later closely examine the decision the agent made and check whether it was a good decision given the information provided. As the platform evolves and we keep adding new features and making improvements, this aspect remains crucial. 

Importantly, we never train models on any customer data. We take extreme care with data privacy - It is essential for enterprise applications. We can also deploy Athena to customer environments, including more sensitive networks like AWS Govcloud.
**What are other things you are proud of, that give you a competitive advantage?**

We need to ship fast too. When Anthropic dropped a new LLM ([Claude-3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)), 30 minutes later it was already available on Athena, and we opened up free account signups for the next 24 hours to allow teams to check out that new model.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797cc5f7270aefbda5d130f_6797cbf97d640e6745d7e264_XruoZkZX0XQJS97rcoMNeWkLyOY.webp)

We use [E2B](/) for code execution under the hood. The whole process starts with a code written by an LLM for you. Previously, the process consisted of manually copying the code to a Jupyter Notebook, running it, checking if it works, dealing with any errors, and repeating this process. 

With the code execution feature, we integrated this entire workflow into Athena, making it a first-class citizen across the platform. It's quite good now and will only improve in the future.

So now, every time an LLM writes Python code, Athena identifies it and executes it using the isolated E2B sandbox. If there are errors, the LLM automatically makes fixes and produces a new output for the user.

We see this unlocking lots of workflows where the agent can do more complex reasoning than without a code execution environment.

‍

> *"With code execution, the LLM has instant feedback on whether or not the code it wrote actually works."*

‍
**How else can the code execution feature improve the quality of results for users? Apart from not having to manually copy-paste and run the code.**

The most tangible thing is that with code execution, the LLM has instant feedback on whether or not the code it wrote actually works. It can immediately test its own output and compute verifiably correct complex operations. For example, multiplying several numbers together or doing complex math that an LLM would not verifiably give the right answer for.

That's a pretty useful primitive in the platform, and a big step in the LLM-powered software.

I am observing that AI programmers and human programmers have a lot of parallels. All LLMs can produce good code output, but some are obviously better than others. If you think about it, even a human can stare at a Python script for twenty-four hours and it still doesn’t have to be perfect or all things checked unless it has a compiler. 

We think LLMs should have the same tools as humans when trying to answer the questions in the right way.
**A lot of people are used to AI chatbots now. What do you think is the “it” AI product of the future?**

There are all sorts of technical questions which are worth answering but for us, we just try to maintain a razor focus on how the enterprise customers want to interact with this new technology.

You could go off and explore all sorts of cool research questions about LLMs. How do you make the context window bigger? How do you control attention? How do you have LLMs use tools in the most effective way? How do you string them together? All these questions are worth asking, a lot of that is gonna get solved, and our job at Athena is to write the future of how people interact with LLMs in a useful way.

I think chat is not the final version of the AI software. Chat is what we're comfortable with now, partially because ChatGPT was the first thing that launched, but the Fortune 500s that are interested in using this technology, probably aren't going to be using chat forever.

Eventually, it's going to have to turn into a workflow, which is more intuitive and probably resembles the places where we do knowledge work now, like spreadsheets and reports.

I would say the most pressing issue that we're working with is not a technical challenge, but sort of a human question of how we actually want to use this technology. That is, how does the UI look like such that it allows us to use this technology in the most useful way possible.

**Do the large customers really care about LLMs and that Athena is “AI-powered”?**

That's a good question. At the end of the day and especially at the enterprise level, things have to be useful. People are interested in Athena, but they're interested because the AI makes the product very useful. Not because it has AI for the sake of AI. [Sklearn](https://scikit-learn.org/stable/) solves Linear Regression better than ChatGPT would produce, and we think it will stay that way for the foreseeable future. So we try to build with that in mind.
**My last question is: What are your plans and vision for the future?**

As a high-level solution, Athena is the enterprise data platform that connects your entire team and empowers everyone with LLMs. Many of the features on our platform are already great and extremely useful, and we are committed to further development.

Our ultimate goal is to be the most immediately and tangibly useful platform possible for the enterprise, serving the largest companies in the world. We want to unlock the tedious portions of knowledge work, and allow Analysts to use their time to think strategically about what will help their business.

### Learn more

- [Athena Intelligence](https://www.athenaintelligence.ai/)
- [Athena Intelligence - X](https://x.com/AthenaIntell)
- [Athena Intelligence - LinkedIn](https://www.linkedin.com/company/athena-intelligence-ai/)
- [Athena Intelligence - YouTube](https://www.youtube.com/@athenaintelligence)
- [Ben Reilly (the founding platform engineer) - LinkedIn](https://www.linkedin.com/in/patrickbenreilly/)