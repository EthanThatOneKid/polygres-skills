source: https://docs.evokoa.com/polygres/sdk/configure-retrieval
title: Dashboard retrieval setup | Polygres
source_hash: aa3f360619ec8d7b3d41aac9343d67e61113033b8d4ce9c7774314475f09ce17
discovered_from: https://docs.evokoa.com/polygres

# Dashboard retrieval setup | Polygres

Dashboard retrieval setup

Retrieval setup does not replace data modeling. It tells Polygres which existing tables, relationships, embedding columns, and text columns should participate in retrieval. Start after your schema and initial data are present.

Legacy Vector and Legacy Hybrid are deprecated compatibility surfaces for

existing pgvector registrations. New vector and hybrid workflows use pgContext

AI Search, which brings semantic, lexical, filter, graph, and Joint retrieval

into one collection-centered setup.

Prepare the source data

Before configuring a feature, confirm its source data has the required shape:

Retrieval feature Source data it needs

Graph Tables with stable primary or unique identifiers and meaningful relationships between columns.

Legacy Vector (deprecated) A vector(n) column whose rows already contain embeddings, plus a stable row ID column from a previously registered configuration.

Text search A text or existing tsvector column, plus a stable row ID column.

Legacy Hybrid (deprecated) A ready graph build and at least one persisted Legacy vector registration that is effectively Ready. If no effective default exists, the request must name an exact configuration.

pgContext AI Search A stable source key, native pgcontext.vector(n) column or reviewed column/table creation plan, and optional text, result, and filter columns.

Use Tables ( /{organization}/{project_id}/tables ) or SQL editor ( /{organization}/{project_id}/sql ) to verify the schema and data before setup.

Configure graph retrieval

Open Graph setup ( /{organization}/{project_id}/workspace/graph ).

Discover and register node tables

Select Auto discover to scan public.* tables that have stable primary or unique keys and to propose relationships based on the schema. Auto discovery replaces the current node registrations and edge suggestions, so review any existing manual setup before running it.

Review the proposed tables under Nodes . Eligible tables from non-system custom schemas are shown by default for manual selection, even though Auto discover scans only public . Clear Include non-public tables to hide them. System and extension schemas are never shown.

Confirm the identifier column for each node table.

Disable irrelevant tables. When a disabled node has connected edges, confirm the warning because those edges are removed with it.

Auto discovery is a starting point, not an instruction to register the entire database. Use Advanced only for the additional graph settings your retrieval design requires; keep the Nodes and Edges tabs as the main review surface.

Select meaningful relationships

Under Edges , add or review each relationship by choosing:

source table and source column,

target table and target column,

a label that describes the relationship, and

forward-only or both-direction traversal.

Register an edge when the hop itself helps answer a retrieval question. Avoid broad administrative hubs—such as organization, tenant, workspace, account, team, region, category, tag, role, audit, or generic event tables—unless the question is specifically about that hub. Those tables can connect many unrelated records and produce technically connected but unhelpful paths.

Enable both directions only when the reverse hop is meaningful. For example, “ticket opened by customer” may reasonably support traversal from ticket to customer and customer to tickets; an audit ownership edge may not.

See Choosing graph relationships for detailed selection patterns and examples.

Save and build the graph

Graph changes remain an in-page draft until you save or build them. A saved configuration is not query-ready until it has been built.

Resolve any unsaved-change or invalid-configuration notice.

Select Save to persist the draft without building, or select Rebuild Graph to save pending edits and start the build.

Wait while the status moves through Queued or Building .

Confirm Ready before running graph or hybrid queries.

One rebuild click is enough while work is queued or building; the dashboard blocks duplicate submissions.

A configuration can also show Not built , Stale , or Failed . Stale means the saved setup changed after the last successful build. For a failure, review nodes and relationships, correct invalid selections, and select Rebuild Graph again.

Polygres reconciles the saved dashboard configuration with the graph registration actually applied inside the database. A saved record alone does not make the graph ready. Ready means the current graph definition has been built and can serve a query. If an extension update, interrupted build, or manual database change causes the database graph to differ from the saved definition, the dashboard reports it as stale or drifted until a successful rebuild applies the current setup.

Tables that use FORCE ROW LEVEL SECURITY cannot be included in a graph build. Remove those tables from the graph or choose a retrieval design that keeps their access rules intact.

Maintain deprecated Legacy Vector retrieval

New pgvector configuration registration is retired. Open AI Context (Vector) setup

( /{organization}/{project_id}/workspace/context ) to create and manage

pgContext collections. Use a collection for every new searchable vector source;

do not try to register a new legacy vector configuration through the dashboard,

CLI, API, or Python SDK.

Previously registered pgvector configurations remain available for existing

vector and hybrid integrations. The dashboard identifies them as legacy

registered columns under the Legacy tab for standard projects. The Legacy status tooltip

directs you to create a pgContext collection to replace the old configuration.

Only persisted enabled registrations that are effectively Ready appear in

this tab and remain usable by legacy retrieval. HNSW requires the registration’s

