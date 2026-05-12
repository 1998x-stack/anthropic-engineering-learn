---
title: "On the Incoming Slopocalypse and the Death(?) of Open Source"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/on-the-incoming-slopocalypse-and-the-death-of-open-source"
category: "general"
---

Content



- [ Open-Source Pillars  ](#open-source-pillars)
- [ 1. General open-source usability/quality  ](#1-general-open-source-usabilityquality)
- [ 2. Knowledge Sharing  ](#2-knowledge-sharing)
- [ 3. Community Interaction  ](#3-community-interaction)
- [ 4. Personal Skill Growth  ](#4-personal-skill-growth)
- [ Where to go from here?  ](#where-to-go-from-here)



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



   1



 I’ve been helping maintain LlamaIndex Open Source Software (OSS) across several repositories for nearly 3 years now. Over that time, I’ve seen codebases change, communities evolve, and many hype cycles come and go. From this position, I’ve noticed a new trend downwards for open-source code that I’ve been grappling with how to deal with: coding agents have lowered the bar to entry so much that contributing to open-source is no longer an exclusive club.



 With this change, it’s left me wondering what makes open-source valuable, and if it can even maintain relevance in the face of coding agent slop. I’ve tried to distil the spirit of open-source into 4 main pillars below, and detailing the impact by coding agents (both positively and negatively).



##  Open-Source Pillars



###  1. General open-source usability/quality



 Creating a general useful tool, library, framework, etc. is one of the main things that makes OSS valuable. A lot of the most famous open-source software examples are doing things that solve hard problems or would be otherwise very annoying to create from scratch (numpy with efficient math and vectors, PyTorch for back-propagation and deep-learning, etc.). Maintainers work to keep these packages efficient, bug free, and usable.



 At the same time, the fact that open-source software is not built in isolation further pushes it to be generally useful to a community of users.



 Coding agents impact this pillar of open-source greatly. [Simple projects](https://www.npmjs.com/package/upper-case) are largely invalidated by the ability of a coding agent to write simple packages from scratch. While this puts the burden of maintenance onto the individual, the decreasing costs and increasing performance of LLMs and their ability to code makes this a moot point.



 Complex packages will continue to thrive (likely with some help from LLMs!), but whether or not a project survives likely depends on its breadth, usefulness, and how annoying or difficult it would be to maintain on your own. This isn’t much different from pre-LLM era’s, but just shifts further into that direction.



###  2. Knowledge Sharing



 Another stream of open-source projects exist purely as knowledge transfer examples. Showing how to build a certain deep-learning architecture, or how to solve a particularly hard algorithm, these projects can be largely seen as educational.



 However, with the rise of coding agents, these are less and less valuable since LLMs end up trained on this data anyways, and individuals have less motivation to seek these types of projects out or create them. With LLMs and agents serving as frontends for knowledge, we will likely see some decrease in activity for these types of projects.



###  3. Community Interaction



 At LlamaIndex, this is my favourite part about OSS. A user opens a PR solving some long-forgotten bug, or adding some useful new feature or integration. You iterate with them to get it merged, maybe learn a bit more about what they are building, and you grow a community.



 Today, I see a noticeable uptick in LLM-generated PRs. Users open sometimes gigantic code changes to attempt to solve some existing issue or add some random integration. Sometimes you can even tell when you are iterating with a bot as you leave PR comments.



 These types of contributions often need a lot of work — LLMs lack a lot of internal learned knowledge for the specific project they are contributing to. Common gotcha’s, forgetting to run linting/formatting, or formatting and structure that does not match the rest of the project. This in addition to the pure size of PRs that these agents can push out adds up to a frustrating experience.



###  4. Personal Skill Growth



 A big motivation for contributing to open-source is developing your own personal skills. Diving into an unknown codebase, solving a bug or learning a new architecture as you work on a contribution, there is a lot of problem solving that goes into opening a PR (especially your first time!).



 However, LLMs again have lowered the barrier here. Why learn rust to fix a bug when an LLM can do it for you. While efficiency is nice, there is some core value being lost here in a developer’s ability to problem solve. A [recent study from Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills) shows that offloading this effort to an LLM does indeed cause some amount of skill atrophy. The only thing stopping you from doing this is personal willpower (something that is all too easy to give into).



##  Where to go from here?



 I’ve observed coding agents and LLMs impact all the above areas in open-source. And as someone who works for a company developing these tools, I feel some responsibility for these changes.



 However, this doesn’t mean open-source is dead or less valuable. Instead, I think open-source needs to adapt to these changing times.



 While the above sections may have came off as ranting or complaining, there are some new open-source pillars that I’ve been thinking about for the age of coding agents:


-  Hackable Open-Source Reference — rather than providing a library that integrates with everything under the sun, provide an LLM friendly reference implementation. Users can fork this and modify as needed (either themselves or with their coding agent of choice).
  -  Community through Knowledge — LlamaIndex has a wealth of integrations that right now, we end up testing and maintaining ourselves. However, it might be more valuable to build community purely through linking to interesting extensions, modifications, and forks of your project for LLMs and users to explore. Meanwhile the core abstractions or implementations can be iterated on with the communities feedback.
  -  Make your codebase agent friendly — accept that LLM agents will continue to open auto-generated PRs, but do your best to counter this with clearly documented development patterns and requirements. You want to PRs on your repo to be an efficient and pleasant process.



 Going forward, I want to push our OSS projects to encapsulate these new pillars. We’ve made some progress in this respect, like updating and simplifying our [CONTRIBUTING.md](https://github.com/run-llama/llama_index/discussions/20577) file. There’s more work to be done here of course, like curating a sample `AGENTS.md`  and documenting our code with docstrings a bit better.



 Overall, I see coding agent usage in open-source projects to continue to grow. Even today, organizations like Anthropic are [shipping entire products built by coding agents](https://x.com/bcherny/status/2010813886052581538?s=20). The lure of a coding agent is hard to resist, and so as open source maintainers, we need to work harder to set our projects up for success.



 Part of this means also deciding when a coding agent shouldn’t be used. When talking about maintaining core implementations above, I fully believe that this is where human taste comes in, and should be at least designed by an actual person and iterated on with community feedback. This also include PR reviews, as tempting as it can be to automate.



 Contributing to open-source no longer some exclusive club, but is changing, to become more of a vehicle and enablement tool for communities, agents, and individuals. Open-source is not dead, its just going to look a little different.







##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)