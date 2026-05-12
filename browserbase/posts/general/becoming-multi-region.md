---
title: "Becoming Multi-Region"
author: "Alex Phan"
date: "2024-12-06"
url: "https://www.browserbase.com/blog/becoming-multi-region"
category: "general"
site: "browserbase"
---

December 06, 2024

# Becoming Multi-Region

![](https://cdn.sanity.io/images/yd6zslid/production/67f2b805367fb7dd6d0b82699cd20cd7c87b6538-502x506.png?fm=webp&amp;h=1613&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Alex Phan

[Engineering](/blog/engineering/)

![](https://cdn.sanity.io/images/yd6zslid/production/d20bdd040b1a5204289faa035ba66a4dc8d0c1a3-2568x1737.png?fm=webp&amp;h=1082&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

## The Challenge: Single-Region Growing Pains

When we first built Browserbase, we operated exclusively from AWS `us-west-1`. While this served our initial needs, we quickly discovered a critical limitation: latency. Every request faced a 70-80ms delay, and these delays weren’t just adding up—they were multiplying as operations stacked on each other.

As our customer base grew globally, performance emerged as the #1 concern in our feedback. This prompted us to make latency reduction our top priority for Q4.

## Our Investigation

Our investigation took us through various possibilities. We first tried utilizing more resources for our browsers. In addition, we also attempted to remove layers of virtualization.

However, the answer to this problem is distance. Our architecture relied heavily on CDP (Chrome DevTools Protocol) commands—small instructions that needed to be executed sequentially. Each command had to complete before the next could begin, creating a waterfall of delays.

## The Root Cause

![](https://framerusercontent.com/images/SCWbcZ9yfFXAmOEFRSRposZVPyU.png)

User Request -&gt; [Long Distance Travel] -&gt; us-west-1 -&gt; [Processing] -&gt; [Long Distance Travel] -&gt; User Response

Whether a customer was in London, Tokyo, or New York, their requests had to make a longer journey to where servers were running, `us-west-1`.

That means for users in Singapore, this meant their browser commands were traveling nearly halfway around the world—and back—for every single operation.

## Multi-Region

Looking at our latency data, we realized we needed to shift our infrastructure strategy. Instead of optimizing traffic through a single region, we needed to rethink how we could minimize the physical distance between our customers and their browser sessions.

**The solution became clear**: rather than forcing all users to connect to a single point, we needed to bring our browser infrastructure closer to where our customers operate.

The entire migration took just one month to implement, proving that sometimes the most impactful solutions aren’t the most complex. Below, we’ve expanded our infrastructure to multiple strategic locations worldwide:

![](https://framerusercontent.com/images/Xkqwo5nwiDEsPN4v1JTuje1KNgQ.png)![](https://framerusercontent.com/images/1nngE0vZaAoEgRLLw20Eoz9dQ.png)

## The Numbers

To validate our multi-region approach, we ran tests using a sample web scraping script that performs multiple CDP operations.

We tested this script from different locations connecting to both nearby and distant regions.

The script performs multiple sequential operations - waiting for elements, selecting DOM nodes, and extracting data - each requiring multiple CDP commands to complete.

To summarize the results:

- **More than 2x faster** task completion for users connecting to their nearest region
- **Reduced resource consumption** due to faster task completion
- **Lower costs** for customers through improved efficiency

### Before vs After Comparison

**Before (Single Region -** `**us-west-1**`**):**

Eastern US (us-east-1) → us-west-1: ~63ms latency

Western US (us-west-2) → us-west-1: ~23ms latency

Frankfurt (eu-central-1) → us-west-1: ~152ms latency

Singapore (ap-southeast-1) → us-west-1: ~169ms latency

Each command must wait for the previous one to complete and every command faces this round-trip latency. Below are the improvements after we’ve implemented multi-region:

**After (Multi-Region):**

With our multi-region deployment, users can specify their preferred region when connecting. By choosing a server closer to their location, they can significantly reduce the distance each CDP command needs to travel.

Here’s what the latency looks like when users connect to their local regions instead of routing everything through `us-west-1:`

New York → us-east-1: ~6ms latency

Frankfurt → eu-central-1: ~3ms latency

Singapore → ap-southeast-1: ~5ms latency

Tokyo → ap-northeast-1: ~4ms latency

**This represents a dramatic improvement:**

Eastern US users: 90% reduction in latency (63ms → 6ms)

Western US users: 87% reduction in latency (23ms → 3ms)

European users: 98% reduction in latency (152ms → 3ms)

Asian users: 97% reduction in latency (169ms → 5ms)

It’s important to remember that these latencies compound with each CDP command, so the real-world performance improvement is even more significant when running complex browser automation tasks that require multiple sequential commands.

## Best Practices for Customers

To get the most out of our multi-region infrastructure, we recommend:

- Choose the region closest to your primary user base
- For applications serving global users, consider using multiple regions
- Monitor latency metrics to ensure optimal performance
- Contact our support team for region-specific optimization advice

The switch to multi-region is straightforward. When creating a new browser session, simply specify your preferred region using the `region` parameter in your API request.

Here’s how to create a session in `us-east-1` using a curl request:

curl --request POST \\

--url [https://www.browserbase.com/v1/sessions](https://www.browserbase.com/v1/sessions) \\

--header ‘Content-Type: application/json’ \\

--header ‘X-BB-API-Key: YOUR_BROWSERBASE_API_KEY’ \\

--data &#x27;{

“projectId”: “&lt;YOUR_BROWSERBASE_PROJECT_ID”,

“region”: “us-east-1”

}’

We have a dedicated page for how to use Multi-Region capabilities here.

For best results, we now recommend that customers simply choose the location nearest to them when using our service. While our main location is still in the Western USA (`us-west-2`), you can choose any of our locations to get the best possible performance for your needs.

## Looking Forward

We are continuously monitoring usage patterns and performance metrics to identify potential new regions and further optimize our existing infrastructure.

For more information, visit Browserbase to learn more!