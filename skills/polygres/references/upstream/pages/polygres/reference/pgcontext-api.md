source: https://docs.evokoa.com/polygres/reference/pgcontext-api
title: pgContext API | Polygres
source_hash: ed8e09a027a3bc49871e32a373a18021bbb10a8de526b4ec9b95a58c0b82416a
discovered_from: https://docs.evokoa.com/polygres

# pgContext API | Polygres

pgContext API

The pgContext API powers the AI Search collection workflow. It is a Preview surface with the contract version context.v1 . It remains separate from the pgvector-backed /vector routes. Ordinary collection creation with source mode existing can convert a compatible public.vector(n) column in place to pgcontext.vector(n) . The onboarding endpoints persist guided candidate discovery and the user’s decision; they do not activate a separate public bridge or replace ordinary collection creation.

Use GET /capabilities before setup or retrieval. Its feature flags, blocker messages, and effective limits are authoritative for the selected project. Point scrolling has its own point_scroll , point_scroll_blocker , and point_scroll_blocker_message fields. These show whether point listings are available and explain what must be corrected when they are not.

Base URLs and authentication

The same 40 route suffixes are available through two project-bound surfaces:

Surface Base URL Credential

Gateway https://api.polygres.com/v1/projects/{project_id}/context Dashboard or CLI bearer credential with project access

Runtime {project_runtime_url}/context Project Runtime API key with project_full scope

The project Runtime URL already ends in /v1 . Copy it from Connect > API access . Do not add a project routing header or database role to Runtime requests.

Gateway callers need context:read for inspection and retrieval, and context:manage for onboarding, collection, filter, point-administration, cancellation, and retry operations. Owners, admins, and developers have both permissions. Viewers have read permission only.

Request conventions

Every response contains request_id . Preserve it when reporting a failure. Errors use the standard envelope:

{

"request_id" : "req_example" ,

"error" : {

"code" : "CONTEXT_COLLECTION_NOT_READY" ,

"message" : "Context collection is not ready." ,

"details" : {}

}

}

Request bodies are strict. Unknown fields return 400 CONTEXT_REQUEST_INVALID . Response bodies can gain additive fields.

Durable resource mutations require an Idempotency-Key header containing 1 to 128 printable ASCII characters. Replaying the same canonical request with the same key returns the original response. Reusing a key for a different request returns 409 CONTEXT_IDEMPOTENCY_CONFLICT . The idempotent onboarding state endpoints do not require this header.

Read-only POST routes, including discovery, preflight, verification, search, and recall check, do not require an idempotency key.

Success statuses

Most reads and retrieval requests return 200 . Mutation success varies:

Success Operations

202 Collection create, update, delete, reindex, and vector addition; filter registration; point reconciliation; operation retry

200 or 202 Point upsert and delete. Up to 1,000 keys can complete synchronously; larger valid requests return an operation.

200 Operation cancellation, including an accepted cooperative cancellation request

A 202 response contains an operation envelope. Poll the returned operation until its status is terminal. Do not treat a client timeout as cancellation.

Request examples

Set the Context base URL for either the Gateway or Runtime surface and provide the corresponding bearer credential:

CONTEXT_URL = "https://api.polygres.com/v1/projects/p0123456789abcdef0123456/context"

Read capabilities:

curl " $CONTEXT_URL /capabilities" \

-H "Authorization: Bearer <token-or-runtime-api-key>"

Evaluate the one-time same-column onboarding offer, then record the user’s explicit decision:

curl -X POST " $CONTEXT_URL /onboarding/evaluate" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{}'

curl -X POST " $CONTEXT_URL /onboarding/acknowledge" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{}'

GET /onboarding reads only the saved decision and candidate snapshot. POST /onboarding/refresh is the only route that reruns eligibility after the first evaluation. POST /onboarding/dismiss records a declined offer. A successful collection create records completed atomically; normal retrieval never reads onboarding state.

Discover visible sources:

curl -X POST " $CONTEXT_URL /discover" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{"schema_names":["public"]}'

Discovery reports dimensions as the vector column’s declared dimension for both native pgContext and pgvector columns. Compare that value directly with the embedding length supplied to preflight and retrieval.

Preflight and create accept the same strict collection request. Preflight is read-only; create requires an idempotency key:

