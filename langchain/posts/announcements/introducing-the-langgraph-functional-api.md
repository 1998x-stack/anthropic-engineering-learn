---
title: "Introducing the LangGraph Functional API"
author: "LangChain Accounts"
date: "2025-01-29"
url: "https://www.langchain.com/blog/introducing-the-langgraph-functional-api"
---

Company AnnouncementsLangGraph

# Introducing the LangGraph Functional API

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaJanuary 29, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)7min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae03a657ab2a6d2fcb7c_Theme-Digital-Nebula--Format-YouTube--Colour-Blue--Text-Alignment-Left--With-Image-Image--1-.png)Have you ever wanted to take advantage of LangGraph&#x27;s core features like **human-in-the-loop**, **persistence/memory**, and **streaming** without having to explicitly define a graph?

We&#x27;re excited to announce the release of the **Functional API** for LangGraph, available in [Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com).

The functional API allows you to leverage LangGraph features using a more traditional programming paradigm, making it easier to build AI workflows that incorporate **human-in-the-loop** interactions, **short-term** and **long-term memory**, and **streaming** capabilities.

The **Functional API** consists of two decorators -- `entrypoint` and `task` -- which allow you to define workflows using standard functions, and use regular loops and conditionals to control the flow of execution. This makes it easy to adopt LangGraph&#x27;s features in your existing applications without having to restructure your code.

This API is complementary to the **Graph API** (StateGraph) and can be used in conjunction with it as both APIs use the same underlying runtime. This allows you to mix and match the two paradigms to create complex workflows that leverage the best of both worlds.

In this post, we&#x27;ll see how to leverage LangGraph&#x27;s key features using the **Functional API**.

## Building Blocks

The Functional API uses two primitives to define workflows:

- **Entrypoint**: A starting point for a workflow that encapsulates workflow logic and manages execution flow, including handling long-running **tasks** and interrupts.
- **Task**: A discrete unit of work, such as an API call or data processing step, that can be executed asynchronously from within an **entrypoint**. Invoking a task returns a future-like object, which can be awaited to obtain the result or resolved synchronously.

## Human-in-the-Loop

Imagine you&#x27;re building a content generation app that helps users create essays. Before finalizing the output, your users need to review and approve the draft.

Here’s how it could work: the AI writes a draft, then pauses for user feedback. Once they approve or reject it, the system picks up right where it left off—no need to rerun the whole workflow or wrestle with complex state management.

Without the right tools, you&#x27;d have to build a persistence layer and pipeline logic yourself. But with LangGraph&#x27;s human-in-the-loop features and Functional API, it&#x27;s straightforward. With the `interrupt` function, you can pause the workflow *indefinitely* while waiting for user input. When user input has been collected you can resume using the `Command` primitive, skipping previously completed tasks thanks to task result persistence.

`from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import interrupt

@task
def write_essay(topic: str) -&gt; str:
  &quot;&quot;&quot;Write an essay about the given topic.&quot;&quot;&quot;
  time.sleep(1) # This is a placeholder for a long-running task.
  return f&quot;An essay about topic: {topic}&quot;

@entrypoint(checkpointer=MemorySaver())
def workflow(topic: str) -&gt; dict:
  &quot;&quot;&quot;A simple workflow that writes an essay and asks for a review.&quot;&quot;&quot;
  essay = write_essay(&quot;cat&quot;).result()
  is_approved = interrupt({
    # Any json-serializable payload provided to interrupt as argument.
    # It will be surfaced on the client side as an Interrupt when streaming data
    # from the workflow.
    &quot;essay&quot;: essay, # The essay we want reviewed.
    # We can add any additional information that we need.
    # For example, introduce a key called &quot;action&quot; with some instructions.
    &quot;action&quot;: &quot;Please approve/reject the essay&quot;,
  })

  return {
    &quot;essay&quot;: essay, # The essay that was generated
    &quot;is_approved&quot;: is_approved, # Response from HIL
  }`

An example workflow that writes a draft of an essay and pauses for human review.

**Why this matters**: A human-in-the-loop (or “on-the-loop”) workflow blends human input into automated processes, allowing for review, validation, or corrections where they matter most. This approach is invaluable in LLM-based applications, where occasional inaccuracies can arise. For low-error-tolerance use cases—like compliance, decision-making, or content creation—human involvement ensures reliability by enabling reviews, overrides, or adjustments at critical stages.

