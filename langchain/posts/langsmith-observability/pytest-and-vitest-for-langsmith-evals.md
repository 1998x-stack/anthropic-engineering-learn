---
title: "Introducing Pytest and Vitest integrations for LangSmith Evaluations"
author: "LangChain Accounts"
date: "2025-01-22"
url: "https://www.langchain.com/blog/pytest-and-vitest-for-langsmith-evals"
---

Company AnnouncementsPartnerLangSmith

# Introducing Pytest and Vitest integrations for LangSmith Evaluations

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJanuary 22, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0bcbdf13f9a16534a7_Blog-with-Image---baga-blog---updated-title.png)Evaluations (evals) are an essential part of building reliable and high-quality LLM applications.  They help you assess performance of your application, ensuring that quality remains consistent as you make updates. If you come from a software engineering background, you’re likely familiar with using tests for this purpose.  To extend this familiar interface, we’re excited to introduce a new way to run evals using **LangSmith’s **[**Pytest**](https://docs.smith.langchain.com/evaluation/how_to_guides/pytest?ref=blog.langchain.com)** and **[**Vitest/Jest**](https://docs.smith.langchain.com/evaluation/how_to_guides/vitest_jest?ref=blog.langchain.com)** integrations.**

These new integrations are available now in beta with v0.3.0 of the LangSmith [Python](https://github.com/langchain-ai/langsmith-sdk/tree/main/python?ref=blog.langchain.com) and [Typescript SDK](https://github.com/langchain-ai/langsmith-sdk/tree/main/js?ref=blog.langchain.com)’s.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534c1_AD_4nXeypfDgdqNebNk7QQpIYVCtzkWoSc6P2P5Q_Bw1plGpeDiYmfz7iu_9VtJ2vDbWYCeDsKh9cPZR2PgxkfU9SBosIbezHQeGaDiHsnAhfTztMv8RvoO4X7yc28ydaJ3OZPxqj70yZA.png)

## Why use testing frameworks for LLM evals

If you’re already using [Pytest](https://docs.pytest.org/en/stable/?ref=blog.langchain.com) or [Vitest](https://vitest.dev/?ref=blog.langchain.com)/[Jest](https://jestjs.io/?ref=blog.langchain.com) to test your application, the new LangSmith integrations give you the flexibility, familiarity and runtime behavior of Pytest/Vitest with the observability and sharing features of LangSmith. These integrations use the exact same developer experience (DX) you’re used to, and have the following benefits:

**Debug your tests in LangSmith**

Applications that use LLMs have additional complexity when debugging due to their non-determistic nature. LangSmith saves inputs/outputs and stack traces from your test cases to help you pinpoint the root cause of issues.

**Log metrics (beyond pass/fail) in LangSmith and track progress over time **

Typically, testing frameworks focus only on pass/fail results, but testing LLM applications often requires a more nuanced approach. You may not have hard pass/fail criteria; rather, you want to log results and see how your application improves over time. With LangSmith, you can log feedback and compare results over time to prevent regressions and ensure that you&#x27;re always deploying the best version of your application.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534b7_Screenshot-2025-01-22-at-8.55.42-AM.png)

**Share results with your team **

Building with LLMs is often a team effort. We commonly see subject matter experts involved in the process of prompt creation or when creating evals. LangSmith allows you to share results of experiments across your team, making collaboration easier.

**Built-in evaluation functions **

If you’re using Python, LangSmith offers some built in evaluation functions to help when checking against your LLM’s output. For example, [expect.edit_distance()](https://docs.smith.langchain.com/reference/python/_expect/langsmith._expect._Expect?ref=blog.langchain.com#langsmith._expect._Expect.edit_distance) is used to compute the string distance between your test’s output and the reference output provided. For more details on built-in evaluation functions, visit our [API reference](https://docs.smith.langchain.com/reference/python/_expect/langsmith._expect._Expect?ref=blog.langchain.com#langsmith._expect._Expect).

## Get started

Here’s a simple test case to demonstrate how to evaluate an application that generates SQL queries. This test checks whether the application correctly identifies off-topic user input and logs the results to LangSmith. When you run a test suite, a dataset in LangSmith will be created/updated and a new experiment will be created.

**Getting started with Pytest**

To track a test in LangSmith add the  `@pytest.mark.langsmith` decorator.

`# tests/test_sql.py
import openai
import pytest
from langsmith import wrappers
from langsmith import testing as t

oai_client = wrappers.wrap_openai(openai.OpenAI())

# Define your app logic elsewhere:
# @traceable
# def generate_sql(user_query: str) -&gt; str: ...

@pytest.mark.langsmith
def test_offtopic_input() -&gt; None:
    # Log the test case inputs and reference outputs.
    user_query = &quot;whats up&quot;
    t.log_inputs({&quot;user_query&quot;: user_query})

    expected = &quot;Sorry that is not a valid question.&quot;
    t.log_reference_outputs({&quot;response&quot;: expected})

    actual = generate_sql(user_query)
    t.log_outputs({&quot;response&quot;: actual})

    # Use this context manager to trace any steps used for
    # generating evaluation feedback separately from the
    # main application logic.
    with t.trace_feedback():
        instructions = (
            &quot;Return 1 if the ACTUAL and EXPECTED answers are semantically equivalent, &quot;
            &quot;otherwise return 0. Return only 0 or 1 and nothing else.&quot;
        )
        grade = oai_client.chat.completions.create(
            model=&quot;gpt-4o-mini&quot;,
            messages=[
                {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: instructions},
                {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: f&quot;ACTUAL: {actual}\nEXPECTED: {expected}&quot;},
            ],
        )
        score = float(grade.choices[0].message.content)
        t.log_feedback(key=&quot;correctness&quot;, score=score)

    assert actual
    assert score`

Kick off the tests like you usually would:

`pytest tests`

This will run like any other pytest test run and also log all test case results, application traces, and feedback traces to LangSmith.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534bd_Screenshot-2025-01-22-at-8.32.21-AM.png)Left to right, top to bottom: 1. Table of runs for a given test suite, 2. Results for a test suite run, 3. Trace for a test case, 4. Trace for test case feedback.![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534ad_Screenshot-2025-01-22-at-8.32.36-AM.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534ba_Screenshot-2025-01-22-at-8.34.31-AM.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae0ccbdf13f9a16534b4_Screenshot-2025-01-22-at-8.35.03-AM.png)

Visit our [Pytest how-to guide](https://docs.smith.langchain.com/evaluation/how_to_guides/pytest?ref=blog.langchain.com) for the full example.

**Getting started with Vitest**

To track a test in LangSmith wrap your test cases in a  `ls.describe()` block.

`import * as ls from &quot;langsmith/vitest&quot;;

import OpenAI from &quot;openai&quot;;
import { traceable } from &quot;langsmith/traceable&quot;;
import { wrapOpenAI } from &quot;langsmith/wrappers/openai&quot;;

//Set OPENAI_API_KEY as an environment variable
const tracedClient = wrapOpenAI(new OpenAI());

const myEvaluator = async (params: {
  outputs: { sql: string };
  referenceOutputs: { sql: string };
}) =&gt; {
  const { outputs, referenceOutputs } = params;
  const instructions = [
    &quot;Return 1 if the ACTUAL and EXPECTED answers are semantically equivalent, &quot;,
    &quot;otherwise return 0. Return only 0 or 1 and nothing else.&quot;,
  ].join(&quot;\n&quot;);
  const grade = await tracedClient.chat.completions.create({
    model: &quot;gpt-4o-mini&quot;,
    messages: [
      {
        role: &quot;system&quot;,
        content: instructions,
      },
      {
        role: &quot;user&quot;,
        content: `ACTUAL: ${outputs.sql}\nEXPECTED: ${referenceOutputs.sql}`,
      },
    ],
  });
  const score = parseInt(grade.choices[0].message.content ?? &quot;&quot;);
  return { key: &quot;correctness&quot;, score };
};

ls.describe(&quot;generate sql demo&quot;, () =&gt; {
  ls.test(
    &quot;offtopic input&quot;,
    {
      inputs: { userQuery: &quot;whats up&quot; },
      referenceOutputs: { sql: &quot;sorry that is not a valid query&quot; },
    },
    async ({ inputs, referenceOutputs }) =&gt; {
      const sql = await generateSql(inputs.userQuery); //generateSql is a function that given user input, generates an SQL query given
      ls.logOutputs({ sql });
      const wrappedEvaluator = ls.wrapEvaluator(myEvaluator);
      // Will automatically log &quot;correctness&quot; as feedback
      await wrappedEvaluator({
        outputs: { sql },
        referenceOutputs,
      });
    }
  );
});
`

Visit our [Vitest/Jest how-to-guide](https://docs.smith.langchain.com/evaluation/how_to_guides/vitest_jest?ref=blog.langchain.com)** **for the full example.

## Testing frameworks vs. evaluate()

Most popular eval libraries, such as [OpenAI Evals](https://github.com/openai/evals?ref=blog.langchain.com), [Hugging Face’s Evaluate](https://github.com/huggingface/evaluate?ref=blog.langchain.com) and [LangSmith’s evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate?ref=blog.langchain.com) work similarly – you first create a dataset upfront and then define a generation function and a set of evaluators to run over the dataset. This approach tends to work well for use cases where you need to run the same set of evals across a dataset, such as if you’re black-box testing the inputs and outputs of an agent. However, we’ve found that it falls short in some cases.

We’ve integrated the new Pytest and Vitest/Jest integrations in a number of applications we’ve built (videos coming soon!) and found that it has three main benefits:

**Specific evaluation logic for each test case.**

If you want to evaluate specific parts of your application, it’s more flexible and intuitive to define examples and evaluators as test cases than to use [evaluate()](https://docs.smith.langchain.com/reference/python/evaluation/langsmith.evaluation._runner.evaluate?ref=blog.langchain.com). For example, when testing an agent that has access to multiple tools you&#x27;ll want to test your model&#x27;s ability to call each tool. But how you evaluate two tools can be completely different, making it tedious to define global evaluator functions. With the new testing integrations, you can have separate test cases with custom evaluation logic in each. To see this in action, check out our** **[tutorial](https://docs.langchain.com/langsmith/test-react-agent-pytest?ref=blog.langchain.com).

**Real-time local feedback.**

Testing frameworks provide real-time feedback on your test status, which makes it much easier to spot and fix issues as you go. This rapid feedback loop is useful when you’re iterating locally on your application, including mocking out parts of your application, and need to test evals quickly.

**CI pipeline integration. **

Running evals as part of your CI pipeline helps catch regressions early. Testing frameworks naturally support defining pass/fail criteria and raising assertion errors in CI workflows.

In the coming weeks, we’ll be releasing a Github Action to make this especially easy to configure.

## Try it out!

We’re excited to share our new approach to running evals using Pytest and Vitest/Jest integrations! Visit our developer [tutorial](https://docs.smith.langchain.com/evaluation/tutorials/testing?ref=blog.langchain.com) and how-to guides ([Python](https://docs.smith.langchain.com/evaluation/how_to_guides/pytest?ref=blog.langchain.com), [TypeScript](https://docs.smith.langchain.com/evaluation/how_to_guides/vitest_jest?ref=blog.langchain.com)) to get started, and check out our video walkthroughs ([Python](https://youtu.be/2n3IUg97paE?ref=blog.langchain.com), [TypeScript](https://youtu.be/B69i3LojvR0?ref=blog.langchain.com)).

If you have feedback or feature requests, let us know what you think by getting in touch with us through the [LangChain Slack Community](https://langchaincommunity.slack.com/?ref=blog.langchain.com) or opening an issue on [GitHub](https://github.com/langchain-ai/langsmith-sdk?ref=blog.langchain.com). If you’re not part of the Slack community yet, sign up [here](https://www.langchain.com/join-community?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)