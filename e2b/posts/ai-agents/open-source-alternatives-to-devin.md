---
title: "Open-Source Alternatives to Devin"
author: "Tereza Tizkova"
date: "2024-04-18"
url: "https://e2b.dev/blog/open-source-alternatives-to-devin"
category: "ai-agents"
site: "e2b"
---

A startup called Cognition AI recently caused controversy by releasing an AI assistant called Devin. In a demo video, this AI software developer was seen working on tasks typically done by high-paid software engineers. One of the creators' goals is to enable Devin to contribute code successfully to large, complex codebases, making a lot of technical people fear about their jobs.

There are quite many coding AI agents and assistants already, but Devin caught everyone’s attention because of these reasons things:

- [Amazing demo](https://www.youtube.com/watch?v=fjHtjT7GO1c&ab_channel=Cognition) showing the assistant completing a wide range of more advanced tasks
- Nice UI, which many agents still don't have
- The ability to not only generate, but execute code
- Scoring relatively high in a SWE-bench.

## What is the SWE-bench?

In October 2023, a [paper](https://arxiv.org/abs/2310.06770) called “SWE-bench: Can Language Models Resolve Real-World GitHub Issues?” introduced the SWE benchmark.

The previous coding benchmarks for LLMs all have a similar format. They present a coding exercise to be solved and evaluate models’ responses by running the generated function on some held-out unit tests. Such tests do not represent the real world tasks accurately.

SWE-bench is a set of 2,294 tasks based on pairs of issues and pull requests from popular Python repositories on GitHub. They form an evaluation set requiring models to understand problems in the context of a real codebase, find and isolate bugs among thousand-line files, and generate solutions that could interact with multiple parts of code. 

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd0a_6797a592f10b67c881a8885e_k2OPq2nr7qg5gYyZJH5HMUMUcQ.avif)](https://arxiv.org/pdf/2310.06770.pdf)

The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues. Advances on SWE-bench represent steps toward LLMs that are more practical, intelligent, and autonomous.]

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd07_6797a5b1487b514feb110a5e_5hGh6FnuzeaJPVzZUcq1gxXByYk.avif)

### Code execution

Chatbots like ChatGPT, Perplexity, and Phind can generate code, but Devin went further. It can also run, test, and implement the code, using a sandbox as runtime. (Read more about how [sandboxes](/docs) might work for running LLM-generated code). 

Devin is the latest example of the emerging AI agents powered by a [code interpreter](/blog/llm-powered-code-interpreters) - which makes it extra powerful and able to take action instead of just giving a piece of passive advice. It's not the first agent with code execution (this can be also achieved by [Open Interpretrer](https://docs.openinterpreter.com/integrations/e2b), [AutoGen](https://github.com/microsoft/autogen), or [ChatGPT Data Analyst](https://chat.openai.com/)), but such capability is still not that common.

## Open-source alternatives

