---
title: "Python Guide: Run OpenAI Codex in an E2B Sandbox"
author: "Tereza Tizkova"
date: "2025-08-25"
url: "https://e2b.dev/blog/python-guide-run-openai-codex-in-an-e2b-sandbox"
category: "integrations"
site: "e2b"
---

OpenAI Codex turns natural-language instructions into code edits and files. Run it inside an **E2B Sandbox** and you get an isolated, long-running environment where the agent can safely create files, install tools, and execute without interactive prompts.

## **What we’ll build**

- Spin up an E2B sandbox from the **prebuilt openai-codex template**.

- Inject your **OpenAI API key** into the sandbox.

- Run a Codex prompt that creates a Hello World file.

- Print the output and shut the sandbox down.

#### See [full example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/openai-codex-in-sandbox-python) in the E2B Cookbook.

## **Components we’ll use**

- **E2B Python SDK** – creates and controls the sandbox.

- **Prebuilt template**: openai-codex – Codex CLI is preinstalled.

- **OpenAI API** – used by Codex via OPENAI_API_KEY.

## **Prerequisites**

- **Python 3.11+**[‍](/dashboard)
- [E2B account](/dashboard) + [`E2B_API_KEY`](/dashboard/keys)

## **Outline**

- Create the project
- Add the files (pyproject.toml, main.py)
- Set E2B_API_KEY in .env
- Install with pip and run

## **1) Create the project**

```
`mkdir openai-codex-in-sandbox-python
cd openai-codex-in-sandbox-python
mkdir -p src/openai_codex_in_sandbox_python`
```

Create and commit `.gitignore` before `.env` so secrets never enter git history.

Target structure:

```
`openai-codex-in-sandbox-python/
├─ src/
│  └─ openai_codex_in_sandbox_python/
│     └─ main.py
├─ pyproject.toml
├─ .gitignore
└─ .env`
```

## **2) Files to add**

#### **File: `pyproject.toml`**

```
`[project]
name = "openai-codex-in-sandbox-python"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "e2b",
    "python-dotenv",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"`
```

#### **File: `src/openai_codex_in_sandbox_python/main.py`**

This script loads `.env` (so the SDK sees `E2B_API_KEY`), creates the sandbox from the `openai-codex` template while injecting your OpenAI key, runs a Codex exec prompt that generates index.html, prints the result, and then shuts the sandbox down.

Load configuration and SDK:

```
`from dotenv import load_dotenv
from e2b import Sandbox

load_dotenv()`
```

Create the sandbox (OpenAI key passed inline) and log its ID:

```
`template_name = 'openai-codex'
sbx = Sandbox(
    template_name,
    envs={
        "OPENAI_API_KEY": "<your api key>",
    },
    timeout=60 * 5,  # 5 minutes; match README (remove this line to match the file exactly)
)
print("Sandbox created", sbx.sandbox_id)`
```

Run a Codex prompt that creates a file (no per-command timeout):

```
`# Print help for Codex
# result = sbx.commands.run('codex --help', request_timeout=0, timeout=0)
# print(result.stdout)

# Run a prompt with Codex
result = sbx.commands.run(
    "codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox 'Create a hello world index.html'",
    timeout=0,
)
print(result.stdout)`
```

Clean up:

```
`sbx.kill()`
```

#### **File: `.gitignore`**

```
`.venv/
.env
__pycache__/
*.pyc`
```

#### **File: `.env`**

```
`E2B_API_KEY="YOUR_E2B_API_KEY"`
```

## **3) Set up and install**

```
`python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -e .`
```

## **4) Run the example**

```
`python src/openai_codex_in_sandbox_python/main.py`
```

**Expected:** console output from Codex. The generated index.html lives inside the sandbox filesystem.

#### See [full example](https://github.com/e2b-dev/e2b-cookbook/tree/main/examples/openai-codex-in-sandbox-python) in the E2B Cookbook.