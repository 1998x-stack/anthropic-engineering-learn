---
title: "Battle of AI coding tools"
author: "Tereza Tizkova"
date: "2023-09-22"
url: "https://e2b.dev/blog/github-copilot-vs-cursor-so-vs-aide-battle-of-ai-coding-tools"
category: "integrations"
site: "e2b"
---

There has been a boom of AI-powered coding tools, like [GitHub Copilot](https://github.com/features/copilot), [Sweep](https://sweep.dev/), [GPT Engineer](https://github.com/AntonOsika/gpt-engineer), [codium](https://www.codium.ai/), or [Open Interpreter](https://openinterpreter.com/) recently trending on global GitHub. They have been a big topic, as people are trying to test as many of them as possible.

I compared the more established GitHub Copilot with two newly launched AI coding copilots, [Cursor](https://www.cursor.so/) and [Aide](https://codestory.ai/), both built as a modification of [VSCode](https://code.visualstudio.com/).

They all intend to make the developer experience easier, are compatible with Windows, MacOS, and Linux, and offer writing, suggesting, debugging, and explaining of code. I compared their features and tested each of them in multiple “categories” on a simple programming task.

### GitHub Copilot

[Copilot](https://github.com/features/copilot) is a two-year-old tool created by Microsoft-backed OpenAI. It has been trained on a selection of English language and source code from publicly available sources, including code in public repositories on GitHub.

### Cursor

[Cursor](https://www.cursor.so/) by Anyspehere is an AI-powered code editor that recently gained [big popularity](https://github.com/getcursor/cursor). The IDE is a fork of VSCode, it can generate code from scratch, ask questions about your codebase, edit code with prompts, debug the code, or explain it. Cursor is currently being developed by a small team and is described by them as an “[attempt at a new way to write code](https://anysphere.co/).

### Aide

[Codestory](https://codestory.ai/) is a YC23 startup, that is a few months old, and the team consists of just two people. Their product, Aide, is an AI-first IDE, currently in the alpha stage, and only supporting JS/TS projects, however already used regularly.

Aide founders realize that SW development is not just about writing code, but also debugging, refactoring, testing, reviewing code, and planning for new features. For example, “Aide agent can invoke to do multi-file edits,” says Sandeep Pani, the CEO of Codestory.

## Comparison

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf072a_67962f9418e0637fe5a0bed4_AEIDEM48pRUUmetQAxAiT1js7E.avif)

**Links**

- Companies: [GitHub](https://github.com/about), [Anysphere](https://anysphere.co/), [Codestory](https://www.ycombinator.com/launches/JCn-codestory-is-an-ai-powered-mod-of-vscode)
- Founders' Linkedin profiles: [Sualeh A.](https://www.linkedin.com/company/anysphere/people/), [Michael T.](https://www.linkedin.com/in/michael-t-5b1bbb122/), [Arvid Lunnemark](https://www.linkedin.com/in/arvid-lunnemark/), [Aman Sanger](https://www.linkedin.com/in/aman-sanger-482243171/), [Sandeep Pani](https://www.linkedin.com/in/sandeep-kumar-pani/), [Naresh Ramesh](https://www.linkedin.com/in/naresh-ramesh/)

I tested each of the tools with GPT-4, and compared them across the following categories:

- How easy they are to set up
- How well they generate code from scratch
- How they suggest code
- Ability to edit
- Debugging
- Code explanation
- Support and communication

Since I am not a full-time developer, I chose a beginner-level program to test the tools on. I created a simple version of a [Blackjack](https://pi.math.cornell.edu/~mec/2006-2007/Probability/Blackjack.htm) card game, where a player decides whether to “hit” (take more cards) or “stand” (skip taking more cards) and then competes with a dealer in getting the sum of their card values closer to 21, without exceeding it.

You can check out the files with code written by myself, Copilot, Cursor, and Aide, in my public [Blackjack repository](https://github.com/tizkovatereza/Blackjack).

## 1. Setting up

First, I looked at how easy it is to install these tools and get them running. All three tools were quick to set up and I started using them almost immediately.

### GitHub Copilot

You can [set up Copilot ](https://docs.github.com/en/copilot/getting-started-with-github-copilot)via JetBrains IDEs, Vim/Neovim, VS, or VSCode, which was my choice. Before you can start using GitHub Copilot, you will need to set up a free trial or subscription for your personal account. You can then enable Copilot on your GitHub or install it as a VSCode extension. I struggled a bit with installation, for example, it took me some time to allow the Chat feature, which was in the pre-released version.

### Cursor

Cursor is downloadable from the [landing page](https://www.cursor.so/). Their UI is almost identical to VSCode. The time between installing and starting to use Cursor was really short for me, compared to the other two. 

### Aide

You can download Aide directly from their [landing page](https://codestory.ai/) or ensure the latest version from the [releases page](https://github.com/codestoryai/binaries/releases).

[Installation](https://codestory.ai/) is easy.

- Open a JS/TS project folder.
- Press Cmd + Shift + P to open the command palette and search for Import settings and keybindings from VSCode. Hit enter to run the command. For this command to work, I first had to sign up to GitHub via Aide and clone my GitHub repo for this command to work.

Aide supports importing all your settings and extensions from VSCode.

### 🥇Winner: Aide

**Reasoning**: I found setting it up the smoothest and liked the structure of their documentation that includes a comprehensive step-by-step guide, and also limitations, given the very early product. I struggled to find Cursor’s docs and to set up all Copilot’s features quickly.

## 2. Code generation

Next, I compared, what the tools provide on my prompt. I used variations of “Please write an interactive blackjack card game program.”

### GitHub Copilot

To access the code-writing feature of Copilot, you need to enable the pre-released version of the product in the VSCode. Once enabled, you can use the chat feature to input prompts and receive code. This feature is not yet available in the released version.

The code generated was satisfactory and fully functional. I was able to run it and play a simple version of the game.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d7e386bc2c61cf0777_67962fd7e386bc2c61cd6b20_H5qjhaw22VCt90LJF5nvi69Jsk.webp)

### Cursor

In Cursor, you have two basic options to communicate with the Agent. 

- Command K lets you edit the highlighted code or ask anything about it.
- Command L opens a chat interface.

I used the latter to generate the entire codebase based on my prompt. However, when I tried generating a Blackjack game, it failed to complete the task to my satisfaction - the provided code doesn't provide an interactive card game when run.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d7e386bc2c61cf0774_67962ff2bc55a4988972692e_uG3xeKkZB8NkHrgfnAlydcrN6E.gif)

### Aide

The Aide agent is incapable of generating code from scratch. Instead, it relies on the code uploaded by the user, searching through the existing codebase for the desired results, as shown in the image.

I asked Sandeep Pani, the CEO of Codestory, about Aide’s ability to generate code. “Aide does not know how to generate code from scratch today,” says Sandeep. “We do think there exists a workflow where code generation from scratch becomes important (e.g., if you are working with a new library or API) and plan to add support for it in the upcoming weeks.”

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0701_6796300b6b224941ce08ef13_fGZOC097ADdPSLIqaKuqaEg.avif)

### 🥇 Winner: Copilot

**Reasoning**: Cursor provided non-functional code, and Aide doesn’t have yet the feature of code generation.

## 3. Code completion

GitHub CopilotRegarding suggesting code, GitHub Copilot managed to create my desired program basically from scratch by suggesting smaller code snippets correctly. It can suggest for example entire functions or methods. I was pleasantly surprised that it copied my style of coding, putting an explanation comment behind every piece of code.For each suggestion, you can pick from (usually) 1-2 options, by switching the suggested snippets with arrows. If you use chat to make the Copilot agent finalize the whole program at once, it will do it.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0710_679630320ad59049d727175e_KKvQPIlopStceYzkocy2mC89OhM.avif)

The only drawback is that the Copilot can get into an infinite loop of suggestions.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0739_67963045e8badf4a70e6b1b4_L4pyBWtnpQxwuVqnhBzMuaFk5Cc.avif)

### Cursor

Cursor managed to complete the blackjack game code. The code it produced as a completion was not an interactive game, but just a mechanism of blackjack that runs automatically.

However, the Cursor agent realized this drawback when asked (it explained that “In the current implementation, the player automatically draws cards until their score is 21 or higher, which isn't how a typical game of Blackjack is played.)” and suggested a modification of a play method in the code to make it interactive.

I appreciate how the agent communicates one step beyond just providing an answer and suggests improvements proactively.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf070c_6796305cbe89e417b2a64773_rtZ7Tzmd8RYXthxKS7gMYNNJzFE.avif)

### Aide

I asked Aide to complete a JS blackjack code. It first searched through my codebase and provided a few queries and selected files to use (image 1).

It took a longer time to complete the code, compared to Copilot and Cursor. It seemed like Aide tried to improve the existing codebase solution it found by suggesting new code snippets to add (images 2, 3).

I often came across the error “Code modification generation failure.” 

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0706_67963072b0176fefe3c7ed4b_SY3zVYizgXXzaTouBcpc9Aa46w.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf071e_679630859cf5e7cf02871511_QhIrbh7UH3ZpMnFueWYQCdMYBcA.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0727_6796309472fda3c1fd1b7a1f_o9QlyaqtjPQxIzyBh8rIrZ9dVDo.avif)

### 🥇 Winner: Copilot

**Reasoning**: The Copilot agent suggests code in smaller parts and offers multiple versions, which helps me, as a beginner programmer, to get insight into the process. It provided the correct solution on the first try.

## 4. Code editing

### Copilot

The Copilot agent easily edits the chosen code. This feature is working even without the pre-released version.

However, it didn't finish my task to put a comment to each line of code, which it did only partially.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf073c_679630b6b490aadf620ada5e_lW32p8Q3g6fYh7jru1MnbcmAN7I.avif)

### Cursor

Cursor edited my code correctly.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf072d_679630cb6b224941ce09ab48_M6uR8WSxYdov1YCsNwFQwG6NrD4.avif)

### Aide

Aide isn’t able to edit code right now.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0713_679630dee8badf4a70e73bee_mi9OSmz8fbNQ2x18xeCwaigtwj8.avif)

### 🥇 Winner: Cursor

**Reasoning**: The Cursor agent was the only one that completed the given task of editing code.

## 5. Code debugging

CopilotCopilot managed to identify and fix all the bugs that I created in the Python code, and I had no objection.CursorCursor debugging made me confused.I made some errors for Cursor, plus I expected it to fix the bugs the agent itself made when generating the code.It didn’t manage to do any of that, and the code wasn’t functioning even after debugging.On the other hand, Cursor sometimes debugged even the correct parts by adding redundant code, e.g., adding a card to a player’s score by re-writing the variable, even though the card was already added there before by .append.

### Aide

For Aide, I appreciated that it not only suggested a proper fix, but also explained my bug in the chat interface.

I struggled to find an option to highlight and debug particular code snippets. Sometimes it doesn't react correctly on debugging (image 2).

However, I still value the error explanation, instead of just suggesting improvements.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0721_6796310879f5325b87405226_uqI04KJPHNyWsnJfVUh67CgQ6OE.avif)

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0709_6796311a093cf1f94c3489c5_ZdS8VUCLjRyBkPTuPIWkGsrMNw.avif)

### 🥇 Winner: Copilot

**Reasoning**: Copilot provided the most reliable debugging, even though it was simple and didn’t explain the bugs.

## 6. Code explanation

I fed Copilot and Cursor agents with my version of the blackjack game python code, so I could benchmark the explanation on the identical program. For Aide, I use the JS version.

### Copilot

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0724_6796313b79f5325b87407eb0_f9s7qGLTF083L0Vj2u2EzXMcBM.avif)

### Cursor

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0749_6796314e1ee23d2cdce2fb17_rMHTAKO91NdXUuDmc18nxIpC34.avif)

