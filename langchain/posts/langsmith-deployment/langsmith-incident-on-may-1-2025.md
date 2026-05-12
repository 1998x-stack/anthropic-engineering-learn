---
title: "LangSmith Incident on May 1, 2025"
author: "LangChain Accounts"
date: "2025-05-07"
url: "https://www.langchain.com/blog/langsmith-incident-on-may-1-2025"
---

Company AnnouncementsLangSmith

# LangSmith Incident on May 1, 2025

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamMay 7, 2025![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)2min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)Requests to the [US LangSmith API](https://api.smith.langchain.com/redoc?ref=blog.langchain.com) from both the [web application](https://smith.langchain.com/?ref=blog.langchain.com) and SDKs experienced an elevated error rate for 28 minutes on May 1, 2025 (starting at 14:35 UTC and ending at 15:03 UTC). During the incident window, approximately 55% of all API requests failed with a connection error. This impacted all endpoints accessible through the API, including endpoints for run ingestion and data fetching.

A conflicting DNS record was accidentally left over during a migration between certificate renewal automation technologies at the end of January. This conflicting record caused renewal to fail all attempts at rotation during the month of April. Once the certificate expired, the LangSmith UI showed "Your connection is not private" when loaded, and all new connection attempts to the LangSmith API failed if they verified SSL.

Once the root cause was identified, the conflicting DNS record was deleted and a manual SSL certificate renewal was triggered, which restored SSL connectivity.

This incident happened due to a combination of human error and lack of observability for cert renewal automation and SSL certificate expiry. The incident was not initially discovered with proactive monitoring - it was instead first reported by both internal and external users. This further pointed to observability gaps that needed closing.

# Incident timeline

💡

All timestamps are in UTC

**Time**
**Event**

January 31, 2025 13:35
Migration to new certificate renewal automation completed, new certificates issued

January 31, 2025 16:07
Conflicting DNS record created via dangling Terraform code

April 1, 2025
Certificate renewal automation begins failed attempts to renew

May 1, 2025 14:35
Certificate expired

May 1, 2025 14:41
Initial user report of certificate expiry error

May 1, 2025 14:47
Root cause identified.

May 1, 2025 14:49
Conflicting DNS record deleted. Manual request to renew certificate issued.

May 1, 2025 14:54
Public incident status page published.

May 1, 2025 15:03
New certificate issuance completed, availability restored.

# Analysis

The indicators of certificate renewal failures included a certificate resource stuck in "pending" status and error logs in the component managing the renewal.

# Resolution

Once we identified the root cause, we were able to restore availability quickly by deleting the conflicting DNS record and manually requesting certificate renewal.

# Next Steps

The human error component of this incident involved:

- Missing deleting the conflicting Google-managed SSL certificate in Terraform code
- An incorrect assumption that we had certificate expiry monitors in place that would remain valid after migration

There were a few contributing factors to the duration of this incident and the slowness of our public response:

- Recent change of log destinations for Kubernetes system components omitted the new component, so manual troubleshooting was required
- Migration between status page providers in progress at the time - this delayed status page publishing

With all of this in mind, we have taken steps to prevent this failure — and others like it — from happening again:

- Added certificate expiry monitors for LangSmith domains
- Added monitors for significant drops in run ingestion volume
- Ensured all Kubernetes system component logs are ingested
- **In Progress**: Monitor error logs from all Kubernetes system namespaces
- **In Progress**: Building an internal dashboard for critical Kubernetes system workflows like certificate renewal

We take the reliability of our platform seriously, and we will invest in this area and others to continue improving our incident response process and reliability.

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef82f01e90bfdf3e83a25e_Blog-02.png)Company Announcements

#### Interrupt Preview: Meet the MC

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Becca WengApril 28, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/interrupt-preview-meet-the-mc)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef66604a47f5049293bcf6_april-newsletter-blog.png)Company Announcements

#### April 2026: LangChain Newsletter

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)4min[](/blog/april-2026-langchain-newsletter)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)