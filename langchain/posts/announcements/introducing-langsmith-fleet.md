---
title: "Introducing LangSmith Fleet"
author: "LangChain Accounts"
date: "2026-03-19"
url: "https://www.langchain.com/blog/introducing-langsmith-fleet"
---

Company AnnouncementsLangSmith

# Introducing LangSmith Fleet

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 19, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)5min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c1e5c865d9ed460b62_Introducing-Fleet-2.png)Today we’re launching LangSmith Fleet - an enterprise workspace for creating, using, and managing your fleet of agents. These agents have their own memory, have access to a collection of tools and skills, and can be exposed through the communication channels your team uses every day.

A key part of LangSmith Fleet (formerly LangSmith Agent Builder) is its agent identity and agent sharing model. A credentials model controls who your agent acts on behalf of. A permissions model gives you control over who can use, edit, and share each agent in your workspace.

[Try Fleet](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com)

## From building agents to managing your agent fleet

Just six months ago, building an agent required an engineer. Today, anyone on your team can describe a task in a short prompt and generate an agent to handle that job for you. That&#x27;s how fast things have evolved.

We launched Agent Builder in October to enable knowledge workers to create their own agents with natural language. Since then, we’ve seen a consistent pattern: teams start with one or two agents for simple tasks like research or status checks. Then use cases expand and they start running more tasks across more agents. This allows people to offload many repetitive tasks that eat up the day so they can focus on the aspects of their job that require human judgment.

When agents are this easy to create, the hard part shifts to managing them: who owns which agents, how they authenticate across tools, who can audit what they do, and how to share a good one across the organization securely.

That&#x27;s what LangSmith Fleet is for.

- **Creating** agents with a simple prompt
- **Sharing** so centralized teams can publish agents and team members can share
- **Permissions** so you control who can edit, run, or clone each agent
- **Agent identity and credentials** so you define how agents authenticate with company tools
- **Inbox** so users can track agent activity and approve actions with human-in-the-loop
- **Observability** to provide an auditable record of what every agent did and why

## Tiered permissions and sharing

A good agent is valuable to the whole team. A vendor intake agent can serve your ops org. A weekly report agent can save every account manager thirty minutes on Monday morning. But sharing an agent across the enterprise requires control over who can modify it, who can use it, and who gets their own copy to customize. You can now configure all of this for each agent you create with Fleet.

Agent sharing has two dimensions: who gets access, and what they can do.

**Who:** Share with individual users or with your entire workspace.

**What:** Three permission levels:

- **Can clone**: Clone the agent into their own version to customize
- **Can run**: Use the agent without modifying its configuration
- **Can edit**: Full access to change instructions, tools, and settings

You can layer these as needed. Give your core team edit access and share run-only with the broader workspace. Change or revoke permissions at any time.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c2e5c865d9ed460b6b_sharing-3.png)

## Agent identity and credentials

When multiple people run the same agent, it needs a secure way to authenticate with external tools. Sometimes each user should authenticate individually. Sometimes a shared service account makes more sense. You now have both options, configurable per agent.

**&quot;Claws&quot;** have a fixed set of credentials regardless of who runs them. Users don&#x27;t need to log in for each tool. This has been the default in Fleet, and it&#x27;s useful for something like a Linear Slack bot, where your entire team searches and creates issues using the same credentials.

**&quot;Assistant&quot;** agents act on behalf of the user who invokes them. Each user authenticates with their own account for each connected tool that requires credentials, using OAuth in Fleet. The agent acts within that user&#x27;s permissions. This makes sense for something like a team knowledge base in Notion, where each user has different document access.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c2e5c865d9ed460b71_agent-identity.png)

## Agent identity for Slack bots

Fleet agents can already respond to messages in Slack. With agent identity, each agent can now have its own Slack bot.

Instead of routing everything through a single Slack bot, each agent can now be triggered with its defined name. Create a bot for each job and give it a Slack handle: `@vendor-intake`, `@weekly-sales-numbers`, `@onboarding-agent`. Your team can @mention an agent in a channel or DM it directly to hand off tasks without switching context.

Agent identity ties into permissions and credentials. A &quot;Claw&quot; with its own Slack bot works as a team resource. An &quot;Assistant&quot; agent is available only to users who authenticate with the agent&#x27;s tools.

We’re expanding these same principles of agent identity to additional channels in the coming weeks.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c2e5c865d9ed460b74_slackbot.png)

## Agent Inbox

When you have multiple agents running tasks in parallel across your org, you need one place to review what&#x27;s happening and act on it. The Inbox gives you human-in-the-loop oversight across all of your agents: review, approve, or reject actions for all of your agents from one central place without switching across tabs. This works for both &quot;Assistants&quot; and &quot;Claws,&quot; based on specific permissions.

With &quot;Claws,&quot; only users with edit access can review agent actions in the Inbox. They can view and respond to each thread. This is useful for an IT admin who needs to track agent activity, or a team lead who wants to review the issues an agent created and approve actions before they go out.

With &quot;Assistants,&quot; each user&#x27;s actions stay private to that user’s Inbox. That&#x27;s what you want for an agent that handles sensitive personal tasks like reading private documents in Notion.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c2e5c865d9ed460b6e_inbox.png)

## Agent observability

LangSmith already provides native tracing for every agent action in Fleet. Every tool call, every decision, every output is captured in a structured trace that you can inspect, search, and export.

For enterprises, this is the audit trail. You can see exactly what an agent did, why it made each decision, and what data it accessed. This works across both agents you build in code and agents created with Fleet.

When combined with agent identity and permissions, tracing gives you a complete picture: which agent acted, on whose behalf, with what credentials, and what it did at each step.

## **From one agent to an enterprise fleet**

Most teams follow the same path: one person builds a good agent. A colleague tries it. Then the team begins running agents across their daily work. Fleet is built for that progression, giving you the control to share agents across your organization and visibility into their actions.

We&#x27;re actively expanding Fleet, with more coming soon for agent sharing, identity, and safe, autonomous work in the weeks ahead.

[Try Fleet](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com)

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