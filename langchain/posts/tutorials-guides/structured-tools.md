---
title: "Structured Tools"
author: "LangChain Accounts"
date: "2023-05-03"
url: "https://www.langchain.com/blog/structured-tools"
---

Partner

# Structured Tools

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 2, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb226055c6a288ae700b8_photo-1613178594694-5f96ae9b5bb0.jpeg)**TL;DR: we&#x27;re introducing a new abstraction to allow for usage of more complex tools. While previous tools took in a single string input, new tools can take in an arbitrary number of inputs of arbitrary types. We are also introducing a new agent class that works well with these new types of tools.**

**Important Links:**

- [**Tools list**](https://python.langchain.com/docs/modules/agents/tools?ref=blog.langchain.com)
- [**New agent**](https://python.langchain.com/docs/modules/agents/agent_types/structured_chat?ref=blog.langchain.com)

Way back in November 2022 when we first launched LangChain, agent and tool utilization played a central role in our design. We built one of the first chains based on [**ReAct**](https://blog.langchain.com/content/files/abs/2210.xml), a groundbreaking paper that brought tool use to the forefront of prompting frameworks.

In the early days, tool use was simplistic. A model would generate two strings:

- A tool name
- An input string for the chosen tool

This approach confined the agent to one tool per turn, and the input to that tool was restricted to a single string. These limitations were primarily due to the model&#x27;s constraints; models struggled to perform even these basic tasks proficiently. Reliably executing more complex operations, such as selecting multiple tools or populating complex schema, would have been a fool’s errand.

However, the rapid development of more advanced language models like `text-davinci-003`, `gpt-3.5-turbo`, and `gpt-4` has raised the floor of what available models can reliably achieve. This prompted us to reassess the limitations on tool usage within LangChain&#x27;s agent framework.

Earlier this year, we introduced a &quot;multi-action&quot; agent framework, where agents can plan multiple actions to perform on each step of the agent executor. Building on that success, we are now breaking free from the single-string input constraint and proudly offering structured tool support!

Structured tool’s enable more complex, multi-faceted interactions between language models and tools, making it easier to build innovative, adaptable, and powerful applications.

## What is a “Structured Tool”?

A structured tool represents an action an agent can take. It wraps any function you provide to let an agent easily interface with it. A Structured Tool object is defined by its:

- `name`: a label telling the agent which tool to pick. For example, a tool named &quot;GetCurrentWeather&quot; tells the agent that it&#x27;s for finding the current weather.
- `description`: a short instruction manual that explains when and why the agent should use the tool.
- `args_schema`: Communicates the interface of the tool for the agent. It typically draws from the wrapped function&#x27;s signature and permits additional validation logic on tool inputs.
- `_run` and `_arun` functions: These define the tool&#x27;s inner workings. It could be something simple like returning the current time or more complex like sending a message or controlling a robot.

The tool `name` is its unique identifier. A good name unambiguously communicates what it does, so a tool called “GetCurrentWeather” is much more useful than “GCTW” . If a tool’s name isn’t clear to you, it probably isn’t clear to the agent either. If you are giving an agent access to multiple tools, the name could also provide information about their relationship. For instance, if you have “AmazonSearch” and “AmazonCurrentBalance” and “NikeShoppingCart” tools, the agent can infer that the first two are related, even without reading the description.

The `description` provides more detailed directives on how to use the tool. A good description is concise but effectively communicates what the tool does. This can also provide space to provide short examples (or counter examples) if needed.

The `args_schema` is a Pydantic `BaseModel` that defines the arguments (along with their type information) that are to be fed to the tool. It has two main jobs: first, to communicate what information is required from the agent. The second job is to validate those inputs before executing the tool&#x27;s inner functionality.

Finally, the `_run` and accompanying async `_arun` methods define tool’s logic. You can put anything here, from arithmetic, to API requests, to calls to other LLM Chains.

## New Structured Tools

In addition to this new base class, we are releasing the following new tools, both of which inherit from this structured tool class.

- File management - a toolkit for all the filesystem operations you might want, including write, grep, move, copy, list_dir, find
- Web Browser - while we previously had browsers for document loaders, we now are releasing an official stateful PlayWright Browser toolkit that let’s an agent go to websites, click, submit forms, and query data

For a list of all tools (old and new) please see the documentation [here](https://python.langchain.com/docs/modules/agents/tools?ref=blog.langchain.com).

### Implementing your own Structured Tools

The fastest way to get started is by calling the `StructuredTool.from_function(your_callable)` constructor.

As an example, suppose you wanted a tool to interact with Hugging Face models via the `requests` library.

`import requests
from langchain.tools.base import StructuredTool

API_KEY = &quot;&lt;MY-API-KEY&gt;&quot;

def get_huggingface_models(
    path: Optional[str] = None, query_params: Optional[dict] = None
) -&gt; dict:
    &quot;&quot;&quot;Tool that calls GET on &lt;https://huggingface.co/models*&gt; apis. Valid params include &quot;search&quot;:&quot;search&quot;, &quot;author&quot;:&quot;author&quot;, &quot;filter&quot;:&quot;filter&quot; and &quot;sort&quot;:&quot;sort&quot;.&quot;&quot;&quot;
    base_url = &quot;&lt;https://huggingface.co/api/models&gt;&quot;
    headers = {&quot;authorization&quot;: f&quot;Bearer {API_KEY}&quot;}
    result = requests.get(base_url + (path or &quot;&quot;), params=query_params, headers=headers)
    return result.json()

get_huggingface_models_tool = StructuredTool.from_function(get_huggingface_models)
models = get_huggingface_models_tool.run({&quot;query_params&quot;: {&quot;search&quot;: &quot;gpt-j&quot;}})
print(models)
`

Behind the scenes, this infers the `args_schema` from the function’s signature. This is used tell the agent that it can provide query parameters to search as well as a path parameter to call other  child endpoints.

If you want more control over the tool definition,  you can subclass the `BaseTool` directly. For instance, maybe you want the api key to be loaded automatically from the environment variables.

`from typing import Optional, Type

import aiohttp
import requests

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, BaseSettings, Field

class GetHuggingFaceModelsToolSchema(BaseModel):
    path: str = Field(default=&quot;&quot;, description=&quot;the api path&quot;)
    query_params: Optional[dict] = Field(
        default=None, description=&quot;Optional search parameters&quot;
    )

class GetHuggingFaceModelsTool(BaseTool, BaseSettings):
    &quot;&quot;&quot;My custom tool.&quot;&quot;&quot;

    name: str = &quot;get_huggingface_models&quot;
    description: str = &quot;&quot;&quot;Tool that calls GET on &lt;https://huggingface.co/models*&gt; apis. Valid params include &quot;search&quot;:&quot;search&quot;, &quot;author&quot;:&quot;author&quot;, &quot;filter&quot;:&quot;filter&quot; and &quot;sort&quot;:&quot;sort&quot;.&quot;&quot;&quot;
    args_schema: Type[GetHuggingFaceModelsToolSchema] = GetHuggingFaceModelsToolSchema
    base_url: str = &quot;&lt;https://huggingface.co/api/models&gt;&quot;
    api_key: str = Field(..., env=&quot;HUGGINGFACE_API_KEY&quot;)

    @property
    def _headers(self) -&gt; dict:
        return {&quot;authorization&quot;: f&quot;Bearer {self.api_key}&quot;}

    def _run(
        self,
        path: str = &quot;&quot;,
        query_params: Optional[dict] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -&gt; dict:
        &quot;&quot;&quot;Run the tool&quot;&quot;&quot;
        result = requests.get(
            self.base_url + path, params=query_params, headers=self._headers
        )
        return result.json()

    async def _arun(
        self,
        path: str = &quot;&quot;,
        query_params: Optional[dict] = None,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -&gt; dict:
        &quot;&quot;&quot;Run the tool asynchronously.&quot;&quot;&quot;

        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.base_url + path, params=query_params, headers=self._headers
            ) as response:
                return await response.json()

get_models_tool = GetHuggingFaceModelsTool()
models = get_models_tool.run({&quot;query_params&quot;: {&quot;search&quot;: &quot;gpt-j&quot;}})
print(models)
`

## How can I use Structured Tools?

We have added a new `StructuredChatAgent` that works natively with these structured tools. Please see [this page](https://python.langchain.com/docs/modules/agents/agent_types/structured_chat?ref=blog.langchain.com) for a walkthrough.

Due to limitations in the default prompts and output parsers of previous agents, they do not effectively work with structured tools without extra customization.

To get started, you can instantiate the structured chat agent executor using the following code snippet:

`from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatAnthropic
tools = [] # Add any tools here
llm = ChatAnthropic(temperature=0) # or any other LLM
agent_chain = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION)
`

These tools are also compatible with the `AutoGPT` agent from `langchain.experimental`.

## FAQ

**Q: Can I use structured tools with existing agents?**

A: If your structured tool accepts one string argument: **YES**, it will still work with existing agents. However, structured tool with more than one argument are not directly compatible with the following agents without further customization:

- `zero-shot-react-description`
- `react-docstore`
- `self-ask-with-search`
- `conversational-react-description`
- `chat-zero-shot-react-description`
- `chat-conversational-react-description`

**Q: Can I still create string Tools?**

A: You can still use the `Tool` constructor and `@tool` decorators to define simple string tools. Tools that inherit from the `BaseTool` class and accept a single string argument will still be treated as string tools.

**Q: Can I use previously defined string `BaseTool`&#x27;s with new agents built for `StructuredTool`’s**

A:  Yes! Structured tools don’t require new agent executors, and older tools are forwards compatible. The original `Tool` class shares the same base class as the `StructuredTool` , which is another way of saying your tools should work out of the box.

Tools that expect json serialized string inputs may require some modifications to interoperate with the output parser of newer agents, or they can be updated to the new format, which should offer better support for more complex interfaces.

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