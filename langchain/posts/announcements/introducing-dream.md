---
title: "Introducing Dream – an AI no-code tool to build fully functional web apps and components with natural language"
author: "LangChain Accounts"
date: "2023-11-21"
url: "https://www.langchain.com/blog/introducing-dream"
---

Agent ArchitectureTutorials &amp; How-Tos

# Introducing Dream – an AI no-code tool to build fully functional web apps and components with natural language

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamNovember 21, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb0c3504e43f62959f63e_Twitter-post---23.png)I’m Calix, and I’m currently a sophomore at USC Iovine &amp; Young Academy. For my hacker residency at LangChain, I continued working on my project, Dream.

Dream is an AI no-code tool to build fully functional web apps and components with natural language. Whether it’s an AI app, a game, or an internal tool, Dream is a way for any technical or non-technical person to build and deploy functional websites. Users on Dream can create website projects, they can create pages within each project, and within each page, they can generate sections that can either be design or functionality-focused. Each section acts as a component, whether it&#x27;s a navigation bar or a blog post generator. Integrations like database storage, authentication, or APIs (OpenAI, Twilio, etc.) are built as modular functions, specifically selected for each section’s generation/regeneration. Upon publishing the project, all of the pages and sections are compiled together and deployed to a custom domain.

## Getting started

At the beginning of my residency, Dream was at a semi-completed stage. I had started Dream back in the summer, thinking “If GPT-4 can generate code, can it generate functional web apps with enough iterations?” I was then working on the 3rd version of Dream, each version becoming more focused on performance, extensibility, and generation quality. Many of the big shifts between each version involved breaking up language operations to become more modular and organized so that the output quality could consistently improve as users iterated on their projects.

At the start, I just wanted to make a few improvements to the code generation process and improve the UX, but it continually grew into a longer, more ambitious roadmap. Here are all of the improvements I made to Dream, and how I did it.

## UX for prompt enhancement

The ultimate goal of Dream is to become an all-encompassing platform for anyone (especially non-technical people) to build functional software and share it with the world without coding or facing a steep learning curve. So, the first major problem I tackled was building a comprehensive UX for a non-technical audience.

There were many questions to be answered. How do you build a platform to empower a user to turn thoughts into words, and words into code? How do you convey an experience that helps the user clearly articulate what they want in their project, even when most of the time they don’t even know what they want? How do you balance user-directed context/instructions with AI-directed decisions in generations? And the hardest one, how do you help a user debug their project and handle unforeseen edge cases from a non-technical perspective?

I wrestled with these questions over the 10 weeks and continued to think about ways to optimize the user’s experience.

I first tried to build a conversational agent to guide the user through their thoughts and articulate what they wanted to build. However, it was hard to properly detect the end of a user’s articulation without either cutting them off early or droning on for way too long and being way too specific.

Then, I tried to take a survey approach, asking a set of templated, open-ended questions, forcing the user to spill cognitive context. This worked much better, but it was still not a great input for my code generation inference.

Finally, I wrestled with a few different iterations to build out what’s currently being used. First, the user fills out a templated survey with open-ended questions and some multiple-choice answers that direct the logical flow of the survey. Then, using that context, an overview of the section or modification being generated is created, and from that, the integrations/data sources as well as a technical scope of the generation are created and displayed to the user for approval. After it’s user-approved, it passes the overview and the technical scope as context, allowing a detailed technical explanation to be generated from a few simple answers from the user survey.

### Improving custom integrations

One of the most important features that makes Dream versatile and dynamic is custom integrations. Dream has pre-built integrations to services and functions that users commonly need, like OpenAI or file extraction. But, Dream users also needed to use integrations and APIs that weren’t already pre-built. This is where custom integrations came in. Previously, Dream had enabled custom integrations by requiring the user to specify all the details of the specific endpoints and API calls they wanted. This still required technical knowledge and a clear vision of the project, which were both pretty big barriers.

