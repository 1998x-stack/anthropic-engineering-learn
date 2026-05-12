---
title: "Improving core tool interfaces and docs in LangChain"
author: "LangChain Accounts"
date: "2024-07-18"
url: "https://www.langchain.com/blog/improving-core-tool-interfaces-and-docs-in-langchain"
---

Company AnnouncementsLangChain

# Improving core tool interfaces and docs in LangChain

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 18, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8a3d7d286a58fa7048_Tool-blog---bagatur.png)“[Tools](https://python.langchain.com/v0.2/docs/concepts/?ref=blog.langchain.com#tools)” in the context of LLMs are utilities designed to be called by a model. They have well-defined schemas that can be input to a model and generate outputs that can be fed back to the model. Tools are needed whenever you want a model to control parts of your code or call out to external APIs, making them an essential building block of LLM applications.

Over the past few weeks, we’ve focused on improving our core tool interfaces and documentation. These updates make it easier to:

- Turn any code into a tool
- Pass different types of inputs to tools
- Return complex outputs from tools
- Create more reliable tools using architectures

Let’s dive into these improvements for integrating, using, and managing tools in LangChain below.

## Simplified tool definitions

Tool integration can be complex, often requiring manual effort like writing custom wrappers or interfaces. At LangChain, we’ve reduced complexity starting from tool definition.

- You can now **pass any Python function into `ChatModel.bind_tools()`** , which allows normal Python functions to be used directly as tools. This simplifies how you define tools, as LangChain will just parse type annotations and docstrings to infer required schemas. Below is an example where a model must pull a list of addresses from an input and pass it along into a tool:

`from typing import List
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic

class Address(TypedDict):
    street: str
    city: str
    state: str

def validate_user(user_id: int, addresses: List[Address]) -&gt; bool:
    &quot;&quot;&quot;Validate user using historical addresses.

    Args:
        user_id: (int) the user ID.
        addresses: Previous addresses.
    &quot;&quot;&quot;
    return True

llm = ChatAnthropic(
    model=&quot;claude-3-sonnet-20240229&quot;
).bind_tools([validate_user])

result = llm.invoke(
    &quot;Could you validate user 123? They previously lived at &quot;
    &quot;123 Fake St in Boston MA and 234 Pretend Boulevard in &quot;
    &quot;Houston TX.&quot;
)
result.tool_calls
[{&#x27;name&#x27;: &#x27;validate_user&#x27;,
  &#x27;args&#x27;: {&#x27;user_id&#x27;: 123,
   &#x27;addresses&#x27;: [{&#x27;street&#x27;: &#x27;123 Fake St&#x27;, &#x27;city&#x27;: &#x27;Boston&#x27;, &#x27;state&#x27;: &#x27;MA&#x27;},
    {&#x27;street&#x27;: &#x27;234 Pretend Boulevard&#x27;, &#x27;city&#x27;: &#x27;Houston&#x27;, &#x27;state&#x27;: &#x27;TX&#x27;}]},
  &#x27;id&#x27;: &#x27;toolu_011KnPwWqKuyQ3kMy6McdcYJ&#x27;,
  &#x27;type&#x27;: &#x27;tool_call&#x27;}]
`

The associated [LangSmith trace](https://smith.langchain.com/public/587a1d4c-c065-42f9-8610-43f99e0435ae/r?ref=blog.langchain.com) shows how the tool schema was populated behind the scenes, including the parsing of the function docstring into top-level and parameter-level descriptions.

Learn more about creating tools from functions in our how-to guides for [Python](https://python.langchain.com/v0.2/docs/how_to/custom_tools/?ref=blog.langchain.com#creating-tools-from-functions) and [JavaScript](https://js.langchain.com/v0.2/docs/how_to/custom_tools/?ref=blog.langchain.com).

- **Additionally, any LangChain **[**runnable**](https://python.langchain.com/v0.2/docs/concepts/?ref=blog.langchain.com#runnable-interface)** can now be cast into a tool**, making it easier to re-use existing LangChain runnables, including chains and agents. Reusing existing runnables reduces redundancies and allowing you to deploy new functionality faster. For example, below we equip a LangGraph agent with another “user info agent” as a tool, allowing it to delegate relevant questions to the secondary agent.

`from typing import List, Literal
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI(temperature=0)

user_info_agent = create_react_agent(llm, [validate_user])

class Message(TypedDict):
    role: Literal[&quot;human&quot;]
    content: str

agent_tool = user_info_agent.as_tool(
    arg_types={&quot;messages&quot;: List[Message]},
    name=&quot;user_info_agent&quot;,
    description=&quot;Ask questions about users.&quot;,
)

agent = create_react_agent(llm, [agent_tool])`

See how to use runnables as tools in our [Python](https://python.langchain.com/v0.2/docs/how_to/convert_runnable_to_tool/?ref=blog.langchain.com) and [JavaScript](https://js.langchain.com/v0.2/docs/how_to/convert_runnable_to_tool?ref=blog.langchain.com) docs.

## Flexible tool inputs

Tools must handle diverse inputs coming from varying data sources and user interactions. Validating these inputs can be cumbersome, especially determining which inputs should be generated by the model versus provided by other sources.

- In LangChain, you can now **pass in model-generated ToolCalls directly to tools** (see [Python](https://python.langchain.com/v0.2/docs/concepts/?ref=blog.langchain.com#invoke-with-toolcall), [JS](https://js.langchain.com/v0.2/docs/concepts/?ref=blog.langchain.com#invoke-with-toolcall) docs). While this streamlines executing tools called by a model, there’s also cases where we *don’t* want all inputs to the tool to be generated by the model. For example, if our tool requires some type of user ID, this input will likely come from elsewhere in our code and not from a model. For these cases, we’ve added **annotations** **that specify which tool inputs shouldn’t be generated by the model**. See docs here ([Python](https://python.langchain.com/v0.2/docs/how_to/tool_runtime/?ref=blog.langchain.com), [JS](https://js.langchain.com/v0.2/docs/how_to/tool_runtime/?ref=blog.langchain.com)).
- We’ve also added documentation on how to **pass LangGraph state to tools** in [Python](https://langchain-ai.github.io/langgraph/how-tos/pass-run-time-values-to-tools/?ref=blog.langchain.com) and [JavaScript](https://js.langchain.com/v0.2/docs/how_to/tool_runtime/?ref=blog.langchain.com). We’ve also made it possible for tools to access the `RunnableConfig` object associated with a run. This is useful for parametrizing tool behavior, passing global params through a chain, and accessing metadata like Run IDs — which provide more control over tool management. Read the docs ([Python](https://python.langchain.com/v0.2/docs/how_to/tool_configure/?ref=blog.langchain.com), [JS](https://js.langchain.com/v0.2/docs/how_to/tool_configure?ref=blog.langchain.com)).

## Enriched tool outputs

Enriching your tool outputs with additional data can help you use these outputs in subsequent actions or processes, increasing developer efficiency.

- Tools in LangChain can now **return results needed in downstream components** but that should not be part of the content sent to the model via an `artifact` attribute in ToolMessages. Tools can also return ToolMessages to set the `artifact` themselves, giving developers more control over output management. See docs here ([Python](https://python.langchain.com/v0.2/docs/how_to/tool_artifacts/?ref=blog.langchain.com), [JS](https://js.langchain.com/v0.2/docs/how_to/tool_artifacts/?ref=blog.langchain.com)).
- We’ve also enabled tools to **stream** **custom events**, providing real-time feedback that improves your tools’ usability. See docs here ([Python](https://python.langchain.com/v0.2/docs/how_to/tool_stream_events/?ref=blog.langchain.com), [JS](https://js.langchain.com/v0.2/docs/how_to/tool_stream_events?ref=blog.langchain.com)).

## Robust handling of tool call errors

Tools can fail for various reasons — as a result, implementing fallback mechanisms and learning how to handle these failures gracefully is important to maintaining app stability. To support this, we’ve added:

- Docs for how to use **prompt engineering and fallbacks** to handle tool calling errors ([Python](https://python.langchain.com/v0.2/docs/how_to/tools_error/?ref=blog.langchain.com), [JS](https://js.langchain.com/v0.2/docs/how_to/tools_error?ref=blog.langchain.com)).
- Docs for how to use **flow engineering** in your LangGraph graph to handle tool calling errors ([Python](https://langchain-ai.github.io/langgraph/how-tos/tool-calling-errors?ref=blog.langchain.com), [JS](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling-errors?ref=blog.langchain.com)).

## What’s next

In the coming weeks we’ll continue adding how-to guides and best practices for defining tools and designing tool-using architectures. We’ll also refresh the documentation for our many tool and toolkit integrations. These efforts aim to empower users to maximize the potential of LangChain tools as they build context-aware reasoning applications.

If you haven’t already, check out our docs to learn more about LangChain for [Python](https://python.langchain.com/v0.2/docs/tutorials/?ref=blog.langchain.com) and [JavaScript](https://js.langchain.com/v0.2/docs/tutorials/?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)