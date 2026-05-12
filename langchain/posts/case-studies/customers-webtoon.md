---
title: "How Webtoon Entertainment built agentic workflows with LangGraph to scale story understanding"
author: "LangChain Accounts"
date: "2025-05-19"
url: "https://www.langchain.com/blog/customers-webtoon"
---

Company AnnouncementsLangGraphDeployment

# How Webtoon Entertainment built agentic workflows with LangGraph to scale story understanding

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 19, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7c9c83842382408e76_Webtoon-case-study.png)**WEBTOON Entertainment** (Nasdaq: **WBTN**) is a global digital entertainment company transforming the future of storytelling. Best known as the pioneer of the vertical scroll web comic format, WEBTOON Entertainment operates two of the world’s largest storytelling platforms: **WEBTOON** and **Wattpad**. Together, they connect millions of users around the globe with diverse, creator-driven content across genres such as romance, fantasy, action, and thriller.

With a strong international presence and partnerships across the media industry, WEBTOON Entertainment adapts its original IP into films, TV series, and animations—producing cross-media hits that resonate with global audiences. The company continues to lead the content-tech landscape by investing in cutting-edge AI to support creators and make their lives easier.

To support teams working with massive volumes of content, the team built WEBTOON Comprehension AI (WCAI)—a system powered by agentic workflows using LangGraph. Whether it&#x27;s a marketer generating ideas from trending arcs, a translator capturing tone for localization, or a product manager retrieving metadata to target segments — WCAI automates deep narrative comprehension, enabling teams to dedicate their resources, rather than spending time on manual browsing, to empowering creators and protecting their rights as WEBTOON&#x27;s global footprint expands. WCAI achieves this without any model training on creators’ works; instead, it analyzes content to interpret and structure information.

## Technical Details: Agentic Workflows Powering WEBTOON Comprehension

**WCAI** is built on a hybrid architecture that leverages **Vision-Language Models (VLMs)** and workflow-based AI agents orchestrated through **LangGraph**.

We evaluated several frameworks—including LangGraph—to find one that could meet production demands. While many frameworks support agentic patterns, our requirements went further. We needed a system that could:

- Scale across a vast amount of WEBTOON series metadata,
- Integrate **subject-matter expertise (SME)** into workflows,
- Maintain high **quality and consistency** for internal business use.

LangGraph’s **node-based architecture** offered the modularity and precision we needed. It enabled us to inject domain-specific knowledge into individual workflow stages—such as visual comprehension, narrative summarization, and translation. Additionally, LangGraph’s tight integration with LangSmith provided robust tracing, debugging, and observability—crucial for development and deployment at scale.

### Core Agentic Workflows

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbab7d9c83842382408e7c_image--90-.png)

WCAI is built around specialized agentic workflows, each designed to handle a specific aspect of WEBTOON series comprehension. Thanks to **dynamic workflow routing**, important information about a webcomic can be processed for multiple business needs simultaneously.

Here are some core workflows:

- **Character Identification: **Identifies important information about each webcomic’s characters by identifying names, roles, and representative images. By analyzing both visual and textual data, it builds structured character profiles—foundational for downstream agents.
- **Speaker Identification: **Since WEBTOON series inherit many conventions from cartoons and comics, speech bubbles are essential to narrative comprehension. This workflow analyzes speech balloons and attributes them to characters using a blend of VLMs and advanced computer vision techniques.
- **Narrative Understanding: **Generates a textual representation of the WEBTOON series, capturing key plot points, events, and emotional beats from visual scenes. It outputs structured summaries that downstream agents or users can easily understand.
- **SME application: **Built atop the foundational workflows, this agent produces business-specific insights based on user intent. For example, the marketing team can discover titles that align with campaign themes, while recommendation teams can identify highlight-worthy scenes. This layer is critical, as outputs are often tied directly to quantifiable KPIs such as Click-Through Rate (CTR). WCAI analyzes a large number of WEBTOON titles and generates high-quality keywords for each one—such as genre, narrative style, and cliffhangers—which are then exposed to help users discover titles that match their preferences.

By combining these workflows, WEBTOON Comprehension transforms unstructured visual narratives into actionable, structured data.

## Why LangGraph?

After extensive production testing, LangGraph stood out for several reasons:

- **Controllable Workflows: **While multi-agent frameworks can be useful in research settings, our production use cases—especially those involving SME collaboration—demanded **controllability, interpretability, and reliability**. Internal users also wanted transparency and the ability to steer outcomes. LangGraph’s architecture was a perfect match.
- **Production-Ready Deployment: **LangGraph is built with real-world deployment in mind, and its robustness is well validated by the LLM community. We were able to build and deploy API servers with ease and integrate them seamlessly into our systems. Reliable, efficient data generation was a top priority, and **LangSmith’s tracing capabilities** helped us identify issues like excessive token usage stemming from inefficient handling of visual tokens.

## Conclusion

**WEBTOON Entertainment** has successfully integrated agentic AI workflows into its internal operations using LangGraph. This initiative has:

- Enabled deep understanding of multi-modal WEBTOON series data for both research and business applications
- Proven that agentic workflows can support a broad range of internal teams
- Significantly reduced the manual effort required for story comprehension, boosting overall productivity. For example, the content team was previously responsible for manually reading every new title to extract keywords for user guidance. By leveraging WCAI, this process was automated—**reducing their workload by over 70% **and enabling the team to focus on more strategic and creative content promotion tasks.

We are actively developing new features and improvements for WCAI, including:

- Systematic evaluation of workflows across various business scenarios,
- Fine-grained control over human-agent interaction through architectural refinements,
- Enhanced tool-chaining to incorporate external data sources.

With WCAI and LangGraph, we’re shaping the future of scalable narrative understanding—empowering creativity across teams and unlocking the full potential of WEBTOON series. On the technical side, we are also continuously validating emerging LangChain features, such as the MCP adapter, to incorporate broader external knowledge into WEBTOON series analysis.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dca440233829941d24d635_interrupt-2026-thumbnail.webp)Company Announcements

#### Previewing Interrupt 2026: Agents at Enterprise Scale

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 9, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/previewing-interrupt-2026-agents-at-enterprise-scale)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)