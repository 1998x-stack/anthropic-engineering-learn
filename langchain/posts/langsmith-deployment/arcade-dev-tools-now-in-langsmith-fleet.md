---
title: "Arcade.dev tools now in LangSmith Fleet"
author: "LangChain Accounts"
date: "2026-04-07"
url: "https://www.langchain.com/blog/arcade-dev-tools-now-in-langsmith-fleet"
---

LangSmith

# Arcade.dev tools now in LangSmith Fleet

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 7, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77adbe5726da9388ccc49_Arcade-tools-fleet.webp)

## Key Takeaways

Arcade is the MCP runtime for production agents, delivering secure agent authorization, reliable tools, and governance. This integration gives your agents access to Arcade’s collection of 7,500+ agent-optimized tools through a single secure gateway.

Today, we&#x27;re announcing a new partnership with Arcade.dev to bring their library of tools to LangSmith Fleet. Arcade is the MCP runtime for production agents, delivering secure agent authorization, reliable tools, and governance. This integration gives your agents access to Arcade’s collection of 7,500+ agent-optimized tools through a single secure gateway.

[**Try Fleet**](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com) |[** Try Arcade**](https://app.arcade.dev/register?ref=blog.langchain.com)

LangSmith Fleet enables every team to create, use, and share agents for daily work. Fleet agents can work across multiple tools autonomously, such as pulling data from Salesforce, updating a page in Notion, and sharing results in Slack. But this means that agents need to have reliable access to every tool a team depends on. Arcade&#x27;s MCP gateway gives agents a secure connection to all of these tools through one endpoint.

### **Centralized gateways for all your tools**

Gateways are a useful pattern for simplifying how agents connect to external services. LLM gateways centralize access and credentials for your model providers. That same logic applies to tools, where the cost of managing individual connections is even greater. Every new tool means its own auth flow, its own API quirks, and its own ongoing maintenance. Multiply that across all the tools your team uses and the integration tax adds up fast.

Arcade&#x27;s MCP Gateway gives your agents a single access point. Connect your Arcade account in Fleet, select your gateway, and your agents have access to Salesforce, Asana, Zendesk, and dozens of other applications in minutes.

You can create a single gateway for the whole organization, or a tailored gateway per team or use case. Users connect with their own credentials and get access to the tools relevant to their work, without adding to your engineering team&#x27;s backlog.

### **Not another API wrapper**

There are a lot of MCP servers available right now. Many of them take an existing REST API and wrap it in the MCP protocol. That gives you standardized tool discovery, which is useful, but it doesn&#x27;t change anything about how the tool actually works underneath.

With agents making the calls to those tools, this distinction matters. APIs were designed assuming a human programmer is deciding which endpoint to call and how to structure the request. They expose large surfaces with many endpoints and parameter combinations. Their schemas describe data shapes, not intent. They expect structured inputs and return raw HTTP errors when something goes wrong. An agent working from natural language context has to navigate all of that. And when an agent gets it wrong, you get hallucinated parameters, poor tool selection, or wasted tokens cycling through irrelevant endpoints.

Arcade offers MCP tools designed specifically for agents. Arcade tools are narrowed to what agents actually need to do, not the full API surface. Every tool follows consistent structural patterns, and tool descriptions are written for how language models select and invoke tools. Better descriptions mean better tool selection.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77aff8eb9058b8910b66a_data-src-image-ff1aff07-e9c9-4d5a-987d-b04e14e850bc.png)

### **Secure tool authentication and authorization**

LangSmith Fleet and Arcade work together to manage tool authentication and authorization for your agents. Arcade handles per-user, session-scoped authorization. Each action enforces least privilege at runtime, inheriting the permissions of the specific user the agent is acting for. This is what makes agent tooling work in environments where different people have different levels of access to different systems.

Fleet is where you configure how credentials flow into Arcade. Agents configured as &quot;Assistants&quot; pass each user&#x27;s own credentials when tool calls are made, so actions reflect that user&#x27;s permissions in the downstream system. Agents configured as &quot;Claws&quot; use a fixed set of credentials shared across all users, which is useful when the agent is acting on behalf of a team or service rather than an individual.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77aff8eb9058b8910b666_data-src-image-462f1e54-f4ff-4dee-b9c9-ac0dee6fcdf9.png)

### **Getting started**

Arcade provides over[** 60 pre-built templates**](https://www.arcade.dev/agents/gateway-templates?partner=langsmith-fleet&amp;ref=blog.langchain.com) for Fleet covering sales, marketing, support, and engineering use cases, each pre-configured with the right tool connections. You can start using Arcade tools with one of these prebuilt templates, or start building anew.

You can get started with Arcade[** here**](https://app.arcade.dev/register?ref=blog.langchain.com), and try LangSmith Fleet for free[** here**](https://smith.langchain.com/agents?skipOnboarding=true&amp;ref=blog.langchain.com).

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