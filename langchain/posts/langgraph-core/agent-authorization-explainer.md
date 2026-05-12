---
title: "Securing your agents with authentication and authorization"
author: "LangChain Accounts"
date: "2025-10-13"
url: "https://www.langchain.com/blog/agent-authorization-explainer"
---

Deep AgentsTutorials &amp; How-Tos

# Securing your agents with authentication and authorization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamOctober 13, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa69431a71bcb2864063_Agent-Auth.png)Lately, every company has been rushing to build agents. And unlike the AI applications of years before, agents aren't limited to chat. Agents are notable because they can take action; they can fetch files, send messages, call tools and update records — which makes the stakes higher and warrants a more thoughtful approach to securing them.

### Access Control Primer

To access sensitive data and use tools, agents need to be authenticated and authorized. While often used interchangeably, the two terms have distinct meanings:

- Authentication (AuthN): verifies *who* you are. When accessing data, your agent needs to have a distinct identity from all the other users or applications that also want access.
- Authorization (AuthZ): determines *what you can do*. Your agent should have limits on what data it can access or what actions it can take.

Authentication and authorization (collectively referred to as “auth”) are relevant to all types of applications, not just agents. To that end, there are existing frameworks like OAuth 2.0 to facilitate AuthN/Z. Many identity providers today have built extensive services on top of OAuth 2.0 to allow developers to implement access control in their applications. However, compared to the applications served by existing solutions, agents have some unique attributes that make it useful to create additional constructs for access.

### What Makes Agents Different?

The biggest distinctions between agents and traditional applications are:

- Compared to most applications, agents will need to access an extremely large number of services and tools.
- Agents are dynamic, and have significantly more fluid access needs.
- Agents are more complex to audit than traditional applications.

Each of these new attributes comes with new considerations for agent authentication and authorization. We break them down below.

**1. Agents will need to access an extremely large number of services and tools:**

- Common constructs will be useful to standardize tool access from agents
- A standardized interface abstracting common OAuth 2.0 flows will simplify giving agents access to the data they need

**2. Agents having significantly more fluid access needs:**

- Traditional applications have structured access needs, where the scope of the application’s behavior is well defined. This means access controls can afford to be simpler, mainly checking if a user is allowed to consent to whatever permissions the app is requesting.
- Agent behavior is nondeterministic, not well-defined. The correct level of access may be heavily context dependent, which can make it useful to set rules like “Agent A is never allowed to request consent for permission A” or “Agent B must request consent each time permission C is needed”

**3. Agents are more complex to audit than traditional applications:**

- Due to the number of services agents can access, audit logs may be spread across many providers
- Each call to an agent may involve many services and actions, which makes individual access trajectories more difficult to interpret
- Agents benefit more from a centralized location to track audit events and analyze access patterns

Taken together, these considerations form the shape of a centralized framework to manage agent authentication and authorization. It should consolidate auditable events and allow flexible rule configurations to match the dynamic access needs of agents. In essence, an auth server for agents.

### An Agent Auth Server

What might such an auth server look like? We could draw inspiration from existing paradigms for human access, such as Role Based Access Control (RBAC) or Just in Time (JIT) access.

RBAC is an access control mechanism that grants humans access to resources based on their role. Instead of tying permissions to a particular user’s identity, the permission is tied to the role the user holds (i.e. administrator). Roles can be granted and removed from users to dynamically adjust their access based on changing conditions, which can help fulfill the fluid access needs of agents.

JIT access is a security principle where users are granted temporary, privileged access to systems or resources only when needed, for a limited time. For agents, JIT access could be an effective method to allow agents to do powerful things while minimizing potential security risks.

By consolidating agent auth through a single service, access to tools and resources can be centralized and standardized. The server could consolidate disparate audit events, and organize them for easier review.

While some of these components are still being built, that doesn’t mean you, as a developer, cannot build authentication and authorization into your agents today. The foundational frameworks of auth, like OAuth 2.0, can still be used to secure your individual agentic applications.

### Agent AuthN and AuthZ Today

Though agents bring new challenges, at a high level they share many similarities with traditional applications. At their core, they’re pieces of software that want access to resources. Most modern applications today use the OAuth 2.0 framework for authorization and the OIDC framework built on top of OAuth 2.0 for authentication. Agents can also effectively use these standards.

