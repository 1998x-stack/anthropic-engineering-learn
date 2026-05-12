---
title: "Announcing the General Availability of LangSmith and Our Series A Led By Sequoia Capital"
author: "LangChain Accounts"
date: "2024-02-15"
url: "https://www.langchain.com/blog/langsmith-ga"
---

Company AnnouncementsLangSmith

# Announcing the General Availability of LangSmith and Our Series A Led By Sequoia Capital

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaFebruary 15, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb026e48474b2f8b4261d_GA---blog-post-header---4.png)Today, we’re thrilled to announce the **general availability of LangSmith** — our solution for LLM application development, monitoring, and testing. We initially launched LangSmith in closed beta in July 2023. Since then, we’ve received invaluable feedback from our early users and customers, and made significant improvements to the platform based on their input. We’ve also made heavy investments in our infrastructure to ensure that the platform is able to seamlessly scale to accommodate our rapidly growing user base. If you want to see LangSmith for yourself, [sign up](https://smith.langchain.com/?ref=blog.langchain.com) today. We’ve removed the waitlist, so you can get building immediately. We hope you love it.

Alongside the GA launch of LangSmith, we’re announcing our **$25M Series A fundraise led by Sequoia Capital**. We’re extremely excited to be working with Sonya Huang and the rest of the Sequoia team to build the future we envision. We&#x27;re also hiring; if you think you could make a difference on our team, [**see our open roles**](https://langchain.com/careers?ref=blog.langchain.com) and get in touch.

Since launching LangSmith, we’ve seen:

- Over 80K signups
- Over 5K monthly active teams
- Over 40 million traces logged in January alone

LangSmith is now trusted by the best teams building with LLMs, at companies such as Rakuten, Elastic, Moody’s, Retool, and more.

James Spiteri, Director of Product Management at Elastic, shares, *“The impact LangChain and LangSmith had on our application was significant. We couldn’t have shipped the product experience in the first place without LangChain, and we couldn’t have done it at the pace we had without LangSmith.”*

## LangSmith supports development from prototyping to production

We learned from our users about the pain points that are common to building with LLMs, and we’re solving those whether you’re building with LangChain or not. In the rest of this post, we’ll highlight the breadth of workflows LangSmith supports and how they fit into each stage of the application development lifecycle. We hope this will inform users how to best utilize our platform or give you something to consider if you are just starting your journey.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb026e48474b2f8b42647_LangSmith-Diagram---GA---final.png)The workflows LangSmith supports at each stage of the LLM application lifecycle

### Prototyping

Prototyping LLM applications often involves quick experimentation between prompts, model types, retrieval strategy and other parameters. The ability to rapidly understand how the model is performing — and debug where it is failing — is incredibly important for this phase.

**Debugging**

When developing new LLM applications, we suggest having LangSmith tracing enabled by default. Oftentimes, it isn’t necessary to look at every single trace. However, when things go wrong (an unexpected end result, infinite agent loop, slower than expected execution, higher than expected token usage), it’s extremely helpful to debug by looking through the application traces. LangSmith gives clear visibility and debugging information at each step of an LLM sequence, making it much easier to identify and root-cause issues. We provide native rendering of chat messages, functions, and retrieve documents.

0:00                            /0:151×

Inspecting a trace from an LLM application run

**Initial Test Set**

While many developers still ship an initial version of their application based on “vibe checks”, we’ve seen an increasing number of engineering teams start to adopt a more test driven approach. LangSmith allows developers to create datasets, which are collections of inputs and reference outputs, and use these to run tests on their LLM applications. These test cases can be uploaded in bulk, created on the fly, or exported from application traces. LangSmith also makes it easy to run custom evaluations (both LLM and heuristic based) to score test results.

0:00                            /0:291×

Inspecting test cases and test runs

**Comparison View**

