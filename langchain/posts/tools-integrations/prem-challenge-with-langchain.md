---
title: "🎉 Prem Challenge🎉"
author: "LangChain Accounts"
date: "2023-06-26"
url: "https://www.langchain.com/blog/prem-challenge-with-langchain"
---

Observability &amp; EvalsAgent Architecture

# 🎉 Prem Challenge🎉

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 26, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d4c0a16b0c1b735cc61a4b_69cf9b384ecc3616c5140df4_langchain--1.webp)We&#x27;re excited to announce a challenge hosted by Prem in collaboration with LangChain.

At LangChain we try to make it easy as possible to experiment with as many different models as possible. That includes the incredible number of emerging open source models. We&#x27;ve made [**efforts**](https://twitter.com/hwchase17/status/1673393425456963611?s=20&amp;ref=blog.langchain.com) to make our framework as suitable as possible for experimentation with open source models. This has already enabled several amazing projects to be built on top of LangChain and open-source models.

We want to see more of these types of projects! Which is why we&#x27;re so excited to be sharing this challenge created by Prem. We&#x27;re also using this as an opportunity to highlight our integration with Prem. Together, we&#x27;re enabling developers to build a new generation of AI applications that leverages LangChain composability and Prem privacy-centric AI model deployments.

### About Prem

Leveraging state-of-the-art Open-Source Large Language Models (LLMs), Prem provides a unified environment to deploy AI models on your infrastructure. Abstracting away all technical complexities for AI deployment and ushering in a new era of privacy-centric AI applications — users can retain control and ownership of their models.

### One-click Integration

All Prem AI services expose APIs in the same way as Open AI does. Using the tools together is as simple as downloading the Prem App and tweaking the URL of your API application to point to the Prem AI services, which operate locally with models of your choice.

If you are used to using LangChain, now you can augment it with Prem. Build AI applications without sensitive data being transferred to any third party.

### The right abstraction

Hosting and deploying open-source models today is a headache. You need to:

- Choose and test the model for your specific use case.
- Serve the model using one of the multiple web frameworks available.
- Package the service for production usage.

Thanks to Prem, we remove all of these pain points with a one-click deployment of models and vector stores. So today, if you are using LangChain with OpenAI and want to point to switch to a self-hosted privacy-preserving solution, all you need to do is to install Prem. Then, because Prem exposes the same API as OpenAI, you can easily use any OpenAI class and just change the `api_base`:

`from langchain.chat_models import ChatOpenAI`

`
chat = ChatOpenAI(openai_api_base=&quot;http://localhost:8111/api/v1&quot;, max_tokens=128)`

### Prem Challenge Overview

Prem Labs aims to foster an ecosystem of privacy-preserving applications. We are excited to announce this challenge to incentivize the developer community to build innovative applications, services, and solutions that put users’ privacy first.

Teams participating in the challenge will leverage Prem to deploy AI models and services on-premise. An important requirement is that the submitted applications shouldn&#x27;t depend on centralized APIs at any point of their stack.

### What

🛠 Teams participating in the challenge will develop Mobile, desktop, or web applications using one or many Prem AI services. Self-hosted AI models provide several benefits, including efficiency, cost optimization, and privacy.

