---
title: "ReactEval: Building LLM Benchmark for Frontend"
author: "Tereza Tizkova"
date: "2024-03-18"
url: "https://e2b.dev/blog/reacteval-building-llm-benchmark-for-frontend"
category: "ai-agents"
site: "e2b"
---

James Murdza created [GitWit](https://gitwit.dev/), an AI-powered online editor for creating React applications. To be able to evaluate the LLM agents within GitWit, James is building [ReactEval](https://github.com/gitwitorg/react-eval), one of the first LLM benchmarks for frontend. We talked about how he automates executing hundreds of runs for each test, how ReactEval helps in building better products, and his view on the AI space.

## Journey to creating GitWit and ReactEval

I started working on GitWit about one year ago. Back then, code generation with LLMs was fairly new. The initial idea was to make programming new applications as easy as possible, particularly for less experienced developers. I focused on things that were really difficult for developers - like managing dependencies or finding working boilerplate code - and built GitWit to automate such tasks using AI.

Since then, GitWit has evolved to a visual editor that allows you to make frontend React applications using AI.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679792aa03428f27ffbec481_6797922334eba1d2f0018e43_DjD3tz3NKlE3HkLHXgh6IAErOls.gif)

ReactEval solves a problem that we came across while building GitWit. Figuring out how well an LLM agent is doing at solving a particular task is an ongoing problem for a lot of people, that there haven't been a lot of great solutions for. Very early on OpenAI created something called [HumanEval](https://github.com/openai/human-eval) which tests GPT on solving Python problems. But that was three years ago and in the meantime, the use cases for code generation have become much more advanced.

I realized that the problem I was solving with GitWit generating React JavaScript code wasn't so unique so I wanted to create a common open-source framework where people could measure what they're doing both internally and then externally to compare different models and agents. And we use [E2B](/docs) for building ReactEval.
Before we make a deep dive into ReactEval, what was the journey to GitWit? From what I understand, today, GitWit is an online tool to build web apps while augmenting your own coding skills with AI. How did the product evolve towards this in the last few months?

We started building an AI agent that you would feed with a single prompt like “Make me a NextJS app with Stripe integration that sells shirts” or something like that, and then the agent would try and come up with a code repository. It would try and create all the files needed for the whole application.

That was the first product that got a lot of usage, but it's just so difficult to solve the general software development use case, and I also realized that the longer the agent is running autonomously, the less the human can actually do to contribute with their own skills. 

That’s why we pivoted to building an editor that gives you a live preview of the application you're building. In this case, the goal is to make the code generation run as fast as possible, allowing a human user to give their input as soon as the generation is finished. We're trying to create this natural development process that doesn't feel like you're ever waiting for the AI to finish anything.
So you moved toward more frequent iteration with the human instead of waiting for the AI to make everything from scratch…

Yes, in the previous version, you would be waiting for a few minutes for the AI agent to generate the whole app. Now, you're generally waiting for the agent to produce around a hundred lines of code, which takes around 10 seconds making GitWit faster than for example [Vercel’s V0](https://v0.dev/). And in the upcoming version, it will be even faster.
How do I, as an end user, start using GitWit?

You just visit [GitWit.dev](https://gitwit.dev/) and you can immediately create a new app without even signing in. Then you have a working app, which you can just edit there with the code inputs. Then you can use AI prompts that make twists in the app and can rewrite it - for the prompting feature you have to sign up.

That is pretty exciting! What is on your roadmap currently?

One thing that we're working on right now, and we're about to release is a version where the AI can handle multiple files initially to simplify things for the editor.

Now we just use the AI to edit one file at a time which works really well, but we are going to allow it now to refactor into multiple files. That means let's say you want. to build an app where you make a header, make a photo, make a sidebar at a map at a list view, … Then the AI will automatically split those components up into different files, which can then be reused. The idea is that you would just directly connect it to make your apps, but right now you can just click a button and then it gives you the whole source code as a zip file.

## Running browser tests in sandboxes

When you want to do LLM benchmarking, where things get difficult is when you try to evaluate an LLM, which is by nature non-deterministic, so it's not just enough to run a couple of tests. I need to run the same test at least ten times in order to see if a certain if the LLM is even working well on a certain task.

For example, if I hypothetically want to make sure that GitWit is really good at adding a button (which it *is* good at by the way), I can perform ten tests, and get the same result nine times, but one time it doesn’t work. If I had just done five tests, maybe I wouldn't have gotten this important piece of information. 

That just shows we need to perform hundreds of tests to achieve a good level of confidence. Every time we make a change, we need to test the app a hundred times to confirm that it is still performing the right way. 

To summarize, I now need to run hundreds of runs in each test, and during the runs, I actually have to build a React application, run it in a web browser, and then observe if there are any errors. To do this manually would take me hours. 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679792aa03428f27ffbec47b_6797923d62300cbe810c68f1_kGOyuHQjwZldiOxgZPhfNqCZsvY.webp)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679792aa03428f27ffbec484_6797924a585820c87ebccb09_yArXLSjzDC7LF3VJVJb0q2juRc.avif)
How do you then automate the tests in ReactEval to be able to run that many tests and not spend a whole day by that?

To automate all these processes we use [E2B sandboxes](/docs) for the code execution in a web browser. It's very lightweight. In particular, we use a [custom sandbox](/docs/sandbox/templates/overview) - its job is to build a React JavaScript application, open it in a browser, and then check for any errors. Each run within each test has its own separate sandbox instance.

