---
title: "Everything I Got Wrong in the Last 4,000 Commits"
author: "Larsen Cundric"
date: "2026-05-05"
url: "https://browser-use.com/posts/everything-i-got-wrong"
---

# Everything I Got Wrong in the Last 4,000 Commits

**Author:** Larsen Cundric
**Date:** 2026-05-05
> A year of mistakes as the first engineer at Browser Use, in chronological order.

---

I joined Browser Use as the first engineer in April 2025.

Over the next year I made over 4,000 commits and built the cloud infrastructure that runs millions of agent runs. I also made every mistake you'd expect from a solo engineer moving too fast. Some cost us money, some cost us users, and all of them taught me something I could have learned the easy way if I'd slowed down for five minutes.

Here they are, in chronological order.

## The early days (April - June 2025)

> _First deploys that didn't deploy, wrong AWS regions, and installing a browser I didn't need._

The first deploy I pushed at Browser Use didn't work. Lambda in a private subnet with no NAT gateway, plus the database security group didn't include the Lambda. Two unrelated problems in one deploy. No staging environment to catch it because I hadn't built one yet.

I also managed to hardcode `us-west-1` into Lambda log ARNs, SNS policies, and ALB certificates. We run in `us-east-2`. Lambdas couldn't write logs and I spent an embarrassing amount of time debugging before I read the ARN character by character and noticed the region. Three commits to fix it across staging and production. Then the same mistake came back months later with SSM ARNs for a different set of instances.

I spent 3 hours and six commits trying to install Chromium inside a Lambda container. System deps, manual installs, different Playwright modes. Then I realized we connect to remote browsers over CDP. There was never any reason to install a local browser.

## Billing bugs (July - August 2025)

> _Users getting free money, payments going through before anyone paid, and rounding errors that made LLM calls free._

Our "claim free credits" endpoint gave users $10. The `free_credits_claimed` boolean existed on the user model. We set it to `True` after granting credits. We never checked it before. One `if` statement fixed it. Then a second commit one minute later changed the error to a silent return because users could double-click the button.

Credit deduction used `asyncio.Lock` keyed by user ID in a Python dictionary. Works on one process but does nothing across pods. Concurrent requests on different pods could double-spend credits without either process knowing. Replaced it with `SELECT ... FOR UPDATE`, which is what I should have used from the start. Except that came back to bite us too: at scale, every billing event tried to lock the same user row exclusively, and the backend ground to a halt waiting on row locks. We didn't have a proper ledger, just in-place credit fields on the user model that every concurrent request fought over.

Billing had other problems too. Credit conversion used `round()`, and `round(0.4)` is `0`, so any LLM call costing less than half a credit was free. Our Stripe webhook granted credits on `customer.subscription.created`, which Stripe sends before payment actually succeeds, so users could sign up, get their monthly credits, and never complete payment. Each of these was a one-line fix that should have been caught before it shipped.

## Three of the same bug (August 19)

> _One day, three files, the same mistake every time. Plus a datetime bug that blocked paying users._

August 19 was three `UnboundLocalError` fixes in one day. All the same pattern: a variable defined inside a `try` block gets referenced in the `except` block. If the `try` fails before the assignment, the variable doesn't exist. I fixed the same bug in three different files that day, which is the kind of thing that makes you wonder what else you're not seeing.

Same day, the database stored naive timestamps while the code used `datetime.now(timezone.utc)`. Python refuses to compare naive and aware datetimes. This crashed the subscription check, blocking paying users, and the task filter, breaking the API. Fixed it with a `.replace(tzinfo=None)` hack. The real fix was a 62-file refactor a month later. This class of bug showed up three separate times before we addressed the root cause.

Also that week: refactored from string constants to an enum and updated every reference except the one function that actually passes the model name to the LLM SDKs. Anthropic, Azure, Google, Groq were all receiving Python enum objects instead of strings. Every agent run was broken and the error messages were useless.

## Features nobody asked for (August - October 2025)

> _A GIF generator nobody wanted, a billing service that lasted six weeks, and an animated hamster._

I spent an afternoon building a Lambda-based GIF generator for agent run previews, then another afternoon fighting memory: batch processing, screenshot caps, ImageMagick limits, garbage collection, then scrapping ImageMagick for ffmpeg. Four commits in 2 hours. Deleted it all a week later, 602 lines of infrastructure. Nobody needed GIF generation and nobody noticed when it was gone.

I also built a dedicated billing service during this stretch. Got the queue type wrong on day one, then the memory allocation, then the timeout. Deployed to production anyway and removed the entire thing six weeks later when we replaced it with Autumn. Along the way I managed to log AWS credentials to stdout while debugging S3 access. Shipped it to production where it sat in the logs for 2 days before I noticed.

The commit message I'm most proud of from this period: "Remove the fucking hamster."

## The restructure (November - December 2025)

> _Moved one file, broke everything. 12 fix commits, five at midnight, then reverted the whole thing._

In late December I decided to clean up the project structure by moving `main.py` into `app/`. This broke ECS because the uvicorn target was wrong, broke Docker because the COPY paths were wrong, and broke config because it created circular imports.