{

"name" : "support_docs" ,

"source" : {

"mode" : "existing" ,

"schema_name" : "public" ,

"table_name" : "articles" ,

"source_key_column" : "id"

},

"vector" : {

"column_name" : "embedding" ,

"dimensions" : 3 ,

"metric" : "cosine"

},

"text_column" : "content" ,

"result_columns" : [ "title" , "url" ],

"filter_columns" : [ "tenant_id" ],

"index_kind" : "hnsw" ,

"max_search_limit" : 1000

}

curl -X POST " $CONTEXT_URL /collections" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-H "Idempotency-Key: create-support-docs-v1" \

--data-binary @collection.json

The initial vector becomes the collection’s default vector. Add another named

vector over the same source table by using an existing compatible column or by

adding a new column to an empty table:

curl -X POST " $CONTEXT_URL /collections/<collection-uuid>/vectors" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-H "Idempotency-Key: add-title-vector-v1" \

-d '{

"name":"title_semantic",

"column_name":"title_embedding",

"dimensions":768,

"mode":"existing",

"metric":"cosine",

"index_kind":"hnsw",

"set_default":true

}'

name is optional and defaults to column_name . mode is existing or

add_column . When set_default is true, the vector becomes the collection

default after the durable operation succeeds.

Collection update accepts text_column , result_columns ,

max_search_limit , and default_vector_name . Setting the default collection

uses the separate body {"is_default":true} . Collection and vector defaults

are independent. Deletion requires the path UUID again in its body:

curl -X DELETE " $CONTEXT_URL /collections/<collection-uuid>" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-H "Idempotency-Key: delete-support-docs-v1" \

-d '{"confirm_collection_id":"<collection-uuid>"}'

Register a filter column, then upsert source-key mappings:

curl -X POST " $CONTEXT_URL /collections/<collection-uuid>/filters/columns" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-H "Idempotency-Key: add-tenant-filter-v1" \

-d '{"key":"tenant_id","column":"tenant_id"}'

curl -X POST " $CONTEXT_URL /collections/<collection-uuid>/points/upsert" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-H "Idempotency-Key: upsert-support-docs-v1" \

-d '{"source_keys":["doc_1","doc_2"]}'

Dense search requires a collection UUID or exact unique name and an embedding that matches its configured dimensions:

curl -X POST " $CONTEXT_URL /search" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{

"collection":"support_docs",

"vector_name":"title_semantic",

"embedding":[0.1,0.2,0.3],

"filter":{"must":[{"key":"tenant_id","match":"acme"}]},

"limit":10

}'

Other retrieval bodies use these strict field sets:

Route Accepted request fields

/grouped-search collection , optional vector_name , embedding , group_by , optional group_limit , optional limit

/recall-check collection , optional vector_name , embedding , optional filter , optional limit , optional minimum_recall

/hybrid/text collection , optional vector_name , embedding , query , optional limit ; the collection must have a text column

/hybrid/graph-first collection , optional vector_name , embedding , start , optional filter , optional limit , and graph traversal fields

/hybrid/vector-first collection , optional vector_name , embedding , optional filter , optional limit , optional context_limit , and graph traversal fields

/hybrid/rank-fusion collection , optional vector_name , embedding , start , optional filter , optional limit , weights , candidate limits, and graph traversal fields

/hybrid/joint collection , optional vector_name , embedding , optional query , optional starts , optional filter , weights , candidate limits, and graph traversal fields

Graph start contains schema , table , and id . Traversal fields are relationship_types , direction , max_depth , and graph_limit . Read the effective caps from /capabilities before constructing large requests. Rank-fusion weights contains context and graph numeric fields. Grouped search and text hybrid do not accept filter in context.v1 . Joint weights contains semantic , lexical , and graph numeric fields. The server normalizes active Joint weights. A positive lexical weight requires both query and a configured collection text column. starts accepts up to 32 complete graph entities. Unlike graph first and rank fusion, Joint can run with no explicit start because its top pgContext results also become graph seeds.

Route inventory

Paths below are relative to either Context base URL.

Capabilities and sources

Method Path Permission Purpose

GET /capabilities read Return effective features, blockers, versions, and limits.

POST /discover read Discover eligible source tables and pgContext or convertible pgvector columns.

POST /preflight read Validate the source, columns, dimensions, and permissions without making changes.

Guided Legacy-source onboarding

These stateful onboarding routes describe optional candidate discovery and the

user’s decision. A client that accepts a candidate still submits an ordinary

source.mode: "existing" collection-create request. The routes do not activate

the Runtime’s internal same-column binding and are never called automatically

