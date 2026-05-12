---
title: "LangChain + Zapier Natural Language Actions (NLA)"
author: "LangChain Accounts"
date: "2023-03-16"
url: "https://www.langchain.com/blog/langchain-zapier-nla"
---

PartnerAgent Architecture

# LangChain + Zapier Natural Language Actions (NLA)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 16, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb24ab02f04cb69c60867_zapier.drawio.png)We are super excited to team up with Zapier and integrate their new [Zapier NLA API](https://zapier.com/l/natural-language-actions?ref=blog.langchain.com) into LangChain, which you can now use with your agents and chains. With this integration, you have access to the **5k+ apps and 20k+ actions** on Zapier&#x27;s platform through a natural language API interface. This is extremely powerful and gives your LangChain agents seemingly limitless possibilities. Big shoutout to Mike Knoop and the rest of the Zapier team for helping with this integration. You can request access in the link shared above. What will you build?

# **Zapier NLA**

NLA supports apps like Gmail, Salesforce, Trello, Slack, Asana, HubSpot, Google Sheets, Microsoft Teams, and thousands more apps: [https://zapier.com/apps](https://zapier.com/apps?ref=blog.langchain.com)

Zapier NLA handles ALL the underlying API auth and translation from natural language -&gt; underlying API call -&gt; return simplified output for LLMs. The key idea is you expose a set of actions via an oauth-like setup window, which you can then query and execute via a REST API.

NLA offers both API Key and OAuth for signing NLA API requests.

- Server-side (API Key): for quickly getting started, testing, and production scenarios where LangChain will only use actions exposed in the developer&#x27;s Zapier account (and will use the developer&#x27;s connected accounts on [Zapier.com](http://zapier.com/?ref=blog.langchain.com))
- User-facing (Oauth): for production scenarios where you are deploying an end-user facing application and LangChain needs access to end-user&#x27;s exposed actions and connected accounts on [Zapier.com](http://zapier.com/?ref=blog.langchain.com)

Review [full docs](https://nla.zapier.com/api/v1/dynamic/docs?ref=blog.langchain.com) or reach out to [nla@zapier.com](mailto:nla@zapier.com) for user-facing oauth developer support.

# **LangChain Integration**

We&#x27;ve integrated Zapier NLA into a LangChain `Tool` and `Toolkit` in both Python ([docs](https://python.langchain.com/docs/modules/agents/tools/integrations/zapier?ref=blog.langchain.com)) and typescript ([docs](https://hwchase17.github.io/langchainjs/docs/modules/agents/zapier_agent?ref=blog.langchain.com)). This gives your agents and chains superpowers.

To use, simply retrieve an NLA API Key (see above), set the `ZAPIER_NLA_API_KEY` environment variable, then create a `Toolkit` and `agent`:

`llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent=&quot;zero-shot-react-description&quot;, verbose=True)
`

‌It&#x27;s really that simple! The `ZapierToolkit` automatically registers all of your enabled Zapier actions as tools with the correct name and descriptions.

You can also register an individual action as a tool manually using the `ZapierNLARunAction` tool.

To see this in action, look at the example below. This agent now has access to my email and slack, and is able to do some amazing feats. In this example, it’s summarizing the latest email I received from a certain bank and sending it to a slack channel.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb24bb02f04cb69c6086d_screenshot-2023-03-14-at-9.42.03-pm.png)

# **Next Steps**

We’re hoping to make this as seamless an integration as possible so let us know if you have any feedback for hit any issues!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)