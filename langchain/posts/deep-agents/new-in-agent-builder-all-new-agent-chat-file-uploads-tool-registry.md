---
title: "New in Agent Builder: all new agent chat, file uploads + tool registry"
author: "LangChain Accounts"
date: "2026-02-18"
url: "https://www.langchain.com/blog/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry"
---

LangSmithObservability &amp; Evals

# New in Agent Builder: all new agent chat, file uploads + tool registry

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 18, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9de29c6654c43484275_LangSmith-Agent-Builder-1.1-4.png)Today, we&#x27;re expanding what you can do with [LangSmith Agent Builder](https://www.langchain.com/langsmith/agent-builder?ref=blog.langchain.com). It’s an big update built around a simple idea: working with an agent should feel like working with a teammate.

We rebuilt Agent Builder around this idea. There is now an always available agent (”Chat”) that you can use to run ad hoc tasks or create specialized agents. We’ve also added the ability for agents to use uploaded files and make it clear what tools your agents can use.

[Try Agent Builder free](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com).

### **Here’s what’s new**

- **One agent with all your tools:** A central “Chat” agent now has access to every tool in your workspace, so you can ask questions and take actions without creating a dedicated agent.
- **Turn any chat into an agent:** Work through a task conversationally, then turn it into a recurring agent with one click.
- **Upload files:** Add CSVs, images, and text files directly into chat for data analysis, image processing, or to give your agent reference material.
- **Manage tools in one place.** View, authenticate, and add tools from a single tools registry, with admin controls for governance.

## One agent with all your tools

Agent Builder Chat can access every tool you’ve connected to your workspace, such as Slack, Gmail, Linear, Pylon, and any others you&#x27;ve connected with [remote MCP server](https://docs.langchain.com/langsmith/agent-builder-remote-mcp-servers?ref=blog.langchain.com). That means you can ask questions like &quot;What are my open Linear tickets?&quot; or &quot;Summarize today’s requests in #support&quot; without needing to set up a dedicated agent first.

Type a question or request, then Agent Builder makes a plan, pulls in the right tools, and works through it step by step. If something needs your approval, like sending a message or creating a ticket, it loops you in before taking action.

Agent Builder can also string together multiple tools based on your needs. If you’re catching up on emails, you can ask for a quick summary of the last 10 messages. Then ask it to create calendar events for any meeting requests. Agent Builder calls new tools as required.

You can run multiple chats at once. Kick off a task in one conversation, open a new thread, and work on something else. Each chat runs independently so you can come back to any of them to check progress, approve actions, or ask follow-up questions.

0:00                            /0:231×

## **Turn any chat into an agent**

This central Chat agent enables a new powerful way to create agents. You start with a question like, &quot;Create a summary of this week&#x27;s support tickets from Pylon and draft a Slack update for my team.&quot; Agent Builder works through the task and you refine the output with feedback.

At any point, you can select &quot;Turn this conversation into a reusable agent” to create an agent for that task.

That&#x27;s it. You&#x27;ve got a recurring agent ready to manage things for you going forward. There’s no prompt engineering and no if/then logic to work through. Your conversation with Agent Builder is the setup. And every conversation is saved for future reference, so you can always return to a task in the future to make it an agent, even if you didn’t think to do so in the first place.

We&#x27;ve seen this pattern work especially well for:

- **Research:** &quot;Find the latest news about my top 10 customers from the web and send me a summary in Slack.&quot;
- **Writing:** &quot;Review the last 20 posts on our company blog and develop a voice and tone guide as a Google Doc.&quot;
- **Summarization:** &quot;Pull this week&#x27;s Linear issues, analyze trends, and draft a summary.&quot;
- **Communications:** &quot;For each new lead in HubSpot, research their company and draft a personalized outreach email.&quot;

For any agent you create, you can trigger them manually, put them on a schedule, or have them respond to external events, like a Slack message or email. And because they started with a real conversation with you, they already know what a good output looks like.

0:00                            /0:351×

## **Upload files to any conversation**

Until now, Agent Builder could only work with data from your connected tools and things you wrote in chat. Now you can upload files directly, like a CSV, a screenshot, or a style guide, and your agent can act on them. Uploading files enables new capabilities like:

**Analyze data on the fly.** Upload a CSV, such as last quarter&#x27;s sales numbers, and ask Agent Builder to find trends and send a report to your team in Slack.

**Work with images.** Upload a screenshot or photo, and ask Agent Builder to use it, such as converting a photo of whiteboard notes into a Google Doc.

**Import docs and reference material.** Upload a writing style guide or an existing prompt to give your agent a head start. This is especially useful when you&#x27;re building a new agent.

## **Manage your tools in one place**

We&#x27;ve also made it easier to see and manage all of your tools in one place.

From your workspace settings, you can view all connected tools, authenticate new ones, and add remote MCP servers. If a tool needs re-authentication, you&#x27;ll see it right away. And when you connect a new tool, it&#x27;s immediately available to all of your agents.

Only workspace administrators can add new tools, so your team stays in control of what tools agents can access.

## **Try it out**

That’s the update: a central chat that can use all your tools, conversations that you can turn into agents, file uploads, and simpler tool management. All of this makes it easier to go from working on a problem to having an agent handle it for you.

If you haven&#x27;t tried Agent Builder yet, this is a great time to start. And if you&#x27;re already building, we&#x27;d love to [hear what you think](https://www.langchain.com/join-community?ref=blog.langchain.com).

[Try Agent Builder free](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com).

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