---
title: "AI Data Analyst in Cloud Sandbox with LangChain & E2B"
author: "Tereza Tizkova"
date: "2023-10-25"
url: "https://e2b.dev/blog/build-ai-data-analyst-with-langchain-and-e2b"
category: "integrations"
site: "e2b"
---

We are [E2B](#). We provide sandboxed cloud environments for AI-powered apps and agentic workflows. Check out our [sandbox runtime for LLMs](#).

In this guide, we will create an example of a LangChain agent that uses [E2B cloud sandbox](#) and GPT-4 to analyze your uploaded data.

**See the final guide and code in the official LangChain documentation **[**here**](#)**.**

## Why build your own agent with E2B?

[E2B's cloud environments ](#)are runtime sandboxes for LLMs. They are an ideal fit for building AI assistants like code interpreters or advanced data-analyzing tools. We can use E2B's Data Analysis Sandbox for our use case.

Compared to assistants running their code locally, e.g. via Docker, the Data Analysis Sandbox allows for safe code execution in a remote environment. 

That is a secure way to run the unpredictable LLM-generated code on your computer without the potential harm that such code can cause to your machine, e.g., unauthorized access to vulnerable data.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b968503_67975e935af30dc4ce7f8f40_PRYOg7K6UyUdymWERwaF76Ygbk.avif)

We will create an assistant that will use OpenAI’s GPT-4 and E2B's Data Analysis sandbox to perform analysis on uploaded files using Python.

Let's get to hacking!

### 1. Get API keys, import packages

First, we have to ensure that we have the latest version of E2B.

```
`pip install -U e2b langchain`
```

We import `E2BDataAnalysisTool` and other necessary modules from LangChain. We get our OpenAI API key [here](https://platform.openai.com/account/api-keys), and our E2B API key [here](/docs/getting-started/api-key) and set them as environment variables.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b968500_67975ed843eed349789baa03_TbRGXAYwuZVSZA1iM8euaDT4U.avif)

🔎 Find the full OpenAI API documentation [here](https://openai.com/blog/openai-api).

```
`import os
from langchain.chat_models import ChatOpenAI
from langchain.tools import E2BDataAnalysisTool
from langchain.agents import initialize_agent, AgentType

os.environ["E2B_API_KEY"] = "<E2B_API_KEY>"
os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"`
```

### 2. Initialize the E2B tool for the LangChain agent

💡When creating an instance of the `E2BDataAnalysisTool`, you can pass callbacks to listen to the output of the sandbox. This is useful, for example, when creating a more responsive UI. Especially with the combination of streaming output from LLMs.

We define a Python function save_artifact, which is used to handle and save charts created by Matplotlib.  When a chart is generated with `plt.show()`, this function is called to print a message about the newly generated Matplotlib chart, downloads it as bytes, and then saves it to a directory named "charts."

```
`# Artifacts are charts created by matplotlib when `plt.show()` is called
def save_artifact(artifact):
  print("New matplotlib chart generated:", artifact.name)
  # Download the artifact as `bytes` and leave it up to the user to display them (on frontend, for example)
  file = artifact.download()
  basename = os.path.basename(artifact.name)
  # Save the chart to the `charts` directory
  # Make sure the "charts" directory exists
  with open(f"./charts/{basename}", "wb") as f:
    f.write(file)
e2b_data_analysis_tool = E2BDataAnalysisTool(
    on_stdout=lambda stdout: print("stdout:", stdout),
    on_stderr=lambda stderr: print("stderr:", stderr),
    on_artifact=save_artifact,
)`
```

### 3. Upload your data file

You can choose your own CSV data file to upload to the E2B sandbox. In our example, we chose a file about Netflix TV shows. You can download the file [here](https://storage.googleapis.com/e2b-examples/netflix.csv).

The following code reads a file named "netflix.csv" from the local file system. It then uses the `e2b_data_analysis_tool.upload_file` method to upload the contents of this file to the sandbox and print the path where the file is saved in the sandbox. 

```
`with open("./netflix.csv") as f:
    remote_path = e2b_data_analysis_tool.upload_file(
      file=f,
      description="Data about Netflix tv shows including their title, category, director, release date, casting, age rating, etc.",
    )
    print(remote_path)`
```
**▶️ Code output**
```
`name='netflix.csv' 
remote_path='/home/user/netflix.csv' 
description='Data about Netflix tv shows including their title, category, director, release date, casting, age rating, etc.'`
```

### 4. Create tools and initialize the agent

Now we get to set up the LangChain agent. It will be using GPT-4 and the `e2b_data_analysis_tool` we created earlier.

```
`tools = [e2b_data_analysis_tool.as_tool()]

llm = ChatOpenAI(model="gpt-4", temperature=0)
agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True, handle_parsing_errors=True
)`
```

### 5. Execute a query

We initiate the execution of the agent with a specific query or task.

```
`agent.run(
  "What are the 5 longest movies on netflix released between 2000 and 2010? Create a chart with their lengths."
)`
```
**▶️ Code output**
![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b968511_67975fa8c4bc76ccf25453b6_9auAgWUnitfeFaOXeXuI62ICJBo.avif)

### 6. Sandbox advanced features

E2B also allows you to install both Python and system (via `apt`) packages dynamically during runtime like this:

```
`# Install Python package
e2b_data_analysis_tool.install_python_packages('pandas')`
```
**▶️ Code output**
![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b96850d_67975fd99c28d8133d015e8a_r65nP8g4jfMQ0Aq55p2Rvowoyg0.avif)

Additionally, you can download any file from the sandbox like this:

```
`# The path is a remote path in the sandbox
files_in_bytes = e2b_data_analysis_tool.download_file('/home/user/netflix.csv')`
```

Lastly, you can run any shell command inside the sandbox via `run_command`.

```
`# Install SQLite
e2b_data_analysis_tool.run_command("sudo apt update")
e2b_data_analysis_tool.install_system_packages("sqlite3")
# Check the SQLite version
output = e2b_data_analysis_tool.run_command("sqlite3 --version")
print("version: ", output["stdout"])
print("error: ", output["stderr"])
print("exit code: ", output["exit_code"])`
```
**▶️ Code output**
![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b968506_6797601c0ec4a8f7e08301e0_uyAN9DT7DIc6kOHnEZa9VzXkUI.avif)

### 7. Close the sandbox

When your agent is finished, don't forget to close the sandbox.

```
`e2b_data_analysis_tool.close()`
```

## Output

If you try this example with our [Netflix file](https://storage.googleapis.com/e2b-examples/netflix.csv), the output should be automatically saved into your local directory like this:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797609c127c2e7d0b968509_6797606bc4b68e6acaec701e_8w00rgLIMwaDXCe0dmkWi0lBzws.avif)

**See the final guide and code in the official LangChain documentation **[**here**](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis?ref=build-ai-data-analyst-with-langchain-and-e2b)**. See **[**E2B docs**](/docs)** here.**

- If you like the guide, please support us with a star on [GitHub](https://github.com/e2b-dev/e2b).
- Follow us on [X (Twitter)](https://twitter.com/e2b_dev).
- You can also reach us at [hello@e2b.dev](mailto:hello@e2b.dev).

‍