---
title: "Gradio &amp; LLM Agents"
author: "LangChain Accounts"
date: "2023-04-24"
url: "https://www.langchain.com/blog/gradio-llm-agents"
---

LangChainTutorials &amp; How-Tos

# Gradio &amp; LLM Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 23, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb2353c7fbd0a6275ef83_photo-1579546929518-9e396f3cc809.jpeg)**Editor&#x27;s note: this is a guest blog post from Freddy Boulton, a software engineer at Gradio. We&#x27;re excited to share this post because it brings a large number of exciting new tools into the ecosystem. Agents are largely defined by the tools they have, so to be able to equip them with all these `gradio_tools` is very exciting to us!**

**Important Links:**

- [Gradio Tools Library](https://github.com/freddyaboulton/gradio-tools?ref=blog.langchain.com)
- [LangChain Integration](https://python.langchain.com/docs/modules/agents/tools/integrations/gradio_tools?ref=blog.langchain.com)
- [Accompanying Gradio Blog Post](https://gradio.app/gradio-and-llm-agents/?ref=blog.langchain.com)

Large Language Models (LLMs) are very impressive but they can be made even more powerful if we could give them skills to accomplish specialized tasks.

The [gradio_tools](https://github.com/freddyaboulton/gradio-tools?ref=blog.langchain.com) library can turn any [Gradio](https://github.com/gradio-app/gradio?ref=blog.langchain.com) application into a [tool](https://python.langchain.com/docs/modules/agents/tools?ref=blog.langchain.com) that an [agent](https://python.langchain.com/docs/modules/agents/?ref=blog.langchain.com) can use to complete its task. For example, an LLM could use a Gradio tool to transcribe a voice recording it finds online and then summarize it for you. Or it could use a different Gradio tool to apply OCR to a document on your Google Drive and then answer questions about it.

This guide will show how you can use `gradio_tools` to grant your LLM Agent access to the cutting edge Gradio applications hosted in the world. Although `gradio_tools` are compatible with more than one agent framework, we will focus on [LangChain agents](https://python.langchain.com/docs/modules/agents/?ref=blog.langchain.com) in this guide.

## Some background

### What are agents?

A [LangChain agent](https://python.langchain.com/docs/modules/agents/?ref=blog.langchain.com) is a Large Language Model (LLM) that takes user input and reports an output based on using one of many tools at its disposal.

### What is Gradio?

[Gradio](https://github.com/gradio-app/gradio?ref=blog.langchain.com) is the defacto standard framework for building Machine Learning Web Applications and sharing them with the world - all with just python! 🐍

## gradio_tools - An end-to-end example

To get started with `gradio_tools`, all you need to do is import and initialize your tools and pass them to the langchain agent!

In the following example, we import the `StableDiffusionPromptGeneratorTool` to create a good prompt for stable diffusion, the
`StableDiffusionTool` to create an image with our improved prompt, the `ImageCaptioningTool` to caption the generated image, and
the `TextToVideoTool` to create a video from a prompt.

We then tell our agent to create an image of a dog riding a skateboard, but to please improve our prompt ahead of time. We also ask
it to caption the generated image and create a video for it. The agent can decide which tool to use without us explicitly telling it.

`import os
if not os.getenv(&quot;OPENAI_API_KEY&quot;):
    raise ValueError(&quot;OPENAI_API_KEY must be set&quot;)
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from gradio_tools import (StableDiffusionTool, ImageCaptioningTool, StableDiffusionPromptGeneratorTool,
                          TextToVideoTool)
from langchain.memory import ConversationBufferMemory
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key=&quot;chat_history&quot;)
tools = [StableDiffusionTool().langchain, ImageCaptioningTool().langchain,
         StableDiffusionPromptGeneratorTool().langchain, TextToVideoTool().langchain]
agent = initialize_agent(tools, llm, memory=memory, agent=&quot;conversational-react-description&quot;, verbose=True)
output = agent.run(input=(&quot;Please create a photo of a dog riding a skateboard &quot;
                          &quot;but improve my prompt prior to using an image generator.&quot;
                          &quot;Please caption the generated image and create a video for it using the improved prompt.&quot;))
`

You&#x27;ll note that we are using some pre-built tools that come with `gradio_tools`. Please see this [doc](https://github.com/freddyaboulton/gradio-tools?ref=blog.langchain.com#gradio-tools-gradio--llm-agents) for a complete list of the tools that come with `gradio_tools`.
If you would like to use a tool that&#x27;s not currently in `gradio_tools`, it is very easy to add your own. That&#x27;s what the next section will cover.

## gradio_tools - creating your own tool

The core abstraction is the `GradioTool`, which lets you define a new tool for your LLM as long as you implement a standard interface:

`class GradioTool(BaseTool):
    def __init__(self, name: str, description: str, src: str) -&gt; None:
    @abstractmethod
    def create_job(self, query: str) -&gt; Job:
        pass
    @abstractmethod
    def postprocess(self, output: Tuple[Any] | Any) -&gt; str:
        pass
`

The requirements are:

- The name for your tool
- The description for your tool. This is crucial! Agents decide which tool to use based on their description. Be precise and be sure to inclue example of what the input and the output of the tool should look like.
- The url or space id, e.g. `freddyaboulton/calculator`, of the Gradio application. Based on this value, `gradio_tool` will create a [gradio client](https://github.com/gradio-app/gradio/blob/main/client/python/README.md?ref=blog.langchain.com) instance to query the upstream application via API. Be sure to click the link and learn more about the gradio client library if you are not familiar with it.
- create_job - Given a string, this method should parse that string and return a job from the client. Most times, this is as simple as passing the string to the `submit` function of the client. More info on creating jobs [here](https://github.com/gradio-app/gradio/blob/main/client/python/README.md?ref=blog.langchain.com#making-a-prediction).
- postprocess - Given the result of the job, convert it to a string the LLM can display to the user.
- *Optional* - Some libraries, e.g. [MiniChain](https://github.com/srush/MiniChain/tree/main?ref=blog.langchain.com), may need some info about the underlying gradio input and output types used by the tool. By default, this will return gr.Textbox() but
if you&#x27;d like to provide more accurate info, implement the `_block_input(self, gr)` and `_block_output(self, gr)` methods of the tool. The `gr` variable is the gradio module (the result of `import gradio as gr`). It will be
automatically imported by the `GradiTool` parent class and passed to the `_block_input` and `_block_output` methods.

And that&#x27;s it!

Once you have created your tool, open a pull request to the `gradio_tools` repo! We welcome all contributions.

## Example tool - Stable Diffusion

Here is the code for the StableDiffusion tool as an example:

`from gradio_tool import GradioTool
import os
class StableDiffusionTool(GradioTool):
    &quot;&quot;&quot;Tool for calling stable diffusion from llm&quot;&quot;&quot;
    def __init__(
        self,
        name=&quot;StableDiffusion&quot;,
        description=(
            &quot;An image generator. Use this to generate images based on &quot;
            &quot;text input. Input should be a description of what the image should &quot;
            &quot;look like. The output will be a path to an image file.&quot;
        ),
        src=&quot;gradio-client-demos/stable-diffusion&quot;,
        hf_token=None,
    ) -&gt; None:
        super().__init__(name, description, src, hf_token)
    def create_job(self, query: str) -&gt; Job:
        return self.client.submit(query, &quot;&quot;, 9, fn_index=1)
    def postprocess(self, output: str) -&gt; str:
        return [os.path.join(output, i) for i in os.listdir(output) if not i.endswith(&quot;json&quot;)][0]
    def _block_input(self, gr) -&gt; &quot;gr.components.Component&quot;:
        return gr.Textbox()
    def _block_output(self, gr) -&gt; &quot;gr.components.Component&quot;:
        return gr.Image()
`

Some notes on this implementation:

- All instances of `GradioTool` have an attribute called `client` that is a pointed to the underlying [gradio client](https://github.com/gradio-app/gradio/tree/main/client/python?ref=blog.langchain.com#gradio_client-use-a-gradio-app-as-an-api----in-3-lines-of-python). That is what you should use
in the `create_job` method.
- `create_job` just passes the query string to the `submit` function of the client with some other parameters hardcoded, i.e. the negative prompt sting and the guidance scale. We could modify our tool to also accept these values from the input string in a subsequent version.
- The `postprocess` method simply returns the first image from the gallery of images created by the stable diffusion space. We use the `os` module to get the full path of the image.

## Conclusion

You now know how to extend the abilities of your LLM with the 1000s of gradio spaces running in the wild!
Again, we welcome any contributions to the [gradio_tools](https://github.com/freddyaboulton/gradio-tools?ref=blog.langchain.com) library.
We&#x27;re excited to see the tools you all build!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c8eea3104c341cdd9b_Screenshot-2026-03-03-at-11.51.04---PM.png)Company AnnouncementsLangChain

#### LangChain Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)2min[](/blog/langchain-skills)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)