The way Devin works has still been seen by most people only in the demo as only a few selected individuals have received access. Luckily, people were quick to build open-source alternatives to try. (Some of them, like [Devika](https://x.com/mufeedvh/status/1770696907943219338) started as a fun hackathon-style projects. Creator of Devika made the first version in about 20 hours.)

Open-source is a preferred choice by many developers,  and even the original Devin even started working on one of the other “Devins". 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd12_6797a5d615de7178c8f706b8_JIJ3KotcVMzW8ADJaZHzwkabM.avif)

Here are some of the popular open-source alternatives to Devin and their capabilities and benchmarks.

### 1. OpenDevin

One of the main reasons Devin got so popular and even reached general public people is the UI where you can see the agents work, without having to use terminal.OpenDevin offers a nice UI as well, and it has received over 20.7k stars. The techstack currenyly used in the project include FastAPI, uvicorn, LiteLLM, Docker, Ruff, MyPy, LlamaIndex, and React.OpenDevin executes code via Docker, though there is ongoing work to add an option for executing code in the [E2B sandboxed environment](https://github.com/OpenDevin/OpenDevin/pull/727). The [sandbox](/docs) is a secure micro VM made for running AI agents and AI-generated code in the cloud. With that, it would be very easy for OpenDevin to download things from internet, use filesystem, a browser, or ability to run different languages besides Python.

### 2. AutoCodeRover

Even though AutoCodeRover doesn’t reach the popularity of OpenDevin yet, it was able to resolve approximately 16% of issues on the SWE-bench (totaling 2,294 GitHub issues) and about 22% of issues on the SWE-bench lite (totaling 300 GitHub issues).

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd04_6797a6218a569d929ebe80ed_mArLk2nE5VVFVSdI4G1cAfVqIeU.avif)](https://github.com/nus-apr/auto-code-rover)

How did AutoCodeRover achieve such results? It operates in two stages. First, in the context retrieval stage, the LLM is equipped with code search APIs to navigate the codebase and gather relevant context. The code search APIs are Structure-aware. Instead of searching over files using plain string matching, the agent searches for relevant code context (such as methods or classes) in the abstract syntax tree.

Then comes the patch generation where the LLM attempts to write a patch based on the retrieved context. When a test suite is available, [AutoCodeRover](https://github.com/nus-apr/auto-code-rover)  can leverage test cases to achieve an even higher repair rate by performing statistical fault localization.

### 3. Devika

Devika is another Agentic AI software engineer with over 15k GitHub stars that aims to compete with Devin by Cognition AI. Devika supports Claude 3, GPT-4, GPT-3.5, and Local LLMs via Ollama. Its architecture includes a Code Writing Module that generates code based on the plan, a Browser Interaction Module that enables Devika to extract information from websites.

In their [demo](https://www.youtube.com/watch?v=GBvNxHiquKM&ab_channel=WorldofAI), Devika is creating a Game of Life using pygame. This is the same task Devin team showed in their famous demo. 

To start, Devika requires you to have API key of OpenAI or Claude, Bing, and Netlify, but it is still great to be able to try an agent that accomplishes tasks similar to Devin.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd21_6797a66289ef31483373ef81_bpCKqVHJd8Yi0LC9WiUZ6V8i3HM.avif)

### 4. Anterion 

[Anterion](https://www.youtube.com/watch?v=J-KZNFVcAxU&ab_channel=Anterion) AI Agent aims to extend the capabilities from GitHub issues to open-ended general engineering tasks, and their frontend is inspired by OpenDevin.

‍[According to the creators](https://www.youtube.com/watch?v=J-KZNFVcAxU&ab_channel=Anterion), they have big plans, for example, adding Vercel, and more features in the future. In their demo, they used the agent to get the number of stars from popular AI software engineer repositories.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd18_6797a6882ad6bcf5e083bb4a_86TrmAoUb8nnc6V4qBkq6Vt9Ob0.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd0d_6797a694932e5cf1a3eba57b_XMTcKZPoABLnAHKnq6dn4cHSIgE.avif)

### 5. MetaGPT

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd1b_6797a6ad1996dfe6cb2faad6_4HhcC6FjjTctwrv7lTtTbJasEQ.avif)](https://docs.deepwisdom.ai/main/en/DataInterpreter/)

### 6. AutoDev

AutoDev has one big advantage and that is a multilingual support. It supports languages like Python, and JavaScript/TypeScript, but also Rust, Java, Kotlin, Golang, or C/C++/OC.

AutoDev is still not that easy to access for a normal user and requires coding knowledge to set up. That makes it slightly disadvantageous among other alternatives, but it's still in its early stage.

In its demo, AutoDev shows capabilities like debugging and customizable prompts.

### 7. Devon

### 8. SWE-agent

This Devin alternative was made by the SWE-bench authors, and it scores 12.3% on the full SWE-bench.There are changes and innovations in [SWE-agent](https://swe-agent.com/) compared to Devin. It executes code locally via Docker. It uses a constrained "Agent-Computer Interface" (ACI), making the agent more user-friendly for LLMs. Only a few commands are allowed: run code, look for code, edit code, and submit changes to GitHub.

The agent's code goes through a syntax check (linter) before submission, and if the syntax is incorrect, the agent receives feedback and is compelled to rewrite the code. The agent can only read 100 lines of code at a time, simplifying the language model's understanding of the code.

The creators [highlight](https://x.com/jyangballin/status/1775114448513958134) that LLMs require carefully designed agent-computer interfaces, akin to how humans appreciate good user interface (UI) design. For instance, when the LM makes a mistake with indentation, the SWE-agent editor prevents it and provides feedback. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd15_6797a71afc999445d5057378_O2eGuT08pbLJ5ohSfDjfYr97VRo.avif)

## So… are Devins replacing software engineers?

I’ve seen a lot of people asking whether engineers and developers are really being replaced by teams of Devins. But is it that big of a threat for developers? The Devin demo was followed by other videos [debunking its capabilities](https://www.youtube.com/watch?v=tNmgmwEtoWE&ab_channel=InternetofBugs) and even claiming that Cognition is overselling their agent.

Looking closely at the SWE-bench, it is a great, but still not a 100% perfect measure either. The bench only includes Python tasks at this moment. If you’re an organization building mobile applications or work with Java, Go, Swift or Typescript then progress against SWE-bench by AI software engineers or models has limited use to you. 

In conclusion, “Devins” are not there yet to replace engineers, but you can still follow their progress closely, for example on this [GitHub map](https://github.com/e2b-dev/awesome-devins?tab=readme-ov-file). Explore the full list of open-source Devins and make a pull request if you want to include a new Devin-like project.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797a76ab8db373ed9cfbd24_6797a73870be130ff0cff093_GVT9iIQYbOSEU9bM1Ethq2UW00.avif)