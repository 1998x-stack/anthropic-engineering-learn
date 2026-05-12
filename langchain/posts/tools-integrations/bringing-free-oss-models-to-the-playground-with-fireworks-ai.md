---
title: "Bringing Free OSS Models to the Playground with Fireworks AI"
author: "LangChain Accounts"
date: "2023-10-02"
url: "https://www.langchain.com/blog/bringing-free-oss-models-to-the-playground-with-fireworks-ai"
---

PartnerAgent Architecture

# Bringing Free OSS Models to the Playground with Fireworks AI

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 2, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb140adb40d0919232a29_photo-1499233983070-99a5f004e720.jpeg)A year ago, the only real LLM people were using was OpenAI&#x27;s GPT-3. Fast forward to now, and there are a multitude of models to choose from - including a wide variety of open source models. These open source models have seen large performance gains over the past six months in particular. As these models get better, we&#x27;ve seen more and more people wanting to try them out. We&#x27;ve teamed up with [Fireworks AI](https://app.fireworks.ai/?ref=blog.langchain.com) to bring these models to the LangSmith playground - completely free of cost (for now, we&#x27;ll see how expensive this gets).

What does mean exactly?

Concretely, we have integrated [Fireworks AI](https://app.fireworks.ai/?ref=blog.langchain.com) into the playground, joining the ranks of OpenAI, Anthropic and Vertex AI as supported model providers. Read more about Fireworks AI below, but at a high level they provide API access to a plethora of OSS models. While other model providers in the playground require an API key to use, we&#x27;ve worked with Fireworks AI to enable anyone to use this integration regardless of whether they have an API key or not (note: you need to be signed into the LangSmith platform in order for this to work).

This now means it is easier than ever to try out prompts with an OSS model. Let&#x27;s walk through an example of this!

First, let&#x27;s go the [LangSmith Hub](https://smith.langchain.com/hub?ref=blog.langchain.com). We can filter existing prompts in the hub to ones that are meant for Llama-2. Note: this is a manual tagging, so it could be incorrect, but it&#x27;s a good start.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb141adb40d0919232a33_Screenshot-2023-09-30-at-5.50.07-PM.png)

Let&#x27;s choose the [`hwchase17/llama-rag` prompt](https://smith.langchain.com/hub/hwchase17/llama-rag?ref=blog.langchain.com). Once on this page, we can click on &quot;Try it&quot; to open it in the playground.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb141adb40d0919232a36_Screenshot-2023-09-30-at-5.52.07-PM.png)

The playground defaults to OpenAI, but we can click on the model provider to change it up.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb141adb40d0919232a39_Screenshot-2023-09-30-at-5.52.43-PM.png)

From here, we can select the Fireworks option.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb141adb40d0919232a3c_Screenshot-2023-09-30-at-5.57.04-PM.png)

We can now select the model we want to use, and then plug in some inputs and hit run!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb141adb40d0919232a3f_Screenshot-2023-10-02-at-8.42.19-AM.png)

## What is Fireworks?

[Fireworks.ai](https://app.fireworks.ai/?ref=blog.langchain.com) provides a platform to enable developers to run, fine-tune, and share large language models (LLMs) to best solve product problems.

The Fireworks.ai Generative AI platform provides developers access to lightning-fast OSS models, LLM inference, and state-of-the-art foundation models for fine-tuning. The platform provides state-of-the-art machine performance for latency-optimized and throughput-optimized settings and cost reduction (up to 20–120x lower) for affordable serving.

Integrating Fireworks.ai models in the LangChain Playground means giving the developer community easy access to the best high-performing open-source and fine-tuned models.

The LangChain Prompt Hub already makes it simple to try different prompts, models, and parameters without any coding. The availability of faster inference or faster LLMs helps to further boost productivity in building LLM workflows.

A big part of the LLM workflow requires testing and optimizing prompts which is a highly iterative and time-consuming process. This integration makes it possible for LangChain Prompt Hub users to more efficiently test and optimize prompts for state-of-the-art open-source and fine-tuned LLMs like Llama 2 70B.

**Trying Fireworks in the Playground:**

- Logged-in users can try Fireworks in the playground without an API key, for free!
- If you’re not logged in or don’t have an account, but want to try Fireworks, you can get one directly from Fireworks

**Below are the instructions to set up an account with Fireworks.ai:**

- Step 1: Visit [app.fireworks.ai](https://app.fireworks.ai/?ref=blog.langchain.com).
- Step 2: Click the &quot;Sign In&quot; button in the top navigation bar.
- Step 3: Click &quot;Continue with Google&quot; and authenticate with your Google account. A new Fireworks developer account will be provisioned for you the first time you sign in.
- Step 4: Next, we&#x27;ll provision a new API key. Click on &quot;API Keys&quot; in the left navigation bar then Click on &quot;New API Key&quot; and give your new API key a name.
- Step 5: Now open-source models like Llama 2 13B Chat are ready to be used in the LangChain Playground.
- Step 6: You can enter you API key in the `Secrets &amp; API Keys` section in the playground

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