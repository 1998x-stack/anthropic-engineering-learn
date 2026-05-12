---
title: "Announcing LangChainJS Support for Multiple JS Environments"
author: "LangChain Accounts"
date: "2023-04-11"
url: "https://www.langchain.com/blog/js-envs"
---

Company AnnouncementsLangChainOpen Source

# Announcing LangChainJS Support for Multiple JS Environments

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 11, 2023![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb240c7d72dc333a9d0f8_photo-1543285198-3af15c4592ce.jpeg)**TLDR: **We&#x27;re announcing support for running [LangChain.js](https://github.com/hwchase17/langchainjs?ref=blog.langchain.com) in browsers, [Cloudflare Workers](https://workers.cloudflare.com/?ref=blog.langchain.com), [Vercel/Next.js](https://nextjs.org/?ref=blog.langchain.com), [Deno](https://deno.com/runtime?ref=blog.langchain.com), [Supabase Edge Functions](https://supabase.com/edge-functions?ref=blog.langchain.com), alongside existing support for Node.js ESM and CJS. See install/upgrade [docs](https://js.langchain.com/docs/getting-started/install?ref=blog.langchain.com) and **breaking changes **[**list**](#).

## Context

Originally we designed LangChain.js to run in [Node.js](https://nodejs.org/en?ref=blog.langchain.com), which is the longstanding serverside JavaScript runtime. Back in February (time flies!) we started to [collect feedback](https://github.com/hwchase17/langchainjs/discussions/152?ref=blog.langchain.com) from the community on what other JS runtimes we should support, and have since received tons of requests for getting LangChain running on browsers, [Deno](https://deno.com/runtime?ref=blog.langchain.com), [Cloudflare Workers](https://workers.cloudflare.com/?ref=blog.langchain.com), [Vercel/Next.js](https://nextjs.org/?ref=blog.langchain.com), [Vite](https://vitejs.dev/?ref=blog.langchain.com), [Supabase Edge Functions](https://supabase.com/edge-functions?ref=blog.langchain.com), etc.

## Changes to Enable Multiple Environments

We&#x27;ve been on a journey since, together with community contributors, to enable support for as many JS environments as possible, some highlights along the way

- converted our codebase to ESM [here](https://github.com/hwchase17/langchainjs/pull/124?ref=blog.langchain.com) (CJS users don&#x27;t have to worry we offer a CJS build too)
- removed usage of node-only APIs where possible [here](https://github.com/hwchase17/langchainjs/pull/97?ref=blog.langchain.com) and [here](https://github.com/hwchase17/langchainjs/pull/213?ref=blog.langchain.com)
- converted streaming and batch OpenAI requests to use `fetch` [here](https://github.com/hwchase17/langchainjs/pull/118?ref=blog.langchain.com) and [here](https://github.com/hwchase17/langchainjs/pull/526?ref=blog.langchain.com)
- worked with the folks at Replicate to convert their SDK to use `fetch`
- created packages that test importing LangChain in all the runtimes we support, see [here](https://github.com/hwchase17/langchainjs/blob/main/docker-compose.yml?ref=blog.langchain.com)
- and finally we have updated our exports to better support optional dependencies and produce smaller bundles, [here](https://github.com/hwchase17/langchainjs/pull/632?ref=blog.langchain.com)

At the beginning we designed the library so that you&#x27;d do use it like this

`import { LLMChain } from &quot;langchain/chains&quot;;
import { PromptTemplate } from &quot;langchain/prompts&quot;;
import { OpenAI } from &quot;langchain/llms&quot;;
import { SupabaseVectorStore } from &quot;langchain/vectorstores&quot;;
import { CohereEmbeddings } from &quot;langchain/embeddings&quot;;
import { GithubRepoLoader } from &quot;langchain/document_loaders&quot;;`

The old way

But that posed a few problems when running outside of Node.js

- In order to support the growing AI ecosystem we add new integrations all the time, but we don&#x27;t want the install size of the library to grow unbounded. Therefore we make third-party SDKs optional dependencies of `langchain`. While that works fine in Node.js, in browsers and other environments where code is bundled, it ends up being a pretty poor experience, with some of the many bundlers out there needing either some custom configuration by the user, or asking the user to install all optional dependencies.
- When code is bundled, developers worry rightly about bundle size, and because not all bundlers support tree-shaking out-of-the-box, users of LangChain would end up with larger code bundles than they expected.

Not anymore! We&#x27;ve reworked how we expose third-party integrations, and the above code now becomes

`import { LLMChain } from &quot;langchain/chains&quot;;
import { PromptTemplate } from &quot;langchain/prompts&quot;;
import { OpenAI } from &quot;langchain/llms/openai&quot;;
import { SupabaseVectorStore } from &quot;langchain/vectorstores/supabase&quot;;
import { CohereEmbeddings } from &quot;langchain/embeddings/openai&quot;;
import { GithubRepoLoader } from &quot;langchain/document_loaders/web/github&quot;;`

This ensures you don&#x27;t pull in code you&#x27;re not using, and no bundlers choke on optional dependencies like before. Modules like `chains` and `prompts` that contain no third-party integrations remain as before.

Check out the install docs for more information on [how to upgrade](https://js.langchain.com/docs/getting-started/install?ref=blog.langchain.com).

### Breaking Changes

We had to make a few breaking changes to enable supporting multiple environments. These are limited to:

- `import { Calculator } from &quot;langchain/tools&quot;;` moved to `import { Calculator } from &quot;langchain/tools/calculator&quot;;`
- `import { loadLLM } from &quot;langchain/llms&quot;;` moved to `import { loadLLM } from &quot;langchain/llms/load&quot;;` and same for all other load* functions

**Deprecations**

- We now require more granular imports for all 3rd-party integrations (i.e. changing `import {OpenAI} from &quot;langchain/llms&quot;;` to `import {OpenAI} from &quot;langchain/llms/openai&quot;;`. However, the old imports are still left around but deprecated. Please transition your code to use the new imports soon, as we plan to phase out the old imports!

## Testing

Finally, a bit on how we test this to ensure we don&#x27;t break compatibility with any environment in the future. For each new environment we want to support

- created a `test-exports-*` package in our monorepo containing a starter project created with that environment&#x27;s tooling. eg. for Next.js with `npx create-next-app@latest`
- added some example usage of LangChain into that test package
- setup the package so that it contains both `build` and `test` scripts
- added to the list of packages tested in isolated docker containers in CI [here](https://github.com/hwchase17/langchainjs/blob/main/docker-compose.yml?ref=blog.langchain.com).
- finally fix whatever issues come up, ensuring it doesn&#x27;t break any other environments

If we&#x27;re not testing with your favorite environment yet, we&#x27;re very open to PRs that add more environments to be tested. Please let us know if you run into any issues running LangChain.js in a particular environment – we&#x27;d love to help!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)