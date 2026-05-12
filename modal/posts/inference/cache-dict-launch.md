---
title: "Modal's Serverless KV Store Gets Its Limit Raised to Infinity"
author: "dshaar_"
date: "2025-05-20"
url: "https://modal.com/blog/cache-dict-launch"
category: "inference"
site: "modal"
---

# Modal's Serverless KV Store Gets Its Limit Raised to Infinity

 ![](https://modal-cdn.com/blog/images/dshaar-modal.webp) [Daniel Shaar@dshaar_](https://twitter.com/dshaar_) Member of Technical Staff  Modal’s [Dict](/docs/guide/dicts) primitive provides users with a simple TTL’ed (time-to-live) key-value store that can be accessed from any container within the same workspace environment. Dicts are well-suited for things like caching the results of function calls and communicating state changes among a fleet of containers.

Today, we’re excited to announce some major improvements to Dicts, including smarter caching, a new locking feature, and data durability!

## 🧑‍🚀 A few small changes to Dict, a giant leap for Dict use

Here’s what we’ve changed:

 Legacy DictsNew Dicts Storage limit10GiBUnlimitedItem expiry policy30 days since last write7 days since last write **OR read**Locking primitiveN/A`.put()` now supports a `skip_if_exists` flagDurability❌✅

These changes will apply to all **newly** created Dicts. Some cool things we think these features enable:

- LRU-like caching: now that reading extends an item’s TTL, hot cache entries will stick around for as long as they’re needed. And with unlimited items, there’s no need to worry about evicting useful data.
 - Distributed locking: in the event that many containers try to perform a redundant operation or state change, you can guarantee “exactly once” semantics using `skip_if_exists`.

With these new properties, let’s see how we can better tackle a common use case for Dicts: reducing backend load by caching function call results.

## 🧱 Building a request cache, Dict by Dict

Let’s look at a common app structure **without Dicts** that we may want to build and optimize on Modal. In this example, we have an “expensive” function that takes a while to run, along with a high concurrency web endpoint that simply calls out to the function.

After running this app in production for a while, we discover that users are issuing the same few requests to the web endpoint—who knew that figuring out 13 squared is 169 is all the rage. Not only that, but our app typically sees bursts of traffic for these hot requests.

As was commonly done by Modal users with the previous version of Dicts, we can define some sort of request caching class to wrap our function calls. A sample interface could look like:

We go ahead and implement some straightforward caching logic—check the cache, if the entry isn’t there, then make the call ourselves and add it to the cache when we’re done. Problem solved!

Or so we thought… turns out those bursts of traffic contain many requests that come in all at once, so we still end up making a bunch of expensive requests to our backend code before the cache is populated. We could work hard to narrow down that race condition window and handle the edge cases. But really, wouldn’t it be great if we could guarantee that we only make the one call to our expensive function?

With Dicts, we can make something quite snazzy to do just this!

## 🔒 Deduping requests—pop it, lock it

![](https://modal-cdn.com/blog/images/request-cacher-flow-2.webp)

Glossing over how a production version of this (that we hope to release in our client 👀) would handle various failure modes, the request handling logic now looks like:

- Try to “acquire a lock” by putting a `pending` entry in the Dict if it doesn’t already exist.
 - If someone else is / was working on the request, we read the Dict entry and poll for / fetch the result.
 - Otherwise, assuming we successfully wrote the `pending` entry:
We [`.spawn()`](https://modal.com/docs/guide/job-queue#creating-jobs-with-spawn) a function call and insert its handle as an `in_progress` Dict entry.
 - Once the function call is complete, we insert the result as a `completed` Dict entry.

Here’s a sample implementation:

The proof is in the dashboard, so here I’ve issued 3 identical requests to our web endpoint. The second request was deduped against the first, and the third request just got the result from cache:

![](https://modal-cdn.com/blog/images/not-so-expensive-function-endpoint-dash.webp)

This not only speeds up our customer experience significantly, but we also ended up calling the expensive function only once—success!

![](https://modal-cdn.com/blog/images/expensive-function-dash.webp)

## 💸 Shut up and give me my Dicts

Whether it’s caching, locking, or some other state management, just create a new Dict to get started! For more details, check out our [docs](/docs/guide/dicts). Caveat: to use the `skip_if_exists` flag, you may need to upgrade your client version.

Got questions? Come hang out in our [community Slack](/slack)—we’d love to hear what you’re building.