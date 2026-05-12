---
title: "LLMs accelerate Adyen&#x27;s support team through smart-ticket routing and support agent copilot"
author: "LangChain Accounts"
date: "2023-11-28"
url: "https://www.langchain.com/blog/llms-accelerate-adyens-support-team-through-smart-ticket-routing-and-support-agent-copilot"
---

Tutorials &amp; How-Tos

# LLMs accelerate Adyen&#x27;s support team through smart-ticket routing and support agent copilot

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 28, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0b25c796b4dae0e5a66_Twitter-post---18--3-.png)

## Challenge

As global commerce accelerates, [Adyen](https://www.adyen.com/?ref=blog.langchain.com), a publicly-traded financial technology platform, is helping large companies like Meta, Uber, H&amp;M, and Microsoft achieve their ambitions faster by providing end-to-end payments capabilities, data-driven insights, and financial products in a single global solution.

With more merchants signing on and with increased transaction volume comes increased pressure on support teams and a team at Adyen that immediately sought out leveraged solutions. &quot;We are engineers so we are always looking at ways to scale our business using technology without having to increase the team size,” said Andreu Mora, SVP of Engineering - Data. “We want to understand, harness, and advance technology like LLMs to make our teams and customers more efficient and more satisfied.”

Adyen spun up a new and lean team of Data Scientists and Machine Learning Engineers based out of their new Tech Hub in [Madrid, Spain](https://careers.adyen.com/locations/madrid?ref=blog.langchain.com) to take on a range of high-impact projects, with the initial goal of accelerating support teams.

## Solution

Focusing on support team efficiency and satisfaction led the team to an insight that passing tickets between teams was a major factor influencing response times. This challenge was particularly well-suited to be solved by two initial LLM applications:

- A smart ticket routing system designed to get a ticket to the right support person as quickly as possible based on content
- A support agent copilot designed to help agents answer tickets faster and more accurately with an approach they call *Question Answering Suggestions*.

Adyen decided to use LangChain to build it because they could rely on a single, easy-to-customize, framework to get from prototype to production, and avoid getting locked into a single model as they experimented. They also relied on LangSmith, LangChain’s developer platform to evaluate performance of their applications and compare how different underlying models affected response quality and costs.

LangChain’s flexibility allowed Adyen to switch the core part of the chain among various LLMs with ease. To ensure seamless interactions with their internal LLM API endpoint, they introduced a custom class extending from LangChain’s base LLM class, and integrated it with an event-driven microservice architecture hosted in a Kubernetes cluster. For a more in-depth exploration of the technical aspects behind Adyen&#x27;s smart ticket routing and support agent copilot, check out the technical deep dive by [Andreu Mora](https://www.linkedin.com/in/andreumora/?originalSubdomain=nl&amp;ref=blog.langchain.com) and [Rafael Hernandez](https://www.linkedin.com/in/rahermur/?locale=en_US&amp;ref=blog.langchain.com) (Team Lead of Operations AI) on the Adyen blog [here](https://www.adyen.com/knowledge-hub/operational-efficiency-llms?ref=blog.langchain.com).

## Results

### ***More efficient and accurate ticket routing***

The foundation of Adyen’s smart ticket router is an internal tool that analyzes the theme and sentiment of each ticket, and dynamically updates its priority based on the user.  With Adyen’s wide array of products, features &amp; services, this LLM-driven approach enables merchants to receive support from the technical experts most suited to respond quickly.

### ***Quicker support response times***

In just 4 months the Adyen team was able to build a comprehensive collection of relevant documents (combining public and private company documents) and store them in a vector database with an embedding model that optimized for effective retrieval. The team’s first milestone on its way to generating proposed ticket responses was finding the most relevant and up-to-date document from a collection of public and private documents. This approach far outperformed traditional keyword-based search and, just as importantly, immediately established the team’s trust in the new system.

The next step was to connect to an LLM to produce a suggested response for support agents through their proprietary copilot. “With the right set of tickets in their queues and easily-modifiable potential answers to customer inquiries at their fingertips, support agents are more efficient and more satisfied.” said Andreu.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9b9e7ec0692a2d079af_gtm-agent-diagram-1--6-.png)Tutorials &amp; How-Tos

#### How we built LangChain’s GTM Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/how-we-built-langchains-gtm-agent)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa2fcd1956c2e4fa1ff2_Evaluating-Deep-Agents.png)Deep AgentsAgent ArchitectureTutorials &amp; How-Tos

#### Evaluating Deep Agents: Our Learnings

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 3, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/evaluating-deep-agents-our-learnings)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa490b26292282bdb573_Rebuilding-Chat-LangChain.png)Company AnnouncementsTutorials &amp; How-Tos

#### Why We Rebuilt LangChain’s Chatbot and What We Learned

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 5, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)13min[](/blog/rebuilding-chat-langchain)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)