### Aide

I failed to ask Aide to explain my code. When I asked to explain the highlighted code, it wrote what mistakes it contained, instead of explaining the structure. 

### 🥇 Winner: Cursor

**Reasoning**:  Cursor provides an explanation with higher granularity, and refers to particular parts of code while it also provides more complex comments on the code, including a high-level description.

## 7. Support & Communication

This category is equally important to me as the technical features.CopilotGitHub Copilot already gained thousands of users, so it is no wonder that they don’t offer any quick support. I think the only way to get support is via the official [GitHub support](https://support.github.com/) page.CursorI contacted Cursor on their contact e-mail, asking a few questions. I have been waiting for their response for few days now.AideAide answered my e-mail until the second day. They provided lengthy answers to my questions and were nice. Also, I appreciate that Aide agents showed me the links for Discord and e-mail support.

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0716_67963179be89e417b2a7616e_lcn7d7CfV1KzeQlR9GYtoaUcgU.avif)

### 🥇 Winner: Aide

**Reasoning:** They were responsive and willing to help.

## Conclusion

It is difficult to state one winner. From my view as a beginner programmer, I would use each of the three tools occasionally for help in the specific areas they work for.

Given the early stage of Cursor and Aide, GitHub Copilot indeed feels more like a mature product. However, each has its pros and cons.

