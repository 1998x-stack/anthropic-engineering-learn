---
title: "How to Use Memory in Agent Builder"
author: "LangChain Accounts"
date: "2026-02-19"
url: "https://www.langchain.com/blog/how-to-use-memory-in-agent-builder"
---

LangSmith

# How to Use Memory in Agent Builder

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9dca2e29eee5bae5072_memory-agent-builder-post.png)*By Jacob Talbot*

Agent Builder gets better the more you use it because it remembers your feedback. Every correction you make, preference you share, and approach that works well is something that your agent can hold onto and apply the next time.

Memory is one of the things that makes Agent Builder feel like a teammate. But like any teammate, it helps to know how to communicate with them effectively. Here are three practical ways to make the most of your agent&#x27;s memory.

[Try Agent Builder free](https://www.langchain.com/langsmith/agent-builder?ref=blog.langchain.com)

### A quick primer on how memory works

Before we dig into the tips, it helps to understand what&#x27;s actually going on under the hood. You can skip ahead to the tips if you&#x27;d prefer.

Agent Builder is built on [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com), LangChain&#x27;s open source agent harness for autonomous, long-running tasks. Your agent has access to an LLM for reasoning, tools for taking actions (like web search, Slack, or Google Sheets), the ability to spawn subagents, and a filesystem.

That filesystem is where memory lives. There are two types of memory:

- **Short-term memory:** Files your agent creates during a task such as plans, outputs from tool calls (such as web search results), and task progress. These exist for the duration of the conversation, or [thread](https://docs.langchain.com/oss/python/langgraph/persistence?ref=blog.langchain.com), but don’t persist across conversations.
- **Long-term memory: **Files your agent saves to a persistent path ([/memories/](https://docs.langchain.com/oss/python/deepagents/long-term-memory?ref=blog.langchain.com)). These stick around across every conversation. Your agent&#x27;s core instructions and skills live here. Memory is stored using standard Markdown files.

That&#x27;s really it. Memory sounds abstract, but it&#x27;s just files your agent can read and write to get better at its job.

### Tell your agent to remember

When you&#x27;re working with your agent, you&#x27;re constantly generating useful context. Maybe you&#x27;ve iterated on a format that works well, or you&#x27;ve refined exactly how you want results presented. That context lives in short term memory but it doesn&#x27;t have to stay there.

You can tell your agent to save what it&#x27;s learned. Try something like:

&quot;That approach worked really well. Update your instructions to always use that going forward.&quot;

&quot;Remember that I prefer bullet points over long paragraphs.&quot;

&quot;Incorporate what you learned from this conversation into your memory.&quot;

Your agent will update its long-term instructions based on your feedback in the same way a teammate would take notes after a productive working session. Over time, this means fewer corrections and better results from the start.

In practice, this step isn&#x27;t always necessary. If you give your agent clear feedback, like &quot;Change your writing style to direct, concise prose,&quot; it will recognize that as something worth remembering. It&#x27;ll propose the change to its instructions and ask for your approval before saving it. Telling your agent to remember is most useful when the takeaway is less obvious, such as when you&#x27;ve been iterating on a problem together and arrived at an approach that works, but never stated it explicitly.

0:00                            /0:231×

### Use skills for specialized context

Skills are a form of long-term memory, but with an important distinction: they&#x27;re only loaded when the task calls for them. Think of it like giving your agent a reference library instead of making it memorize everything upfront. The agent sees the titles on the shelf and only pulls a book down when it&#x27;s relevant.

This matters because more context isn&#x27;t always better. An agent trying to hold onto everything at once can lose focus on what matters for the current task. This can lead to hallucinations.

Here&#x27;s a practical example. I have an agent I use for writing content about our products. When I&#x27;m writing about LangSmith Deployment, I want the agent to reference that product&#x27;s features, audience, and positioning. When I&#x27;m writing about Agent Builder, it needs different context entirely. And when I&#x27;m writing about something unrelated, like LangChain’s upcoming agent conference, [Interrupt](https://interrupt.langchain.com/?ref=blog.langchain.com), it doesn&#x27;t need detailed product context at all.

So I set up skills for each product. My agent&#x27;s core instructions handle voice and writing style. The skills handle product-specific context. The agent pulls in the right skill based on what I&#x27;m writing about and ignores the rest.

You can ask your agent to create a skill anytime: &quot;Create a skill for [topic] that includes [what context the agent needs].&quot;

0:00                            /0:101×

### Edit your agent&#x27;s memory directly

Your agent’s instructions and configuration files are accessible to edit directly. You don&#x27;t need to do this because Agent Builder updates its own instructions based on your feedback. But there are two good reasons to consider it.

It helps you understand how your agent thinks. Reading your agent&#x27;s instructions is like reviewing a teammate&#x27;s project plan. You can see how the agent is approaching your problem, what it prioritizes, and where its assumptions might not match yours. If something looks off, such as an unnecessary step or a wrong assumption, you can fix it directly.

Sometimes it&#x27;s just faster. If you want to change when a scheduled task runs, or tweak a single line in the instructions, a direct edit takes seconds. Asking the agent to make the change works too, but for small, precise updates, editing the file yourself can be the quickest path.

To view and edit your agent&#x27;s instructions, you can navigate to the agent&#x27;s memory files.

0:00                            /0:151×

### Start building

These are a few simple ways to make your agent smarter over time: tell it to remember, give it specialized skills, and don&#x27;t be afraid to look under the hood.

If you build something you love, share it with us in the [Community Slack](https://www.langchain.com/community?ref=blog.langchain.com).

[Try Agent Builder](https://www.langchain.com/langsmith/agent-builder?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)