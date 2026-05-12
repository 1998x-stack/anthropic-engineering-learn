---
title: "The State of AI Agents"
author: "Tereza Tizkova"
date: "2023-09-07"
url: "https://e2b.dev/blog/the-state-of-ai-agents-reliability-sdks-benchmarking-and-market-trends"
category: "case-studies"
site: "e2b"
---

Here is what we learned about products built on top of agents, their challenges, standardization, and the future.

## 1. The space lacks consensus on the definition of an AI agent

There is still some ambiguity in the terms like "agents", "AI agents", "autonomous agents", or "LLM agents".

We define an agent (using interchangeably with the other variations) similarly to Shawn Wang, aka “Swyx” (founder of [smol ai](https://github.com/smol-ai)), [Matt Schlicht](https://www.mattprd.com/p/the-complete-beginners-guide-to-autonomous-agents) (CEO of Octane AI), and mainly [Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent/) from OpenAI.

AI agents possess three main capabilities.

- They combine reasoning and acting. The agent uses LLMs like GPT-3.5 and GPT-4 to understand, execute, and reflect on tasks.
- They have both short and long-term memory.
- Agents can use "tools" by calling external APIs - for example, it can browse the web, use apps, read and write files, make payments, and even control a user's laptop.

These qualities distinct agents from semi or non-autonomous LLM-powered apps. When compared with “mainstream” automation - where you set up a range of triggers based on data or system states and configure what happens next - AI agents can work in unpredictable environments where there's a lot of new information. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bd0_67962261196323fddadd7252_yDQFjos5NPbHthiHRDibtZE.avif)**Fig. 1. **Overview of an LLM-powered autonomous agent system. [Source](https://lilianweng.github.io/posts/2023-06-23-agent/)

## 2. Agents switch from a standalone product to an “invisible” feature

Defining agents correctly may not be needed soon, as the trend is moving from popular standalone agents, often trying to solve a broad variety of problems at the expense of quality, to agents being just an unmentioned part of a bigger product.

Companies work on agent-powered assistants as an additional feature in existing products. Examples include Hyperwrite AI's [Otherside](https://github.com/e2b-dev/awesome-ai-agents#othersides-ai-assistant), which serves as a personal assistant for daily tasks, [MultiOn](https://multion.ai/), a personal life assistant, and [Deepnote’s AI Copilot](https://deepnote.com/blog/introducing-deepnote-ai). 

We see an increase in the complexity of the agents-centered projects. [Sweep](https://github.com/e2b-dev/awesome-ai-agents#sweep), for instance, is an open-source GitHub assistant with a significant amount of code built around the AI agent. Another example is [Grit.io](https://www.grit.io/) - a tool for automated code migrations and dependency upgrades.

## 3. Agents still have a long way to enterprise-level reliability

The main incentives for enterprises to use agents are saving costs and money. However, they are still hesitant towards agents until they become more reliable.

“For enterprise customers, we are talking at least ~99.9% reliability," thinks David Zhang, the founder of Aomni Agent.

The end users have high standards for fast software, while LLM-powered agents sometimes run slow. Sully Omar, the CEO of Cognosys, [comments](/blog/about-deployment-evaluation-and-testing-of-agents-with-sully-omar-the-ceo-of-cognosys-ai): "In traditional SW engineering, around 200 milliseconds is already considered slow. For agents and LLM apps, latency is a big issue, with LLM calls taking more than 30 seconds."

In general, developers of agents currently struggle with testing, evaluating, debugging, latency, and monitoring. One particular example of a common problem is identifying at what step their agent broke and why.

Another big question that runs through the entire AI industry is that of privacy, security, and data retention policy.

## 4. Agents are in need of specific SDKs and frameworks

Agent developers differ in the paradigms they choose for solving the said challenges. 

They either build on top of existing tools, create their own internal solutions, or adopt some of the products built specifically for agents, many still in an early stage or in alpha/beta version.
Existing “traditional software” solutions

David Zhang, the founder of Aomni, points out how[ a lot of agent developers try to reinvent the wheel](/blog/david-zhang-from-aomni-gives-his-view-agents-reliability-debugging-and-orchestration) with new frameworks and SDKs, instead of building on top of existing technology. 

Developers chose solutions for equivalents of agents’ problems in traditional software, e.g.

- [Inngest](https://www.inngest.com/) for orchestration and debugging of agents
- [Sentry](https://sentry.io/welcome/) for observability
- [LlamaIndex](https://www.llamaindex.ai/) for data integration.

Agent-specific solutions

The traditional software solutions still fail for very agent-specific challenges given by the nature of LLMs. One example is debugging agents, which is essentially playing around with prompts, and the [lack of an agent equivalent of real-time debugging](/blog/david-zhang-from-aomni-gives-his-view-on-ai-agents). 

We have met with developers of agents like [Grit](https://www.grit.io/) or [Sweep](https://sweep.dev/), who are either building their completely custom infrastructure or trying to use existing technologies to at least somehow fit their agent use-case. As [mentioned by Swyx](https://www.latent.space/p/aug-2023), the infrastructure complement to multi-agent systems is agent clouds. E2B has built [AI playgrounds](/docs?ref=framer-the-state-of-ai-agents-reliability-sdks-benchmarking-and-market-trends), sandboxed cloud environments for agents or AI apps, that are especially useful for the coding use-case of agents.

There are more projects tailored for AI agents or LLM apps, most often frameworks for building, monitoring, and analytics.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6be5_67962299d0b90a0fe27dd7b5_BWjLLinQIaN0j7zwHb2z8IH0O8o.avif)**Fig. 2. **Overview of agent-specific SDKs, frameworks, and tools. [Source](https://github.com/e2b-dev/awesome-sdks-for-ai-agents)

## 5. The community is looking for standards for autonomous agents

As we're moving closer and closer to more advanced agents, the [community is having discussions](/blog/agent-protocol-developers-community-setting-a-new-standard) about establishing a common “framework” to help the agent ecosystem grow faster and simplify the work.

Particular questions include how to design realistic benchmarks for better evaluation of agents' performance, and also to incorporate safety considerations. 

### Benchmarking

The [benchmarking effort](https://github.com/Significant-Gravitas/Auto-GPT-Benchmarks) (a benchmarking tool for [Agent Evals](https://github.com/agbenchmark/agent-evals/tree/main)) by AutoGPT originates from a need to truly understand the agent’s ongoing processes and to determine whether the modifications made to an agent genuinely enhance its performance. 

The biggest challenges with designing the agents’ benchmarks are cost, time, and choosing the most optimal design of tests. There is a tradeoff between the diversity and uniqueness of the testing environment versus realism and naturality.

“If an agent fails a simple test, it won’t pass the more difficult ones. Part of the challenge is hence structuring tests in the correct order” said Silen Naihin, an R&D lead at AutoGPT, in the [X space about agents benchmarking](https://twitter.com/TechySwift/status/1689669584683503618?s=20).
Other benchmarking efforts:
- [WebArena](https://webarena.dev/) - A realistic web environment for building agents
- [MACHIAVELLI benchmark](https://aypan17.github.io/machiavelli/) - An environment is based on human-written, text-based Choose-Your-Own-Adventure games containing over half a million scenes with millions of annotations.

### The Agent Protocol

The [Agent Protocol](#), adopted in the AutoGPT [benchmarks](https://github.com/Significant-Gravitas/Auto-GPT-Benchmarks), is a tech stack agnostic way to standardize and hence benchmark and compare AI agents.

It is an OpenAPI specification v3-based protocol - a list of endpoints, which the agent should expose with predefined response models, and defines an interface for interacting with your agent. Developers of LLM apps, such as [AutoGPT, LemonAI, or BabyAGI ](https://github.com/AI-Engineers-Foundation/agent-protocol#open-source-agents-and-projects-that-have-adopted-agent-protocol)are currently adopting the protocol.

The protocol serves as a single communication interface with agents, making it also easier to develop developer tools that work with agents out of the box.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bdc_679622c8196323fddaddb94e_Q5gYGyeeY9U2lW9DBoCwYHfFbUw.avif)**Fig. 3.** Use of the protocol within an AI agent architecture. [Source](https://twitter.com/felixbrockm/status/1691513745036431363)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6be2_679622e225b824ebb53c2758_9U20LlxUzWGBVbm0cdNU9Ac7M.avif)**Fig. 4.** Imprompt AI adding the Agent Protocol as an "external plugin". [Source](https://www.linkedin.com/feed/update/urn:li:activity:7094350987674443776?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7094350987674443776%2C7094386907295465472%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287094386907295465472%2Curn%3Ali%3Aactivity%3A7094350987674443776%29)

## 6. Agents are moving in the vertical direction

The hype where people experimented with the first open-source agent projects like [AutoGPT](https://github.com/e2b-dev/awesome-ai-agents#autogpt) or [BabyAGI](https://github.com/e2b-dev/awesome-ai-agents#babyagi) is starting to gradually calm down. End users are now looking to solve specific problems.

Agent use cases are being narrowed down to achieve perfection in one specific role. Today’s most common use cases are [coding, personal daily tasks, or research](https://github.com/e2b-dev/awesome-ai-agents). 

The future of software will likely include apps powered by dozens of “small” AI agents serving specific purposes and interacting with each other. Agents will need their own secure cloud space to seamlessly communicate and conduct their tasks with autonomy.

We may expect a further shift towards a vertical market, for example, one app with different underlying agents designed for code writing, code debugging, code migration, e-mail communication, calendar planning, and task management.

#### Communication with end users

To increase the ratio of returning users, developers focus on showcasing real tangible results and use cases instead of over-explaining how the agent works and why people should use it.

Sully Omar, the founder of Cognosys AI, enhances, how users care about tangible results, rather than underlying technology. [“For example, offering users different models is redundant if they do not understand which is the most suitable for their needs,”](/blog/about-deployment-evaluation-and-testing-of-agents-with-sully-omar-the-ceo-of-cognosys-ai)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bd3_67962315e6088be835303038_cRDSMzuB8TAPNfw8BE6aLKluv8.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bd9_67962327def1bd0ef6b66c01_tmaOvSfLa8jGrtWz49wMOS2PE0w.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bd6_6796230afb0de8aa9dd60a79_nao4fdzaqOjlmaiL5VWEDiwvM.avif)**Fig. 5, 6, 7.  **Examples of companies avoiding any mention of the underlying agent technology. Source: [Saga AI](https://saga.so/ai), Heymoon.ai, [Lindy.ai](https://www.lindy.ai/)

A famous example of avoiding description of the technology itself is Apple, [not mentioning “AI” at all](https://www.businessinsider.com/why-ai-artificial-intelligence-wasnt-mentioned-apple-wwdc-tim-cook-2023-6) during an important presentation, or not mentioning “metaverse” because[ “the average person doesn't know what it means](https://www.businessinsider.com/tim-cook-apple-avoids-term-metaverse-facebook-2022-10)”.

## Conclusion

Agents still have a long way to enterprise-level reliability. There are still challenges to overcome with [agent-specific SDKs, frameworks, and tools](https://github.com/e2b-dev/awesome-sdks-for-ai-agents). The biggest ones are debugging, monitoring, deployment, and benchmarking of agents. The Agent Protocol is one of the efforts to standardize agents and improve their communication and benchmarking.

The space switches from agents as a standalone code to “agent as a feature”, being part of a more complex product. Agent developers are focusing on more narrow use cases and learning to communicate better with end users.

The most common use cases of agent technology are coding, personal assistance with daily tasks, and search. We see that the future of software includes autonomous LLM agents. 

For trying out autonomous agents, check out the [overview of popular AI agents](https://github.com/e2b-dev/awesome-ai-agents).

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796239428099e7106bf6bdf_67962355196323fddade19a3_h6Lum8N8Gj8kudzC8IWLdvFkpf8.avif)**Fig. 8.** Agents categorized according to open/closed source and main use-case. [Source](https://github.com/e2b-dev/awesome-ai-agents)