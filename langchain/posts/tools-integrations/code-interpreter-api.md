---
title: "Code Interpreter API"
author: "LangChain Accounts"
date: "2023-07-16"
url: "https://www.langchain.com/blog/code-interpreter-api"
---

Observability &amp; Evals

# Code Interpreter API

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 16, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1fca83bd2fbf570991e_photo-1615525137689-198778541af6.jpeg)**Editor&#x27;s Note: This is another installation of our guest blog posts highlighting interesting and novel use cases. This blog is written by **[**Shroominic**](https://shroominic.com/?ref=blog.langchain.com)** who built an open source implementation of the ChatGPT Code Interpreter. **

Important Links:

- [GitHub Repo](https://github.com/shroominic/codeinterpreter-api?ref=blog.langchain.com)

In the world of open-source software, there are always exciting developments. Today, I am thrilled to announce a new project that I have been working on - Code Interpreter API. It&#x27;s an implementation of the ChatGPT Code Interpreter using LangChain Agents. Keep in mind this is an unofficial implementation and I am not affiliated with OpenAI.

## Motivation

As an indie developer, I am constantly searching for new features to add to my projects. While working on a Discord bot, I attempted to incorporate the code interpreter as a feature. I never tried it at that point but got hyped by seeing people using it on YouTube. It started as an experiment, but with some tinkering, it evolved into a functional and progressively improving feature. I noticed a significant interest in this area and identified a gap in the market - there was no API for this and especially not open source.

## **Unique Features and Benefits**

The biggest advantage over the already existing Code Interpreter from OpenAI is that this open-source version has internet access. For example, this is useful when asking “Plot the Bitcoin chart of 2023” the agent uses yahoo finance to download live data about the current situation and then shows it as an image plot to the user. Another advantage is that you can use your hardware. For example, if you want to do something that includes running stable diffusion you need to have a dedicated GPU that can run the model. This is not the case in the cloud environment you have from OpenAI. Other features include chat memory so you can ask follow-up questions and automatic Python package installation (when missing) so the agent tries again.

## **Technical Details**

The core of this project is a LangChain Agent, specifically the new OpenAIFunctionsAgent which gives the advantage of calling functions/tools to better handle the user needs. For the code interpreter, we need to give it access to a Python interpreter so it can execute Python code. This interpreter is represented as a tool so the Agent can call the tool and use Python to fulfill what the user wants.

For example, if the user asks to plot a sin wave and show it as an image, the agent writes Python code and inputs it to the Python interpreter which runs the code, outputs the image and then this image can be displayed to the user. Additionally, the Agent can comment on the result and explain what happened or give more details about the output.

It is not straightforward to give LangChain Agents access to a Code Execution Environment. There is already Python REPL but this does not allow for FileIO and it also forgets variables after every run. So I had to write my solution for this: CodeBoxAPI.

When starting a Code Interpreter Session it creates a small Jupyter kernel on your device similar to how Jupyter notebooks work. A CodeBox is the underlying Python execution env where the agent can run code and receive its outputs. A small personal computer the agent has access to and which it can use to serve the user its request.

## Examples

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1fda83bd2fbf5709934_screenshot_2023-07-16_at_17.49.13.png)

AI: Here is the normalized plot showing the relative performance of the tech giants (Apple, Google, Microsoft, Amazon) in 2023. The plot is normalized so that the starting point of each stock is 100, which allows for easy comparison of the percentage changes in each stock&#x27;s price over the period.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1fda83bd2fbf570992e_untitled--10.png)

**Another Example**

Prompt: ”Select representative ETFs for different sectors (Technology, Healthcare, Consumer Discretionary, etc.). Plot their performance during the last two economic cycles. Analyze how different sectors behave in different stages of an economic cycle.”

**Response**

AI: The plot above shows the performance of the selected ETFs representing the Technology, Healthcare, and Consumer Discretionary sectors during the last two economic cycles (the dot-com bubble from 2000-2002 and the financial crisis from 2007-2009).

As we can see, all sectors were negatively affected during these periods, with significant drops in value. However, the extent and timing of these drops vary between sectors.

For a more detailed analysis, we could look at the performance of these sectors during different stages of the economic cycles (e.g., pre-recession, during the recession, and post-recession). However, this would require a more complex analysis and might be beyond the scope of this discussion.

Please note that this analysis is quite simplified and doesn&#x27;t take into account many factors that could influence the performance of these sectors during different economic cycles. For a more accurate and detailed analysis, you might want to consider consulting with a financial advisor or conducting a more in-depth research.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1fda83bd2fbf5709931_untitled--9.png)

## Roadmap

The next step is to make CodeBox production-ready, enabling developers to create public apps as it allows for easy scaling. Currently, each user requires a small sandboxed execution environment, making it challenging to deploy to production with this API. Plans also include making it available using other LLMs) like ClaudeV2 or Open Orca. In time, users may be able to run this API 100% locally and offline on their home PC.

## **How to Use It**

The installation is straightforward: get your OpenAI API Key [**here**](https://platform.openai.com/account/api-keys?ref=blog.langchain.com) and install the package using pip. You can use the API in your Python code: start a session, generate a response based on user input - stop your session. You can find detailed instructions on the project&#x27;s GitHub [**README**](https://github.com/shroominic/codeinterpreter-api/blob/main/README.md?ref=blog.langchain.com).

## **Contribute**

If you&#x27;re interested in contributing to the Code Interpreter API, there are several opportunities. Have a look into the Issues I put some tagged as ToDo. But you can also work on your ideas and just push a PR. Thanks!

## Do Experiments

If you have not checked out the repository I highly recommend to do so and just try out your prompts! Try out a lot of different stuff to get an idea of what is possible and what is not. If you encounter any bugs please publish them as GitHub Issues and I will try to fix them.

This is my first blog post ever so thanks for reading this and I hope you had fun! If you want to get updated feel free to check out my [Twitter @shroominic](https://twitter.com/shroominic?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce8a01c18c14b60cd4372_76.webp)LangSmithObservability &amp; Evals

#### Human judgment in the agent improvement loop

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2d3bf32d4fc06a289383_rahul-verma.png)Rahul VermaApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/human-judgment-in-the-agent-improvement-loop)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dce9138b145f1419b6b38b_74--2-.webp)Observability &amp; Evals

#### Better Harness: A Recipe for Harness Hill-Climbing with Evals

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Vivek TrivedyApril 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)8min[](/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)