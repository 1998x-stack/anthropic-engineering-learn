---
title: "Permissions-Aware SharePoint Retrieval Guide | LlamaIndex"
author: "Unknown"
date: "Unknown"
url: "https://www.llamaindex.ai/blog/permissions-aware-content-retrieval-with-sharepoint-and-llamacloud"
category: "rag"
---

Follow us on


 -  [


](https://github.com/run-llama/)
 -  [

](https://discord.com/invite/eN6D2HQ4aX)
 -  [


](https://twitter.com/llama_index)
 -  [


](https://www.linkedin.com/company/91154103/)
 -  [


](https://www.youtube.com/@LlamaIndex)







 A much-requested feature of LlamaParse&#39;s SharePoint integration is being permissions-aware: the ability to use SharePoint&#39;s granular access controls to also control access to documents in your RAG application. LlamaParse supports this out of the box! In this step-by-step walkthrough, we&#39;ll show you how it works and what it looks like.



 First we&#39;ll want to create a new Index by clicking &quot;Create Index&quot; in the top-right of the LlamaParse interface.



##  Ready to get started with LlamaParse?



 Explore our free and paid plans today.


 -  [ Learn more ](/pricing)

   ![](https://cdn.sanity.io/images/7m9jw85w/production/199f976e8d3cf4d3cd5007094bf16218d02944fb-2912x1072.png)

 We&#39;ll give our Index a human-readable name:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/2aef1b4ac1c9152f379e392302de38b19296fd71-1642x778.png)

 If we don&#39;t have one already, we&#39;ll need to create a SharePoint data source from the drop-down:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/dd11cc4a3e4cfba4b181294122997bcb6e7db3e6-2222x1286.png)

 To share with LlamaParse itself, you&#39;ll need a Site Name, a Client ID and secret, and a tenant ID. The other fields are optional but let you specify more specific access for LlamaParse. You&#39;ll want LlamaParse to have as much access as any user will need, because the permissions-awareness happens on your app:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/5e62ffb5dfc78eddb5a30d39ef01fa1716d1f594-1634x2070.png)

 We&#39;ll configure a managed data sink, OpenAI embeddings, and use the defaults for things like multi-modal indexing, parse settings (not shown) and transform settings (not shown). Then we&#39;ll click &quot;Deploy index&quot; at the bottom of the screen.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/7cacf422400de52578e1b5b29f83298dd6ceccdf-1632x922.png)

 If all is well, LlamaParse will connect and sync to your documents, pulling them in, parsing them, chunking them, and indexing them for you.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/ff09106469487cb66d1ab6854757f6c2879b3992-880x1102.png)

 Once everything is indexed, you can go to your Index page and choose &quot;data sources&quot; to see a list of all the files LlamaParse indexed for you.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/d4d7046025842010c3cd79eb7f7a324f5b7a1cb2-2468x1698.png)

 Click the &quot;eye&quot; icon to view more detail about any file and click into the &quot;chunks&quot; tab. Here you&#39;ll see `allowed_siteUser_ids`  and related fields indicating who has access.

  ![](https://cdn.sanity.io/images/7m9jw85w/production/07e0bb90f66bc02b1a39a260db94b9ed8a8629b3-1702x1450.png)

 Over in SharePoint&#39;s interface, you can click the &quot;share&quot; icon and select specific users with whom to share any individual file (you can also click the 3 dots and select &quot;Manage Access&quot;):

  ![](https://cdn.sanity.io/images/7m9jw85w/production/85759ee6b3a2ce23811ed51279fa7b4ef3bf753e-1662x526.png)

 With that done, head back to LlamaParse and click the &quot;sync&quot; button (or wait for automatic syncing to occur). You&#39;ll see the list of allowed users has changed in the chunks preview:

  ![](https://cdn.sanity.io/images/7m9jw85w/production/2c6397e3df37987eb11e1cd42374d09f407ee7f6-1704x1280.png)

 Now you can build a RAG app that is aware of the permissions on chunks and treats them appropriately!