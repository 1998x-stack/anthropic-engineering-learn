---
title: "Build LangChain agent with code interpreter"
author: "Tereza Tizkova"
date: "2024-06-13"
url: "https://e2b.dev/blog/build-langchain-agent-with-code-interpreter"
category: "integrations"
site: "e2b"
---

This example shows how to add code interpreting to an LLM using the [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [LangChain](https://www.langchain.com/).

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langchain-python)** **

## Why Code Interpreter SDK

The [E2B Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) quickly creates a secure cloud sandbox powered by [Firecracker](https://github.com/firecracker-microvm/firecracker). Inside this sandbox is a running Jupyter server that the LLM can use.

In general, the Code Interpreter SDK allows you to build custom code interpreters. For example, you can [install custom packages](/docs/sandbox/custom), have access to the internet, [use the filesystem](/docs/sandbox/api/filesystem), or [connect your cloud storage](/docs/guide/connect-bucket).

The Code Interpreter SDK works with [any LLM](https://github.com/e2b-dev/e2b-cookbook/tree/main), in this example, we are using OpenAI's [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo) to plot a sine wave.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c7c266ddfaa2408fdb4f_6797c6b023a9b2a2132ffc11_K1FPr12IZMCTIr7mOKYRr6LoQw.avif)](/docs/code-interpreter/installation)

### Key links

- [Get started with E2B](/docs)
- [Get started with LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)

### Overview

- Install dependencies
- Get API keys, prompt, and tools
- Implement the method for code interpreting
- Implement the methods for formatting messages, create and invoke the LangChain agent
- Run the program

## Setup

### 1. Install dependencies

We start by install the [E2B code interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [LangChain Python SDK](https://console.groq.com/).

```
`pip install e2b-code-interpreter langchain langchainhub langchain-openai`
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

The class `LangchainCodeInterpreterToolInput` defines the input schema for the tool using [Pydantic](https://docs.pydantic.dev/latest/), specifying that the input will be a string of Python code.

```
`import os
import json

from typing import Any, List
from langchain_core.tools import Tool
from pydantic.v1 import BaseModel, Field
from e2b_code_interpreter import CodeInterpreter
from langchain_core.messages import BaseMessage, ToolMessage
from langchain.agents.output_parsers.tools import (
    ToolAgentAction,
)

class LangchainCodeInterpreterToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")`
```

We then create the `CodeInterpreterFunctionTool` class, which handles the code interpreting. The constructor (`__init__` method) initializes the `CodeInterpreter`, which creates a long-running sandbox instance.

Note that at the end of the class definition, we are filtering out the `"results"` key from the `observation` dictionary.  The [`result` object](/docs/code-interpreter/execution) represents the data to be displayed as a result of executing a cell in a Jupyter notebook.

We need to filter it out because, by default, LangChain attaches all LLM-generated output, but the `result` object can contain multiple types of data, such as text, images, plots, etc. represented as a string that would be difficult for the LLM to process and could take a large portion of the context window.

```
`class CodeInterpreterFunctionTool:
    """
    This class calls arbitrary code against a Python Jupyter notebook.
    It requires an E2B_API_KEY to create a sandbox.
    """

    tool_name: str = "code_interpreter"

    def __init__(self):
        # Instantiate the E2B sandbox - this is a long lived object
        # that's pinging E2B cloud to keep the sandbox alive.
        if "E2B_API_KEY" not in os.environ:
            raise Exception(
                "Code Interpreter tool called while E2B_API_KEY environment variable is not set. Please get your E2B api key here https://e2b.dev/docs and set the E2B_API_KEY environment variable."
            )
        self.code_interpreter = CodeInterpreter()

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

    def close(self):
        self.code_interpreter.close()

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
        agent_action: ToolAgentAction,
        observation: dict,
    ) -> List[BaseMessage]:
        """
        Format the output of the CodeInterpreter tool to be returned as a ToolMessage.
        """
        new_messages = list(agent_action.message_log)

        # TODO: Add info about the results for the LLM
        content = json.dumps(
            {k: v for k, v in observation.items() if k not in ("results")}, indent=2
        )
        new_messages.append(
            ToolMessage(content=content, tool_call_id=agent_action.tool_call_id)
        )

        return new_messages`
```

### 4. Implement the methods for formatting messages, create and invoke the LangChain agent

Now we define the `format_to_tool_messages` function to identify for each agent's action whether it corresponds to a specific tool. If it does, the function formats the action and observation into messages and appends them to the `messages` list, ensuring no duplicates.

We create a prompt template that will be used by the agent to generate responses. We define and invoke the agent, during which we specify the prompt, which is to plot and show sinus.

```
`from typing import List, Sequence, Tuple
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnablePassthrough
from langchain.agents.output_parsers.tools import (
    ToolAgentAction,
    ToolsAgentOutputParser,
)

def format_to_tool_messages(
    intermediate_steps: Sequence[Tuple[ToolAgentAction, dict]],
) -> List[BaseMessage]:
    messages = []
    for agent_action, observation in intermediate_steps:
        if agent_action.tool == CodeInterpreterFunctionTool.tool_name:
            new_messages = CodeInterpreterFunctionTool.format_to_tool_message(
                agent_action,
                observation,
            )
            messages.extend([new for new in new_messages if new not in messages])
        else:
            # Handle other tools
            print("Not handling tool: ", agent_action.tool)

    return messages

# 1. Pick your favorite llm
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# 2. Initialize the code interpreter tool
code_interpreter = CodeInterpreterFunctionTool()
code_interpreter_tool = code_interpreter.to_langchain_tool()
tools = [code_interpreter_tool]

# 3. Define the prompt
prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}"), ("placeholder", "{agent_scratchpad}")]
)

# 4. Define the agent
agent = (
    RunnablePassthrough.assign(
        agent_scratchpad=lambda x: format_to_tool_messages(x["intermediate_steps"])
    )
    | prompt
    | llm.bind_tools(tools)
    | ToolsAgentOutputParser()
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True,
)

# 5. Invoke the agent
result = agent_executor.invoke({"input": "plot and show sinus"})

code_interpreter.close()

# Each intermediate step is a Tuple[ToolAgentAction, dict]
result["intermediate_steps"][0][1]["results"][0]`
```

### 5. Run the program

Finally, we run the program. The task given to the agent was to plot and show a sine function.

```
`> Entering new AgentExecutor chain...

Invoking: `code_interpreter` with `{'code': "import matplotlib.pyplot as plt\nimport numpy as np\n\nx = np.linspace(0, 2*np.pi, 100)\ny = np.sin(x)\n\nplt.plot(x, y)\nplt.title('Sine Wave')\nplt.xlabel('x')\nplt.ylabel('sin(x)')\nplt.grid(True)\nplt.show()"}`

***Code Interpreting...
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
====
{'results': [<e2b_code_interpreter.models.Result object at 0x11a267d90>], 'stdout': [], 'stderr': [], 'error': None}Here is a plot of the sine wave.

> Finished chain.`
```

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c7c266ddfaa2408fdb53_6797c782f04dd9889b737f82_kLfBWs6JGdR7Ph7nl6aGgOxcA8o.avif)](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/langchain-python/langchain_code_interpreter.ipynb)

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langchain-python)** **

### Key links

- [Get started with E2B](/docs)
- [Get started with LangChain](https://python.langchain.com/v0.2/docs/introduction/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)