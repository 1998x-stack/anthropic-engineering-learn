---
title: "Give LangGraph code execution capabilities"
author: "Tereza Tizkova"
date: "2024-06-17"
url: "https://e2b.dev/blog/langgraph-with-code-interpreter-guide-with-code"
category: "integrations"
site: "e2b"
---

This example shows how to add code interpreting to an LLM using the [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [LangGraph](https://langchain-ai.github.io/langgraph/).

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langgraph-python)** **

## Why Code Interpreter SDK

The [E2B Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) quickly creates a secure cloud sandbox powered by [Firecracker](https://github.com/firecracker-microvm/firecracker). Inside this sandbox is a running Jupyter server that the LLM can use.

In general, the Code Interpreter SDK allows you to build custom code interpreters. For example, you can [install custom packages](/docs/sandbox/custom), have access to the internet, [use the filesystem](/docs/sandbox/api/filesystem), or [connect your cloud storage](/docs/guide/connect-bucket).

The Code Interpreter SDK works with [any LLM](https://github.com/e2b-dev/e2b-cookbook/tree/main), in this example, we are using OpenAI's [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo) to plot a sine wave.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797cb3bfc99e75ad2d26dbe_6797ca1e81743c521cabdf8e_exp.png)](/docs/code-interpreter/installation)

### Key links

- [Get started with E2B](/docs)
- [Get started with LangGraph](https://langchain-ai.github.io/langgraph/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)

### Overview

- Install dependencies
- Get API keys, prompt, and tools
- Implement the method for code interpreting
- Implement the methods for calling tool, create workflow and invoke the LangGraph app
- Run the program

## Setup

### 1. Install dependencies

We start by installing the [E2B code interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [LangChain Python SDK](https://console.groq.com/).

```
`pip install langgraph e2b-code-interpreter langchain langchainhub langchain-openai`
```

### 2. Define API keys, prompt, and tools

Now we store your the [E2B API KEY](/docs/getting-started/api-key) and [OPENAI API KEY](https://platform.openai.com/settings).

```
`import os

# TODO: Get your OpenAI API key from https://platform.openai.com/api-keys
os.environ["OPENAI_API_KEY"] = ""

# TODO: Get your E2B API key from https://e2b.dev/docs
os.environ["E2B_API_KEY"] = ""`
```

### 3. Implement the method for code interpreting

This part includes the tool definition that uses the [E2B Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter). We'll be using this to get the E2B code interpreter tool and to format the output of the tool.

First, we import all necessary libraries.

```
`import os
import json

from typing import Any
from langchain_core.tools import Tool
from pydantic.v1 import BaseModel, Field
from e2b_code_interpreter import CodeInterpreter
from langchain_core.messages import ToolMessage`
```

Then we define classes to allow the LLM use a code interpreter as a tool. The class `LangchainCodeInterpreterToolInput` defines the input schema for the tool using [Pydantic](https://docs.pydantic.dev/latest/), specifying that the input will be a string of Python code.

The class `CodeInterpreterFunctionTool` calls arbitrary code against a Python Jupyter notebook. It requires an `E2B_API_KEY` to create a sandbox.

We define the `format_to_tool_messages` function to identify for each agent's action whether it corresponds to a specific tool.

```
`class RichToolMessage(ToolMessage):
    raw_output: dict

class LangchainCodeInterpreterToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")

class CodeInterpreterFunctionTool:
    tool_name: str = "code_interpreter"

    def __init__(self):
        # Instantiate the E2B sandbox - this is a long lived object
        # that's pinging E2B cloud to keep the sandbox alive.
        if "E2B_API_KEY" not in os.environ:
            raise Exception(
                "Code Interpreter tool called while E2B_API_KEY environment variable is not set. Please get your E2B api key here https://e2b.dev/docs and set the E2B_API_KEY environment variable."
            )
        self.code_interpreter = CodeInterpreter()

    def close(self):
        self.code_interpreter.close()

    def call(self, parameters: dict, **kwargs: Any):
        code = parameters.get("code", "")
        print(f"***Code Interpreting...\n{code}\n====")
        execution = self.code_interpreter.notebook.exec_cell(code)
        return {
            "results": execution.results,
            "stdout": execution.logs.stdout,
            "stderr": execution.logs.stderr,
            "error": execution.error,
        }

    # langchain does not return a dict as a parameter, only a code string
    def langchain_call(self, code: str):
        return self.call({"code": code})

    def to_langchain_tool(self) -> Tool:
        tool = Tool(
            name=self.tool_name,
            description="Execute python code in a Jupyter notebook cell and returns any rich data (eg charts), stdout, stderr, and error.",
            func=self.langchain_call,
        )
        tool.args_schema = LangchainCodeInterpreterToolInput
        return tool

    @staticmethod
    def format_to_tool_message(
        tool_call_id: str,
        output: dict,
    ) -> RichToolMessage:
        """
        Format the output of the CodeInterpreter tool to be returned as a RichToolMessage.
        """

        # TODO: Add info about the results for the LLM
        content = json.dumps(
            {k: v for k, v in output.items() if k not in ("results")}, indent=2
        )

        return RichToolMessage(
            content=content,
            raw_output=output,
            tool_call_id=tool_call_id,
        )`
```

### 4. Implement the methods for calling tool, create workflow and invoke the LangGraph app

Now we define the `format_to_tool_messages` function to identify for each agent's action whether it corresponds to a specific tool. If it does, the function formats the action and observation into messages and appends them to the `messages` list, ensuring no duplicates.

We create a prompt template that will be used by the agent to generate responses. We define and invoke the agent, during which we specify the prompt, which is to plot and show sinus.

```
`from typing import List
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph

# Define the function that determines whether to continue or not
def should_continue(messages) -> str:
    last_message = messages[-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return END
    else:
        return "action"

# Handle tools execution
def execute_tools(messages, tool_map) -> List[RichToolMessage]:
    tool_messages = []
    for tool_call in messages[-1].tool_calls:
        tool = tool_map[tool_call["name"]]
        if tool_call["name"] == CodeInterpreterFunctionTool.tool_name:
            output = tool.invoke(tool_call["args"])
            message = CodeInterpreterFunctionTool.format_to_tool_message(
                tool_call["id"],
                output,
            )
            tool_messages.append(message)
        else:
            content = tool.invoke(tool_call["args"])
            tool_messages.append(RichToolMessage(content, tool_call_id=tool_call["id"]))
    return tool_messages

# 1. Pick your favorite llm
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# 2. Initialize the code interpreter tool
code_interpreter = CodeInterpreterFunctionTool()
code_interpreter_tool = code_interpreter.to_langchain_tool()
tools = [code_interpreter_tool]
tool_map = {tool.name: tool for tool in tools}

# 3. Define the graph
workflow = MessageGraph()
workflow.add_node("agent", llm.bind_tools(tools))
workflow.add_node("action", lambda x: execute_tools(x, tool_map))

# Conditional agent -> action OR agent -> END
workflow.add_conditional_edges(
    "agent",
    should_continue,
)
# Always transition `action` -> `agent`
workflow.add_edge("action", "agent")

workflow.set_entry_point("agent")

app = workflow.compile()

# 4. Invoke the app
result = app.invoke([("human", "plot and show sinus")])

code_interpreter.close()

def display_results(messages):
    for message in result:
        if hasattr(message, 'raw_output'):
            if message.raw_output["results"]:
                rs = message.raw_output["results"]
                for r in rs:
                    display(r)

display_results(result)`
```

### 5. Run the program

Finally, we run the program. The task given to the agent was to plot and show a sine function.

```
`***Code Interpreting...
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
====`
```

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c7c266ddfaa2408fdb53_6797c782f04dd9889b737f82_kLfBWs6JGdR7Ph7nl6aGgOxcA8o.avif)](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/langgraph-python/langgraph_code_interpreter.ipynb)

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langgraph-python)** **

### Key links

- [Get started with E2B](/docs)
- [Get started with LangCraph](https://langchain-ai.github.io/langgraph/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)