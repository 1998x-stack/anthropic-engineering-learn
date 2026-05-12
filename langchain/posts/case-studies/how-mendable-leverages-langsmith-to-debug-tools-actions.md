---
title: "How Mendable leverages LangSmith to debug Tools &amp; Actions"
author: "LangChain Accounts"
date: "2024-01-25"
url: "https://www.langchain.com/blog/how-mendable-leverages-langsmith-to-debug-tools-actions"
---

Case StudiesLangSmith

# How Mendable leverages LangSmith to debug Tools &amp; Actions

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 25, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05444d72d9752568dbf_Frame-730--1-.png)***Editor&#x27;s Note: this blog is from Nicolas Camara, CTO @ Mendable. Mendable.ai is a platform helping enterprise teams answer technical questions with AI. We&#x27;re incredibly excited to highlight how they are using LangChain Agents and LangSmith on their newest feature: ***[***Tools &amp; Actions***](https://www.mendable.ai/blog/tools?ref=blog.langchain.com)***.***

It is no secret that 2024 will be the year we start seeing more LLMs baked into our workflows. This means that the way we interact with LLM models will be less just Question and Answer and more action-based.

At [Mendable.ai](https://www.mendable.ai/?ref=blog.langchain.com), we are seeing this transformation first hand. Late last year, we equipped ~1000 customer success + sales people at a $20+ billion tech company with GTM assistants that help with tech guidance, process help, and industry expertise. In five months, the platform achieved $1.3 million in savings, and it&#x27;s projected to save $3 million this year due to decreased research time and dependency on technical resources. Now we are working with that same company to enable these assistants to take action, enabling even more efficiency improvements.

An example use case would be a salesperson who wants to get the latest focus areas for a prospect and their company. When asking an assistant enabled with our Tools &amp; Actions “what are the latest key initiatives for X”,  the assistant could:

- Call the CRM API and get the exact team the salesperson is trying to sell to
- Use the Google News or DUNS API to get the latest news on the specific team and related initiatives
- Call the CoreSignal API to get the latest hiring trends for the company based on job postings and more
- Interpret the news and hiring trends, highlighting ways the salesperson can use these new found initiatives to sell in meeting

As you can see the introduction of Tools &amp; Actions in Mendable expands capabilities quite a bit, enabling chatbots to access and utilize a wider range of data sources and perform various automated tasks. On the backend, to ensure the precision and efficiency of these features, Mendable leverages LangSmith&#x27;s debugging tools, a critical component in the development and optimization of our AI-driven functionalities.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05544d72d9752568ddc_g94ETB3qq1plVmeCy1QvGEQxHu97tYYRcY0hJsnaUKuVC56RE1790dL4xM2VxfpSxALb4tyZ7Oz2OkxeTfk2kMuZ0zgI9tDXD7ELOCbC_Tu3J63lZJ24qgHETg17Cix2XlYhlkgRGmeQ7kzNVPzpFQs.png)

**Opening the ‘black box’ of agent execution**

One of the biggest problems when building applications that depend on agentic behavior is reliability and lack of observability. Understanding the key interactions, decisions of an Agent loop can be quite tricky. Especially when it has been giving access to multiple resources and is embedded in a production pipeline.

While building Tools &amp; Actions, the core aspect we had in mind was giving the ability for the user to create their own Tool via an API call. We designed this so the user could input a tag such as &lt;ai-generated-value&gt; when creating the API request and the AI can fill that value at request time with an ‘AI generated’ value based on the user&#x27;s question and schema. This is one example, but there were a lot more just in time AI inputs/outputs that went into it. This posed some challenges in the building process that we weren’t expecting. Soon our development process was full of “console.logs” everywhere and high latency runs. Trying to debug why a tool wasn’t being called or why the API request had failed became a nightmare. It quickly started to get messy and we had no proper visibility on what the agentic behavior looked like nor if custom tools were working as expected.

Here is where LangSmith from LangChain came to help. If you are not familiar, LangSmith allows you to easily debug, evaluate and manage LLM apps. It, of course, integrates swiftly with LangChain. As we were already using parts of the [OpenAI tool agents](https://js.langchain.com/docs/modules/agents/quick_start?ref=blog.langchain.com) that LangChain provides, the integration was smooth.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05644d72d9752568e08_2WdpnNZdjPfjFICqpmTUia_KHMPsPNgiLRkJ4CMUSDJ4_qT5rHIuhvit4Omw0km3cILErutLaB2BTVkWVjvg5ZGxgkVhQ9pAFsWlhtB95hRhUc9s_o9YPzK0ZfIqwaM4uZCnfXCcr0HS8-XiKC309bw.png)

**The Debugging Process**

LangSmith allows us to have a peek inside of the agents’ brain. This is very useful for debugging how an agent&#x27;s thinking and decision process can impact the output.

When you enable tracing in a LangChain, the app captures and displays a detailed visualization of the runs’ call hierarchy. This feature allows you to explore the inputs, outputs, parameters, response times, feedback, token consumption, and other critical metrics of your run.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05644d72d9752568de7_krFAGGVskiSW9jRNXTx3aXZJVs3J4g_eW6laEADv7TYuKXI81oljAg3vppsCVTlVOPA-qV1vWZ4FDk5GdeQqS82G-oCjW4rHQXSEWfS-kYhqCFI0zkuihM4e2RmraeI1pv5mUc2NGl4m8iHHFkwy18U.png)

When we connected LangSmith to our tools &amp; action module, we quickly spotted problems that we didn’t have the visibility for.

Take a look for instance on one of our first traces using Tools. As you can see here, the last call to `ChatOpenAI` took a long time: 7.23 seconds.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05544d72d9752568dd8_15pEFeaqlxWKWA4IVeqmDLokrIyQO-W4j71IlZKYkDaGz3mIOCpPiG0tIoa0pYB4L72e6R-y-yijmtTlUTA56J5wEfx8xPF8tRkRXCx2n16DIjQcK_wxEh5AaJlYr0NF2GpUSfj_5qtI_S9tk4zUPNI.png)

