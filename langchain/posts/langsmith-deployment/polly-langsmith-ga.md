---
title: "Polly is generally available everywhere you work in LangSmith"
author: "LangChain Accounts"
date: "2026-03-18"
url: "https://www.langchain.com/blog/polly-langsmith-ga"
---

Company AnnouncementsLangSmith

# Polly is generally available everywhere you work in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 18, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c4b9745cbd1116035a_6--2-.png)Debugging agents is different from debugging anything else you&#x27;ve built. Traces run hundreds of steps deep, prompts span thousands of lines, and when something goes wrong, the context that caused it is buried somewhere in the middle.

We built Polly to be the AI assistant that can read a 300-step trace, spot the failure, and tell you exactly what happened. Today, Polly is generally available for LangSmith users.

## What changed

Previously, Polly lived in a handful of places in LangSmith (trace pages, thread views, and the playground). We’ve now expanded the surface area of what Polly can do.

Here’s what’s different today:

- **Polly lives across all LangSmith pages**. Whether it’s tracing projects, runs, threads, experiments, datasets, annotation queues, evaluators, or the playground – Polly is available in every page or workflow at the bottom-right corner.
- **Polly remembers the conversation. **Start debugging a trace, switch to experiments to compare runs, come back, and Polly will still know what you were working on. This persistence across navigation reduces friction as you move from one view to another.
- **Polly can take action.** In addition to answering questions, Polly can also update your prompt, create datasets from failing runs, filter your project view, write evaluator code, and compare experiments. Hence, Polly is like an engineer on your team you can turn to for hands-on help.

## Where Polly shines now

### **Follow the problem wherever it leads**

The hardest debugging problems don&#x27;t live on one page. You start in a trace, realize you need to compare to another experiment, pull an example into a dataset, then go fix the prompt. Polly now follows that workflow with you with context intact the whole way.

In a thread view, Polly can also be very powerful for analyzing a thread (i.e. an entire conversation between users and your agent) across many back-and-forth interactions. Instead of reading through every message yourself, just ask:

- *&quot;Did the user seem frustrated?&quot;*
- &quot;*What issues is the user experiencing?&quot;*
- *&quot;Was the user&#x27;s problem solved?&quot;*
- *&quot;What was the main topic of this thread?&quot;*

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c5b9745cbd111603e5_data-src-image-189bc895-c024-4ff3-86a2-7c9ec1ff9de6.png)Using Polly to understand user sentiment in a thread

Polly answers from the full conversation context and can help you quickly understand user sentiment, conversation outcomes, and interaction patterns.

**Write better evaluators, faster**

Polly now helps you write and refine evaluator logic directly in the Evaluators pane. Ask Polly to write an evaluator that checks for hallucinations, improve an existing one&#x27;s accuracy, or add handling for edge cases. It can generate the code, explain what it&#x27;s checking for, and iterate with you. This lets you spend less time on the scaffolding and more time on *what* the evaluator actually needs to catch.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c5b9745cbd111603e8_data-src-image-7d448aab-cb92-4659-86b5-7eca1022502e.png)Using Polly to write and improve an evaluator

**Turn experiment results into a clear decision**

After running an eval, ask Polly which experiment performed best and it will give you a recommendation grounded in your actual data. You can ask Polly to compare two runs directly. This can help you make the call on which prompt change, model, or architecture actually moves the needle without having to manually parse every result yourself.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92c5b9745cbd111603f0_data-src-image-0f058228-52b6-4a19-91cb-49d292f0d3fd.png)Using Polly to compare the results of different experiments

## How we arrived at Polly

We spent a lot of time working with teams building production agents on LangSmith before we built Polly. The same failure patterns kept coming up: traces too long to scan, prompts too tangled to reason about, conversations too sprawling to follow.

Polly doesn’t replace the engineering judgment, but just handles the parts that slow you down. Polly knows what you&#x27;re looking at, acts on it, and can stay with you for the whole session.

## Get started

If you&#x27;re already on LangSmith, Polly is waiting in the bottom-right corner. You can open Polly with Cmd+I (Mac) or Ctrl+I (Windows/Linux) on any page.

To start chatting with Polly, you’ll need to add an API key for your model provider set as a workspace secret, which takes just 2 minutes. [Learn how in our docs](https://docs.langchain.com/langsmith/polly?ref=blog.langchain.com#get-started).

If you&#x27;re new to LangSmith, you’ll first want to [set up tracing](https://docs.langchain.com/langsmith/observability-quickstart?ref=blog.langchain.com). Once your data is flowing into LangSmith, Polly can start helping you understand what&#x27;s happening and how to improve it.

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