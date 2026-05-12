---
title: "Microsoft's AutoGen - A guide to code-executing agents"
author: "Tereza Tizkova"
date: "2023-10-08"
url: "https://e2b.dev/blog/microsoft-s-autogen"
category: "announcements"
site: "e2b"
---

After the initial hype around AI agents, there has been a cooling-off period as people realize that **AI agents are not *that *autonomous**. An agent won’t create the whole complex program dreamed up by a no-code user. Usually, until reaching a desired quality, agents' output needs multiple iterations.

These iterations may not be just human-agent, but rather among a higher number of agents specialized in narrow areas. For example, one agent writes a code specified by the end user, another agent then takes over and debugs the code, then hands it to another agent who can visualize the data, and so on. 

[Recently launched](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/) AutoGen by Microsoft has gained especially big popularity among multi-agent [frameworks](https://github.com/e2b-dev/awesome-sdks-for-ai-agents).

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb156_67963723821572b190261c5f_fxNxdn18NHujydYR4S7lznsU.avif)**Fig. 1. **Google trends results for "AutoGen". [Source](https://trends.google.com/trends/explore?date=now%207-d&q=AutoGen&hl=cs)

## Simple Guide to AutoGen

What is special about AutoGen is that it is execution-capable of the code output it produces.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb153_6796374779f5325b8744dbf5_AkmNC9lUnpdDXwKOJiscJ9l0o.avif)**Fig. 2. **The AutoGen paper compares with Multi-agent Debate, CAMEL, BabyAGI, and MetaGPT.

We will hence focus on that feature and create a simple data visualization Python script, where we explore different types of AutoGen pre-defined agent classes, and demonstrate how AutoGen generates and runs code. I hope it helps understand the principles of AutoGen.

