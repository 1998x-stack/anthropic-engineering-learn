---
title: "Launching the Code Interpreter SDK"
author: "Tereza Tizkova"
date: "2024-05-06"
url: "https://e2b.dev/blog/launching-the-code-interpreter-sdk"
category: "announcements"
site: "e2b"
---

Building a good product with underlying AI agents means overcoming the challenges of hallucinations, and unreliability, and navigating the agent to use the right tools. One way to solve these problems is to equip agents with code execution capabilities. We see more and more agents powered by a code interpreter.

Examples include [**Flint**](https://www.flintk12.com/) (AI tutoring assistant), [**Athena Intelligence**](https://www.athenaintelligence.ai/) (enterprise data analysis) or [**Maisa**](https://maisa.ai/) (knowledge processing unit).

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797accaa1e515686a5ecba1_6797abffcb7fcf379df2699f_OHz0zrdi2axZ52rVhqRwaeIpfU.avif)](https://www.athenaintelligence.ai/)

The power of code interpreters is also shown with open-source AI software developers like [**OpenDevin**](https://github.com/OpenDevin/OpenDevin)**.**

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797accaa1e515686a5ecba7_6797ac1f0d51d1b170b00bc6_hIgB3myj4zQlf2Z2CfnWQvek0.avif)](https://github.com/OpenDevin/OpenDevin)

## Code Interpreter SDK

At E2B, we are giving AI agents their own computers. We are building the code interpreting layer for AI apps and agents, allowing them to run the LLM-generated actions in a secure and isolated cloud environment.

We just released the [Code Interpreter SDK](https://github.com/e2b-dev/code-interpreter) - open-source building block for AI developers. The SDK makes it easy to add code interpreting to AI apps. The Code Interpreter SDK is built on top of our open-source [runtime for AI agents](https://github.com/e2b-dev/e2b).  Start with [our docs](/docs).

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797aeba1d10081ccea1c911_6797aeb57c829575f82edfae_TeF7ukOo0D1mL2A69TAA8eovRrA.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797accaa1e515686a5ecbb4_6797ac3dede5636467c231c1_ayQ6UPerSuba5cuXI71h0LfQc.webp)

## Features

The Code Interpreter SDK, and also the core E2B SDK works with any LLM and any popular AI framework like LangChain, AutoGen, or CrewAI. 

The SDK has Python or JS version, and supports streaming content like charts and stdout, stderr. It runs on serverless and edge functions and executes the AI-generated code in secure sandboxed environments. It is 100% open source (including [infrastructure](https://github.com/e2b-dev/infra)).

For inspiration, see our [Cookbook](https://github.com/e2b-dev/e2b-cookbook) with examples of using the Code Interpreter SDK with [LangChain](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langchain-python), [Claude](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/claude-code-interpreter-python), [Llama 3](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/groq-code-interpreter-python/llama_3_code_interpreter.ipynb), [Next.js](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/nextjs-code-interpreter), and more.

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797accaa1e515686a5ecba4_6797ac582377bb5db727e330_r4mJYdfO8rWeATS3Hx65LJCIQPE.avif)](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/langchain-python/langchain_code_interpreter.ipynb)

## Built with the Code Interpreter SDK 

We built the special SDK for code interpreting, becaue this is the main use-case we are observing among our customers. Examples of companies using the E2B code interpreting layer for their product are:

- [Cognosys](https://www.cognosys.ai/) - AI agent automating everyday tasks like summarizing emails or creating market reports
- [PGA](https://www.pga.com/) - One of the world's largest sports organizations
- [Menza](https://menza.ai/) - Company transforming unstructured data into insights
- [Flint](https://www.flintk12.com/) - AI tutoring for personalized learning
- [Athena Intelligence](https://www.athenaintelligence.ai/) - Data analyst for enterprise-level companies
- [Maisa](https://maisa.ai/) - AI system that improves reasoning of LLMs.

## Cookbook examples

**The SDK works with any LLM**
- [Anthropic Claude 3 Opus with code interpreter](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/claude-code-interpreter-python)
- 🦙 [Llama 3 with code interpreter](https://github.com/e2b-dev/e2b-cookbook/blob/main/examples/groq-code-interpreter-python/llama_3_code_interpreter.ipynb)
- [Codestral with code interpreter](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/codestral-code-interpreter-python)

**And you can try it with popular AI frameworks**
- 🦜⛓️ [LangChain with code interpreter](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langchain-python)
- 🦜🕸️ [LangGraph with code interpreter](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langgraph-python)
- [Autogen with secure sandboxed code interpreter](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/autogen-python).

[![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797ad54a1e515686a5f38dc_6797ad4dffecc988fe3247d8_rIV1NQc9YGT3gvM1NsYPHkWVOQ.png)](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/langgraph-python)

#### Contact us

Need help setting up E2B? We are happy to connect! Give us any feedback on your experience with E2B.

## We are hiring!

Check out the [open positions](https://e2bdev.notion.site/Careers-at-E2B-2163f176991f43f69b0984bf2a142920) at E2B. We’re a pre-seed startup with a [small team](https://www.notion.so/Careers-at-E2B-2163f176991f43f69b0984bf2a142920?pvs=21) focused on shipping. We work in-person from our office in San Francisco.

We’re backed by founders like [Guillermo Rauch](https://twitter.com/rauchg) (CEO of [Vercel](https://vercel.com/)), [Paul Copplestone](https://twitter.com/kiwicopple) (CEO of [Supabase](https://supabase.com/)), [Juraj Masar](https://www.linkedin.com/in/jurajmasar/) (CEO of [Better Stack](https://betterstack.com/)), [Jakub Jurových](https://www.linkedin.com/in/jakubjurovych/) (CEO of [Deepnote](https://deepnote.com/join-us)) or [Flo Crivello](https://twitter.com/Altimor) (CEO of [Lindy](https://lindy.ai/)), together with people from companies like Stripe, Retool, Figma, OpenAI, and Google.