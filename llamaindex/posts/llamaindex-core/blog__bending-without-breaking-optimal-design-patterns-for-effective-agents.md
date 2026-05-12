---
title: "Agent Design Patterns: Workflows And Autonomy Tips | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/bending-without-breaking-optimal-design-patterns-for-effective-agents"
category: "llamaindex-core"
---

Content



- [ Workflows: the core of agentic systems in LlamaIndex  ](#workflows-the-core-of-agentic-systems-in-llamaindex)
- [ Blending autonomy and structure  ](#blending-autonomy-and-structure)
- [ Optimizing agent design  ](#optimizing-agent-design)
- [ When to define structure  ](#when-to-define-structure)
- [ When to provide autonomy  ](#when-to-provide-autonomy)
- [ Agentic patterns are the future  ](#agentic-patterns-are-the-future)



 Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







 There has been a lot of productive dialogue recently about what agents are, and the best way to build them. It was arguably kicked off last December when [Anthropic](https://www.anthropic.com/) published [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), an almost universally well-received guide to the basic patterns underlying agentic software, as well as thoughts about when to apply them. Three weeks ago, [Dexter Horthy](https://www.linkedin.com/in/dexterihorthy/) went viral with his [12 Factor Agents](https://github.com/humanlayer/12-factor-agents), a thoughtful list of design principles to use when building agents. Then a few days ago [OpenAI](https://openai.com/) released [A Practical Guide To Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), which summarized their own thoughts on the same topic. All three are insightful reads.



 We’ve been asked by open source users and enterprise customers for our own takes on these principles. We find ourselves happily in agreement with much of what’s been written, drawing on our own direct experience of building complex agentic systems like [LlamaParse](https://www.llamaindex.ai/enterprise) as well as from working with our many enterprise customers and hundreds of thousands of open source users. We thought it would be useful to share what we’ve learned.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  Workflows: the core of agentic systems in LlamaIndex



 To understand how we think about designing agentic systems it’s worth first understanding Workflows, our system that exists in both our [Python](https://docs.llamaindex.ai/en/stable/understanding/workflows/) and [TypeScript](https://ts.llamaindex.ai/docs/llamaflow) frameworks to orchestrate agentic execution (OpenAI’s guide coincidentally refers to agent execution paths as “workflows” throughout, so we guess it’s a pretty good name!).



 Workflows are an event-based system that allows you to connect a series of execution steps implemented as vanilla functions, connected by emitting events that carry data and trigger execution of other steps. This system is fundamentally simple but powerful, allowing you to easily design chains, branches, loops, fan-outs and collections, including all of the [design patterns](https://www.anthropic.com/engineering/building-effective-agents#building-blocks-workflows-and-agents) mentioned by Anthropic in their post. (We recently released a [tutorial showing how to implement each pattern](https://www.youtube.com/watch?v=Dh9iJjM0mKE).)

  ![](https://cdn.sanity.io/images/7m9jw85w/production/5fab4f000d36bd85e8d42fceead220ca4118f58f-782x684.png) A visualization of a LlamaIndex workflow showing branching, looping and parallelization.

 Workflows allow the implementation of agents as well as the use of sub-agents within each step. Decisions about control flow can be made by LLMs, via traditional imperative programming, or any combination of the two. Workflows have been well-received by our community and are increasingly fundamental to how software is written in LlamaIndex.



##  Blending autonomy and structure



 The core insight behind the design of Workflows is one mentioned by all three of the posts: there exists a tension between a fully autonomous agent, which is given a goal and a set of tools and is allowed to figure out the path to the goal entirely on its own, and a more rigid structure such as a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) in which every step is precisely defined. All three posts agree that successful agentic software lies somewhere between these two extremes.



 This specific section of OpenAI’s Practical Guide was widely shared on social media:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/c1ab3dd538a475caed0c5c93b12505c76c7fa76f-1454x566.png)

 This is why Workflows work the way they do: we experimented with more rigid, graph-based approaches and came away dissatisfied. Instead, Workflows provide optimized, imperative paths when appropriate while leaving LLMs free to work their magic. We see **six key benefits** to the hybrid pattern embodied by Workflows:


-  Better reliability through predictable execution paths for critical operations
  -  Clearer error handling and recovery mechanisms
  -  Easier debugging and tracing of agent behavior
  -  Improved performance through optimized pathways for known scenarios
  -  Maintaining autonomy where it provides value
  -  First-class support for human oversight via human-in-the-loop



##  Optimizing agent design



 Of course, declaring that the best pattern for an agent is a hybrid is easy if you don’t have to define exactly when structure makes sense versus when to opt for autonomy. It remains a tricky question, but we have some basic guidelines and examples to help:



###  When to define structure




      Situation
      Example




      Well-understood processes
      Accepting a sequence of user inputs: you know exactly what fields are required, and a deterministic approach provides a better, more predictable user experience.


      Critical business logic
      Creating a billing event: an irreversible, expensive operation (in both financial terms and in terms of time if it needs to be reversed) where you need to be 100% certain of who is being billed for what and when.


      Error-prone operations
      “Close call” decisions: when making a decision about whether to issue a refund, a variety of human factors come into play. This is a perfect opportunity for human-in-the-loop involvement to avoid customer service disasters.


      Structured output
      When the output of your system needs to be consumed by another, downstream system, it makes sense to constrain the output to precise output formats.



###  When to provide autonomy




      Situation
      Example




      Unstructured inputs
      The most obvious use case for LLM autonomy is handling unstructured and semi-structured data: contracts, invoices, emails, customer service queries. LLMs can make decisions about unstructured data without needing to implement a thousand regular expressions.


      Flexible rule sets
      Traditional, imperative automation can create enormous, inflexible decision trees that still fail to capture edge cases. LLMs, given rough priorities and an overall goal, are great at handling edge cases in the way that a human would.


      Handling novel situations
      Event-based systems are particularly good at situations where it is necessary to “jump track” from one situation to another in response to new information, such as in customer service interactions where the customer is not sure exactly what they want.



##  Agentic patterns are the future



 We agree with all three authors that a pragmatic approach to agent design is the best one: use structure where it helps, provide autonomy where it shines. We think Workflows are the best option in the current marketplace of frameworks to easily implement such hybrid systems, and we encourage you to try them today! Of course, we also offer [LlamaParse](https://cloud.llamaindex.ai/), our enterprise platform with pre-built agentic solutions to common enterprise use-cases, complete with engineering assistance to get your system off the ground.







 Some resources to help you get started:


-  Python resources:
 Text: [Workflows tutorial](https://docs.llamaindex.ai/en/stable/understanding/workflows/)
  -  Video: [Implementing agentic and multi-agent systems](https://www.youtube.com/watch?v=AxW8gIQ-z5Y)

    -  TypeScript resources:
 Text: [Workflows tutorial](https://ts.llamaindex.ai/docs/llamaflow)
  -  Video: [Knowledge-augmented agents with LlamaIndex.TS](http://llamaindex.ts)

    -  [LlamaParse documentation](https://docs.cloud.llamaindex.ai/)