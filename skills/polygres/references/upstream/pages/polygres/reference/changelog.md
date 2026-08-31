source: https://docs.evokoa.com/polygres/reference/changelog
title: Changelog | Polygres
source_hash: 8f9e833e792f2dbb8dd73641f75081b1e0079ac63264f538055a2fdb549b74bf
discovered_from: https://docs.evokoa.com/polygres

# Changelog | Polygres

Changelog

2026-08-30

Choose project limits during creation

New projects start with the Free Nano values: 500 MiB Storage, 100,000

Context points, and 100,000 Graph units.

Increasing any value switches the project to the Paid Basic minimum: 2 GiB

Storage, 200,000 Context points, and 200,000 Graph units for $16 per month.

The new-project page now uses one set of Storage, Context, and Graph controls

instead of a separate Free or Paid selector. Use free capacity returns all

three controls to the Free values.

Paid synchronized projects are prepared directly on Basic after source checks

and table selection.

Pay for projects directly

Billing is now based directly on Paid projects. It shows Launch as the

account category when the organization has an active Paid project.

The first Paid project starts the organization’s monthly billing period and

is charged for one full month. Later Paid projects are prorated to the same

next billing date.

Available credits are applied before the payment method. If payment setup is

needed, Stripe Checkout returns to the saved project flow after confirmation.

Billing shows Paid projects, credit and top-up history, the next billing date,

and invoice history. Stripe invoices identify each project and its selected

limits.

Increase or reduce a Paid project’s limits

Open a Paid project’s Upgrade page to add limits immediately or schedule

lower limits for the next billing date.

The dashboard warns when Context or Graph usage approaches its limit and

explains whether to increase the limit or reduce usage.

Graph usage counts each active node as 1 unit and every 10 active edges as 1

unit.

Project pages show configured limits separately from current measured usage.

Synchronized project access

Synchronized project pages focus on source status, table progress, and

retrieval. Continue using the source PostgreSQL database for SQL and writes.

2026-08-25

Improved AI Context error messages

When an AI Context setup, synchronization, or indexing task fails, Polygres

now explains what went wrong and what to do next.

Polygres CLI 0.4.1 shows which step failed

and the operation ID, making it easier to correct the problem, retry, or

contact support.

Polygres SDK 0.4.1 makes the same recovery information

available to applications and logs. Existing SDK methods continue to work

without changes.

AI Context limits

Hourly collection deletion, reindex, reconciliation, and operation-retry

budgets are now 20 per user and project, 10 per API key, and 25 per project.

The IP budget remains 300 per hour. See Limits .

2026-08-20

PlanetScale Postgres is now a first-class synchronized-project source with provider-specific role, logical-replication, and connection guidance.

PlanetScale connection URLs that use sslrootcert=system are accepted while arbitrary client certificate paths remain blocked.

2026-08-19

Sync an existing PostgreSQL database

You can now create a synced project from Supabase, Neon, or another PostgreSQL

database.

Polygres continuously syncs the eligible public schema tables you select.

Each table needs a stable primary or unique key. Tables containing unsupported

columns can offer a supported column subset when the synchronization key

remains available.

Synchronization can be paused, resumed, retried, or reconfigured after

creation.

Synced projects support graph, text, vector, hybrid, and AI Context retrieval.

Database connections, SQL editing, imports, migrations, and row writes remain

on the source database. See how synced PostgreSQL projects

work and the

provider-specific setup guides .

CLI, Python SDK, and Agent Skills

Polygres CLI 0.4.0 adds

polygres projects create sync , a guided command for checking a source,

selecting tables, and creating a synced project. Source credentials are read

from hidden prompts or named environment variables.

Polygres SDK 0.4.0 aligns its

AI Context interface with pgContext 0.2.0 and adds typed operations for

collections, vectors, points, filters, facets, query plans, diagnostics,

telemetry, and embedding migrations.

Existing SDK 0.3.0 methods remain available with unchanged signatures and

behavior. Synced projects return a clear permission error when an application

requests a database connection, while supported retrieval and readiness

operations remain available.

Polygres Agent Skills 0.5.0

can recognize synced projects, guide their creation, and keep writes,

embeddings, and schema changes on the source database.

Retrieval and dashboard improvements

AI Context collection setup now uses one consistent dashboard workflow for

standard and synced projects, including existing source tables and vector

columns.

2026-08-14

Misc Fixes

Returned json and jsonb columns from a Runtime row write now remain

structured values, so applications do not need to decode a JSON string after

a successful write.

AI Context readiness now accounts for collection readiness, current point

reconciliation, and the selected vector index. The dashboard identifies when

a ready collection still needs a project default.

Graph traversal now reports a missing start entity as

GRAPH_NODE_NOT_FOUND . An unknown requested relationship type reports

GRAPH_RELATIONSHIP_TYPE_NOT_FOUND with an actionable correction.

Agent Skills now route one-record writes to the rows surface and datasets to

