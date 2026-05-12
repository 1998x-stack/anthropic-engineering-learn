---
title: "LangChain Skills"
author: "LangChain Accounts"
date: "2026-03-04"
url: "https://www.langchain.com/blog/langchain-skills"
---

Company AnnouncementsLangChain

# LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)We're releasing our first set of skills to give AI coding agents expertise in the open source LangChain ecosystem. This includes building agents with [LangChain](https://docs.langchain.com/oss/python/langchain/overview?ref=blog.langchain.com), [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview?ref=blog.langchain.com), and [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com). On our eval set, this bumps Claude Code's performance on these tasks from 29% to 95%.

## What are Skills?

Skills are curated instructions, scripts, and resources that improve coding agent performance in specialized domains. Importantly, skills are dynamically loaded through progressive disclosure — the agent only retrieves a skill when its relevant to the task at hand. This enhances agent capabilities, as historically, giving too many tools to an [agent would cause its performance to degrade](https://blog.langchain.com/react-agent-benchmarking/).

Skills are portable and shareable — they consist of markdown files and scripts that can be retrieved on demand. We're sharing a set of LangChain skills that can be ported to any coding agent that supports skill functionality.

## LangChain Skills

Within the [langchain-skills repo](https://github.com/langchain-ai/langchain-skills?ref=blog.langchain.com), we maintain a set of 11 skills, split broadly across 3 categories:

- **LangChain:** Guidance on how to use LangChain's `create_agent()`, middleware, and tool patterns. Fundamentals for working with the classic tool calling agent loop
- **LangGraph:** Guidance on how to work with LangGraph's primitives, and take advantage of its native support for Human In the Loop, durable execution, and more.
- **Deep Agents:** Guidance on working with our open source [Deep Agents package](https://github.com/langchain-ai/deepagents?ref=blog.langchain.com) and leverage its prebuilt middleware and `FileSystem`

## Skill Impacts

Using skills, we saw significant improvements in Claude Code's performance on basic LangChain, LangGraph, and Deep Agent tasks.

TestModelPass RateClaude Code without SkillsSonnet 4.625% Claude Code with SkillsSonnet 4.695%

*Pass rate was calculated using LangSmith evaluations. We plan to open source the testing benchmark we used*

To see how easy these skills can make building agents, see the below video:

## **Installation**

To install these skills, you can use [`npx skills`](https://github.com/vercel-labs/skills?ref=blog.langchain.com):

**Local** (current project):

`npx skills add langchain-ai/langchain-skills --skill '*' --yes
`

**Global** (all projects):

`npx skills add langchain-ai/langchain-skills --skill '*' --yes --global
`

To link skills to a specific agent (e.g. Claude Code):

`npx skills add langchain-ai/langchain-skills --agent claude-code --skill '*' --yes --global
`

## **Conclusion**

We're excited for the community to use LangChain and [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) to improve your experience building with our ecosystem. We plan to continue adding skills content as new capabilities are added to our Open Source and LangSmith. In addition to these skills for LangChain open source - we are also releasing a set of [LangSmith skills](https://blog.langchain.com/langsmith-cli-skills/) today as well. If you have ideas for additional skills or improvements, we'd love to hear from you!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)