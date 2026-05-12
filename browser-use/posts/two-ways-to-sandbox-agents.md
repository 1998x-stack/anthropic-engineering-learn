---
title: "How We Built Secure, Scalable Agent Sandbox Infrastructure"
author: "Larsen Cundric"
date: "2026-02-25"
url: "https://browser-use.com/posts/two-ways-to-sandbox-agents"
---

# How We Built Secure, Scalable Agent Sandbox Infrastructure

**Author:** Larsen Cundric
**Date:** 2026-02-25
> From AWS Lambda to Unikraft micro-VMs with a control plane architecture.

---

## How we got here

We run millions of web agents at Browser Use. We started with browser-only agents on AWS Lambda, where each invocation is isolated, scaling is instant, and there are no secrets to worry about.

Then we added code execution. Agents could write and run Python, execute shell commands, create files. We built this as an isolated sandbox the agent called as a tool. Security was fine: the code ran in the sandbox, not on the backend.

But the agent loop still ran on the same backend as our REST API. Redeploy? All running agents die. Memory-hungry agent? The API slows down. Two fundamentally different workloads sharing the same process.

## The two patterns

When an agent can run arbitrary code, it can access anything on the machine: environment variables, API keys, database credentials, internal services. It needs to be isolated from your infrastructure and secrets. There are two ways to do this.

**Pattern 1: Isolate the tool.** The agent runs on your infrastructure. Dangerous operations (code execution, terminal access) run in a separate sandbox. The agent calls the sandbox via HTTP. The code runs somewhere with nothing to leak.

**Pattern 2: Isolate the agent.** The entire agent runs in a sandbox with zero secrets. It talks to the outside world through a control plane that holds all the credentials.

The agent becomes disposable. No secrets to steal, no state to preserve, you can kill it, restart it, scale it independently. The control plane holds the truth.

We started with Pattern 1 and moved to Pattern 2.

## The sandbox

The same container image runs everywhere. In production it runs as a [Unikraft](https://unikraft.cloud/) micro-VM. In local development and evals it runs as a [Docker](https://www.docker.com) container. A single config switch (`sandbox_mode: 'docker' | 'ukc'`) controls which path the provisioning code takes.

### Unikraft in production

Each agent gets its own Unikraft micro-VM, booting in under a second. We provision them via Unikraft Cloud's REST API on dedicated bare metal machines in AWS.

The sandbox receives only three env variables from the outside world: `SESSION_TOKEN`, `CONTROL_PLANE_URL`, and `SESSION_ID`. No AWS keys, no database credentials, no API tokens.

Unikraft gives us scale-to-zero out of the box. When a sandbox is idle, the VM suspends. When the next request comes in, it resumes.

### Docker in development and evals

Locally and in our eval pipelines, the same image runs as a Docker container. Same image, same entrypoint, same control plane protocol.

### Hardening

The sandbox does several things before any agent code runs:

1. **Bytecode-only execution.** During the Docker build we compile all Python source to `.pyc` bytecode, then delete every `.py` file.
2. **Privilege drop.** The entrypoint starts as root, then immediately drops to a `sandbox` user via `setuid`/`setgid`.
3. **Environment stripping.** After reading env vars into Python variables, we delete them from `os.environ`.

## How the control plane works

Think of the control plane as a proxy service. The sandbox has no direct access to the outside world. Every request has to hop through the control plane. Need to call an LLM? Goes through the control plane. Need to upload a file to S3? Goes through the control plane.

It's a stateless FastAPI service. Every request from the sandbox carries a `Bearer: {session_token}` header. The control plane looks up the session by token, validates that it's still active, and executes the operation with real credentials.

### LLM proxying

For each LLM call, the sandbox sends only the new messages. The control plane owns the full conversation history in the database, reconstructs it on each call, and forwards the complete context to the provider.

### File sync via presigned URLs

The sandbox has a `/workspace` directory where the agent reads and writes files. A file sync service watches for changes and periodically syncs them to S3, but the sandbox never sees AWS credentials.

### The gateway protocol

Inside the sandbox, the agent talks to the control plane through a `Gateway` protocol. In production, `ControlPlaneGateway` sends HTTP requests to the control plane. For local development and evals, `DirectGateway` calls the LLM directly and keeps history in memory.

## Scaling

The control plane is stateless: validate the token, do the work, return the result. Need more agents? Spin up more sandboxes. Need more throughput? Add control plane instances behind a load balancer. Each layer scales based on its own bottleneck.

## Wrapping up

There are two ways to sandbox an agent that can execute code. You can isolate the tool (run code execution in a sandbox, keep the agent on your backend) or isolate the agent (put the entire agent in a sandbox, talk to the outside world through a control plane).

We went with Pattern 2. The key takeaway: your agent should have nothing worth stealing and nothing worth preserving.
