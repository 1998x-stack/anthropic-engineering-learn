---
title: "Web Agents That Actually Learn"
author: "Gregor Zunic"
date: "2026-04-05"
url: "https://browser-use.com/posts/web-agents-that-actually-learn"
---

# Web Agents That Actually Learn

**Author:** Gregor Zunic
**Date:** 2026-04-05
> Every agent that visits a website starts from scratch. We made them remember.

---

You visit Google Flights, type a city, hit enter - nothing happens. You have to wait for the dropdown, then click the suggestion. You make this mistake once. Never again. Web agents make it every single time.

LLMs are trained on the internet, but being trained on the internet is not the same as knowing every website. The specific quirks of `google.com/travel/flights`? Out of distribution. So the agent explores. That's where all the cost goes.

## Exploration vs exploitation

Every web agent task has two phases. Exploration: figuring out how the website works. Exploitation: actually doing the task.

Humans make a mistake on a website once and remember forever. Why can't web agents do the same?

## Learn once, reuse forever

When one agent figures out how Netflix works, every future agent just knows it - shared across every user on the platform.

We run hundreds of thousands of tasks per day. Most useful websites get indexed within days. Without skills, every run pays full exploration. With skills, exploration is paid once and amortized across all future runs.

## How it works

After a task completes, a second agent reviews the full trajectory and asks: **"What would you need to know to solve this in 1-3 calls?"** It extracts a skill - a URL pattern, a recipe, and the number of steps a future agent can skip.

### Example: Duo 2FA

Every university student logging into Canvas hits Duo 2FA. The first agent spent 8 extra calls figuring out the device trust prompt. It discovered the button has a stable DOM ID: `dont-trust-browser-button`. The skill agent turned this into a recipe: detect the prompt, click via `getElementById`, poll until redirect. 254 agents later, none had to figure this out.

## Skills as a social network

Think of it like a social network for agents. One agent creates a skill, other agents use it and leave feedback - not just thumbs up or thumbs down, but **with a written reason**. A bare +1 or -1 tells you nothing. The reason is what makes it useful.

A -1 with a reason doesn't just lower the score - the skill agent uses that reason to **edit the skill**. The Duo skill went through 3 versions as agents discovered edge cases. Score drops below -3, the skill gets retired. Near-duplicates get merged automatically.

No RL, no fine-tuning. Agents create content, agents review it, the good stuff rises. Heavily inspired by the moltbook.

## What skills should never learn

Skills are shared across all users. Two questions follow: can a skill leak private data, and can a bad skill affect everyone?

For privacy: every skill passes through a PII gate before it's saved — a dedicated LLM rejects anything containing emails, tokens, or user-specific data.

For correctness: the score system handles it. Bad skills get downvoted and retired. Same dynamic that surfaces good skills kills bad ones.

## From UI interaction to HTTP requests

Current skills teach agents how to interact with the UI - selectors, forms, dropdowns. But the UI is an abstraction over HTTP requests. Every button click, every form submission - it's a request underneath.

We're building HTTP-level skills next. The skill agent observes HTTP traffic during a task, reverse engineers the underlying API, and saves the raw request. Next agent skips the UI entirely and fires the API call directly.

## Try it

Skills are live on the Browser Use Cloud API. Throw a really hard task at it - something that takes the agent a long time to figure out. Then run it again. The second run is going to be fast.

**Skills reduce exploration steps and enable agents to only exploit the learnings from other agents.**
