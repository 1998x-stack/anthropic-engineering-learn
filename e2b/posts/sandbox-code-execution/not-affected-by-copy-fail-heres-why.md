---
title: "E2B Sandboxes Aren't Affected by Copy Fail (CVE-2026-31431). Here's why."
author: "Tomas Srnka"
date: "2026-04-30"
url: "https://e2b.dev/blog/not-affected-by-copy-fail-heres-why"
category: "sandbox-code-execution"
site: "e2b"
---

Theori disclosed CVE-2026-31431 yesterday. A 732-byte PoC Python script. Deterministic root on essentially every Linux system shipped since 2017. If you run untrusted code, this is the kind of bug worth stopping for.

**E2B sandboxes are not affected. By design.**

## Background

`algif_aead` is a kernel module that exposes the crypto API to userspace via `AF_ALG` sockets. A 2017 in-place optimization let page cache pages land in a writable scatterlist during AEAD operations. Combined with `splice()`, an unprivileged process gets a deterministic 4-byte write into the kernel's page cache, the in-memory copy of any file the system reads.

Aim those 4 bytes at `/usr/bin/su`. Run `su`. You're root.

- **Deterministic.**
- **Invisible.** Corruption only exists in memory. Disk forensics show the original file.

Theori named Kubernetes clusters, CI runners, and "cloud SaaS running user code" as priority targets for patches. That last category covers **most** sandbox-as-a-service providers.

## Why E2B is not affected.

**The module isn't compiled in.** We build custom minimal kernels for agent sandboxes. These run code interpreters, drive browsers and CLIs, power RL rollouts, and host long-running agents. `CONFIG_CRYPTO_USER` and `CONFIG_CRYPTO_USER_API_AEAD` have never been enabled, cause they're not needed by AI agents.

```
`# CONFIG_CRYPTO_USER is not set
# CONFIG_CRYPTO_USER_API_AEAD is not set`
```

`‍`Fewer features mean fewer places for vulnerabilities.

## If your sandbox provider runs on containers

Ask them three questions today:

- Have you patched every host kernel?
- What was your exposure window?
- Could one tenant have written into another tenant's page cache before the patch?

## What you should do

Patch to mainline `a664bf3d603d`. Ubuntu 26.04 (Resolute) and later are unaffected.

If you can't patch immediately:

```
`echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null || true`
```

Container platforms running untrusted workloads: block `AF_ALG` socket creation with seccomp even after patching. Almost nothing legitimate uses it.

Security and isolation won't affect 99% of your day-to-day. The 1% when it does affect you outweighs the other 99% combined. The reason we chose VM-based architecture is that 1%.

‍