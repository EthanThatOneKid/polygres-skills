source: https://docs.evokoa.com/polygres/getting-started/key-concepts
title: Key concepts | Polygres
source_hash: 6f3f07f8f764bd794d152835eb9a745a9a66060ece7575c907e7e42aba93ae8f
discovered_from: https://docs.evokoa.com/polygres

# Key concepts | Polygres

Key concepts

Polygres is easiest to understand as a shared SaaS workspace around one or more managed PostgreSQL projects.

Organization

The organization is the top-level customer workspace and project owner. It appears in dashboard URLs as {organization} .

An organization contains:

members and their fixed roles,

a project allowance shared by all members,

the projects the team operates together.

Project limits are counted for the organization, not separately for each user.

Roles

Polygres uses four fixed roles in the current beta. Roles have predefined permissions; organizations do not create custom roles or per-member permission overrides.

Role High-level access

Owner Full organization control, including tier and member management, plus sensitive project operations.

Admin Operational administration across projects; member management is available where the fixed role rules allow it.

Developer Day-to-day project work such as creating or updating projects, loading data, running SQL and migrations, and configuring retrieval.

Viewer Read-only organization and project access. No project mutations, native password reveal, or API-key management.

The organization creator is the owner. Invitations assign admin, developer, or viewer access.

Project

A project is an organization-owned managed PostgreSQL environment. It is the unit you connect to, load data into, configure, and query.

Each project has a stable project ID, represented in developer examples as {project_id} . Dashboard routes use the organization and project together, such as /{organization}/{projectId} .

PostgreSQL connections

Every project exposes two connection URLs:

Connection Use it for

Pooled ( DATABASE_URL ) Application traffic, ORMs, serverless functions, and short request-time queries.

Direct ( DIRECT_URL ) Schema changes, migrations, COPY , imports, restores, and tools that need a stable database session.

Both connect to the same PostgreSQL project. Choose the URL based on the job rather than creating separate databases.

Open connection details ( /{organization}/{projectId}/connect ) to copy passwordless connection templates and reveal the native PostgreSQL password when your role allows it.

For more details, see Connect Your App and Connection Examples .

Credentials

Polygres separates three kinds of access so that one secret does not unlock every surface.

Credential Main purpose

Dashboard session Manage the organization and projects, use data tools, configure retrieval, test queries, and manage allowed credentials.

Native PostgreSQL password Connect an application or database tool through the pooled or direct PostgreSQL URL.

Polygres API key Call graph, vector, text, hybrid, and pgContext retrieval, plus explicit pgContext Runtime resource management, from trusted application code. Keys look like poly_live_<...> and the raw value is shown once.

A dashboard session is not an application API key. A PostgreSQL password does not authenticate retrieval calls. A Polygres API key cannot reveal the database password or perform dashboard-only setup work.

Learn more about Database Access & Connections and Security Basics .

PostgreSQL as the source of truth

Your application tables remain the authoritative data. Polygres retrieval is configured over those tables:

Graph configuration selects records and relationships that can be traversed.

A Legacy vector configuration is a persisted registration over an existing

fixed-dimension vector(n) embedding column. It is usable only while it is

effectively Ready. HNSW requires its exact physical index to be Ready;

index_kind: none can be Ready for exact-scan retrieval without HNSW. A

physical-only pgvector index is never an implicit registration. New

registration and re-enabling are retired.

Text configuration points to a tsvector column for TSVector full-text

search or a plain text column for Fuzzy pg_trgm matching. Polygres can

create and maintain a stored generated TSVector column during configuration,

or register an existing one.

Legacy Hybrid retrieval combines a ready graph build with an effectively

Ready persisted Legacy vector registration.

A pgContext collection binds a source table, source-key column, native

pgcontext.vector(n) columns, optional text and filter fields, and its

managed point mappings. It starts with one default vector and can add more

named vectors over the same source rows. Creating a collection from a

compatible public.vector(n) source converts that column in place to the

native pgContext type. The project default collection is independent of each

collection’s default vector. Ranked retrieval uses an exact vector_name

when supplied and otherwise uses that collection’s default vector.

Polygres does not generate embeddings and does not require you to move the project into a separate vector or text-search database.

Retrieval configuration and readiness

Configuration defines what a query is allowed to use: tables, relationships, embedding columns, text columns, metadata, filters, limits, and indexes.

Readiness is mode-specific:

Graph queries require a ready graph build.

Legacy vector queries require an effectively Ready persisted registration.

HNSW requires a Ready matching index; exact-scan index_kind: none does not.

Text search requires a ready saved TSVector or Fuzzy configuration.

Legacy Hybrid queries require both their graph and Legacy vector inputs to be

ready.

pgContext uses its own capability, collection status, verification,

diagnostics, and durable-operation views.

The shared project readiness view covers graph, Legacy vector, and Legacy

Hybrid. Text search reports status through its own configuration. pgContext

readiness is collection-specific and begins with Context capabilities and

preflight.

For more details, see Configure Retrieval .

Application queries

Use the dashboard to configure retrieval and confirm readiness. Exercise graph,

vector, text, hybrid, and pgContext retrieval through the CLI, public API, or SDK.

After the results look right, create a project API key and move the same graph,

Legacy vector, or Legacy Hybrid query into backend application code. Exercise

text retrieval through the API or SDK. For pgContext, configure collections in

the dashboard or preflight them through the CLI, then query them through the

CLI, public API, or SDK. The Database Access &

Connections page explains the split.

See also Integration Patterns .

Next steps

Product Guides

Connect and credentials

Configure and query retrieval

Retrieval integration patterns

Limits, security, and troubleshooting

Reference

Routes

Error codes
