---
title: "TypeScript Support"
author: "LangChain Accounts"
date: "2023-02-17"
url: "https://www.langchain.com/blog/typescript-support"
---

Company AnnouncementsLangChainOpen Source

# TypeScript Support

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 17, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb25b504e43f6295ac087_photo-1627398242454-45a1465c2479.jpeg)It&#x27;s finally here... TypeScript support for LangChain.

What does this mean? It means that all your favorite prompts, chains, and agents are all recreatable in TypeScript natively. Both the Python version and TypeScript version utilize the same serializable format, meaning that artifacts can seamlessly be shared between languages. As an example of using this, we&#x27;ve also recreated ChatLangChain with TypeScript.

A huge thank you to the community for helping with this.

Important Links:

- GitHub Repo: [https://github.com/hwchase17/langchainjs](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com)
- Documentation: [https://hwchase17.github.io/langchainjs/docs/overview/](https://hwchase17.github.io/langchainjs/docs/overview/?ref=blog.langchain.com)
- ChatLangChain-js: [https://github.com/sullivan-sean/chat-langchainjs](https://github.com/sullivan-sean/chat-langchainjs?ref=blog.langchain.com)

# Why TypeScript?

Initially, the crowd playing with language models was more of the researchy, ML-oriented folks - most of whom prefer Python. However, since the launch and quick success of ChatGPT, the idea of using LLMs has gone mainstream. As such, we saw a massive increase in interest in LangChain from folks across the stack, many of whom prefer to using javascript. As such, we thought it appropriate to develope a javascript native version of LangChain.

# What is in this package?

All of the same abstractions that are in the Python package are in the Typescript package.

- [Prompts](https://hwchase17.github.io/langchainjs/docs/modules/prompts/prompt_template?ref=blog.langchain.com)
- [LLMs](https://hwchase17.github.io/langchainjs/docs/modules/llms/openai?ref=blog.langchain.com)
- [Text Splitters](https://hwchase17.github.io/langchainjs/docs/modules/indexes/text_splitter?ref=blog.langchain.com)
- [Embeddings](https://hwchase17.github.io/langchainjs/docs/modules/indexes/embeddings?ref=blog.langchain.com)
- [Vectorstores](https://hwchase17.github.io/langchainjs/docs/modules/indexes/vectorstore?ref=blog.langchain.com)
- [Chains](https://hwchase17.github.io/langchainjs/docs/modules/chains/llm_chain?ref=blog.langchain.com)
- [Agents](https://hwchase17.github.io/langchainjs/docs/modules/agents/overview?ref=blog.langchain.com)
- [Memory](https://hwchase17.github.io/langchainjs/docs/modules/memory/buffer_memory?ref=blog.langchain.com)

Since the Typescript version is much newer, there are fewer of these implementations in there. Also, many of the more ML-centric functionality (tokenizers, LLMs, etc) have worse TypeScript support. Still, we intend to bring and grow that functionality over time.

With these abstractions, we found it very easy to recreate the &quot;ChatLangChain&quot; web application we previously made in Python to have a chatbot over our documentation. This utilizies many of those abstractions, and so is a perfect showcase. Check out the TypeScript version [here](https://github.com/sullivan-sean/chat-langchainjs?ref=blog.langchain.com).

# Relationship to the Python package

We intend the TypeScript package to mirror the Python package as closely as possible. To that end, it was a priority to make sure that serialized format we introduced for prompts, chains, and agents in Python worked for the TypeScript version.

We considered this a priority because as we grow the [LangChainHub](https://github.com/hwchase17/langchain-hub?ref=blog.langchain.com) over time, we want these artifacts to be shareable between languages. This will allow for largely and more widespread community adoption and sharing of best prompts, chains, and agents. This will also make it possible to prototype in one language and then switch to the other. At the moment, since the TypeScript package does have slightly less functionality than the Python package, not all the chains are portable between languages. However, we intend to push hard to make them equal.

Over time, it is not out of the question that the packages do diverge somewhat, in line with their respective audiences. For example, the Python package may start to include more researchy or data centric concepts, while the TypeScript package may include more features aimed at facilitating web dev. We are actually excited to explore the different priorities and use cases with the community. But throughout it all, we intended to keep on making the core set of prompts, chains, agents (and soon more) serializable and usable between languages.

# Thank You

A huge thank you to the community support and interest in &quot;Langchain, but make it typescript&quot;. At one point there was a Discord group DM with 10 folks in it all contributing ideas, suggestion, and advice. In particular, large shoutout to [Sean Sullivan](https://twitter.com/_seanyneutron?ref=blog.langchain.com) and [Nuno Campos](https://twitter.com/nfcampos?ref=blog.langchain.com) for pushing hard on this.

We also pre-emptively thank the community for their feedback, contributions, and ideas for this package. We&#x27;ve already gotten a lot of interest in the short time we&#x27;ve been teasing it, and we&#x27;re really excited to work on it together.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)