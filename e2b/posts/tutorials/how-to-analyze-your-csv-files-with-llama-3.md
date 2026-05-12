---
title: "How to analyze your CSV files with Llama 3"
author: "Tereza Tizkova"
date: "2024-06-05"
url: "https://e2b.dev/blog/how-to-analyze-your-csv-files-with-llama-3"
category: "tutorials"
site: "e2b"
---

In this guide, we will show how to upload your own CSV file for an AI assistant to analyze. The assistant is powered by [Meta's Llama 3](https://ai.meta.com/blog/meta-llama-3/) and executes its actions in the secure sandboxed environment via the [E2B Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter).

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/upload-dataset-code-interpreter/llama_3_code_interpreter_upload_dataset.ipynb)** **

## Why Code Interpreter SDK

The [E2B Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) quickly creates a secure cloud sandbox powered by [Firecracker](https://github.com/firecracker-microvm/firecracker). Inside this sandbox is a running Jupyter server that the LLM can use.

In general, the Code Interpreter SDK allows you to build custom code interpreters. For example, you can [install custom packages](/docs/sandbox/custom), have access to the internet, [use the filesystem](/docs/sandbox/api/filesystem), or [connect your cloud storage](/docs/guide/connect-bucket). The Code Interpreter SDK works with [any LLM](https://github.com/e2b-dev/e2b-cookbook/tree/main).

### Key links

- [Get started with E2B](/docs)
- [Get started with Llama](https://llama.meta.com/docs/get-started/)
- [Get started with Groq](https://wow.groq.com/docs/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)

### Overview

- Install dependencies
- Get API keys, prompt, and tools
- Implement the method for code interpreting
- Implement the method for calling LLM and parsing tools
- Implement method for uploading dataset to code interpreter sandbox
- Put everything together

## Setup

### 1. Install dependencies

First, we install the [E2B code interpreter SDK](https://github.com/e2b-dev/code-interpreter) and [Groq's Python SDK](https://console.groq.com/).

```
`pip install groq e2b_code_interpreter`
```

### 2. Get API keys, prompt, and tools

Then we store the [Groq](https://console.groq.com/) and [E2B](/docs) API keys and set the model name for the Llama 3 instance we will use. In the system prompt we define the rules for the interaction with Llama. We define our tools - there will be just one tool for executing Python code.

```
`# TODO: Get your Groq AI API key from https://console.groq.com/
GROQ_API_KEY = ""

# TODO: Get your E2B API key from https://e2b.dev/docs
E2B_API_KEY = ""

# Or use 8b version
# MODEL_NAME = "llama3-8b-8192"
MODEL_NAME = "llama3-70b-8192"

SYSTEM_PROMPT = """You're a Python data scientist that is analyzing daily temperature of major cities. You are given tasks to complete and you run python code to solve them.

Information about the the temperature dataset:
- It's in the `/home/user/city_temperature.csv` file
- It has following columns (examples included):
  - `Region`: "North America", "Europe"
  - `Country`: "Iceland"
  - `State`: for example "Texas" but can also be null
  - `City`: "Prague"
  - `Month`: "June"
  - `Day`: 1-31
  - `Year`: 2002
  - `AvgTemperature`: temperature in celsiu, for example 24

Generally you follow these rules:
- the python code runs in jupyter notebook.
- every time you call `execute_python` tool, the python code is executed in a separate cell. it's okay to multiple calls to `execute_python`.
- display visualizations using matplotlib or any other visualization library directly in the notebook. don't worry about saving the visualizations to a file.
- you have access to the internet and can make api requests.
- you also have access to the filesystem and can read/write files.
- you can install any pip package (if it exists) if you need to but the usual packages for data analysis are already preinstalled.
- you can run any python code you want, everything is running in a secure sandbox environment
"""

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

### 3. Implement the method for code interpreting

We define the main function that uses the E2B code interpreter to execute code in a Jupyter Notebook that's running inside the E2B sandbox. We'll be calling this function a little bit further when we're parsing the Llama's response with tool calls.

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

### 4. Implement the method for calling LLM and parsing tools

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

### 5. Implement method for uploading dataset to code interpreter sandbox

The file gets uploaded to the E2B sandbox where our code interpreter is running. We get the file's remote path in the `remote_path` variable.

```
`def upload_dataset(code_interpreter):
  print("Uploading dataset to Code Interpreter sandbox...")
  with open("./city_temperature.csv", "rb") as f:
    remote_path = code_interpreter.upload_file(f)
  print("Uploaded at", remote_path)`
```

### 6. Put everything together

Finally, we put all the pieces together. We instantiate a new code interpreter instance using

`with CodeInterpreter(api_key`**`=`**`E2B_API_KEY) as code_interpreter:`

and then call the `chat_with_llama` method with our user message and the `code_interpreter` instance.

```
`from e2b_code_interpreter import CodeInterpreter

with CodeInterpreter(api_key=E2B_API_KEY) as code_interpreter:

  # Upload the dataset to the code interpreter sandbox
  upload_dataset(code_interpreter)

  code_results = chat_with_llama(
    code_interpreter,
    "Plot average temperature over the years in Algeria"
  )
  if code_results:
    first_result = code_results[0]
  else:
    raise Exception("No code results")

# This will render the image
# You can also access the data directly
# first_result.png
# first_result.jpg
# first_result.pdf
# ...
first_result`
```

```
`Uploading dataset to Code Interpreter sandbox...
Uploaded at /home/user/city_temperature.csv

==================================================
User message: Plot average temperature over the years in Algeria
==================================================
Running code interpreter...`
```

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797c621acfdf2011c05ba58_6797c5ea9813c9b1721a2ccb_Lqg0oBRHtpkTcUaqiCSRlfxY44.avif)](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/upload-dataset-code-interpreter/llama_3_code_interpreter_upload_dataset.ipynb)

🔗 [**Full code on GitHub**](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/upload-dataset-code-interpreter/llama_3_code_interpreter_upload_dataset.ipynb)** **

### Key links

- [Get started with E2B](/docs)
- [Get started with Llama](https://llama.meta.com/docs/get-started/)
- [Get started with Groq](https://wow.groq.com/docs/)
- [Follow E2B](https://twitter.com/e2b_dev?lang=en)