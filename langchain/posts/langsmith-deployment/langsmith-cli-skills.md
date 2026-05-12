---
title: "LangSmith CLI &amp; Skills"
author: "LangChain Accounts"
date: "2026-03-04"
url: "https://www.langchain.com/blog/langsmith-cli-skills"
---

LangSmith

# LangSmith CLI &amp; Skills

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMarch 4, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cba9c6bf847dfe35ee98df_Screenshot-2026-03-03-at-11.52.03---PM.png)We&#x27;re releasing a CLI along with our first set of skills to give AI coding agents expertise in the [LangSmith](https://docs.langchain.com/langsmith/home?ref=blog.langchain.com) ecosystem. This includes adding tracing to agents, understanding their execution, building test sets, and evaluating performance. On our eval set, this bumps Claude Code&#x27;s performance on these tasks from 17% to 92%.

## The LangSmith CLI

At the core is our new [LangSmith CLI.](https://github.com/langchain-ai/langsmith-cli?ref=blog.langchain.com) The LangSmith CLI is designed to be agent-native: it gives coding agents (and developers) the building blocks needed to do anything within [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com). This includes fetching traces, curating datasets, and running experiments. When combined with the guidance in skills, coding agents gain the ability to fluently navigate LangSmith completely through the terminal. We believe that enabling this is critical to the future of agent development, as we expect agent improvement loops to increasingly be driven by other agents that are terminal-first.

You can install the CLI with the following installation script:

`curl -sSL https://raw.githubusercontent.com/langchain-ai/langsmith-cli/main/scripts/install.sh | sh`

## What are Skills?

Skills are curated instructions, scripts, and resources that improve coding agent performance in specialized domains. Importantly, skills are dynamically loaded through progressive disclosure — the agent only retrieves a skill when its relevant to the task at hand. This enhances agent capabilities, as historically, giving too many tools to an [agent would cause its performance to degrade](https://blog.langchain.com/react-agent-benchmarking/).

Skills are portable and shareable — they consist of markdown files and scripts that can be retrieved on demand. We&#x27;re sharing a set of LangSmith skills that can be ported to any coding agent that supports skill functionality.

## LangSmith Skills

Within the [langsmith-skills](https://github.com/langchain-ai/langsmith-skills?ref=blog.langchain.com) repo, we maintain a set of 3 skills:

- trace: add tracing to existing code, and query traces
- dataset: build up datasets of examples
- evaluator: evaluate agents over those datasets

These three areas represent the three core areas of LangSmith AI engineering. We will add to this set of skills over time.

## Skill Impacts

Using skills, we saw significant improvements in Claude Code&#x27;s performance on basic LangSmith tasks.

TestModelPass RateClaude Code without SkillsSonnet 4.617%Claude Code with SkillsSonnet 4.692%

*Pass rate was calculated using LangSmith evaluations. We plan to open source the testing benchmark we used*

These skills enable coding agents to create a virtuous cycle in agent development. Your coding agent can use LangChain and LangSmith skills to:

- Add tracing logic to your agent
- Generate traces with the agent and use them to effectively debug behavior
- Use generated traces to create a systematic testing dataset
- Create evaluators to run on the dataset and validate agent correctness
- Iterate further on the agent architecture based on evaluations and human feedback

This loop is a powerful tool to accelerate agent development. To see it in action, see our demo of the skills:

## **Installation**

You can install these skills using [`npx skills`](https://github.com/vercel-labs/skills?ref=blog.langchain.com):

**Local** (current project):

`npx skills add langchain-ai/langsmith-skills --skill &#x27;*&#x27; --yes
`

**Global** (all projects):

`npx skills add langchain-ai/langsmith-skills --skill &#x27;*&#x27; --yes --global
`

To link skills to a specific agent (e.g. Claude Code):

`npx skills add langchain-ai/langsmith-skills --agent claude-code --skill &#x27;*&#x27; --yes --global
`

## **Conclusion**

We&#x27;re excited for the community to use LangChain and [LangSmith](https://smith.langchain.com/?ref=blog.langchain.com) to improve your experience building with our ecosystem. We plan to continue adding skills content as new capabilities are added to LangSmith. In parallel, we are also releasing [a set of skills](https://blog.langchain.com/langchain-skills/) for interacting with LangChain&#x27;s open source libraries (LangChain, LangGraph and DeepAgents). If you have ideas for additional skills or improvements, we&#x27;d love to hear from you!

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