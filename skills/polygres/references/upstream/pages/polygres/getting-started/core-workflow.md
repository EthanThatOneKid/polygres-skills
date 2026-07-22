source: https://docs.evokoa.com/polygres/getting-started/core-workflow
title: Core workflow | Polygres
source_hash: b36e63c4ab01cf1e6cafcb592b2e67e922da09730a2c9901dadf685fd5990af8
discovered_from: https://docs.evokoa.com/polygres

# Core workflow | Polygres

Core workflow

The Polygres customer journey starts with an account and organization, not an API key. Set up the shared SaaS workspace first, then create projects, connect data, configure retrieval, and add application access.

1. Create your account

Create an account with an email and password, or use Continue with email for a secure passwordless link. Password signup requires accepting the Terms of Service and acknowledging the Privacy Policy. Account setup then asks for the organization name; a display name is optional.

Self-service activation uses available shared-tier capacity. When capacity is available, Polygres creates the organization and opens its dashboard. Otherwise, the account remains on Pending approval until capacity is available. Suspended or rejected accounts cannot use project tools or application retrieval.

Email verification is enforced when a workflow requires verified ownership, including creating a project and joining an invited organization. Use the newest verification message, because an older or expired email link may no longer be valid.

2. Join or create an organization

An organization is the top-level workspace for members, roles, tier selection, and projects.

After authentication, use one of these paths:

Review and accept or decline an invitation for the authenticated email address.

Create an organization and become its owner when no invitation is selected.

Continue with the active organization already attached to an existing account.

Each user can have one active organization membership. If several invitations exist for the same email, choose one organization. Joining it automatically closes the other pending invitations after verification. You can cancel a provisional choice from the verification page and continue with normal organization setup instead. Owners can invite members as admins, developers, or viewers. The organization tier sets a shared project allowance for the whole team rather than a separate allowance for each member.

Open the organization home ( /{organization} ) and Members ( /{organization}/members ) for membership management.

3. Create a project

Open New project ( /{organization}/new ), name the project, and submit it. Polygres creates the managed PostgreSQL environment and shows its status while setup completes.

If the account email is not yet verified, project creation first sends a verification message and preserves the intended destination. Complete verification from that message, then return to the project workflow.

Wait until the project reports ready before using data tools or retrieval setup. Open the project overview ( /{organization}/{projectId} ) to see its status and next actions.

A project belongs to the organization and contains:

one managed PostgreSQL database,

pooled and direct PostgreSQL connection URLs,

data import, table, SQL, and migration tools,

graph, vector, and text configuration,

dashboard queries and project API keys.

4. Connect or load data

Open connection details ( /{organization}/{projectId}/connect ).

Use the pooled connection URL , commonly stored as DATABASE_URL , for normal application traffic, ORMs, and short-lived requests. Use the direct connection URL , commonly stored as DIRECT_URL , for migrations, schema changes, COPY , restores, and bulk ingestion.

Then choose the data path that matches your situation:

Point a new application at the pooled URL and create its schema.

Move an existing PostgreSQL database with SQL or pg_dump import.

Upload CSV data through Imports ( /{organization}/{projectId}/import ).

Inspect data in Tables ( /{organization}/{projectId}/tables ).

Run SQL in the SQL editor ( /{organization}/{projectId}/sql ).

Apply forward-only schema changes in Migrations ( /{organization}/{projectId}/migrations ).

The native PostgreSQL password is revealed from the dashboard only to a role with permission to see it. Keep it in trusted server-side configuration, not browser code.

5. Configure retrieval

Open the project workspace ( /{organization}/{projectId}/workspace ).

Graph

Use Graph setup ( /{organization}/{projectId}/workspace/graph ) to review candidate tables and relationships, save the paths that matter to your product, and build the graph configuration. A ready build is required before graph queries work.

Vector

Use Vector setup ( /{organization}/{projectId}/workspace/vector ) to select an existing fixed-dimension vector(n) embedding column, choose how it is searched, and prepare its index. Polygres does not create embeddings.

Text

Use Text search setup ( /{organization}/{projectId}/workspace/text-search ) to configure PostgreSQL full-text search over a tsvector column or fuzzy search over a plain text column. Each saved text configuration reports its own index status.

Hybrid

Hybrid retrieval combines graph and vector results. It does not require a separate data copy or text configuration, but it does require the relevant graph build and vector configuration to be ready.

The shared retrieval-readiness check summarizes graph, vector, and hybrid. Text search is independent in the current product and is ready when its selected text configuration has a ready index.

6. Query in the dashboard

Open the query workbench ( /{organization}/{projectId}/workspace/query ) to test graph, vector, text, and hybrid retrieval with your signed-in dashboard session.

Start with a human task rather than an endpoint name—for example:

explore records connected to a customer,

find content similar to an existing row,

search ticket text for an error message,

find semantically similar records within related account data.

The dashboard query workbench uses the same retrieval behavior available to applications, making it the best place to validate data shape, configuration, filters, and result quality before writing code.

7. Query from your application

Create a project API key from Settings > Project API Key ( /{organization}/{projectId}/settings ). The raw value, such as poly_live_<...> , is shown once. Store it immediately in a secret manager or backend environment variable.

Use that key from a trusted backend for graph, vector, text, and hybrid retrieval. Continue to use the PostgreSQL connection URL and native database password for normal application reads and writes. These credentials serve different jobs and should not be exchanged.

Next steps

Product Guides

Connect and credentials

Connection examples

Load and manage data

Configure and query retrieval

Retrieval integration patterns

Reference

Routes

Error codes
