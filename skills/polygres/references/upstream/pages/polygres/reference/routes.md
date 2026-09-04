source: https://docs.evokoa.com/polygres/reference/routes
title: Runtime routes | Polygres
source_hash: 68bf7ba6200be651df2287cbb5847f0afc90a1f0adfad1e86eb84002a1bcc619
discovered_from: https://docs.evokoa.com/polygres

# Runtime routes | Polygres

Runtime routes

This page covers application-facing Runtime routes, not every dashboard or control-plane route.

Gateway retrieval paths are relative to the gateway API base URL, such as

https://api.polygres.com/v1 . Runtime retrieval paths are relative to the

project Runtime API URL copied from Connect > API & SDK , such as

https://p0123456789abcdef0123456.api.db.polygres.com/v1 .

Authentication labels

Label Credential

Public No bearer credential.

Dashboard Authorization: Bearer <dashboard_session_jwt> .

Retrieval Authorization: Bearer poly_live_<32hex> sent to the project Runtime API URL. Dashboard query surfaces may use a dashboard session through gateway-managed calls.

Row write A project_full Runtime API key, or a delegated Runtime token with the exact rows:write scope, sent to the project Runtime API URL.

An API key used on a dashboard-only route returns AUTH_MODE_NOT_ALLOWED .

Row writes

Method Route Auth Purpose

POST /tables/{schema_name}/{table_name}/rows/validate Row write Check one insert, upsert, or ignore request without changing data.

POST /tables/{schema_name}/{table_name}/rows Row write Insert, upsert, or ignore one row, with optional pgContext reconciliation.

These routes are available directly on the project Runtime API. They are not

available through the Gateway Runtime token used for dashboard retrieval. See

the Runtime Row Writes reference for payloads,

responses, idempotency, and recovery guidance.

Graph

Method Route Auth Purpose

POST /graph/expand Retrieval Expand from one entity.

POST /graph/neighborhood Retrieval Return a neighborhood around one entity.

POST /graph/related Retrieval Return related entities.

POST /graph/path Retrieval Find paths between source and target entities.

POST /graph/connection Retrieval Find connections among two to ten entities.

See the Graph Retrieval API reference for request and response shapes, traversal controls, filter scoping, pagination, and REST and Python examples.

Vector (deprecated)

The /vector family is a deprecated compatibility surface for existing

integrations. New vector retrieval uses a pgContext collection through

POST /context/search , POST /context/recommend , or

POST /context/query/execute .

These compatibility routes require a persisted vector configuration registered

before new pgvector registration was retired. It must be effectively Ready. An

HNSW configuration requires its exact physical index to be Ready; an existing

index_kind: none configuration can be Ready for exact-scan retrieval without

HNSW. Register physical pgvector indexes to make them available as explicit

Legacy configurations. For new vector setup and retrieval, use a pgContext

collection and the /context routes.

Method Route Auth Purpose

POST /vector/search Retrieval Search with a supplied embedding.

POST /vector/similar-to Retrieval Search from an existing row ID.

Text

Text configuration and retrieval use the same route suffixes through the

Gateway and project Runtime surfaces. Gateway configuration paths begin with

/projects/{project_id}/text ; Runtime paths begin with /text .

Method Route Auth Purpose

GET , POST /text/configurations Dashboard or Retrieval List or create saved text configurations.

GET , PATCH , DELETE /text/configurations/{config_id} Dashboard or Retrieval Read, update, or delete one configuration.

GET /text/configurations/{config_id}/diagnostics Dashboard or Retrieval Inspect physical index health.

POST /text/configurations/{config_id}/reindex Dashboard or Retrieval Rebuild and verify the text index.

POST /text/tsvector Retrieval Search with a saved tsvector configuration.

POST /text/fuzzy Retrieval Search with a saved fuzzy configuration.

See the Text Search API reference for both base

URLs, setup payloads, backwards compatibility, and query examples.

Hybrid (deprecated)

The /hybrid family is a deprecated compatibility surface for existing

pgvector integrations. New composed retrieval uses

/context/hybrid/graph-first , /context/hybrid/vector-first ,

/context/hybrid/rank-fusion , or /context/hybrid/joint .

Method Route Auth Purpose

POST /hybrid/graph-first Retrieval Produce graph candidates, then score them with vector search.

POST /hybrid/vector-first Retrieval Produce vector candidates, then evaluate graph context.

POST /hybrid/joint Retrieval Combine graph and vector rankings with Reciprocal Rank Fusion.

These legacy hybrid routes use the retained pgvector plan by default. With an

active pgContext compatibility binding, vector retrieval delegates through

pgContext while preserving the legacy request and response contract. The

collection-based pgContext surface also exposes distinct /context/hybrid/*

routes. Context rank-fusion combines independent pgContext and pgGraph

rankings, while Context joint couples candidate generation, graph expansion,

combined-pool pgContext rescoring, and one final weighted reciprocal-rank

fusion.

pgContext AI Search

The pgContext Preview API exposes 75 project-scoped routes. Use the Gateway

base /projects/{project_id}/context with a dashboard or CLI bearer credential,

or the project Runtime base /context with a project_full Runtime API key.

Area Routes

Capabilities and sources GET /capabilities ; POST /discover ; POST /preflight

Collections list, create, get, status, verify, diagnostics, update, delete, reindex, aliases, exact-name settings, and named vectors

Filters and points registered column and JSONB filters; point status, scroll, upsert, delete, reconcile, bounded batches, and payload updates

Operations list, get, cancel, and retry durable operations

Aggregates POST /count ; POST /facets

Retrieval dense, candidate, explicit-array, recommendation, discovery, exploration, grouped, recall, query plans, text hybrid, graph first, vector first, rank fusion, and coupled Joint

Insight index health, memory estimates, vacuum guidance, query statistics, collection telemetry, model versions, and embedding migrations

See the pgContext API reference for every method, path, permission, core request convention, and lifecycle examples.

Readiness

Method Route Auth Purpose

GET /retrieval/readiness Retrieval Return graph, aggregate Legacy-vector, and hybrid readiness. Text and pgContext collection readiness are not included.

Aggregate Legacy-vector readiness is true when at least one persisted

configuration is effectively Ready. When several are Ready and none is the

default, the response sets selection_required ; the query must name an exact

configuration.

Response conventions

Successful and error responses include a top-level request_id . Errors also use

an error object with code , optional variant , catalog-owned message , and

safe details . The variant identifies the specific condition when one code has

more than one message or status. Branch on code and variant , not message

text. See Handle API errors for integration

patterns and the complete error catalog for exact

identities.

For a gateway-proxied request, X-Request-ID identifies the gateway request. The JSON body’s request_id and the optional X-Polygres-Upstream-Request-ID header identify the corresponding Runtime request. Preserve both IDs when contacting support.

Cursor-paginated retrieval responses return next_cursor and has_more . Treat cursors as opaque and send next_cursor back as cursor .