The new experience I wanted was similar to Cursor — a user can drop a link to the documentation of the integration they want to add, the documentation will be scraped and saved in memory, and the new integration can be used by just mentioning it semantically and describing the desired functionality.

My first approach to building this out was simple: scrape all of the unique links that held the same apex domain (ex. “docs” subdomain), scrape all the content off each page, chunk + embed it, and then retrieve relevant chunks upon generation time. The issue became clear: there was so much hidden gibberish content and metadata on the pages that the retrieval became continually more inaccurate.

My second approach was to scrape all of the page contents but then use LangChain’s contextual compression upon generation time to chunk and retrieve relevant documents to use. This produced better results, but the context window was extremely long, making retrieval much more expensive and still relatively inaccurate.

Finally, the approach I settled on utilized both embeddings and Claude 2. I realized that I just needed to scrape the content off of the API reference and pages that included information about REST API information specifically (not SDKs!). To do this, I used Claude 2’s 100k context window and some basic regular expression matching to classify the content of each page to determine if it was relevant to be scraped. After filtering, all of the page content would be chunked and embedded. Upon generation time, relevant vectors are queried and then compressed using LangChain contextual compression.

## Migrating generation output from HTML/JS to React

Before, Dream was generating raw HTML with TailwindCSS and vanilla JS for function calling and integrations. I knew this system had to change and with the support from LangChain (s/o Jacob!) I decided to migrate all projects to generating React instead. There were a few reasons behind this decision:

React was cleaner, more versatile, and easier to work with

2. The context and completion lengths of my inference were getting too long since raw HTML/JS isn’t as token-efficient as React

3. It opened up the opportunity to work with pre-built components and UI libraries that would normally take up a lot of tokens to write logic and styling for

Making the change wasn’t too hard since it was mainly a change in the prompts, but I took a good amount of time to set up the context to instruct GPT-4 how to properly use the UI component libraries I was feeding it (for now, shadcn UI). Just like integrations, I set up an LLM selection pipeline to select the UI components that were most relevant to the generation being made, so that the context length could be cut as short as possible and my inference calls were more specific and modular.

## Pivot prompting style and context management

I was pretty happy with the improvements I had been making, but randomly on Hacker News, I came across openv0. It was an open-source build of v0, a popular platform that Vercel had been promoting in private beta in the first few weeks of my hacker residency. I was well aware of v0 and what directions they wanted to take with it and didn’t necessarily feel threatened.

With openv0 being open-source, I got the opportunity to see how someone else was approaching the problem of optimizing generation quality. As I looked through the repo, I saw a lot of opportunities on how I could clean up my code and manage my context templates and dynamic injections a lot cleaner and more effectively.

More importantly, I made a strong pivot from my previous prompting strategy, which was heavily example-based. I had 3 custom-written section examples put into the context to guide the inference to follow specific output formats, but it ended up commonly generating designs that were all very similar and clearly showed bias in certain edge case generations. With inspiration from openv0, I fully removed my contextual examples and shortened my context window by a great deal while still maintaining good quality and improving the model’s design flexibility.

## Conclusion

Throughout the 10-week residency, I made so many more changes and improvements to Dream than I had initially imagined. Over a few months, I realized that a platform like Dream is not one that’s well-suited for a scrappy approach but rather requires a detailed, thoughtful approach with a lot of engineering time.

Non-technical stakeholders trying to build software has been a long-standing problem, and the existing solutions like Bubble have steep learning curves of their own. Code generation is still a very hard technical process to build for in production, and designing an intuitive interface around it is very hard. Non-deterministic platforms still do not have design standards, which gave me the freedom to design completely new modes of interaction.

Dream is still a huge work in progress and the last 10 weeks have been a challenge, but I’m excited to continue to improve the platform and hopefully enable non-technical founders, designers, and others to build software that they could never before.

Huge shout out to LangChain and my mentor Jacob Lee for the support over the last 10 weeks!1 It’s been extremely helpful to have technical guidance on a lot of the problems that I tackled, and it helped me accelerate my engineering time by a lot.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)