exact physical index to be Ready; an existing index_kind: none registration

can be Ready for exact scan without HNSW. An unregistered physical pgvector

index is not a supported legacy source. There is no dashboard or API action to

register or re-enable one.

The pgContext collections tab renders each collection as a separate table.

The rows are the collection’s named vector columns, including their dimensions,

metric, index state, and default status. Every collection has one default

vector. Select Add vector to attach another existing vector column or add a

new vector column to the same source table, then wait for the durable operation

and, for index_kind: hnsw , its managed index. index_kind: none uses exact

scan without an HNSW index. Select Make default to change which vector

ranked retrieval uses when vector_name is omitted.

Collection and vector defaults are separate. At most one collection is the

project default; every collection independently has one default vector. The

first user-created collection becomes the project default automatically, and

the vector supplied during collection creation becomes that collection’s

default. Deleting the project default does not promote another collection, so

select a replacement explicitly when default resolution is required.

Select Create collection to open the configuration form. Opening the modal

does not run source discovery by itself. When Existing vector column is the

active source mode, the tab shows its loading state while Polygres searches for

eligible native pgcontext.vector(n) columns, then renders those sources. The

current dashboard picker does not offer public.vector(n) columns.

Deleting an item on the Legacy tab removes only that persisted legacy

registration. It does not automatically create a pgContext collection or

convert the database column. To convert a compatible pgvector source in place,

use an explicitly reviewed ordinary collection-creation request through the

CLI or public API after resolving the legacy registration. That operation can

take an ACCESS EXCLUSIVE lock, drop non-constraint indexes that depend on the

column, convert it to pgcontext.vector(n) NOT NULL , and create a managed

index. Actual NULL vectors, dimension mismatches, and constraint-backed

dependent indexes block conversion.

The dashboard’s collection Rebuild action, like the CLI reindex command,

rebuilds only the collection’s current default vector index. It does not rebuild

every named vector.

Collection deletion follows the source ownership recorded at creation.

existing and add_column preserve the source table and rows. An owned

new_table source is permanently dropped with the collection after identity

and exclusive-ownership checks, even though the current dashboard confirmation

copy says source tables stay unchanged.

Maintain a previously registered configuration

The following settings and lifecycle actions apply only to configurations that

were registered before creation was retired.

Choose a metric

Metric Choose it when

Cosine You care about vector direction and are using a typical semantic embedding model. This is the dashboard default.

Inner product The model or ranking design explicitly expects dot-product scoring.

L2 The model expects Euclidean distance.

Changing the metric changes how nearest neighbors are ranked and requires an index compatible with that metric.

Build and reindex HNSW

The index can show states such as Missing , Creating , Ready , Stale , or Failed .

Wait for Creating to become Ready before testing vector or hybrid retrieval.

Use Reindex after a configuration change that makes the current index stale.

Use the retry or Reindex action when an HNSW build fails.

Check the populated embeddings, dimensions, row ID, and metric before retrying the same failed definition.

Deleting a legacy registration does not delete its database vector column or

embedding values. Retired registrations cannot be created or re-enabled.

Polygres can adopt an existing compatible HNSW index instead of rebuilding it. The index must target the configured embedding column directly, use the operator class that matches the selected metric, be valid and ready, and have a supported predicate. A non-partial index is supported. A partial index is supported only when its predicate is exactly the indexed embedding column IS NOT NULL . Expression indexes and other partial predicates are reported as unsupported rather than silently treated as ready.

When an adopted physical index no longer matches the saved dimensions, metric, row ID, operator class, index kind, or index name, the configuration becomes Stale . Review the discovered definition before reindexing so Polygres does not replace an intentionally different database index.

Set the project default

Choose one enabled, effectively Ready vector configuration as the default when requests should be able to omit config . Hybrid readiness requires graph readiness plus at least one effectively Ready persisted registration; if several are Ready and none is default, readiness reports selection_required and each request must name one exactly.

Changing the default does not rewrite embeddings. It changes which configured table and vector column an unspecified query uses.

Configure text search

Open Text-Search setup ( /{organization}/{project_id}/workspace/text-search ). Text search is a first-class retrieval workflow with two different configuration kinds.

Choose TSVector or Fuzzy

Kind Best for Configuration behavior

TSVector Search Longer natural-language fields such as titles, descriptions, notes, content, and articles; exact terms, word variants, and ranked matches. Uses an existing tsvector column or creates a generated stored tsvector column from text, with a selected language parser.

Fuzzy Search Names, codes, labels, and short phrases where misspellings, partial text, or close matches should still succeed. Searches a normal text column using a similarity threshold from 0 to 1. It does not create a tsvector column.

A higher fuzzy threshold is stricter; a lower threshold accepts looser matches. Start with the dashboard default of 0.3 , test representative queries, and adjust based on false positives and missed matches.

Set up TSVector with Auto Scan

Select Add configuration and choose TSVector Search .

Select Auto Scan .

