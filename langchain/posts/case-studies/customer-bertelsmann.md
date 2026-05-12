---
title: "How Bertelsmann Built a Multi-Agent System to Empower Creatives"
author: "LangChain Accounts"
date: "2025-07-29"
url: "https://www.langchain.com/blog/customer-bertelsmann"
---

Company AnnouncementsPartnerLangGraph

# How Bertelsmann Built a Multi-Agent System to Empower Creatives

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJuly 29, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9b4adc4ed56a45bee3ca_Bertelsmann-case-study--1-.webp)[Bertelsmann](https://www.bertelsmann.com/?ref=blog.langchain.com) is one of the world&#x27;s largest media companies that has produced some of the most influential content of our time. From publishing Barack Obama&#x27;s and Prince Harry&#x27;s bestselling biographies and Pulitzer-winning novels, to producing Emmy- and Academy Award-winning productions like Poor Things and The Young Pope, the company&#x27;s creative teams span dozens of brands and platforms to reach millions globally.

But with that scale also comes a challenge: When a creative or researcher at Bertelsmann asks a seemingly simple question like &quot;What kind of content do we have about Barack Obama?&quot; the answer could be scattered  across dozens of different systems, databases, and platforms.

The internal Bertelsmann Content Search changes that. Built by Bertelsmann&#x27;s AI Hub team using LangGraph, this multi-agent system has gone from early prototype to full production deployment. It now powers content search and discovery across the company, empowering creativity across the entire organization.

## **The Challenge: Unified Search Across a Media Empire**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa90cd1956c2e4fa6f0a_AD_4nXeulBgySdfWXGZbhStSSCOd77PSakjothtqeOm5p2V6hp_6QsCJ2ZHvgJ_oOEA967NC1tJWs9ML4xAw42SkXcjfv_yQObq7HdJN-bWmRsk4AqZ-0pHpZaMxPeaFgRwFkAnxRE-Tvg.png)

##

Bertelsmann&#x27;s creative teams face a unique internal challenge: navigating a vast, decentralized content ecosystem. Across its divisions, the company produces and manages:

- Books and audiobooks
- TV shows, films, and documentaries
- News archives and journalistic content
- Third-party commentary and web trends

Each division at Bertelsmann operates within its own systems, databases, and content workflows. So, if a producer wants to understand what content exists around a trending topic, or if a marketing team needs to identify cross-platform opportunities, they need to know exactly where to look and need to have access to each relevant system.

This fragmentation leads to missed opportunities, research effort duplication, and creative teams spending more time searching for information than creating.

## **The Solution: Multi-Agent Content Discovery**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa90cd1956c2e4fa6f16_AD_4nXdNTtp799B-qyP20hJuh-AdSCptWN2UrKZwOzRx4O8tGW4axsOUxUkN2zo7y7_UX3jusQPylusJCZnn7FHXVorFj_zdq-dtzniV9vFzGXJStQp5s38aYg68Ar1FZETaLEFqXnqonQ.png)

The Bertelsmann Content Search takes a fundamentally different approach. Instead of centralizing all data into a single system— a daunting task given Bertelsmann’s expansive portfolio— the team built a multi-agent system that orchestrates searches across existing platforms and data sources.

Here&#x27;s how it works:

**Natural Language Interface**: Users can ask questions in natural language, such as: &quot;What documentaries do we have about renewable energy?&quot; or &quot;Show me content related to emerging artists in electronic music.&quot;

**Intelligent Routing**: Behind the scenes, a router analyzes each query and determines which specialized agents should handle the search. One agent might query the documentary archives, another searches the catalog for related books, while a third checks internal news archives for journalistic coverage.

**Specialized Domain Agents**: Each agent is purpose-built for its specific domain – understanding the metadata, search patterns, and content types unique to that system.

**Unified Response Generation**: Individual agent responses are synthesized into a single, coherent answer.

**Flexible Agent Deployment**: With LangGraph’s flexible architecture, agents can be deployed directly within the systems that own the data. For example, an agent searching the proprietary news archive can be deployed as a standalone API that internal teams can integrate directly into their existing systems. This means divisions get enhanced agentic search capabilities within their own platforms, while the broader organization benefits from cross-platform search through the unified system.

## **Inside the Architecture**

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa90cd1956c2e4fa6f13_AD_4nXeDeUfL1k0gwhw6RN38H7YJFMSLcIKTJrIX-Iw1gPTf2QuZk2bmvTIh0kGr-8VdG7-C-2cjkOK5WX0j5muBTtQnHJKiwR7BBOE0O4oq0NS8GpTLS4jtyZkd1PQxu16_TQlcDJEk.png)

At the core of Bertelsmann Content Search is a LangGraph-powered multi-agent architecture that coordinates complex, cross-domain content discovery in production. Here’s how it works:

### **Intelligent Query Routing via a Coordinator**

The system begins with a coordinator agent, which analyzes the user questions and sends them to the respective agents. This isn&#x27;t simple keyword matching— the router understands context, intent, and domain relevance to ensure queries reach the most appropriate specialists.

### **Parallelized Domain-Specialized Agents**

These queries then get sent to a central and parallelized node, triggering relevant agents for each specific content domain. For example:

- **Publishing Agent**: Searches catalogs, understanding book metadata, author information, and publication timelines
- **Broadcasting Agent**: Queries archives with knowledge of show formats, air dates, and content classifications
- **News Agent**: Navigates journalistic archives with understanding of article metadata, publication dates, and content categorization.
- **Web Intelligence Agent**: Monitors external trends and commentary to provide context from beyond Bertelsmann&#x27;s owned content.