- For a more detailed example of the workflow above please review the Functional API docs ([Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com#example) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com#example)).
- For an overview of human-in-the-loop patterns, refer to the conceptual documentation ([Python](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/?ref=blog.langchain.com)).
- For more information about persistence, see: [Python](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com), [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/persistence/?ref=blog.langchain.com).

## Short-term memory

Building a chatbot or conversational agent? You&#x27;ll need short-term memory to keep track of the conversation history — without it, your chatbot can&#x27;t maintain a coherent conversation with a user.

In the Functional API, you can handle short-term memory using:

- `previous` parameter: Automatically gives you the state from the last checkpoint in a conversation thread.
- `entrypoint.final()` type: Lets you return a final value for the workflow and optionally save a different value for the next checkpoint.

`from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint

# Set a checkpointer to enable persistence.
# Additional implementations are available.
checkpointer = MemorySaver()

@entrypoint(checkpointer=checkpointer)
def conversational_agent(user_message, *, previous: Any = None):
    # Initialize messages list from previous state
    messages = previous or []

    # Add the new user message to the conversation history
    messages.append(user_message)

    # Get agent&#x27;s response based on conversation history.
    # Replace with call_llm with actual implementation.
    new_messages = call_llm(messages)

    # Add agent&#x27;s messages to conversation history
    messages.extend(new_messages)

    # Return agent&#x27;s messages as output
    # while saving full conversation history
    return entrypoint.final(value=new_messages, save=messages)`

Example conversational agent implementation

LangGraph&#x27;s built in persistence layer allows you to implement short-term memory that maintains a conversation history and works for multiple users without requiring complex setup or management.

- For more details, please see the how-to guide for adding long term memory (cross-thread persistence) in [Python](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/?ref=blog.langchain.com).
- You can find more conceptual information about memory here: [Python](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/memory/?ref=blog.langchain.com).

## Long-term memory

Some apps, like recommender systems or personal assistants, need to remember user preferences to deliver better experiences. This is called **long-term memory** -- your app learns and adapts over time by storing and updating information about the user across different conversations.

You can implement long-term memory in LangGraph using the `store` parameter in the Functional API. The `store` parameter provides access to a persistent storage layer that can be used to store and retrieve data across different interactions with the same user.

`from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore

# Set a checkpointer to enable persistence.
# Additional implementations are available.
checkpointer = MemorySaver()

# Configure a store for long-term memory.
# Additional implementations are available.
store = InMemoryStore()

@entrypoint(checkpointer=checkpointer, store=store)
def workflow(
    some_input: dict,
    *,
    store: BaseStore
):
    # Use the store for long-term memory operations
    stored_data = store.get(&quot;user_info&quot;)
    # Your workflow will also be able to update the stored data.
    # A common way to do this is by having an LLM invoke tool calls that
    # update the stored data based on the conversation, user input, etc.

`

A workflow can use LangGraph&#x27;s BaseStore interface to implement long-term memory.

- For more details, please see the how-to guide for adding long term memory (cross-thread persistence) in [Python](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/?ref=blog.langchain.com).
- You can find more conceptual information about memory here: [Python](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/memory/?ref=blog.langchain.com).

## Streaming

Building a responsive app for end-users? Real-time updates are key to keeping users engaged as your app progresses.

There are three main types of data you’ll want to stream:

- Workflow progress (e.g., &quot;Task 1 completed&quot;).
- LLM tokens as they’re generated.
- Custom updates (e.g., &quot;Fetched 10/100 records&quot;).

LangGraph makes this easy with built-in streaming support. When you define an entrypoint, you get a `stream` method to send real-time data. It returns a generator, so you can yield updates as they happen. You can subscribe to different streams using the stream_mode argument, subscribing to workflow progress (`updates`), LLM tokens (`messages`), or custom data (`custom`).

`from langgraph.func import entrypoint
from langgraph.types import StreamWriter

@entrypoint(checkpointer=checkpointer)
def workflow(inputs, writer: StreamWriter):
  writer(&quot;Processing started&quot;)  # Write to custom stream
  # Do stuff (e.g., call tasks, call llms)
  writer(&quot;Processing completed&quot;)
  return result

# Consume the stream
for chunk in main.stream(input_data, stream_mode=[&quot;custom&quot;, &quot;updates&quot;, &quot;messages&quot;], config=config):
  print(chunk)

`

- You can find more conceptual information about streaming here: [Python](https://langchain-ai.github.io/langgraph/concepts/streaming/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/streaming/?ref=blog.langchain.com).

## Observability

The Functional API provides built-in observability features to monitor and debug workflows. The inputs and outputs into **entrypoints** and tasks can be logged to [LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com), LangChain&#x27;s observability platform. This allows you to track the progress of workflows, identify bottlenecks, and troubleshoot issues and improve your workflows.

## Deployment

If you’ve created a workflow using **entrypoint **you can deploy it to production using [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com).

## Graph API vs. Functional API

The **Functional API** and the **Graph APIs** (StateGraph) provide two different paradigms to create in LangGraph. Here are some key differences:

- **Control flow:** The **Functional API** does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write for control flow.
- **State management:** The **Graph API** requires declaring a State and may require defining reducers to manage updates to the graph state. **entrypoints** and **tasks** do not require explicit state management as their state is scoped to the function and is not shared across functions.
- **Time-travel:** In the **Graph API** checkpoints are more granular being generated after every node execution (or group of nodes if some nodes are being executed in parallel). In the **Functional API** checkpoints are generated after every **entrypoint** execution. When tasks are executed they update the existing checkpoint associated with the **entrypoint**, but it does not generate a new checkpoint. As a result, **time-travel** is better supported in the **Graph API**.
- **Visualization:** The **Graph API** makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The **Functional API** does not support visualization since the execution flow is dynamically generated at run time.

Because the both the **Functional API** and **Graph API** use the same underlying run time, you can mix and match them in the same project. For example, you can call a graph from an entrypoint, or you can use tasks from within a graph etc.

## Conclusion

The **Functional API** in **LangGraph** provides a flexible approach to building AI workflows, with powerful features like **human-in-the-loop interactions**, **state management**, **persistence**, and **streaming**. These capabilities enable developers to create sophisticated applications that effectively combine automation with human input.

📘** Ready to get started?** Check out the Functional API documentation for [Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com).

🎥 We&#x27;ve also prepared [this YouTube video](https://www.youtube.com/watch?v=NXhyWJozM8A&amp;ref=blog.langchain.com) that covers the Functional API for Python.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)