Review the proposed columns. The scan favors likely content fields, requires a stable single-column primary key, and excludes oversized values and obvious IDs, code fields, join tables, and internal configuration tables.

Select the proposals you actually want to search.

Select Set Up n Columns .

For each selected plain-text column, the dashboard sends one request to the

existing text configuration endpoint. Polygres creates a generated

<column>_tsv column using the English parser, builds and verifies its GIN

index, and saves the configuration as one operation. It does not create a

migration. Auto Scan excludes a candidate when any checked value exceeds 1 MB.

Set up TSVector manually

Use manual setup when you need a different table, column, row ID, language, or an existing tsvector column.

Choose TSVector Search and scroll to Manual setup .

Select the table and source column.

Select the Row ID Column .

Choose English , Simple , Spanish , or French as the Language Parser .

Select Create Configuration .

When the selected source is ordinary text, the dashboard creates a stored

generated tsvector column through POST /text/configurations . PostgreSQL

keeps that generated value current when the source text changes. When the

selected column is already a tsvector , Polygres registers it directly without

changing the table.

Set up Fuzzy manually

Select Add configuration and choose Fuzzy Search .

Select the table, text column, and Row ID Column .

Enter a Similarity Threshold between 0 and 1.

Select Create Configuration .

Maintain text configurations

The configuration list shows Config Name , Kind , Table , Column ,

Row ID , language or threshold details, and Status . Manual setup also

accepts metadata columns, filter columns, default and maximum result limits,

and compound row keys. You can edit an existing configuration, inspect index

diagnostics, rebuild its index, test a query in Search Preview, or delete a

configuration that is no longer needed.

A status notice can show Text Search Inactive , Text Search Index

Building , or Text Search Index Failed . For a failure, open diagnostics,

correct the selected columns or row key, then use Rebuild . Search Preview

calls /text/tsvector or /text/fuzzy for the selected ready configuration and

accepts JSON exact-match filters.

Deleting a configuration removes its managed index. It does not drop a stored

generated TSVector column from the source table.

List existing TSVector and Fuzzy configurations before creating another so the saved search names and source columns remain easy to identify.

Confirm deprecated Legacy Hybrid readiness

Hybrid retrieval combines graph and vector signals. It is ready only when:

the graph configuration has a successful Ready build, and

the selected or default persisted Legacy vector registration is effectively

Ready . HNSW requires its exact physical index to be Ready; index_kind: none can be Ready for exact scan without HNSW.

Text-search readiness is independent; it does not substitute for graph or vector readiness in a hybrid query.

Configure pgContext AI Search

pgContext is the supported path for new vector setup. It uses

collection-specific capabilities, preflight, verification, and durable

operations. The dashboard’s AI Context (Vector) setup manages the same collection lifecycle.

An ordinary collection-creation request through the CLI or API can migrate a

compatible pgvector embedding column in place after an explicit review. The

CLI’s polygres context init command guides candidate selection from eligible

persisted legacy registrations, but then submits the same ordinary native

collection-creation request. It is not a public same-column bridge and is not

the dashboard’s collection-creation workflow.

For an interactive setup:

Select the intended project with the Polygres CLI .

Run polygres context capabilities and discover eligible source tables.

Preflight the exact source, vector, text, result-column, and filter plan.

Review any proposed schema change and ownership details.

Create the collection and wait for its durable operation. Its initial vector

becomes the collection default.

Add any additional named vectors through the dashboard, public API, or

Python SDK, wait for each operation, and set the intended default vector.

The current CLI has no add-vector or set-default-vector command.

Verify the collection and each vector index, then inspect status,

diagnostics, filters, and point mappings as the application evolves.

Backend services that explicitly own collection provisioning can use project.context in the Python SDK . The application supplies embeddings with the selected vector’s dimensions. Authorize the request from trusted server-side identity before retrieval, then derive any collection filter used for result scoping; registered filters are not an authorization boundary.

Readiness checklist

Before testing graph, vector, text, or Hybrid retrieval in the dashboard, confirm:

Graph: saved configuration, meaningful nodes and edges, latest build Ready .

pgContext: collection ready, point reconciliation current, and the

intended vector index Ready when it uses HNSW. Collection and vector

defaults must be understood, and vector_name supplied when the query should

not use the collection default.

Legacy vector: persisted enabled registration exists, embeddings are

populated, stable row ID, appropriate metric, and effective readiness. HNSW

requires its exact physical index to be Ready; index_kind: none does not.

Text: TSVector or Fuzzy configuration exists and its index is ready.

Legacy Hybrid: graph is Ready and at least one persisted Legacy vector

registration is effectively Ready. Supply an exact configuration when

readiness reports selection_required .

Continue with Retrieval integration patterns .

For pgContext, confirm that the selected capability is available, including point scrolling when you need to inspect mappings. Confirm that the collection is ready and passes verification. Point listings respect source-table row-level security and can be empty while more visible results remain, so continue while has_more is true. Exercise the intended method through the CLI, API, or SDK, then continue with pgContext application patterns .
