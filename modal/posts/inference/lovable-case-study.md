---
title: "How Modal powered 250,000 Lovable app creations in a weekend"
author: "Unknown"
date: "2025-07-07"
url: "https://modal.com/blog/lovable-case-study"
category: "inference"
site: "modal"
---

# How Modal powered 250,000 Lovable app creations in a weekend

  [Lovable](https://lovable.dev/) is one of the fastest growing startups in history, having hit $75M ARR a mere 7 months after they launched. Lovable is on a mission to build the “last piece of software,” enabling anyone to create fully functional applications without writing code. Users enter a prompt describing the app they want, and Lovable generates the code, spins up the application, and enables real-time visual edits. Lovable uses [Modal Sandboxes](/docs/guide/sandboxes) at massive scale to run LLM-generated code for thousands of apps in safe and isolated sandboxes.

![](https://modal-cdn.com/blog/images/lovable.gif)

## The problem: performance and reliability at scale

In June 2025, Lovable had a major promotional weekend event coming up, in collaboration with Anthropic, OpenAI, and Google. This event was set to dramatically increase user activity.

Unfortunately, Lovable’s existing code sandbox provider—a distributed cloud VM platform—raised concerns around scalability and operational risk. The team wasn’t confident the provider could scale fast enough to meet the expected demand, and with only this single vendor in place, Lovable was exposed to high risk of service disruption.

 “It was pretty clear when I joined that our biggest pain point was sandbox infrastructure. Any outage would essentially take us offline.” — Erik Lindblad, Senior Infrastructure Engineer

## Build vs. buy

Lovable explored building their own sandbox solution on AWS and Kubernetes. This direction presented its own challenges, from learning the intricacies of AWS identity management to needing to create their own pod provisioning system. While they eventually built a system that scaled up to meet existing demand, they knew that they would need to invest much more time to support the current customer growth trajectory.

With this in mind, they started evaluating other vendors, including Modal.

## Proving out Modal’s reliability and speed

Lovable’s key criteria were reliability, scalability, and fast sandbox startup times.

 “There’s tons of cheap providers for sandboxes. But as soon as you start scaling up, more and more of these vendors have trouble serving you with capacity. We wanted to find a vendor that could scale to where we needed to go for multiple years.” — Erik Lindblad

Lovable was able to get a proof of concept on Modal up and running in just days. They went from 15,000 lines of sandbox orchestration code with their previous provider to just 700 lines with Modal! This was partly enabled by Modal’s rich networking features, like [Tunnels](/docs/guide/tunnels). Each of Lovable’s Sandboxes uses an encrypted Tunnel to allow communication with the server running inside the Sandbox. Behind the scenes, Modal operates a fleet of TCP relays around the globe to ensure low latency and reliability at petabyte scale.

Modal’s reliability and stability were fully proven out during the promotional weekend. Lovable saw concurrent sessions surge by 2.5-3x, successfully enabling users to build an estimated 250,000 applications in just 48 hours. Over the course of the event, Modal ran over 1 million sandboxes, powering up to 20,000 concurrent sandboxes at peak. Lovable’s platform team wasn’t paged even once during the whole weekend.

Modal Sandboxes are now used to serve every app generation session in Lovable. Below is an app built on Lovable—try it out yourself!

![](https://modal-cdn.com/blog/images/lovable-game-small.gif)  [https://lovable-modal-adventures.lovable.app/](https://lovable-modal-adventures.lovable.app/)

## Unlocking more performance gains

Now that baseline reliability is no longer a concern, Lovable plans to use more Modal Sandbox capabilities like [snapshotting](/docs/guide/sandbox-snapshots) to make the end user experience more performant. And of course, Modal will continue to support their viral growth as they push the limits of infrastructure at scale.

 “We've previously managed to break services like GitHub because of our load, so when Modal was able to handle the massive scale of our AI weekend event so smoothly, that meant a lot. We now trust Modal to keep up with our growth, and we're excited to build together in the long term.” — Anton Osika, Founder and CEO

Interested in a deep dive on how Modal Sandboxes fit in to Lovable’s architecture? Stay tuned for Part 2!