#### Overall, these were my biggest struggles with each tool:

- **Copilot**: Setting up the chat, price (no free option)
- **Cursor**: Doing too much work at one time, but with not a great quality
- **Aide**: Knowing how to control it (e.g. how to refer to a particular code when chatting about it), and frequent error messages that I didn’t understand

#### Overall, these were the biggest strengths I see in each tool:

- **Copilot: **The suggestions for code snippets
- **Cursor**: Intuitive UI, generating entire codebase from scratch
- **Aide**: Explanations during debugging code, support, price

![](https://cdn.prod.website-files.com/6731db4b7372e95e7d18a926/679631d6e386bc2c61cf0736_6796319806642054bfef4a14_JUzUQQKAtoiMt6CqdtD2DAdAuM.avif)

**Disclaimer: **This review is highly subjective, and your experience may differ by the type of your work, seniority level, or purpose of using the tools. If you have any comments on this comparison, please contact me at tereza@e2b.dev

#### More reading and listening on the coding tools

- [More open or closed-source agent-powered coding tools](https://github.com/e2b-dev/awesome-ai-agents)
- [Latent space podcast about Cursor with a founder of Anysphere](https://www.latent.space/p/cursor#details)
- [Introducing GitHub Copilot X - a leveled-up Copilot](https://github.com/features/preview/copilot-x)