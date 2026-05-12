---
title: "Berkeley Hackathon Projects: Prize Winners Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/special-feature-berkeley-hackathon-projects-llamaindex-prize-winners-c135681bb6f0"
category: "llamaindex-core"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







We had an awesome time at the Berkeley Hackathon two weeks ago (6/17–6/18). The attendance stats were impressive:



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)


- 1200 hackers
- 262 submitted projects
- 2 real-life llamas 🦙

LlamaIndex sponsored a “Best Knowledge-Intensive LLM App” prize series at the hackathon. The criteria was an app that leveraged a knowledge base of custom data to build innovative new application experiences.

We announced three prize winners along with an honorable mention. We are excited to feature each project in a special highlight below. In each highlight, the creators describe the project mission and what it solves, the implementation+tech stack, challenges, and future directions. Check it out! 👇

# First Prize Winner: Helmet AI

Creators: Jaiveer Singh, Devin Mui, Ethan Mehta, Manav Rathod

Devpost: [https://devpost.com/software/helmet-ai](https://devpost.com/software/helmet-ai)

![](/blog/images/0*GfFIf2fjROahG0NR)

## Introduction

In today’s rapidly evolving business landscape, staying ahead of the competition is paramount for success. However, the deluge of information and the ever-changing market dynamics can make it challenging for business leaders to make informed decisions. In this blog post, we introduce Helmet AI, a cutting-edge market intelligence tool designed to empower leadership teams with real-time insights and a competitive edge. Join us as we explore the capabilities, technology stack, and future prospects of Helmet AI.

## Unveiling Helmet AI

![](/blog/images/0*HU5mhnG6pQ2noJoh)

Helmet AI is an innovative market intelligence tool that harnesses the power of advanced technologies to provide leaders with actionable insights and an unparalleled understanding of the global business landscape. With its context-aware Ingestion Engine and Insight Extractor powered by OpenAI’s GPT models, Helmet AI offers a comprehensive solution for tracking breaking news, uncovering hidden relationships, and extracting valuable, personalized insights from vast amounts of data. For ease of use, Helmet AI displays these insights in a familiar, Twitter-like “Feed” interface. Additionally, Helmet AI offers a Chat interface for users to ask questions about a particular news story to Helmet’s knowledgeable chat agent.

## Key Features and Technology Stack

**Context-Aware Ingestion Engine:**

- Helmet AI’s Ingestion Engine continuously monitors the vast landscape of breaking news and global events. By leveraging techniques such as subscribing to RSS feeds for up to date news data and processing documents with LlamaIndex and LangChain, the engine builds a complete understanding of real-time events and their implications on various user profiles. Embeddings are stored in a Pinecone Vector Database.

**Insight Extractor with OpenAI’s GPT Models:**

- The Insight Extractor component of Helmet AI utilizes the power of OpenAI’s GPT models to identify and concisely explain the intricate relationships between seemingly disparate topics surfaced in your feed. By transforming raw data into actionable insights with intelligent explanations, leaders can make informed decisions based on an understanding of market trends and complex dynamics.

**Scalable Infrastructure:**

- Helmet AI is built on Azure’s robust infrastructure, utilizing a range of services such as App Services, a PostgreSQL Database, and Github Actions for orchestrating Deployments. The implementation also incorporates GraphQL for efficient data retrieval and processing.

![](/blog/images/0*8xKcEOqLiD29X4Pa)

## Challenges Overcome and Accomplishments

During the development of Helmet AI, our team encountered various challenges, including integrating MindsDB with Azure and overcoming limitations with Gmail authentication. However, we were able to overcome these obstacles and successfully implemented Helmet AI in just 36 hours during the Berkeley AI Hackathon. Additionally, we established a seamless deployment process using GitHub Actions, automating manual service orchestration. The experience was particularly rewarding for the first-time hackers on the team.

## Key Learnings

Throughout the development process, our team gained valuable insights. We discovered the importance of setting up deployment flows early on to reduce stress during crunch time. Embracing best practices in software engineering proved crucial. Furthermore, we realized the potential of leveraging advanced language models as implicit knowledge graphs, expanding their applications beyond traditional embeddings.

## Future Prospects

Looking ahead, Helmet AI aims to scale up the Ingestion Engine to handle the entirety of the web, leveraging technologies like AnyScale. The team plans to collaborate with enterprise business development teams to initiate pilot programs and gather feedback for further refinement. With a solid foundation in place, Helmet AI hopes to have an impact on the way leaders gather insights and make strategic decisions.

## Conclusion

Helmet AI represents a solid attempt at a game-changing solution for business leaders seeking to stay ahead in today’s fast-paced business world. By leveraging cutting-edge technologies, including AI-powered insight extraction and explanation and real-time data analysis, Helmet AI empowers leaders to confidently navigate market challenges and seize emerging opportunities. As the tool continues to evolve and expand its capabilities, the future of market intelligence looks promising. Stay tuned for more updates on Helmet AI’s journey towards transforming the way we approach gathering information and strategic decision-making.

# Winner: Split

Creators: Aditya Ariyur, Nikhil Patel, Ronit Nagarapu

Devpost: [https://devpost.com/software/split-pv4hn7](https://devpost.com/software/split-pv4hn7)

![](/blog/images/1*Q4nURcU0-iRh0SjgVIg04A.png)

## Background/Motivation

We wanted to develop an easy-to-use workflow that allowed users to generate personalized emails with the assistance of AI, while retaining the user’s unique writing style and emotion inflections.

## What It Is

Our product learns from your previous emails and trains a custom LLM that will draft emails that sound like you, not like a robot. It learns from your writing style and how you respond to specific people. Then, it generates emails from user prompts that match that style.

## How We Built It

We used the Google API and LlamaIndex to parse through a user’s old emails and develop an LLM model built on OpenAI’s text-davinci-003. Then, we use Hume to understand the user’s tone and emotion in their emails, and associate it with specific subjects and recipients so future
emails can be fine-tuned to fit the user’s emailing habits. The current interface was developed using React.js for the website and a Flask API to interact with the backend LLM model.

## Challenges + What We Learned

It was quite difficult to get all of the different aspects of our model working together in unison, especially establishing the connection between the parsed emails and Hume emotion tags to the LlamaIndex model. We had to experiment with many different tools and prompt styles to get an accurate email generation. However, with a lot of dedication and troubleshooting, we were able to develop a working model to demonstrate our concept and its potential functionality. We learned how rewarding it was to train our own LLM using LlamaIndex. Base LLMs like ChatGPT are already so powerful, so the functionality of training a custom LLM based on your
own data unlocks endless possibilities.

## What’s Next

We hope to completely integrate the code and workflow into a Google plugin or extension so users can easily implement it into their daily emailing. We want to ensure the privacy and security of the user’s data, so we want to experiment with methods to reduce how much data is
sent to third-party services like OpenAI. We also want to dedicate further development to the emotion training, as this could boost the effectiveness of our product and add to our main value proposition of personalized, user-specific email generation.

# Winner: Prosper AI

Creators: Alan Yang, Ashay Changwani, Punit Sai Arani, Vedant Tapadia

Devpost: [https://devpost.com/software/prosper-ai](https://devpost.com/software/prosper-ai)

[Vercel Demo](https://prosperai.vercel.app/) / [YouTube Video](https://www.youtube.com/watch?v=_-v0BhFPjAQ)

## Overview

Prosper AI is a trailblazer in utilizing Artificial Intelligence to unlock your full financial potential. It serves as an accessible and smart virtual financial advisor, armed with precise insights and personalized advice. Our mission is to democratize financial expertise. By bridging the resource gap, Prosper AI aims to level the playing field for all.

## The Genesis of Prosper AI

The spark that ignited Prosper AI was a simple observation of the wealth disparity among different social classes. The rich have always had access to knowledge and resources that help in growing and safeguarding their wealth. In contrast, those from modest backgrounds often lack the necessary knowledge and tools to utilize what they earn effectively. Many resort to social media for financial advice, which is often generic and occasionally unreliable as it comes from unqualified influencers. Hiring a financial advisor, on the other hand, could be exorbitant and impractical for those with a limited budget.

This is where Prosper AI steps in. We embraced the challenge to develop an innovative solution utilizing state-of-the-art technology and models to help digest and simplify complex financial data.

## The Prosperity Engine: How Prosper AI Works

Prosper AI sources your financial data from any number and type of bank or investment account to provide qualified financial advice that adheres to regulatory policies, to give you personalized tips, advice and explanations.

Prosper AI achieves this by leveraging an open finance provider such as Plaid to source users financial information. Then Prosper AI will ask a series of financial goal questions to help contextualize the ideal outcomes for the user. Using this combination of personal financial data and goals, Prosper AI will provide a set of optimal and personalized recommendations on how to achieve these goals.

The beauty of Prosper AI lies in its interactivity and support. Users have the liberty to pose questions at any juncture if they find something perplexing. This is particularly invaluable for demystifying complicated charts or financial jargon. Furthermore, Prosper AI goes beyond just answering questions about the current recommendations. It’s like having an expert financial advisor at your beck and call, ready to generate insights, charts, and suggestions for any aspect of your financial landscape. Whether it’s planning for retirement, optimizing investments, or understanding tax liabilities, Prosper AI stands ready to guide users with precision and personalized insights to cultivate financial acumen and empower smarter financial decision-making.

## The Building Blocks of Prosper AI: A Look into Our Tech Stack

**Backend: **Our backend, the engine that powers Prosper AI, is written in Python and based on a FastAPI server. We chose Python because of its agility and the vast availability of open-source libraries that expedite the development process. Additionally, Python’s native packages provided by OpenAI and Plaid seamlessly integrate with our backend, ensuring both development and runtime efficiency.

One of the cornerstones of Prosper AI’s backend is a powerful prompting pipeline which simulates a fine-tuned model. To achieve this, we tap into the capabilities of OpenAI’s GPT-4, enhanced with function calling, and interlink it with Pinecone’s vector database using additional tools like LlamaIndex. This fusion forges a streamlined yet powerful interface.

**Frontend:** When we started out, especially during the hackathon phase, we developed the web application frontend using Next.js, which was our comfort zone. However, as we progressed and aimed for higher benchmarks, we recognized the need to migrate to a more performant framework. We decided on SvelteKit, which stands out for its simplicity and performance, significantly accelerating the development process.

One of our key objectives is to make Prosper AI accessible and user-friendly. We crafted a minimalist user interface, which declutters the screen while maintaining the essence of information. Moreover, we supplemented this with visualizations, which are crucial in translating complex financial data into understandable and actionable insights for the user. Through this combination of a robust backend and an intuitive frontend, Prosper AI is poised to revolutionize personal financial management.

## Overcoming Challenges: The Journey of Prosper AI’s Development

The primary challenge we encountered during the initial stages was the creation of a pipeline to ingest and process years of financial data analytically. The sheer volume of data was not just overwhelming to handle all at once, but it was also crucial to process it responsibly and meaningfully.

To tackle this, we had to design a system that dissected the vast financial data into digestible segments, structuring it in an orderly manner that enabled logical understanding and actionable insights. Although crafting such a system under time pressure was strenuous, it offered us a valuable insight into the magnitude of data we were dealing with. It further emphasized the significance of our mission: to efficiently and comprehensively process such vast data for the benefit of our users.

Another demanding task was incorporating the complexities of tax code into our platform. Thousands of pages of tax regulations had to be converted into intelligent code, capable of offering savvy financial suggestions. Despite the enormous effort this task required, it was crucial in creating a comprehensive wealth management system. The result is a platform that delivers an optimized, personalized financial plan tailored to each user’s specific goals and needs, as well as future plans. Our platform not only identifies the type of accounts and the cash flow strategies that would minimize tax liabilities but also charts a roadmap for maximizing net worth growth over the next 30 years.

This is the essence of Prosper AI — using technology to simplify complex financial management and facilitate the path towards prosperity.

## The Road Ahead for Prosper AI

As we set our sights on the future, the Prosper AI team is more determined than ever to make strides in revolutionizing personal wealth management. Our immediate focus is to transition into full-time startup mode, which entails delving deeper into the development of feature functionalities and solidifying the foundation of our platform.

A key milestone on our roadmap is engaging in pilot use cases with our initial group of customers who have eagerly joined our waitlist. This phase is critical, as it allows us to validate the effectiveness and impact of Prosper AI in real-world scenarios. Through feedback and insights gathered from this initial group, we’ll be able to refine and enhance the platform to ensure it not only meets but surpasses the expectations of our users.

But we won’t stop there. The learnings from the pilot phase will serve as the springboard for subsequent developments and innovations. As we continue to harness cutting-edge technology and data analytics, Prosper AI aims to democratize access to financial knowledge and tools that can empower individuals to unlock their financial potential.

Stay tuned as Prosper AI embarks on this exciting journey towards transforming the landscape of personal finance, making it more accessible, intelligent, and personalized for all.

Together with Prosper AI, let’s cultivate the seeds of financial growth and harvest the fruits of prosperity.

## Video/screenshots/links to material.

Learn more and join our waitlist for a chance to win a $50 Amazon voucher:

[

## Unleash The Power of Comparison

### Tap into Prosper AI, your intelligent sidekick for personalized &amp; optimal financial advice.

prosperai.vercel.app

](https://prosperai.vercel.app/?source=post_page-----c135681bb6f0--------------------------------)

[https://www.youtube.com/watch?v=_-v0BhFPjAQ](https://www.youtube.com/watch?v=_-v0BhFPjAQ)