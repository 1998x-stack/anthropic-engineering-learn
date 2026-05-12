---
title: "Goodbye CVEs, Hello `langchain_experimental`"
author: "LangChain Accounts"
date: "2023-07-31"
url: "https://www.langchain.com/blog/goodbye-cves-hello-langchain-experimental"
---

Company Announcements

# Goodbye CVEs, Hello `langchain_experimental`

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 31, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb1e42c7f205b929c520b_photo-1614935151651-0bea6508db6b.jpeg)One of the things that LangChain seeks to enable is connecting language models to external sources of data and computation. This allows language models to act as the reasoning engine and outsource knowledge and execution to other systems. Some examples of this include:

- Retrieval augmented generation: Hooking a language model up to a retrieval system and using that influence the generation. This allows language models to answer questions about information other than what they were trained on.
- Interacting with APIs: Having a language model generate the route and parameters to call for a specific API request. This allows humans to interact with an API through natural language.
- Code generation: Having a language model write and then execute code. This can enable people to generate code just by asking.

While this is powerful, it can also be dangerous. A lot has been discussed around AI safety, and there are many different types and considerations for AI safety. The type that we are most concerned with is what happens when you hook up language models to other systems. While doing this can enable lots of amazing experience (like the ones listed above) it also opens up a whole new risk vector.

This risk vector emerges when the language model generates output that is unsafe to pass downstream, whether that be an API request that deletes some data or some malicious code that deletes all files. This can occur naturally or maliciously. It can occur naturally when the language model simply messes up - as its prone to do. It can also occur maliciously, through techniques like prompt injection.

LangChain started off as highly experimental and included a lot of these use cases, as those uses were the ones pushing boundary of what was possible. Some of these use cases have security concerns, some don’t. As LangChain matures, we want to better separate those uses to allow for that distinction.

We’ve taken a first stab at that by releasing `langchain_experimental`, a separate Python package. We’ve moved all components that raised CVEs into that package. We’ve also moved everything previously in the `langchain.experimental` module there as well. You can find instructions on how to migrate [here](https://github.com/langchain-ai/langchain/blob/master/MIGRATE.md?ref=blog.langchain.com).

Going forward, we have the dual goals of making core `langchain` more robust and production ready, while also pushing forward rapidly with `langchain_experimental`. We’ve been slow to accept some more experimental features, but this separation will now hopefully speed that up.

We will also likely move more things over to `langchain_experimental` over time. When we do this, we will always give at least a week’s notice before making any breaking changes, and update the [migration guide](https://github.com/langchain-ai/langchain/blob/master/MIGRATE.md?ref=blog.langchain.com).

We’d like to thank the entire community for understanding, as well as their patience as we iron out any kinks. In particular we’d like to thank some community members for their help and encouragement on this: Rich Harang (and the entire Nvidia team), Justin Flick, Or Raz, and Boaz Wasserman.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)