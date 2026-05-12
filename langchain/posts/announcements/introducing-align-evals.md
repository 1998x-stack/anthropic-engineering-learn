---
title: "Introducing Align Evals: Streamlining LLM Application Evaluation"
author: "LangChain Accounts"
date: "2025-07-29"
url: "https://www.langchain.com/blog/introducing-align-evals"
---

Deployment

# Introducing Align Evals: Streamlining LLM Application Evaluation

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 29, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa8bdddec1fc20580dcf_ALIGN-EVALS--3-.png)Evaluations are a key technique for improving your application — whether you’re working on a single prompt or a complex agent. As you compare models, update logic, or iterate on your architecture, evaluations are a reliable way to score outputs and understand the impact of your changes.

But, one big challenge we hear consistently from teams is:* &quot;Our evaluation scores don&#x27;t match what we&#x27;d expect a human on our team to say.&quot; *This mismatch leads to noisy comparisons, and time wasted chasing false signals.

That’s why we’re introducing **Align Evals,** a new feature in LangSmith that helps you calibrate your evaluators to better match human preferences. This feature was inspired by [Eugene Yan&#x27;s article](https://eugeneyan.com/writing/aligneval/?ref=blog.langchain.com) on building [LLM-as-a-judge](https://www.langchain.com/articles/llm-as-a-judge?ref=blog.langchain.com) evaluators.

This feature is **available today** for all LangSmith Cloud users and will be released to LangSmith Self-Hosted later this week. View our [video walkthrough](https://www.youtube.com/watch?v=-9o94oj4x0A&amp;ref=blog.langchain.com) or read our [developer docs](https://docs.smith.langchain.com/evaluation/tutorials/aligning_evaluator?ref=blog.langchain.com) to get started.

## **Creating high quality LLM-as-a-judge evaluators just got easier**

Until now, iterating on evaluators has often involved a lot of guesswork. It&#x27;s hard to spot trends or inconsistencies in evaluator behavior and, after making changes to your evaluator prompt, it can be unclear which data points caused scores to shift or why.

With this new LLM-as-a-Judge Alignment feature, you get:

- A playground-like interface to iterate on your evaluator prompt and see the evaluator’s “alignment score”
- Side-by-side comparison of human-graded data and LLM-generated scores, with sorting to identify “unaligned” cases
- A saved baseline alignment score in order to compare your latest changes to the previous version of your prompt

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa8cdddec1fc20580e77_image-11.png)

## **How it works**

Here’s how the alignment flow works:

**1. Select evaluation criteria**

The first step is identifying the right evaluation criteria. Your eval criteria should include the things your app should do well. For example, if you’re building a chat app, correctness is important —but so is conciseness. A technically accurate answer that takes many paragraphs to get to the point will still frustrate users.

**2. Select data for human review**

Create a set of representative examples from your app. These should cover both good and bad examples —the goal is to cover the range of outputs that your app would actually generate. For example, if you’re working on adding a new product that your customer support assistant can answer questions about, include both correct responses and incorrect ones.

**3. Grade the data with expected scores**

For each eval criteria, manually assign a score for each example. These scores become your “golden set” which will serve as a benchmark against which the evaluator’s responses will be judged.

**4. Create an evaluator prompt and test it against the human grading**

Create an initial prompt for your LLM evaluator and use the the alignment results to iterate. For each version of your prompt, you&#x27;ll test it against your human-graded examples to see how well your LLM&#x27;s scores align with yours.

For example, if your LLM consistently over-scores certain responses, try adding clearer negative criteria. Improving your evaluator score is meant to be an iterative process. Learn more about best practices on iterating on your prompt in our [docs](https://docs.smith.langchain.com/evaluation/tutorials/aligning_evaluator?ref=blog.langchain.com#tips-for-improving-evaluator-alignment).

## **Whats next?**

We’re just getting started. This is the first step towards helping you build better evaluators. Looking ahead, you can expect:

- **Analytics** so you can track how your evaluator’s performance evolves over time.
- **Automatic prompt optimization**, where we automatically generate prompt variations for you!

Give it a try! Get started by [heading to our developer documentation](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback?ref=blog.langchain.com) or watch our [video tutorial](https://youtu.be/-9o94oj4x0A?ref=blog.langchain.com). Let us know what you think by providing feedback in the [LangChain Community fourm](https://forum.langchain.com/t/introducing-align-evals-streamlining-llm-application-evaluation/817?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92b9f48cfd92b76f4795_Nullframe-Moda.png)Case StudiesDeep AgentsDeployment

#### How Moda Builds Production-Grade AI Design Agents with Deep Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 24, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)6min[](/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cb92becc1b0764b5d200f1_agent-identity-banner.png)Harrison&#x27;s In the LoopDeploymentAgent Architecture

#### Two different types of agent authorization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedd2eda55edd2cc8a271_Harrison.png)Harrison ChaseMarch 23, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/two-different-types-of-agent-authorization)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba997e64abfa0ac01a371_LangSmith-Sandboxes.png)Company AnnouncementsLangSmithDeployment

#### Introducing LangSmith Sandboxes: Secure Code Execution for Agents

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)3min[](/blog/introducing-langsmith-sandboxes-secure-code-execution-for-agents)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)