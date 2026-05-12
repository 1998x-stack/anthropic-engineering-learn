---
title: "Autobrowse: The Mythos moment for Browser Agents is here"
author: "Kyle Jeong"
date: "2026-05-06"
url: "https://www.browserbase.com/blog/autobrowse"
category: "announcements"
site: "browserbase"
---

# Autobrowse: The Mythos moment for Browser Agents is here

![](https://cdn.sanity.io/images/yd6zslid/production/95c585473bfcf3c8eb260a3b9418033dbcce9ee9-552x556.png?fm=webp&amp;h=1612&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Kyle Jeong

![](https://cdn.sanity.io/images/yd6zslid/production/9a017fd88507647e3ee51a27fa0573eeb8f4567d-540x542.png?fm=webp&amp;h=1606&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Shubhankar Srivastava

[Engineering](/blog/engineering/)

**TL;DR **Browser agents have an amnesia problem. They re-discover every site from scratch on every run, paying the full discovery tax forever. Autobrowse fixes that by letting an agent iterate on a real task until it converges, then graduating the winning approach into a durable, reusable skill. That skill is memory the next agent, teammate, or customer can pick up and run without “re-learning” what&#x27;s already been learned.

### The genius without a hippocampus

If you&#x27;ve shipped a browser agent into production, you already know the shape of this problem.

The first run on a new site is exciting. The agent wanders around, figures out the page, eventually completes the task. The second run looks almost identical. The hundredth run is depressing. By then you&#x27;ve paid for the same exploration a hundred times, the cost graph is a straight line going up, and you still don&#x27;t have a clean artifact you can hand to a teammate to say &quot;this is how we do this job.&quot;

Real sites are messy. They render differently for different user agents, gate content behind JavaScript, hide the data you actually want behind an undocumented JSON endpoint, throw captchas when they don&#x27;t recognize the session, and sometimes redesign their flow on a Tuesday. A generic agent loop copes with all of that fluently in the moment, then forgets everything once the session closes. The reasoning that solved Monday&#x27;s problem evaporates along with the session.

**The real bottleneck for browser agents in production is memory, in a form humans and agents can both read and trust. Reasoning has stopped being the constraint.**

### What is Autobrowse?

Autobrowse is a workflow that uses AI to improve AI. You give an agent a real task on a real site. It runs the task end to end, studies the trace it produced, iterates on its strategy, and keeps going until the workflow becomes reliable rather than lucky. Once it converges, it graduates the winning approach into a reusable skill: a markdown file plus the deterministic glue (CLI calls, fetches, selectors, helper scripts) needed to repeat the job.

This is similar to Karpathy&#x27;s autoresearch harness, but for learning faster and cheaper browser skills. The first run is expensive on purpose, it&#x27;s the run that pays for everything that comes after.

The artifact is the point. Every Autobrowse run produces a durable markdown file any future agent can load and execute, on top of whatever value you got from the run itself.

### How it works:

The learning loop:

![](https://cdn.sanity.io/images/yd6zslid/production/e30797a60ff943f82ca62fe0b4eb422a1452476e-3968x2408.png?fm=webp&amp;h=971&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

The core loop is simple:

- **Objective**. Hand the agent a real task on a real site (&quot;book a 7pm dinner reservation at this restaurant on OpenTable&quot;).
- **Run**. Let the agent attempt the task end to end against a live browser.
- **Study**. The agent reads its own trace. Where did it stall? Where did it guess? Where did it spend tokens it didn&#x27;t need to?
- **Strategy**. The run’s “outer loop” maintains a strategy.md file, basically a scratchpad where the agent dumps observations after each iteration (what worked, what broke, what to try next, what to stop doing). On the next iteration, the agent reads strategy.md first and uses it as context, so improvements compound instead of resetting every run.
- **Iterate**. Refine the strategy based on those notes. Drop steps that didn&#x27;t pull weight. Lean on deterministic helpers (browse fetch, browse search, custom Python) wherever possible.
- **Converge**. Once consecutive iterations stop yielding meaningful improvements in cost or turn count, short-circuit.
- **Graduate**. Write out a SKILL.md plus any helper files into the public skills repo.

In practice, we cap iterations low (~ 3 to 5) and short-circuit aggressively. The goal is a reliable, cheap path that&#x27;s good enough to be reused, (technically short of any theoretical global optimum).

**The output?**

What comes out the other side is a small, readable file. No transcript, no vector of embeddings, no screenshot reel. Just markdown (just skim this):

```
markdown

--- name: &quot;craigslist-search-listings&quot; title: &quot;Craigslist Search Listings&quot; description: &quot;Search Craigslist in a given city and category for listings matching a query, returning each listing&#x27;s title, price, location, posting date, and listing URL.&quot; website: &quot;craigslist.org&quot; category: &quot;marketplace&quot; tags: [&quot;craigslist&quot;, &quot;marketplace&quot;, &quot;listings&quot;, &quot;search&quot;] status: &quot;autobrowsed-run-004 + prod-validated-002&quot; source: &quot;autobrowse + browser-trace · 4 iters · converged 2026-04-30 · cross-region prod validation 2026-05-01 (NY/SF/Boston, cta+apa) · postal-override discovery 2026-05-01 (Chicago/NYC, mca+apa)&quot; updated: &quot;2026-05-01&quot; recommended_method: &quot;api&quot; alternative_methods:  - method: &quot;browser&quot;  rationale: &quot;When the JSON API is rate-limited or blocked (rare — no auth or anti-bot today), fall back to browsing the city subdomain&#x27;s /search/{category} page and extracting listings from the rendered text + anchor hrefs.&quot; ---
# Craigslist Search Listings — Browser Skill
## Purpose
Return a list of Craigslist postings matching a query in a given city and category — title, price, location, posting time, lat/lon, posting ID, and canonical listing URL. Read-only; never posts or edits.

## When to Use
- Daily / hourly monitoring of new listings matching a query. - Bulk extraction across multiple cities or categories. - Anywhere you&#x27;d otherwise scrape Craigslist HTML — the API is faster, cheaper, and structurally more reliable.
## Workflow
The Craigslist web UI is a thin client over a public JSON API at `https://sapi.craigslist.org` — no auth, cookies, session state, or anti-bot stealth. Send a `Referer` header matching the target city subdomain; if your outbound IP is in a different region than the target city, add `postal=&lt;zip&gt;&amp;search_distance=&lt;mi&gt;` to the query — the API geo-scopes by IP only when no `postal` is supplied (see the gotcha below). **A residential proxy is not required.** Lead with the API path; the browser path works as a fallback but pays a ~100× cost premium because the search page is fully JS-rendered (`browse snapshot` returns 0 a11y refs and harvesting per-listing URLs costs ~3 turns each).
1. **Pick city + category** (and optionally subarea). City is the Craigslist subdomain (`sfbay`, `newyork`, `losangeles`, `seattle`, ...). Category is the search-path abbreviation (`sss` for-sale-all, `cta` cars+trucks, `apa` apartments, `ggg` for-sale-by-owner, etc.). To scope to a specific subarea (city-within-region), prefix the category in `searchPath` — e.g. `searchPath=sfc/apa` for SF-proper apartments, `searchPath=eby/cta` for East Bay cars. Subarea codes are listed in each response&#x27;s `data.decode.locations[i][2]`. Subarea-scoping is significantly more efficient than fetching region-wide and filtering client-side (e.g. `apa` returns 9,798 bay-wide vs. 253 for `sfc/apa`).
2. **First page**:

GET https://sapi.craigslist.org/web/v8/postings/search/full

?searchPath={cat}

&amp;query={q}

&amp;sort={date|rel|priceasc|pricedsc}

&amp;batch=1-0-360-1-0

&amp;lang=en&amp;cc=us

Referer: https://{city}.[craigslist.org/](http://craigslist.org/)

 Returns JSON with `data.totalResultCount`, `data.items[]`, and decode tables under `data.decode`. Confirm the response is scoped to the right region via `data.areas` (e.g. `{&quot;1&quot;: {&quot;name&quot;: &quot;newyork&quot;}}`) — if it shows the wrong city, add `postal=&lt;zip&gt;&amp;search_distance=&lt;mi&gt;` (any ZIP in the target metro) to override the IP-based geo-scope.
 **Common filter params** (append as query args; check `data.humanReadableParams` to confirm acceptance): `min_price`, `max_price`, `min_bedrooms`, `max_bedrooms`, `min_bathrooms`, `bundleDuplicates=1`, `hasPic=1`, `postal=&lt;zip&gt;`, `search_distance=&lt;mi&gt;`, `availabilityMode=available`, `auto_make_model=&lt;text&gt;`, `min_auto_year`/`max_auto_year`, `min_auto_miles`/`max_auto_miles`. Unrecognized params are silently dropped.
3. **Decode each item**. `data.items[]` is an array of positional arrays. **Critical: many fields are offsets / lookup keys, not absolute values** — always read against `data.decode.*`:  - `item[0]` — `postingIdOffset`. Absolute id = `data.decode.minPostingId + item[0]`.  - `item[1]` — `postedDateOffset` (seconds). Absolute epoch = `data.decode.minPostedDate + item[1]`.  - `item[2]` — `categoryId` (integer). Maps to a 3-letter sub-category abbreviation (`cat3`) used in canonical URLs. The mapping is **not** in the response — it&#x27;s a fixed Craigslist enum. Observed during iter-2 verification: `68 → bik` (bicycles), `93 → spo` (sporting goods), `122 → pts` (parts), `197 → bop` (bicycle parts/accessories). Other categories will need to be back-derived from the `data.decode` block or a click-through verification.  - `item[3]` — price as integer (0 or missing for free items).  - `item[4]` — `&quot;locIdx:hoodDescIdx:hoodIdx~lat~lon&quot;`. Look up `data.decode.locations[locIdx]` → `[1, city, subareaAbbr]`; `data.decode.locationDescriptions[hoodDescIdx]` → display location string; parse `lat~lon` for coordinates.  - **Title** — last array element that is a plain string (i.e. not a tagged `[code, ...]` block). For `cta` (cars+trucks) this is `item[-1]`. For `apa` (apartments) and other housing categories, a trailing `[5, beds, sqft]` housing-meta block pushes the title earlier — iterate from the end and take the first plain string.  - Tagged blocks `[code, value]` mid-array: `code === 5` is `[beds, sqft]` (housing categories); `code === 6` is the URL slug; `code === 10` is the formatted price string (&quot;$1,350&quot;); other codes carry image refs and metadata.
4. **Construct canonical post URL**:

https://{city}.[craigslist.org/{subareaAbbr}/{cat3}/d/{slug}/{postingId}.html](http://craigslist.org/{subareaAbbr}/{cat3}/d/{slug}/{postingId}.html)

 - `postingId` from step 3 (offset + minPostingId)  - `subareaAbbr` from `data.decode.locations[locIdx][2]` (e.g. `nby`, `sby`, `sfc`, `eby`, `pen`)  - `cat3` from the categoryId enum (step 3)  - `slug` from the `[6, ...]` tagged block
 **Wrong `cat3` will 404**. If you don&#x27;t know the mapping for a categoryId, fall back to `https://{city}.craigslist.org/search/{cat}?postingId={postingId}` which redirects to the canonical URL.
5. **Paginate** (only if results &gt; 360):

GET https://sapi.craigslist.org/web/v8/postings/search/batch

?batch=1-{OFFSET}-1080-1-0-{startTs}-{endTs}

&amp;cacheId={cacheId from step 2}

Referer: https://{city}.[craigslist.org/](http://craigslist.org/)

 Increment `OFFSET` in steps of 1080. `startTs`/`endTs` are the `data.cacheTs` and current epoch.
## Site-Specific Gotchas
- **Geo-redirect on bare domain**: `https://www.craigslist.org/` redirects to a city based on the request IP (in our trace, `provo.craigslist.org`). Always open `{city}.craigslist.org` directly. - **API geolocates by request IP — `postal=&lt;zip&gt;&amp;search_distance=&lt;mi&gt;` overrides it**: No auth, no cookies, no anti-bot — but if no `postal` is supplied, the API scopes results to the city corresponding to the request&#x27;s source IP, not the `Referer` header (e.g. a NY query from an SF IP silently returns `{&quot;1&quot;: {&quot;name&quot;: &quot;sfbay&quot;}}` results). Adding `postal=&lt;zip&gt;` for any ZIP in the target metro plus `search_distance=&lt;mi&gt;` forces the result set to that region. Verified 2026-05-01 with direct curl from an SF IP returning correct Chicago (`postal=60601&amp;search_distance=50`, 0.21s, 41 results) and NYC (`postal=10001&amp;search_distance=10`, 2.19s, 475 results) listings. **A residential proxy is not required** — `bb fetch --proxies` *without* `postal` is also geo-locked to sfbay (proxy doesn&#x27;t change the source-IP region for this API), and adding `postal` to a direct curl is ~8× faster than the proxy path (0.21s vs 1.63s on the same Chicago query). Always verify scope via `data.areas` in the response. - **Snapshot returns 0 refs on `/search/`**: The search page is fully JS-rendered. Don&#x27;t use `browse snapshot`/`click` to enumerate listings. - **Compact response format**: `data.items[]` uses positional arrays + `data.decode.*` lookup tables to keep the response small. Don&#x27;t expect named fields per item — decode by position. - **Pagination batch sizes**: First page is ~360 (`batch=1-0-360-1-0`); subsequent batches are 1080 each (`batch=1-OFFSET-1080-1-0`). - **Free items have no price**: `item[3]` may be `0` or absent. - **Posting time precision**: The rendered page shows relative (&quot;&lt; 1 hr ago&quot;); absolute epoch = `data.decode.minPostedDate + item[1]`. - **`item[0]` is NOT the postingId** — it&#x27;s an offset from `data.decode.minPostingId`. Naïvely treating `item[0]` as the postingId produces 404s. - **`data.decode.locations` indexing is per-response, not stable.** Iter-3 saw `locations[1] → [&quot;sfbay&quot;,&quot;sfc&quot;]`; iter-4 saw `locations[1] → [&quot;sfbay&quot;,&quot;eby&quot;]` for the same city/query. The decode block is rebuilt per cache TTL — **always look up `locations[locIdx]` from the response in hand**, never cache or hardcode the table. - **Neighborhood labels are unreliable**: `data.decode.locationDescriptions` varies per response and per category. The same neighborhood may appear under different label-table indices across responses, may be missing in some categories (e.g. &quot;Russian Hill&quot; shows up in `apa` but is absent from `cta` decode tables), and is sometimes replaced by a generic city-level label by the poster. For neighborhood-scoped searches, use **lat/lon bounding-box matching** on `item[4]`&#x27;s coordinates as a fallback or supplement to label-string matching. Example bbox for North Beach + Russian Hill: `lat 37.794–37.810, lon -122.425 to -122.404`. - **Categories are an undocumented enum** — the response decode tables don&#x27;t include the `categoryId → cat3` mapping; observed values across iters: `68→bik, 93→spo, 101→foa, 122→pts, 197→bop, 5→fua` (and likely many more for non-bicycle queries). The redirect URL `https://{city}.craigslist.org/search/{cat}?postingId={id}` is the safest fallback when an unknown categoryId is encountered. - **Rate-limit self-imposed**: No formal block but Craigslist throttles aggre
```

If the agent discovered an undocumented JSON endpoint, that endpoint is in there. If a particular form needs a small wait before submission, that&#x27;s in there too. If a domain-specific helper (`helpers/amazon.py`, `helpers/opentable.py`, `helpers/sf-portal.py`) is worth keeping around, it gets checked in next to the skill.

This is the same shape we use inside `bb`, our internal generalist agent. In our post on [how we build agents at Browserbase](https://x.com/kylejeong/status/2044878529666662616), we wrote about how every internal workflow (feature requests, session investigations, PRs, sales triage) runs through one agent that loads small markdown skills on demand. The general loop stays simple. The domain knowledge lives in skills, where it can be read, edited, versioned, and reused.

**Autobrowse pushes that idea one layer further: the agent writes its own skill, learned by actually doing the task. **

The hand-written skills inside `browse` and the Autobrowse-graduated skills inside the public Browse CLI ecosystem are, importantly, the same kind of artifact. Once a skill exists, nothing about how an agent loads or runs it cares whether a human or another agent wrote it.

### What is it good at?

Autobrowse shines on sites that genuinely require exploration.

- Hidden or undocumented APIs that aren&#x27;t visible from the rendered page but show up in network traffic.
- Heavy client-side rendering, where the &quot;real&quot; content only appears after a sequence of interactions.
- Multi-step login or wizard flows, where the right path isn&#x27;t obvious from the first screen.
- Any UI where the shortest reliable path is non-trivial enough that a human reverse-engineering it would take a couple of hours.
- Token-saving opportunities where parts of the loop are redundant (e.g. skipping `browse screenshot` when the UI isn’t changing meaningfully).

For example, we used Autobrowse to play around with a federal grants portal and surface an undocumented JSON endpoint that returned every current grant in a single call. What looked like a 28-page scrape collapsed into a single `browse fetch`, and that discovery is now baked into the graduated skill so we never have to re-find it.

![](https://cdn.sanity.io/images/yd6zslid/production/649565218c3ff88b9c57ee97e3824c4add02a9cc-800x491.gif?auto=format&amp;h=982&amp;w=1600&amp;fit=min&amp;q=75)

This is the recurring pattern that makes the whole approach worth investing in: **an agent tries something a person never would, and finds something a person would never see.**

### A concrete benchmark: Craigslist

`Traditional Claude Code loop`: ~$0.22, ~71s

`Graduated Autobrowse skill`: ~$0.12, 27s

![](https://cdn.sanity.io/images/yd6zslid/production/d94081b15877dc2bab4d57e83e0cd9aae83a0b57-3456x1362.png?fm=webp&amp;h=631&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

The shape matters more than the absolute numbers. The first run on the site costs about what you&#x27;d expect from a generic agent loop. The end skill changes the unit economics of every subsequent run by an order of magnitude or more, because it encodes the shortest reliable path the agent could find and reuses it instead of re-deriving it.

We see the same shape on smaller tasks. On an early form-fill experiment, cost dropped from $1.40/run to $0.24/run in four iterations, just by letting the agent notice and remove the parts of its own approach that weren&#x27;t pulling weight.

### Where Autobrowse breaks

It would be easy to oversell this. Autobrowse is genuinely strong on a specific shape of problem and genuinely the wrong tool on another. The discipline of not using Autobrowse is part of using it well.

**Autobrowse is not the right tool when the task is deterministic parsing**. We learned this the hard way against a 167-row static HTML state catalog. The data was right there in the markup. No JavaScript, no auth, no anti-bot, just rows.

We threw Autobrowse at it anyway, because the framing of &quot;let the agent figure it out&quot; is seductive. Four iterations and ~$24 later, the loop still hadn&#x27;t returned all 167 rows in a single output. The model&#x27;s per-turn output cap kept truncating its reasoning, and the iteration loop kept trying to be clever about a problem that didn&#x27;t reward cleverness.

Once we recognized the regime mismatch, the agent pivoted to ~200 lines of deterministic Python with `browse fetch` and BeautifulSoup. Sub-second runtime, zero inference cost, all 167 rows surfaced.

The lesson got written into the skill itself:

```
# Step 1: probe with fetch first.
browse fetch &quot;&lt;https://example.gov/programs&gt;&quot;
# If the data comes back cleanly in the response, write the parser.
# If the response is empty / dynamic / gated, escalate to Autobrowse.
```

Browser agents come in different agency levels, from a static script with no LLM in the loop, through router-style and tool-using agents, all the way up to fully autonomous loops that can spawn other agents and define their own tools. Choosing the right level is a real engineering decision.

**Autobrowse sits at the high-agency end of that spectrum, and like any high-agency tool, you reach for it once the cheaper, more deterministic options have given up.**

## Why this changes workflows

A skill operates as a customer handoff, with all the weight that implies.

Today, when an agent succeeds at a job, the customer&#x27;s engineering team gets a trace, maybe a session replay, maybe a paragraph of natural-language reasoning. None of those are legible to the people who actually own the workflow.

A skill is legible. It&#x27;s durable, debuggable, human-auditable, and ownable. An engineer can read it, edit it, and commit it. A non-engineer (a technical PM, a VP of technology, a grants manager who knows their portal inside out) can also read it and roughly understand what the agent is doing without ever touching code.

We go from &quot;just trust the agent&#x27;s output&quot; to &quot;read the agent&#x27;s playbook.&quot; That, in our view, is the thing that makes browser agents robust enough to live inside a serious enterprise workflow rather than awkwardly next to it.

The compounding effect matters too. Each new site an agent encounters yields one more durable skill. The library grows. The agent gets cheaper and faster on the long tail of repetitive workflows because it stops paying the discovery tax.

Autobrowse already functions as a factory for browser-agent capabilities, well beyond what any single agent could ship on its own. A single Autobrowse skill is useful. A growing public directory of them, accessible to anyone running a browser agent, is the actual prize.

### What we&#x27;re working on next

**Smarter stopping **

Right now we cap iterations at a small number and short-circuit when consecutive runs converge in cost and turn count. It&#x27;s a reasonable heuristic, but a blunt one. We&#x27;re letting the agent reason about its own convergence more explicitly, comparing not just cost and turns but the structure of its trace across runs.

Some of Autobrowse&#x27;s most useful wins (like the federal-portal JSON endpoint) come from the agent randomly varying its approach and stumbling onto a much shorter path. We don&#x27;t want to optimize that variance away too aggressively.

**Better priors about how to explore**

We want to make sure the agent reaches for our `fetch` and `search` primitives before spawning a full browser session. A lot of what looks like exploration can be answered with one fetch. For more advanced tasks, it’s reasonable to let the agent inspect browser traces, network events, and CDP logs so it can discover internal APIs by watching network requests rather than guessing at them from the rendered DOM.

**Recursive Autobrowse **

The most exciting direction is recursive: Autobrowse improving Autobrowse. Today the iteration loop, the convergence heuristic, and the skill template are mostly hand-crafted. The same way we use Autobrowse to graduate skills for individual sites, we can use it to graduate improvements to its own harness. Better prompts for the iteration step. Better priors for which primitives to reach for first. Better templates for what the final skill should look like for a given class of task.

### The bigger picture

A dominant story about browser agents right now is that they&#x27;ll get good when the underlying models get good. We&#x27;re one Anthropic or OpenAI release away from agents that just work on the web. We don&#x27;t entirely buy that.

Even a perfect model still has to discover (on every new site) what a perfect model would already know if it had been there before. Without a place to put what the agent learns, every run is a fresh start.

The real bottleneck is memory, in a form humans and agents can both understand and trust.