by retrieval.

Method Path Permission Purpose

GET /onboarding manage Read the saved onboarding decision and candidate snapshot.

POST /onboarding/evaluate manage Evaluate the one-time bridge offer.

POST /onboarding/refresh manage Explicitly rerun eligibility discovery.

POST /onboarding/acknowledge manage Accept the saved eligible candidate.

POST /onboarding/dismiss manage Record that the offer was declined.

Collections

Method Path Permission Purpose

GET /collections read List collections with status and cursor filters.

POST /collections manage Create a collection and return a durable operation.

GET /collections/{collection_id} read Return collection configuration and its deletion plan.

GET /collections/{collection_id}/status read Return the saved serving and index state.

POST /collections/{collection_id}/verify read Actively verify collection correctness without repair.

GET /collections/{collection_id}/diagnostics read Return sanitized checks and recommended actions.

PATCH /collections/{collection_id} manage Update logical configuration or set the default collection.

DELETE /collections/{collection_id} manage Delete the collection and its managed resources after UUID confirmation. A new_table source is deleted only when no other collection references it.

POST /collections/{collection_id}/reindex manage Rebuild the current default vector’s Polygres-owned HNSW index.

POST /collections/{collection_id}/vectors manage Add a named vector. index_kind: hnsw creates a managed index; none uses exact scan without HNSW.

Collection creation accepts three source modes:

existing registers an existing table and native pgcontext.vector(n) NOT NULL column, or converts a compatible public.vector(n) column in place before registration.

add_column adds a vector column to an empty existing table. Polygres does not generate embeddings.

new_table creates a managed source table. Deleting the collection also deletes that table and its rows when no other collection references it. A shared source table is preserved and becomes user-managed. Collections created with existing or add_column preserve their source tables.

Collection creation always defines one initial vector, which becomes the

collection default. Later vector-add operations attach more named vectors to

the same source table. Collection responses expose vectors and

default_vector_name . Updating default_vector_name changes the fallback used

by ranked retrieval and does not change the project’s default collection.

The initial vector’s optional name defaults to its column_name .

For an existing pgvector source, preflight validates the declared dimensions

and reads the source to determine whether any vector value is NULL . A column

may be declared nullable when every stored row is populated. Actual NULL

values return CONTEXT_VECTOR_NULLABLE ; mismatched dimensions return

CONTEXT_VECTOR_DIMENSION_INVALID .

Eligible conversion is performed inside the collection-create transaction. It

takes an ACCESS EXCLUSIVE lock, drops non-constraint indexes that depend on

the selected column, converts values through real[] , changes the column type

to pgcontext.vector(n) , and sets the column NOT NULL . A dependent index that

backs a database constraint returns CONTEXT_INDEX_CONFLICT and rolls back the

operation.

The source key is id in context.v1 . It must be unique and non-null. UUID, text, varchar, smallint, integer, and bigint keys are supported.

Filters and points

Method Path Permission Purpose

GET /collections/{collection_id}/filters read List registered public filter keys.

POST /collections/{collection_id}/filters/columns manage Register an ordinary source column as a filter.

POST /collections/{collection_id}/filters/jsonb-paths manage Register an ordered JSONB path as a filter.

GET /collections/{collection_id}/points/status read Return point reconciliation state.

GET /collections/{collection_id}/points manage Scroll active, source-visible point mappings.

POST /collections/{collection_id}/points/upsert manage Add or reactivate mappings for supplied source keys.

POST /collections/{collection_id}/points/delete manage Logically delete mappings for supplied source keys.

POST /collections/{collection_id}/points/reconcile manage Reconcile point mappings with source rows.

Point scrolling returns point_id and the canonical source_key ; it does not return vectors or source payloads. Results respect row-level security on the source table. If hidden rows are skipped, a page can be empty while has_more is still true. Continue with next_cursor until has_more is false. If Polygres cannot verify the source table or enforce its access rules, the request returns a 409 error instead of exposing unverified results.

Upsert and delete accept 1 through 10,000 keys. Requests of up to 1,000 keys can complete synchronously; larger valid requests return a durable operation. Reconciliation adds missing mappings and normally removes mappings for deleted rows. When the source table uses row-level security, orphan cleanup is skipped because a hidden row may still exist. The result includes orphan_cleanup_skipped_reason: "source_rls_enabled" ; explicitly delete keys for rows that you know were removed.

