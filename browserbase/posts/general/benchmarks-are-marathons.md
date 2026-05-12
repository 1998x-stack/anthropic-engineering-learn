---
title: "Benchmarks are marathons, here’s how we 5x’d our browser performance"
author: "Paul Klein"
date: "2026-04-30"
url: "https://www.browserbase.com/blog/benchmarks-are-marathons"
category: "general"
site: "browserbase"
---

# Benchmarks are marathons, here’s how we 5x’d our browser performance

![](https://cdn.sanity.io/images/yd6zslid/production/92ccd19d7aa2bb46f8c3b3da11a94ac50ba10f95-498x502.png?fm=webp&amp;h=1613&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Paul Klein

[Engineering](/blog/engineering/)

![](https://cdn.sanity.io/images/yd6zslid/production/4c0655f69ea346fb71c5ce1f5b5ced500782d850-2568x1737.png?fm=webp&amp;h=1082&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

Good benchmarks are hard. The best ones are well-designed, fair, and continuously updated (not point-in-time marketing snapshots). That’s why we’re excited to stand behind the new browser benchmarks from ComputeSDK.

![](https://cdn.sanity.io/images/yd6zslid/production/f6f7a526cd5f0abab0341b855205907833f593cb-1450x1048.png?fm=webp&amp;h=1156&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

Browserbase shows up near the top because we’ve spent the last year making the “boring” parts of browser infrastructure fast: session creation, CDP connection, navigation overhead, and teardown.We didn’t get here overnight. Performance also hasn’t historically been our single highest priority. Our prioritization has been:

- Security
- Reliability
- Performance

That ordering is why leading AI companies like Ramp, Lovable, and Stripe trust Browserbase to power their agents’ browsing capabilities.

If you haven’t met me before, I’m Paul. I’m a software engineer turned founder, and I’m obsessed with headless browsers. This is the third company I’ve worked at where running browsers at scale is fundamental to the job. At this point, I’ve spent a big chunk of my life banging my head against Chromium in the cloud. That’s why I started Browserbase.

Below are the biggest lessons I’ve learned after running 100M+ browser sessions.

### 1) Observability is everything: you can’t improve what you can’t measure

![](https://cdn.sanity.io/images/yd6zslid/production/d78b8e5d75952343e3cb540174a668e37dc1d821-680x334.png?fm=webp&amp;h=786&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

Performance work starts with humility: if you can’t measure it, you’re guessing.

For this project we started by:

- Observing real customer behavior (what operations they do, at what frequencies)
- Building benchmarks that reflect the real workload
- Using statistical analysis to understand true impact vs noise

We also invested in instrumentation:

- OpenTelemetry tracing for each request
- Custom tooling to analyze CDP traffic (which is often where “mysterious” latency hides)

Most importantly: benchmarking isn’t a one-off exercise. If you measure once and then stop, you’ve created a vanity metric. The only benchmarks that matter are the ones you keep running while you ship.

### 2) Round-trip latency (RTT) is the most important metric

For remote browsers, distance is a feature until it isn’t.Two things make RTT especially punishing:

- CDP is a chatty protocol. Loading a page can mean thousands of CDP requests.
- If your client does request/response work (like routing, interception, or instrumentation), page loads often depend on repeated round trips to the client.

This is why putting a browser closer to your agent can matter as much as any micro-optimization inside Chromium.

### 3) “CDP connect time” tells the truth

One of the easiest ways to “win” a benchmark is to make create look fast... and then do the real work later. That shows up immediately if you measure connect time separately.

We measure connect carefully because it’s where infrastructure reality is hardest to fake:

- If you defer configuration until connect, you may appear fast—until the first real user operation.
- If you configure upfront, you may fail earlier—but you fail in the right place, and you give developers deterministic behavior.

This also matters because retry behavior differs by layer:

- HTTP request libraries often retry transient 500s on create.
- CDP connection retries generally aren’t built into common browser frameworks (e.g., Playwright).

Our philosophy: configure the browser upfront and fail early if something is wrong, rather than failing at connection time.

### 4) Less hops is more: every proxy and load balancer matters

Browser infrastructure is effectively “WebSockets as a service.” Customers hold long-lived connections and send events through your stack. As systems mature, it’s common for teams to layer:

- load balancers,
- reverse proxies,
- service meshes,
- application-level WebSocket proxies,

on top of legacy paths.

Every hop adds latency:

- Not just “speed of light” RTT, but real compute delay

A major unlock for us was ruthlessly removing unnecessary hops—especially application-layer WebSocket proxies.

### 5) Goroutines &gt; event loops (for the hot path)

CDP traffic is inherently bursty. When a page loads or an animation plays, you can get thousands of network/screencast events in a short window. The faster you can move those events over the wire, the better performance (and tail latency) looks.

For hot-path WebSocket and CDP proxying, we’ve found Go’s concurrency model (goroutines) is simply a better fit than a single event loop, particularly under burst and fan-out. That doesn’t mean “Go good, Node bad” universally; it means we should pick the right tool for the path that carries the most packets.

### In summary

![](https://cdn.sanity.io/images/yd6zslid/production/e7fbfc07137dd55745a4bda8e3a13f695260412e-680x259.jpg?auto=format&amp;h=609&amp;w=1600&amp;fit=min&amp;q=75)

Performance work is iterative: fixing one bottleneck usually reveals the next one. There are rarely silver bullets.

But that’s also why it’s fun. When you keep chasing the slowest part of the system, you eventually discover what your architecture is truly capable of, and what needs to change to go further.

The best improvements are still ahead. I’m excited to write more about the technical details behind Browserbase performance (including some wild stories from the trenches, like how we were encoding more videos per second than Twitch). Stay tuned!