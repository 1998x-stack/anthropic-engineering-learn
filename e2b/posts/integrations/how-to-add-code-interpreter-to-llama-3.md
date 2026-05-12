---
title: "How to add code interpreter to Llama 3"
author: "Tereza Tizkova"
date: "2024-04-22"
url: "https://e2b.dev/blog/how-to-add-code-interpreter-to-llama-3"
category: "integrations"
site: "e2b"
---

At this moment, Llama 3 is one of the most capable open-source models. In this guide, we give Llama 3 code interpreter capabilities and test it on data analysis and data visualization task.

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/groq-code-interpreter-python/llama_3_code_interpreter.ipynb)

## Code Interpreter SDK

We will show how to build a code interpreter with Llama 3 on [Groq](https://groq.com/), and powered by** open-source **[**Code Interpreter SDK**](https://github.com/e2b-dev/code-interpreter)** **by E2B.** **The** **E2B Code Interpreter SDK quickly creates a secure cloud sandbox powered by [Firecracker](https://github.com/firecracker-microvm/firecracker). Inside this sandbox is a running Jupyter server that the LLM can use. 

#### Key links

- [Get started with E2B](/docs)
- [Get started with Llama](https://llama.meta.com/docs/get-started/)
- [Get started with Groq](https://wow.groq.com/docs/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)

#### Overview

- Setup
- Configuration and API keys
- Creating code interpreter
- Calling Llama 3
- Connecting Llama 3 and code interpreter

### 1. Setup

We will be working in Jupyter notebook. First, we install the E2B code interpreter SDK and [Groq's Python SDK](https://console.groq.com/).

```
`%pip install groq e2b_code_interpreter`
```

```
`Collecting groq
  Downloading groq-0.5.0-py3-none-any.whl (75 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.0/75.0 kB 937.3 kB/s eta 0:00:00
Collecting e2b_code_interpreter
  Downloading e2b_code_interpreter-0.0.3-py3-none-any.whl (10.0 kB)
Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.10/dist-packages (from groq) (3.7.1)
Requirement already satisfied: distro<2,>=1.7.0 in /usr/lib/python3/dist-packages (from groq) (1.7.0)
Collecting httpx<1,>=0.23.0 (from groq)
  Downloading httpx-0.27.0-py3-none-any.whl (75 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.6/75.6 kB 4.2 MB/s eta 0:00:00
Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from groq) (2.7.0)
Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from groq) (1.3.1)
Requirement already satisfied: typing-extensions<5,>=4.7 in /usr/local/lib/python3.10/dist-packages (from groq) (4.11.0)
Collecting e2b>=0.14.11 (from e2b_code_interpreter)
  Downloading e2b-0.14.14-py3-none-any.whl (100 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.3/100.3 kB 4.8 MB/s eta 0:00:00
Requirement already satisfied: websocket-client<2.0.0,>=1.7.0 in /usr/local/lib/python3.10/dist-packages (from e2b_code_interpreter) (1.7.0)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq) (3.7)
Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.5.0->groq) (1.2.1)
Collecting aenum>=3.1.11 (from e2b>=0.14.11->e2b_code_interpreter)
  Downloading aenum-3.1.15-py3-none-any.whl (137 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 137.6/137.6 kB 2.5 MB/s eta 0:00:00
Requirement already satisfied: aiohttp>=3.8.4 in /usr/local/lib/python3.10/dist-packages (from e2b>=0.14.11->e2b_code_interpreter) (3.9.5)
Collecting jsonrpcclient>=4.0.3 (from e2b>=0.14.11->e2b_code_interpreter)
  Downloading jsonrpcclient-4.0.3-py3-none-any.whl (7.0 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from e2b>=0.14.11->e2b_code_interpreter) (2.8.2)
Requirement already satisfied: requests>=2.31.0 in /usr/local/lib/python3.10/dist-packages (from e2b>=0.14.11->e2b_code_interpreter) (2.31.0)
Requirement already satisfied: urllib3>=1.25.3 in /usr/local/lib/python3.10/dist-packages (from e2b>=0.14.11->e2b_code_interpreter) (2.0.7)
Collecting websockets>=11.0.3 (from e2b>=0.14.11->e2b_code_interpreter)
  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 130.2/130.2 kB 4.2 MB/s eta 0:00:00
Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx<1,>=0.23.0->groq) (2024.2.2)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->groq)
  Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 kB 4.7 MB/s eta 0:00:00
Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->groq)
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 3.9 MB/s eta 0:00:00
Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq) (0.6.0)
Requirement already satisfied: pydantic-core==2.18.1 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1.9.0->groq) (2.18.1)
Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (1.3.1)
Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (23.2.0)
Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (1.4.1)
Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (6.0.5)
Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (1.9.4)
Requirement already satisfied: async-timeout<5.0,>=4.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->e2b>=0.14.11->e2b_code_interpreter) (4.0.3)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->e2b>=0.14.11->e2b_code_interpreter) (1.16.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.31.0->e2b>=0.14.11->e2b_code_interpreter) (3.3.2)
Installing collected packages: aenum, websockets, jsonrpcclient, h11, httpcore, httpx, e2b, groq, e2b_code_interpreter
Successfully installed aenum-3.1.15 e2b-0.14.14 e2b_code_interpreter-0.0.3 groq-0.5.0 h11-0.14.0 httpcore-1.0.5 httpx-0.27.0 jsonrpcclient-4.0.3 websockets-12.0`
```

### 2. Configuration and API keys

Then we store the Groq and E2B API keys and set the model name for the Llama 3 instance you will use. In the system prompt we define sets the rules for the interaction with Llama. 

```
`# TODO: Get your Groq AI API key from https://console.groq.com/
GROQ_API_KEY = ""

# TODO: Get your E2B API key from https://e2b.dev/docs
E2B_API_KEY = ""

# Or use 8b version
# MODEL_NAME = "llama3-8b-8192"
MODEL_NAME = "llama3-70b-8192"

SYSTEM_PROMPT = """you are a python data scientist. you are given tasks to complete and you run python code to solve them.
- the python code runs in jupyter notebook.
- every time you call `execute_python` tool, the python code is executed in a separate cell. it's okay to multiple calls to `execute_python`.
- display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.
- you have access to the internet and can make api requests.
- you also have access to the filesystem and can read/write files.
- you can install any pip package (if it exists) if you need to but the usual packages for data analysis are already preinstalled.
- you can run any python code you want, everything is running in a secure sandbox environment"""

tools = [
  {
    "type": "function",
      "function": {
        "name": "execute_python",
        "description": "Execute python code in a Jupyter notebook cell and returns any result, stdout, stderr, display_data, and error.",
        "parameters": {
          "type": "object",
          "properties": {
            "code": {
              "type": "string",
              "description": "The python code to execute in a single cell.",
            }
          },
          "required": ["code"],
        },
      },
  }
]`
```

### 3. Creating code interpreter

We define the main function that uses the E2B code interpreter to execute code in a Jupyter Notebook cell. We'll be calling this function a little bit further when we're parsing the Llama's response with tool calls.

```
`def code_interpret(e2b_code_interpreter, code):
  print("Running code interpreter...")
  exec = e2b_code_interpreter.notebook.exec_cell(
    code,
    on_stderr=lambda stderr: print("[Code Interpreter]", stderr),
    on_stdout=lambda stdout: print("[Code Interpreter]", stdout),
    # You can also stream code execution results
    # on_result=...
  )

  if exec.error:
    print("[Code Interpreter ERROR]", exec.error)
  else:
    return exec.results`
```

### 4. Calling Llama 3

Now we're going to define and implement `chat_with_llama` method. In this method, we'll call the LLM with our `tools` dictionary, parse the output, and call our `code_interpret` method we defined above.

See the [Groq documentation](https://wow.groq.com/docs/) to get started.

```
`import os
import json
import re
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)

def chat_with_llama(e2b_code_interpreter, user_message):
  print(f"\n{'='*50}\nUser message: {user_message}\n{'='*50}")

  messages = [
      {"role": "system", "content": SYSTEM_PROMPT},
      {"role": "user", "content": user_message}
  ]

  response = client.chat.completions.create(
      model=MODEL_NAME,
      messages=messages,
      tools=tools,
      tool_choice="auto",
      max_tokens=4096,
  )

  response_message = response.choices[0].message
  tool_calls = response_message.tool_calls

  if tool_calls:
    for tool_call in tool_calls:
      function_name = tool_call.function.name
      function_args = json.loads(tool_call.function.arguments)
      if function_name == "execute_python":
        code = function_args["code"]
        code_interpreter_results = code_interpret(e2b_code_interpreter, code)
        return code_interpreter_results
      else:
        raise Exception(f"Unknown tool {function_name}")
  else:
    print(f"(No tool call in model's response) {response_message}")
    return []`
```

### 5. Connecting Llama 3 and code interpreter

Finally, we can instantiate the code interpreter and pass the E2B API key. Then we call the `chat_with_llama` method with our user message and the `code_interpreter` instance.

```
`from e2b_code_interpreter import CodeInterpreter

with CodeInterpreter(api_key=E2B_API_KEY) as code_interpreter:
  code_results = chat_with_llama(
    code_interpreter,
    "Visualize a distribution of height of men based on the latest data you know"
  )
  if code_results:
    first_result = code_results[0]
  else:
    print("No code results")
    exit(0)

# This will render the image
# You can also access the data directly
# first_result.png
# first_result.jpg
# first_result.pdf
# ...
first_result`
```

```
`==================================================
User message: Visualize a distribution of height of men based on the latest data you know
==================================================
Running code interpreter...
`
```

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797aa4a77bc7a713e6e306c_6797aa19af90ed3769671119_gPjhnWqqZfFl3WRSAnXctNf1yPc.avif)

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/groq-code-interpreter-python/llama_3_code_interpreter.ipynb)