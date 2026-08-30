source: https://docs.evokoa.com/polygres/getting-started/core-workflow
title: Core workflow | Polygres
source_hash: 2d60acfbe2920622fcac0895960a1927228f498952b4b19a85a6a36c606c7999
discovered_from: https://docs.evokoa.com/polygres

# Core workflow | Polygres

Core workflow

The Polygres customer journey starts with an account and organization, not an API key. Set up the shared SaaS workspace first, then create projects, connect data, configure retrieval, and add application access.

1 Create your account

Sign up with the available method and accept the current legal terms. Polygres creates your organization and makes you its owner.

Details →

2 Use your organization or accept an invitation

The organization is the top-level workspace for members, roles, project allowances, and projects.

/{organization} /{organization}/members

Details →

3 Create a project

Choose a Free Nano project or, when available, a Paid Basic project. Wait until the project reports ready.

/{organization}/new

Details →

4 Connect or load data

Use the pooled URL for application traffic and the direct URL for migrations, imports, and bulk work.

/{organization}/{projectId}/connect

Details →

5 Configure retrieval

Set up graph, vector, text, hybrid, and pgContext AI Search over the tables you already manage.

/{organization}/{projectId}/workspace

Details →

6 Query through the Runtime API or SDK

After confirming readiness, exercise queries through the Runtime API, CLI, or Python SDK.

Details →

7 Query from your application

Create a project API key and move the same queries into trusted backend code.

/{organization}/{projectId}/settings

Details →

1. Create your account

Create an account with the available sign-up

method and accept the current legal terms. For a normal self-service sign-up,

Polygres generates a unique organization name, creates the organization, and

makes you its owner automatically. There is no organization-name, tier, or

use-case questionnaire in the sign-up flow. You can rename the generated

organization later.

When a workflow requires verified email ownership, use the newest verification

message. An older or expired link may no longer be valid.

2. Use your organization or accept an invitation

An organization is the top-level workspace for members, roles, project

allowances, and projects.

A normal self-service sign-up opens the organization Polygres created for the

account. If the authenticated email has a pending invitation, review it and

explicitly accept or decline it. Each user can have one active organization

membership. If several invitations exist for the same email, choose one

organization. Owners can invite members as admins, developers, or viewers.

Open the organization home ( /{organization} ) and Members ( /{organization}/members ) for membership management.

3. Create a project

Open New project ( /{organization}/new ) and choose Free or, when the dashboard offers it for your organization, Paid . Free creates a shared Nano project at no cost. An organization owner or admin with an eligible subscription can create an isolated Paid Basic project starting at $10 per month. See Free and Paid projects for capacity pricing, billing, and availability.

Choose Host with Polygres for a managed PostgreSQL environment. To synchronize an existing database, choose Supabase , Neon , PlanetScale , or Postgres Database and follow the synced-project guide . When Paid synchronization is offered, the payment review shows the estimated first-cycle charge, applies available credits first, and shows the remainder paid through Stripe. Polygres activates Basic automatically after synchronization is established.

Polygres creates the project as Default Project and shows its status while setup completes. You can rename it later from its Settings page. Each organization has one Free Nano slot shared across hosted and synchronized project types. Paid Basic projects leave that slot available. Existing organizations with multiple Nano projects can keep them and can create another Free project after the organization no longer has a Nano project.

If the account email is not yet verified, project creation first sends a verification message and preserves the intended destination. Complete verification from that message, then return to the project workflow.

Wait until the project reports ready before using data tools or retrieval setup. Open the project overview ( /{organization}/{projectId} ) to see its status and next actions.

A managed database project belongs to the organization and contains:

one managed PostgreSQL database,

pooled and direct PostgreSQL connection URLs,

data import, table, SQL, and migration tools,

graph, Legacy vector, and text configuration plus pgContext AI Search

collections,

project API keys for Runtime retrieval.

4. Connect or load data

Open connection details ( /{organization}/{projectId}/connect ).

The complete pooled and direct database workflow in this section applies to managed database projects. For a synced project, continue using the source PostgreSQL database for SQL, writes, imports, and migrations. After Synced Basic activates, its overview displays stable destination hostnames; the connection details shown there are limited to those hostnames.

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

AI Context (Vector)

Use AI Context (Vector) setup ( /{organization}/{projectId}/workspace/context ) to create a

pgContext collection over a vector source, choose its search settings, and

prepare its indexes. The pgContext collections tab displays each collection

as a separate table of named vectors and provides Add vector . Every

collection has a default vector, independently of the project’s default

collection.

For standard projects, the Legacy tab is only for persisted pgvector registrations that are

effectively Ready. An HNSW registration needs its exact physical index to be

Ready. An existing index_kind: none registration can be Ready for exact-scan

retrieval without HNSW. A physical pgvector index without a persisted

registration is never made implicitly usable, and new registration or

re-enabling through the retired Legacy API is unsupported.

Polygres does not create embeddings. When an existing public.vector(n) column

must be migrated, use Context discovery and preflight to review the in-place

conversion and ownership effects. Deleting a Legacy registration, when one

exists, is a separate explicit operation rather than automatic dashboard

cleanup.

Text

Use Text search setup ( /{organization}/{projectId}/workspace/text-search ) to configure PostgreSQL full-text search over a tsvector column or fuzzy search over a plain text column. Each saved text configuration reports its own index status.

Hybrid

Legacy Hybrid retrieval combines a ready graph build with an effectively Ready

persisted Legacy vector registration. For new graph-and-semantic workflows, use

pgContext graph-first, vector-first, rank-fusion, or Joint retrieval.

The shared retrieval-readiness check summarizes graph, Legacy vector, and

Legacy Hybrid. Text search is independent in the current product and is ready

when its selected text configuration has a ready index.

pgContext AI Search

Use the Polygres CLI for an interactive collection workflow:

check capabilities, discover source tables, run preflight, review the proposed

schema and ownership plan, create the collection, and verify it. Backend-owned

automation can use the Python SDK and the same project API

key. Collection status and durable operations provide lifecycle visibility.

6. Query through the Runtime API or SDK

After confirming retrieval readiness in the dashboard, exercise graph, vector,

text, hybrid, and pgContext queries through the Runtime API, CLI, or Python SDK.

Start with a human task rather than an endpoint name—for example:

explore records connected to a customer,

find content similar to an existing row,

find semantically similar records within related account data.

Configure and inspect pgContext collections in AI Context (Vector) setup, then exercise their dense,

text-hybrid, graph-composed, rank-fusion, or Joint methods through the CLI,

public API, or Python SDK.

7. Query from your application

Create a project API key from Settings > Project API Key ( /{organization}/{projectId}/settings ). The raw value, such as poly_live_<...> , is shown once. Store it immediately in a secret manager or backend environment variable.

Use that key from a trusted backend for graph, Legacy vector, text, Legacy

Hybrid, and pgContext retrieval. Continue to use the PostgreSQL connection URL

and native database password for normal application reads and writes. Each

credential has a focused role in the application architecture.

Next steps

Product Guides

Connect and credentials

Connection examples

Load and manage data

Configure and query retrieval

Retrieval integration patterns

pgContext CLI guide

Reference

Routes

Error codes