imports. They reconcile a selected Context collection after an import and

preserve the recovery boundary for Context-backed writes.

Write one row through the Runtime API

Polygres CLI 0.3.0 and SDK 0.3.0 can now

validate, insert, upsert, or ignore one row at a time through the project

Runtime API . This is useful for application

events, agent memory, and other small writes that do not need a bulk import.

You can ask Polygres to return selected columns from the row, and you can

validate the request before changing data .

A row write can also refresh its matching AI Context

point . Context-backed

writes use an idempotency key so you can safely check or resume the Context

step without writing the database row twice.

The CLI and SDK do not automatically replay a write when the server cannot

confirm whether it committed. They return a clear recovery error instead, so

your application can avoid creating duplicate

rows .

A guided way to set up Polygres

Polygres Agent Skills 0.4.0 adds a data-pipeline skill. You

can describe what you want in ordinary language, point it at an accessible

source, and let it inspect a small sample before recommending a setup.

The skill chooses only the pieces that help with your goal. It can work with

files, databases, APIs, or conversations, and can add text, semantic, or

connected-data search when those options are useful. See how guided pipeline

setup works .

Before it uploads data or changes your project, the skill shows one review

covering the project, data scope, external processing, cost, and destructive

effects.

The project dashboard now includes a ready-to-copy prompt that helps your

coding agent review the workspace and recommend a Polygres setup. The data

loading guide

explains when to use this workflow instead of a one-time import.

Clearer errors

Graph depth errors now include the limit configured for your project instead

of showing one fixed number for every plan. See the graph capacity

limits .

Dashboard page errors now give a direct refresh step and make it clearer which

support code to include if the problem continues. See how to handle API

errors for request IDs and safe recovery.

2026-08-13

Graph retrieval update

Graph path and connection searches now follow the relationship types and

directions you select, so results do not use relationships you excluded.

When the same filter name exists on several connected tables, you can choose

which table Polygres should filter. For example, you can make status: open

apply to support tickets instead of customers.

Graph neighborhood results now show accurate counts for each table and its

distance from the starting record. These counts describe the current page of

results.

Errors and limits

Errors are now more consistent across the dashboard, CLI, API, and Python

SDK. Each error includes a code you can use to find the right troubleshooting

steps, and some errors include a more specific reason.

The limits guide now explains how to find the current search result limit for

your project. This helps you choose a valid result count instead of relying on

plan values that may have changed.

2026-08-12

Safer database migrations

Failed migrations now roll back changes made by earlier statements in the

same migration. You will not be left with a partially applied schema change.

Polygres now prevents migration files from ending the managed transaction

early. Remove top-level commands such as BEGIN , COMMIT , END ,

ROLLBACK , ABORT , and PREPARE TRANSACTION from migration files. These

words still work normally inside functions, procedures, and DO blocks.

If another migration is already running, Polygres leaves your migration

unchanged and asks you to retry after the active migration finishes.

Existing dashboard workflows, API routes, and CLI commands continue to work

without changes.

CLI and Python SDK

Polygres CLI 0.2.2 adds commands to inspect, update, diagnose, rebuild, and

remove text-search configurations. TSVector setup now supports generated or

existing columns, compound row keys, metadata and filter columns, and

project-specific result limits.

Polygres SDK 0.2.1 now catches unsupported pgContext operations and requests

that exceed project limits before sending them to Polygres. Existing method

signatures have not changed.

2026-08-11

Text search setup is now one operation

The existing POST /text/configurations endpoint can now create a stored

generated TSVector column, build and verify its GIN index, and save the text

configuration in one request.

The additive tsvector request supports mode: "generate" for one or more

text source columns and mode: "existing" for an existing TSVector column.

The older flat tsvector_column create input remains supported for backwards

compatibility and is now marked deprecated.

Failed generated-column setup attempts automatic cleanup of the new column,

index, and configuration. An explicit cleanup error is returned if that

recovery is incomplete.

TSVector and Fuzzy configurations now include physical-index diagnostics and

reindex operations. Queries support configured default and maximum limits,

compound row keys, exact NULL filters, and cursors bound to the original

query while continuing to accept older cursors.

Dashboard, CLI, and SDK

Text Search setup now uses the configuration endpoint directly. Auto Scan and

manual generated-column setup no longer create or apply a separate migration.

The dashboard adds index diagnostics, rebuild actions, metadata and filter

fields, compound row keys, result limits, and a TSVector or Fuzzy Search

Preview.

The Python SDK keeps its existing query interface:

project.text.tsvector(...) and project.text.fuzzy(...) . Setup remains a

dashboard, API, or CLI workflow, so current SDK query code does not need to

change.

Polygres Agent Skills 0.3.1 updates CLI operations, SDK integration,

retrieval design, and troubleshooting guidance for the completed text-search

behavior. It requires Polygres CLI 0.2.1 .

2026-08-10

A smoother pgContext experience

Creating collections from existing vector columns is now more reliable. Your selected setup option stays in place while Polygres checks the project.

