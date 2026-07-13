source: https://docs.evokoa.com/polygres/platform/dashboard-api-database-access
title: Dashboard, API, and database access | Polygres
source_hash: 92cf63e7e9573e858c686a6792d9a4c5cb0a39d53b3063e0768b873c25f58142
discovered_from: https://docs.evokoa.com/polygres

# Dashboard, API, and database access | Polygres

Dashboard, API, and database access

A Polygres project can be used through complementary surfaces. The dashboard operates the SaaS workspace, the Polygres CLI covers terminal setup workflows, PostgreSQL connections serve application data, and the Polygres API serves retrieval to backend code.

Confusing these surfaces is a common setup mistake. Each one is meant for a different job, and each one has its own credential boundary.

Surface Best for Access used

Dashboard Organizations, members, projects, imports, SQL, migrations, retrieval setup, query testing, and credential management. Signed-in dashboard session.

Polygres CLI Project selection, environment output, psql , Runtime API keys, CSV import, migrations, and retrieval configuration from a terminal. CLI login session for the authenticated user and active organization.

PostgreSQL Normal application reads and writes, ORM traffic, database clients, schema tools, and bulk data work. Project connection URL plus native PostgreSQL password.

Polygres API or SDK Graph, vector, text, and hybrid retrieval from an application. Project API key such as poly_live_<...> .

The three surfaces work with the same project data, but their credentials are intentionally not interchangeable.

What each surface cannot do

A dashboard session is not an application credential for backend retrieval code.

A PostgreSQL password does not authenticate graph, vector, text, or hybrid API calls.

A project API key does not create projects, run migrations, import data, or reveal the native database password.

Choose the surface by task first, then use the credential that belongs to it.

Use the dashboard for setup and operations

The dashboard is the primary customer interface. It is where your team creates and manages the organization before working with projects.

Common starting points include:

Organization home ( /{organization} ) for the shared workspace,

Members ( /{organization}/members ) for members and fixed roles,

New project ( /{organization}/new ) to create a project,

Project overview ( /{organization}/{projectId} ) for status and navigation,

Connection details ( /{organization}/{projectId}/connect ) for PostgreSQL connection details and project API keys,

Project workspace ( /{organization}/{projectId}/workspace ) for graph, vector, text, and hybrid retrieval work.

Use a dashboard session to import data, browse tables, run SQL, apply migrations, configure graph, vector, and text search, and test hybrid queries. Sensitive actions remain subject to the member’s organization role.

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

After retrieval is configured and tested in the dashboard, create a project API key in Settings ( /{organization}/{projectId}/settings ) and copy the Runtime API URL from connection details ( /{organization}/{projectId}/connect ).

Use the key from trusted backend code to call:

graph retrieval over configured relationships,

vector retrieval over an existing embedding column,

text search through full-text or fuzzy configurations,

hybrid retrieval that combines graph and vector results.

The raw key is shown only when it is created. Store it immediately and use a placeholder such as poly_live_<...> in documentation, examples, and tickets.

A project API key is not a general administration credential. It does not create projects, import data, run migrations, configure retrieval, manage keys, or reveal the native database password. Those remain dashboard or CLI operations.

Query first in the dashboard, then in code

The query workbench ( /{organization}/{projectId}/workspace/query ) is the bridge between product setup and application development.

A practical workflow is:

Configure the relevant graph, vector, or text search in the workspace.

Confirm its build or index is ready. For hybrid, confirm both graph and vector are ready.

Run the query in the dashboard and inspect returned records, paths, scores, and filters.

Create a project API key.

Reproduce the validated graph, vector, text, or hybrid query from a trusted backend using the generated examples or the documented retrieval patterns.

This keeps schema and retrieval decisions visible to SaaS operators while giving application code a stable retrieval interface.

A typical production split

A SaaS application commonly uses both project credentials on the server:

DATABASE_URL and the native PostgreSQL password for transactional product data.

POLYGRES_API_KEY=poly_live_<...> and POLYGRES_RUNTIME_URL=https://{project_id}.api.db.polygres.com/v1 for retrieval features.

The browser talks to your application backend. It should not receive either secret. Team members use their own dashboard sessions for Polygres administration and query testing.

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