When prototyping different versions of your applications and making changes, it’s important to see whether or not you’ve regressed with respect to your initial test cases. Oftentimes, changes in the prompt, retrieval strategy, or model choice can have huge implications in responses produced by your application. In order to get a sense for which variant is performing better, it’s useful to be able to view results for different configurations on the same datapoints side-by-side. We’ve invested heavily in a user-friendly comparison view for test runs to track and diagnose regressions in test scores across multiple revisions of your application.

0:00                            /0:141×

Viewing test runs side by side

**Playground**

LangSmith provides a playground environment for rapid iteration and experimentation. This allows you to quickly test out different prompts and models. You can open the playground from any prompt or model run in your trace. Every playground run is logged in the system and can be used to create test cases or compare with other runs.

0:00                            /0:181×

Opening up a run in the Playground

### Beta Testing

Beta testing allows developers to collect more data on how their LLM applications are performing in real-world scenarios. In this phase, it’s important to develop an understanding for the types of inputs the app is performing well or poorly on and how exactly it’s breaking down in those cases. Both feedback collection and run annotation are critical for this workflow. This will help in curation of test cases that can help track regressions/improvements and development of automatic evaluations.

**Collecting Feedback**

When launching your application to an initial set of users, it’s important to gather human feedback on the responses it’s producing. This helps draw attention to the most interesting runs and highlight edge cases that are causing problematic responses. LangSmith allows you to attach feedback scores to logged traces (oftentimes, this is hooked up to a feedback button in your app), then filter on traces that have a specific feedback tag and score. A common workflow is to filter on traces that receive a poor user feedback score, then drill down into problematic points using the detailed trace view.

0:00                            /0:411×

Logging a trace and feedback score from ChatLangChain, viewing the results in LangSmith

**Annotating Traces**

LangSmith also supports sending runs to annotation queues, which allow annotators to closely inspect interesting traces and annotate them with respect to different criteria. Annotators can be PMs, engineers, or even subject matter experts. This allows users to catch regressions across important evaluation criteria.

0:00                            /0:261×

Sending a trace to an Annotation Queue

**Adding Runs to a Dataset**

As your application progresses through the beta testing phase, it&#x27;s essential to continue collecting data to refine and improve its performance. LangSmith enables you to add runs as examples to datasets (from both the project page and within an annotation queue), expanding your test coverage on real-world scenarios. This is a key benefit in having your logging system and your evaluation/testing system in the same platform.

0:00                            /0:141×

Adding the inputs/outputs of a run as an example to a dataset

### Production

Closely inspecting key data points, growing benchmarking datasets, annotating traces, and drilling down into important data in trace view are workflows you’ll also want to do once your app hits production. However, especially at the production stage, it’s crucial to get a high-level overview of application performance with respect to latency, cost, and feedback scores. This ensures that it&#x27;s delivering desirable results at scale.

**Monitoring and A/B Testing**

LangSmith provides monitoring charts that allow you to track key metrics over time. You can expand to view metrics for a given period and drill down into a specific data point to get a trace table for that time period — this is especially handy for debugging production issues.

The platform also allows for tag and metadata grouping, which allows users to mark different versions of their applications with different identifiers and view how they are performing side-by-side within each chart. This is helpful for A/B testing changes in prompt, model, or retrieval strategy.

0:00                            /0:271×

Viewing monitoring charts and grouping by LLM type

## **The Road Ahead**

LangSmith can help with every important workflow at each stage of the LLM application development cycle. As we continue to improve and expand the platform, our future directions include:

- Support for regression testing
- Ability to run online evaluators on a sample of production data
- Better filtering and conversation support
- Easy deployment of applications with hosted LangServe
- Enterprise features to support the administration and security needs for our largest customers.

To learn more about pricing, or reach out to sales, check out our[ website](https://www.langchain.com/pricing?ref=blog.langchain.com) for information.

We believe we are in a super early, very fast-moving industry, and our users trust us to be their guide and partner. With LangSmith, and all our products, we strive to stay ahead of the curve and innovate for the needs of our users today. Thank you for going on this journey with us. Onwards!

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb026e48474b2f8b4264b_Trace-on-lilac-bg.png)

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)