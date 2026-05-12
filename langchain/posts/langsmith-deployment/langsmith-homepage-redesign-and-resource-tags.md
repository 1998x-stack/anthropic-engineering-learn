---
title: "LangSmith: Redesigned product homepage and Resource Tags for better organization"
author: "LangChain Accounts"
date: "2024-11-19"
url: "https://www.langchain.com/blog/langsmith-homepage-redesign-and-resource-tags"
---

Company AnnouncementsLangSmith

# LangSmith: Redesigned product homepage and Resource Tags for better organization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 19, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4107bc92c96efbbf76_LangSmith-homepage-redesign---blog-thumb.png)Today, we’re excited to release a redesigned LangSmith product homepage as well as improved support for resource organization within your workspaces. These updates reflect our ongoing insights into how engineering teams build, optimize, and iterate on their LLM applications. In this post, we will walk through our updated beliefs and how they guided our design.

## Our approach to redesigning the LangSmith homepage

Through collaborating with thousands of developers and companies, we’ve observed that they work across three main areas when building LLM applications: observability, evaluation, and prompt engineering. To reflect the critical role each plays in an effective developer workflow, we’ve split our [LangSmith product homepage](http://smith.langchain.com/?ref=blog.langchain.com) into these three areas.

### Observability

*This section in LangSmith includes Tracing Projects and Dashboards.*

One of the biggest recommendations for AI engineers is to “look at your own data” — and LangSmith enables this by helping users identify issues and understand their LLM application’s performance over time.

**Tracing Projects** are collections of traces emitted from your AI application. Inside this page, you can search and filter traces, then click into a specific trace for a more detailed view. This type of datapoint-level observability is crucial for understanding what is going on in your application, so that you can debug and identify issues quickly.

**Dashboards** allow you to create custom monitoring charts to track the metrics that matter the most to your application over time. This includes basic metrics like cost, latency, and quality as well as more specific criteria like agent actions over time or realtime evaluation scores.

Our observability features are designed to empower users to optimize their LLM application at every step in the lifecycle — from detailed debugging in development, to monitoring performance at scale in production.

### Evaluation

*This section in LangSmith includes Datasets, Experiments, and Annotation Queues.*

Evaluating your LLM application is often a bottleneck in development. High-quality, continuous evaluations (or “evals”) help developers understand how well their application is performing and pinpoint areas for improvements. LangSmith Evaluation removes the guesswork, highlighting regressions or improvements across metrics like accuracy, style, and other key criteria.

First, LangSmith makes it easy to curate **datasets**. Users can import existing data, or automatically add data points from their logs in the Observability section of LangSmith. You can then run experiments over these datasets, score the result with automatic evaluators, and track the results of these over time.

Human review remains a crucial part of evaluating LLM applications, and LangSmith simplifies this process with **Annotation Queues**. Using Annotation Queues, users can organize and manage data points that need human review, streamlining the workflow for reviewers and ensuring consistent, high-quality feedback.

### Prompt Engineering

*This section in LangSmith includes Prompts and the Playground.*

Effective prompt engineering is necessary for building a responsive and reliable LLM application. LangSmith enables user to **store and version prompts**, making it easy to track their evolution and collaborate seamlessly with team members.

Additionally, the **Playground** in LangSmith allows users to iterate on prompts in real-time. Users can run prompts against individual datapoints or over an entire dataset to assess their impact at scale. The Playground also allows for side-by-side comparisons of how different prompt and model combinations perform.

Prompt engineering is an area where we’re interested in pushing the boundaries. What could an “IDE for prompt engineering” truly look like? We’re diving into this question, reimagining the tools that prompt engineers need, and we’re excited to share some of our ideas soon.

### Onboarding guides to get started

To help new users get started quickly, we also added an onboarding guide at the top of the homepage, covering Observability, Evaluation, and Prompt Engineering.

## Improved resource organization with Resource Tags

In LangSmith, **Workspaces** are designed to separate resources and provide dedicated environments for different teams or business units within an organization. However, as teams have grown in LangSmith, so has the need for better resource organization within workspaces. Earlier this year, we introduced [**Resource Tags**](https://changelog.langchain.com/announcements/resource-tags-to-organize-your-workspace-in-langsmith?ref=blog.langchain.com) to enhance resource grouping and accessibility.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4107bc92c96efbbf84_Creating-a-new-resource-tag.png)Creating a new resource tag in LangSmith

We’ve now made resource tags even more intuitive and flexible. In a typical application, you might have multiple tracing projects for different LLM pipelines, various datasets, numerous prompts, and numerous annotation queues. We aim to simplify how these resources can be logically grouped and accessed.

Initially, we considered introducing a strict “Application” concept, where each resource would belong to a single application. However, UX research revealed that this was too rigid; users often need resources to span multiple projects or want to organize resources by environment (e.g. dev, staging, or prod), rather than solely by project.

**Resource tags** now offer this customizable grouping. You can filter by “Application” by default, or just create and filter by custom tags that suit your workflow. This flexibility supports varied organizational needs, including environment-based separation, making resources easy to locate and manage.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4107bc92c96efbbf7c_Filtering-by-application.png)Filtering by “Application” or custom tags![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae4107bc92c96efbbf81_View-of-resource-organized.png)View of resources organized by “Application” - in this case, it displays resources for the chat-langchain application.

To further enhance security and customization, we’ll soon introduce Attribute-Based Access Control (ABAC) for resource tags. This feature will enable fine-grained access control for teams to assign conditional permissions based on specific tag attributes, so users can securely organize and access resources across different projects and environments.

## Try out LangSmith

Explore the new LangSmith homepage and features today at [smith.langchain.com](http://smith.langchain.com/?ref=blog.langchain.com) — and let us know what you think through the in-app feedback form.

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