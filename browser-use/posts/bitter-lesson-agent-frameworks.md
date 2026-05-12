---
title: "The Bitter Lesson of Agent Frameworks"
author: "Gregor Zunic"
date: "2026-01-16"
url: "https://browser-use.com/posts/bitter-lesson-agent-frameworks"
---

# The Bitter Lesson of Agent Frameworks

**Author:** Gregor Zunic
**Date:** 2026-01-16
> All the value is in the RL'd model, not your 10,000 lines of abstractions.

---

An agent is just a for-loop of messages. The only state an agent should have is: keep going until the model stops calling tools. You don't need an agent framework. You don't need anything else. It's just a for-loop of tool calls.

Our first Browser Use agents had thousands of lines of abstractions. They worked - until we tried to change anything. Every experiment fought the framework. The agents weren't failing because the model was dumb. They were failing because we were.

## Why abstractions break learning

Here's the thing about abstractions: they freeze assumptions about how intelligence should work. RL breaks those assumptions.

Every time you add a "smart" wrapper around model behavior - planning modules, verification layers, output parsers - you're encoding what you think the model should do. But the model was trained on millions of examples. It has seen more patterns than you can anticipate. Your abstractions become constraints that prevent the model from using what it learned.

The Bitter Lesson from ML research is clear: general methods that leverage computation beat hand-crafted human knowledge every time. Agent frameworks are just the latest instance of this mistake.

## 99% of the work is in the model

Here's the thing: 99% of the work is done within the model itself. We don't need some highly abstract framework around it.

Claude Code these days can just write AppleScript directly. It needs information from some obscure Spotify player? It doesn't need a Spotify computer-use tool. It just writes AppleScript on macOS. It has perfect context. It's well-trained on this.

You don't anticipate every use case. The model already knows.

## The key insight

This led to something important:

**Agent frameworks fail not because models are weak, but because their action spaces are incomplete.**

Instead of defining every possible action up front, start from the opposite assumption: the model can do almost anything. Then restrict.

**Give the LLM as much freedom as possible, then vibe-restrict based on evals.**

## Why we threw everything away

The first version of Browser Use was a classic agent framework: a model wrapped in a complex message manager with lots of abstractions meant to control behavior. It worked, but it was painful to extend. Every experiment fought the framework.

So we stepped back and asked a more fundamental question:

**What are LLMs actually trained to be extremely good at - and what will remain true as models get better?**

We threw the entire agent away and started from scratch. To understand what "minimal" could really mean, we reverse-engineered the Claude Code and Gemini CLI.

**Don't over-specify intelligence - let the model reason.**

## BU Agent: the application

We built this philosophy into BU Agent - a minimal agent framework that powers Browser Use.

Rather than exposing a small set of brittle "click / type / scroll" primitives, BU Agent gives the model access to raw browser control surfaces.

At the core: the ability to emit pure Chrome DevTools Protocol (CDP) instructions. In practice, the model can do almost anything in the browser.

On top of that: browser extension APIs. They make certain tasks trivial that are awkward or impossible with CDP alone - like accessing the active window or working with permissioned browser state.

CDP and extension APIs each have blind spots. But together they form a nearly complete action space.

When the model has that freedom, something important happens. If one approach fails, it routes around it. If a tool breaks, it finds another path.

**As long as in principle everything is possible, LLMs are extremely good at fixing themselves on the fly.**

## The inversion

So BU Agent is built from a simple inversion:

**Start with maximal capability, then restrict.**

Give the model the freedom to do anything a human could do in a browser. Only then layer on safety, structure, and constraints.

That's what lets the system scale with better models instead of fighting them.

## Ephemeral messages

One interesting thing we need for browser agents: if you request the browser state, it's massive. DOM snapshots, screenshots, element indices - easily 50KB+ per request.

Without ephemeral messages, here's what happens: after 10 browser interactions, you have 500KB of state in context. After 20, you're at 1MB. The model starts losing coherence.

So I introduced ephemeral messages.

```python
@tool("Get browser state", ephemeral=3)  # Keep last 3 only
async def get_state() -> str:
    return massive_dom_and_screenshot
```

If you make a tool call X times (whatever you define), it removes all the previous outputs. Destroys cache a little bit. But it's a very good trade off - LLMs can't really handle massive contexts anyway.

## The for-loop doesn't work (until you fix it)

The naive approach - stop when the model returns no tool calls - doesn't work well. Agents prematurely finish. Especially if they're missing some context.

The best way to fix it is the done tool.

```python
@tool('Signal that the current task is complete.')
async def done(message: str) -> str:
    raise TaskComplete(message)
```

When the model outputs a done tool call, it terminates the agent. This forces explicit completion instead of implicit "I guess we're done?"

We have two modes:
- **CLI mode:** Stop when LLM returns no tool calls (quick interactions)
- **Autonomous mode:** Only stop on explicit done() call

## The bitter truth

Every abstraction is a liability. Every "helper" is a failure point.

The models got good. Really good. They were RL'd on computer use, coding, browsing. They don't need your guardrails. They need:
- A complete action space
- A for-loop
- An explicit exit (done tool)
- Context management

**The bitter lesson: The less you build, the more it works.**
