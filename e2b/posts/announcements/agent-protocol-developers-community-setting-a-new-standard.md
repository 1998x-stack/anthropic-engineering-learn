---
title: "Agent Protocol: Developers community setting a new standard"
author: "Tereza Tizkova"
date: "2023-08-07"
url: "https://e2b.dev/blog/agent-protocol-developers-community-setting-a-new-standard"
category: "announcements"
site: "e2b"
---

The [agent space](https://github.com/e2b-dev/awesome-ai-agents) is evolving rapidly, with new agents launching every week. They differ in use cases, e.g. coding assistance ([Sweep](https://sweep.dev/), [Clippy,](https://github.com/ennucore/clippy/) [yAgents](https://github.com/yeagerai/yeagerai-agent)), business intelligence ([Aomni](https://www.aomni.com/)), research ([GPT Researche](https://github.com/assafelovic/gpt-researcher)r), and more.  But more importantly, they differ in their architecture and approach toward building the agents.

It is clear that a standardized protocol is essential and has recently been a big subject of [community discussions](https://www.blog.e2b.dev/log/discussed-agent-protocol-with-community). By establishing a common framework, we aim to help the agent [ecosystem](https://www.blog.e2b.dev/log/ai-agents-in-the-wild) grow faster and simplify the work. The need for a standard becomes even more crucial within applications.

Our approach towards the Agent Protocol is starting with a minimal core and iteratively building on it. We are using[ guidance from agent developers](https://www.blog.e2b.dev/log/discussed-agent-protocol-with-community), trying to reflect their needs and lead the Protocol as an open-source community effort towards the gold standard in the agents field.

The development and invention of the Agent Protocol was significantly influenced and spearheaded by E2B's founding engineer - [Jakub Novak](https://www.linkedin.com/in/novak-kuba/). He has served as the lead inventor and code contributor of the project.

## What is The Agent Protocol

The Agent Protocol itself is the most important part. It is defined as an OpenAPI specification of endpoints. 

### Key Components

- Protocol Specification - Central to the Agent Protocol is the OpenAPI specification - a list of endpoints that the agent should expose. Picture it as something that wraps your agent in a web server that allows for communication with your agent (and in between agents in the future). 
- SDK - The SDK wraps your agent within a web server. In enables communication with your agent, and potential inter-agent interactions in the future. The wrap is created to make setting up the protocol super simple and user-friendly, while also making sure there are no limitations.
- Client SDK

The Client SDK allows end users to interact with the agent easily. Thanks to the standard the users can try multiple agents without the need for any additional adjustments (or very minimal) in their code.

## Overcoming agents' challenges

The incentive of adopting the Protocol lies in overcoming current agents’ problems, that are being repeatedly described by their developers. The most common struggles have been the development and debugging of the agent (both in the building phase and production), monitoring, evals, tracing, observability, and deployment of agents. 

The Protocol brings some immediate benefits for solving current challenges.

### Building dev tools for better agents reliability

The agents have a long way to go before agents' reliability starts approaching at least 90%. They have to improve debugging agent prompts, tracing agents’ fails, monitoring the logs, or rerunning certain steps of an agent instance. Not talking about communicating bugs and root causes of problems to end users. 

So far, developers have been working on in-house tools to solve these problems, as well as trying tooling available on the market, but there is no efficient way to make agents enterprise-ready.

On top of the Protocol, developers can build general dev tools for the development, testing, and debugging of agents. They won’t need to write boilerplate API and you can focus on developing their agent.

Moreover, if one person (for example your team member) has started using the protocol, other people should be able to use and integrate other agents more easily, without any additional implementation.

### Benchmarking

Setting a general simple standard that would allow for easy-to-use benchmarking of agents. Another immediate benefit that adopting the Agent Protocol brings is the ease with which you can use the benchmarks. 

### Great developer experience

In general, one of the primary goals of the protocol is a great developer experience and simple implementation on the end of agent developers. You just start your agent and that’s all you have to do.

*Listen to a *[*recording from the Twitter Space *](https://www.blog.e2b.dev/log/discussed-agent-protocol-with-community)*where founders and builders gave their view on the future approach towards agents and discussed the Agent Protocol.*

## Your Input Matters!

At e2b, the community is at the core of our mission. You can find all information about installation and usage in [the official Agent Protocol repo](https://github.com/e2b-dev/agent-protocol).

If you're missing a feature or have a great idea for improvement, or just want to discuss the protocol, don't hesitate to reach out.

Open an issue or reach us at [hello@e2b.dev](mailto:hello@e2b.dev). You can also join AutoGPT discord or E2B discord.