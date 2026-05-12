---
title: "Browser agent bot detection is about to change"
author: "Aitor Mato"
date: "2026-02-02"
url: "https://browser-use.com/posts/bot-detection"
---

# Browser agent bot detection is about to change

**Author:** Aitor Mato
**Date:** 2026-02-02
> How we built Browser Use to stay undetectable

---

**Your cloud browser provider's "stealth mode" is detectable in under 50ms.**

Playwright with stealth plugins. "Stealth" cloud providers. Selenium forks claiming to be undetectable. None of that works—not at scale. Thousands of concurrent sessions, millions of requests. That's where everything breaks.

## The cat & mouse game is about to get harder

Antibot systems (Akamai, Cloudflare, DataDome) **can detect far more than they actually block.** False positives kill conversion rates, so they set thresholds conservatively. This is the only reason most automation still works.

**AI agents are about to flood the web.** When bot traffic reaches a tipping point, the cost of letting bots through starts exceeding the cost of occasionally blocking humans. And when that happens, they'll tighten the screws.

**The tools that work today won't work tomorrow.** JavaScript patches, stealth plugins, CDP hacks—already detectable. Antibots just haven't flipped the switch yet.

We're building for that future. A browser that's undetectable not because antibots are lenient, but because there's genuinely nothing to detect.

## So we did something different: we forked Chromium

We maintain a custom Chromium fork with dozens of patches at the C++ and OS level.

When our browser says `navigator.webdriver === false`, it's not because JavaScript lied about it. It's because **the value was never true in the first place**. Every function returns `[native code]` when stringified. Every prototype chain is intact. We didn't override anything—we changed what the browser actually does.

**Running fully headless, we bypass all major antibot systems**: Cloudflare, DataDome, Kasada, Akamai, PerimeterX, Shape Security. Not with hacks. With a browser engineered to be undetectable.

## Not everything is in the browser...

What most "stealth" solutions miss: **JavaScript fingerprinting is just one layer.**

Modern antibot systems don't just check `navigator.webdriver`. They cross-reference everything:

- **IP reputation**: Is this a datacenter IP? A known proxy? A residential address?
- **Timezone & locale**: Does your reported timezone match your IP's geolocation?
- **Hardware consistency**: Does your GPU, audio hardware, and screen resolution make sense together?
- **API availability**: Are the APIs present that should exist on your reported OS and browser version?
- **Behavioral signals**: Mouse movements, scroll patterns, typing cadence

**We cover all of it.** Our stack isn't just a browser—it's a complete solution:

- **Chromium fork** for JavaScript fingerprint consistency
- **Proxy infrastructure** with residential IPs and proper geolocation
- **Timezone and locale injection** matched to your exit IP
- **Behavioral layer** for human-like interaction patterns

Every signal, cross-referenced and consistent.

## Real-world fingerprints instead of Linux everywhere

**Our competitors run everything on Linux and hope nobody notices.** Linux desktop is less than 5% of global web traffic.

When they try to fake Windows or macOS fingerprints, they fail. Missing APIs. Wrong audio configs. Inconsistent GPU reports. The mismatch is obvious.

Real desktop traffic:
- **Windows**: ~60%
- **macOS**: ~35%
- **Linux**: ~5%

At scale, you simply can't use Linux-only fingerprints.

## In-house CAPTCHA solving

We built our own CAPTCHA solving with in-house models. No third-party APIs. No external dependencies.

**Currently supported:** Cloudflare Turnstile, PerimeterX Click & Hold, reCAPTCHA. More coming soon.

Because it's all in-house, **CAPTCHA solving is free for all Browser Use customers**. No per-solve fees. No usage limits.

**Good fingerprinting means fewer CAPTCHAs in the first place.** When your browser looks legitimate, websites don't challenge it as often.

My prediction? CAPTCHAs will fade away. Modern solvers outperform humans in speed and accuracy, and they harm conversion rates for legitimate visitors.
