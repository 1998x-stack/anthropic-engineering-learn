---
title: "Closer to the Metal: Leaving Playwright for CDP"
author: "Nick Sweeting"
date: "2025-08-20"
url: "https://browser-use.com/posts/playwright-to-cdp"
---

# Closer to the Metal: Leaving Playwright for CDP

**Author:** Nick Sweeting
**Date:** 2025-08-20
> Why we dropped Playwright and switched to raw CDP for faster, more capable browser automation.

---

## Goodbye Playwright, Hello CDP

Playwright and Puppeteer are great for making QA tests and automation scripts short and readable, but as AI browser companies have been learning the hard way over the last year, sometimes these adapters obscure important details about the underlying browsers.

We decided to peek behind the curtain and figure out what the browser was really doing, and it made us decide to drop playwright entirely and just speak the browser's native tongue: CDP.

By switching to raw CDP we've massively increased the speed of element extraction, screenshots, and all our default actions. We've also managed to add new async reaction capabilities to the agent, and proper cross-origin iframe support.

## The Curse of Abstraction

Building AI browser automation is like building on top of a jenga tower of complexity. Every layer presents its own leaky abstractions, its own subtle crashes, and its own resource constraints.

If you've ever heavily depended on an adapter library and build up a large codebase around it, you know the feeling that eventually comes when you realize the adapter library is no longer saving you any time by "hiding the true complexity". In our case that time has finally come for Browser-Use and playwright-python, the library that we've historically used to drive our browsers with LLM-powered tool calls like `click`, `input_text`, `go_to_url`.

Playwright also introduces a 2nd network hop going through a node.js playwright server websocket, which incurs a meaningful amount of latency when we do thousands of CDP calls to check for element position, opacity, paint order, JS event listeners, aria properties, etc.

## How do Browser Drivers Work?

All these adapter libraries, drivers, and AI helper extensions really just exist to pass messages and make RPC calls to these underlying browser APIs:

- **Chrome Extension APIs**: `chrome.tabs.captureVisibleTab()`, `chrome.automation.getTree()`, `chrome.scripting.executeScript()`, `chrome.debugger.sendCommand()`
- **CDP APIs** (via pure CDP Websocket or WebDriver BIDI socket): `Page.navigate({url})`, `Target.createTarget()`, `DOMSnapshot.captureSnapshot()`, `Page.handleJavaScriptDialog({accept: true})`, `Browser.setDownloadBehavior()`
- **OS-Level Accessibility & screenreader APIs**
- **Internal Chromium C++ APIs**
- **Launch Flags, User Data Dir, and Preferences**

## Playwright's Sharp Edges

The playwright happy paths usually work fine, but the devil is in the details:

- `fullPage=True` screenshot on pages longer than >16,000px high (reliably crashes playwright)
- `alert()`/`confirm()`/`onbeforeunload` handling
- attempting to keyboard/mouse/dialog input without focusing a page
- file upload & download handling on remote browsers
- `about:*`, `chrome://*`, `chrome-error://`, `chrome-extension://`, PDF tab handling
- chrome preferences and enterprise/registry configuration management
- crashed tab handling

## At least 10 different ways a tab can crash in Chrome

- all targets start in a briefly semi-"crashed"/unresponsive state while initial requests are inflight
- chrome zygote/root process can crash (slow user_data_dir/filesystem io, oom, cpu lag, etc.)
- GPU process can crash
- page renderers can crash due to exceptions raised within chrome source (sigsev, oom, etc.)
- page renderers can crash because the page exceeds allowed resources
- page can spinlock/oom due to infinite loops or crypto mining in its JS main thread
- scrolling/input/screenshot before `activateTarget` focus can crash targets (5sec delayed!)
- handling a JS popup before activateTarget or attempting to handle it after already closing
- parent frame navigation during child `onbeforeunload` "are you sure you want to leave?"
- any of the above crashes in a nested OOPIF leading to subtle issues in the parent target

Playwright handled about half of these well, and presented impassible barrier to solving the other half, so we made the call to switch.

## Case Studies: Key Changes in the Migration

### New CDP-USE Library Providing Python Type Bindings

A type-safe Python client generator for the Chrome DevTools Protocol (CDP). This library automatically generates Python bindings with full TypeScript-like type safety from the official CDP protocol specifications.

### New Event-Driven Architecture

We used to only update our view of the world between actions, right before sending the next state summary to the LLM. This makes sense when your assumption is that the page contents will only change as a result of actions, but this is not always true!

We've introduced a new event-driven architecture to better fit the underlying event-driven architecture of CDP. Now we can subscribe to and respond to CDP events, which we set up in "watchdog" services that monitor for various things.

For example, our `downloads_watchdog` watches for any file downloads that start spontaneously, whether triggered by a click, js executing, or any other method. `crash_watchdog.py` can now watch for page crashes in a single place by just subscribing to a crash event, and we no longer have to scatter crash detection and retry logic all over the rest of the codebase.

### New Extracted Element Handle that works across OOPIFs

A tab is not a page; it's a constellation of **targets** (root + cross-origin iframes + workers), each hosting **frames**, each containing **nodes**. Abstract that away and you lose the ability to route input, correlate events, and re-find elements after DOM churn.

We now represent nodes with "super-selectors" that include `targetId`, `frameId`, `backendNodeId`, x/y position, and fallback selectors.
