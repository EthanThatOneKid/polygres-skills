source: https://docs.evokoa.com/polygres/reference/changelog
title: Changelog | Polygres
source_hash: 8b274c771283794ce11cd2a0553769b3b174919393b8b66503580659a15d6d91
discovered_from: https://docs.evokoa.com/polygres

# Changelog | Polygres

Changelog

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

The current dashboard only offers native pgcontext.vector(n) columns in its

Existing vector column picker. It does not delete a Legacy registration

automatically.

The CLI, API, and Python SDK can submit ordinary collection creation for a

compatible public.vector(n) column after any conflicting Legacy

registration is deleted explicitly. The create operation converts the

physical column in place and creates a native collection.

Stored NULL vectors, dimension mismatches, and constraint-backed dependent

indexes block unsafe conversion with specific Context errors.

Developer package versions

Polygres CLI 0.2.0 adds the pgContext, generic API, and notice command surfaces.

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
