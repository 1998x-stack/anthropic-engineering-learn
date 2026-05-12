---
title: "Building Open-Source Codebase Copilot with Code Execution Layer"
author: "Tereza Tizkova"
date: "2024-03-12"
url: "https://e2b.dev/blog/building-open-source-codebase-copilot-with-code-execution-layer"
category: "case-studies"
site: "e2b"
---

**Ted Spare** is one of three co-founders of [Rubric Labs](https://rubriclabs.com/) - an AI-focused software studio. The Rubric Labs team works with startups and financial firms, builds AI-enabled products and features with them, and invests in open-source. They also build their own AI projects like assistants for various coding tasks or [calendar management](https://cal.com/ai) (Cal).

We asked Ted what it's like to build an AI-powered GitHub copilot, how he makes techstack choices, and how he leverages the open-source community.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797902b8cf6ddbcc635a08c_67978fdf4c6e463edd3f496f_gAIlmVxfZyVeCx9NPBrTF48kzQk.webp)

## Introducing a GitHub codebase copilot

One of your popular projects within Rubric Labs is [Maige](https://maige.app/). Can you please introduce it?

Maige is an AI companion for codebase managers or open-source maintainers. It can do anything that a person could do with the GitHub API, from labeling issues to reviewing pull requests. It can even start to write basic code and run it in [E2B sandboxes](/docs?ref=e2b-blog).

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797902b8cf6ddbcc635a089_67978ff562300cbe810a05d6_FXFeQ2dU9WXI3aIAaM3qr0a7mk.webp)
I’ve seen that Maige is in the alpha stage as of today. Who are your users and how do you work with them?

Maige has been installed on more than 2,000 GitHub repos. For example, the issues-labeling use case is being used on [Cal.com](http://cal.com/), a repository with over 27,000 stars and hundreds of collaborators or contributors. We spend a lot of time with users, watching them go through the onboarding flow. That helps us to spot papercuts and see how they interact with the product.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/6797902b8cf6ddbcc635a086_679790104e12c0c0e348383d_r5WC2IajgPloPaMYwohJL4DPnMk.webp)

## Techstack considerations

What does the AI agent’s workflow look like and what is the underlying architecture?

Open-source maintainers integrate Maige with their repository (this takes about three clicks) and they get started writing custom rules to specify what the Maige agent should do based on certain events. For example, the agent can react every time an issue related to a certain topic is created.

Maige has a very lean event-driven architecture. When a repo is added, and then later on when an issue is opened or a comment is added, there are a whole set of actions that have to take place. The set of actions can be customized through natural language.
Can you describe the tech stack of your product, as well as your thought process when choosing individual components?

Maige runs in a serverless function and then it spins up the Node.js environment in [E2B](/). As a team of TypeScript developers, our frontend choices are Next.js, then Tailwind, and Schadcn.

We use OpenAI embedding endpoints and the latest GPT-4 Turbo because it's currently the best at what we want to do, but we have our eyes on the [Code Llama](https://huggingface.co/codellama) family of models and [Groq](https://groq.com/) hardware for inference. It's very fast.

The vector database we chose is [Weaviate](https://weaviate.io/) hosted on [Railway](https://railway.app/) - which has been working greatly for us.

We have [Planetscale MySQL](https://planetscale.com/) as the database chosen for the other parts. We focused on portability and the ability to self-host which is available to all users, since [Maige is open-source](https://github.com/RubricLab/maige).

Self-hosting shows users that we're not trying to lock them in and they can continue using the infrastructure even if the team behind the product switches gears and stops maintaining the product. I’ve noticed on tech Twitter that not locking people in one type of tech stack is being put an even higher emphasis on recently.

## Execution layer for AI-generated code

You mentioned running code in E2B sandboxes. Why do you use it and what exactly is happening in the sandbox?

E2B is officially communicated as a cloud sandbox for AI agents and that's exactly how we use it.

Every repository that integrates with Maige gets its own sandbox for the AI agent to run in. The repository is cloned in the sandbox, the dependencies can be installed there, and the agent can run shell commands the way a junior developer would. It can run tests or try to reproduce an issue or an error or even write code, commit it, and open a pull request. That is, we use E2B as the kind of developer workspace for Maige, and every repo gets its own isolated sandbox instance.
What alternatives were you considering before choosing E2B for this purpose?

We probably would have used just [AWS](https://aws.amazon.com/free/?gclid=Cj0KCQjw-r-vBhC-ARIsAGgUO2C3x1L33z14opqMc_OjxMObfdgNfi8PO0ZfqXry6Tzk_sXRxbAU77kaAmB_EALw_wcB&trk=f17b4b4e-aa1b-4189-b0c4-81a19b53f625&sc_channel=ps&ef_id=Cj0KCQjw-r-vBhC-ARIsAGgUO2C3x1L33z14opqMc_OjxMObfdgNfi8PO0ZfqXry6Tzk_sXRxbAU77kaAmB_EALw_wcB:G:s&s_kwcid=AL!4422!3!645186168166!e!!g!!aws!19579892551!148838343321&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all). We are not infrastructure engineers so that would mean a great challenge to make it scalable and cost-effective in-house. That's also why we chose E2B.
How do you ensure the sandboxes are tailored exactly to the needs of the Maige copilot?

We set up the [custom sandbox](/docs/sandbox/templates/overview) for writing and committing code. We just clone the user's repository, sign in to GitHub as a bot user, open a pull request, and have it attributed to the right bot.

## Leveraging the open-source community

You mentioned Maige is open-source. Is this a strategic decision for you? What benefits of open-source do you consider important?

Of course, it’s a personal preference, but I am naturally attracted to open source because I see how impactful such projects are and that they don’t have to rely on one person. That's really important. Any tool that makes scaling and maintaining a project easier is useful.

Another consideration is that I see costs to develop software dropping with AI. Thanks to AI it's harder and harder to build a moat around proprietary software. Going the open-source way, I believe Maige is aligned with the trend of software becoming commoditized.

Finally, we like to work with open-source customers because naturally their use cases are shown in public, which helps form the network around the product. In that way, we can provide a lot of open-source project discounts and free credits.
What does the space of GitHub AI agents look like currently?

There are more players in the space, like [Sweep.dev](https://sweep.dev/), [Dosu.dev](https://dosu.dev/), and [Codegen](https://www.codegen.com/) which is heavily funded and focused on large repositories. I see room for all of them if we grow the pie and allow small teams to scale a community around a commercial open-source company, which is a trend we see for more and more products. 

## Challenges of building AI agents

What are some of the biggest struggles that you have to overcome when building Maige?

There is always the technical challenge of AI agents being non-deterministic and generative AI not being very good at writing code and it's even harder to get it to insert code or modify code. AI agents still can get stuck in loops or give up the task, so the question is how to make them more effective.
The security topic is a big part of AI discussions. How important is it for your users and how do you approach it?

To ensure security, we are conservative with major outputs and are confident in features before putting them into production.

Within Maige, we ask for some generic permissions, for example, to open a pull request. Even if that raises concerns for some users, we address those by reminding users of branch protection rules and that the AI agent isn’t allowed to commit code to their production environment without review.

## Future outlook

What’s your plan for the upcoming months?

We want to get deeper into front-end development with a vision-based AI and be able to identify accessibility issues or just UI bugs. There is a lot of room for growth there.

We also want to improve the code search feature. Now we embed the full code base that integrates Maige with a vector database and this kind of search still has room for improvement.
With the advancements of LLMs and AI techstack overall, how do you think the future AI space development will impact Maige?

According to betting markets, we can expect GPT-5 around October. We are seeing [open-source models getting better](https://rubriclabs.com/blog/designing-for-abundant-intelligence) and I think that even having GPT 3.5 level models that are 10 or 100x cheaper or faster could yield some really interesting results. Maige uses an AI agent so it runs in an open-ended loop and if we could have that loop 100x faster and cheaper, it could be a lot more exploratory and a lot less efficient, but also do more interesting things.

That’s what I'm really excited about.

## Discover more

- [Rubric Labs web](https://rubriclabs.com/)
- [Maige web](https://maige.app/)
- [Ted Spare - X (Twitter) profile](https://twitter.com/TedSpare)
- [Rubric Labs - X (Twitter) profile](https://twitter.com/rubriclabs)