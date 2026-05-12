---
title: "Runway Chooses Modal to Power Real-Time Inference for Runway Characters"
author: "Unknown"
date: "2026-03-26"
url: "https://modal.com/blog/runway-chooses-modal-to-power-real-time-inference-for-runway-characters"
category: "inference"
site: "modal"
---

# Runway Chooses Modal to Power Real-Time Inference for Runway Characters

  Today, we're announcing that Runway is partnering with Modal to power real-time inference for [Runway Characters](https://runwayml.com/product/characters).

Runway Characters is a real-time video agent API that lets developers, startups, enterprises and consumers build fully custom conversational characters. These video agents can have any appearance and any visual style, with full control over voice, personality, knowledge and actions. Built on Runway’s general world model, [GWM-1](https://runwayml.com/research/introducing-runway-gwm-1), Characters generates expressive digital personas from a single image, with zero fine-tuning required.

![](https://modal-cdn.com/cdnbot/runwaycoverimagecxy6f3ie_2895d6ff.webp)

Thousands of organizations are already using Characters, including Fortune 10 technology companies, major Hollywood studios, global advertising agencies and gaming companies, with use cases ranging from customer support and internal training to experiential advertising and immersive game worlds. Characters represents the first step toward a future of online interaction built around real-time video rather than text.

This kind of continuous, expressive, low-latency video generation held across extended conversations and experiences requires infrastructure purpose-built for real-time interaction. Modal's serverless compute platform is designed for exactly this type of workload: GPU-intensive, latency-critical and highly variable in demand. The iteration speeds Modal afforded allowed Runway’s team to move from proof of concept to production in under 30 days.

"Real-time video inference is a fundamentally different engineering challenge than batch generation, especially given our customers are running these experiences globally," said Kamil Sindi, CTO of Runway. "Runway Characters requires sustained low latency across the full duration of a conversation—expressions, lip-sync, gestures—without degradation. Modal's infrastructure gave us the performance and reliability we need to ship this in every global region, at production scale."

Achieving the latency required for real-time interaction means distributing inference across multiple GPUs with high-bandwidth communication between nodes. By adding a single line of code on Modal, Runway can turn their containers into multi-node GPU clusters with RDMA networking, available instantly across every region. Modal deploys these workloads across geographies as a single unified pool, routing them close to users and scaling on demand, so Runway can serve users anywhere without pre-provisioning or managing regional infrastructure directly.

"Runway is pushing the frontier for what's possible with world models, which requires running complex models at large scale with very low latency. This is something Modal does extremely well,” said Erik Bernhardsson, CEO of Modal. “We're proud to be the infrastructure powering Characters."

Runway Characters is available today to all developers and businesses at [dev.runwayml.com](http://dev.runwayml.com), and to consumers at [runwayml.com](http://runwayml.com). Enterprise teams can [reach out](https://runwayml.com/enterprise?utm_source=runway-product-characters&amp;utm_medium=rw-website&amp;utm_campaign=runway-characters#inquiry-form) to learn more about deploying custom avatar experiences at scale.