Deleting a collection no longer removes its source table when another collection still uses it.

Graph-aware search now works correctly with mixed-case schema and table names.

When an older vector workflow needs to be migrated, the CLI now provides clearer upgrade instructions and the command to run.

Developer tools

Polygres SDK 0.2.0 now works correctly on Python 3.10.

Dashboard connection guides now help you confirm that your CLI and SDK are up to date before starting an integration.

Earlier client versions are being retired. Upgrade to Polygres CLI 0.2.1 and SDK 0.2.0 to avoid interrupted API access.

Dashboard improvements

Fixed an issue that could interrupt account setup after repeated sign-ins.

2026-08-08

pgContext AI Search Preview

Introducing pgContext AI Search, a new way to build semantic, keyword, filtered, and graph-aware search over your project data.

Create searchable collections from existing data, keep them synchronized as your data changes, and combine multiple retrieval methods to build relevant search experiences.

Get started with the configuration guide , or explore the CLI , Python SDK , and API reference .

AI Context collections support multiple vectors

One pgContext collection can now contain multiple named vector columns over

the same source table. Collection creation supplies the initial vector, which

becomes that collection’s default vector.

Add vectors from the collection table in the dashboard. You can select a new

default vector without changing the project’s default collection. Ranked

retrieval can select an exact vector_name ; omitting it uses the collection

default.

Vector setup now separates pgContext collections and Legacy into two

tabs. Each pgContext collection has its own table of vectors.

The Legacy tab and Legacy retrieval expose only persisted registrations

that are effectively Ready. HNSW registrations require their exact physical

index to be Ready. Existing exact-scan registrations can be Ready without

HNSW. Physical-only pgvector indexes cannot be registered or enabled through

the retired API.

Existing pgvector conversion is available through public automation

The dashboard labels retired pgvector registrations as Legacy and

explains that they should be replaced with a pgContext collection.

The dashboard offers eligible native pgcontext.vector(n) and compatible

pgvector.vector(n) columns in its Existing vector column picker. After

explicit confirmation, it creates the collection or additional vector and

then deletes the conflicting Legacy registration automatically.

The CLI, API, and Python SDK can submit ordinary collection creation for a

compatible public.vector(n) column after any conflicting Legacy

registration is deleted explicitly. The create operation converts the

physical column in place and creates a native collection.

Stored NULL vectors, dimension mismatches, and constraint-backed dependent

indexes block unsafe conversion with specific Context errors.

Developer package versions

Polygres CLI 0.2.1 adds the pgContext, generic API, and notice command surfaces.

Polygres SDK 0.2.0 adds the project.context namespace and version notices.

Polygres Agent Skills 0.3.0 documents safe migration of compatible

pgvector columns into native pgContext collections.

New vector setup moves to pgContext collections

New pgvector configuration registration is retired across the dashboard,

CLI, API, and Python SDK. Older creation calls return

VECTOR_CREATION_RETIRED .

Use a pgContext collection with a native pgcontext.vector(n) column for new

vector setup.

Previously registered vector configurations continue to support maintenance.

Legacy retrieval requires a persisted registration that is effectively

Ready. HNSW configurations require a Ready physical index; existing

exact-scan configurations do not. The CLI can guide selection of an eligible

Ready registration and then submit ordinary native collection creation when

the certified compatibility extension is available.

Platform updates

Maintenance notices now keep users informed when project changes are temporarily paused. Project information remains available in read-only mode during maintenance.

Runtime settings now show the installed pgContext version.

Dashboard improvements

Improved the reliability of Graph setup after saving or rebuilding a graph.

Query Helper now identifies invalid inputs before running a query.

2026-07-20

Accounts and teams

Organization invitations now have a clearer review flow. After signing in, you can choose which organization to join, verify your email if needed, or decline the invitation and create your own organization.

Projects and data

Project API Keys are displayed immediately after creation. Copy the secret when it appears because it cannot be shown again.

Graph and vector readiness now reflects the actual database configuration more accurately, reducing false ready states after configuration or index changes.

Developer tools

Polygres CLI 0.1.2 increases the supported CSV upload size to the storage allowance of your project tier and improves upload reliability.

polygres-skills

Released an expanded polygres-skills package for Polygres operations and Python retrieval:

polygres-cli operates projects, imports, migrations, credentials, and retrieval setup;

polygres-sdk builds Python graph, vector, text, and hybrid retrieval.

Install the package with npx skills add Evokoa/polygres-skills , or through the Polygres plugin marketplace for Codex or Claude Code.

2026-07-09

Polygres CLI 0.1.0

Added browser-based sign-in and commands for managing projects, connection details, Runtime API Keys, CSV imports, and migrations.

Added graph, vector, and text-search configuration commands, plus retrieval-readiness checks.

Added JSON output, stable exit codes, and confirmation prompts for automation and destructive operations.

Runtime API Key secrets are shown once when created and are excluded from later list and environment output.
