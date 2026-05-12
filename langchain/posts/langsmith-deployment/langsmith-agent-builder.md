---
title: "Introducing LangSmith’s No Code Agent Builder"
author: "LangChain Accounts"
date: "2025-10-29"
url: "https://www.langchain.com/blog/langsmith-agent-builder"
---

Company AnnouncementsLangSmith

# Introducing LangSmith’s No Code Agent Builder

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 29, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa4ebf847dfe35eeea97_Blog-04--1--1.png)*By Brace Sproul and Sam Crowder*

Today, we’re expanding who can build agents beyond developers. While a lot of the highest volume, customer-facing agents will be built by technical teams, nearly every business user has use cases for agentic applications in their daily routines. Our new **LangSmith Agent Builder** provides a no code agent-building experience — complete with memory and guided prompt creation — that lowers the barrier to building agents.

[Try Agent Builder](https://smith.langchain.com/?ref=blog.langchain.com) today, and learn more about our approach below.

## What’s different

We’ve spent the past three years building agents alongside millions of developers. We hear from engineering teams how much their colleagues want to build their own agents. Even technical users have asked for faster ways to get started with agents that doesn&#x27;t always involve writing and deploying code.

That’s why we’re launching **LangSmith** **Agent Builder** in private preview. It empowers everyone in an organization to build agents in a safe and accessible way. Unlike other solutions out there, LangSmith Agent Builder is an agent builder, [not a visual workflow builder](https://blog.langchain.com/not-another-workflow-builder/). Visual workflows builders have two major pitfalls:

- **A visual workflow builder is not “low” barrier to entry.**
- **Complex tasks quickly get too complicated to manage in a visual builder.**

Rather than follow a predetermined path, agents can delegate more decision-making to an LLM, allowing for more dynamic responses. By focusing on letting users build agents, we make agent building accessible to a broader audience while enabling users to tackle more complicated and complex tasks, rather than simple workflows.

## What an agent consists of

Every agent in LangSmith is built from four core components that work together:

- **Prompt: **This is the brain of your agent containing the logic to describe what the agent should do. With LangSmith agents, all the complexity of the agent is pushed into the prompt (rather than into a complex visual workflow). Writing good prompts is hard but really important, which is why we&#x27;ve built tools to make it easier (learn more in the next section).
- **Tools:** In order to interact with the world, agents need to call tools. LangSmith uses MCP to connect your agent to external services and data. We provide built-in tools, but you can also easily bring your own MCP servers. With LangSmith’s new Agent Authorization functionality, you can securely connect to tools your team has approved such as Gmail, Slack, LinkedIn, or Linear – all within the agent building flow.
- **Triggers: **Agents don&#x27;t just respond to chat messages – they can also act automatically on background events. Set up triggers to launch your agent when you receive an email, get a Slack message in a particular channel, or on a time-based schedule.
- **Subagents: **We recommend starting out by putting most complexity in the prompt. But as complexity grows, you may want to keep the system manageable by creating smaller, more focused subagents for specific tasks.

## How we make it easier to build your agent

We&#x27;ve consistently seen that the hardest part of building agents is **writing effective prompts**. Two challenges make this difficult:

- Good prompts require detail and specificity, but most people lack prompt engineering experience.
- Prompts need to evolve or be updated as you discover edge cases and new requirements.

We&#x27;ve set out to make these things easier:

- **Start with a conversation** **instead of a blank canvas**. First, start with your request and describe what you want your agent to do in plain language. The system then asks you follow up questions to get the details right, auto-generates your agent&#x27;s system prompt, connects tools, and sets triggers based on your answers. This guided conversation makes it easy to create detailed, effective prompts without prompt engineering expertise.
- **Have your agent remember over time.** LangSmith agents have built-in memory for not only their prompt but also the tools that they (and any subagents) have access to. At any point, the agent can update its memory. If you correct the agent, it will now remember that correction so you don&#x27;t have to prompt it to do so again in the future.

LangSmith Agent Builder is great for internal productivity use cases like email, chat, and Salesforce assistants. For instance, you can build an agent to send you a summary of your schedule with meeting prep every day. You could build an email agent that dynamically creates next steps based on the message, from creating Linear tickets, to drafting responses, or sending a Slack message. And, you can make sure to approve any messages before they get sent.

We&#x27;ll continue to expand what&#x27;s possible with Agent Builder based on community feedback — [start building with Agent Builder](https://smith.langchain.com/?ref=blog.langchain.com) to help shape what comes next.

## Under the hood

We’ve incorporated learnings from the last three years building open source agent frameworks LangChain and LangGraph, as well as our early iteration of this product Open Agent Platform, to inform our design decisions.

Today, LangSmith Agent Builder is built on top of our `deepagents` package. Deep Agents gives your agents access to planning capabilities, persistent memory, and the ability to break down complex tasks into manageable subtasks. This means your agent can handle complex, multi-step workflows without you needing to map out every possible scenario; they problem-solve in real time.

For folks already using the LangChain ecosystem of tools, here&#x27;s a table with some tips on when to use LangSmith Agent Builder vs. our open source frameworks.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa4fbf847dfe35eeeacb_Screenshot-2025-10-28-at-6.49.38---PM-1.png)

## Try Agent Builder

If you’re interested in checking out the new experience, you can [try Agent Builder](https://smith.langchain.com/?ref=blog.langchain.com) today! We can’t wait to hear input from the community to continue to improve the experience for everyone.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)