LangGraph helped Bertelsmann to access these diverse data sources in a variety of ways. The agents interfaced with:

- Vector databases (e.g. Qdrant) for fast semantic search
- APIs for structured queries.
- Graph databases for relationship-based lookup
- Custom tools to simplify complex interactions and boost reliability

### **Response Synthesis**

The final  layer combines individual agent responses into coherent, actionable insights. The system understands relationships between different content types and can identify cross-platform opportunities. Users can also drill down into any content by chatting directly with an individual agent.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cf9bc24c7204277c1913ed_gif111-ezgif.com-resize.gif)

### **Supercharging Agent Use via Modular APIs**

One of LangGraph&#x27;s most powerful features for Bertelsmann’s use case is how easily individual agents can be deployed as standalone APIs. This architectural flexibility allowed the team to serve the same agent that powers their cross-platform search directly to the division that owns the underlying data source. For example, teams can integrate their specialized news agent directly into their content management systems all while maintaining the agents&#x27; availability for the broader unified search platform.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa90cd1956c2e4fa6f0d_AD_4nXdN6NrUNXP5AoPRaKm2EOO1NPOukn-y3kvaV0vG3T3YeNb1BVEau7KJse6bcsf4ofGkUz0o9h42aChinl9AXJrr2jZ1Wn61awEnAv38a6OEFOKniIAUHQfMGP3ev-d4AUVcGH7BXg.png)

As a result, the multi-agent system can kill two birds with one stone: Business units can pick up and use smart, agentic search for data sources that are deployed in Content Search. They can use these agents to help their own teams and place them right in people’s workflows, for example in the news archives UI.

## **Why LangGraph: First mover and still state of the art**

The Bertelsmann AI Hub team started to work with LangGraph the first week it was released— back in 2024, when &quot;agents&quot; were far from the buzzword they&#x27;ve become today. This early adoption proved crucial, and their multi-agent systems are deployed in production today.

&quot;We started exploring a multi-agent approach towards empowering creative discovery in late 2023&quot; says Moritz Glauner, Head of Data Science at Bertelsmann Data Services. &quot;And what was initially earmarked as a pilot for exploring the potential of the still early agentic tech, evolved into fully-fledged internal product development given what turned out to be possible with LangGraph and agentic tech&quot;, adds Carsten Mönning, Bertelsmann AI Hub Lead. &quot;Looking back, we started by exploring a lot of what were then research frameworks across the market,” points out Lion Schulz, Head of Machine Learning at the Bertelsmann AI Hub. &quot;We then quickly realized that LangGraph was exactly what we were looking for, as it offered reliability and predictability for our production systems – so we committed to building our multi-agent system on it, and haven’t looked back.&quot;

In particular, the Bertelsmann team benefitted from LangGraph and its:

- **Modular Design**: The node-based architecture allowed the team to build specialized agents for each content domain while maintaining clean interfaces between components.
- **Production-Ready Infrastructure**: The maturity of the LangChain ecosystem provided the observability and debugging capabilities necessary for lifting the system from prototype to production and maintaining a complex multi-agent system at scale.
- **Scalable Orchestration**: As Bertelsmann&#x27;s content universe expanded, the system could easily accommodate new agents and data sources without architectural changes.

## **Impact: Empowering Creativity at Scale**

Built on LangGraph, the Bertelsmann Content Search has transformed how creative teams find information across the organization:

**Faster content discovery**: What used to require **hours** of searching across multiple systems now takes **seconds**. Creative teams spend less time hunting for information and more time creating with it.

**Cross-platform insights**: The system reveals connections and opportunities that might be missed when searching individual systems in isolation. A documentary producer might discover related books that could inform their research, or a book editor might find inspiration in the news archives.

**Democratized access**: Teams no longer need to know which system contains what information—or have access to every database. The unified interface makes the entire Bertelsmann content universe accessible to authorized users.

**Enhanced collaboration**: By surfacing content across divisions, the system encourages collaboration and identifies opportunities for cross-brand initiatives.

The result is a more agile, informed creative organization that can respond quickly to trends and opportunities while making the most of Bertelsmann&#x27;s vast content portfolio.

## **Looking Ahead: The Future of Agentic Content Systems**

The Bertelsmann Content Search represents more than just a successful deployment— it&#x27;s a proof point for the future of AI in media and creative industries. By starting early with LangGraph and focusing on production reliability from day one, the team has built a system that continues to evolve with the organization&#x27;s needs.

As multi-agent systems become more mainstream, the Bertelsmann Content Search stands as an example of what&#x27;s possible when cutting-edge technology meets thoughtful engineering and real-world creative needs. Even beyond the Content Search, the Bertelsmann AI Hub Team now employs LangGraph in its agentic developments, for example supporting ideation or storyboarding.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc07193192cebc73980fd3_logo%20and%20title%20-%2020%20characters%20max%20(6).png)PartnerDeep Agents

#### Building a company due diligence agent with Deep Agents, LangSmith and Parallel

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01c6959ca5fd924ab432_MattHarris.jpg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fc01b812793b72539057d5_nick%20headshot.jpeg)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd2d50cd0f84dacf92e7b_ProfilePic.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69fbd29baf4c28709e2566a7_headshot.jpg)Matt HarrisNick MartitschSrimanth TangedipalliKaran SinghMay 8, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)9min[](/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)