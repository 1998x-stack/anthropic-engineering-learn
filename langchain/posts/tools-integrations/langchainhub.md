---
title: "LangChainHub"
author: "LangChain Accounts"
date: "2023-01-24"
url: "https://www.langchain.com/blog/langchainhub"
---

Company AnnouncementsLangChain

# LangChainHub

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb271ba9d0fc7237844bf_photo-1576403103737-dc646cbf7de5.jpeg)We are excited to announce the launch of the [LangChainHub](https://github.com/hwchase17/langchain-hub?ref=blog.langchain.com), a place where you can find and submit commonly used prompts, chains, agents, and more!

This obviously draws a lot of inspiration from Hugging Face&#x27;s Hub, which we believe has done an incredible job of fostering an amazing community.

## Motivation

Over the past few months, we’ve seen the LangChain community build a staggering number of applications using the framework. These applications use LangChain components such as prompts, LLMs, chains and agents as building blocks to create unique workflows. We wanted to make it easy to share and discover these workflows by creating a hub where users can share the components they’ve created.

Our goal with LangChainHub is to be a single stop shop for sharing prompts, chains, agents and more. As a starting point, we’re launching the hub with a repository of prompts used in LangChain. Often, the secret sauce of getting good results from an LLM is high-quality prompting, and we believe that having a collection of commonly-used prompts will make it easier for users to get great results without needing to reinvent the wheel. We hope to follow up by adding support for chains and agents shortly.

## Usage

We don&#x27;t just want to build a collection of prompts, agents, and chains - we want to make it as easy and as straightforward as possible for people to actually use these. To that end, we are taking two concrete steps:

- We will offer first-class support in the [LangChain Python library](https://github.com/hwchase17/langchain?ref=blog.langchain.com) for loading these artifacts. For example, you are able to easily load a prompt from the hub with the following snippet:

`from langchain.prompts import load_prompt
prompt = load_prompt(&#x27;lc://prompts/hello-world/prompt.yaml&#x27;)`

2. We will prioritize clear documentation on how to use these artifacts. For example, all prompts contain not only the artifact itself but also a README file. This file contains information like a description of how it is to be used, the inputs it expects, and a code snippet for how to use this prompt in a chain.

For more detailed information on how to use the artifacts on the Hub, check out the documentation on the [Hub itself](https://github.com/hwchase17/langchain-hub?ref=blog.langchain.com).

## Community

We highly intend this to be community driven. We have seeded the Hub with a collection of artifacts that are used in the core library, but we hope it quickly becomes filled with prompts, chains, and agents that are NOT in the core library.

Since we are using GitHub to organize this Hub, adding artifacts can best be done in one of two ways:

- Create a fork and then open a PR against the repo.
- Create an issue on the repo with details of the artifact you would like to add.

### Up Next

Today, LangChainHub contains all of the prompts available in the main `LangChain` Python library.

In the (hopefully near) future, we plan to add:

- Chains: A collection of chains capturing various LLM workflows
- Agents: A collection of agent configurations, including the underlying LLMChain as well as which tools it is compatible with.
- Custom prompts repo URI: The ability to set a custom [URI](https://www.techtarget.com/whatis/definition/URI-Uniform-Resource-Identifier?amp=1&amp;ref=blog.langchain.com) for prompt repositories, so that users can create their own LangChain hubs.

## Conclusion

We are looking forward to the community&#x27;s contributions and feedback as we continue to build out the Hub. Check it out [here](https://github.com/hwchase17/langchain-hub?ref=blog.langchain.com) and join the conversation on [Discord](https://discord.com/invite/6adMQxSpJS?ref=blog.langchain.com)!

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