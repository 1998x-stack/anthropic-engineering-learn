---
title: "Custom Authentication and Access Control for LangGraph Platform"
author: "LangChain Accounts"
date: "2024-12-19"
url: "https://www.langchain.com/blog/custom-authentication-and-access-control-in-langgraph"
---

Agent ArchitectureLangGraph

# Custom Authentication and Access Control for LangGraph Platform

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcedc81683c99062bba702_Ankush.png)Ankush GolaDecember 19, 2024![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg)4min[

Go back to blog](/blog)[Create agents](#)Share[

](#)[

](#)[

](#)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2057c432b84a729f60_custom_auth.png)*Note: As of October 2025, LangGraph Platform has been re-named to &quot;LangSmith Deployment&quot;.*

Today we&#x27;re introducing custom authentication and resource-level access control for Python deployments in LangGraph Cloud and self-hosted environments. This feature lets you integrate your own auth providers and implement granular access patterns directly in your LangGraph applications.

## Quick Links

- [Video Tutorial: Adding Custom Authentication to LangGraph](https://youtu.be/g7s_6t5Jm4I?ref=blog.langchain.com)
- Authentication tutorial series:
[Basic Authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/?ref=blog.langchain.com) - Learn to add user authentication to a `langgraph` app
- [Resource Authorization](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/?ref=blog.langchain.com) - Add authorization &amp; resource filtering to make conversations private
- [Production Auth](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/?ref=blog.langchain.com) - Connect your application with OAuth2 providers like Supabase

- [Conceptual Guide: Authentication &amp; Access Control](https://langchain-ai.github.io/langgraph/concepts/auth/?ref=blog.langchain.com)
- [Quick guide](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/?ref=blog.langchain.com) on how to implement custom auth
- [`Auth`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.Auth) reference docs

## Why Custom Authentication?

While LangGraph Cloud provides built-in API key authentication, production deployments often need deeper integration with existing auth systems. Teams frequently need to:

- Validate credentials using their own auth provider
- Scope conversations to specific users
- Add OAuth support for end-user authentication
- Implement role-based access control (RBAC)

Custom authentication provides low-level primitives that integrate with any auth system while maintaining LangGraph&#x27;s simplicity. A typical flow would look something like the following:

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2157c432b84a729fac_image-12.png)

Your [`@auth.authenticate`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.Auth.authenticate) handler in LangGraph handles steps 4-6, while your [`@auth.on`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.Auth.on) handlers implement step 7. Keep reading to learn more!

## Adding to your app

The system centers around the [`Auth`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.Auth) object, which provides two key capabilities:

- **Authentication**: Validate credentials and identify users. The authentication handler (marked by `@auth.authenticate` ) receives each request and returns a [`MinimalUserDict`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.types.MinimalUserDict) containing the user&#x27;s identity:

`from langgraph_sdk import Auth

auth = Auth()

@auth.authenticate
async def get_current_user(authorization: str | None) -&gt; Auth.types.MinimalUserDict:
    &quot;&quot;&quot;Validate JWT tokens and extract user information.&quot;&quot;&quot;
    assert authorization
    scheme, token = authorization.split()
    assert scheme.lower() == &quot;bearer&quot;

    # Validate with your auth provider
    user = await validate_token(token)
    return {
        &quot;identity&quot;: user[&quot;id&quot;],
        &quot;email&quot;: user[&quot;email&quot;],
        &quot;is_authenticated&quot;: True
    }
`

With authentication alone, non-credentialed requests are rejected. However, authenticated users are still able to access all resources since we haven&#x27;t introduced any resource ownership. That&#x27;s the role of the authorization handlers below.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2157c432b84a729f98_image-13.png)
- **Authorization**: Control access to specific resources. Authorization handlers receive an [`AuthContext`](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.types.AuthContext) containing user information (from your `@auth.authenticate` function above) and can add metadata to the resource indicating ownership and/or return filters that control resource access:

`@auth.on
async def add_owner(ctx: Auth.types.AuthContext, value: dict):
    &quot;&quot;&quot;Make resources private to their creator.&quot;&quot;&quot;
    filters = {&quot;owner&quot;: ctx.user.identity}
    metadata = value.setdefault(&quot;metadata&quot;, {})
    metadata.update(filters)
    return filters
`

Now that an authorization handler has been implemented, resources&#x27; metadata are stamped with an &quot;`owner`&quot; ID to restrict access only to threads the user has created.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae2157c432b84a729f9c_image-15.png)

Authorization event handlers have three main jobs:

- Add metadata to resources being created.
- Return filters so users can only access matching resources
- Reject requests from users who lack permissions to this resource or action.

To use custom auth in your deployment, add an auth configuration to your `langgraph.json`, pointing to the `auth` variable name and path in your app deployment.

`{
  &quot;auth&quot;: {
    &quot;path&quot;: &quot;src/security/auth.py:auth&quot;
  }
}
`

## Resource-Level Control

The authorization system provides fine-grained control over `threads`, `assistants`, and `crons`  (support for authorization on `store` actions to be released soon). Instead of a single global handler, you can implement custom logic for different operations:

`@auth.on.threads.create
async def on_thread_create(ctx: Auth.types.AuthContext, value: Auth.types.on.threads.create.value):
    &quot;&quot;&quot;Custom logic for thread creation&quot;&quot;&quot;
    if not has_permission(ctx.user, &quot;threads:create&quot;):
        raise Auth.exceptions.HTTPException(status_code=403)
    return {&quot;owner&quot;: ctx.user.identity}

@auth.on.assistants
async def on_assistants(ctx: Auth.types.AuthContext, value: Auth.types.on.assistants.value):
    &quot;&quot;&quot;Restrict access to assistants resource&quot;&quot;&quot;
    if not is_admin(ctx.user):
        raise Auth.exceptions.HTTPException(status_code=403)
`

LangGraph will use the most specific handler that matches the resource and action being accessed, falling back to broader handlers when needed. For a given event, at most one handler is called.

## Current Support

Custom authentication is currently available for Python deployments only. Support for JavaScript deployments is coming soon.

## Next Steps

The fastest way to get started is by checking out the [quick how-to guide](https://langchain-ai.github.io/langgraph/how-tos/auth/custom_auth/?ref=blog.langchain.com) on implementing custom auth. We also have the following resources:

- [Video Tutorial: Adding Custom Authentication to LangGraph](#)
- Authentication tutorial series:
[Basic Authentication](https://langchain-ai.github.io/langgraph/tutorials/auth/getting_started/?ref=blog.langchain.com) - learn to add user authentication to a langgraph app
- [Resource Authorization](https://langchain-ai.github.io/langgraph/tutorials/auth/resource_auth/?ref=blog.langchain.com) - add authorization &amp; resource filtering to make conversations private
- [Production Auth](https://langchain-ai.github.io/langgraph/tutorials/auth/add_auth_server/?ref=blog.langchain.com) - integrate with an identity server to finish the implementation

To learn even more, check out the [conceptual guide on custom authentication &amp; access control](https://langchain-ai.github.io/langgraph/concepts/auth/?ref=blog.langchain.com), and the [reference docs](https://langchain-ai.github.io/langgraph/cloud/reference/sdk/python_sdk_ref/?ref=blog.langchain.com#langgraph_sdk.auth.Auth) on the auth object.

And check out the [full-stack template](https://github.com/langchain-ai/custom-auth?ref=blog.langchain.com) ([demo](https://custom-auth.vercel.app/?ref=blog.langchain.com)) that connects your LangGraph chatbot with a react frontend.

Try it out and share your feedback on [GitHub](https://github.com/langchain-ai/langgraph/discussions?ref=blog.langchain.com). This is another step toward supporting more sophisticated deployment patterns - we&#x27;re excited to see what you build!

### Related content

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f20536df00c0eb15eab1d3_blue-77%20characters%20max.png)Deep AgentsAgent ArchitectureOpen Source

#### Tuning Deep Agents to Work Well with Different Models

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcefac505b6b48827abf84_vivek-trivedy.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dcf032ce65a32e276a4d0a_mason-daugherty.png)Vivek TrivedyMason DaughertyApril 29, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)5min[](/blog/tuning-deep-agents-different-models)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69ef96ff74c638e982ff68c6_86%20(1).png)Agent ArchitectureLangSmithOpen Source

#### How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e0003a1af368dfae13c23c_jacob-talbot.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69dd2ddbdd2243fd1398a523_becca-weng%201.png)Jacob TalbotBecca WengApril 27, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)7min[](/blog/langsmith-langchain-oss-eu-ai-act)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23754937c2f749d12bb0b_76%20(1).png)Agent ArchitecturePartner

#### Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e234176723e6111407b935_renuka-kumar.png)![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69e23427e77d2631610e5d62_Prashanth-Ramagopal.png)Renuka KumarPrashanth RamagopalApril 17, 2026![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69cd1fd0002272ce39bf1241_Icon-6.svg)11min[](/blog/agentic-engineering-redefining-software-engineering)![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce01ea562f8cc223cabf25_Frame%202147254328.svg)Sign up for our newsletter to stay up to date

Thank you! Your submission has been received!Oops! Something went wrong while submitting the form.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[Try LangSmith

](https://smith.langchain.com/)[Get a demo

](/contact-sales)