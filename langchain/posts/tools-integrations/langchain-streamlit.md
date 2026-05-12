---
title: "LangChain 🤝 Streamlit"
author: "LangChain Accounts"
date: "2023-07-11"
url: "https://www.langchain.com/blog/langchain-streamlit"
---

Agent ArchitecturePartner

# LangChain 🤝 Streamlit

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 11, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb207ba9d0fc723780a64_langchain-and-streamlit.svg)**Editor&#x27;s Note: This post was written in collaboration with the Streamlit team. From the beginning, Streamlit has been a fantastic tool for LangChain developers. In fact, **[**one of the first examples**](https://github.com/hwchase17/notion-qa?ref=blog.langchain.com)** we released used Streamlit as the UI. It has been a honor to have the opportunity to work more closely with the team over the past months, and we&#x27;re thrilled to share some of the stuff we&#x27;ve been working on and thinking about.**

Today, we&#x27;re excited to announce the initial integration of Streamlit with LangChain and share our plans and ideas for future integrations.

The LangChain and Streamlit teams had previously [used](https://blog.langchain.com/auto-eval-of-question-answering-tasks/) and [explored](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/?ref=blog.langchain.com) each other&#x27;s libraries and found that they worked incredibly well together.

- [Streamlit](https://streamlit.io/generative-ai?ref=blog.langchain.com) is a faster way to build and share data apps. It turns data scripts into shareable web apps in minutes, all in pure Python.
- [LangChain](https://blog.langchain.com/) helps developers build powerful applications that combine LLMs with other sources of computation or knowledge.

Both libraries have a strong open-source community ethic, and a &quot;batteries included&quot; approach to quickly delivering a working app and iterating rapidly.

**Rendering LLM thoughts and actions**

Our first goal was to create a simpler method for rendering and examining the thoughts and actions of an LLM agent. We wanted to show what takes place before the agent&#x27;s final response. It&#x27;s useful for both the final application (to notify the user about the process) and the development stage (to troubleshoot any problems).

The [Streamlit Callback Handler](https://python.langchain.com/docs/modules/callbacks/integrations/streamlit?ref=blog.langchain.com) does precisely that. Passing the callback handler to an agent running in Streamlit displays its thoughts and tool input/outputs in a compact expander format.

Try it out with this MRKL example, a popular Streamlit app:

What are we seeing here?

- An expander is rendered for each thought and tool call from the agent
- The tool name, input, and status (running or complete) are shown in the expander title
- LLM output is streamed token by token into the expander, providing constant feedback to the user
- Once finished, the tool return value is also written out inside the expander

We added this to our app with just one extra line of code:

`# initialize the callback handler with a container to write to

st_callback = StreamlitCallbackHandler(st.container())

# pass it to the agent in the call to run()

answer = agent.run(user_input, callbacks=[st_callback])
`

For a complete walkthrough on how to get started, please refer to our [docs](https://python.langchain.com/docs/modules/callbacks/integrations/streamlit?ref=blog.langchain.com#installation-and-setup).

## **Advanced usage**

You can configure the behavior of the callback handler with advanced options available [here](https://api.python.langchain.com/en/latest/callbacks/langchain.callbacks.streamlit.streamlit_callback_handler.StreamlitCallbackHandler.html?ref=blog.langchain.com):

- Choose whether to expand or collapse each step when it first loads and completes
- Determine how many steps will render before they start collapsing into a &quot;History&quot; step
- Define custom labels for expanders based on the tool name and input

The callback handler also works seamlessly with the new [Streamlit Chat UI](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps?ref=blog.langchain.com), as you can see in this &quot;chat with search&quot; app (requires an OpenAI API Key to run):

🤝

View more example apps and a 1-click GitHub Codespaces setup to start hacking from our [shared repo](https://github.com/langchain-ai/streamlit-agent?ref=blog.langchain.com).

## **Where are we going from here?**

We have a few improvements in progress:

- Extend StreamlitCallbackHandler to support additional chain types like VectorStore, SQLChain, and simple streaming (and improve the default UI/UX and ease of customization).
- Make it even easier to use LangChain primitives like Memory and Messages with Streamlit chat and session_state.
- Add more app examples and templates to [langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent?ref=blog.langchain.com).

We&#x27;re also exploring some deeper integrations for connecting data to your apps and visualizing chain/agent state to improve the developer experience. And we&#x27;re excited to collaborate and see how you use these features!

If you have ideas, example apps, or want to contribute, please reach out on the [LangChain](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) or [Streamlit](https://discord.gg/bTz5EDYh9Z?ref=blog.langchain.com) Discord servers.

Happy coding! 🎈🦜🔗

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)