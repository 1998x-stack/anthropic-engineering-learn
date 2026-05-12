---
title: "Boost Your Bottom Line and Performance: OpenAI’s 3.5T Fine-Tuning with LangSmith"
author: "LangChain Accounts"
date: "2023-08-29"
url: "https://www.langchain.com/blog/chatopensource-x-langchain-the-future-is-fine-tuning-2"
---

PartnerTutorials &amp; How-Tos

# Boost Your Bottom Line and Performance: OpenAI’s 3.5T Fine-Tuning with LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamAugust 29, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18bd2a13d9d6050d8bd_5-social--13-.png)*Editor&#x27;s Note: This post was written in collaboration with *Author *Ryan Brandt from* *the *[*ChatOpenSource.com*](http://chatopensource.com/?ref=blog.langchain.com)* team. It&#x27;s a detailed look at how fine-tuning can meaningfully improve model performance. And how *[*LangSmith*](https://www.langchain.com/langsmith?ref=blog.langchain.com)* + LangChain can help you experiment with different models and measure and compare results.*

Unable to use gpt-3.5-turbo for your most critical AI workflows? Then it’s time to think about fine-tuning. Today, we’ll dive into the perks, prep steps, and cost-cutting advantages, all while putting it to the test with Langchain’s AI evaluator, LangSmith. It’s the next-level upgrade you’ve been searching for.

### **Why Fine-Tuning should interest you**

