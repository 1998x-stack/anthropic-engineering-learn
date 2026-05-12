---
title: "How I taught an AI to use a computer"
author: "James Murdza"
date: "2025-01-20"
url: "https://e2b.dev/blog/how-i-taught-an-ai-to-use-a-computer"
category: "ai-agents"
site: "e2b"
---

#### Table of contents

- An open source computer use agent
- Technical Challenges
Challenge 1: Security
- Challenge 2: Clicking on things
- Challenge 3: Reasoning
- Digression: Agent frameworks are mostly useless
- Challenge 4: Deploying Niche LLMs
- Challenge 5: Streaming the display

- Thoughts on the future
APIs and Accessibility APIs
- Authentication and Sensitive Information

- Conclusion

## An open source computer use agent

I made this! It’s an LLM-powered tool that can use all the functionalities of a personal computer.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67881298b8cac169629243a9_1b2bcd9f-150b-44c0-a75b-4f6ef79f4016.gif)

It takes a command like “Search the internet for cute cat pictures” and uses LLM-based reasoning to operate the mouse and keyboard of the computer on autopilot.

How is this different than other tools that exist already? It’s [**fully open source**](https://github.com/e2b-dev/secure-computer-use/) and uses **only open weight models**. That means that anyone can run and modify my project in any way.

The computer use agent is a work in progress and has limited accuracy, but is showing noticeable improvement every few days. In this article, I’ll give you a tour of how it works. The short explanation is as follows:

The agent **takes many screenshots and asks Meta’s Llama 3.3 LLM what to do next** (click, type, etc.) until the response is that that the task is finished.

Technically, there are a few more components in the system. Here’s an in-depth flow chart of the program and **all of the critical components**:

![Open Computer Use Architecture](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/678812f76430c3f2ca0fe7e6_architecture.png)

This schematic, of course, is just a snapshot of what I have right now, which took me about a month to develop. The LLMs and tools in the diagram will rapidly change as I experiment.

## Technical Challenges

To solve this, I had some pretty daunting challenges.

- **Security:** Isolating the operating system in a safe, controlled environment
- **Clicking on things:** Enabling the AI to click precisely to manipulate UI elements
- **Reasoning:** Enabling the AI to decide what to do next (or when to stop) based on what it sees
- **Deploying niche LLMs:** Hosting open source models, specifically OS-Atlas, in a cost-effective way
- **Streaming the display:** Finding a low latency way to show and record video of the sandbox

### Challenge 1: Security

The ideal environment to run an AI agent should be easy to use, performant, and secure. Giving an AI agent direct access to your personal computer and file system is dangerous! It could delete files, or perform other irreversible actions.

Rather than give the agent access to my computer, I used [**E2B**](/). E2B is a cloud platform that provides secure sandboxes meant to augment AI agents. It’s most common use-case is to run Python code (to generate Perplexity’s charts, for example) but it now supports running a full-fledged Ubuntu system with GUI applications. Thus, it’s perfect for this project.

### Challenge 2: Clicking on things

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67881298b4df8a121e69d991_e406d335-9dde-452d-806b-a7f117fe9884.jpeg)

Now, we’re getting to the fun part. LLM-based “computer use” is fairly straightforward when the interface is text-based, and you can get far with just text-based commands.

However, there are some applications you will basically never be able to use without a mouse. Thus, for a comprehensive computer use agent, we need this feature.

I was also not satisfied with solutions that used traditional computer vision models as a “bridge” between the screen and LLM. They did great for recognizing text and some icons, but they had no idea what was a text field vs. a button or some other element.

Then, I came upon some promising research out of China on building “grounded VLMs.” This is a vision LLM with the ability to output precise coordinates referencing the input image. Both Gemini and Claude have this ability, but are neither are open source nor published. The OS-Atlas team, on the other hand, has published their weights on Hugging Face and outlined [**the fascinating training process in this paper**](https://arxiv.org/pdf/2410.23218).

### Challenge 3: Reasoning

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67881298749bcd91a3f15938_e5d5a2a2-2241-4572-8849-2cbab8596d09.jpeg)

