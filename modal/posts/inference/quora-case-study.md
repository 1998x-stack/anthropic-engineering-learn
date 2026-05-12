---
title: "How Quora uses Modal to run thousands of Python sandboxes simultaneously"
author: "Unknown"
date: "2025-06-30"
url: "https://modal.com/blog/quora-case-study"
category: "inference"
site: "modal"
---

# How Quora uses Modal to run thousands of Python sandboxes simultaneously

  [Quora](https://www.quora.com/) is a Q&amp;A platform where users can ask, answer, and peruse questions on a variety of topics. With 400 million monthly unique visitors, it’s an invaluable contributor to the world’s knowledge-sharing. Quora uses [Modal Sandboxes](/docs/guide/sandboxes) to securely execute LLM-generated code in Poe, their AI chatbot platform. The team shipped months earlier using Modal rather than building in-house. They’re also saving an ongoing 2 engineers’ worth of infrastructure maintenance time!

## Hello, Poe

In 2023, Quora launched [Poe](https://poe.com/), an AI chatbot platform where anyone can deploy a public chatbot. With millions of monthly active users, Poe is the default destination for many AI builders to experiment with different models. Quora has since raised $75M to keep expanding Poe.

## A code interpreter for Poe

Many of the LLM bots in Poe can generate code, and users expected to run that code in Poe rather than copy-pasting it to their editors. The Quora team needed a way to safely execute code in Poe in a completely isolated way, keeping that code separate from both the main Quora infrastructure and any other user’s session.

![](https://modal-cdn.com/blog/images/poe.gif)  In-chat Python execution in a Poe chatbot

There were three key requirements for this feature.

- Security, since LLM-generated code can’t be trusted by default.
 - Low latency, since chatbot responses need to be fast in order to feel conversational.
 - Reliability, since the product has millions of users and is expected to be polished.

Low latency, reliable systems are effortful to construct. While a basic sandbox prototype would have been easy to build, the Quora team knew that orchestrating a fast-scaling system for millions of users would have taken months. And that was just considering the core code execution primitive. If they wanted security features like outbound networking restrictions or debugging features like container-level observability, that would have taken even longer.

Modal’s Sandbox product was fully featured and scalable right out of the box. Quora was already familiar with Modal and, due to Modal’s superior reliability over alternatives, had it recommended as the default deployment solution for users publishing their own Poe bots. This gave Quora the confidence to expand their usage into Modal Sandboxes.

 “There would be a lot of edge cases and unknowns if we built code sandboxes ourselves: dealing with setting separate environments, minimizing risk areas—this is not just for set-up but needs continuous consideration. We offloaded this to Modal and are actively saving 2 engineers' worth of ongoing engineering time.” — Hwan Seung Yeo, Director of Engineering

## A Modal Function by any other name

[Modal Sandboxes](/docs/guide/sandboxes) are really just our core primitive—Modal Functions—minus our client running inside of them. This means that Quora got a battle-tested and continuously improving product right out of the box.

✅ Modal’s custom container stack, which we have invested years into making robust and secure, is already built on gVisor for enterprise-grade container isolation.

✅ Fast scalability is built in. Quora stress-tested Sandbox creation throughput to 1000 Sandboxes per second with no issue, allowing them to support thousands of users who might be generating code at any given point in time.

✅ Powerful [networking primitives](/docs/guide/sandbox-networking) like Tunnels and IP allowlisting come for free, too, allowing Quora to have full customizability and control over Sandbox communications.

This is just the beginning. The Poe team is working on an under-the-wraps new product that will also leverage Modal Sandboxes for code execution. We’re looking forward to sharing more once they launch!

## Build fast like Quora

Want to ship LLM coding features in days rather than months? Get started today with [Modal Sandboxes](/docs/guide/sandboxes).

- Install Modal: `pip install modal`
 - Create an account: `python -m modal setup`
 - Run: