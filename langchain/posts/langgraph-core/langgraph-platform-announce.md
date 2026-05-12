---
title: "LangGraph Platform in beta: New deployment options for scalable agent infrastructure"
author: "LangChain Accounts"
date: "2024-10-31"
url: "https://www.langchain.com/blog/langgraph-platform-announce"
---

Company AnnouncementsLangGraph

# LangGraph Platform in beta: New deployment options for scalable agent infrastructure

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 31, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae522c7f205b929aa55a_editing---langgraph-platform--3-.png)*Note: As of October 2025, LangGraph Platform has been re-named to &quot;LangSmith Deployment&quot;.*

A few months ago, we [launched LangGraph Cloud](https://blog.langchain.com/langgraph-cloud/), our infrastructure purpose-built for deploying agents at scale. Today, we are enhancing that original value proposition by expanding our LangGraph deployment options and rebranding our service as LangGraph Platform.

[LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com#overview) is our service for deploying and scaling LangGraph applications, with an opinionated way to build agent UXs, plus an integrated developer studio. We now offer [multiple deployment options](https://langchain-ai.github.io/langgraph/concepts/deployment_options/?ref=blog.langchain.com) in beta:

- **Self-Hosted Lite**: Access a free (up to 1 million nodes executed), limited version of LangGraph Platform that you can run locally or in a self-hosted manner.
- **Cloud SaaS**: Fully managed and hosted as part of LangSmith, our Cloud offering lets teams deploy quickly, with automatic updates and zero maintenance. While it is in beta, anyone with a LangSmith Plus or Enterprise plan can try the Cloud SaaS version for free.
- **Bring Your Own Cloud (BYOC)**: Run LangGraph Platform in your VPC with our managed service, so you can keep data in your environment while we handle provisioning and maintenance. Currently only for AWS.
- **Self-Hosted Enterprise**: Deploy LangGraph applications entirely on your own infrastructure.

Below, we’ll dive into how we’ve arrived at LangGraph Platform and what it provides for developers today.

## How we arrived at LangGraph Platform

When we first launched LangGraph Cloud back in June, it included a few components:

- **LangGraph Studio**: A developer studio for visualizing, interacting with, and debugging agentic apps
- **LangGraph Server**: A server providing an opinionated way to deploy and interact with agents (e.g. endpoints for streaming, human-in-the-loop, etc) as well as manage agents (e.g. create assistants, version assistants, etc).
- Hosting of LangGraph Server on our cloud platform

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae542c7f205b929aa56a_Screenshot-2024-10-30-at-6.10.48-PM.png)

As feedback came in, the first thing that we noticed was that **people really liked **[**LangGraph Studio**](https://blog.langchain.com/langgraph-studio-the-first-agent-ide/). In fact, they liked it so much that they were deploying their graphs on LangGraph Cloud - just so they could debug with LangGraph Studio! From this learning, we released a desktop version of LangGraph Studio so that developers could debug on it locally.

The next thing we realized is that **people were finding a lot of value in LangGraph Server**. Deploying long-running, stateful agents is difficult due to the complexity of managing state and context. We heard consistently from developers that prior to using LangGraph Server, they had to rewrite much of the core infrastructure that we had built-in to support these agents effectively.

Finally, we discovered that some users preferred to host their agents on a cloud service — but others did not. Our service required significant infrastructure, and for most teams it was easier for us to manage running that infrastructure. However, some developers needed to meet **strict data privacy requirements** or to connect to internal APIs — and so running in our cloud was not an option.

With these learnings under our belt, we decided to couple some of our latest offerings under LangGraph Platform. **LangGraph Platform today includes LangGraph Server, LangGraph Studio, plus the CLI and SDK.**

## What’s in LangGraph Platform?

We’re now provide several flexible deployment options under LangGraph Platform — with LangGraph Studio and LangGraph Server as essential components of the platform to deliver a complete infrastructure solution for deploying agents at scale.

LangGraph Platform consists of the following:

- LangGraph Server
- LangGraph Studio
- LangGraph CLI and the Python/JS SDK

As we’ve worked with companies to deploy their LangGraph apps, we’ve seen nearly all of their teams build the same deployment infrastructure — and to address their needs, we added features in LangGraph Server to deliver on a few key value areas. Below, we’ll focus on these aspects of LangGraph Platform.

First, LangGraph Server is designed for handling large workloads gracefully. To do so, it has:

- **Horizontally scalable infrastructure and task queues** to handle high volume or bursts of incoming requests
- **Support for long-running agents** that can handle continuous, stateful tasks (unlike most web infrastructure, which is aimed at running short jobs)
- **Ability to persist data** within and across conversation threads

In addition, LangGraph Platform’s APIs allow users to create interactive, context-aware agent experiences. With the following LangGraph Platform features, humans can more easily steer their agent and interact with it to accomplish their goals:

- **Streaming runs** for interactive UX and real-time outputs seen by users
- **Background runs** for batch processing to support research-style or time-intensive tasks
- **Interactive state tracking** for humans to interact with the persistence layers and update it, rollback, etc.
- **Concurrency control,** including ways to deal with multiple incoming user messages before the agent can respond to the first
- **Cron jobs and webhooks** to support multi-step workflows

We’re planning on adding even more features (authentication/authorization to call the LangGraph APIs, intelligent caching, etc.) shortly.

We’ve seen that building all of this infrastructure is non-trivial, and we imagine it will become even more complicated as agents get more complex. As a result, we’re investing heavily in not only helping developers in building agents, but deploying them as well.

## How to get started

There are several different ways to get started on LangGraph Platform (now in beta).

If you’d like to host the infrastructure yourself, you can [try out LangGraph Platform for free](https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/?ref=blog.langchain.com) (for up to 1 million nodes executed). Once you grow beyond 1 million nodes, you can easily upgrade to the Self-Hosted Enterprise version with no migration needed.

To host and deploy agentic applications accessible from anywhere, [get started on the Cloud SaaS version](https://langchain-ai.github.io/langgraph/cloud/quick_start/?ref=blog.langchain.com).

If your deployment requires greater security or support needs, please [contact us here](https://www.langchain.com/contact-sales?ref=blog.langchain.com) to learn more about our Bring Your Own Cloud (BYOC) or Self-Hosted Enterprise options.

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