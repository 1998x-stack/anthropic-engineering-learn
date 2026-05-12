---
title: "Command: A new tool for building multi-agent architectures in LangGraph"
author: "LangChain Accounts"
date: "2024-12-10"
url: "https://www.langchain.com/blog/command-a-new-tool-for-multi-agent-architectures-in-langgraph"
---

Company AnnouncementsLangSmithObservability &amp; Evals

# Command: A new tool for building multi-agent architectures in LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 10, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2fde8e41198284b489_Theme-Fractal-Matrix--Format-Blog--Colour-Blue--Text-Alignment-Centred--With-Image-Text-Only.png)Agent and multi-agent systems are all about how the different components of the the system [communicate with each other](https://blog.langchain.com/communication-is-all-you-need/). We spend a lot of time thinking about the best infrastructure and developer experience for facilitating this type of communication. Today, we’re excited to announce `Command`: a new tool in `langgraph` to more easily facilitate multi-actor (or multi-agent) communication.

## Technical Background

Our [agent framework `langgraph`](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) is powered by an event-driven system. We expose a graph-based developer experience heavily influenced by [`NetworkX`](https://networkx.org/?ref=blog.langchain.com), which we&#x27;ve found maps nicely to developer’s mental models of agents. Given the underlying event-driven architecture, we can easily add variants of this graph-based devX.

`langgraph` graphs have traditionally been represented as nodes and edges. This declarative architecture is helpful for mapping an agent’s path to a visual representation. On the flip side, requiring edges to connect nodes can sometimes make it harder or unintuitive to express more dynamic logic. In these situations, you would want nodes to be able to specify dynamically which node to go to next.

## Command: Edgeless graphs

With this in mind, we are excited to release `Command` in LangGraph. This is a special type that when returned from a node specifies not only the update to the state (as usual) but also which node to go to next. This allows nodes to more directly control which nodes are executed after-the-fact.

Usage looks something like this (Python):

`# With type hints, you can specify the possible nodes this can go to.
def agent(state: MessagesState) -&gt; Command[Literal[..., END]]:
    ...
    return Command(
	    goto=...,  # The next node(s) to go to
	    update={&quot;messages&quot;: [response]}  # The update to apply to the state
	  )
`

This can be returned by any node. The type hints on the node can let the graph know which nodes can possibly be executed next. (This allows you to still visualize the graph.)

Read these more technical guides to learn more:

- [Python docs](https://langchain-ai.github.io/langgraph/how-tos/command/?ref=blog.langchain.com)
- [JS docs](https://langchain-ai.github.io/langgraphjs/how-tos/command/?ref=blog.langchain.com)

## Impact on multi-agent flows

One of the primary motivators for this is to more easily allow dynamic multi-agent architectures.

One emerging component of multi-agent architectures is a “handoff”. A handoff involves on agent handing off control to another agent (with or without adding any initial response). OpenAI’s swarm framework actually does this quite well.

The `Command` type lets us perform handoffs easily. We can easily specify any other node in the graph to jump to. As part of this, we can also specify nodes in the **parent** graph to jump to. This allows for better communication and handoffs in hierarchical agent architectures.

For more information on this, see [our conceptual guide on multi-agent architectures](https://langchain-ai.github.io/langgraph/concepts/multi_agent/?ref=blog.langchain.com) which we&#x27;ve updated to reflect our updated thoughts on handoffs. You can also check out our [multiple tutorials on building multi-agent systems with `Command`](https://langchain-ai.github.io/langgraph/tutorials/?ref=blog.langchain.com#multi-agent-systems).

## Conclusion

Building agentic and multi-agent systems is all about communication. As such, our goal is to make `langgraph` the agent framework that gives you the most control over how these agents communicate. We believe that this new `Command` type is an improvement in that direction.

For a video guide of this, see [our walkthrough on YouTube](https://youtu.be/6BJDKf90L9A?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)