The power of LLM-based agents is that they can decide between multiple actions, and make educated decisions using the most recent information.

Over the past year, we’ve seen a gradual increase in LLMs’ abilities to make these decisions. The first approach was to simply prompt the LLM to output actions in a given text format, and to add the result of the action to the chat history before calling the LLM again. All following approaches have been roughly the same, with fine-tuning used to compliment the system prompts. This general ability was called **function calling**, while the term **tool-use** is now more popular.

The combination of vision to inform tool-use in a single LLM call is a fairly new thing that hasn’t seen much mileage yet. I tried a few different open source models to get this, and I’ll summarize the following part briefly since it will probably be outdated in a couple of weeks anyway. In my agent, I used:

- **Llama-3.2-90B-Vision-Instruct** to view the sandbox display, and decide on next steps to take
- **Llama 3.3-70B-Instruct** to take the decision from Llama 3.2 and rephrase it in tool-use format
- **OS-Atlas-Base-7B** as a tool that can be called by the agent to perform a click action given a prompt of what to click

### Digression: Agent frameworks are mostly useless

If you’ve looked into building AI agents, you’ve probably asked the question: Why are there so many frameworks out there?

In my personal experience, the utility of these frameworks is to abstract 1) LLM input formatting and output parsing, 2) the agent prompts and 3) the agent run loop. Since I want to keep my run loop very simple, the main use in a framework would be to handle the interface with the LLM provider, especially for tool-use and images. However, most providers are now standardizing towards the OpenAI tool-use format **anyways**, and when there are exceptions it’s often not clear from the documentation if the framework handles them. And as for the system prompts, I really **don’t** want this to be abstracted, since this is one part of the code I need to adjust all the time.

If you’ve had a different experience than the above—That’s cool, I’d love to hear your thoughts!

Also, one big lesson that I have learned about tool use is that it’s not really a single feature. It’s a whole hodgepodge of LLM fine-tuning, various prompts, and string formatting and parsing on either the API side or on the client side. It is just so hard to make a framework (and keep it updated) to fit together all these parts without the developer needing to look inside.

### Challenge 4: Deploying Niche LLMs

Since I want my agent to run fast, I wanted to run the LLM inference in the cloud. I also wanted it to work out-of-the-box for curious people like yourself.

Unfortunately, this was much easier said than done. There are numerous inference hosting providers, and they all have there different points of friction. Fortunately, Llama 3.2 and 3.3 are fairly common, and I found OpenRouter, Fireworks AI, and the official Llama API to be pretty good options. They all provide “serverless” hosting, which essentially means that you only pay marginal costs and no fixed costs.

But, there were no such options for OS-Atlas. I reached out to a number of inference providers, and what I eventually learned is that economies of scale make it prohibitive for hosts to put out serverless versions of infrequently used models. With few users, it’s hard for them to distribute the costs of the hosting and the engineering time amongst these users.

I ended up using a free Hugging Face Space to call OS-Atlas. This is relatively slow (takes a few seconds for each call) and is rate-limited (a few dozen calls per hour) but it gets the job done for now.

### Challenge 5: Streaming the display

In order to see what the AI is doing, we want to get live updates from the Sandbox’s screen. I wondered if I do this using ffmpeg. After bashing random shell commands for a while, I found the right magic incantations:

Server: `ffmpeg -f x11grab -s 1024x768 -framerate 30 -i $DISPLAY -vcodec libx264 -preset ultrafast -tune zerolatency -f mpegts -listen 1 http://localhost:8080`

Client: `ffmpeg -reconnect 1 -i http://servername:8080 -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -f mpegts -loglevel quiet - | tee output.ts | ffplay -autoexit -i -loglevel quiet -`

The first command basically creates a video streaming server over HTTP which can stream to one client at a time. The second command captures the stream, and simultaneously writes it to a .ts file, and displays it in a GUI.

