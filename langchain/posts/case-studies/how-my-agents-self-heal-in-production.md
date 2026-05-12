---
title: "How My Agents Self-Heal in Production"
author: "LangChain Accounts"
date: "2026-04-03"
url: "https://www.langchain.com/blog/how-my-agents-self-heal-in-production"
---

Open Source

# How My Agents Self-Heal in Production

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ce47650a7400dec1de7_vishnu-suresh.png)Vishnu SureshApril 3, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)6min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b5962d9b8e037eaadc1_68.webp)*By Vishnu Suresh, Software Engineer @ LangChain*

*This blog was initially published *[***on X***](https://x.com/vishsuresh_/status/2039748786290037038?ref=blog.langchain.com)*.*

I built a self-healing deployment pipeline for our [**GTM Agent**](https://x.com/LangChain/status/2031055593360990358?ref=blog.langchain.com). After every deploy, it detects regressions, triages whether the change caused them, and kicks off an agent to open a PR with a fix.

With coding agents, the hard part of shipping isn&#x27;t getting code out. It&#x27;s everything after: figuring out if your last deploy broke something, investigating what caused the issue, and fixing it before users notice. I wanted to deploy, move on, and trust that if something regressed, the system would catch it and close the loop itself.

## How the Self-Healing Flow Works

The GTM Agent is built on [**Deep Agents**](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com) and deploys through [**LangSmith Deployments**](https://www.langchain.com/langsmith/deployment?ref=blog.langchain.com). We already had an internal coding agent called [**Open SWE**](https://x.com/LangChain/status/2033959303766512006?ref=blog.langchain.com), an open-source async coding agent that can research a codebase, write fixes, and open PRs. The missing piece was automated regression detection and triage to connect production errors back to Open SWE.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b988a0b947a48e8de49_self-healing-flow.png)

Right after a deployment to production, a self-healing GitHub Action triggers, capturing the build and server logs. The flow has two paths: (1) catching build failures immediately and (2) detecting server-side regressions over a window. If either path finds a real issue, Open SWE gets kicked off to fix it and open a PR.

### Catching Docker Build Failures

First, I check the build logs to make sure the Docker images build properly. If the image fails to build, the pipeline automatically pipes the error logs from the CLI, fetches the git diff from the last commit to main, and hands it off to Open SWE, no human involved. Build failures are almost always caused by the most recent change, so a narrow diff gives Open SWE enough context to act on.

### Monitoring for Post-Deploy Errors

Server-side issues are trickier than build failures. A production system carries a background error rate—network timeouts, third-party API issues, transient failures, etc. In an ideal world you&#x27;d track and fix every single one, but when trying to answer &quot;did my last deploy break something,&quot; you need to separate the errors your change caused from the noise that was already there. That&#x27;s what this step does.

First, I collect a baseline of all error logs from the past 7 days. These get normalized into error signatures, regex replaces UUIDs, timestamps, and long numeric strings, then truncates to 200 characters, so logically identical errors get bucketed together even when the specifics differ.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b998a0b947a48e8de4f_error-logs-grouped-signatures.png)

Next, I poll for errors from the current revision over a 60-minute window after deployment, normalizing the same way. Once that window closes, I have error counts from two very different time scales, a week of baseline data and an hour of post-deployment data. While I could naively compare these two numbers to detect if our latest change caused an error, I wanted to take a more principled approach (and brush up on my probability distributions 🙃).

### Gating with a Poisson Test

A Poisson distribution models how many times an event occurs in a fixed interval, given a known average rate (λ) and the assumption that events are independent:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b988a0b947a48e8de46_Screenshot-2026-04-03-at-1.39.31---PM.png)

Baseline production errors fit a Poisson model reasonably well. Using the 7-day baseline, I estimate the expected error rate per hour for each error signature, then scale it to the 60-minute post-deployment window. If the observed count significantly exceeds what the distribution predicts (*p &lt; 0.05*), I flag it as a potential regression. For error signatures that are completely new (not present in the baseline at all), I flag them if they occur repeatedly in the monitoring window.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b998a0b947a48e8de52_poisson-test.png)

But server errors aren&#x27;t always independent. Correlated failures from traffic spikes or API outages can violate the independence assumption, and a statistical test alone can&#x27;t distinguish &quot;this error spiked because of our code change&quot; from &quot;this error spiked because a third-party API went down.&quot; That&#x27;s where the triage agent comes in.

