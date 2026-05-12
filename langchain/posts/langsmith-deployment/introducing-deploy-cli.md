---
title: "Introducing deploy cli"
author: "LangChain Accounts"
date: "2026-03-16"
url: "https://www.langchain.com/blog/introducing-deploy-cli"
---

Company AnnouncementsDeployment

# Introducing deploy cli

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)1min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9a39c83842382406f0c_7--2--1.png)We’re excited to introduce the deploy cli, a new set of commands within the `langgraph-cli` package that makes it simple to deploy and manage agents directly from the command line.

The first command in this new set, `langgraph deploy`, lets you deploy an agent to [LangSmith Deployment](https://docs.langchain.com/langsmith/deployments?ref=blog.langchain.com#langsmith-deployment) in a single step. This makes it easy to integrate LangSmith Deployment into existing CI/CD workflows using tools like GitHub Actions, GitLab CI, or Bitbucket Pipelines.

When you run the command, the cli builds a Docker image for your local LangGraph project and provisions [the infrastructure](https://docs.langchain.com/langsmith/data-plane?ref=blog.langchain.com#server-infrastructure) needed to run it. This includes setting up supporting services like Postgres for persistence and Redis for streaming messages, so your agent can run reliably in production without any manual infrastructure setup.

Alongside `langgraph deploy`, we’re also introducing a few other commands to help create and manage deployments in your workspace.

You can:

- View all available commands using `langgraph deploy --help`
- List deployments in your workspace using `langgraph deploy list`
- View deployment logs using `langgraph deploy logs`
- Delete deployments using `langgraph deploy delete`

We’ve also released new [deep agent](https://github.com/langchain-ai/deep-agent-template?ref=blog.langchain.com) and [simple agent](https://github.com/langchain-ai/simple-agent-template?ref=blog.langchain.com) templates that you can generate with `langgraph new` .

To see how easy it is to deploy and manage your agents with the cli, see the below video:

## Try It Out

The new commands are available now in the latest version of **`langgraph-cli`**. You can use `uvx` to get started easily:

`uvx --from langgraph-cli langgraph deploy
`

See the docs here: [https://docs.langchain.com/langsmith/cli#deploy](https://docs.langchain.com/langsmith/cli?ref=blog.langchain.com#deploy).

As always, we’d love your feedback as we continue improving the developer experience around building and deploying agents.

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