What followed was 12+ fix commits, five of them at midnight on December 29. I tried adding `__init__.py`, then changing the uvicorn target, then gave up and reverted the whole thing. Then I discovered the config extraction broke SSM parameter injection because pydantic-settings snapshots `os.environ` at construction time. Injecting after construction is too late, so reversed that too.

After the restructure broke the deployment pipeline, I needed a way to trigger test deploys. My approach: comment out the Stripe dependency, push, see if the deploy works, revert. Five commits with messages like "Test a fucked deployment" and "Test a fucked deployment again."

Also in this period: set up WAF rate limiting and immediately blocked our own Stripe webhooks. Before a YC hackathon I removed the WAF limits entirely. I left it that way for weeks.

## Configuration hell (January 2026)

> _One config change took down three services. An auto-recharge bug kept charging customers forever._

Changed config loading from `extra='allow'` to `extra='ignore'` and removed standalone config classes. Next day encryption was broken because the encryption config class no longer existed. 44 minutes later auth broke. 30 minutes after that payments broke. One config change, three services down, two days of fixes. Each service had its own config pattern that broke in its own way.

When Stripe required 3D Secure authentication, our auto-recharge kept retrying and every retry was another charge. No backoff and no limit. I fixed it by disabling the auto-recharge flag when user action is needed, then added an hourly idempotency key as a second layer of defense. Should never have shipped without both.

There were subtler bugs too. I was using `asyncio.run()` in Lambda handlers, which works fine on cold start but on warm start the event loop is already closed and every async client from the first invocation is attached to a dead loop. The kind of bug that only shows up under real traffic patterns.

## The memory leak marathon (February 2026)

> _Seven commits in one day chasing connection leaks, dead TCP sockets that looked alive, and the same bug coming back four months later._

February 18 was seven commits to fix memory leaks. Every LLM call was creating a new httpx client and each one allocates a connection pool that never closes. I made the gateway a singleton, then pre-built the provider instances, then made the billing client a singleton, then cached the HTTP client, then tried injecting a bounded httpx client into the Google SDK, then reverted that because the SDK wasn't designed for it, and finally sanitized the error responses that were leaking internal details.

Every fix revealed the next leak. I also discovered `ssl.create_default_context()` takes ~1.8s of CPU, so per-request client creation was blocking the event loop under load. An entire day to learn that HTTP clients should be singletons.

Our agents run in micro-VMs that suspend between queries. When the VM wakes up every TCP socket is dead but the HTTP client doesn't know. My first fix used an API that doesn't exist and crashed the sandbox. My second fix used the right API but the monotonic clock freezes during suspension, so the timer thinks zero seconds passed and every dead connection looks alive. My third fix was to destroy and recreate the client on every query. I spent days trying to be smart about it before brute force won.

The DB connection bug from July also came back. Different endpoint, same pattern: holding a database connection while making an HTTP call, so the pool drained under load. This time it was code our frontend engineer wrote on the backend, and I didn't catch it in review because I'd already "fixed" this problem months ago and wasn't looking for it anymore.

## Scale problems (March 2026)

> _I killed our own production machines with a load test. Then a third-party SDK froze the entire platform for 4 minutes._

The biggest incident of the year was self-inflicted. I was load testing our Unikraft bare metal machines and managed to kill them. 45 minutes of downtime while I scrambled to bring them back up. The machines that run our agent sandboxes, gone, because I pointed a load test at production infrastructure without thinking through what would happen at the limits.

Another major incident: a third-party agent SDK was making synchronous HTTP calls internally, and we were calling it from async handlers. When their API got slow the event loop froze and took down every endpoint with it. We had 262 gateway timeouts in 4 minutes. APM made it look like a network issue because all HTTP calls slowed down at once, but the event loop was just frozen so nothing could complete. We already had the fix on 1 of 21 call sites. The comment literally said "offload sync SDK call to thread to avoid blocking event loop." We just never applied it everywhere.

## What I actually learned

Most of my mistakes fall into a few patterns.

I assumed instead of checking. I assumed the SDK was async, assumed keepalive timers would survive VM suspension, assumed `round()` was fine for billing. Every assumption eventually broke in production and every time I was surprised.

I shipped without testing the full path. The Stripe SDK, the S3 event processor, the backend restructure, the config migration. Each one worked in my head but broke on deploy. Then I fixed it commit by commit, live, in production.

I picked the clever solution over the simple one. Keepalive timers vs client recreation. Singleflight with `asyncio.shield()` vs per-follower futures. The clever solution was always the one that needed more fixing.

I didn't finish what I started. Sync-to-async fix on 1 of 21 call sites. DB connection audit that never happened. Every partial fix gave me false confidence.

I built things nobody asked for. GIF generation. A standalone billing service. 602 lines of infrastructure for features nobody used and nobody missed.

This is what shipping fast actually looks like. You fuck up, you learn, you fuck up again, you learn again. The loop never stops, but you get faster at the learning part. We grew as fast as we did because we could adapt quickly, not because we avoided mistakes.

The gap between "works in a demo" and "works at scale" is about 4,000 commits. This is what most of them looked like.
