---
title: "Introducing Build System 2.0"
author: "Jakub Dobry"
date: "2025-10-16"
url: "https://e2b.dev/blog/introducing-build-system-2-0"
category: "announcements"
site: "e2b"
---

We’ve released **E2B Build System 2.0** — a faster and simpler way to create custom sandboxes in E2B.

With the new system you don’t need Dockerfiles, extra config files, or manual CLI build commands. You just write code. The build step still exists, but it runs automatically when you execute your template.

## **Why we rebuilt it**

The old build system was functional, but:

- Required juggling config files, Dockerfiles, and CLI commands.
- Builds were slow, mostly local, and debugging was painful.
- Hard to expose or extend build logic for your own users.

Build System 2.0 addresses these problems head-on.

## **What’s new**

### **1. Better Developer Experience**

- **Before:** e2b template build + config + Dockerfile
- **Now:** Just run your code → the template builds automatically/

What previously took a config file, a Docker file, and running a terminal command is now just running a script with a few lines of code. This enables type hints, linters, dynamic builds inside apps, and exposing build logic directly to users.

**Javascript: **

```
`Template()
  .fromImage("node:24")
  .copy("src/", ".")
  .runCmd("npm install")
`
```

**Python:**

```
`Template()
  .from_image("node:24")
  .copy("src/", ".")
  .run_cmd("npm install")
`
```

### **2. Agentic Experience**

Templates are now expressed as code, so AI IDEs and agents like Cursor or Claude Codecan parse, suggest, and generate them without extra config.
This makes it straightforward to plug the build system into an LLM as a tool.

### **3. Speed**

- Intelligent caching
- Parallel uploads
- Server-side optimizations

Builds are **up to 14× faster** when cached, and ~2× faster without cache.
They now run on E2B infra — making the feedback loops shorter, performance more stable, and have clearer error messages.

### **4. Painless Migration**

We kept backwards compatibility and added multiple migration paths:

- `e2b template migrate` (CLI)`‍`
- `Template().fromDockerfile()/Template(path).from_dockerfile(path)` → parses your Dockerfile`‍`
- `fromImage(tag)/from_image(tag)` → continue building from an existing base image

## **Helper Methods**

The API now includes helpers for common tasks such as:

**JavaScript**

```
`Template()
  .fromUbuntu("24.04")
  .pipInstall(["numpy", "pandas"])
  .aptInstall(["curl", "wget"])
  .gitClone("https://github.com/user/repo.git", { branch: "main" })
  .setEnvs({ DEBUG: "true" })
  .runCmd("npm start")
`
```

**Python**

```
`Template()
  .from_ubuntu("24.04")
  .pip_install(["numpy", "pandas"])
  .apt_install(["curl", "wget"])
  .git_clone("https://github.com/user/repo.git", branch="main")
  .set_envs({ DEBUG: "true" })
  .run_cmd("npm start")
`
```

## **Get Started with Build System 2.0**

If you’re on the latest E2B SDK, you already have Build System 2.0. Here’s how to try it out:

### **1. Install or update the SDK**

Make sure you’re on the newest version:

**JavaScript**

`npm install e2b@latest`

**Python**

`pip install --upgrade e2b`

### **2. Create a simple template**

Define your build directly in code:

**JavaScript**

```
`import { Template, waitForPort } from "e2b"

const template = Template()
  .fromImage("node:24")
  .copy("src/", ".")
  .runCmd("npm install")
  .setStartCmd("npm start", waitForPort(3000))
`
```

**Python**

```
`from e2b import Template, wait_for_port

template = (
    Template()
    .from_image("python:3.11")
    .pip_install(["requests", "numpy"])
    .copy("app.py", ".")
    .run_cmd("python app.py", wait_for_port(3000))
)
`
```

### **3. Build the template**

The build step is automatic — just run code:

**JavaScript**

```
`await Template.build(template, {
  alias: "my-template",
  onBuildLogs: defaultBuildLogger(),
})
`
```

**Python**

```
`Template.build(template, alias="my-template", on_build_logs=default_build_logger())`
```

### **4. Run your sandbox**

Once the template is built, launch a sandbox from it:

**JavaScript**

```
`import { Sandbox } from "e2b"

const sandbox = await Sandbox.create("my-template")
const result = await sandbox.commands.run("echo Hello E2B")
console.log(result.output)
`
```

**Python**

```
`from e2b import Sandbox

sandbox = Sandbox.create("my-template")
result = sandbox.commands.run("echo Hello E2B")
print(result.output)
`
```

### **5. Migrating existing templates**

If you already have templates built with the old system, you can migrate:

`e2b template migrate`

Or update your code with:

**JavaScript**

`Template().fromDockerfile("./e2b.Dockerfile")`

**Python**

`Template().from_dockerfile("./e2b.Dockerfile").`

### **Resources**

- [E2B documentation](/docs)
- [Template migration guide docs](/docs/template/migration-v2)