source: https://docs.evokoa.com/polygres/platform/query-from-dashboard
title: Query from the dashboard | Polygres
source_hash: b81303ee08f28503e6319e8abf1556f124df6bfd0619c807fd66af626b3d9552
discovered_from: https://docs.evokoa.com/polygres

# Query from the dashboard | Polygres

Query from the dashboard

Polygres provides two dashboard experiences for query testing:

Workspace ( /{organization}/{project_id}/workspace ) keeps query controls beside a visual graph of the project’s registered tables and relationships.

Query Helper ( /{organization}/{project_id}/workspace/query ) provides a larger task form, advanced JSON editing, response preview, generated code, and browser-local history.

Both use the saved project retrieval configuration. Neither substitutes for building a graph or vector index on the setup pages.

Query beside the visual workspace

Use Workspace when the graph context helps you choose records or understand a result.

Open the workspace and inspect the visualized tables and relationships.

Select a table or relationship to focus the sidebar when useful.

Open Run Queries .

Choose the applicable group: Graph , Vector , Text , or Hybrid .

Fill in the compact structured fields and run the query.

The workspace result panel opens as soon as a valid query starts. It shows the running method, then records, paths, scores, trace details, raw response data, or a method-specific empty state. Result records and paths can also highlight relevant parts of the visual graph. Use Load more when the response indicates that another page is available.

The workspace query runner is intentionally compact. Go to the Graph, Vector, or Text Search setup page to discover, build, reindex, or change a configuration.

Use the Query Helper workbench for a repeatable test

Open Query Helper ( /{organization}/{project_id}/workspace/query ).

Under Choose a retrieval task , select a group and the question shape that matches what you are testing.

Complete Task fields . The form uses registered graph tables and vector configurations where available.

Open Advanced only when you need to inspect or edit the synchronized JSON request.

Select Run query , or use Command+Enter on macOS or Control+Enter on Windows and Linux.

Graph tasks cover common shapes such as expanding from a record, inspecting a neighborhood, finding related records, finding a path, or connecting multiple records. Vector tasks cover similarity from an existing row and direct vector search. Hybrid tasks combine graph-first, vector-first, or joint retrieval behavior. Text recipes in the workspace let you test saved TSVector and Fuzzy configurations with query text.

When a task’s required feature is not ready, Query Helper disables execution and shows a scoped notice such as Graph config required , Vector config required , or Hybrid config required . Use Open Graph setup or Open Vector setup from that notice rather than editing around the readiness check.

Test vector search from an existing record

Record-anchor search is the preferred dashboard flow because it does not require you to generate or paste an embedding array.

Choose the Vector task for finding records similar to an existing record.

Select a vector configuration, or leave it unspecified to use the project default.

Enter the row ID of a record whose embedding column is populated.

Set the limit, filters, or similarity bounds available in the form.

Run the query and compare the returned records and scores with the anchor record.

The row ID is looked up through the configuration’s Row ID column. A missing row, empty embedding, wrong configuration, or non-ready HNSW index prevents a useful result.

Literal embedding arrays remain available in Advanced for API testing, but they are not required for the primary record-anchor workflow.

Test text search

From Workspace > Run Queries > Text :

Choose TSVector for term-based, language-aware full-text search or Fuzzy for typo-tolerant similarity.

Select the saved configuration when more than one is available.

Enter representative query text.

Run the query and inspect ranking or similarity in the result preview.

Use real examples from the application, including expected misspellings for Fuzzy search. When a Text task is unavailable or the index is not ready, return to Text-Search Settings ( /{organization}/{project_id}/workspace/text-search ).

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

Vector anchor returns nothing: confirm the row ID, populated embedding, selected/default configuration, and index status.

Graph path is too broad: remove administrative hub relationships and rebuild the graph.

Fuzzy results are noisy: raise the similarity threshold; lower it when expected close matches are missing.

TSVector misses expected terms: check the source column and language parser.

Hybrid task is blocked: both graph and default vector must be ready.

Response failed: keep the request ID and review the error code before retrying.