However, OAuth 2.0 covers a lot of ground, and not all flows will be relevant for the agents you build. Access patterns can be broadly broken into two categories: Delegated Access and Direct Access

Delegated Access
Direct Access

Definition
The agent needs to access a resource on behalf of a user
The agent needs to access a resource without user involvement

Agent Types
Useful for agents dedicated to fulfilling human requests OR agents reliant on human oversight
Useful for ambient agents, which can trigger off events, or agents conducting autonomous processes

Benefits
Delegated access allows you to limit your agent’s permissions to what the human is allowed to do. It also lets you associate agent actions with human approvers
Direct Access access allows your agents to operate independently of humans, and identify when agents are conducting fully autonomous flows

Examples
An email assistant needing access to your emails would need you to delegate access to read your emails
A security agent triaging large amounts of incidents might need access to system logs independent of a human

In practice, most agents will have some tasks where they need delegated access, and some where they want direct access. Most of these access scenarios can be covered by a few particular OAuth flows, which we’ll break down in this next section.

### Delegated Access

Let’s list some common requirements for tasks in which agents need delegated access.

- The agent needs to fulfill human requests, and is available to users as a service
- Users should not be able to view the requests of other users without explicit permission. This means you need to…
Identify who the user accessing your agent is — meaning you need to authenticate users
- Control whether users have access to view a particular request to your agent — meaning you need to authorize your users

- The Agent needs to access data across several platforms (Microsoft, Slack, Jira, Google, Datadog, etc.) to do useful work. This means…
Your agent needs to obtain access to other services — meaning your agent needs authorization from these other services
- While handling user requests, your agent should be limited to what the user is allowed to do. If the user can’t view a top secret Microsoft document, the agent shouldn’t use that document when answering their question.

The most common OAuth 2.0 flow used to fulfill Requirement 2 is [**Auth Code Flow**](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow?ref=blog.langchain.com)**.**

The OAuth 2.0 flow used to fulfill Requirement 3 is the [**OBO (On-Behalf-Of) Token Flow.**](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow?ref=blog.langchain.com)

**In most delegated access scenarios, Auth Code Flow and OBO Token Flow are all you need for your agent.**

### Direct Access

We can take the same approach for Direct access, and list some requirements:

- Your agent needs to access one or more services without human involvement. This means…
Other services need to be able to identify your agent and distinguish it from other applications — meaning your agent needs to be authenticated to these services
- Your agent needs access to other services — these services need to authorize your agent to control what it has access to

**The OAuth flow used to accomplish the Direct Access scenario above is the **[**Client Credentials Flow**](https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow?ref=blog.langchain.com)

- Client Credentials flow requires that your agent is running in a private environment where its source code is not exposed to third parties - so no mobile apps or Single Page Apps (SPAs)
- In production, it’s good practice to use a credential management mechanism to avoid long-lived credentials (which are vulnerable to compromise).

To recap, if you’re looking to set up access for your agent, there’s likely 3 flows you’ll need:

Type of Access
OAuth 2.0 Flows

Delegated Access
1. Auth Code Flow                          2. OBO Token Flow

Direct Access
3. Client Credentials Flow

### Conclusion

As agents become more capable, more autonomous, and more useful, the need for a good authentication and authorization story increases.

Part of that story is a continuation of what’s already been built: the existing standards of OAuth 2.0 and OIDC. If you need to implement auth for your agent, you’ll likely find yourself implementing Auth Code Flow, OBO Token Flow, or Client Credentials Flow.

However, agents *do* bring new challenges to the table. Agents will routinely span dozens of services, request access in fluid ways, and trigger chains of actions that are harder to audit. We believe there’ll be a need for new tooling to centralize control and standardize agent access.

We’ve written about [agent access control](https://blog.arcade.dev/agent-authorization-langgraph-guide?ref=blog.langchain.com) before with our friends at [Arcade](https://www.arcade.dev/?ref=blog.langchain.com), in case you’re interested in diving deeper.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ea236ce872ec8be413bd2f_runtime-behind-production-deep-agents-thumbnail.png)Conceptual GuideDeep Agents

#### The runtime behind production deep agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcee60745f0e15b18ad4d5_sydney-runkle.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)Sydney RunkleVivek TrivedyApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)24min[](/blog/runtime-behind-production-deep-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)