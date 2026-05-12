---
title: "LangChain 🤝 DemoGPT: New Era for Gen-AI Applications"
author: "LangChain Accounts"
date: "2023-08-21"
url: "https://www.langchain.com/blog/langchain-demogpt-new-era-for-gen-ai-applications"
---

Partner

# LangChain 🤝 DemoGPT: New Era for Gen-AI Applications

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 21, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9b1296d2991ed2aea6f7_image6.webp)*Editor&#x27;s Note: This post was written in collaboration with the *[*DemoGPT*](https://github.com/melih-unsal/DemoGPT?ref=blog.langchain.com)* team. We&#x27;re excited about what they&#x27;re doing to make it easier to not only build LLM applications, but also get them in the hands of users and build community in the process. We also thought way they built the platform on top of LangChain and Streamlit is really neat–their under-the-hood walkthrough offers some cool ideas for anyone using a language model to generate an app.*

Today we’re happy to announce the collaboration of[ DemoGPT](https://github.com/melih-unsal/DemoGPT?ref=blog.langchain.com) with LangChain to make generative ai application creation easier. In this blog post, we’ll dig deeper into the details of this collaboration and how to use DemoGPT to build scalable LLM-powered applications with LangChain.

**DemoGPT: Emerging Marketplace for LangChain Applications**

DemoGPT is[ an open-source project](https://github.com/melih-unsal/DemoGPT?ref=blog.langchain.com) that aspires to keep pushing the boundaries of Large Language Model (LLM) based application development. At its core, DemoGPT synergizes the capabilities of various Foundation Models, enabling the auto-generation of LangChain x Streamlit applications with just a prompt.

Here’s a look under the hood at how it works and where we see it going in the future.

**Unpacking DemoGPT: A Glimpse into its Technical Core**

*DemoGPT Architecture*

Navigating through the architecture of DemoGPT reveals a structured approach to code generation operations. This detailed exploration will take you through its core stages: Planning, Task Creation, Code Snippet Generation, Combining the Code Snippets, and DB Saving. Each stage plays a pivotal role in ensuring optimal functionality and efficiency. Let&#x27;s delve into each of these components to understand the intricacies of DemoGPT&#x27;s workflow.

**Planning**: DemoGPT starts by generating a plan from the user&#x27;s instruction.

When a user submits an instruction, its first port of call is the planning module. This segment is the bedrock of the entire DemoGPT structure because the following steps lean heavily on the valid global planning inspired by HuggingGPT. However, unlike HuggingGPT, which goes straight from instruction to task list, DemoGPT first creates a plan in natural language and later creates a task list. This way of processing is more intuitive for LLMs.

The Planning module knows all of the available toolsets to minimize hallucinations. It also uses a self-refining strategy so that planning continues until it is validated by itself.

**Task Creation:** It then creates specific tasks using the plan and instruction.

In our experiments, we have seen that using a natural language plan minimizes hallucinations vs. going straight from instruction to task list. Our novel approach reduces the number of refining steps needed in the task creation process. This step also has a self-refining subphase to get rid of hallucinated tasks. During this subphase, the module checks the (input, output) pairs of each task, then according to the result, it gives feedback to itself, then generates the tasks again according to the last iteration and continues until it passes the tests.

**Code Snippet Generation:** Tasks are transformed into Python code snippets.

Each task has its own prompt so that when the corresponding task is converted into a Python code, it uses its custom prompts for this transformation. The transformation process is mindful of previously generated code, so everything works well in tandem.

**Combining the Code Snippets:** The code snippets are combined into a final code, resulting in an interactive application.

All code snippets are put into a prompt to combine them together. Here, the final code is made compatible with Streamlit (such as state management). The output of this module is further improved by a self-refining technique to make sure everything is compatible with Streamlit.

**DB Saving (coming in next release):** The generated plan, tasks and code snippets stored in a vector database

In the whole architecture, each phase is applying self-refining to itself to get rid of hallucinated results. In addition, each module has its own examples for few-shot learning and for most applications. This works pretty well and allows applications to be created by lighter models like GPT-3.5 at 10% of the cost of GPT-4. However, to decrease the cost even more and make it more performant, the DB Saving module aims to save the approved results (plans, tasks, and code snippets) to a vector database so that next time, the relevant examples from the vector database will be fetched and used for the few-shot learning to decrease the number of refining steps. This will decrease the cost of application generation and at the same time make generation faster.

**How to Install DemoGPT?**

[Installing DemoGPT](https://github.com/melih-unsal/DemoGPT?ref=blog.langchain.com) is a straightforward process, designed to get you up and running with minimal hassle.

pip install demogpt

**How to Use DemoGPT?**

You can use the DemoGPT library either via CLI or by using its Python interface.

- **As a Command Line Interface (CLI)**

You can run the DemoGPT application as a Streamlit app by simply typing:

demogpt

Once running; enter your own API key and choose which base model you want to use.

When everything is ready, you can start creating applications just from a prompt. Let your imagination guide you. You can create a chat with your PDF app in seconds, or create a sentiment analysis tool that takes in a website and returns the tone of text.

Applications are limited only by prompts given, so with longer prompts you too can create sophisticated and unique AI applications.

*Tweet Generator: An application that can generate tweets from given hashtags and tone of the tweet.*

*Web Blogger: An application that can generate Medium blog from given website url*

- **As a Python Library**

You can run the DemoGPT application as a Python library. To incorporate DemoGPT into your Python applications, follow the steps below.

#### Import the necessary module:

from demogpt import DemoGPT

#### Instantiate the DemoGPT agent

agent = DemoGPT(model_name=&quot;gpt-3.5-turbo-0613&quot;, openai_api_key=&quot;YOUR_API_KEY&quot;, max_steps=10)

#### Set your instruction and title

instruction = &quot;Your instruction here&quot;
title = &quot;Your title here&quot;

#### Iterate through the generation stages and extract the final code

code = &quot;&quot;
for phase in agent(instruction=instruction, title=title):
    print(phase)  # This will display the resulting JSON for each generation stage.
    if phase[&quot;done&quot;]:
        code = phase[&quot;code&quot;]  # Extract the final code.
print(code)

For further information, you can visit [DemoGPT Docs](https://docs.demogpt.io/?ref=blog.langchain.com)

**From Idea to Marketplace: The Journey with LangChain x DemoGPT**

To provide a clearer picture of this collaboration, let&#x27;s walk through a potential user journey:

Imagine Sarah, an AI enthusiast with a brilliant idea for an application that leverages the power of language models. She visits the LangChain website, where she&#x27;s introduced to the integrated DemoGPT application generation tool.

*As a first step, app generation occurs on LangChain website*

With a few prompts and inputs, Sarah crafts her application, watching it come to life in real-time. Once satisfied with her creation, Sarah is presented with the opportunity to showcase her application on the [DemoGPT Marketplace](https://marketplace.demogpt.io/?ref=blog.langchain.com). With a simple click, her application is listed, making it accessible to a global audience.

*Once the app is generated, it will be listed on DemoGPT Marketplace*

Other developers, businesses, or AI enthusiasts can now discover Sarah&#x27;s application, interact with it, provide feedback, or even propose collaborative enhancements.

*All the generated apps will be listed and used on *[*DemoGPT Marketplace*](https://marketplace.demogpt.io/?ref=blog.langchain.com)

Furthermore, the marketplace offers Sarah the chance to monetize her application, either through licensing or API sales. As her application gains traction, she receives feedback from the community, leading her back to the LangChain website to iterate and refine her application, ensuring it remains relevant and valuable to its users.

This cyclical process of creation, showcase, feedback, and refinement ensures that the LangChain x DemoGPT ecosystem remains vibrant, innovative, and user-centric.

**The Power of Collaboration: LangChain x DemoGPT**

One of the most exciting prospects of our collaboration is the emergence of the [DemoGPT Marketplace](https://marketplace.demogpt.io/?ref=blog.langchain.com). We envision the DemoGPT Marketplace as a platform where the LangChain community, alongside developers and AI enthusiasts globally, can create, showcase, exchange, and even monetize their auto-generated applications.

This marketplace will be more than just a platform; it will be a vibrant community and a space where LangChain users can collaborate, iterate, and refine applications, ensuring that our ecosystem remains dynamic, user-centric, and on the cutting edge of technological advancements. With the added interactivity and user experience enhancements brought by Streamlit, these applications will promise to be not just functional but truly transformative.

**What’s Next?**

As users craft their unique applications on LangChain, we hope and envision that these innovative creations will find a new home on the [DemoGPT Marketplace](https://marketplace.demogpt.io/?ref=blog.langchain.com). This platform will be set to become a bustling hub where these auto-generated applications are prominently listed and showcased. It will not just be about giving visibility to the applications but also creating a space where a broader audience can discover, interact with, and derive value from these tools.

The vision behind this collaboration is to establish a synergistic ecosystem. By enabling application generation on LangChain and providing a platform for discovery on the DemoGPT Marketplace, we aim to bridge the gap between creators and consumers.

Collaboration between LangChain and DemoGPT can be a really huge step for the LLM world!

We encourage our community to share their feedback, insights, and experiences on[ LangChain Discord channel](https://discord.gg/Hc6QyDYr?ref=blog.langchain.com). Your input is invaluable to us, and it will play a pivotal role in shaping the future of this collaboration.

For more detailed information, advanced configurations, or troubleshooting, you can always refer to the[ DemoGPT GitHub repository](https://github.com/melih-unsal/DemoGPT?ref=blog.langchain.com) or [DemoGPT Marketplace](https://marketplace.demogpt.io/?ref=blog.langchain.com) and consider giving a star.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)