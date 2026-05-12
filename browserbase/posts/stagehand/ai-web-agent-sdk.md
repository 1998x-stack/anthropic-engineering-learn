---
title: "Stagehand gets even better – The AI Web Agent SDK"
author: "Anirudh Kamath"
date: "2025-04-07"
url: "https://www.browserbase.com/blog/ai-web-agent-sdk"
category: "stagehand"
site: "browserbase"
---

# Stagehand gets even better – The AI Web Agent SDK

![](https://cdn.sanity.io/images/yd6zslid/production/10bc88d1f54aa5e5e540a63bda82f56495022d8f-314x286.png?fm=webp&amp;h=1457&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Anirudh Kamath

![](https://cdn.sanity.io/images/yd6zslid/production/434ac786c934447c22ba10df244525f9321fc42e-1510x1504.png?fm=webp&amp;h=1594&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Ash Rathie

[Stagehand](/blog/stagehand/)

![](https://cdn.sanity.io/images/yd6zslid/production/16791d7e0582c285bca14b722de2709d3590b66d-856x579.png?fm=webp&amp;h=1082&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

In a landscape where conventional automation tools are painfully brittle and fully agentic solutions can be too unpredictable, Stagehand emerges as the best AI-powered browser automation framework available today. By combining atomic instructions with the flexibility of a dynamic agent, **Stagehand delivers a complete and robust framework for any Web AI Agent workflow.**

## TL;DR

- **Stagehand** is an AI web agent framework that bridges the gap between brittle traditional automation (e.g., Playwright, Puppeteer, Selenium) and unpredictable full-agent solutions (e.g., OpenAI Operator).
- It uses **atomic primitives** (act, extract, observe) for precise control and a **dynamic Stagehand Agent** for high-level decision making.
- Key innovations include cleaner data extraction via the **Chrome Accessibility Tree**, optimized **LLM selection**, and **better self-healing**.
- The integration of the **Model Context Protocol (MCP)** brings Stagehand to any external LLM—combining Stagehand with Claude delivers an OpenAI Operator alternative that’s more controlled and reliable.

## The Stagehand Philosophy: Control and Flexibility

Let’s be honest: traditional browser automation frameworks such as Playwright, Puppeteer, or Selenium are fantastic for executing explicit commands—click this here, type that there—but they crumble when a website changes just slightly. A tiny UI tweak can break an entire script, leaving you scrambling to fix brittle code. On the other end of the spectrum, full agent-based solutions like OpenAI Operator or Anthropic Computer Use promise full automation from just a prompt. You simply instruct the agent in natural language, and it takes over. However, that level of abstraction often comes at the cost of control—developers can end up with unpredictable outcomes.

Stagehand was born out of the need for a middle ground. Instead of forcing you to choose between writing fragile code or handing everything over to an opaque agent, Stagehand gives you the best of both worlds:

**Atomic Instructions:** The framework provides three key primitives—**act(), extract(), and observe()**—that let you define precise, one-to-one browser interactions. Think of these as the building blocks of reliable automation: you tell Stagehand to “click this button” or “type this text,” and it maps that command directly to a browser action. In the new Stagehand, act() no longer recursively loops. Complex, multi-step actions are now handled by agent().

```
await page.act(&quot;click on the contributors selection&quot;);

const { title } = await page.extract({
  instruction: &quot;the top contributor&#x27;s username&quot;,
  schema: z.object({
    title: z.string(),
  }),
});
```

**Dynamic** **Agent**: For those tasks that require higher-level decision making, Stagehand introduces the Stagehand agent(). This component breaks down even complex workflows into a sequence of browser commands. It allows you to delegate high-level instructions—like “retrieve the top 5 contributors to the stagehand repo”—while still maintaining granular control over how each step is executed. agent() caches the preview steps it took, reducing LLMs calls and optimizing performance. It makes new calls when the cached actions fail.

```

const {message,actions} = await.execute(

&quot;Extract the top contributor&#x27;s username&quot;

)
```

### A High-Level Use Case Comparison

Imagine you need to automate the process of filling out a web form and then extracting specific lead data:

- **Using Playwright (Traditional Automation):** You’d write explicit code to navigate to the form, identify each field, input data, and submit the form. While this offers precision, if the website’s structure changes even slightly (say, the form’s layout is updated), your code might break, leaving you with brittle automation.
- **Using a Fully Agent-Based Product (OpenAI Operator):** You’d simply instruct the agent in natural language: “Fill out this form and extract the lead information.” The agent would decide the best approach, but you’d lose control over which elements are interacted with and how. The process might work in some cases but could lead to unpredictable outcomes if the agent’s reasoning isn’t aligned with the desired precision.
- **Using** **Stagehand**: You can combine the strengths of both approaches. With Stagehand, you can use act, extract, and observe to issue precise commands (e.g., “click the submit button,” “extract the email field”) while also employing the Stagehand Agent for high-level orchestration when necessary. This gives you an automation script that’s both resilient to UI changes and flexible enough to handle complex decision-making processes.

### Real World Applications

Stagehand’s flexibility makes it an ideal choice for developers seeking reliable AI-powered browser automation. Here are a few examples of how developers are using Stagehand:

- **Automated Form Filling &amp; Lead Enrichment:** Consider a scenario where you need to extract lead information from hundreds of company websites. With traditional tools, you’d write and maintain brittle scripts that could break at the slightest UI change. A full agent solution might not provide the control you need to ensure accurate data capture. Stagehand, however, empowers you to design an automation pipeline that fills out forms with atomic precision and then dynamically enriches data using high-level reasoning—all while adapting to slight changes in the website’s layout.
- **Intelligent Document Editing:** Product managers and developers often need to compare documentation versions or even auto-generate code samples based on changes. The Stagehand Agent can review the documentation, compare it with a changelog, and suggest improvements all in one fell swoop. This hybrid approach makes the process more efficient and reliable compared to conventional manual editing or a fully automated agent that lacks context.
- **Robust Web Crawling for Data Extraction**: In applications where continuous, reliable data extraction is critical—such as monitoring pricing, gathering competitor intelligence, or even parsing news sites—Stagehand shines. By blending atomic commands with high-level agentic decisions, it enables your script to carry out tasks reliably and resiliently.

### What We Learned While Building Stagehand

The evolution to this new version of Stagehand has been a journey of discovery and refinement. Here are some of the key lessons the team learned along the way:

- **From Raw DOM to the Chrome Accessibility Tree:** Initially, our approach relied on parsing the raw DOM of web pages. However, we soon discovered that the Chrome Accessibility Tree offers a much cleaner, more reliable view of a webpage by filtering out unnecessary noise. This shift not only improved the accuracy of actions but also increased the overall resilience of our automation scripts. Previously an optional flag, this is now the default behavior in the new version of Stagehand.
- **Understanding LLM Behavior:** In building Stagehand, we tested various large language models (LLMs) and found that they each have their unique strengths. For instance, Claude excels in high-level reasoning, making it ideal for dynamic decisions, whereas GPT-4o and GPT-4o mini are better suited for executing specific browser actions. Conversely, Gemini struggled with structured outputs, but is really good at observe(). These insights allowed us to fine-tune our integrations, ensuring that Stagehand delivers the highest-quality overall performance.
- **Implementing Multidimensional Self-Healing**: A major challenge was building highly resilient self-healing by understanding intent rather than just actions. If a single element changes, your script might fail. If you’ve built in some level of self-healing, then perhaps your script can re-examine the page to find a viable alternative. But what happens if a button disappears altogether? There is no clear alternative to “click the Pricing button”. Stagehand’s multidimensional self-healing option allows you to fall back to a full agent that reviews what has happened and reassess the overall goal. The agent then decides how to complete the task using the current context. The end result is minimized downtime as your automation keeps running smoothly even when unexpected changes occur.

![](https://framerusercontent.com/images/DxkJfgkWBXIKVQCwTBM3mjy9Fk.png)

### MCP Integration

In addition to its core framework (act(), extract(), observe(), and agent()), the capabilities of Stagehand can also be leveraged through MCP (Model Context Protocol). Particularly effective with Claude, the Stagehand MCP enables external agentic AI to perform browser actions better than any alternative—effectively emulating OpenAI Operator, but with far greater control and reliability. In practice, this means that when you instruct an agent with access to Stagehand MCP, it translates natural language prompts into a structured, reproducible sequence of browser operations. See it in action or experience it yourself. Browserbase has been a pioneer in the open source MCP community (we first released our MCP server in November 2024).

![](https://framerusercontent.com/images/7k2A82QeOUdbOB0yNP1vLH2Ba0.png)

### Open Source, Developer Support &amp; Community

![](https://framerusercontent.com/images/bAviGPxjGjRyI73m8fRNOKPZ4rA.png)

Trust and transparency are critical as we create new AI capabilities. We believe the best way to achieve that is through open source. A vibrant community of developers continue to contribute, refine, and build upon Stagehand, making it even more innovative and high-quality. Comprehensive documentation, active support from the team (reach out to Ani at [anirudh@browserbase.com](mailto:anirudh@browserbase.com)), and regular community feedback ensure that Stagehand remains a reliable and cutting-edge solution.

This open source model has proven invaluable. It allows developers to understand exactly how the automation works, customize it to their needs, and even suggest improvements that can be quickly integrated. The result is a robust ecosystem where trust and collaboration drive continuous innovation—exactly what you’d want from an AI web agent framework.

### Stagehand, Now and in the Future

Where is the world of AI web agents headed? The conversation is evolving, and the future holds both great opportunities and tough challenges. How we use AI web agents today is not how we will use them in five years.

Imagine a future where an ecosystem of mini-agents emerges—each one specialized in its own domain yet working together on complex tasks. In this vision, the main agent could delegate specific jobs to sub-agents that handle form filling, image recognition, data extraction, and more. This microservice-like approach is an evolution we are already beginning to see, especially as MCP gains momentum.

Alternatively, we might reach a point where a single, highly agentic AI performs all actions without assistance. Whatever the future may bring, we at Browserbase are always thinking about how the space is evolving. Today, developers need both control over the workflow and relief from the tedious details, and that’s the balance we wanted to strike with Stagehand 2.0. As this balance shifts, Stagehand will evolve with it.