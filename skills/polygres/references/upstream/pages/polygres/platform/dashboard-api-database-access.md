source: https://docs.evokoa.com/polygres/platform/dashboard-api-database-access
title: Dashboard, API, and database access | Polygres
source_hash: 38b2cfccde9baa2d464f3be86fdf8e4428589a50854686a6669b9d3d5e7fd1a8
discovered_from: https://docs.evokoa.com/polygres

# Dashboard, API, and database access | Polygres

Dashboard, API, and database access

A Polygres project can be used through complementary surfaces. The dashboard operates the SaaS workspace, the Polygres CLI covers terminal setup workflows, PostgreSQL connections serve application data, and the Polygres API serves retrieval to backend code.

Confusing these surfaces is a common setup mistake. Each one is meant for a different job, and each one has its own credential boundary.

Surface Best for Access used

Dashboard Organizations, members, projects, imports, SQL, migrations, retrieval setup, query testing, and credential management. Signed-in dashboard session.

Polygres CLI Project selection, environment output, psql , Runtime API keys, CSV import, migrations, and retrieval configuration from a terminal. CLI login session for the authenticated user and active organization.

PostgreSQL Normal application reads and writes, ORM traffic, database clients, schema tools, and bulk data work. Project connection URL plus native PostgreSQL password.

Polygres API or SDK Graph, vector, text, hybrid, and pgContext retrieval, including backend-owned Context collection operations. Project API key such as poly_live_<...> .

These four surfaces work with the same project data, with a focused access

method for each task.

Match each surface to the task

Use a dashboard session for signed-in organization and project workflows.

Use a PostgreSQL password for direct or pooled database connections.

Use a project API key for application retrieval and pgContext Runtime

resource management. Use the dashboard or CLI login for control-plane tasks

such as projects, imports, migrations, keys, and database credentials.

Choose the surface by task first, then use the credential that belongs to it.

Use the dashboard for setup and operations

The dashboard is the primary customer interface. It is where your team creates and manages the organization before working with projects.

Common starting points include:

Organization home ( /{organization} ) for the shared workspace,

Members ( /{organization}/members ) for members and fixed roles,

New project ( /{organization}/new ) to create a project,

Project overview ( /{organization}/{projectId} ) for status and navigation,

Connection details ( /{organization}/{projectId}/connect ) for PostgreSQL connection details and the Runtime API URL,

Settings ( /{organization}/{projectId}/settings ) for Project API Key management,

Project workspace ( /{organization}/{projectId}/workspace ) for visual graph exploration,

Graph, Vector, and Text Search pages under the project workspace for retrieval setup.

Use a dashboard session to import data, browse tables, run SQL, apply migrations, and configure graph, AI Context, Legacy vector, and text retrieval. Sensitive actions remain subject to the member’s organization role.

Configure AI Context in the dashboard

The Vector page has separate pgContext collections and Legacy tabs. Each pgContext collection appears separately, with one row for each named vector in that collection. Creating a collection creates its initial vector and makes that vector the collection default. Use Add vector to attach more named vectors to the same collection.

Every collection has one default vector. That choice is independent of the project’s default collection: the project default chooses a collection when no collection is named, while the collection default chooses a vector when no exact vector_name is supplied. Ranked retrieval can instead select an exact vector by name.

In collection setup, Existing vector column lists eligible native pgcontext.vector(n) and compatible pgvector.vector(n) columns. Creating from a compatible pgvector column converts it in place. If that column has a persisted Legacy registration, the dashboard asks for confirmation and deletes the registration after the collection or additional vector is created successfully. The Legacy tab shows persisted Legacy registrations that are effectively Ready ; a physical-only pgvector index is not implicitly registered or usable by Legacy retrieval.

Use PostgreSQL for application data

A project exposes a pooled URL and a direct URL. Both reach the project’s managed PostgreSQL database.

Pooled URL

Use the pooled URL as DATABASE_URL for normal application traffic. It is the default choice for web services, ORMs, serverless functions, and other workloads that open many short-lived connections.

Direct URL

Use the direct URL as DIRECT_URL for migrations, schema changes, COPY , imports, restores, and database tools that need a stable session.

The dashboard shows connection strings with a password placeholder until an authorized user explicitly reveals the native PostgreSQL password. Keep the completed URL in trusted backend configuration or a secret manager. Do not place it in browser code or public logs.

Resetting the native database password rotates it immediately and invalidates old direct and pooled credentials. The reset action does not send the new password by email and does not automatically show it. Use the dashboard reveal flow after reset to copy the new password into trusted application secrets.

For client examples and detailed connection behavior, use the Product Guide for Connect and credentials .

Use the API or SDK for application retrieval

After the relevant retrieval resources are configured, create a project API key in Settings

( /{organization}/{projectId}/settings ) and copy the Runtime API URL from

connection details ( /{organization}/{projectId}/connect ). You can configure

pgContext collections in the dashboard, or use CLI preflight and collection

verification or an explicit backend-owned SDK workflow.

Use the key from trusted backend code to call:

graph retrieval over configured relationships,

Legacy vector retrieval over an existing eligible registration,

text search through full-text or fuzzy configurations,

Legacy hybrid retrieval that combines graph and vector results,

pgContext collection lifecycle, point synchronization, filters, durable

operations, dense and grouped search, text hybrid, graph composition, rank

fusion, and Joint retrieval.

The raw key is shown only when it is created. Store it immediately and use a placeholder such as poly_live_<...> in documentation, examples, and tickets.

A project API key is scoped to one project Runtime. It supports application

retrieval and pgContext collection management. Use a dashboard session or CLI

login for organization and control-plane workflows such as creating projects,

imports, migrations, API-key management, and database credential access.

Configure in the dashboard, then query from code

A practical workflow is:

Configure the graph or inspect an existing persisted Legacy vector registration.

Confirm the graph build or persisted Legacy registration is Ready . HNSW needs its exact physical index Ready; index_kind: none can serve exact scan without HNSW. For hybrid, confirm both graph and Legacy vector readiness.

Create a project API key.

Exercise the query from a trusted backend using the documented retrieval patterns and inspect returned records, paths, scores, and filters.

For pgContext, configure the collection from the dashboard or use CLI preflight and collection setup , then query it from the API or SDK. Backend services with explicit ownership of the lifecycle can manage the same collection through project.context . For text retrieval, confirm the saved configuration in the dashboard and test it from the API or SDK.

This keeps schema and retrieval decisions visible to SaaS operators while giving application code a stable retrieval interface.

A typical production split

A SaaS application commonly uses both project credentials on the server:

DATABASE_URL and the native PostgreSQL password for transactional product data.

POLYGRES_API_KEY=poly_live_<...> and POLYGRES_RUNTIME_URL=https://{project_id}.api.db.polygres.com/v1 for retrieval features.

The browser talks to your application backend. It should not receive either secret. Team members use their own dashboard sessions for Polygres administration and retrieval setup.

Next steps

Product Guides

Polygres CLI

Connect and credentials

Connection examples

Load and manage data

Configure and query retrieval

Retrieval integration patterns

Reference

Changelog

Routes

Error codes
