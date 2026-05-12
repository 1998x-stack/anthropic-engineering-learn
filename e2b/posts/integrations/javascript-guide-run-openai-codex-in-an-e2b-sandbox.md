---
title: "JavaScript Guide: Run OpenAI Codex in an E2B Sandbox"
author: "Tereza Tizkova"
date: "2025-08-25"
url: "https://e2b.dev/blog/javascript-guide-run-openai-codex-in-an-e2b-sandbox"
category: "integrations"
site: "e2b"
---

OpenAI Codex turns natural-language instructions into code edits and files. Run it inside an **E2B Sandbox** and you get an isolated, long-running environment where the agent can safely create files, install tools, and execute without interactive prompts.

## **What we’ll build**

- Spin up an E2B sandbox from the **prebuilt openai-codex template**.

- Inject your [**OpenAI API key**](https://platform.openai.com/api-keys) into the sandbox.

- Run a Codex prompt that creates a Hello World file.

- Print the output and shut the sandbox down.

#### See [full example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/openai-codex-in-sandbox-js) in the E2B Cookbook.

## **Components we’ll use**

- **E2B JS SDK** – creates and controls the sandbox.

- **Prebuilt template:** openai-codex – Codex CLI is preinstalled.

- **`dotenv`** – loads [`E2B_API_KEY `](/dashboard/keys)from `.env`.

## **Prerequisites**

- **Node.js 18+**[‍](/dashboard)
- [E2B account](/dashboard) + [`E2B_API_KEY`**‍**](/dashboard/keys)
- [**OpenAI API key**](/dashboard/keys)

## **Outline**

- Create the project
- Add the files (package.json, src/index.ts)
- Set `E2B_API_KEY` in `.env`
- Install and run

## **1) Create the project**

```
`mkdir openai-codex-in-sandbox-js
cd openai-codex-in-sandbox-js
mkdir -p src`
```

Create and commit **.gitignore before .env** so secrets never enter git history.

Target structure:

```
`openai-codex-in-sandbox-js/
├─ src/
│  └─ index.ts
├─ package.json
├─ .gitignore
└─ .env`
```

## **2) Files to add**

### **File: `package.json`**

```
`{
  "name": "openai-codex-in-sandbox",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "tsx src/index.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "dotenv": "^16.5.0",
    "e2b": "^1.4.0",
    "tsx": "^4.19.4"
  }
}`
```

### **File: `.gitignore`**

```
`.env
node_modules/`
```

### **File: `.env`**

```
`E2B_API_KEY="YOUR_E2B_API_KEY"`
```

### **File: `src/index.ts`**

**This script loads .env (so the SDK sees E2B_API_KEY), creates the sandbox from the openai-codex template while injecting your OpenAI key, runs a Codex exec prompt that generates index.html, prints the result, and then shuts the sandbox down.**

Load configuration and SDK:

```
`import { Sandbox } from 'e2b'
import dotenv from 'dotenv'

dotenv.config()`
```

Create the sandbox (OpenAI key passed inline) and log its ID:

```
`const templateName = 'openai-codex'
const sbx = await Sandbox.create(templateName, {
  envs: {
    OPENAI_API_KEY: '<your api key>',
  },
})

console.log('Sandbox created', sbx.sandboxId)`
```

Run a Codex prompt that creates a file (no per-command timeout):

```
`// Print help for Codex
// const result = await sbx.commands.run('codex --help')
// console.log(result.stdout)

// Run a prompt with Codex
const result = await sbx.commands.run(
  `codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox "Create a hello world index.html"`,
  { timeoutMs: 0 }
)

console.log(result.stdout)`
```

Clean up:

```
`sbx.kill()`
```

## **3) Install & run**

```
`npm install
npm run start`
```

**Expected:** console output from Codex. The generated index.html lives inside the sandbox filesystem.

#### See [full example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/openai-codex-in-sandbox-js) in the E2B Cookbook.