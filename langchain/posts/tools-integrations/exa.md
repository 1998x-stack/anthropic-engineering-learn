---
title: "How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith"
author: "LangChain Accounts"
date: "2025-07-01"
url: "https://www.langchain.com/blog/exa"
---

Case StudiesAgent Architecture

# How Exa built a Web Research Multi-Agent System with LangGraph and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 30, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaaabbf847dfe35ef4841_Exa.png)[Exa](https://exa.ai/?ref=blog.langchain.com), known for their high-quality search API, recently launched their most ambitious product yet: a deep research agent that can autonomously explore the web until it finds the structured information users need.

This case study explores how Exa&#x27;s engineering team leveraged LangGraph to build a production-ready multi-agent system that processes hundreds of research queries daily, delivering structured results in 15 seconds to 3 minutes, depending on complexity.

## The evolution to agentic search

Exa didn&#x27;t begin with agentic search, but evolved into it. The company started with a search API, then progressed to an answers endpoint that combined LLM reasoning with search results. Finally, they&#x27;ve now arrived at their deep research agent: their first truly agentic search API.

This reflects a broader trend across the industry: LLM applications are becoming more agentic and long-running over time. For example, we see this in research-related tasks –  where what started as RAG has evolved into Deep Research. We see this in coding as well, shifting from simple auto-complete to question-answering, and now to asynchronous, long-running coding agents.

This evolution is also reshaping how teams think about and utilize frameworks and tools. We&#x27;ve long been close partners with the Exa team via a [popular open-source integration](https://python.langchain.com/docs/integrations/tools/exa_search/?ref=blog.langchain.com), but hadn&#x27;t collaborated with them on a product until now. Their original answers endpoint didn&#x27;t rely on framework, but as they transitioned to a more complex deep-research architecture, they reevaluated their options and chose to use LangGraph. This again mimics a common trend we see — as architectures get more complex, LangGraph increasingly becomes the framework of choice for building systems.

## Multi-agent architecture design

Exa&#x27;s research agent follows a sophisticated multi-agent pattern built entirely on LangGraph:

- **Planner**: Analyzes the research query and dynamically generates multiple parallel tasks
- **Tasks**: Independent research units that can use specialized tools and reasoning
- **Observer**: Maintains full context across all planning, reasoning, outputs, and citations

A key insight in Exa&#x27;s architecture is its intentional context engineering. While the observer maintains full visibility across all components, individual tasks only receive the final cleaned outputs from other tasks, not intermediate reasoning states.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaaabbf847dfe35ef4847_Diagram.png)

Unlike rigid workflows, Exa&#x27;s system dynamically adjusts the number of research tasks to spin up based on the complexity of the query. Each task receives:

- Specific task instructions
- A required output format (always JSON schema)
- Access to specialized Exa API tools

This flexibility allows the system to scale from simple single-task queries to complex, multi-faceted research requiring numerous parallel investigations.

## Evolving the agent blueprint

Many of Exa&#x27;s design choices mirror those in the [Anthropic Deep Research system](https://www.anthropic.com/engineering/built-multi-agent-research-system?ref=blog.langchain.com). This is intentional. Like us, the Exa team read that blog post, thought it was fantastic, and drew many learnings from it.

Here are a few key of their insights and decisions that build on top of those learnings:

### Search Snippets vs Full Results

One of the most interesting examples of context engineering in Exa&#x27;s system is how it handles search content. Rather than automatically crawling full page content, the system first attempts reasoning on search snippets.

This approach significantly reduces token usage while preserving research quality, as the agent only requests full content when snippet-level reasoning proves insufficient. This ability to swap between search snippets and full results is powered by the Exa API.

### Structured Output

Unlike many research systems that produce unstructured reports, Exa&#x27;s agent maintains structured JSON output at every level. The output format can be specified at runtime.

This design choice was driven by how Exa expects the agent to be used. Unlike consumer-facing research tools, they designed their system specifically for API consumption. When being used as an API, having a reliable output format is more critical. This structured output is generated via function calling.

## Gaining observability with LangSmith

For Exa, one of the most critical LangSmith features was observability, especially around token usage.

> &quot;The observability – understanding the token usage – that LangSmith provided was really important. It was also super easy to set up.&quot; – Mark Pekala, Software Engineer at Exa.

This visibility into token consumption, caching rates, and reasoning token usage proved essential for informing Exa&#x27;s production pricing models and ensuring cost-effective performance at scale.

## Conclusion

Exa&#x27;s deep research agent demonstrates how LangGraph enables sophisticated multi-agent systems in production. By leveraging LangGraph&#x27;s coordination capabilities and LangSmith&#x27;s observability features, Exa built a system that processes real customer queries with impressive speed and reliability.

The key takeaways for teams building similar systems:

- **Start with observability**: Token tracking and system visibility are critical for production deployment
- **Design for reusability**: Well-architected agent flows can power multiple products
- **Prioritize structured output**: API consumers need reliable, parseable results
- **Dynamic task generation**: Flexible task creation scales better than rigid workflows

As the agent ecosystem continues to evolve, Exa&#x27;s implementation provides a compelling example of how to build production-ready agentic systems that deliver real business value.

*To learn more about building multi-agent systems with LangGraph, visit our documentation at *[*langchain-ai.github.io/langgraph*](https://langchain-ai.github.io/langgraph?ref=blog.langchain.com)*. To try Exa&#x27;s deep research API, visit *[*exa.ai*](https://exa.ai/?ref=blog.langchain.com)*.*

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)