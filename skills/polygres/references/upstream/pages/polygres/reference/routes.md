source: https://docs.evokoa.com/polygres/reference/routes
title: Routes | Polygres
source_hash: 71ab300c2f33cf93f4c856f0ed7073a18e1b0779cbeb456a1136f100125727b7
discovered_from: https://docs.evokoa.com/polygres

# Routes | Polygres

Routes

Dashboard and setup paths are relative to the gateway API base URL, such as

https://api.polygres.com/v1 . Retrieval paths are relative to the project Runtime API URL copied from Connect > API access , such as https://p0123456789abcdef0123456.api.db.polygres.com/v1 .

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

Readiness

Method Route Auth Purpose

GET /retrieval/readiness Retrieval Return graph, default-vector, and hybrid readiness. Text readiness is not included.

Response conventions

Successful and error responses include a top-level request_id . Errors also use an

error object with code , message , and details , and return the request ID in the

X-Request-ID header.

Cursor-paginated retrieval responses return next_cursor and has_more . Treat cursors

as opaque and send next_cursor back as cursor .
