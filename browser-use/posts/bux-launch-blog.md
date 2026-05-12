---
title: "BUX: Your 24/7 Remote Agent with Browser Harness"
author: "Johannes Dittrich"
date: "2026-04-25"
url: "https://browser-use.com/posts/bux-launch-blog"
---

# BUX: Your 24/7 Remote Agent with Browser Harness

**Author:** Johannes Dittrich
**Date:** 2026-04-25
> Browser Use Box (BUX) is a 24/7 remote VM with Claude Code and Browser Harness pre-installed, controlled from Telegram, the web, or SSH.

---

## Introducing BUX

Today we're shipping Browser Use Box (BUX). A 24/7 remote VM with Claude Code and [Browser Harness](https://browser-use.com/posts/bitter-lesson-agent-harnesses) pre-installed, controlled from Telegram, the web, or SSH.

## How we got here

Everyone at Browser Use is obsessed with the combination of Claude Code and Browser Harness. However, we wanted the experience to be as seamless as possible.

Now with BUX you can access this combination from your phone 24/7.

## What we use it for

It can complete tasks in complicated dashboards like Microsoft Azure and Google Workspace that browser agents historically struggled with.

From the gym, in an Uber, walking somewhere, we throw any task at it:

> "deploy PR #235 to staging and test the new flow"
>
> "book the earliest flight Zurich to SF next Wednesday"
>
> "take a picture of our granola, order this on Amazon"

We are yet to find a work-related or everyday-web task that BUX can't do.

## How it works

Spin-up takes 30–60 seconds from a pre-baked AMI with Claude Code and Browser Harness pre-installed. Login to Claude, set up your Telegram, and you've got a 24/7 personal agent.

The VM runs under a locked-down IAM role with zero AWS permissions. It can't touch your infra or ours.

Telegram talks to one resumed Claude Code session, so context persists. Browser sessions rotate every 240 minutes.

On [cloud.browser-use.com/bux](https://cloud.browser-use.com/bux) you can access your VM directly through a browser terminal. And SSH in locally. The architecture is open source. See the [bux repo](https://github.com/browser-use/bux) if you're curious, or you'd like to host it yourself.

## Setup (under 5 min)

1. Go to [cloud.browser-use.com/bux](https://cloud.browser-use.com/bux) and start your VM.
2. Log in to Claude Code in the web terminal.
3. Create a Telegram bot via @BotFather and paste the token. It stays in your box.

## Giving it access

BUX is only as useful as the accounts it can reach. Use [Browser Use Profiles](https://cloud.browser-use.com/profiles) to sync your local Chrome cookies or build new ones by hand.

When the agent hits a login wall, it sends you a live URL from the remote browser. You sign in, it picks up where it left off, and saves the cookies for next time.

## Try it

Head to [cloud.browser-use.com/bux](https://cloud.browser-use.com/bux). All you need to get started is a Browser Use account and Claude Code.