[**See the final code in on GitHub**](https://github.com/tizkovatereza/Multi-Agent-Frameworks/blob/main/Autogen.py)

### 1. Install AutoGen

Start with installing AutoGen from their [documentation](https://microsoft.github.io/autogen/docs/Getting-Started) or from [GitHub](https://github.com/microsoft/autogen).

```
`pip install pyautogen
pip install "pyautogen[blendsearch]" for optional dependencies`
```

AutoGen offers good support on their [Discord](https://discord.gg/E5YAjB5gRY), even though I don’t know whether it’s official. It also provides a page with concisely written [Examples](https://microsoft.github.io/autogen/docs/Examples) from which I choose the data analyst one to try.

### 2. Import packages

AutoGen has a default abstract class called [Agent](https://microsoft.github.io/autogen/docs/reference/agentchat/agent) that can communicate with other agents and perform actions. Agents can differ in what actions they perform in the receive method. We import `AssistantAgent` and `UserProxyAgent` classes, which are both subclasses of a more generic class - [ConversableAgent.](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent) (We will get to this later.)

```
`from autogen import AssistantAgent, UserProxyAgent`
```

### 3. Get API Keys

Now, we get our API keys. I store mine as the `.env` variable.

```
`import os
import openai
from dotenv import load_dotenv
load_dotenv()`
```

### 4. Create the agents

In this step, we can define a set of agents with specialized capabilities and roles.

We create an instance of the [`AssistantAgent class`](https://microsoft.github.io/autogen/docs/reference/agentchat/assistant_agent) representing the chatbot that will respond to the user input and an instance of the [`UserProxyAgent class`](https://microsoft.github.io/autogen/docs/reference/agentchat/user_proxy_agent/) representing the user that will initiate the conversation.

The LLM inference configuration in AssistantAgent can be configured via `llm_cofig`.

```
`assistant = AssistantAgent(name="assistant")
user_proxy = UserProxyAgent(name="user_proxy")`
```

### 5. Define the interaction

After creating the agents, the script initiates a chat between the user and the chatbot by calling the `initiate_chat` method on the `user_proxy` instance. The `initiate_chat` method takes two arguments: the assistant instance, which represents the chatbot, and a message string that contains the task description.The script then creates a text completion request using the `openai.Completion.create` method.The `config_list` parameter is set to a list that contains a dictionary with the model name, API base URL, API type, and API key.The prompt parameter is set to a string that contains the text to be completed. The `Completion.create` method sends a request to the OpenAI API and returns a response that contains the completed text.

```
`user_proxy.initiate_chat(
    assistant,
    message="""Hello, today you are my data analyst assistant and you should help me visualize data, make predictions, and explain your thinking.""",
)
response = oai.Completion.create(
    config_list=[
        {
            "model": "chatglm2-6b",
            "api_base": "http://localhost:8000/v1",
            "api_type": "open_ai",
            "api_key": "NULL", # just a placeholder
        }
    ],
    prompt="Hi",
)
print(response)`
```

### 6. Create a chat completion request

Finally, we create a chat completion request using the `openai.ChatCompletion.create` method. The  `config_list` parameter is set to the same list as before, and the messages parameter is set to a list that contains a dictionary with the role and content of the user's message.The `ChatCompletion.create` method sends a request to the OpenAI API and returns a response that contains the chatbot's response to the user's message.

```
`response = oai.ChatCompletion.create(
    config_list=[
        {
            "model": "chatglm2-6b",
            "api_base": "http://localhost:8000/v1",
            "api_type": "open_ai",
            "api_key": "NULL",
        }
    ],
    messages=[{"role": "user", "content": "Hi"}]
)
print(response)
`
```

## Output

As I mentioned earlier, AssistantAgent and UserProxyAgent classes are both subclasses of a more generic class - [ConversableAgent.](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent) 

The [AssistantAgent ](https://microsoft.github.io/autogen/docs/reference/agentchat/assistant_agent)(a subclass of ConversableAgent) is designed to solve a task with LLM. This agent doesn't execute code by default and expects the user to execute the code. After the AssistantAgent produces code output, the user can execute the code by pressing Enter.

I chose my agent to visualize data, which is a task requiring multiple steps like planning the process, writing the code, and executing it in visual form. That should best show its capabilities.

First, the program answers to my default intro message: 

```
`message="""Hello, today you are my data analyst assistant and you should help me visualize data, make predictions, and explain your thinking."""`
```

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb15f_67963857b0176fefe3ce9ae3_ayvDJcL4uOau1yf4W4D5waVtsRI.avif)

I now instruct the agent to plot a chart of NVDA and TESLA stock price change YTD. It then prints user input and devises an action plan - which may include even installing new libraries.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb15c_6796386960c39d88511b0aab_9CPU21DBk2Ks5XNwnMNLU5R2I8.avif)

The agent returned a code that contains an error that is indicated under user_proxy. Here, the user_proxy is used as another agent that provides feedback to the assistant, as opposed to a human instructing the agent with a prompt to fix the code.

The assistant makes another iteration that seems to be functioning code. This was a nice example of [self-healing code](https://stackoverflow.blog/2023/06/07/self-healing-code-is-the-future-of-software-development/).

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb167_6796387e7dda8553d4efdf13_ZSonvgTwOeyBSCsJ3GDzpxyJY.avif)

The following diagram summarizes the workflow of iterating between multiple agents.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb14e_6796388f093cf1f94c3a19cb_i37k1eRXOA3dp0rg9GI80kNms.avif)**Fig. 3. **Schema of the communication between UserProxyAgent and AssistantAgent. [Source](https://microsoft.github.io/autogen/docs/Getting-Started)

## Code execution

The output explains what happens if the user (you) decides to run the code. You can always execute the proposed code by pressing “enter”.

When a human user chooses to execute the code, the output opens in a new window like this:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb159_679638a8b0176fefe3cecfff_3V70uYihSorAXl602mVanKkj5Eo.avif)

It is possible to configure various arguments of the AutoGen agents. It is [open-source](https://github.com/microsoft/autogen), and I like how their [docs](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent/) are structured. 

When modifying the ConversableAgent class, you can change the code_execution_config argument in the [__init__ method](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent#__init__) to even disable the execution of the code.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb162_679638bcd8808eafbbac7c50_EHsgL9oqzfU570auLYldGZGLrmM.avif)**Fig. 4. **Configuring code execution in AutoGen docs. [Source](https://microsoft.github.io/autogen/docs/Getting-Started)

You can also modify the way to execute code blocks, single code blocks, or function calls, by overriding `execute_code_blocks`, `run_code`, `and execute_function` methods respectively.

The code from AutoGen agents is executed locally via `use_docker` - Bool value of whether to use docker to execute the code, or str value of the docker image name to use or None when code execution is disabled.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6796392b99fc75590facb16a_679638dadef1bd0ef6c71d7d_4wsi0wLaoR9ILFzmpjeCdm4neEM.avif)**Fig. 5. **Setting up use_docker in AutoGen docs. [Source](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent)

## Potential limitations

Why would you want to keep a close eye on the execution of the code run locally via Docker? 

As the [Docker security article](https://docs.docker.com/engine/security/) mentions,

*One primary risk with running Docker containers is that the default set of capabilities and mounts given to a container may provide incomplete isolation, either independently, or when used in combination with kernel vulnerabilities.*

Granting autonomous AI tools access to executing code locally may be a challenge, especially for enterprise users. 

#### Alternative solutions may be:

- Another option is using [sandboxed cloud environments](/docs). This provides security for running any code, starting processes, using the filesystem, and so on.

Another challenge with agent frameworks is scalability when the product acquires hundreds or thousands of users each developing their own AI applications, which would require thousands of containers.

This problem is solved for example by using cloud with [E2B SDK](/docs?ref=framer-microsoft-s-autogen).

## AutoGen Use Cases

I found a few examples of how people try AutoGen. It seems like it is still experimenting with the framework mostly for fun purposes, but maybe a time shows whether AutoGen becomes regularly used for work purposes too.

- [Snake Game Development with AutoGen](https://github.com/Poly186-AI-DAO/AutoGen-Snake-Game) - A project structured around a group chat setup where different agents collaborate to bring the snake game to life. [YouTube video](https://www.youtube.com/watch?v=gnn1H4H81IY)
- [Enhanced Agents](https://github.com/Andyinater/AutoGen_EnhancedAgents) - Debuting with a MemoryEnabledAgent with improvements in context/token control, portability, and PnP functionality
- [Scene Writer](https://github.com/abhilashi/ai-explorations/blob/main/ai_scene_writer.py) - A simulation of a fictional scene with AI screenwriters, a couple of assistant agents, and a critique
- [AgentXP](https://twitter.com/oscarmoxon/status/1708603929011863871) - A self-improving agent that is eventually able to write itself
- [Meme creator ](https://colab.research.google.com/github/githubpradeep/notebooks/blob/main/autogen_meme_creator.ipynb)
- [Agentcy](https://github.com/amadad/agentcy) - An example with agents’ roles such as Account Manager, Strategist, Marketer, Researcher, or Designer

## Resources

- [The final code from this example](https://github.com/tizkovatereza/Multi-Agent-Frameworks/blob/main/Autogen.py)
- [Paper: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
- [AutoGen Documentation](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent)
- [GitHub - AutoGen](https://github.com/microsoft/autogen)
- [Docker Documentation - Docker Security](https://docs.docker.com/engine/security/)
- [My tweet about AutoGen](https://x.com/tereza_tizkova/status/1707771482779127923?s=20)
- [AutoGen: Enabling next-generation large language model applications](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/)