When you click on the 7.23s Run we saw that the prompt was massive, it had concatenated all of our RAG pipeline prompts/sources with our Tools &amp; Actions, leading to delay in the streaming process. This allowed to further optimize what chunks of the prompt need to be used by the Tools &amp; Action module, reducing total latency overall.

**Inspecting Tools**

Another valuable aspect of having ease access to traces is the ability to inspect a tool input. As I mentioned in the beginning, we allow users to create custom tools in Mendable. With that we need to make sure that the building process of a tool in the UI is easy and quick but also performs well. This means that when we create a tool in the backend, it needs to have the correct schema defined partially by what the user inputted in our UI (API request details) but also by what the AI will automatically feed in at request time.

In the example below, it shows a Recent News Tool that was run. The question inside the {query : { q } } parameter was generated by the AI.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05644d72d9752568de0_BWLrbAca9GfoE6MIZ_HMDMNY74DhbtsPjD79RyNj3TysM6mUYVLngyC8Kn04aJB_AC3KXEcV31vQlwO3UiCu7EnueS1YmgzT7EPLPIsWp8CIp-EFt1AdbujiHXl7zJbXoU1zwl9IZxLzR4zFFtOLqjI.png)

Making sure that query was accurate with what the user inputted but also optimized for the tool being used was very challenging. Thankfully it was very easy to double check that with LangSmith. What we did is we ran the same tool with different queries ~20 times and quickly scrolled through LangSmith making sure the output and schema were accurate. The times that weren’t accurate, we could easily understand why by opening the trace further or by annotating in LangSmith so we could review it later.

What we realized is that the Tools description was critical for the correct schema and input to be generated. With this new insight we obtained from running tons of experiments, we went ahead and improved the AI generated part of that in our product and also made users aware that they need to provide good detailed descriptions when creating a Tool.

**Building our Dataset**

With all the optimization experiments taking over, the need to quickly save inputs/outputs for further evaluation became evident. With LangSmith we selected the runs that we wanted to add to our dataset and clicked the “Add to Dataset” button.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05644d72d9752568df7_T-IabDUJQrGIGh8PmkIhKk7ctpGjsDaOixlwfg5nHODKhiv5LfVSBli3Ul55pg8JFKFKGfxZAZ61ZjN8QPk6bU6NE08HCtrDONVFxqwKXg5k_2x56vmJ5uz60QPA4zggBMdTczdKQqTXH0dIxOSENvo.png)

This was a very quick and easy win for us as we now had all the data in one place from our runs and we could even evaluate that using LangSmith itself.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb05644d72d9752568dfe_eTsj-cy9H7EIxAhprCM97_KDhSqKeUWb18qbpigX5_tGaoytH71OvXqo3SMdOe6jPLtTlkGlcglHjs_auKtzJZGVZFXe_7ZqfWdOzRJHn678e1vKHcQRh6mtcRGab9bdZdHKN0_rB_5wOKfstN0Nv-E.png)

**Conclusion**

LangSmith&#x27;s debugging tools have been a game-changer for us. They&#x27;ve given us a clear window into how our Tools and Action AI agent thinks and acts, which has been helpful for tackling tricky issues like slow response times and making our debugging process way smoother. [Mendable Tools &amp; Actions](https://mendable.ai/blog/tools?ref=blog.langchain.com) has launched but we are still early in the process. We have been working with amazing enterprises to help improve it and tailor custom actions to them. If you are interested in testing Mendable, email us at [garrett@mendable.ai](mailto:garrett@mendable.ai) with your use case.

Also, if you are looking to speed up your LLM development process, I would definitely recommend trying [LangSmith](https://www.langchain.com/langsmith?ref=blog.langchain.com) out - especially if you already use LangChain in your pipeline.

I hope my insights were helpful and thanks to LangChain for being an awesome partner.

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