Only registered filter keys are accepted. A filter can use must , should , and must_not groups. Each condition contains a key plus exactly one scalar match, match set, range, is_null , or is_empty expression.

Durable operations

Method Path Permission Purpose

GET /operations read List or filter durable operations.

GET /operations/{operation_id} read Return current operation status and stage.

POST /operations/{operation_id}/cancel manage Request cooperative cancellation.

POST /operations/{operation_id}/retry manage Retry failed or cancelled work as a new operation.

Operation statuses are queued , running , cancel_requested , succeeded , failed , and cancelled .

Verification includes a point_scroll_access check for source-table permissions. If it fails, diagnostics recommends repair_permissions . Run preflight and verification again after changing source ownership, permissions, or row-level security policies.

Aggregates and retrieval

Method Path Permission Purpose

POST /count read Count active, source-visible points with an optional filter.

POST /facets read Count values for a registered filter key.

POST /search read Run dense pgContext retrieval.

POST /grouped-search read Group dense results by a registered filter key.

POST /recall-check read Compare HNSW and exact top-K result sets.

POST /hybrid/text read Combine dense and full-text rankings.

POST /hybrid/graph-first read Expand a graph neighborhood, then rank Context points.

POST /hybrid/vector-first read Retrieve Context points, then enrich with graph evidence.

POST /hybrid/rank-fusion read Fuse independent Context and graph rankings with weights.

POST /hybrid/joint read Run coupled pgContext retrieval, graph expansion, combined-pool rescoring, and one final fusion.

The collection request field accepts a collection UUID or exact unique name.

Every ranked request can include an exact vector_name ; omitting it selects

the collection’s default_vector_name . Every embedding must contain finite

JSON numbers and match the selected vector’s configured dimensions. Ranked

responses preserve server order and scores and never contain a pagination

cursor.

Rank fusion and Joint are different operations. /hybrid/rank-fusion combines independently produced Context and graph rankings. /hybrid/joint couples candidate generation: pgContext results create graph seeds, graph traversal can introduce candidates, every admitted candidate receives an exact pgContext rescore, and the final weighted reciprocal-rank fusion is applied once over the combined pool. Neither route is an alias for the other.

Joint true-hybrid retrieval

Joint accepts one pgContext collection and optional application-resolved graph anchors:

curl -X POST " $CONTEXT_URL /hybrid/joint" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{

"collection":"support_docs",

"embedding":[0.1,0.2,0.3],

"query":"Which deployment guidance is current?",

"starts":[

{"schema":"public","table":"accounts","id":"acct_123"}

],

"filter":null,

"relationship_types":["account_document","document_supersedes"],

"direction":"any",

"max_depth":2,

"context_limit":50,

"seed_limit":8,

"graph_limit":200,

"traversal_limit":500,

"weights":{"semantic":0.4,"lexical":0.2,"graph":0.4},

"limit":10

}'

Joint executes one bounded data-plane statement under one retrieval transaction:

Initial semantic retrieval runs through pgContext.

A configured text lane runs when query is present and lexical is positive.

Explicit starts and the highest-ranked pgContext results form the bounded graph seed set.

Typed graph.expand traversal can add candidates from the collection source table.

Semantic, text, and graph candidates are deduplicated into one candidate pool.

Every admitted candidate, including graph-only discoveries, receives an exact pgContext rescore.

One-based lane ranks are combined with normalized weighted RRF using k = 60 .

The final limit is applied once after fusion.

The response uses mode = "joint" , score_kind = "joint_weighted_rrf" , and returns lane evidence, a score breakdown, fusion metadata, and bounded trace counts. introduced_by_graph distinguishes candidate introduction from rank reordering. Graph-introduced results have null baseline_rank and rank_lift ; other results compare their final rank with the semantic-plus-lexical baseline.

Joint does not infer arbitrary entities from the query. Resolve application entities before the request and send them through starts . The endpoint also does not provide application-specific temporal boosts, structured-fact hydration, or answer synthesis.

Minimal lifecycle

Read /capabilities .

Discover sources and preflight the intended collection.

Create the collection with an idempotency key.

Poll the returned operation until it is terminal.

Add any additional named vectors and set the intended default vector.

Check collection status, each vector index, and verification.

Upsert or reconcile points after source-row changes.

Query the collection, supplying vector_name when it should not use the

default.

Use diagnostics when serving is degraded or blocked.

For an interactive workflow that generates idempotency keys and waits for operations, use the pgContext CLI guide .
