---
title: "We Stealth Benchmarked Every Major Cloud Browser Provider"
author: "Aitor Mato"
date: "2026-03-21"
url: "https://browser-use.com/posts/stealth-benchmark"
---

# We Stealth Benchmarked Every Major Cloud Browser Provider

**Author:** Aitor Mato
**Date:** 2026-03-21
> We built a stealth benchmark from real production data and tested every major cloud browser.

---

In our first stealth post, we explained why current "stealth" solutions are fundamentally broken and how we forked Chromium to build the best browser infra.

**Bold claim. This post is the proof.**

## Why stealth needs its own benchmark

The bottleneck for agents is not their intelligence. On most websites users care about, agents get blocked by a CAPTCHA or an antibot challenge.

We collected 300,000 security check events from production traffic. The data made it clear: **agent intelligence and browser stealth are orthogonal**. You need to measure them separately.

## Dataset distribution

From those 300,000 security checks, we extracted the 71 most common and well-known websites where agents were getting blocked, and categorized them by antibot vendor:

| Vendor | Sites |
| --- | --- |
| Cloudflare | 23 |
| PerimeterX | 18 |
| Datadome | 13 |
| Akamai | 8 |
| reCaptcha | 6 |
| Others (incl. Kasada, Shape) | 3 |
| Total | 71 |

## Judge criteria

- **Simple tasks**: 3 steps per site (search, visit a page, read a link). No auth. If it fails, it's because the browser got blocked.
- **LLM judge** (`gemini-2.5-flash`): only evaluates whether the agent was blocked, not whether it completed the task correctly.
- **Page load failures count as blocks**, since some antibots prevent the page from loading entirely.

## Control experiments

To confirm the benchmark measures stealth, we tested two baseline browsers on a datacenter IP (GitHub Actions runner):

- **Headless Chromium**: scored **2%**. The most suspicious browser possible, fewer than 2 tasks passed per run.
- **Headful Chromium**: scored **50%**. Same machine, just rendering a visible window. Headless detection is one of the easiest signals for antibots.

This validates that the task set consists of high-security sites and that score improvements reflect real stealth capability.

## Results

We ran the benchmark across every major cloud browser provider. Each provider was evaluated multiple times with the same agent and model (`bu-2-0`).

The differences are large and consistent. **Browser Use Cloud leads at 81%**, followed by Anchor at 77% and Onkernel at 67%. The bottom half (Steel 47%, Browserbase 42%, Hyperbrowser 40%) is far behind.

The vendor breakdown reveals where each provider is strong or weak. Browser Use Cloud's highest bypass rates are against Cloudflare (93%), Akamai (85%), and PerimeterX (81%).

## BrowserBench

We also ran BrowserBench from Halluminate, a third-party benchmark with 296 tasks across antibot-protected sites. Their task set is not fully focused on high-security websites, so overall scores are higher and differences between providers are smaller.

Browser Use Cloud achieved the highest success rate of all providers tested:

- **Browser Use Cloud**: **84.8%**
- **Hyperbrowser**: **76.4%**
- **Anchor**: **76.0%**
- **Steel**: **73.3%**
- **Browserbase**: **70.3%**

## Should we trust benchmarks?

Not blindly. Proxy quality varies by the hour, sites update their configs, CAPTCHA difficulty fluctuates. But **benchmarks show who is actually putting in the work**. When one provider consistently leads across multiple independent benchmarks, that's not noise.

71 sites is a start, not an endpoint. We know vendors and CAPTCHA providers are missing. We'll keep expanding and re-running as the landscape changes.

## "Stealth" in the industry

Let's cut the bullshit. Most cloud browser providers slap a residential proxy and a third-party CAPTCHA solver extension on a stock Chromium, put **"Advanced Stealth"** on the landing page, and call it a day. 🤡

Most major competitors report the same fingerprint: **headful Linux Chromium.** The movie ends as soon as major antibots stop being lenient and start blocking these obvious leaks.

TL;DR: if your provider's user-agent starts with `Mozilla/5.0 (X11; Linux x86_64)`, run.

What we do instead:

- **Fully headless on latest major Chromium version**. The only provider that can pull it off
- **macOS, Windows & Linux** with tens of thousands of real fingerprints
- **In-house CAPTCHA solvers** and monitoring tools
- **Own Chromium fork**, maintained and patched non-stop

Stealth is not a feature for us. It's the **top priority**.

## The never-ending cat & mouse game

A solution that works today might break tomorrow. Antibots evolve constantly and no one is immune. We don't pretend to sell a 100% success rate, that doesn't exist. Things break, but nobody works harder than us to keep up.

When your business relies on stealth, the most important thing when choosing a provider is **trust in their expertise and work ethic**. At Browser Use, we lead, and we prove it.
