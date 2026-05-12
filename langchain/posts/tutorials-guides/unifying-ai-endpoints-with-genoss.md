---
title: "Unifying AI endpoints with Genoss, powered by LangChain"
author: "LangChain Accounts"
date: "2023-08-02"
url: "https://www.langchain.com/blog/unifying-ai-endpoints-with-genoss"
---

Agent ArchitecturePartner

# Unifying AI endpoints with Genoss, powered by LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 2, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)***Editor’s Note: This blog post was written by ***[***Matt Carey***](https://twitter.com/mattzcarey?ref=blog.langchain.com)***, one of the builders of Genoss. We&#x27;re sharing it on our blog too because we hear from a lot of people that don&#x27;t want to get locked in to a single model. We think tools like Genoss that provide clean interfaces for interoperability will help more builders get robust apps into production fast. We&#x27;re also incredibly excited about the integration it has with ***[***LangSmith***](https://www.langchain.com/langsmith?ref=blog.langchain.com)*** to enable easy debugging, logging, monitoring, and observability!***

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e03fe3e9a95a560c6b_genoss_front_logo-1.jpeg)

**Introducing **[**Genoss GPT**](https://genoss.ai/?ref=blog.langchain.com)**: One line GPT application portability with the Genoss model gateway.**

*TL;DR: GenossGPT offers a universal interface for interacting with GPT models, simplifying the task of integrating and switching between models in your GenAI-powered application. It gives businesses control over their model usage, while leveraging LangSmith to provide enhanced observability and analytics in production.*

Development in the generative AI space continues to pick up steam, with an ever-expanding range of uses being found for large language models (LLMs). These uses span diverse domains including personal assistants, document retrieval, as well as image and text generation. Groundbreaking apps like ChatGPT have paved the way for companies to dive into the space and start building with this technology.

Big players are building their own models such as AWS with their Titan models, Meta with their newly released Llama 2, and Microsoft with their partnerships with both OpenAI and Meta, showing that there is serious investment in the space.

Unicorn startups like Hugging Face, [raising money at a $4 billion valuation](https://www.forbes.com/sites/alexkonrad/2023/07/13/ai-startup-hugging-face-raising-funds-4-billion-valuation/?ref=blog.langchain.com), have dominated the open-source space and allow anyone to deploy models with ease. Universities will continue to push the envelope of what is possible on a budget, and these innovations will feed back into open-source projects. However, it is unlikely that smaller companies will be able to compete with big tech giants in building production LLMs from scratch due to the high costs.

Ecosystems like [LangChain](https://python.langchain.com/docs/get_started/introduction.html?ref=blog.langchain.com) provide a set of helpful utilities for developers interacting with these third-party LLMs, or foundational models as they are often called. LangChain classes help developers leverage models with I/O and memory, as well as providing model chains to accomplish specific tasks such as document retrieval. Additionally, LangChain establishes a standard vocabulary, introducing terms like ‘RetrievalChain’ and ‘MemoryStore’ with well-defined meanings in the ecosystem, thereby streamlining discourse among AI engineers.

# The integration problem

A discernible gap, still resides in the current tooling designed to facilitate integrations with LLM providers. As newer and improved models are introduced and the technology progresses, engineers want the freedom to be able to quickly implement new features with these models.

LangChain provides classes for a huge amount of models, such as OpenAI and Hugging Face, based on a common LLM class. However it requires using different classes for each provider. These classes have various methods and properties and although you would hope they are directly plug and play, the actual solution is rarely that simple.

Factors such as model streaming and nested chains further complicate the problem. LangChain does a great job at building interoperability between composable pieces (e.g. VectorStores, DocumentLoaders &amp; Retrievers) but we need to improve the developer experience when it comes to switching between LLM models.

# Genoss is the solution

Genoss is a model gateway powered by LangChain. It standardises the process of calling any supported LLM into one unified interface, compatible with the OpenAI API specification. By simply changing your base URL to your Genoss endpoint, you have the power of any LLM model at your fingertips. Direct integration with any 3rd party tool that supports the OpenAI interface is enabled out of the box.

Genoss does the heavy lifting for you to provide a single cohesive interface for interacting with both Completions and Embeddings models across multiple providers. You can switch between local open-source models, OpenAI models, AWS Bedrock models or any Hugging Face model with just a simple change to the model name.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e03fe3e9a95a560c66_1-2jyuuxqovdj5xkgagh9jdq.png)[https://genoss.ai/](https://genoss.ai/?ref=blog.langchain.com)

When using Genoss in an enterprise setting, an admin can update the model with a singular change on the dashboard (*coming soon)*. There is no need to update any application code to point towards new providers, the mapping is handled entirely by Genoss. This is useful for applications which use different models for different tasks or even users tiers. Paid users of your application could be given access to a choice of models with varying benefits such as enhanced privacy or fine-tuning using specific knowledge, whereas demo users would use a generic and cheaper model.

# Usage in production

Genoss is open-source and is free to use via the hosted version or to self-host on your own infrastructure. Think of Genoss like [Supabase](https://supabase.com/?ref=blog.langchain.com) for LLM applications. It empowers developers to go from a weekend side-project straight to production using the same infrastructure and tech stack.

Genoss leverages LangChain’s new tool, LangSmith. LangSmith provides observability, debugging and testing on the inputs and outputs of the models at each stage of the workflow. Analytics of LLM calls can be performed to help improve the usage and effectiveness of the model and the prompts. This allows companies to run LLM based workflows in production with higher confidence in their models and their outputs than ever before.

When using Genoss as your model gateway, LangSmith is automatically setup and ready to use. Companies can also use LangSmith to track token usage, manage costs of their LLM calls and keep an eye on latencies directly from the Genoss console.

# Conclusion

The lack of consistency between model interfaces makes building with LLMs unnecessary complicated. As cloud providers, commercial and open-source models are not aligned on a standard interface, Genoss provides interface unification. Genoss reduces the learning curve for developers starting to build, and for organisations scaling applications harnessing the power of Generative AI.

Given the rapid pace of LLM advancements, developers will use Genoss to test the latest models, experiment with fine-tuning and run private models locally. Enterprises will use Genoss to control the model usage of their users in both internal and production apps whilst utilising LangSmith for observability, debugging and testing.

**Find the code repository for Genoss **[**here**](https://github.com/OpenGenenerativeAI/GenossGPT?ref=blog.langchain.com)**. We look forward to seeing what you will build with it.**

**Thanks to the team **[**Stan Girard**](https://twitter.com/_StanGirard?ref=blog.langchain.com)**, **[**Maxime Thoosen**](https://twitter.com/maxthoon?ref=blog.langchain.com)**, **[**Arnault Chazareix**](https://twitter.com/Arnault_Chaz?ref=blog.langchain.com)** for all your hard work.**

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)