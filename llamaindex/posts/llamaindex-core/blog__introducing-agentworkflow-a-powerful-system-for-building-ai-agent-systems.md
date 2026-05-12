---
title: "AgentWorkflow Guide: Build AI Agent Systems | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems"
category: "llamaindex-core"
---

Content



- [ The Challenge of Building Agent Systems  ](#the-challenge-of-building-agent-systems)
- [ Enter AgentWorkflow  ](#enter-agentworkflow)
- [ Getting Started is Simple  ](#getting-started-is-simple)
- [ Building Multi-Agent Systems  ](#building-multi-agent-systems)
- [ Key Features That Make It Powerful  ](#key-features-that-make-it-powerful)
- [ 1. Flexible Agent Types  ](#1-flexible-agent-types)
- [ 2. Built-in State Management  ](#2-built-in-state-management)
- [ 3. Real-time Visibility  ](#3-real-time-visibility)
- [ 4. Human-in-the-Loop Support  ](#4-human-in-the-loop-support)
- [ Ready to build?  ](#ready-to-build)



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



   7



 We&#39;re excited to introduce `AgentWorkflow` , a new system in LlamaIndex that makes it easy to build and orchestrate AI agent systems. `AgentWorkflow`  builds on top of our popular `Workflow`  abstractions to make agents even easier to get up and running. AgentWorkflows take care of coordinating between agents, maintaining state, and more, while still giving you the flexibility and extensibility of Workflows.



 Whether you need a single specialized agent or a team of collaborative agents, `AgentWorkflow`  provides the building blocks to create robust, stateful agent applications.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)



##  The Challenge of Building Agent Systems



 As AI applications grow more sophisticated, simple one-off agent interactions often aren&#39;t enough. Consider building a research assistant that needs to:


-  Search and analyze information from multiple sources
  -  Synthesize findings into a coherent report
  -  Review and refine the content for accuracy
  -  Maintain context across multiple interactions
  -  Handle complex back-and-forth between different specialized components



 Traditional approaches to building such systems often involve:


-  Complex coordination logic between components
  -  Difficulty maintaining state and context
  -  Brittle handoffs between different stages
  -  Limited visibility into the system&#39;s operation



 [After introducing `Workflows`  in LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/workflow/), these types of systems became much easier to build. We even built our own [multi-agent example](https://github.com/run-llama/multi-agent-concierge)! However, we found that there was enough boilerplate code and complexity that we could abstract away to make it easier to build agent systems, while still maintaining the flexibility and power of the `Workflow`  system.



##  Enter AgentWorkflow



 The `AgentWorkflow`  addresses these challenges by providing a structured way to build agent systems that can:


-  Maintain state and context across interaction
  -  Coordinate between specialized agents
  -  Handle complex multi-step processes
  -  Stream and monitor agent activities in real-time



 Built on top of our battle-tested [Workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/), `AgentWorkflow`  makes it easy to create both simple and sophisticated agent systems.



##  Getting Started is Simple



 For basic use cases, you can quickly create a workflow with a single agent:



python






```
workflow = AgentWorkflow.from_tools_or_functions(
    [search_web],
    llm=llm,
    system_prompt=(
        "You are a helpful assistant that can search the web for information."
    )
)

# Run the agent
response = await workflow.run(
    user_msg="What is the latest news about AI?",
)
```


##  Building Multi-Agent Systems

  For more complex scenarios, `AgentWorkflow`  can also be used to build multi-agent systems. Let&#39;s look at how to build a research report system with multiple specialized agents:



python






```
# Create specialized agents
research_agent = FunctionAgent(
    name="ResearchAgent",
    description="Searches and analyzes information from multiple sources",
    system_prompt="You are a thorough researcher...",
    tools=[search_web, record_notes],
    can_handoff_to=["WriteAgent"]
)

write_agent = FunctionAgent(
    name="WriteAgent",
    description="Writes clear, comprehensive reports",
    system_prompt="You are an expert writer...",
    tools=[write_report],
    can_handoff_to=["ReviewAgent", "ResearchAgent"]
)

review_agent = FunctionAgent(
    name="ReviewAgent",
    description="Reviews content for accuracy and quality",
    system_prompt="You are a meticulous reviewer...",
    tools=[review_report],
    can_handoff_to=["WriteAgent"]
)

# Create the workflow
agent_workflow = AgentWorkflow(
    agents=[research_agent, write_agent, review_agent],
    root_agent="ResearchAgent",
    initial_state={
        "research_notes": {},
        "report_draft": "",
        "review_feedback": "",
    }
)
```


##  Key Features That Make It Powerful



###  1. Flexible Agent Types

  Support for different agent architectures to match your needs:


-  `FunctionAgent`  for LLMs with function calling capabilities
  -  `ReActAgent`  for any LLM
  -  Easily extensible for custom agent types



###  2. Built-in State Management



 Maintain context across interactions. Tools/functions in an `AgentWorkflow`  have access to the global workflow Context.



python






```
async def record_notes(ctx: Context, notes: str) -> str:
    """Record research notes for later use."""
    current_state = await ctx.get("state")
    current_state["research_notes"].append(notes)
    await ctx.set("state", current_state)
    return "Notes recorded."
```


###  3. Real-time Visibility

  Monitor the execution process through event streaming:



python






```
handler = workflow.run(user_msg="Research quantum computing")
async for event in handler.stream_events():
    if isinstance(event, AgentInput):
        print(f"Agent {event.current_agent_name}: ")
    if isinstance(event, AgentStream):
        print(f"{event.delta}", end="")
    elif isinstance(event, ToolCallResult):
        print(f"Tool called: {event.tool_name} -> {event.tool_output}")
```


###  4. Human-in-the-Loop Support

  Easily integrate human oversight and input:



python






```
async def get_approval(ctx: Context) -> bool:
    """Request human approval before proceeding."""
    ctx.write_event_to_stream(
        InputRequiredEvent(
            prefix="Please review and approve this section:"
        )
    )
    response = await ctx.wait_for_event(HumanResponseEvent)
    return response.approved
```


##  Ready to build?

  Dive in!


-  Start with our [basic agent workflow tutorial](https://docs.llamaindex.ai/en/stable/examples/agent/agent_workflow_basic/)
  -  Check out the [more detailed documentation](https://docs.llamaindex.ai/en/stable/understanding/agent/multi_agents/)
  -  Explore the [multi-agent research workflow example](https://docs.llamaindex.ai/en/stable/examples/agent/agent_workflow_multi/)
  -  [Join our Discord community](https://discord.com/invite/eN6D2HQ4aX) to discuss your use cases
  -  Check out our [introductory video on YouTube](https://www.youtube.com/watch?v=MmiveeGxfX0)



 Over the coming weeks, we&#39;ll be releasing more examples showing how to use `AgentWorkflow`  for various real-world applications. Stay tuned!