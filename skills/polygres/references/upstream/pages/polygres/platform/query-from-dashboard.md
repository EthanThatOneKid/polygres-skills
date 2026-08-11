source: https://docs.evokoa.com/polygres/platform/query-from-dashboard
title: Query from the dashboard | Polygres
source_hash: fa103b9acdd3b3b98a065ee2e480b27e617377729e49076909050007ee43f400
discovered_from: https://docs.evokoa.com/polygres

# Query from the dashboard | Polygres

Query from the dashboard

Query Helper ( /{organization}/{project_id}/workspace/query ) provides structured task forms, advanced JSON editing, response previews, generated code, and browser-local history. The visual Workspace does not contain a separate query runner.

Query Helper supports graph tasks and retrieval through existing Legacy vector registrations. It does not query pgContext collections or saved text-search configurations. Use the API, SDK, or CLI for pgContext retrieval, and use the API or SDK for text retrieval.

Use the Query Helper workbench for a repeatable test

Open Query Helper ( /{organization}/{project_id}/workspace/query ).

Under Choose a retrieval task , select a group and the question shape that matches what you are testing.

Complete Task fields . The form uses registered graph tables and vector configurations where available.

Open Advanced only when you need to inspect or edit the synchronized JSON request.

Select Run query , or use Command+Enter on macOS or Control+Enter on Windows and Linux.

Graph tasks cover common shapes such as expanding from a record, inspecting a neighborhood, finding related records, finding a path, or connecting multiple records. Vector tasks cover similarity from an existing row and direct vector search. Hybrid tasks combine graph-first, vector-first, or joint retrieval behavior.

For record-based graph queries, the table selector shows registered tables with one ID column. Tables with multi-column IDs are not available for this query type. Query Helper also highlights incomplete fields and invalid embedding values before sending the request.

When a task’s required feature is not ready, Query Helper disables execution and shows a scoped notice such as Graph config required , Vector config required , or Hybrid config required . Use Open Graph setup or Open Vector setup from that notice rather than editing around the readiness check.

Vector and Hybrid tasks require a persisted enabled Legacy vector registration that is effectively Ready . HNSW configurations require their exact physical index to be Ready; an existing index_kind: none configuration can be Ready for exact scan without HNSW. A physical pgvector index without that persisted registration is not implicitly usable. The retired Legacy setup APIs cannot create a new registration or re-enable one, so Query Helper should be treated as a testing surface for qualifying registrations that already exist.

Test vector search from an existing record

Record-anchor search is the preferred dashboard flow because it does not require you to generate or paste an embedding array.

Choose the Vector task for finding records similar to an existing record.

Select a Ready Legacy vector registration. If the task permits omission, Query Helper uses the project’s default qualifying Legacy registration.

Enter the row ID of a record whose embedding column is populated.

Set the limit, filters, or similarity bounds available in the form.

Run the query and compare the returned records and scores with the anchor record.

The row ID is looked up through the registration’s Row ID column. A missing row, empty embedding, wrong registration, or registration that is not effectively Ready prevents a useful result.

Literal embedding arrays remain available in Advanced for API testing, but they are not required for the primary record-anchor workflow.

Read the response preview

Query Helper switches the Console to Results when execution starts. A successful preview can contain:

returned records and their identifying fields,

graph paths and traversed relationships,

vector or hybrid scores,

trace or warning information,

a result count and pagination state,

elapsed time, and

a request ID.

Use a follow-up action offered on a result when you want to continue from that record, and use Load more when a next cursor is available. An empty result is different from a failed query: it means the request ran but matched nothing under the current configuration, filters, depth, threshold, or limit.

A failed query shows a safe error message, error code, and request ID. Preserve that request ID when the problem appears to be platform-side.

Move from a successful test to application code

Open the Code tab after configuring the task. It mirrors the current request and generates Python SDK and cURL examples. Project API Key values are referenced through environment variables rather than inserted into the snippet.

Create the key in Settings > Project API Key , store it in a secret manager, and use the generated code from a server-side application. See Security basics .

Reuse browser-local query history

The History tab records query executions for the current project in the current browser. Select an entry to reload its task and fields, or select Clear to remove local history.

History is a convenience for iteration. It is not a shared organization history or a replacement for application observability.

Troubleshoot an unexpected result

Task cannot run: follow the readiness notice to the required setup page.

Graph table is missing from a record selector: use a registered table with exactly one ID column; compound-key tables are not valid record anchors.

A required value is incomplete: complete the highlighted task field or replace the placeholder in Advanced JSON before running the query.

Vector anchor returns nothing: confirm the row ID, populated embedding, selected or default qualifying Legacy registration, and effective index status.

Graph path is too broad: remove administrative hub relationships and rebuild the graph.

Hybrid task is blocked: the graph and the selected or default qualifying Legacy vector registration must both be ready.

A pgContext collection is missing: Query Helper does not query pgContext. Use project.context in the SDK, the pgContext Runtime API, or the corresponding CLI workflow.

A text configuration is missing: Query Helper does not provide text recipes. Use the API or SDK after confirming the configuration in Text Search setup.

Response failed: keep the request ID and review the error code before retrying.