### The Triage Agent

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d77b998a0b947a48e8de4c_triage-agent.png)

Rather than feeding errors directly into Open SWE (which is tempted to make changes), I add another gating mechanism. The diffs from the last commit and the specific error get passed into a triage agent (built on Deep Agents).

First, the triage agent classifies every changed file as runtime, prompt/config, test, docs, CI, etc. If a change only touches non-runtime files, it&#x27;s extremely unlikely the deployment caused the error. This prevents false positives where the agent might hallucinate a causal chain from a test file to a production bug.

For runtime changes, the agent must establish a concrete causal link between a specific line in the diff and the observed error.

The agent returns a structured verdict with its decision, confidence, reasoning, and the error signatures it attributes to the change. This narrowing means Open SWE receives a focused investigation prompt rather than a dump of every error that spiked.

### Closing the Loop with Open SWE

Once the triage agent green-lights an investigation, Open SWE takes over, works through the bug, and opens a PR. I get notified when it&#x27;s ready for review, so the entire flow from error detection to proposed fix happens without any manual intervention.

So far, it&#x27;s been most useful for catching bugs that don&#x27;t crash loudly: silent failures that return wrong defaults, configuration mismatches between code and deployment, and cascading regressions where fixing one bug unmasks the next on the subsequent deploy.

## Future Improvements

### Wider Lookback Window

The triage agent currently looks at the difference between the current and previous version. Bugs introduced in earlier versions that only surface later won&#x27;t get auto-attributed. Widening the look back is an obvious fix, but the more diffs you feed into the triage agent, the noisier the signal gets and the harder it is to pinpoint a causal link. I haven&#x27;t landed on the right balance yet.

### Smarter Error Grouping

The current approach uses fuzzy matching by sanitizing IDs and timestamps from error messages. It took some time to get right, and there are probably still cases where related errors don&#x27;t get grouped together due to limitations in the sanitization logic.

One idea I&#x27;ve been considering is embedding error messages into a vector space and clustering them, rather than relying on regex normalization. Errors that mean the same thing would naturally land near each other regardless of surface-level differences, and I could detect regressions by monitoring for new clusters forming or existing clusters growing after a deploy. The challenge is tuning distance thresholds for what constitutes a meaningful cluster shift versus normal variance.

Another option is using a smaller model (likely open source) to classify and group errors, then pass those structured clusters directly to Open SWE as part of the investigation prompt, giving it a much richer picture of what&#x27;s failing and how the full error looks.

All of these approaches improve grouping after errors happen. Ramp took an interesting approach that works the other way around, defining what to watch for before errors happen. To make their [**Sheets product self-maintaining**](https://x.com/RampLabs/status/2036165188899012655?ref=blog.langchain.com), on every PR merge an LLM reads the diff and generates monitors tailored to the changed code, each with explicit thresholds for error rate spikes, latency regressions, etc. When a monitor fires, a webhook delivers the alert context directly to an agent for triage. Defining a targeted monitor upfront produces a much clearer signal, making it easier for a downstream agent to diagnose the issue.

### Fix-Forward vs Looking Back

Right now the system always fixes forward, Open SWE works on a PR while the broken deployment stays live. A smarter approach would be deciding between the two based on severity, error rate, and triage confidence. A high-severity spike with a low-confidence causal chain might warrant an immediate rollback, while a well-attributed bug with a clear fix path is better handled by pushing a patch forward.

## The Loop as Default

The pattern is simple: deploy, monitor, triage, and fix—automatically in a loop. I built this for a single agent deployment, but it generalizes to any service that deploys code. Every deployment has the same problem. Something breaks, someone has to notice, someone has to fix it. The more of that loop you automate, the more engineering time shifts from reacting to building. Systems get more resilient because the feedback loop between breaking and fixing approaches zero.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e127982faf6124b586b6e4_82.png)Agent ArchitectureDeep AgentsOpen Source

#### Running Subagents in the Background

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12735c02bb07c894a067a_hunter-lovell.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e12775881c2a7fc9aba41e_colin-francis.png)Hunter LovellColin FrancisApril 16, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/running-subagents-in-the-background)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)