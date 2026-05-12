---
title: "Introducing: Modal 1.0"
author: "app"
date: "2025-06-09"
url: "https://modal.com/blog/introducing-client-1-0"
category: "inference"
site: "modal"
---

# Introducing: Modal 1.0

  Last week, we launched [version 1.0 of the Modal client](https://pypi.org/project/modal/). This is a significant milestone for us because it marks a new level of maturity and stability for the Modal platform. We’ve worked to make the client API more robust and predictable, and we expect far fewer breaking changes moving forward.

So what do we mean by “Modal client”? If you’re new to Modal, you can think of Modal in two parts: our client, which is a Python SDK, and our managed cloud platform, which we use to run user workloads around the world.

The client gives developers the ability to access serverless cloud compute from their application code via decorators. Here’s a basic example:

Developer ergonomics has been a core principle of Modal from the very beginning. Crafting a good developer experience requires making tricky tradeoffs along the way, however. Working towards 1.0 has given us a chance to reflect on our core design principles and some of the major decisions we’ve made along the way.

## Design principles for 1.0

### 1. Avoiding unpredictable magic

We want using Modal to feel a little magical, but “magic” behavior can be a double-edged sword. With 1.0, we’ve intentionally moved away from some of these “magic” behaviors.

One example is our old “automounting” feature. If your App had imports of local packages, we’d automatically find and include them in your Modal deployment. While helpful on the surface, this became unpredictable in many cases. Users could end up with more packages than needed, making deployments slower. Users could also start expecting every file they read to be automatically included, even when that wasn’t the case.

With 1.0, these behaviors are now explicit. You’ll specify exactly what local files and packages are included in your container, apart from the Function’s own package. Your App definition might become more verbose, but the benefit is much more predictable and easy-to-debug behavior.

Before:

After:

### 2. Separating core functionality from additional concepts

As the number of use cases powered by Modal grows, so does the number of concepts, and thus also the need for organizing them in a scalable way. We want to be able to add new features without making it harder to understand the basics.

After adding many new parameters to the `@app.function` decorator, we’ve recognized that trying to put every possible configuration into a single decorator quickly becomes unwieldy. Going forward, we’ll be clearly separating core functionality from additional concepts by splitting them up over separate decorators. An example of this is the new `@modal.concurrent` decorator, which lets you express concurrency patterns independently from the configuration in `@app.function`.

This pattern also allows us to add config options that are specific to each decorator, such as `target_inputs` in the code snippet below.

Before:

After:

### 3. One canonical path

We believe in providing clear paths for users to accomplish common tasks. This means reducing redundant methods for similar actions, simplifying the mental model for developers.

One example is how local files are brought into your Modal container. Previously, you could either specify them in your image setup or pass a `modal.Mount` directly in your Function configuration. This meant that two distinct object types were responsible for bringing local assets into the remote environment. We’ve now moved all of this functionality under the `modal.Image` class. This aligns with Modal’s core promise of abstracting the container environment: everything related to the container *filesystem* and its initial state is now managed explicitly and consistently within the `Image` definition. The `Image` class already had robust ways to bring over local data, so [consolidating](/docs/guide/modal-1-0-migration#deprecating-mount-as-part-of-the-public-api) here provides a more coherent experience.

## A more predictable client release cycle

You’ll also notice a shift in our client release cycle. We’ll be batching updates together so it’s easier for you to quickly see what’s new and decide when to upgrade. This gives you more predictability and control over your development environment. You’ll always be able to see what changes we’ve made in our [changelog](/docs/reference/changelog).

## What’s next?

Modal 1.0 is a significant milestone, but it’s just the beginning. There are a couple of particularly exciting directions we’re taking the client SDK. One is creating SDKs for other languages, which we’ve made [good progress](/blog/sdk-javascript-go) on already. The other is exploring the distinction between Modal as a software tool for humans versus a tool for agents. What does it mean to have good ergonomics in a world where development is mediated by AI tools? How can we adapt the platform to better serve the unique needs of AI-driven workflows?

We think you’ll appreciate the stability and clarity that Modal 1.0 brings, and we hope this release will make building with Modal even more productive. For detailed instructions on how to migrate to 1.0, check out the [1.0 release notes](/docs/reference/changelog#100-2025-05-16) and our [migration guide](/docs/guide/modal-1-0-migration).