This works fine over the internet. The server is some kind of built in feature of FFmpeg, but has the limitation that it can only stream to one client at a time. Therefore, the client must use the tee command to split the stream so it can be both saved and displayed. (Please don’t ask me anything about codecs or any of the other flags up there!) In the future, the plan is to either reduce the latency of the stream or replace it entirely with a VNC connection.

## Thoughts on the future

This has mainly been an article of what I built with the tools available to me. A major goal of the project was that it is operating system agnostic, application agnostic, and to the extent possible, LLM agnostic. This worked, although

### APIs and Accessibility APIs

One recurring theme that came up in my work was the question of whether computer use agents in general should lean more heavily on APIs (coded pathways) or GUI only (pure vision). The answer is clearly: Agents **should** make use of APIs as much as possible, but most software is just not made to be controlled this way.

That’s why in my testing, I wanted to make sure the agent could open a web browser, click on the URL bar, type some text, etc., even though there is an equivalent shell command that can do the same thing. When designing a computer use agent, we should also consider the non-visual interfaces that are available to us, and here are a few:

- **Standard APIs**: These include APIs such as the file system API, the Microsoft Office API, or the Gmail REST API, which provide structured access to useful functionalities.
- **Code Execution**: This involves running scripts or commands, such as executing Bash or Python code to launch an application or parse the contents of a file.
- **Accessibility APIs**: The OS or desktop environment often provides accessibility APIs that allow direct interaction with the GUI hierarchy. Unfortunately, support on Linux tends to be worse than macOS or Windows.
- **Document Object Model (DOM)**: The DOM enables interaction with web pages in a semi-structured, text-based manner.
- **Model Context Protocol (MCP)**: The Model Context Protocol is a is a newly introduced API specifically designed to both provide context and actions in an agent-friendly manner.

Given the number of options, it’s somewhat of a tragedy that we have to rely on vision which is a far more burdensome task for an AI. This is especially true for #3, since better accessibility APIs would be beneficial for many (vision impaired) humans as well. It would be amazing if everything could work like Zapier, where everything is connected with the right adapters. We can only hope!

### Authentication and Sensitive Information

Another huge open question is how to securely handle authentication. The **insecure approach** would be to provide the agent with the same level of access as the user. A **secure approach would be to scope permissions**, as is commonly used by OAuth apps, iOS apps, etc. such as the example below:

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/67881298e3e6dbe706ba1e85_093327e0-504c-4a22-9c29-dfeb25adc5ed.jpeg)

In our agent we’ve avoided this problem entirely by creating a fresh, isolated sandbox with no user data or credentials. But this also doesn’t solve the problem.. If a secure approach isn’t available to users, they tend to create an insecure one. Therefore, it’s important to already start thinking about the following:

- Ways to provide computer use agents with **scoped access to APIs**: For example, a computer use agent uses a traditional API to view the user’s email inbox without the ability to delete or send emails
- Ways to **redact sensitive information** passed to the LLM, and restore it in the LLM output: For example, a user can set secrets, such as CREDIT_CARD_NUMBER, which can be passed to tools but not seen by the LLM

## Conclusion

The AI computer use agent I made is a prototype that can use the computer about as well as I could when I was five or six. It still has a lot of trouble planning next steps and often doesn’t know where to focus its attention on the screen. For example, it may not notice if a text field is selected or not, or it may lose sight of the original goal when presented with a full screen of text. This is not at all surprising for an LLM.

That said, reasoning with vision is an area where we expect to see a lot of improvement in open source models on a monthly basis, and even while I’ve been writing this article, new models have been released that I’m excited to try out. Meanwhile, I’m also excited to augment the agent’s abilities by adding additional APIs to the agent’s toolbox.

If this is a problem that’s interesting to you, check out [**the source code**](https://github.com/e2b-dev/secure-computer-use/) and [**reach out to me**](https://www.linkedin.com/in/jamesmurdza/).