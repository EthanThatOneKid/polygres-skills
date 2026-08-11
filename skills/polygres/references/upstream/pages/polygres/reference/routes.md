source: https://docs.evokoa.com/polygres/reference/routes
title: Retrieval routes | Polygres
source_hash: 2f19599958d7f9a96da6d01b17973732caa8ef77d80bf4c23a75d853343eb5b1
discovered_from: https://docs.evokoa.com/polygres

# Retrieval routes | Polygres

Retrieval routes

This page covers retrieval routes, not every dashboard or control-plane route.

Gateway retrieval paths are relative to the gateway API base URL, such as

https://api.polygres.com/v1 . Runtime retrieval paths are relative to the

project Runtime API URL copied from Connect > API & SDK , such as

https://p0123456789abcdef0123456.api.db.polygres.com/v1 .

Authentication labels

Label Credential

Public No bearer credential.

Dashboard Authorization: Bearer <dashboard_session_jwt> .

Retrieval Authorization: Bearer poly_live_<32hex> sent to the project Runtime API URL. Dashboard query surfaces may use a dashboard session through gateway-managed calls.

An API key used on a dashboard-only route returns AUTH_MODE_NOT_ALLOWED .

Graph

Method Route Auth Purpose

POST /graph/expand Retrieval Expand from one entity.

POST /graph/neighborhood Retrieval Return a neighborhood around one entity.

POST /graph/related Retrieval Return related entities.

POST /graph/path Retrieval Find paths between source and target entities.

POST /graph/connection Retrieval Find connections among two to ten entities.

Vector

These retrieval routes require a persisted vector configuration registered

before new pgvector registration was retired. It must be effectively Ready. An

HNSW configuration requires its exact physical index to be Ready; an existing

index_kind: none configuration can be Ready for exact-scan retrieval without

HNSW. Unregistered physical pgvector indexes are never discovered as implicit

Legacy configurations. For new vector setup and retrieval, use a pgContext

collection and the /context routes.

Method Route Auth Purpose

POST /vector/search Retrieval Search with a supplied embedding.

POST /vector/similar-to Retrieval Search from an existing row ID.

Text

Method Route Auth Purpose

POST /text/tsvector Retrieval Search with a saved tsvector configuration.

POST /text/fuzzy Retrieval Search with a saved fuzzy configuration.

Hybrid

Method Route Auth Purpose

POST /hybrid/graph-first Retrieval Produce graph candidates, then score them with vector search.

POST /hybrid/vector-first Retrieval Produce vector candidates, then evaluate graph context.

POST /hybrid/joint Retrieval Combine graph and vector rankings with Reciprocal Rank Fusion.

These are the pgvector-backed hybrid routes. The collection-based pgContext surface uses separate /context/hybrid/* routes. Context rank-fusion combines independent pgContext and pgGraph rankings, while Context joint couples candidate generation, graph expansion, combined-pool pgContext rescoring, and one final weighted reciprocal-rank fusion. These Context routes are distinct from the pgvector-backed /hybrid/joint route above.

Legacy /hybrid/joint does not delegate through a pgContext compatibility binding. If the selected legacy vector configuration has an active pgContext binding, the route returns USE_CONTEXT_HYBRID_JOINT ; call /context/hybrid/joint with the bound Context collection instead.

pgContext AI Search

The pgContext Preview API exposes 40 collection-based routes. Use either the Gateway base /projects/{project_id}/context with a dashboard or CLI bearer credential, or the project Runtime base /context with a project_full Runtime API key.

Area Routes

Capabilities and sources GET /capabilities ; POST /discover ; POST /preflight

Collections list, create, get, status, verify, diagnostics, update, delete, reindex, and add named vectors under /collections

Filters and points registered column and JSONB filters; point status, scroll, upsert, delete, and reconcile

Operations list, get, cancel, and retry durable operations

Aggregates POST /count ; POST /facets

Retrieval dense, grouped, recall, text hybrid, graph first, vector first, rank fusion, and coupled Joint; ranked routes accept an optional exact vector_name

See the pgContext API reference for every method, path, permission, core request convention, and lifecycle examples.

Readiness

Method Route Auth Purpose

GET /retrieval/readiness Retrieval Return graph, aggregate Legacy-vector, and hybrid readiness. Text and pgContext collection readiness are not included.

Aggregate Legacy-vector readiness is true when at least one persisted

configuration is effectively Ready. When several are Ready and none is the

default, the response sets selection_required ; the query must name an exact

configuration.

Response conventions

Successful and error responses include a top-level request_id . Errors also use an error object with code , message , and details .

For a gateway-proxied request, X-Request-ID identifies the gateway request. The JSON body’s request_id and the optional X-Polygres-Upstream-Request-ID header identify the corresponding Runtime request. Preserve both IDs when contacting support.

Cursor-paginated retrieval responses return next_cursor and has_more . Treat cursors as opaque and send next_cursor back as cursor .
