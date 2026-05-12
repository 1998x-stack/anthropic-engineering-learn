---
title: "LangChain Partners with CommandBar on their Copilot User Assistant"
author: "LangChain Accounts"
date: "2024-02-08"
url: "https://www.langchain.com/blog/langchain-partners-with-commandbar-on-their-copilot-user-assistant"
---

PartnerCase Studies

# LangChain Partners with CommandBar on their Copilot User Assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamFebruary 8, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb035e48474b2f8b42990_Twitter-post---24.png)[CommandBar](https://commandbar.com/?ref=blog.langchain.com) is a user assistance platform that helps software companies make their products easy to use by capturing and predicting user intent, and then delivering personalized in-product help. CommandBar’s Copilot widget, which companies embed into their applications, goes beyond a typical chatbot. It can answer user questions, trigger personalized product tours, even fulfill a user’s intent directly by carrying out actions on their behalf.

CommandBar’s customers have slightly different needs from each other, and in order for the Copilot to be helpful across all of CommandBar’s customers, the team had to find common threads for user assistance that could be streamlined or automated with LLMs as well integrate with many different content providers (such as help desks and knowledge bases) for information retrieval.

CommandBar decided to use LangSmith to give them visibility over their Copilot’s performance and ultimately deliver better experiences for their customers. While the team did not use LangChain in production, getting up and running in LangSmith was fast. “I was surprised how straightforward it was to set up the traces just with the decorators in LangSmith. It was super easy to get started.” says Senior Software Engineer Jared Luxenberg.

LangSmith helped the CommandBar team is these four ways primarily:

- **Trace Visibility: **The team was able to see if an end user had a bad experience just by looking at a LangSmith trace and didn’t have to rely on receiving a screenshot or email. LangSmith visibility down to the conversation thread allowed CommandBar to be proactive about identifying how the customer could avoid a bad interaction in the future.
- **Debugging: **Building a good Copilot came down to building a good retrieval system, and LangSmith traces helped the team understand if the right documents were even retrieved in the first place, and if not, they had information to try different techniques to improve the system.
- **Increased testing coverage: **The team 5x’d the number of tests it could run on any new code change. Before LangSmith, CommbandBar relied solely on manual QA, but after adopting LangSmith, they could augment human evaluation with better auto-evaluation over grounded pairs of question : response that were known to be good.
- **Monitoring: **The CommandBar team relied on LangSmith to alert if their LLM provider was having an outage, and they could keep a view of the overall health of their application in LangSmith’s monitoring tab.

LangSmith mapped easily to the workflows they wanted to accomplish, aiding them throughout the entire application development lifecycle. CommandBar’s Copilot has been live since November 2023, and it makes life easier for thousands of support teams and millions of end users, and this translates into concrete results for customers – like a 44% decrease in support tickets from a recent case study “Every week we hear from one of customers enthusiastically sharing that the Copilot responses are so on point, and it’s become one of our product’s biggest competitive advantage and probably our flagship product at this point.” says Luxenberg.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb035e48474b2f8b429be_WHBbnrH_dPOtjz1nGI-jy8PjbDnN4zMOGSK3sMOZDcMkhdg80awBTxk46a_VYaNg-iQG536JhTliMJD4PJaG60TT8buPiZiJUPrYpbWkRKmON0Tr_nKgX0VsqKfyhKd-jZD8zz--J7ivaI_noYzrWtM.png)

CommandBar believes Copilot can become even more useful and proactive for users. Commandbar has a lot of cool improvements rolling out in the coming months, which are all powered by Langsmith. To read more about their launch, head to their blog [here](https://www.commandbar.com/blog/why-we-built-copilot/?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efb41ab2584d1733d866c5_case-study-madrigal.png)Case Studies

#### How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba6c52ebbc1e377743b4_Parth.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69efba87c585b65247366c20_Ron.png)Parth PatelRon FilippoApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/customers-madrigal)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)