At [ChatOpenSource.com](http://chatopensource.com/?ref=blog.langchain.com), we see fine-tuning as your next step when out-of-the-box models just don’t cut it. Why keep rephrasing prompts when you can teach your model to grasp context, tone, and complexity? Or those pesky edge cases. Think of it as “showing” rather than “telling” your AI what you need. Trust me, you’ll want to stick around to the end to learn more.

### **Why Fine-Tuning is a Game-Changer**

- Ensure greater consistency in style, tone, or format.
- Amplify the reliability of your desired outputs.
- Improve the model&#x27;s understanding of complex or highly specific prompts.
- Address unique edge cases more effectively.
- Train your model in tasks that are hard to articulate in a prompt.
- cost savings from shorter overall prompts, and using `gpt-3.5-turbo* over using larger prompts with `gpt-4`

### Mastering Data Prep: The Secret Sauce of Fine-Tuning

Before diving into fine-tuning, arm yourself with a robust set of training examples that reflect the dialogues you expect the model to handle. Ensure each dataset aligns with OpenAI&#x27;s [**Chat completions API**](https://platform.openai.com/docs/api-reference/chat/create?ref=blog.langchain.com) guidelines, as illustrated below.

Our sample training setup feeds the chatbot a directive under the **`System`** role, followed by a **`User`** prompt and the corresponding correct answer.

`{
        &quot;messages&quot;: [{
            &quot;role&quot;: &quot;system&quot;,
            &quot;content&quot;: &quot;Given a product review, provide the following fields in a JSON dict, where applicable: \&quot;product\&quot;, \&quot;star_rating\&quot;, \&quot;specific_likes\&quot;, and \&quot;specific_dislikes\&quot;.&quot;
        },
            {
                &quot;role&quot;: &quot;user&quot;,
                &quot;content&quot;: &quot;This desk chair gets 2 stars from me. It&#x27;s uncomfortable and the height adjustment is faulty.&quot;
            },
            {
                &quot;role&quot;: &quot;assistant&quot;,
                &quot;content&quot;: &quot;&quot;&quot;{
                    &quot;product&quot;: &quot;desk chair&quot;,
                    &quot;star_rating&quot;: 2,
                    &quot;specific_likes&quot;: [],
                    &quot;specific_dislikes&quot;: [&quot;Uncomfortable&quot;, &quot;faulty height adjustment&quot;]
                }&quot;&quot;&quot;
            }
        ]
    }
`

Never underestimate the value of edge-case examples, especially when a prompt is missing information crucial for generating structured JSON outputs. OpenAI recommends a baseline of 10 examples for **`gpt-3.5-turbo`** fine-tuning, but the more you include, the more you optimize performance. In this article, we&#x27;re using only 20 training examples to shine the spotlight on how powerful high quality datasets can be.

### **Cost Efficiency with Fine-Tuning**

Don’t underestimate fine-tuning’s ability to slash both costs and lag time. If `gpt-4` has been good to you, you may discover that a fine-tuned `gpt-3.5-turbo` delivers equal or even better results—plus the perks of speedier and more efficient operations. Next, let’s dive into how the pricing models stack up.

Model

Training

Input usage

Output usage

GPT-3.5 Turbo 4K context

N/A

$0.0015 / 1K tokens

$0.002 / 1K tokens

GPT-3.5 Turbo 16K context

N/A

$0.003 / 1K tokens

$0.004 / 1K tokens

GPT-3.5 Turbo Fine-Tuned

$0.0080 / 1K tokens

$0.0120 / 1K tokens

$0.0160 / 1K tokens

GPT-4 8K context

N/A

$0.03 / 1K tokens

$0.06 / 1K tokens

GPT-4 32K context

N/A

$0.06 / 1K tokens

$0.12 / 1K tokens

As you can see, `gpt-4` isn’t cheap, and while relying on larger context windows is currently in vogue, for the moment your wallet won’t be a fan.

### How LangSmith Evaluation Works

Before we unveil each model’s performance, let’s get familiar with our evaluation process. LangSmith provides ready-to-use evaluators, but you’re free to build your own. In our case, we’re leveraging `gpt-4` to assess the outputs from various models, using a chain-of-thought Q&amp;A prompt. If the model’s answer doesn’t match the expected response, it’s labeled INCORRECT. Just like DataDog, you run the code on your end and send the results to LangSmith for logging and comparison.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18cd2a13d9d6050d8ce_Untitled--2-.png)LangSmith’s pre-built evaluators.

Here’s an example of output from gpt-3.5-turbo-finetunedbeing evaluated. gpt-4 uses the provided context in the input as an example of “correct”. You can see how based on that context, the fine tuned model outputted successfully.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18cd2a13d9d6050d8d4_Untitled--3-.png)gpt-3.5-turbo Fine tuned on 20 training examples

gpt-4 on the other hand with the same prompt, fails to pass the same bar:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18cd2a13d9d6050d8c8_Untitled--4-.png)gpt-4-8k incorrectly returning the proper format

### Benchmarking Performance

Now we use LangSmith to determine the efficacy of our fine tuning. We do this by evaluating the baseline **`gpt-3.5-turbo`** , then performing the same evaluation on our **`gpt-3.5-turbo-finetuned`** and comparing the results.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18cd2a13d9d6050d8d1_Untitled--5-.png)LangSmith allows you to easily compare models on the same dataset

When I evaluate the baseline `gpt-3.5-turbo`on 142 example product reviews, it’s median runtime is roughly a third faster. It’s worth noting that the P99 of our fine tuned model is higher, but that was not the case every time we ran a test run.

However, it’s really the accuracy where things get interesting. LangSmith measures the output accuracy of **`gpt-3.5-turbo-finetuned`** at 99 percent correct. It got only 1 incorrect. Let’s take a look at the other models.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb18cd2a13d9d6050d8cb_image--1-.png)

The results are… surprising. Our fine tuned model absolutely destroyed both its baseline self and its upgraded `gpt-4` in output performance. It is true that with larger prompting, `gpt-4` and likely `3.5` might have attained the same performance as the fine tuned model, but our test uses the same prompt for each model to emphasize the difference in outcome.

Let’s plug in the cost numbers from before to show the difference in cost between each run, assuming usage in a low transaction production environment:

Model

Input Tokens

Output Tokens

Input Cost ($)

Output Cost ($)

Training Cost ($)

Total Cost ($)

gpt-3.5-t

3,000,000

1,000,000

4.5

2

0

6.5

ft:gpt-3.5-turbo-0613

3,000,000

1,000,000

36

16

0.2

52.20

gpt-4-8k

3,000,000

1,000,000

90

60

0

150

So we can see that while fine tuning is almost 9 times more expensive than the baseline, it’s roughly 3 times cheaper than `gpt-4`, with substantially better accuracy, and a median response time of nearly 4 times faster. These are massive numbers!

### In Conclusion

Fine-tuning is not just an option but a strategic necessity for organizations seeking to optimize their AI models. We&#x27;ve demonstrated through LangSmith that a fine-tuned **`gpt-3.5-turbo`** model can dramatically outperform its baseline and even **`gpt-4`** in terms of accuracy, response time, and cost-efficiency. Don’t miss the opportunity to supercharge your LLMs-It’s the AI boost your company has been waiting for.

At [ChatOpenSource.com](http://chatopensource.com/?ref=blog.langchain.com) we’re the go-to experts in fine-tuning both OpenAI and open-source models like **`llaama-2`**. Don’t let the AI revolution leave your organization in the dust. We’re experts in customizing high-performance, open-source AI models to fit your data—all at a fraction of the cost of building an in-house ML team. Stay ahead of the curve with [www.ChatOpenSource.com](http://www.chatopensource.com/?ref=blog.langchain.com).

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e122306b7173e8fad25030_81%20(1).png)LangChainPartner

#### A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0e375654393ca0c125e00_siddhant-dash.png)Siddhant DashApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/secure-agents-cisco-ai-defense)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)