When performing these tests, I just run the sandbox a hundred times with each code that I want to test, and then record the results so we can put together a report of errors and analyze what caused them.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679792aa03428f27ffbec492_6797926c62300cbe810c970c_acg38clkLkrsoX3yqKlXwlS5Q.gif)
What types of errors are you usually getting when running the tests?

There are two kinds of error messages.

Either you receive an exit code in case you get a standard error from the testing process itself, for example, if the app fails to build because of a TypeScript error.

Another type of error is the one in the JavaScript console. Once the app builds and runs in the browser using Puppeteer, then you may still get errors while the app is running.

During the tests, we record both kinds of errors, but we check mainly the errors that come out of the browser because the most frustrating part with GitWit is when it generates some code that causes an error in the browser. It happens a significant amount of the time using GPT because it has limited knowledge. GPT performs very well at coding but it knows very little about what things are compatible with each other so it might install two different packages that are just completely not compatible with each other, so the code can look completely fine, but the program still doesn’t run in the end.
What were other difficulties you encountered when finding the optimal solution for running the tests?

The most challenging part of the whole process was setting up computing resources for the evaluation process. Before trying E2B I experimented with [AWS](https://aws.amazon.com/), but I'm not an expert in AWS so this took me a lot of time.

E2B sandbox turned out to be a lot easier than using AWS, specifically for quickly creating a container and accessing the filesystem.
Can you describe in more detail what is happening with the sandbox and how its features help with running the tests?

The benefit of using the sandbox for performing a test is that we can simply copy a base project and don't have to reinstall everything for React from scratch.

Our big goal is to make it faster to install everything in the sandbox from the beginning. The sandbox works just like a Docker container that has Puppeteer and Chrome in it. When we want to run a test, we open the sandbox and rewrite the template code inside.

The sandbox we spawn already has our template for a blank React app inside, and this template gets modified before we start running the test. The sandbox allows us to perform operations and change files inside it, so we change the application code, build the application, and then run it in a browser.

## Comparison of LLMs

Everyone is anticipating the new GPT and the models get better and better at reasoning. How do you think the new LLMS will impact what you’re building?

OpenAI team has said that they will never let GPT get as outdated again as it is now. However, there is a trade-off between being up-to-date and speed. If you look at GPT-4, it is almost three times smaller than GPT-3.

We use ReactEval to demonstrate this trade-off for LLMs and solve questions like how much one LLM is slower, given it has 20% better performance than another LLM. For example, if one wants to switch to Mistral, we can evaluate the pros and cons and quantify the performance when we run it through ReactEval.

We are planning to soon publish results of how well the different LMS compare for producing React code.
So, the users can switch between LLMs, based on the tests performed by ReactEval. What are other actionable things to do, based on your findings from the tests?

Yes, as a very fundamental thing, you can switch models, but you can also do anything else imaginable to improve your app.

For example, you can implement retrieval augmented generation (RAG) and add context to your prompts with documentation from different libraries. We can measure whether that's improving your project, or having no effect, how big the effect is, or how the performance changes compared to let’s say two weeks ago.

The main improvement that we've made so far is with dependencies, which is a really annoying problem for many developers. No model is trained on a hundred percent up-to-date data, they all have a cut-off date, but we allow the models to use any newer packages than the date that they were trained on. That means we need to figure out what versions the models are referencing and install the right versions, which the model itself doesn’t know (that's a scary thing). 

## Open-sourcing the product

You are using ReactEval to improve your product - GitWit. Are you offering ReactEval to other companies to use?

Yes, we're working with one other company in the same space right now to enable them to do the same thing we're doing. It's very easy, just a few lines of code that need to be changed to get ReactEval to work for their products. We want to offer what we built with ReactEval to other companies in the space as well. I think collaboration would just be a win for everyone.
You built quite an impressive product with ReactEval. How do you communicate the advantages of evaluating LLMs and LLM-powered apps to your users?

The downside of working with text prompts is that users don't know the full scope of what they can do with the product. We have to record a lot of demos to show people what's even possible with ReactEval.  

I made some videos where we explained what was going on in the code - this is helping a lot of people to understand all of the hard work that needs to go on before you have something that “magically” works. The demos brought more companies that we hadn’t heard about before to collaborate with us.
Sounds good! What’s your next step with ReactEval now?

I think showing the product in demo videos is still not enough, so now we are open-sourcing our code generation algorithms because it's a long journey and we're going to need a lot of people working together.
How frontend-specific is your solution? In general, what are other approaches to the evaluation of LLMs and LLM apps?

One option is to analyze users’ historical data. We don't have thousands of users using it every day, so this approach wouldn’t work for us. Another approach is creating an evaluation platform where you can manage the data of the evaluation.

For us, the hard part of the process isn't the data management, but the problem that we solved with the [E2B sandbox](/docs). Which is, how can we build and test hundreds of React applications in 10 minutes because, for example, my own computer wouldn't have enough RAM to do that.

We just need to run hundreds of apps in the browser and the rest of the process is mostly just storing the results in JSON files or database, which is a piece of cake compared to that. 

Note that what we're doing is very specific to this frontend generation, and it won't apply to other areas very much.

### Discover more

- [GitWit - webpage](https://gitwit.dev/)
- [ReactEval - GitHub](https://github.com/gitwitorg/react-eval)
- [James Murdza - X (Twitter) profile](https://twitter.com/jamesmurdza)
- [GitWit - X (Twitter) profile](https://twitter.com/GitWitDev)