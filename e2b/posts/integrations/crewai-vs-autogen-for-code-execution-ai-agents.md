---
title: "CrewAI vs AutoGen for Code Execution AI Agents"
author: "Tereza Tizkova"
date: "2024-02-16"
url: "https://e2b.dev/blog/crewai-vs-autogen-for-code-execution-ai-agents"
category: "integrations"
site: "e2b"
---

A new paper[ More Agents Is All You Need](https://arxiv.org/abs/2402.05120) finds that, simply via a sampling-and-voting method, the performance of LLMs scales with the number of agents instantiated. This can imply that the popularity of multi-agent frameworks is justified.

CrewAI, also[ called AutoGen 2.0](https://www.toolify.ai/ai-news/developing-autonomous-ai-agents-with-crewai-autogen-20-installation-guide-541783), is a recently popular multi-agent framework. I tested CrewAI and compared it to AutoGen, mainly regarding the LLM-generated code execution capabilities.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529cb_679789a6c7f8c04728e5d332_ZENZwp7yz2lDR8thDShMps2NU.avif)[GitHub stars rating evolution of AutoGen and CrewAI](https://star-history.com/#joaomdmoura/crewAI&microsoft/autogen&Date)

CrewAI is built on top of LangChain and allows one to orchestrate multiple agents working on a user-defined task. Same as[ AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat/), CrewAI is open-source and uses the concept of agents with different roles, but on top of that, CrewAI allows agents to delegate work to each other.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529de_679789c02b9f245c9daef673_aDxmqmhdK3LFo27uR70IOnaroY.avif)Working model of CrewAI agents. [Source](https://github.com/joaomdmoura/crewai)

## Why the hype?

There are several explanations for CrewAI's popularity. It is quick to set up, and works well for a variety of interesting use cases with clear guides and demos, e.g.:

- [Stock Analysis](https://github.com/joaomdmoura/crewAI-examples/tree/main/stock_analysis)
- [Creating Instagram posts](https://www.youtube.com/watch?v=NY97B2jDCo8&ab_channel=MervinPraison)
- [Trip Planner](https://github.com/joaomdmoura/crewAI-examples/tree/main/trip_planner)
- [Landing Page Generator.](https://github.com/joaomdmoura/crewAI-examples/tree/main/landing_page_generator)

## Code execution comparison

### AutoGen

What I like about AutoGen is that it is[ execution-capable](https://microsoft.github.io/autogen/docs/FAQ/#code-execution) of the code output it produces. That is, when I wanted to analyze and visualize a dataset, AutoGen agents generated a code for it, executed the code via Docker, and saved the resulting chart as a PDF file on my computer.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797874f99cf3b77c548221d_679786eb61d6b9b50cd00a5c_i4D0DFLwLMzYJv1b3OQTuBn6QbI.png)](/blog/microsoft-s-autogen)[AutoGen code execution feature used for generating a chart for stock prices](/blog/microsoft-s-autogen)

By default, AutoGen[ currently uses](https://microsoft.github.io/autogen/blog/2024/01/23/Code-execution-in-docker/) Docker containers to execute Python code. They even[ added a Code Interpreter example](https://microsoft.github.io/autogen/blog/2023/11/13/OAI-assistants/) made with a new (experimental) agent called the GPTAssistantAgent that lets you add the new OpenAI assistants into AutoGen-based workflows.

Executing LLM-generated code locally via Docker may be limiting o for some use cases and possesses some risks, but there exists a cloud alternative. In this [open-source code interpreter example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/e2b_autogen), the code produced by AutoGen agents is running in an isolated cloud environment.

### CrewAI

When asked for similar data analysis tasks, CrewAI by default generates a text report. It works well with search tools like[ LangChain DuckDuckGo Search](https://python.langchain.com/docs/integrations/tools/ddg), but to perform more complex data analysis tasks, it would need tools that allow code execution of the LLM-generated code.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529e1_67978a5aa07e8839dae270ce_U2ih06UL8wL1o3PjjR4XSco0y4.avif)Another example of CrewAI performing a stock analysis task. [Source](https://www.youtube.com/watch?v=e0Uj4yWdaAg&ab_channel=BuildNewThings)

I haven’t found a quick way to add such tools, but it still should be possible to integrate them. In some examples, like[ generating a landing page](https://github.com/joaomdmoura/crewAI-examples/tree/main/landing_page_generator), CrewAI uses other (custom) tools, like writing a new file with content.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529d9_67978a6fb8af30bbcbd9ceeb_rMXXkDezcLZqMZ9chXVELughvlU.avif)[Source](https://github.com/crewAIInc/crewAI-examples/blob/main/landing_page_generator/src/landing_page_generator/tools/file_tools.py)

### LangChain tools for code execution

Lang Chain offers several[ Tools](https://python.langchain.com/docs/modules/agents/tools/) where LLM-generated code gets automatically executed.

One example is the[ Pandas Dataframe](https://python.langchain.com/docs/integrations/toolkits/pandas) where a Python agent is used to execute the LLM-generated Python code.

Another example is[ Python REPL](https://python.langchain.com/docs/integrations/tools/python) which can execute Python commands.

There is even one Langchain tool for remote code execution.[ Bearly Code Interpreter](https://python.langchain.com/docs/integrations/tools/bearly) allows safe LLM code execution by evaluating Python code in a sandbox environment. This environment resets on every execution.

Apart from these, users can even build their[ custom Langchain tools](https://python.langchain.com/docs/modules/agents/tools/custom_tools) for code execution and add them to CrewAI.

In conclusion, LangChain tools are able to execute code snippets for example via the Python runtime environment.

### Limitations

Running LLM-generated code can pose a security risk in general. Either because a user asks the LLM to generate malicious code or the LLM generates malicious code accidentally.

Even the official LangChain tool Pandas Dataframe explicitly mentions “This can be bad if the LLM generated Python code is harmful. Use cautiously.”

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529d4_67978a8eb27439aa15e1e5ae_FS5xeuM3mhqLm30WzN6ae9sYgw.avif)[Source](https://python.langchain.com/docs/integrations/toolkits/pandas)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67978b366674fd38c03529d1_67978aa13c863f20b9aec7bb_0XACPN6zz3t2Yw2Zeee9IUbAOQ.avif)[Source](https://python.langchain.com/docs/integrations/tools/python)

LangChain recently[ received feedback](https://github.com/langchain-ai/langchain/discussions/16572) to add a more secure way of running the LLM-generated code, e.g., the same way AutoGen does.

## Conclusion

I can understand the popularity of both AutoGen and CrewAI as they have proven the ability to deliver some interesting and useful examples quickly. While CrewAI is younger than AutoGen, it would be cool to see benchmarks and evals from both frameworks to make it easier for developers to make the right decision when deciding.

I heard from some developers that they chose CrewAI because they were already familiar with LangChain, and others argued that AutoGen is more customizable. However, when discussing with developers, most said that they don’t see a big difference between CrewAI and AutoGen as they accomplish similar tasks.