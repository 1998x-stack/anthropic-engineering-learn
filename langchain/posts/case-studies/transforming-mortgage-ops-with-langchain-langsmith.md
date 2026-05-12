---
title: "Transforming Mortgage Ops with LangChain &amp; LangSmith"
author: "LangChain Accounts"
date: "2023-12-05"
url: "https://www.langchain.com/blog/transforming-mortgage-ops-with-langchain-langsmith"
---

Tutorials &amp; How-TosLangChainLangSmith

# Transforming Mortgage Ops with LangChain &amp; LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamDecember 5, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb09f394beb695265a37a_image-8-2-1.png)*Editor&#x27;s Note: This post was written by *[*Sasha Aptlin*](mailto:sasha@aptford.com)* at *[*Aptford*](https://aptford.com/?ref=blog.langchain.com) *through LangChain&#x27;s Partner Program.*

Meet Maya, a loan officer at [InstaMortgage](https://instamortgage.com/?ref=blog.langchain.com), whose professional life was once consumed by the flood of loan applications and constant demands for accuracy and precision. Imagine her desk, buried under piles of paperwork, her inbox constantly filled with client requests, her days a never-ending cycle of entering data manually and conducting thorough reviews.

At InstaMortgage, Maya is not just a loan officer. She is a champion for customer service and education. Her objective is to make sure that the process of obtaining a home loan is transparent and straightforward. However, conventional methods frequently left her clients waiting for an answer for way too long, resulting in more confusion than empowerment.

Maya&#x27;s experience was not unique. Loan officers throughout the mortgage industry encounter the same difficulties: outdated systems, manual procedures, and the need to juggle precision, accuracy, and client satisfaction. It was evident that the mortgage industry, which relied on traditional and error-prone methods, required a significant overhaul.

## Meet InstaAI

Leading the transformation, [InstaMortgage](https://instamortgage.com/?ref=blog.langchain.com) joined forces with [Aptford](https://aptford.com/?ref=blog.langchain.com) to create InstaAI, an AI platform reshaping the mortgage landscape with three core modules powered by Langchain &amp; LangSmith:

- **Mortgage AI** navigates through complex data and guidelines, offering immediate, accurate guidance. Think of a challenging loan application that gets deciphered in minutes, not hours – Mortgage AI makes it possible.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3a8_public.gif)
- **Content AI** enables the creation of clear, concise multi-media content, ensuring that clients are well informed. It also helps Loan Officers build credibility and reputation through content creation that is relevant and educational for future homeowners. Imagine a client receiving tailor-made insights that make complex mortgage concepts easily digestible in the distinctive voice of InstaMortgage – that&#x27;s ContentAI at work.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3b0_public.gif)
- **Policy AI** clarifies InstaMortgage policies, employment practices, benefits, compliance, and communication standards. An ever-present guide, it nurtures a positive, productive workplace environment where every team member can thrive.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a3b3_public.gif)

With InstaAI, Maya&#x27;s role underwent a radical change. Her job evolved from juggling tedious tasks to fostering meaningful relationships at scale. &quot;InstaAI hasn&#x27;t just changed how I work; it&#x27;s redefined my role, supercharging my efforts of enriching the experience for our clients,” she remarks.

## InstaMagic of LangChain &amp; LangSmith

LangChain&#x27;s [LCEL](https://python.langchain.com/docs/expression_language/?ref=blog.langchain.com) has been instrumental in developing InstaAI&#x27;s three core modules, simplifying the construction of dynamic prompts across various data sources, most of which are more than 500 pages long and include tabular data. Under the hood, each user request is rephrased into a question by a separate chain, which is then used to pick the sources to pull from in parallel. The retrieved chunks, enriched with metadata about their source, are then injected into the context before the final run of the “Writer” chain.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0a0394beb695265a39f_image-10.png)

To generate content ideas, InstaAI follows a straightforward multi-step process. Here&#x27;s how it works:

- Randomly select blog posts from the InstaMortgage sitemap.
- Analyze the selected blog posts using an LLM to identify any missing points or generate related ideas.
- Create a rough draft based on one of the seven content types and context from the knowledge base.
- Refine the draft and extract important details such as summary, hashtags, duration (for video scripts), or call-to-action (CTA) into a Pydantic model for future user review.

LCEL has simplified the developer experience to a couple of lines of Python for each of the steps above.

LangSmith had an important role in debugging and logging throughout the development process, as well as monitoring performance in production. Its debugging capabilities enabled precise monitoring and improvement of interactions within each module. By visualizing the exact sequence of events in complex chains that retrieve context from various sources, LangSmith provided insights into the inputs and outputs of LLM calls and ensured that the conversational aspects of MortgageAI, ContentAI, and PolicyAI were logical, precise, and user-friendly.

## Results

Mortgage questions that used to take hours to research can now be completed in minutes or even seconds. InstaAI has not only improved efficiency but also strengthened client relationships. Early results show that speed to resolution has increased by an average of 67%, and error rates have significantly decreased. The impact on client satisfaction is clear, with testimonials like Rupert&#x27;s, a long-term client who said, &quot;The speed and accuracy in handling my request were unlike anything I&#x27;ve experienced before.&quot; This transformation also benefits our employees, as Shashank Shekhar, CEO of InstaMortgage, explains: &quot;With our newfound capabilities, our team can focus on more challenging and fulfilling tasks, thus making their work at InstaMortgage less tedious and way more rewarding.” He further added that the company intends to continue working with LangChain to further its AI capabilities and become a truly AI-powered mortgage company that delivers the best experience for both its employees and clients.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251cee3c69c0b64e26c79_case-study-16_9%20(1).png)Case StudiesLangSmith

#### How Credit Genie used Insights Agent to improve their AI financial assistant

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e251111d491175462a384c_david-li.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e25199461e789ce4b875a7_jeffrey-ngai.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2518d5b449e720f9f295a_goyo-lozano-palacio.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e2515f9f57e45d15dbd331_charles-yuan.png)David LiJeffrey NgaiGoyo Lozano PalacioCharles YuanApril 20, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/credit-genie-insights-agent-financial-assistant)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e113adb98acef39fe4aa32_Reusable-evaluators.png)Observability &amp; EvalsLangSmith

#### Reusable Evaluators and Evaluator Templates in LangSmith

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0006d57fa417eb9caf388_catherine-qiao.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)Catherine QiaoJacob TalbotApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/reusable-langsmith-evaluator-templates)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)