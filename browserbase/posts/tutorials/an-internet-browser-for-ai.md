---
title: "An Internet Browser for AI"
author: "Paul Klein"
date: "2023-12-01"
url: "https://www.browserbase.com/blog/an-internet-browser-for-ai"
category: "tutorials"
site: "browserbase"
---

December 01, 2023

# An Internet Browser for AI

![](https://cdn.sanity.io/images/yd6zslid/production/92ccd19d7aa2bb46f8c3b3da11a94ac50ba10f95-498x502.png?fm=webp&amp;h=1613&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

By Paul Klein

[Engineering](/blog/engineering/)

![](https://cdn.sanity.io/images/yd6zslid/production/9b071753cad93ecade27ab35084c4cd6006980d5-2568x1737.png?fm=webp&amp;h=1082&amp;w=1600&amp;auto=format&amp;fit=min&amp;q=75)

## The story so far

After thirty years, the web browser remains the default way we interact with new software. Humans are visual creatures, and the graphical user interface is the simplest way for people to operate online tools. There have been many innovations to improve the website-building process, accelerating the creation of new websites to meet consumer demand. But what if the majority of website consumers aren’t people, but other computers?

[According to Cloudflare](https://www.cloudflare.com/learning/bots/what-is-bot-traffic/#:~:text=According%20to%20various%20sources%2C%20bots,traffic%20coming%20to%20their%20sites), over 40% of all internet traffic comprises of other computers (aka bots). Since the internet is filled with information, these dutiful bots search and extract the best pieces — a process called scraping. Bots scrape data because there often isn’t a public API available to help them to consume it in a structured way. They have to consume data the same way we do: navigating a website.

Large language models (LLMs) such as GPT-4 are trained using data collected from all over the internet. To continue training and updating these models, fresh data needs to be scraped.

Furthermore, some promising implementations of LLMs have demonstrated their ability to [complete tasks autonomously](//https://github.com/Significant-Gravitas/AutoGPT). These new types of bots, known as *Web Agents*, will use the same websites that we do to complete tasks on our behalf. Imagine your own AI assistant starting a chat session on [United.com](http://United.com) to rebook your flight. In a world where API integrations aren’t available, websites emerge as the primary gateway for data access and interaction.

The preeminence of internet bots, continued demand for scraping, and the rise of web agents begs the question: **How are developers building automation for parsing data on the internet?**

## The problem: Scraping isn’t easy

**The beauty in web scraping is the simplicity of a naive approach and the depth of a robust solution.** When you ask a developer to fetch data from a website, they’ll often mimic web browsers and make a simple HTTP request for the URL.

`curl https://www.airbnb.com`

This simple command fetches data from [Airbnb.com](http://Airbnb.com), with a few caveats.

- Modern websites don’t load everything in the first request, which requires you to wait for scripts on the page to “hydrate” the relevant data. To run these scripts, you’ll need to simulate a web browser so the scripts can access the browser APIs they need to function.

![](https://framerusercontent.com/images/p7jYuq0dvs8M3nFN1RBEdXPCywc.png)
- Sometimes the data you want isn’t accessible by a public URL, and page navigation is required to get to where you need to go. A “click” or “type” event may need to be triggered on the page. You need some automation of page interaction.

![](https://framerusercontent.com/images/WKawPU1n50xgJqY8qnco5Z0dBQ.png)
- Some websites detect scraping and block it with interaction or CAPTCHA checks. These checks are hard to bypass and involve impersonating a browser by sending specific headers with your request.

![](https://framerusercontent.com/images/koKGSoyzuD1PX2GsxPrJKYVibE.png)
- Once you can access the website, you’ll need to parse the data. With modern web development, this is easier said than done. The structure of these pages is unpredictable, often containing unfriendly labels that change every time the developer compiles the page.

![](https://framerusercontent.com/images/oxO8ho95sHfFGZrUyzncesQ2CH8.png)
- These challenges make it nearly impossible for developers to build scraping workflows with their built-in tools. Surprisingly, the best tool is something they use every day — a web browser.

![](https://framerusercontent.com/images/692TtUY4MIiHgfKgAJxf1GxSDzA.png)

## An imperfect solution: A (programmable) browser

A programmable web browser is different from a regular web browser in that it’s “headless,” meaning that it’s operated completely using code. Rather than a GUI rendering in a window, it’s all happening in memory. **This is because computers can only read**, not see, so they don’t need to render the pages on screen while they scrape the data.

There are a few popular libraries for programmable browsers. Puppeteer (made by Google) and Playwright (made by Microsoft) are the two dominant solutions. They offer comprehensive access to the browser APIs and are widely adopted in the ecosystem for a variety of use cases.

![](https://framerusercontent.com/images/uoGbPORQC7wrRd0SEy4dWVtAA.png)

The primary method programmers use to interact with websites in a headless browser is a CSS selector. As you can see in the above example, selectors are used to determine what is visible on the screen, where to type, and what to click on. These selectors don’t have types, so you don’t benefit from any of the compile-time advantages of modern programming languages. Defining these flows is tedious because they are brittle. Structure can change at a moment’s notice and everything you’ve built will break. If any step happens out of order, the whole process halts. One of the best ways to determine if a page is done loading is to wait for network requests to stop, a paradigm that results in… a lot of waiting.

Outside of the language complexities, the library itself is bloated. Puppeteer installs 282MB of dependencies on Linux, which is gigantic! For reference, the maximum deployment size of an AWS Lambda is 250 MB (meaning you have to use a complex workaround). This factor isn’t unique to Puppeteer, as Playwright has the same issue.

![](https://framerusercontent.com/images/i7NbTwtUdmWRGhAErCKjjYaFL8Q.png)

These large dependencies are a direct result of the fact that Puppeteer requires a whole web browser to run, packaging additional functionalities that your code will never need. With the exception of emojis… you’ll need to install those separately.

As a reminder, these are *the most popular* headless browser libraries. Despite being at the core of massive workflows, they still have rough edges that make building with them no fun.

![](https://framerusercontent.com/images/hWZtU3696neCTfr0bIzo4iyI4Mw.png)

**Who is making browser automation fun?**

## Browser automation is already an AI primitive

Large language models (LLMs) have a limited set of knowledge based on their training data, and AI applications often leverage browsers to fill the gaps. There are two main techniques for accomplishing this.

One method is Retrieval Augmented Generation (RAG). Applications fetch information using a browser and add that information in the prompt with an LLM. The additional context helps the LLM provide a better response.

![](https://framerusercontent.com/images/f8iy2vQW0RTXGTHWhTmaP0LEelM.png)

Another technique is the Plugins/Web Agents paradigm. An application exposes an interface for an LLM to call upon, i.e. a web browser. If a task given to the LLM requires interfacing with the internet, the LLM will use the browser interface autonomously, navigating between pages and parsing the results until it satisfactorily handles the task provided by the user.

![](https://framerusercontent.com/images/MRSPwbf34nyCbNVY7XmgwL8AGU.png)

Outside of ChatGPT, existing LLM orchestration frameworks have already built hooks for browser automation. Langchain, the predominant AI app framework, offers a Web Browser plugin that uses the naive scraping approach I described earlier. There’s also an integration with Browserless (covered later) for more robust data collection use cases.

In his recent YouTube video, Andrej Karpathy, a famous AI researcher working at OpenAI, described the not-so-distant future of an LLM operating system. In this diagram, you can see that the browser is a core primitive of an LLM, along with the file system and embeddings/vector databases. To me, this is the clearest declaration of the importance of the browser for LLMs, especially as their ability to use tools increases over time.

![](https://framerusercontent.com/images/SOXv6u8Okimf7RCFNlJ3lYQt7Q.png)

## A big market that’s about to get bigger

The existing scraping and browser automation market is sizable. When looking at download numbers via NPM, the Puppeteer library has grown as much as Next.JS, a very popular web framework maintained by Vercel.

![](https://framerusercontent.com/images/mGsvzNRcGoTPZ5eduhzpzgbkW14.png)

A public company to compare with is UiPath. They develop software for Robotic Process Automation (RPA) that helps automate routine business tasks. UiPath is on track to exceed $1 billion in revenue this year — a great example of the massive market available for task automation with AI. However, their browser automation tools are less inspirational.

Existing startups in the space showcase logos from F500 companies, which demonstrates an appetite for enterprise adoption.

![](https://framerusercontent.com/images/fuU4P4iRWajQl03tW0otddlD5Kc.png)

Finally, several major tailwinds will drive the adoption of browser automation tools.

- Developers are training new foundational models that require data scraping in massive quantities.
- Data owners (Wikipedia, Reddit, StackOverflow) want to capture the value of their data, which will make scraping more complex and require more robust browser automation tools.
- A new category of software businesses will automate interaction with websites on the user’s behalf using Web Agents. This will either be a feature or a major focus of their product.
- Existing SaaS businesses may add AI features that depend on browser automation to function.
- Many legacy websites won’t offer sufficient APIs for AI consumption, which means browser automation will be required for the long tail of websites.

## Existing players

Compared to vector databases, the browser primitive is underfunded by venture capital. The majority of existing companies are bootstrapped or have raised less than $5 million. Most of the companies that *have* raised significant funds don’t cater to the developer audience building these applications.

I’ll break down the startups into three categories: browser automation, scraping APIs, and information retrieval APIs.

#### **Browser Automation**

The following are generalist browser automation startups that are building a horizontal platform.

- **Browserless**
Browserless is the closest to an incumbent in the space, with good market penetration and brand recognition among developers.
- Its infrastructure is essentially remote Puppeteer and focuses on innovating at the infrastructure level as opposed to the SDK level.
- It has a small team that recently sold to an emerging buyout fund.

- [**Browse.ai**](http://Browse.ai)
This startup is venture-backed but more consumer/low-code.
- Their “Website to API” feature is really interesting.

- [**Induced.ai**](http://Induced.ai)
This startup is venture-backed ($2.3 million seed) but focused on enterprise RPA/prosumer.

#### **Scraping APIs**

All of these APIs are pretty similar — give a URL and get mostly unstructured data back. They often bundle other features alongside the core scraping features, such as CAPTCHA bypass or proxies.

- ScrapingBee
- WebScrapingAPI
- ScraperAPI

#### **Information Retrieval APIs**

These startups are more oriented toward specialized information search and retrieval rather than generalized browser automation.

- Metaphor Systems
- SerpAPI

A best-in-class startup should draw inspiration from each of these categories. Right now, it doesn’t appear that any one incumbent is dominating. The biggest competitors are likely developers DIYing their own implementations.

## Building a better browser

The world deserves a 10x better browser automation platform.

Allow me to recap the problems I identified earlier:

- Existing libraries are bloated and not optimized for performance.
- Deployments to modern cloud environments are complicated.
- The language for building integrations results in brittle applications that break often.
- Scripts often depend on waiting for steps to function with arbitrary timeouts.
- Parsing data from a page is a painstaking process of trial and error.

To simplify further, developers desire a better-performing, more reliable, and easier-to-use product than the one that currently exists.

Jarred Sumner built Bun because he believed that developers had an appetite for a new, 10x better Javascript runtime. And he was right!

After reading through dozens of comments from developers, including some that I’ve mentioned in this memo, it’s clear that developers want a better browser automation platform.

There are three key innovations that can unlock a 10x better, cloud-native, AI-first browser automation platform.

- **Build an open-source, highly-optimized headless browser for the community.**a. Cold start times and bloated dependencies shouldn’t exist in 2023.
- **Give the browser superpowers using AI.**a. Instead of forcing developers to build complex parsing trees, use LLMs to reliably find the information they need within the page, even if the structure has changed.b. Or use GPT-4V to identify objects using screenshots instead of code parsing.c. This unlocks the ability for developers to ask questions like “Has the page completely loaded yet?” or “Can you see the login button?” with zero tricks.d. And allows for access to obfuscated information. Sometimes, websites hide critical information like prices in images instead of text to prevent scrapers from accessing it.e. There have already been some experiments with similar implementations.
- **Offer new interfaces at a different abstraction level that delights developers.**a. Rewrite the SDK from first-principles. Developers find the procedural nature of the current approach makes forking and retrying complex.Maintaining the familiar Puppeteer interface would also be necessary to support migrations.b. Allow developers to take advantage of the new “AI-native” innovations. Sometimes it might be too heavy handed to use AI when tradition methods will do just fine. Developers should be able to choose what makes sense for their use-case.c. Build a great API to manage the infrastructure these browsers run on and delight customers.

## Distribution

> “The battle between every startup and incumbent comes down to whether the startup gets distribution before the incumbent gets innovation.” –Alex Rampell @ a16z

Even if the innovations above are exactly right, they’re nothing without a strong go-to-market motion. As they say, “First-time founders are obsessed with product. Second-time founders are obsessed with distribution.”

![](https://framerusercontent.com/images/1B2flDKUDtYxBeGQX6EBrD0nes.png)

The most effective distribution levers for a developer tools product are as follows

- Make a best-in-class product
- Invest in the community via open source
- Build a trusted brand
- Educate and enable developers

Most importantly, the product needs to be exceptional. Putting lipstick on a pig — or a pretty landing page on a waitlist — won’t create the foundational change needed to capture the massive opportunity that’s out there.

Investing in the community means giving back, especially when you take. Existing browser libraries are open source, and this one should be as well. Open source is a great distribution lever, and it’s much easier to give away great software for free and then convince someone to try your paid offering after seeing what your team is capable of.

The importance of creating an established brand in the developer tools community cannot be overstated. I’d argue that it’s almost as important as offering the best product. Word of mouth is by far the strongest channel for developer tools companies, followed by organic search.

Meeting developers where they are is a crucial part of converting customers through the funnel. If you’re spending a ton of time acquiring developers, but not putting in the effort to educate them with great docs or make things easier with SDKs in their language, why bother? These investments contribute to word-of-mouth referral, and there’s no higher compliment than “Wow, have you seen this startup’s docs?”

Because existing browser automation flows break all the time (as explained earlier), there’s ample opportunity to capture developers while they’re dealing with the pain of fixing their previously working code. This is a rare scenario for developer tools, which are often “set it and forget it” integrations.

A trusted brand with an engaged developer community is a reinforcing moat, especially as developers contribute to the open-core product. The best way to avoid becoming a commodity is by becoming the default choice for new developers in the space, and the open source project is crucial for that.

Because the majority of revenue will come from the top 20% of the market (this is almost always the case for developer tools), a bottoms-up GTM motion functions mostly to establish stronger word of mouth, which unlocks enterprise inbound for future revenue.

Finally, there are ample opportunities for expansion as the core business succeeds. Some examples include bundling scraped data storage and exposing a query API, supporting persistence for users to enable faster task completion, or a community marketplace for commonly implemented workflows (i.e. buying specialized screws from McMaster-Carr).

While I’m a bigger fan of the horizontal platform, there’s a world where becoming a unified data API for legacy data providers captures value in the short term, allowing automation flows that wouldn’t otherwise exist to be built directly on top of the platform.

## Risk Areas

Startups are always hard. For any new startup entering this space, there are a few risk areas that particularly stand out. I’ll do my best to offer mitigation strategies or counter-arguments to these common concerns.

- **Risk**: It’s hard to become the default choice in an established market.
**Strategy**: Disrupt a market with a new paradigm to allow startups to segment the market and carve out space to break in.
- **Example**: Heroku (Incumbent) vs Vercel (Challenger), Mailgun (Incumbent) vs Resend (Challenger)

- **Risk**: Browser Automation might be too central to a customer’s core product offering, creating a reluctance to outsource.
**Counter**: If the feature is important enough with sufficient complexity, customers would be crazy to build it on their own.
- This is a classic build vs buy risk.

- **Risk**: LLM Inference cost makes any use case prohibitively expensive.
**Counter:** Inference cost will likely decrease over time.
- **Strategy**: Make LLM features opt-in to allow customers to have more pricing control and enable the product to serve a wider variety of use cases.

- **Risk**: This is a commodity infra product with race-to-the-bottom margins.
**Strategy**: Consider innovating on pricing if possible. Instead of paying for sessions, you can potentially charge for throughput.
- Remember the consequences of being COGs.

- **Risk**: Abuse/Legality
**Counter**: As of 2022 and according to the U.S. Ninth Circuit of Appeals, web scraping is legal.
- Innovations in AI make abuse detection 100x easier.

- **Risk:** What if X builds this? (OpenAI, Google, Etc)
**Counter:** Fundamentally, LLMs cannot ship with a browser because it’s a separate technology. It’s unlikely that OpenAI will bundle it with the GPT API, as that would introduce additional complexity (billing or otherwise) into the API.
- Even if OpenAI bundles it, there will be many applications for which developers will need bespoke configurations.
- The “personal assistant” use case will likely be dominated by Apple or Google, and they will build integrations with the most commonly-used services.
- But the long tail of SMBs that we interact with on a daily basis (i.e. your corner bakery or barber) won’t offer an API for personal assistant integration, and browser automation will need to be used instead.

- **Risk:** Is this a venture scale opportunity?
Yes, certainly.

## In Summary

We’re going to be scraping websites for a long time.

The internet is nondeterministic, but we’re using deterministic tools to navigate it.

Browser automation is an under invested-in primitive that AI applications will depend on for years to come.

There’s an opportunity for a great startup to disrupt a market that has plenty of AI and non-AI use cases.

The right founder to build this likely has deep experience with headless browsers, developer tools, and a passion for AI.

![](https://framerusercontent.com/images/L4S8UNxzN2Rg8vaHZIfYWlOa9A.png)

> Originally published on November 30, 2023 [here.](https://memos.hawkhill.ventures/p/an-internet-browser-for-ai)