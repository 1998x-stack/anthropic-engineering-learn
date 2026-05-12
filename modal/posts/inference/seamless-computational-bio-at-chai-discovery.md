---
title: "Seamless Computational Bio at Chai Discovery"
author: "Unknown"
date: "2026-01-15"
url: "https://modal.com/blog/seamless-computational-bio-at-chai-discovery"
category: "inference"
site: "modal"
---

# Seamless Computational Bio at Chai Discovery

 ![](https://modal-cdn.com/cdnbot/gretas_ktpny8_7364f421.webp) Greta Workman Product Marketing  Chai Discovery is a frontier drug discovery company using machine learning to design new medicines. Their mission is to develop a flexible, ML-driven platform that can adapt to new biological targets and experimental data, accelerating discovery across diseases and modalities—the “computer-aided design suite for molecules”.

Too often, infrastructure is the bottleneck for research and discovery. By building on Modal, Chai can scale experiments seamlessly, keep data consistent, and run the same workflows from research through production.

## The challenge: complex, bursty bio workloads

Chai’s machine learning pipelines combine diverse models, large biological datasets, and GPU-heavy computations. Each experiment can differ dramatically in scale, from small protein structure tests to full antibody design campaigns, and must scale from one run to thousands overnight. The workloads are heterogeneous and bursty, with frequent precomputation steps each with shifting hardware demands.

Running all this on traditional cloud infrastructure would have meant maintenance overhead that would have slowed their research:

- **Repetitive data setup:** Huge datasets, often hundreds of gigabytes, would need to be downloaded and indexed repeatedly on every machine.
- **Hardware drift:** Inconsistent GPU types and driver versions could introduce subtle reproducibility bugs.
- **Operational overhead and idle time:** Scaling inference would mean manual orchestration, days of setup, and paying for idle clusters.

“I used to wrangle AWS, Google Cloud, and Azure, but when I was dealing with raw instances and volumes I frequently felt like I was operating at the wrong level of abstraction. With Modal, building infrastructure has shifted from being an imperative task to a declarative one. You add a few lines of code specifying what you want to do and it just runs.” — Kevin Wu, Machine Learning Researcher

## **Fast, scalable, consistent compute with Modal**

Chai adopted Modal from day one to eliminate the infrastructure overhead that could have slowed experimentation. With Modal, compute is elastic, consistent, and instantly accessible, so researchers can focus on science, not infrastructure.

“Our ML team can just say, I’m going to run this — I don’t have to think about whether it needs 10,000 queries or what my data needs. It all just happens behind the scenes.” — Kevin Wu, Machine Learning Researcher

**Consistent and reproducible execution environments for heterogeneous models**

Before Modal, reproducibility was fragile. Small mismatches in GPU or driver versions could derail results and force hours of debugging. On Modal, every job runs in an identical, reproducible environment. That consistency is essential for Chai’s pipelines, which chain together many heterogeneous models and needs, like protein embeddings, multiple sequence alignments (MSA), and antibody design models. Furthermore, the ease of managing Modal environments enables Chai to deploy outputs exactly as they are developed in research, improving efficiency and scientific rigor.

“We have a lot of different models that give us different layers of insights on these proteins, and being able to run them all on the hardware that makes sense is what makes the product possible.” — Kevin Wu, Machine Learning Researcher

“You’d spend six hours just downloading the database to get one query out. With Modal Volumes it’s downloaded once, instantly available everywhere, and scales to thousands of queries.” — Kevin Wu, Machine Learning Researcher

**Dynamic GPU scaling and workload elasticity**

Chai’s workloads are highly variable—relatively quiet one day, bursting to thousands of inference jobs the next. Modal’s elastic scaling matches that pattern automatically. GPUs spin up in minutes, handle the peak load, and spin down again as demand drops. The team never has to manage clusters, plan capacity, or worry about underutilization.

“Sometimes we spin up hundreds of GPUs at a time, and the fact it’s up in a few minutes without onerous configurations or dashboards whenever we need to is kind of a miracle.” — Kevin Wu, Machine Learning Researcher

![](https://modal-cdn.com/cdnbot/peptide_mhc framehgulbpsx_73faccae.webp)

## **From research to production on one platform**

Today, Modal is a key component in Chai’s compute platform, powering everything from large-scale model training experiments to molecular design inference pipelines.

With Modal, Chai can move research ideas into production with almost no friction. Retries, scaling, and hardware orchestration happen automatically, giving researchers the same reliability whether they’re quickly prototyping a new model or deploying a battle-tested server for a production pipeline.

Chai can now spin up hundreds of GPUs in minutes, processes terabyte-scale biological datasets instantly, and ships new production pipelines directly from Python, without needing to rewrite infrastructure. What once took days of setup now happens automatically, giving researchers faster feedback and freeing them to focus on discovery.

“It’s not just a time savings, it’s the mental overhead that disappears. With Modal, we add a few decorators to a function we need to scale, forget about them, and they just work.” — Kevin Wu, Machine Learning Researcher