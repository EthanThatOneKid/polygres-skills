source: https://docs.evokoa.com/polygres/reference/changelog
title: Changelog | Polygres
source_hash: 1368ac3936248e04018e4c906ea61dd698f165f7d5bc5e60c73e6c70f89f90e0
discovered_from: https://docs.evokoa.com/polygres

# Changelog | Polygres

Changelog

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
