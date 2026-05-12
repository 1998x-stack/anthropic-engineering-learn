---
title: "How to Authenticate AI Web Agents"
author: "Laith Weinberger"
date: "2026-03-08"
url: "https://browser-use.com/posts/web-agent-authentication"
---

# How to Authenticate AI Web Agents

**Author:** Laith Weinberger
**Date:** 2026-03-08
> A comprehensive guide to logging AI web agents into your accounts — from syncing browser profiles to handling 2FA codes.

---

AI web agents can browse the web, click buttons, fill forms, and extract data. They can do almost anything a human can do online...except log in.

Authentication isn't a minor inconvenience; it prevents agents from completing tasks truly useful to you. Unauthenticated agents can't check your email, manage your calendar, or process a return.

Here's how to enable your agents to securely authenticate with your accounts, so they can access the services you use.

## Cookie Syncing

When you log into a website, your browser stores cookies that prove you're authenticated. On future visits, your browser automatically sends these cookies back, so the server recognizes you without another login.

Cookie syncing copies your browser's cookie store to the agent's browser. Since the browser now has the same cookies, each website treats the agent as "you."

Most browser automation platforms support this. Browserbase calls them Contexts. Steel and Kernel call them Profiles. Internally, they're all persisting user data directories with their own cookie stores.

### Browser Use

Browser Use supports syncing your real Chrome profile to the cloud with a single terminal command. You can also export cookies as a file.

### Browserbase

Browserbase persists auth state via reusable **Contexts**. The API is straightforward; you authenticate once, save the context, and load it in future sessions.

Browserbase also supports syncing cookies from your local Chrome browser to a persistent context via their cookie-sync skill. You can filter by domain and refresh existing contexts.

### Steel

Steel uses **Profiles**, persistent browser identities that store cookies, auth tokens, and fingerprints across sessions.

### Kernel

Kernel saves cookies and local storage via profiles so future sessions start authenticated.

## Password Managers

Password managers like 1Password let agents retrieve credentials from a vault and fill login forms automatically. This includes stored TOTP codes — the 6-digit codes from authenticator apps that refresh every 30 seconds.

The agent never sees your actual passwords, and values are filled programmatically.

## Two-Factor Authentication (2FA)

Many sites require a second factor after your password. The most common type is TOTP. These codes are derived from a shared secret key and the current time, refreshing every 30 seconds.

If you have the secret key, you can generate these codes programmatically without having to use an authenticator app.

**Best for password manager integration:** Kernel. Its Managed Auth auto-discovers credentials by matching the target domain against your vault. If you need human approval before every credential fill, Browserbase's Director integration provides the most interactivity. Browser Use is most flexible if you want to customize the integration, with both cloud-managed and open source options.

### Browser Use

Browser Use generates TOTP codes automatically. Use placeholders ending in `bu_2fa_code`, and fresh codes are generated at input time:

```python
agent = Agent(
    task='Go to example.com/login, enter x_user, x_pass, and x_bu_2fa_code',
    sensitive_data={
        'x_user': 'myusername',
        'x_pass': 'mypassword',
        'x_bu_2fa_code': 'JBSWY3DPEHPK3PXP',  # TOTP secret key
    },
)
```

The agent never sees your actual credentials, only placeholder names. Values are injected directly into the page.

**Where to find your TOTP secret:** During 2FA setup, look for "manual entry" or "can't scan QR code." In 1Password, edit the item and reveal the one-time password secret.

### Other Platforms

- **Browserbase**: Provides a code template for TOTP generation that you implement yourself.
- **Steel**: Credentials API handles TOTP as part of its credential injection system.
- **Kernel**: Handles TOTP automatically through Managed Auth when credentials include a `totp_secret`.

## Email & SMS Verification

Some sites send verification codes via email or SMS instead of using TOTP. You can send these codes to an inbox managed by your agent so it can complete the verification.

[AgentMail](https://docs.agentmail.to/welcome) is a standalone API for creating agent-managed inboxes.

## Comparison

| | Browser Use | Browserbase | Steel | Kernel |
| --- | --- | --- | --- | --- |
| Persistent sessions | ✓ | Contexts | Profiles | Profiles |
| Profile sync (real Chrome profile) | ✓ | | | |
| Storage state export | ✓ | | | |
| 1Password integration | ✓ | via Director | | ✓ |
| TOTP generation | Built-in | Via template | Credentials API | Managed Auth |
| Email/SMS verification | AgentMail | | | |

### Best for each use case

- **Syncing existing logins**: Browser Use. It's the only platform that can export your real Chrome profile to the cloud.
- **Hands-off credential management**: Kernel. Connect your 1Password vault, point Managed Auth at a domain, and Kernel handles credential discovery, form fill, and TOTP automatically.
- **Human-in-the-loop approval**: Browserbase. Director's 1Password integration requires explicit approval before every credential fill.
- **Multi-tenant credential security**: Steel. Their Credentials API handles form detection, auto-fill, and auto-submit without exposing values to the agent.
- **OSS and self-hosted**: Browser Use. The only platform with full auth support in its open-source library.

## The Bigger Picture

Right now, we're in an odd moment. Agents have become remarkably capable, but the infrastructure they operate on was built for humans. There's no native authentication framework for autonomous agents that's been widely adopted.

The methods above — cookie syncing, password managers, TOTP generation, and persistent hosted browsers — let agents access your accounts today.
