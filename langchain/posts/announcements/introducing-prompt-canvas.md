---
title: "Introducing Prompt Canvas: a Novel UX for Developing Prompts"
author: "LangChain Accounts"
date: "2024-11-12"
url: "https://www.langchain.com/blog/introducing-prompt-canvas"
---

Observability &amp; Evals

# Introducing Prompt Canvas: a Novel UX for Developing Prompts

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 12, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae473d7d286a58fa59c6_Screenshot-2024-11-10-at-12.00.49-PM.png)What it means to “build” applications is changing. When building AI applications, you are not just writing code - you’re also writing prompts. Tooling has evolved over the years to make software engineering more accessible - like code editors, code collaboration tools, pen testing, and more. We believe that tooling will emerge that makes **prompt engineering** just as accessible.

To that end, we are excited to announce Prompt Canvas, a novel UX for developing prompts. On top of a better editing experience, it also facilitates the sharing of prompting best practices - a game changer in a new discipline like prompt engineering.

## **What Is Prompt Canvas?**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae473d7d286a58fa59c6_Screenshot-2024-11-10-at-12.00.49-PM.png)

Prompt Canvas is an interactive tool designed to simplify and accelerate the prompt-creation experience. With Prompt Canvas, you can collaborate with an LLM agent to iteratively build and refine your prompts. This approach not only saves time but enables you to craft highly optimized prompts for any use case.

Instead of manually adjusting your prompt to follow best practices, Prompt Canvas leverages the expertise of an LLM agent to automate prompt development and offer guidance. This interactive and conversational setup makes prompt creation dynamic, empowering you to optimize as you go, while still maintaining control over the process.

Many of the features are inspired by the recent “Canvas” UX that OpenAI launched. We think the “Canvas” UX is fantastic for collaborating on documents with AI, much better than chat. At the end of the day, prompts are just a specific type of document - so it makes complete sense to bring this experience to prompting.

### How to Use Prompt Canvas

Prompt Canvas is built with a dual-panel layout:

**Chat Panel**

The chat panel is where your collaboration with the LLM agent takes place. You can:

- Request prompt drafts or adjustments to existing prompts. Each request generates a new version of your prompt, which you can iterate through to compare performance.
- Ask questions about your prompt, like, “What improvements can I make?” or “Is my prompt too long?”

**Canvas**

The canvas provides a hands-on editing area where you can:

- Directly edit your prompt.
- Select specific text for targeted feedback or adjustments from the agent.
- Utilize quick actions to quickly alter your prompt:
Default actions include adjusting reading level or length.
- Define/apply custom quick actions tailored to your workspace, making it easy to apply team-wide prompt standards (more on this later).

- View differences between the current and previous versions, making it clear how each change impacts the prompt.

### Custom Quick Actions

While most of the features are very similar to OpenAI’s Canvas UX, “custom quick actions” are one that we added in ourselves.

This was born out of talking to companies and hearing a pain point around sharing best practices of how to prompt. We are still extremely early on in “prompt engineering” as a field, and not that many people have a ton of expertise. What we consistently saw was that there may be a few prompting experts, and they wanted to share their knowledge with others in the organization. Custom quick actions enables exactly this.

With custom quick actions, you can define quick actions to apply to the prompt at an organization level — this makes it easier to maintain consistent style and structure in your prompt design when working with other stakeholders For example, if your expert prompt engineer has a specific format they like to write prompts in, they can just write a quick action to reformat prompts in that way; then, all other developers will be able to easily apply that to their prompt with one click!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae483d7d286a58fa59d2_Screenshot-2024-11-11-at-11.02.03-AM.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae483d7d286a58fa59ce_Screenshot-2024-11-11-at-11.01.51-AM-1.png)

### **Ready to Try It?**

Whether you’re building a prompt from scratch or modifying an existing prompt, Prompt Canvas offers a robust set of tools to make prompt engineering a collaborative and more efficient process.

See our [walkthrough video](https://youtu.be/nXrx-_9Yucc?ref=blog.langchain.com) on the Prompt Canvas for more information. And try it out inside the LangSmith Playground!

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