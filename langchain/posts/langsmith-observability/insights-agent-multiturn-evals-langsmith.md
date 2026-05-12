---
title: "Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith"
author: "LangChain Accounts"
date: "2025-10-23"
url: "https://www.langchain.com/blog/insights-agent-multiturn-evals-langsmith"
---

Company AnnouncementsLangSmith

# Improve agent quality with Insights Agent and Multi-turn Evals, now in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 23, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa58d3aab32815f81955_Blog-02.png)**TL;DR:** We’re releasing new capabilities in **LangSmith** to help monitor agents in production. We’re making the concept of “threads” - representing a multi-turn agent interaction - a first-party concept, and we’re adding two new tools to monitor threads: **Insights Agent** for automatically categorizing agent usage patterns, and **Multi-turn Evals** for scoring complete agent conversations.

More and more agents are moving to production. As they do so, AI teams find themselves needing better visibility into what’s happening across all user interactions. But, traditional observability and testing that focus on uptime can&#x27;t tell whether your agent is actually accomplishing users’ goals. And testing your agent before it goes into production (what we call offline evals) only covers what you had in mind to start.

Today, we’re releasing new features to help you understand what’s happening inside your agent *while it’s in production*, so you can prioritize improvements:

- **Insight Agent**: automatically categorizes agent behavior patterns
- **Multi-turn Evals**: helps you evaluate the complete agent trajectory in each conversation

## **Discover patterns in production traces with the Insights Agent**

Today&#x27;s popular agents produce millions of traces per day—soon to be billions. These traces contain valuable signal about an agent&#x27;s capabilities and how real users engage with it. If you could review each interaction, you would gain deep insight into how to improve your agent. Manual review is time-consuming and impossible at scale, so how can we automate this insight generation process?

**Insights Agent** is our first step towards helping LangSmith users find signal in their production traces. Insights Agent analyzes traces to discover and surface common usage patterns, agent behaviors, and failure modes.

In agent engineering, you need to iterate rapidly to build reliable experiences. This new feature helps you answer questions like “What are users asking my agent?”, so you can determine where to focus your next set of tests based on real interactions your agent is having.

Once you [trace your data](https://docs.langchain.com/langsmith/observability-quickstart?ref=blog.langchain.com) to LangSmith, you have a few options for how to categorize usage insights.

- **Group by usage patterns:** Cluster based on common usage patterns. This helps you understand how users are actually using your agent. When you put a chatbot in front of people, they can ask it anything. Now you can find out what they are asking.
- **Group by poor interactions:** Cluster based on how your agent is messing up. We will look for signals in each conversation that indicate a negative interaction (user getting frustrated, etc), and then group the root causes. This helps you understand common ways your agent fails, so you can prioritize improvements.
- **Customize configurations:** Insights Agent is highly configurable. You can specify which categories it should group by, filter on existing attributes (like traces from a particular time period or keywords in a chat), define new attributes, and save configs for future use.

Generating insights can take up to 15 minutes depending on how much data the agent is crunching. Once the report is ready, you’ll see traces organized into categories and subcategories based on your initial request. You can click into any category to explore the underlying traces and add them to datasets or annotation queues. You can also see other LangSmith metrics split by category, like latency, number of runs, and any evals you have set up.

Our goal in building this feature was to help you kick off exploration and ideas for improvements as quickly as possible.

**Insights Agent is now generally available** for LangSmith Plus and Enterprise cloud customers. [Sign up for LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) and [check out our docs](https://docs.langchain.com/langsmith/insights?ref=blog.langchain.com) to get started.

## Evaluate end-to-end agent interactions with Multi-turn Evals

Once you have a good sense of the top usage patterns your agent is handling, you can start to drill into how each complete conversation is performing. Until now, that’s been tricky — most other evaluation platforms only focus on individual traces or steps, making it hard to understand whether the overall interaction achieved the user’s goal.

Today, we&#x27;re launching **Multi-turn Evals** to help you measure whether your agent accomplished the user’s goal across an *entire* interaction. You can do still evaluate at the trace level in LangSmith, but now you can also but also evaluate the whole interaction.

Multi-turn evals are online evaluations that let you measure things like:

- **Semantic intent**: What the user was actually trying to do.
- **Semantic outcomes:** Whether the task was completed (and if not, why).
- **Agent trajectory:** How the interaction unfolded, including tool calls and decisions made along the way.

In LangSmith, we represent these multi-turn exchanges between users and agents as [**threads**](https://docs.langchain.com/langsmith/threads?ref=blog.langchain.com). If you’re already using threads, getting started is simple. Multi-turn evals run automatically once a conversation is complete, and you define the LLM-as-a-judge prompt to guide scoring.

Insights Agent and Multi-turn evals are the first of several thread-level features we’re working on. Stay tuned for thread-level metrics and dashboards, automations to add threads to an annotation queue and datasets, and SDK support so you can programmatically pull and analyze threads.

**Multi-turn evals are live today for all LangSmith users.** [Visit our docs](https://docs.langchain.com/langsmith/online-evaluations?ref=blog.langchain.com#configure-multi-turn-online-evaluators) to get started.

## **Iterate faster with LangSmith**

Our latest LangSmith updates work together to address tough challenges when engineering reliable agents. Now, you can understand what&#x27;s happening in production (Insights Agent) and measure whether agents accomplish user goals (Multi-turn Evals). These features provide new levels of visibility to help you figure out what’s the best next step to improving your agent.

Ready to ship reliable agents? Get started with [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) today.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)