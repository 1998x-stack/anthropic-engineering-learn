---
title: "How Athena Intelligence optimized research reports with LangSmith, LangChain, and LangGraph"
author: "LangChain Accounts"
date: "2024-07-22"
url: "https://www.langchain.com/blog/customers-athena-intelligence"
---

Case StudiesLangSmithLangGraph

# How Athena Intelligence optimized research reports with LangSmith, LangChain, and LangGraph

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaJuly 21, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8007bc92c96efc0707_Case-study---athena---ghost.png)Athena Intelligence is an AI-powered employee that is transforming enterprise analytics by automating time-consuming data tasks  and democratizing data analysis for data scientists and business users alike. Their natural language interface, Olympus, aims to connect all data sources and applications so that users can query complex datasets easily, much like asking a question to a colleague.

One of Athena’s most powerful features is the ability to generate high-quality enterprise reports. In this case study, we will go over what this feature entails and how LangSmith helped during the development process.

## **Generating reports on complex topics**

Generating elaborate reports on complex topics requires pulling information from various sources, both web-based and internal. Having proper source citation and data-rich reports was especially important to Athena&#x27;s customers.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8107bc92c96efc0749_AD_4nXctm4mlm0V2lehaGHB6UVzQHC2_-1K7C_Q6V0M8jl4E_2s4krG3uxl7OH_PpwJflqsOI3Z8nzZw-YQC5nBye2xrW6tCpal8bt5dFKiP1j57lYs-LXxnu43pZXLI77oVOKMcVtr76kq_w-ummkFMfiCBbPHt.png)*Example of types of research reports Athena can create*

Building a product to reliably generate these types of reports is hard work. It may be easy to build a prototype of a report writer and make something that passes as a Twitter demo — but as with many GenAI applications, it&#x27;s significantly more difficult to build a reliable production system like Athena’s.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8107bc92c96efc074c_AD_4nXfxsRLZZDfnGkZxML1zhTwoIIR76x7ZydvyQMKKA55VjBCGaBAytfvfnPT2amCx14tfZx1quQI4gxRWPUqL1VPO7InBsP7zHNty9wXjiBpNKTPsBAU4FpsekEVZUWLdSOvFRGQX3zt9EhKoKbt_bZ0IeTDQ.png)*Example of a research report generated with Athena’s Olympus platform *

To bridge the gap between prototype and production, Athena turned to LangChain, LangGraph, and LangSmith. They used LangChain to stay agnostic to the underlying LLM they used and manage integrations with thousands of tools. LangGraph helped them orchestrate complex custom agent architectures. They used LangSmith first to rapidly iterate during the development process, and then to observe their applications in production.

### **Maximum flexibility and interoperability with LangChain**

Athena Intelligence began its journey with [LangChain](https://python.langchain.com/v0.2/docs/introduction/?ref=blog.langchain.com), relying on its interoperability to swap in different models and build their AI apps. LangChain&#x27;s architecture allowed Athena to be completely LLM-agnostic throughout their platform, reducing their dependency on any one model provider.

Athena also heavily used LangChain’s document, retriever, and tool abstractions. By using the standard LangChain document format, Athena could ensure that documents they passed around were always in the same format. LangChain’s retriever interface made this even easier, exposing a common way to access these documents. Athena’s research reports also heavily relied on tool usage - by using LangChain’s tool interface they could easily manage the collection of tools they had and pass them in the same manner to all LLMs.

### **Building production-ready agent architecture with LangGraph **

*As* Athena developed more agentic capabilities, they turned to [LangGraph](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com). The agentic architecture they adopted was highly customized for their use case. LangGraph provided low-level controllability, allowing the team to build out complex agent architectures that orchestrated hundreds of LLM calls.

LangGraph provides Athena engineers with a stateful environment to build production-ready agentic architectures. It enables them to create specialized nodes with tuned prompts, and then quickly assemble them into complex multi-agent workflows. The composability of LangGraph, with its stateful arguments, allows the team to reuse components across different applications in their cognitive stack.

To manage computationally intensive workflows with hundreds of LLM calls introduced by their agentic system, Athena then also LangSmith to improve observability in their development lifecycle.

### **Rapid iteration in development using LangSmith**

[LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) played a crucial role in Athena&#x27;s development process. To give an example of this, let’s consider the feature in the research reports that cited where the data came from.

Doing in-text source citation properly typically takes a lot of prompt engineering effort. LangSmith greatly accelerated this process. With tracing in LangSmith, the Athena team had logs of all runs that generated reports and could quickly identify runs where citations had failed.

Instead of pushing code to production and testing, Athena developers could just then just open up the LangSmith Playground from a specific run and adjust their prompts on the fly. This made it easier to isolate an LLM call to see cause-and-effect, in a way that was tailored for Athena’s complex and bespoke stack — saving countless development hours for the Athena team as they iterated quickly on prompts before shipping to production.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaf8107bc92c96efc074f_AD_4nXdYTOpitCXe-JGTZXJuyt3Ywx3jWv_xlLFkj9MUhzQJqi_lwWp18saSwZjfTwK0GcUjdyam8VCQ9fGycmhTvmXduruqIBTZz2-coDiOAKZxPiae4y0JXS0eG5zJiCSkEBbfLu2ymK2A8uTvfF-hLyz5aWil.png)

*Caption: Using LangSmith Playground view to optimize a market research report *

By tuning prompts to understand and correctly cite sources, Athena engineers could link similarly-named data points back to their applications accurately, enhancing their development quality and speed.

### **Monitoring in production with LangSmith **

Once their application was released to production, Athena monitored the performance of several key metrics with LangSmith traces. Prior to LangSmith, Athena engineers would read through server logs and building manual dashboards to identify issues in production — a time-consuming and cumbersome process.

LangSmith provided out-of-the-box metrics like error rate, latency, and time-to-first-token to help the Athena team keep an eye on the uptime of their LLM app. This was especially beneficial for tasks like document retrieval, where tracing let the team see exactly what documents were pulled up and how different steps in the retrieval process affected their response times.

As Ben Reilly, Founding Platform Engineer at Athena Intelligence, notes:

>  “*The speed at which we’re able to move would not be possible unless we had a full-stack observability platform like LangSmith. It has saved countless hours for our developers and made tasks that would have been almost unfeasible, feasible.”*

## **Conclusion **

Athena Intelligence has successfully leveraged LangChain, LangGraph, and LangSmith to create a powerful AI-powered analytics platform. By using these tools, Athena was able to rapidly iterate on their development, efficiently debug and optimize their system, and deliver high-quality, reliable reports to their enterprise customers.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)