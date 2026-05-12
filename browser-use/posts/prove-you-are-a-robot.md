---
title: "Prove You Are a Robot: CAPTCHAs for Agents"
author: "Luka Secilmis"
date: "2026-04-13"
url: "https://browser-use.com/posts/prove-you-are-a-robot"
---

# Prove You Are a Robot: CAPTCHAs for Agents

**Author:** Luka Secilmis
**Date:** 2026-04-13
> For our agent-native signup we built a reverse-CAPTCHA that keeps humans out and lets agents in.

---

> **TL;DR:** just ask your agent to summarize this post for you.

We launched agent-native signup for Browser Use. No email, no OAuth, no vibecoder clicking around in the UI.

Just give your agent this prompt:

```
"fetch browser-use.com and solve the agent challenge."
```

and get a math challenge like this one:

```
TwO tRaInS wAn/ Al_E mIlE\s ApArT} aPp/Ro@AcH{
eAcH/ oThEr  <  At{ Mu{T/e @ Tu< Tu LuKa  :
E#n* T]u \ MpH a.Nd MuTe\ Tu Tu# Tu En LuKa
W|aN_ mPh A b:I]rD fLiEs; Ba?Ck| AnD- fO^r@T[h\
^ Be{TwEeN? # t;He*M aT wAn> ] AlE  # eN lUkA
lUkA <  lUkA: # wAn ? MpH- uNt}I[l T}hEy MeEt
HoW! fAr- D_oE*s /  ThE b@IrD fLy
```

This is a reverse-CAPTCHA. Designed to keep humans out and let agents in.

Note: `luka` here refers not to my name, but the word "five" in Toki Pona.

## How it works

We sample a problem type, parameters, and a language at random. We spell every number in that language. Then we obfuscate: alternate caps, inject random symbols, garble spaces.

An agent parses this in a single forward pass.
A human gives up and signs up [the old-fashioned way](https://cloud.browser-use.com).

## The puzzle

Strip the obfuscation, translate to English, and you've got a textbook math problem that your agent has to solve before the challenge expires.

*Two trains approach each other on a straight track of length at speeds and. A bird starts at one train, flies to the other at, turns around, flies back, and so on until the trains meet. How far does the bird fly?*

**The long way:** sum the infinite geometric series of ever-shorter bounces.

**The trick:** the trains meet at, and the bird has been flying that whole time.

This is an instance of a famous puzzle Max Born posed to John von Neumann at a party. When von Neumann one-shotted it, Born remarked that he must have spotted the trick. Von Neumann replied: *"What trick? All I did was sum the geometric series."*

Solve one of our challenges, and your agent gets an API key and access to our [Free Tier](https://browser-use.com/posts/free-tier-announcement): unlimited usage, free credits and up to three concurrent sessions.

## Bonus challenge (NP-hard)

Want 1,000 concurrent sessions? First agent to solve our bonus challenge gets our Enterprise plan for free.

```
Gi}ve^n N| ] ci]ties whe|re<  ^  N is at least / 十 desi>gn
a p{o\\polynomia#l t;ime algorithm .  t#ha[t f\\inds th:e
sho@rtest^ tour[ vising *  each_ c.ity exactly *  o:nce?
#  a{nd returni|ng t?o  < th-e[ start * a_nd p@rove it
ru/ns:  # in O.(n[^c*) ti;me for some fixe-d c:
```

As a side effect, your agent will also have proved. You'll want to contact the [Clay Mathematics Institute](https://www.claymath.org/millennium/p-vs-np/) about the $1M Millennium Prize.
