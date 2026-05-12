---
title: "Test Run Comparisons"
author: "LangChain Accounts"
date: "2023-10-17"
url: "https://www.langchain.com/blog/test-run-comparisons"
---

LangChain

# Test Run Comparisons

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 17, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb122c83ac7211fe594d2_Screenshot-2023-10-14-at-3.42.23-PM-1.png)

> One pattern I noticed is that great AI researchers are willing to manually inspect lots of data. And more than that, they build infrastructure that allows them to manually inspect data quickly. Though not glamorous, manually examining data gives valuable intuitions about the problem.

[- Jason Wei, OpenAI](https://twitter.com/_jasonwei/status/1708921475829481683?s=20&amp;ref=blog.langchain.com)

Evaluations continue to be one of the hardest parts of building LLM applications. It&#x27;s really tough to evaluate in a quantitative way the effect of changes to your prompt, chain, or agent. We&#x27;re bullish on [LLM-assisted evaluation](https://docs.smith.langchain.com/evaluation/evaluator-implementations?ref=blog.langchain.com), but, at the same time, we definitely recognize that it&#x27;s hard to have complete trust in them.

Jason&#x27;s tweet above sums up what we see a lot of the best researchers (and engineers) doing. They want to manually inspect data to gain intuition about the problem. At LangChain, we want to build the infrastructure to help do that - which is why we&#x27;re excited to announce Test Run Comparisons today.

In the [initial release of LangSmith](https://blog.langchain.com/announcing-langsmith/) we had support for running tests, including scoring them with LLM-assisted feedback. However, each test was run in isolation. We quickly saw two usage patterns emerge:

- People are still hesitant to trust the LLM-assisted feedback directly
- Users often wanted to not only score their test run in isolation, but also compare it to previous iterations

When building Test Run Comparisons, we kept both of these insights in mind. We wanted to create an easy UX to see multiple test runs side-by-side. We also wanted to create an easy UX where people could use LLM-assisted evals (or regex/other eval) to get an initial score, then manually explore those datapoints for further insights.

So how does it work?

First, you need to set up a dataset and run some tests. See [documentation here](https://docs.smith.langchain.com/evaluation?ref=blog.langchain.com) for instructions on how to do that. Nothing new here, so if you&#x27;ve already done that for an existing project you&#x27;re all good.

Inside a dataset, you can easily select two (or more) test runs, then click `Compare`.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594e4_Screenshot-2023-10-14-at-3.42.42-PM.png)

From there, you will be brought into the Test Run Comparison view. This should look like the below

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb122c83ac7211fe594d2_Screenshot-2023-10-14-at-3.42.23-PM-1.png)

You can easily see the inputs, the reference output, and then the actual output for each datapoint - along with any [eval metrics](https://www.langchain.com/articles/llm-evaluation-metrics), time and latency for that run.

This view is designed to make it easy to quickly compare test runs across the same inputs. If you want a deeper look at a particular datapoint, you can click on that row and sidebar will pop up allowing you to drill down into the details of those runs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594dd_Screenshot-2023-10-14-at-3.46.17-PM.png)

On that sidebar, we&#x27;ve also added up and down carets (▲ and ▼) to easily flip between runs.

This view should hopefully make it easy to compare runs for a particular datapoint. But how do you know what datapoints to be looking at?

We&#x27;ve added filters for each column - similar to Excel. Using these filters, you can filter the rows according to any criteria.

💡

The criteria we recommend using to start? Filter one test run to datapoints it got correct, and the other one to datapoints that it got incorrect. This allows you to quickly drill on places of significant difference between the two test runs, which should more easily allow you to discover what has changed.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb123c83ac7211fe594da_Screenshot-2023-10-14-at-3.53.17-PM.png)

Building an LLM application is hard. A big part of that is understanding how the LLM is working on a particular task. Setting up an evaluation dataset and then being able to easily compare runs on that dataset is crucial for developing the understanding needed to improve the application.  Test Run Comparison in LangSmith aimed at solving this problem. Please let us know any feedback you have!

LangSmith is in private beta - [sign up here](https://smith.langchain.com/?ref=blog.langchain.com). We&#x27;ll be rolling out more access over the next few weeks, as well as continuing to add features like this.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa08cd1956c2e4f9ff39_Remote-case-study.png)Case StudiesLangChainLangGraph

#### How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/customers-remote)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)