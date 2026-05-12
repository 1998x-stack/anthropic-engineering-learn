---
title: "Announcing LangChain Hub"
author: "LangChain Accounts"
date: "2023-09-05"
url: "https://www.langchain.com/blog/langchain-prompt-hub"
---

Company AnnouncementsLangChain

# Announcing LangChain Hub

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamSeptember 5, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb17857c432b84a74581c_5-social--19-.png)Today, we&#x27;re excited to launch LangChain Hub–a home for uploading, browsing, pulling, and managing your prompts. (Soon, we&#x27;ll be adding other artifacts like chains and agents).

💡

[Explore the Hub here](https://smith.langchain.com/hub?ref=blog.langchain.com)

LangChain Hub is built into LangSmith (more on that below) so there are 2 ways to start exploring LangChain Hub.

- **With LangSmith access: **Full read and write permissions. You can explore all existing prompts and upload your own by logging in and navigate to the Hub from your admin panel.
- **Without LangSmith access: **Read only permissions. You can view and download and run prompts. Head directly to [https://smith.langchain.com/hub](https://smith.langchain.com/hub?ref=blog.langchain.com) to start exploring.

**If you would like to upload a prompt but don&#x27;t have access to LangSmith **fill out [this form](https://airtable.com/appbtdQ3PDLqWq3By/shrjPqoBROI1bJTpR?ref=blog.langchain.com) and we will expedite your access so you can start publishing your prompts.

### Motivation for LangChain Hub

We launched a very early version of LangChain Hub at the beginning of the year as a directory of code and README&#x27;s with the same goal we have today–make it easier to share and discover prompts for any use-case.

As LangChain and the broader ecosystem has evolved, the role of prompting has only become more important to the LLM development process. As Ethan Mollick recently wrote in a ([FANTASTIC) article](https://www.oneusefulthing.org/p/now-is-the-time-for-grimoires?ref=blog.langchain.com) on the topic, &quot;now is the time for grimoires.&quot; By &quot;grimoires&quot; he means &quot;prompt libraries that encode the expertise of their best practices into forms that anyone can use.&quot;

We whole-heartedly agree–the value of a Hub extends beyond individual applications. It&#x27;s about advancing our collective wisdom and translating that into knowledge we can all put to use now. We want to help make this easier on an individual, team, and organization scale, across any use-case and every industry.

Our goal for LangChain Hub is that it becomes *the *go-to place for developers to discover new use cases and polished prompts.

Today, polished prompts and the wisdom that comes with it are distributed across the web and all-too-often buried in the crannies of blog posts, Twitter threads, and people&#x27;s head&#x27;s. By bringing all tis knowledge together in one easily-navigable place, we think we can accelerate the pace of development and learning together.

To use Mollick&#x27;s terminology–we&#x27;re starting with public grimoires today, but we&#x27;ll be enabling private, company-specific grimoires very soon.

**So why now?** A few new insights emerged over the past months that motivated us to rebuild the hub properly.

- **Model Variety and Non-Transferable Prompts**

People aren&#x27;t just using OpenAI anymore. Anthropic with `claude-2` has become the go-to choice for people needing long context windows. Google is releasing (and will release) more powerful models. And, most excitingly, the open source model community is catching up and Llama2 proving to be a viable alternative.

Unfortunately, prompts don&#x27;t simply transfer from one model to another. Each model may have different tricks that work best for that model (e.g. `claude-2` prefers XML encoding when prompting) or different syntax (e.g. `SYS` and `INST` for Llama2).

As developers explore the wide variety of models, we hope the LangChain Hub can assist in that exploration by providing starter prompts for those models. We&#x27;ve added tags to prompts to indicate which model(s) they work best with.

2. **Inspectability**

Prompts power the chains and agents in LangChain. Often times, the prompts are obfuscated away. We built LangChain Hub in a way that puts them front and center, so that anyone can see what&#x27;s going on under the hood.

3. **Cross-Team Collaboration**

While most LLM applications require substantial engineering work to set up, we&#x27;ve noticed that non-technical team members are participating in the process of editing and refining prompts. We wanted to make it *much *easier for more team members to get involved in what we believe is going to become a core part of every company&#x27;s app development process. Along these lines, we don&#x27;t believe that prompts should be treated as traditional code–it&#x27;s simply not the best way to facilitate this kind of collaboration.

We&#x27;re aiming to make LangChain Hub the best place for teams to write and manage prompts, together. The product isn&#x27;t quite there today–this first iteration only supports personal accounts–but we&#x27;re actively looking for organizations that are excited to explore an Alpha with us so if you want organizational support for the Hub, please reach out to us directly at `support@langchain.dev` with the subject `[Hub: Orgs]`

**4. Artifact Management and LangSmith**

From partnering with early LangSmith users, the tie-in between debugging, logging, testing, and evaluation and artifact management has become increasingly obvious. By making LangChain Hub a part of LangSmith, we knew we could help teams not only identify and collaborate on prompts, but also make informed decisions about how to implement them. Testing integrations with prompts aren&#x27;t out yet but they are coming soon!

## Favorite Features

**Home Page**

We want to make discoverability and navigability as easy as possible. You should be able to go from curiosity to coding in just a few clicks.

You can view sort prompts by:

- Most favorites
- Most viewed
- Most downloaded
- Recently uploaded

You can filter prompts by:

- Use cases (chatbots, extraction, summarization, etc)
- Type (prompt template, etc)
- Language (English, Chinese, etc)
- Model (OpenAI, Anthropic, Llama2, VertexAI, etc)

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb17957c432b84a745851_image-1.png)

**Downloading and Uploading Prompts**

We have released an SDK to enable [easy programatic downloading](https://docs.smith.langchain.com/hub/dev-setup?ref=blog.langchain.com#3-pull-an-object-from-the-hub-and-use-it) of prompts:

`from langchain import hub

prompt = hub.pull(&quot;hwchase17/eli5-solar-system&quot;)`

You can also [easily upload](https://docs.smith.langchain.com/hub/dev-setup?ref=blog.langchain.com#4-push-a-prompt-to-your-personal-organization) prompts via the SDK

`from langchain import hub
from langchain.prompts.chat import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(&quot;tell me a joke about {topic}&quot;)

hub.push(&quot;&lt;handle&gt;/topic-joke-generator&quot;, prompt)`

If you want to upload an prompt to the Hub, but don&#x27;t yet have access to LangSmith, fill out this [form](https://airtable.com/appbtdQ3PDLqWq3By/shrjPqoBROI1bJTpR?ref=blog.langchain.com) and we will expedite your access.

**Prompt Versioning**

Each time you commit a prompt, it is added as a new commit. This means that you can easily access previous versions of prompts should you want to go back to a previous version.

**Playground**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb17957c432b84a74584d_Screenshot-2023-09-04-at-3.47.02-PM.png)

All prompts can be opened in the playground by clicking the &quot;Try it&quot; button. This allows you to interact with prompts right from LangChain Hub. It&#x27;s useful for testing prompts...and it&#x27;s fun!

*Note: You will be required to enter an OpenAI or Anthropic API key in order to run it in the playground. These keys are only stored in your browser are used solely to communicate directly to services.*

**Editing and Saving**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb17957c432b84a745854_Screenshot-2023-09-04-at-3.48.59-PM.png)

From the playground you can edit a prompt, and then save it by clicking the &quot;Commit&quot; button in the top right corner. You can do this either for your own prompts, or for others (when saving, you will have to create your own repo to save it to). This is exciting because it helps everyone build on top of each other&#x27;s work!

## Coming Soon

- **More Artifact Types: **Right now, only prompt templates are supported. We plan to expand support for other types of artifacts like chains and agents.
- **Organization Support: **Right now the Hub only works for your personal account. If your organization needs the ability to collaborate on prompts, for now please reach out to us directly at `support@langchain.dev` with the subject `[Hub: Orgs]`. We will be rolling this out more widely in a few weeks.
- **Integration with testing: **Just as you test code, you should test prompts. We are working on integrating the Hub with our dataset &amp; testing functionality. If you need to test your prompts in the meantime, please check out our [LangSmith cookbooks](https://github.com/langchain-ai/langsmith-cookbook?ref=blog.langchain.com).
- **More social features: **Just as you test code, you should test prompts. We are working on integrating the Hub with our dataset and testing functionality. If you need to test your prompts in the meantime, please check out our [LangSmith cookbooks](https://github.com/langchain-ai/langsmith-cookbook?ref=blog.langchain.com).
- **What else? **If you have product feedback or ideas for us, we want to hear it! [Join us in Discord](https://discord.gg/6adMQxSpJS?ref=blog.langchain.com) to share more.

## Show us your prompts!

We’ll be rounding up and sharing the most creative, useful, thought-provoking prompts with the community.

So share your prompts, ❤️ your favorites, and tag us when you post your prompts or stumble across ones you like!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)