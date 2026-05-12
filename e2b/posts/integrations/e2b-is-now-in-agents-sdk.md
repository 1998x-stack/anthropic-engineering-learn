---
title: "E2B is now supported in the OpenAI Agents SDK"
author: "Matt Brockman"
date: "2026-04-15"
url: "https://e2b.dev/blog/e2b-is-now-in-agents-sdk"
category: "integrations"
site: "e2b"
---

We're happy to announce that E2B is a sandbox provider in the new [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents). 

With this release, agents built with the OpenAI Agents SDK will get their own sandboxes featuring a custom environment with resource isolation, security boundaries, and persistence, requiring no infrastructure setup. Your agents will be able to:

- Edit files and run shell commands in isolated environments
- Maintain temporary workspace state across steps
- Generate frontend output with live preview URLs
- Produce artifacts you can review before publishing
- Run multiple sandboxes in parallel for concurrent workloads

## **Integration takes just a few lines of code**

You can set up computer use with just a few lines of code. You just need to define your tools, the agent to use them, and something to get started.

## **See it in action**

In the demo below, we walk through the full workflow of creating a landing page:

- **Set up a sandbox session** with the E2B SDK and define a builder agent with file-editing capabilities.
- **Generate a landing page from scratch**: the agent writes HTML/CSS, deploys into the sandbox, and serves it at a preview URL.
- **Iterate with diffs**: instead of rewriting everything, the agent applies patches for faster turnaround.
- **Compare variants side by side**: each variant lives at its own URL, making visual comparison straightforward.
- **Parallelize**: spin up multiple sandboxes simultaneously, each running an independent agent, to generate several variants at once.

The result: multiple landing page variants, each pre-viewable at its own URL, generated in parallel with minimal code.

‍

## ‍
**Sample applications and use cases for the OpenAI Agent SDK**

Browse examples in the[ E2B Cookbook](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples).

- Computer use
- Webpage building
- Parallelize data science tasks for grid searches and more
- Parallelize code review

## **Get started**

You'll need an [E2B](/sign-up) account and an[ OpenAI API](https://openai.com/api/) account. Check out the repos:

- [E2B Infrastructure](https://github.com/e2b-dev/infra)
- [E2B SDK](https://github.com/e2b-dev/E2B)
- [OpenAI Agents Python SDK](https://github.com/openai/openai-agents-python)
- [OpenAI release post](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)

Note: Sandboxing is currently supported in the Python Agents SDK. Stay tuned for TypeScript support.