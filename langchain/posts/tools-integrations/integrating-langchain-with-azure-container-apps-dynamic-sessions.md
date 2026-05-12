---
title: "Integrating LangChain with Azure Container Apps dynamic sessions"
author: "LangChain Accounts"
date: "2024-05-16"
url: "https://www.langchain.com/blog/integrating-langchain-with-azure-container-apps-dynamic-sessions"
---

PartnerLangChain

# Integrating LangChain with Azure Container Apps dynamic sessions

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 16, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafcfa83bd2fbf57012c0_Azure-container-apps.png)Azure Container Apps dynamic sessions provide a secure, low-latency, reliable Python REPL API. With the new dynamic sessions LangChain integration, you can safely give your LangChain chains and agents the ability to write and execute Python code.

### Relevant Links

- LangChain: [docs](https://python.langchain.com/v0.2/docs/integrations/tools/azure_dynamic_sessions/?ref=blog.langchain.com)
- Azure Container Apps: [docs](https://learn.microsoft.com/en-us/azure/container-apps/sessions-code-interpreter?ref=blog.langchain.com) and [tutorial](https://learn.microsoft.com/en-us/azure/container-apps/sessions-tutorial-langchain?ref=blog.langchain.com)
- LangGraph data analyst: [video](https://www.youtube.com/watch?v=NsVnUz7sp_Y&amp;ref=blog.langchain.com) and [code](https://github.com/langchain-ai/langchain/blob/master/cookbook/azure_container_apps_dynamic_sessions_data_analyst.ipynb?ref=blog.langchain.com)

# The value of code execution

LLMs excel at solving complex problems but, just like human brains, struggle with certain computational tasks.  While these current state-of-the-art models can explain intricate concepts like statistical mechanics, they may not be able to perform tasks like correctly computing the average of 10 floats. However, these models can proficiently write Python code to compute the average of a list of floats.

Just as computers ushered in a new era of human productivity by handling raw computations so that we could focus on defining algorithms and programmatic logic, code execution tools will also enhance LLM agents’ capabilities, leading to higher productivity and performance.

# Azure Container Apps dynamic sessions

Dynamic sessions is a new feature in Azure Container Apps that allows you to run LLM-generated code securely in a sandbox. You can augment the limitations of LLMs with  mathematical computations by running their generated Python code securely in dynamic sessions without any containers’ knowledge needed.

Sessions have the following attributes:

- **Strong isolation**: Sessions are isolated from each other and from the host environment. Each session runs in its own Hyper-V sandbox, providing enterprise-grade security and isolation. Optionally, you can enable network isolation to further enhance security.
- **Fully managed**: The platform fully manages a session&#x27;s lifecycle. Sessions are automatically cleaned up when no longer in use.
- **Fast startup**: A new session is allocated in about 100ms. Rapid start-ups are achieved by automatically maintaining a pool of ready but unallocated sessions.
- **Scalable**: Sessions can run at a high scale. You can run hundreds or thousands of sessions concurrently.
- **Data access**: You can upload files to a Session so that your code can interact with your data.
- **Private**: Files are written in the session&#x27;s file system inside the Hyper-V isolation boundary. They are not accessible directly by default. They can be downloaded using an API.
- **Preinstalled packages**: Sessions comes with many of the most popular packages preinstalled, like NumPy, pandas, and scikit-learn. You can also run `!pip install ...` like in a notebook cell to add more (if egress is enabled).

For full documentation of the sessions API head to the [Azure Container Apps docs](https://learn.microsoft.com/en-us/azure/container-apps/sessions-code-interpreter?tabs=azure-cli&amp;ref=blog.langchain.com).

# Using the LangChain integration

Getting started with the LangChain integration is simple. You can do the following:

- Set up your Azure Container Apps service by following the instructions [here](https://learn.microsoft.com/en-us/azure/container-apps/sessions-code-interpreter?tabs=azure-cli&amp;ref=blog.langchain.com#create-a-session-pool-with-azure-cli). Make sure to get your Sessions pool management endpoint as shown [here](https://learn.microsoft.com/en-us/azure/container-apps/sessions-code-interpreter?tabs=azure-cli&amp;ref=blog.langchain.com#get-the-pool-management-api-endpoint-with-azure-cli).
- Install the required dependencies

`!pip install langchain-azure-dynamic-sessions`

- Import and run

`from langchain_azure_dynamic_sessions import SessionsPythonREPLTool

tool = SessionsPythonREPLTool(
	pool_management_endpoing=&quot;&lt;&lt;Enter Pool Management Endpoint&gt;&gt;&quot;,
)

code = &quot;&quot;&quot;
import numpy as np

print(&quot;sampling 3 datapoints from standard normal distribution&quot;)

np.random.normal(size=3).tolist()
&quot;&quot;&quot;

# To get string output:
print(tool.invoke(code)))`

This will generate a JSON string like:

`&quot;&quot;&quot;{
  &quot;result&quot;: [
    0.34904792009397784,
    -2.237593977256981,
    1.2965825537776963,
  ],
  &quot;stdout&quot;: &quot;sampling 3 datapoints from standard normal distribution&quot;,
  &quot;stderr&quot;: &quot;&quot;
}&quot;&quot;&quot;`

If we want the raw outputs, not at as a string, we can use tool.execute()

`# To get dict output:
tool.execute(code)`

This would return a dictionary with a list of floats for the &quot;result&quot;:

`{
  &quot;result&quot;: [
    0.34904792009397784,
    -2.237593977256981,
    1.2965825537776963,
  ],
  &quot;stdout&quot;: &quot;sampling 3 datapoints from standard normal distribution&quot;,
  &quot;stderr&quot;: &quot;&quot;
}`

Head to the [LangChain docs](https://python.langchain.com/v0.2/docs/integrations/tools/azure_dynamic_sessions/?ref=blog.langchain.com) to see how to upload files to a session, pass model-generated code to the tool, use the tool in an agent, and more.

# Data analyst agent with LangGraph

One of the most exciting use cases for Sessions is building agents that can analyze large datasets using code. In the below walkthrough we show how to build a data analyst agent using LangGraph and dynamic sessions:

Here&#x27;s the link to the agent [code](https://github.com/langchain-ai/langchain/blob/master/cookbook/azure_container_apps_dynamic_sessions_data_analyst.ipynb?ref=blog.langchain.com).

# Conclusion

Code executing tools are indispensable for data analysis and software engineering LLM application. With the new LangChain and Azure Container Apps dynamic sessions integration, you can write and execute Python code safely and with low latency.

Head to the [LangChain docs](https://python.langchain.com/v0.2/docs/integrations/tools/azure_dynamic_sessions/?ref=blog.langchain.com) to get started!

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