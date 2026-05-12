---
title: "Code Interpreter Sandbox"
author: "Tereza Tizkova"
date: "2023-11-07"
url: "https://e2b.dev/blog/e2b-sandbox"
category: "integrations"
site: "e2b"
---

We are [E2B.](/?ref=ai-agents-vs-developers) We provide sandboxed cloud environments for AI-powered apps and agentic workflows. 

Try our [Sandbox Runtime for LLMs](/docs?ref=october-newsletter)[.](https://github.com/e2b-dev)

[We are open-source](https://github.com/e2b-dev), so please check out our [GitHub](https://github.com/e2b-dev/e2b), and support us with a star. ✴️

### E2B Sandbox

LLM Sandboxes are **cloud environments, general-purpose** machines powered by Ubuntu. Sandboxes are an ideal fit for AI assistants like coding copilots, code interpreters, AI data analysts, AI browser assistants, and other AI-powered apps.** **Read more about it [here](/docs/sandbox/overview). 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679767b7004a77fc44138814_6797674bd35808d3824a2094_o9eOHxitnoYifZQZsnBSXFOwLOQ.avif)Features of the E2B Sandbox. [Source](/docs/sandbox/overview#features)

### E2B Custom Sandboxes

While OpenAI announced major updates, E2B silently launched Custom Sandboxes today. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679767b7004a77fc44138811_679767661577ae3c1a2f67aa_R4ciA2SAeXzprunSofwnvX37hA4.avif)

Follow [our guide](/docs/guide/custom-sandbox) on how to create your own Custom Sandbox. 

You can create your own Custom Sandboxes for different purposes, from data analysis through AI internet browsing to very popular code execution. You can use Template Files for building the Custom Sandboxes.

**The Code Interpreter Sandbox is just one of the Custom Sandboxes**, and it may seem similar to what was released by OpenAI at the DevDay conference.

#### How is the OpenAI Code Interpreter different from the E2B Code Interpreter Sandbox?

This is the question we have been asked a lot. The differences include:

- The [E2B Code Interpreter Sandbox](/docs/sandbox/overview) is just a sandbox - without any LLM "connected" to it. Our Sandbox can be **controlled with SDK **(`run_code`, `install_pkg`, `create_file`, etc) and gives you the freedom to **connect it to (any) LLM**. 

On the other hand, you **control the OpenAI Code Interpreter by talking to an AI assistant.**

- While the OpenAI CI API is a good fit if you want something working right out of the box, E2B Sandbox comes in handy if you want **more granular control **over what's and when is happening. We give you [**complete environment customization**](/docs/sandbox/templates/overview)**.**‍
- E2B is (partly) [open-source](https://github.com/e2b-dev) and we are going full open-source soon.