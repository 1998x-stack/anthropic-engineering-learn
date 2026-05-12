---
title: "AutoGen Code Interpreter with E2B"
author: "Tereza Tizkova"
date: "2024-02-19"
url: "https://e2b.dev/blog/community-contribution-autogen-code-interpreter-with-e2b"
category: "ai-agents"
site: "e2b"
---

Last week, our community contributor built an open-source [cookbook example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/autogen-python) of a code interpreter using AutoGen agents.

The LLM-generated code in this example project is executed in the cloud, using [E2B sandbox](/docs). By default, AutoGen agents do the code execution locally via Docker which can be [limiting](/blog/limitations-of-running-ai-agents-locally) for some use cases or possess some [risks](/blog/microsoft-s-autogen).

### The E2B Sandbox

The [E2B Sandbox](/docs) is a secure way to run your AI app. It is a long-running cloud environment where you can let any LLM (GPTs, Claude, local LLMs, etc) use tools exactly like you would do locally. E2B is fully [open sourced](https://github.com/e2b-dev/e2b) including the infrastructure layer. To try E2B sandboxes for free, start with [documentation](/docs).

### Credits

The author of this example is [Keegan McCallum](https://github.com/keeganmccallum), the founder of [Xler.ai](https://xler.ai/). Xler is a general-purpose multi-agent platform built on top of AutoGen. It also provides production-grade services like evaluation, deployment, monitoring, and fine-tuning.

### Want to show your example?

Write us at [hello@e2b.dev](mailto:hello@e2b.dev) or make a pull request to the [E2B cookbook](https://github.com/e2b-dev/e2b-cookbook). We have a strong preference for accepting projects such as LLM-powered code interpreters or coding AI agents. The condition is that the app uses E2B sandboxes.

Check out other open-source community examples in the [E2B cookbook.](https://github.com/e2b-dev/e2b-cookbook)