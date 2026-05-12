---
title: "RealChar x LangSmith: Using Open Source tools to create an AI companion"
author: "LangChain Accounts"
date: "2023-07-24"
url: "https://www.langchain.com/blog/realchar-x-langsmith-ai-companions"
---

PartnerLangSmith

# RealChar x LangSmith: Using Open Source tools to create an AI companion

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 24, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eca2e6df4d389b4cee_5-social--8.png)***Editor’s Note: This blog post was written in collaboration with RealChar, an early ***[***LangSmith***](https://www.langchain.com/langsmith?ref=blog.langchain.com)*** BETA user. They moved fast and created something really, really sophisticated and really, really fun to use–all with open source tools.***

***We&#x27;re also very excited about AI characters and companions internally, which is part of the reason we&#x27;re excited to highlight RealChar. As seen by the meteoric rise of platforms like CharacterAI, allowing people to converse with different personas can be really fun. ***

***RealChar may be the most complete and most exciting OSS AI character framework out there. Besides impressive underlying technology, it also offers a really polished UI and UX. They were one of the top trending GitHub repos for basically all of last week, and we&#x27;d highly recommend that you check it out if you haven&#x27;t already.***

We (RealChar team) are pleased to share our experience using LangSmith and working with LangChain team.

In case you don’t know, [RealChar](http://realchar.ai/?ref=blog.langchain.com) is an open source project to let you create, customize and talk to your AI character/companion in realtime (all in one codebase). We offer users natural and seamless conversations with AI on all the common platforms (mobile, web, terminal and desktop soon). We built RealChar leveraging some of best open source tools in the Generative AI/LLM space, including LangChain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cf4_image-5.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cfd_image-6.png)

*Just a fun demo: asking AI Elon about whether he is afraid of losing in the much anticipated cage fight. Full version *[*here*](https://youtu.be/VR61lsWGj6k?ref=blog.langchain.com)*.*

RealChar received a ton of attention and usage from the community after [releasing](https://github.com/Shaunwei/RealChar?ref=blog.langchain.com) it just a week ago, and our site has undergo significant traffic. With conversations piling up and logs get cluttered very quickly, we found LangSmith to be a perfect tool for us to monitor and observe the traffic.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d00_image-7.png)

It’s also easy to filter logs easily based on various conditions, to allow us track issues more accurately. For example, we can easily see all the errors when interacting with the Language Model, which has helped us understand and maintain our reliability better.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4cfa_image-8.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d05_image-9.png)

LangSmith also allows us to identify important conversations and add to dataset easily. This is then helpful for us to evaluate and safe checking the prompts going forward, using the Evaluation features of LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1eda2e6df4d389b4d08_image-10.png)

The UI of LangSmith is also top-notch and easy to work with. It largely replaced our monitoring tools previously built in-house.

All these features are almost free to get as we already use LangChain. As soon as the API Key are set up in LangSmith, only a few environment variables are needed:

`LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=YOUR_LANGCHAIN_API_KEY
LANGCHAIN_PROJECT=YOUR_LANGCHAIN_PROJECT
`

Overall, we see LangSmith as a great tool for Analytics, Observability, and Evaluation, all in one place. It’s very useful for a production-level application with large volume of traffic like RealChar.

[/content/media/5101573/253656635-5de0b023-6cf3-4947-84cb-596f429d109e.mp4](https://storage.ghost.io/c/97/88/97889716-a759-46f4-b63f-4f5c46a13333/content/media/5101573/253656635-5de0b023-6cf3-4947-84cb-596f429d109e.mp4?ref=blog.langchain.com)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

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