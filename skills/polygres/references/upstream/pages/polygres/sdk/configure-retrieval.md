source: https://docs.evokoa.com/polygres/sdk/configure-retrieval
title: Configure retrieval | Polygres
source_hash: 1e0e55fb558b86cad7d24dcc9bde05839efd846b47eff08821f8b5bec82a7520
discovered_from: https://docs.evokoa.com/polygres

# Configure retrieval | Polygres

Configure retrieval

Retrieval setup does not replace data modeling. It tells Polygres which existing tables, relationships, embedding columns, and text columns should participate in retrieval. Start after your schema and initial data are present.

Prepare the source data

Before configuring a feature, confirm its source data has the required shape:

Retrieval feature Source data it needs

Graph Tables with stable primary or unique identifiers and meaningful relationships between columns.

Vector A vector(n) column whose rows already contain embeddings, plus a stable row ID column.

Text search A text or existing tsvector column, plus a stable row ID column.

Hybrid A ready graph build and a ready default vector configuration.

Use Tables ( /{organization}/{project_id}/tables ) or SQL Editor ( /{organization}/{project_id}/sql ) to verify the schema and data before setup.

Configure graph retrieval

Open Graph setup ( /{organization}/{project_id}/workspace/graph ).

Discover and register node tables

Select Auto discover to scan tables that have stable primary or unique keys and to propose relationships based on the schema. Auto discovery replaces the current node registrations and edge suggestions, so review any existing manual setup before running it.

Review the proposed tables under Nodes . Enable only tables that represent entities you want retrieval to traverse.

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

Graph changes save automatically after a brief pause. A saved configuration is not query-ready until it has been built.

Resolve any unsaved-change or invalid-configuration notice.

Select Rebuild Graph .

Wait while the status moves through Queued or Building .

Confirm Ready before running graph or hybrid queries.

A configuration can also show Not built , Stale , or Failed . Stale means the saved setup changed after the last successful build. For a failure, review nodes and relationships, correct invalid selections, and select Rebuild Graph again.

Configure vector retrieval

Open Vector setup ( /{organization}/{project_id}/workspace/vector ). Polygres scans the project for existing vector(n) columns and shows their dimensions, populated-row count, row-ID choices, search status, and whether each configuration is enabled.

Use an existing embedding column

An existing vector column is useful only after its rows contain embeddings produced by your embedding model or pipeline. Polygres does not infer that a non-null vector is semantically correct for your application.

Find the table and vector column.

Confirm that Rows populated is greater than zero and reflects the records you expect to search.

Choose a stable Row ID column, normally the table’s primary key.

Enable the column for vector search.

Review the generated search configuration and wait for its index to become Ready .

When the column has no populated embeddings, the configuration remains pending or not ready even if the column exists.

Add an embedding column

Use Add embedding column when the table does not yet have a vector column.

Select the table.

Enter a column name; embedding is the default.

Choose the embedding dimensions. The setup offers common sizes such as 384, 512, 768, 1024, 1536, and 2000.

Review the SQL preview and create the column.

Populate that column from your application, an embedding job, an import, or SQL.

Return to Vector setup and enable it after values exist.

Creating the column does not generate embeddings. HNSW-indexed configurations support dimensions up to 2000 in this workflow, so choose a size that matches the model output exactly.

Understand the initial configuration

Enabling an eligible vector column creates a search configuration with dashboard defaults:

a search name derived from the table and column,

the first eligible row-ID candidate,

Cosine distance,

an HNSW index, and

no metadata or filter columns until you add them.

Review these values rather than assuming every embedding model uses the defaults.

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

Disabling a search configuration does not delete its database vector column or embedding values.

Set the project default

Choose one enabled, ready vector configuration as the default . Polygres uses it when a vector query does not name a specific configuration. Hybrid readiness also depends on this default being ready.

Changing the default does not rewrite embeddings. It changes which configured table and vector column an unspecified query uses.

Configure text search

Open Text-Search Settings ( /{organization}/{project_id}/workspace/text-search ). Text search is a first-class retrieval workflow with two different configuration kinds.

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

For a selected plain-text column, Polygres creates a generated <column>_tsv column using the English parser and registers the text configuration. Auto Scan excludes a candidate when any checked value exceeds 1 MB.

Set up TSVector manually

Use manual setup when you need a different table, column, row ID, language, or an existing tsvector column.

Choose TSVector Search and scroll to Manual setup .

Select the table and source column.

Select the Row ID Column .

Choose English , Simple , Spanish , or French as the Language Parser .

Select Create Configuration .

When the selected source is ordinary text, the dashboard creates a generated tsvector column. When it is already a tsvector , Polygres registers that column directly.

Set up Fuzzy manually

Select Add configuration and choose Fuzzy Search .

Select the table, text column, and Row ID Column .

Enter a Similarity Threshold between 0 and 1.

Select Create Configuration .

Maintain text configurations

The configuration list shows Config Name , Kind , Table , Column , Row ID , language or threshold details, and Status . You can change the table, eligible column, row ID, language, or threshold from the list, or delete a configuration that is no longer needed.

A status notice can show Text Search Inactive , Text Search Index Building , or Text Search Index Failed . For a failure, review the selected column and row ID, then save the corrected configuration again to retry the index build.

TSVector and Fuzzy configuration counts can each be limited by the project tier. Delete an unused configuration or change the applicable tier when no slots remain.

Confirm hybrid readiness

Hybrid retrieval combines graph and vector signals. It is ready only when:

the graph configuration has a successful Ready build, and

the selected or default vector configuration has a Ready index.

Text-search readiness is independent; it does not substitute for graph or vector readiness in a hybrid query.

Readiness checklist

Before testing in the dashboard, confirm:

Graph: saved configuration, meaningful nodes and edges, latest build Ready .

Vector: embeddings populated, stable row ID, appropriate metric, HNSW Ready , default selected.

Text: TSVector or Fuzzy configuration exists and its index is ready.

Hybrid: both graph and default vector requirements are ready.

Continue with Query from the dashboard .