To learn more about the challenge and review some reference implementations, head over to our [**basic tutorial**](https://github.com/premAI-io/challenge-with-langchain/blob/main/README.md?ref=blog.langchain.com) to get up to speed with Prem

### When

📆 26th of June - 10th of July

### Where

🌍 Anywhere, Virtual

### How many?

🚶🚶🚶 Both solo and team accepted. Teams can be up to 4 people.

### Prizes

Judges will shortlist and reward 3 of the best application submitted. 💰Up to $ 10,000+ will be awarded to the final selected projects.

## Submission Requirements

To qualify for the challenge, your application should:

- **Open Source Github Repository** As Prem is open-source from the start. Also, apps and services MUST be open-source in all of their parts.
- **Use Prem Services** From your local machine in development to production remote servers with the same interface, API, and services.
- **Don&#x27;t Log User Data on your server or third parties** No centralized API at any point of the stack! Your users want you to keep your data private!

## Judging Criteria

- **Prompt utilization** We all know open-source models are not there yet, like OpenAI with powerful GPUs at their disposal: from constraints, humans can leverage their creativity to produce unexpected results. Be smart at prompting.
- **Commodity Hardware** If we want to bring the benefits of AI to billions of people in the global south without locking them in the Big Brother sight, we must work around it and make sure anyone can afford to buy computing resources. Run your apps on cheap VPS without GPU or very inexpensive ones.
- **Composability** Combine all Prem services: LLMs, Diffusers, Embedding, and Vector stores.
- **Production Status** How polished is your application? Can my grandma use it?

## **Submission Process**

10th of July **- BEFORE 6 PM UTC** [**google form link**](https://forms.gle/SHpQE1JtdSJAwo9S8?ref=blog.langchain.com)

Show some love to the [**Prem App on Github**](https://github.com/premAI-io/prem-app?ref=blog.langchain.com)

Follow us on Twitter - [**https://twitter.com/premai_io**](https://twitter.com/premai_io?ref=blog.langchain.com)

Join us on Discord - [**https://discord.com/invite/kpKk6vYVAn**](https://discord.com/invite/kpKk6vYVAn?ref=blog.langchain.com)

## Getting Started

### Install Prem

You can run Prem in two different ways:

- MacOS: go to [**https://premai.io**](https://premai.io/?ref=blog.langchain.com) and download Prem App.
- Server: run the installer script: `wget -q &lt;https://get.prem.ninja/install.sh&gt; -O install.sh; sudo bash ./install.sh`

### Run the services in the GUI

When the UI is up and running, you can see all the services available. With just one click you can download the service you are interested in. In the background, the docker image associated with the service will be downloaded based on your hardware requirements.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d4c7f2f39028d27e794253_69d4c33529223a08a21e833a_69cbb20903935dbc92e09409_downloadvicuna.gif)

While waiting for the download to be completed, read more about the service, in the detail view. Just click on the card and you will be redirected to the service page. Each service page is packaged with some general info as well as complete documentation giving more details into the model exposed. When the download has been completed, just click on `Open` and the service will start. You can interact with the service from the playground or from APIs.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d4c7f2f39028d27e79425a_69d4c33529223a08a21e8337_69cbb20903935dbc92e09402_startvicuna.gif)

You can check the port on which the service is running from the service detail view.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d4c7f2f39028d27e794257_69d4c33529223a08a21e833f_69d4c0a06b0c1b735cc61a29_69d4be8385fc1f4427b51f24_runningport-ezgif.com-resize.gif)

### Start Building Your App

Now that the service is running, you can connect to it at [**http://localhost:8111**](http://localhost:8111/?ref=blog.langchain.com) and start building. Here is a simple snippet using LangChain to connect to the service.

`import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

os.environ[&quot;OPENAI_API_KEY&quot;] = &quot;random-string&quot;

chat = ChatOpenAI(openai_api_base=&quot;&lt;http://localhost:8111/api/v1&gt;&quot;, max_tokens=128)

messages = [
    HumanMessage(content=&quot;Can you explain what is a large language model?&quot;)
]
chat(messages)`

Certainly! A large language model is a type of machine learning algorithm that has been trained on a very large dataset of text to learn how to generate human-like language. These models can be used for tasks such as text generation, question answering, and natural language processing. In this project, we will use the Hugging Face Transformers library to train a large language model on a dataset of text and then fine-tune it on a smaller dataset of text related to fashion and beauty.

`messages = [
    HumanMessage(content=&quot;Write me a story about a superstar.&quot;)
]

chat(messages)`

Once upon a time, there was a young woman who had always dreamed of becoming a star. She sang like a bird, danced like a dream, and captivated every audience she performed for with her sheer talent and charm.

When she was just starting out, she worked tirelessly to make her mark on the music industry, taking any opportunity that came her way and honing her skills day by day. Finally, after years of hard work and dedication, she was offered a record deal and shot to fame almost overnight, becoming an instant superstar in the process.

People everywhere were captivated by this talented young woman, who seemed to have it all: the voice, the looks, the style, and the stage presence that left audiences begging for more. She quickly became a household name, known for her infectious smile, her magnetic energy, and the way she made everyone feel like they knew her personally.

As she continued to tour and perform, the superstar began to accumulate an enormous following, with fans from all

**And Done 🎉 You are now using Prem with LangChain.**

### More Information

Check out our documentation at: [**https://github.com/premai-io/prem-app**](https://github.com/premai-io/prem-app?ref=blog.langchain.com)

Check out a simple talk to your data notebook: [**https://github.com/premAI-io/prem-daemon/blob/main/resources/notebooks/talk_to_your_data.ipynb**](https://github.com/premAI-io/prem-daemon/blob/main/resources/notebooks/talk_to_your_data.ipynb?ref=blog.langchain.com)

Check out our YouTube tutorials

- Getting Started with Prem: [**https://www.youtube.com/watch?v=XixH46Ysl5A**](https://www.youtube.com/watch?v=XixH46Ysl5A&amp;ref=blog.langchain.com)
- Deploy Prem in your Paperspace instance: [**https://www.youtube.com/watch?v=aW8t6wouwx0**](https://www.youtube.com/watch?v=aW8t6wouwx0&amp;ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)