---
title: "Workspaces in LangSmith for improved collaboration and organization"
author: "LangChain Accounts"
date: "2024-06-13"
url: "https://www.langchain.com/blog/workspaces-in-langsmith"
---

Company AnnouncementsLangSmith

# Workspaces in LangSmith for improved collaboration and organization

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69d50051c5c24f19b81fd73a_Group%202147239256-2.svg)The LangChain TeamJune 13, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)3min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafc92dfe8bfbc12813ec_Workspaces.png)For large companies with many teams and business units, resource separation is a must. Workspaces in LangSmith now provide a logical grouping of users and resources within an organization, enhancing productivity and security for enterprises and startups.

Now, LangSmith activity and workflows will happen in the context of a **workspace** that separates resources between different teams, business units, or deployment environments. LangSmith now supports organization-scoped roles and actions, and each workspace has settings distinct from that of the overall organization. Read on for more on what’s changed and how workspaces can streamline your workflow, especially for larger companies managing multiple workloads and dividing responsibilities among teams.

## Using Workspaces to effectively manage resources

When you login for the first time in LangSmith, the default will be to have a Personal organization created for you. This organization will be limited to a single workspace.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbafc92dfe8bfbc1281412_Workspace-settings.png)

**Users in shared organizations** for LangSmith can create multiple workspaces and assign teams, business units, deployment environments, or another internal grouping to each one for streamlined efficiency. They’ll also be able to invite multiple users to your organization and workspace(s) at the same time, at the organization level. See [our docs](https://docs.smith.langchain.com/concepts/admin?ref=blog.langchain.com) for more details.

Resources such as trace projects, datasets, annotation queues, and prompts will now be associated with a single workspace within an organization, rather than shared across workspaces. Existing workflows remain unchanged, but if you have multiple workspaces, you must select which one to work in.

The introduction of workspaces does not change how seats for billing will be counted. API keys will also function as before and are scoped to the workspace they were created.

## Resource management that scales with enterprises

For large enterprises, it’s important to have workspaces that scale with your organization. **Users on the Enterprise plan** for LangSmith can create 10 workspaces and may request to have the limit increased. This allows you to have more granular control over employee access, so you can  isolate access to any sensitive data and operations. With the modularity of workspaces, you can also handle more diverse projects and make quick adjustments to the specific needs of each one.

Workspaces also play well with [Role-based access control (RBAC](https://blog.langchain.com/access-control-updates-for-langsmith/)) in LangSmith. [Learn more](https://docs.smith.langchain.com/concepts/admin?ref=blog.langchain.com#workspace-roles) about how workspace roles can be managed using RBAC.

When adding users, you can save time by inviting each batch of users to a group of workspaces with the same Workspace Role. A user’s Workspace Role determines their granular permissions within the specific workspace where it is assigned. This may be a Custom role or pre-defined System role. See the “User management and permissions” section below for more details.

0:00                            /0:551×

## User management and permissions

For users on paid plans of LangSmith, user management is now scoped at the organization level. This means you can invite users — who are designated as either an *Organization Admin* or an *Organization User* — to your organization and workspace(s) at the organization level.

An *Organization Admin *has full access to manage all organization configuration, users, billing, and workspaces. Any *Organization Admin* has *Admin* access to all workspaces in an organization.

Meanwhile, an *Organization User* may read organization information but cannot execute any write actions at the organization level. If [RBAC is enabled](https://blog.langchain.com/access-control-updates-for-langsmith/), then you should assign the *Organization User *role for any users that need granular permissions (whether that means access to a subset of workspaces, or selecting workspace roles besides Workspace Admin).

You can check your Organization role under *Organization members and roles *under Settings &gt; Members and roles. See [the docs](http://o/?ref=blog.langchain.com) for more on all organization permissions.

## What&#x27;s next for Workspaces

As we continue, we’ll be enabling workspaces for self-hosted customers. For self-hosted installations, there will be a configuration option to disable Personal organizations.

Additionally, future improvements include enabling organization-level management of usage limits. We’ll also enable programmatic access to organization-level APIs, which will allow enterprises to manage users, roles, and other organization settings using API keys with a programming language of their choice.

Furthermore, there will be an option to consolidate workspaces between organizations. For those interested, please contact [support@langchain.dev](mailto:support@langchain.dev).

## Conclusion

Workspaces enhance productivity and security by organizing users and resources into distinct groupings within an organization. This structure lets you more efficiently manage trace projects, datasets, and other resources – with customizable settings for each workspace.

Plans with multiple workspaces can manage user membership by workspace, and plans with RBAC can additionally assign users granular roles within each workspace.

***For more information, check out our ***[***conceptual guide***](https://docs.smith.langchain.com/concepts/admin?ref=blog.langchain.com#workspaces)*** and how-to guides on ***[***setting up a workspace***](https://docs.smith.langchain.com/how_to_guides/setup/set_up_workspace?ref=blog.langchain.com)*** and ***[***managing/navigating a workspace***](https://docs.smith.langchain.com/how_to_guides/setup/set_up_organization?ref=blog.langchain.com#manage-and-navigate-workspaces)***. Try out our features in LangSmith today, and reach out to us at ***[***support@langchain.dev***](mailto:support@langchain.dev)*** for any questions/feedback. ***

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