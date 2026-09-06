source: https://docs.evokoa.com/polygres/mcp/workflows
title: Common MCP workflows | Polygres
source_hash: ad603ee1db845d28a38024df08e9e64c83c5c47cc3cd4ed69cf93c25e9009f68
discovered_from: https://docs.evokoa.com/polygres

# Common MCP workflows | Polygres

Common MCP workflows

These workflows show how an AI client combines Polygres tools. Each one starts

with the tools available to the current connection and keeps the selected

project visible throughout the work.

Set up a standard project

Use an organization-wide connection.

Review get_project_creation_options .

Prepare create_standard_project with the selected region and capacity.

Approve the displayed action.

Follow the project with get_project_status .

Check get_retrieval_readiness before adding retrieval features.

If provisioning reports an eligible failure, review the current status and use

retry_project_provisioning with a new action confirmation.

Set up a synchronized project

Start synchronized-project setup in the Polygres Dashboard and enter the

source connection there.

Keep the returned preflight attempt ID.

Review get_synchronized_project_preflight and

list_synchronized_source_tables .

Choose the source tables with select_synchronized_tables .

Create the project with create_synchronized_project .

Follow progress with get_synchronization_status and

get_project_status .

Application writes continue in the source PostgreSQL database. Polygres keeps

the selected tables synchronized for retrieval.

Import a dataset

Inspect and prepare the local dataset.

Open the standard project’s Import page.

Upload the CSV, review the preview, choose the import settings, and start.

Use list_imports to find the job and get_import to follow it.

Verify the result with list_tables and read_table_rows .

cancel_import provides an action review for an eligible running job.

Configure AI Search

Read get_context_capabilities .

Discover a source with discover_context_sources .

Review the collection plan with preflight_context_collection .

Create the collection and follow its operation.

Check status and run verify_context_collection .

Register the filters used by the application.

Generate a query embedding in the client and run one focused retrieval

method.

Keep source keys, scores, provenance, and request IDs with the results.

Use full text for keyword matching, Context search for semantic similarity,

and a hybrid mode when both signals improve the result.

Configure graph retrieval

Run discover_graph_schema and review the verified tables and foreign keys.

Prepare nodes, relationships, filters, and traversal limits.

Save the configuration with configure_graph .

Start build_graph and follow get_graph_status .

Verify a known expansion, related-record lookup, and path or connection

query that matches the application.

Graph relationships come from verified schema and application knowledge. This

keeps paths meaningful and easy to explain.

Build a grounded answer

Inspect the collection status and embedding contract.

Create the query embedding in the client when semantic retrieval applies.

Choose one Context, full-text, or hybrid retrieval tool.

Deduplicate the returned evidence by stable source identity.

Fit the strongest evidence into the answer’s context budget.

Cite the returned source records and keep their provenance.

When the evidence is limited, explain what information would complete the

answer.

Polygres retrieves evidence. The AI client uses that evidence to compose the

answer.

Improve retrieval quality

Start with verify_context_collection , diagnostics, index status, query stats,

and check_context_recall . Use a labeled query set to compare recall,

precision, rank, latency, and empty-result rate at fixed limits. Review graph

direction and depth, text tokenization, filters, freshness, and authorization.

Apply one focused improvement, then run the same evaluation again. This makes

the effect clear and measurable.

Build agent memory

Define the memory owner, tenant, subject, retention period, deletion policy,

stable source identity, and content selected for capture.

Keep credentials, system instructions, retrieved evidence, attachments, and

tool output outside captured memory by default.

For a standard project, run validate_row_write , then use upsert_row with

a stable event key. Include Context reconciliation and a stable idempotency

key when AI Search should update with the write.

For a synchronized project, write the memory record to the source PostgreSQL

database and follow synchronization readiness in Polygres.

Generate embeddings in the client or application. Reconcile the associated

Context point when the collection uses explicit point mappings.

Apply application authorization before and after recall, then preserve the

source identity and provenance of every selected memory.

Use the Python SDK with an application hook, queue, outbox, or worker when

capture needs durable delivery and automatic retries.

Interactive MCP calls work well for reviewed capture and recall. Application

code provides the delivery guarantees for continuous memory collection.
