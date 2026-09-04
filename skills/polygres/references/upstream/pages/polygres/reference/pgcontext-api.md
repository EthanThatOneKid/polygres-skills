source: https://docs.evokoa.com/polygres/reference/pgcontext-api
title: pgContext API | Polygres
source_hash: dfbc4928378859dd4e495b41c425c063e01ee1bba491bd3e25c5129f14d8f559
discovered_from: https://docs.evokoa.com/polygres

# pgContext API | Polygres

pgContext API

The pgContext API powers the AI Search collection workflow. It is a Preview

surface with the contract version context.v1 , distinct from the

pgvector-backed /vector routes. Ordinary collection creation with source mode

existing can convert a compatible public.vector(n) column in place to

pgcontext.vector(n) . The onboarding endpoints persist guided candidate

discovery and the user’s decision, while ordinary collection creation remains

the activation path.

Use this Context API for new vector and hybrid application development. The

/vector and /hybrid route families remain available as deprecated

compatibility surfaces for existing pgvector integrations.

Use GET /capabilities before setup or retrieval. Its feature flags, blocker messages, and effective limits are authoritative for the selected project. Point scrolling has its own point_scroll , point_scroll_blocker , and point_scroll_blocker_message fields. These show whether point listings are available and explain what must be corrected when they are not.

Base URLs and authentication

The same 75 route suffixes are available through two project-bound surfaces:

Surface Base URL Credential

Gateway https://api.polygres.com/v1/projects/{project_id}/context Dashboard or CLI bearer credential with project access

Runtime {project_runtime_url}/context Project Runtime API key with project_full scope

The project Runtime URL already ends in /v1 . Copy it from Connect > API

access and send the Project Runtime API key as the bearer credential. The URL

and key bind each request to its project and database role.

Gateway callers need context:read for inspection and retrieval, and context:manage for onboarding, collection, filter, point-administration, cancellation, and retry operations. Owners, admins, and developers have both permissions. Viewers have read permission only.

Request conventions

Every response contains request_id . Preserve it when reporting a failure. Errors use the standard envelope:

{

"request_id" : "req_example" ,

"error" : {

"code" : "CONTEXT_DELETE_CONFIRMATION_INVALID" ,

"variant" : "context_collection_delete_confirmation_invalid" ,

"message" : "Context collection delete confirmation is invalid." ,

"details" : {}

}

}

variant is omitted when the base error code supplies the message. A variant

selects the exact catalog message and can also select a different status for

the same code. Branch on code and, when present, variant . Do not parse the

message text. The complete error catalog lists every

public pgContext base error and variant.

Request bodies are strict. Unknown fields return 400 CONTEXT_REQUEST_INVALID . Response bodies can gain additive fields.

Durable resource mutations require an Idempotency-Key header containing 1 to

128 printable ASCII characters. Replaying the same canonical request with the

same key returns the original response. Reusing a key for a different request

returns 409 CONTEXT_IDEMPOTENCY_CONFLICT . The idempotent onboarding state

endpoints accept requests without this header.

Read-only POST routes, including discovery, preflight, verification, search, and

recall check, accept requests without an idempotency key.

pgContext 0.2.0 API additions

The SDK 0.4.0 release expands the public Context API with 35 project-scoped

routes. Together with the established collection and retrieval routes, these

additions cover the stable pgContext 0.2.0 application workflows through typed

HTTP requests.

Workflow Added API coverage

Collection identity and configuration Aliases, exact-name collection information, collection limits, vector listings, and vector configuration

Point synchronization Bounded bulk upsert, bulk delete, backfill, and registered payload updates

Retrieval Candidate search, explicit-array search, recommendation, discovery, exploration, query-plan execution, and query explanation

Operations insight Index status, diagnostics, memory estimates, vacuum advice, index recommendations, optimization status, telemetry, and query statistics

Embedding lifecycle Model-version registration and embedding-migration tracking

The Gateway and Runtime expose matching paths and response envelopes. The

Python SDK guide maps these routes

to task-oriented methods and typed results.

Success statuses

Most reads and retrieval requests return 200 . Mutation success varies:

Success Operations

202 Collection create, update, delete, reindex, and vector addition; filter registration; point reconciliation; operation retry

200 or 202 Point upsert and delete. Up to 1,000 keys can complete synchronously; larger valid requests return an operation.

200 Operation cancellation, including an accepted cooperative cancellation request

200 Alias and exact-name configuration; bounded point batches; payload updates; model-version and embedding-migration records

A 202 response contains an operation envelope. Poll the returned operation

until its status is terminal. A successful cancellation request returns its own

operation acknowledgment.

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

GET /onboarding reads the saved decision and candidate snapshot. POST /onboarding/refresh reruns eligibility after the first evaluation. POST /onboarding/dismiss records a declined offer. A successful collection create

records completed atomically, and retrieval reads collection state directly.

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

Execute a typed query plan by placing one validated plan tree under plan :

curl -X POST " $CONTEXT_URL /query/execute" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{

"collection":"support_docs",

"plan":{

"kind":"nearest",

"vector_name":"title_semantic",

"vector":[0.1,0.2,0.3],

"limit":10

}

}'

Query plans support dense and sparse nearest search, full-text search,

late-interaction search, recommendation, discovery, point lookup, branch

prefetch, weighting, score thresholds, formulas, and reranking. Nested plans

let one request express a complete retrieval strategy. The Python SDK supplies

typed builders for each plan kind.

Other retrieval bodies use these strict field sets:

Route Accepted request fields

/grouped-search collection , optional vector_name , embedding , group_by , optional group_limit , optional limit

/recall-check collection , optional vector_name , embedding , optional filter , optional limit , optional minimum_recall

/hybrid/text collection , optional vector_name , embedding , query , optional limit ; the collection must have a text column

/hybrid/graph-first collection , optional vector_name , embedding , start , optional filter , optional limit , and graph traversal fields

/hybrid/vector-first collection , optional vector_name , embedding , optional filter , optional limit , optional context_limit , and graph traversal fields

/hybrid/rank-fusion collection , optional vector_name , embedding , start , optional filter , optional limit , weights , candidate limits, and graph traversal fields

/hybrid/joint collection , optional vector_name , embedding , optional query , optional starts , optional filter , weights , candidate limits, and graph traversal fields

Graph start contains schema , table , and id . Traversal fields are

relationship_types , direction , max_depth , and graph_limit . Read the

effective caps from /capabilities before constructing large requests.

Rank-fusion weights contains context and graph numeric fields. In

context.v1 , filters apply to dense, recall, graph-composed, rank-fusion, and

Joint retrieval. Grouped search uses its registered group_by key, while text

hybrid uses the collection’s text configuration. Joint weights contains

semantic , lexical , and graph numeric fields. The server normalizes active

Joint weights. A positive lexical weight requires both query and a configured

collection text column. starts accepts up to 32 complete graph entities.

Joint can also use its top pgContext results as graph seeds.

Route inventory

Paths below are relative to either Context base URL.

Capabilities and sources

Method Path Permission Purpose

GET /capabilities read Return effective features, blockers, versions, and limits.

POST /discover read Discover eligible source tables and pgContext or convertible pgvector columns.

POST /preflight read Validate the source, columns, dimensions, and permissions without making changes.

Guided Legacy-source onboarding

These stateful onboarding routes describe optional candidate discovery and the

user’s decision. A client that accepts a candidate submits an ordinary

source.mode: "existing" collection-create request, which activates the

collection. Application code calls onboarding explicitly.

Method Path Permission Purpose

GET /onboarding manage Read the saved onboarding decision and candidate snapshot.

POST /onboarding/evaluate manage Evaluate the one-time bridge offer.

POST /onboarding/refresh manage Explicitly rerun eligibility discovery.

POST /onboarding/acknowledge manage Accept the saved eligible candidate.

POST /onboarding/dismiss manage Record that the offer was declined.

Collection aliases and exact-name configuration

Aliases provide a stable application-facing name while a deployment retargets

traffic to another collection. Exact-name routes expose pgContext configuration

for automation that already knows the collection name.

Method Path Permission Purpose

POST /aliases manage Create an alias or retarget it to a collection name.

GET /aliases read List visible aliases and their target collections.

DELETE /aliases/{alias_name} manage Drop an alias.

GET /collections/by-name/{collection_name}/info read Read pgContext collection metadata by exact name.

GET /collections/by-name/{collection_name}/limits read Read strict-mode collection limits.

PATCH /collections/by-name/{collection_name}/limits manage Configure strict-mode collection limits.

GET /collections/by-name/{collection_name}/vectors read List registered dense vectors.

PATCH /collections/by-name/{collection_name}/vectors/{vector_name} manage Configure HNSW, quantization, and lifecycle metadata for a vector.

Collections

Method Path Permission Purpose

GET /collections read List collections with status and cursor filters.

POST /collections manage Create a collection and return a durable operation.

GET /collections/{collection_id} read Return collection configuration and its deletion plan.

GET /collections/{collection_id}/status read Return the saved serving and index state.

POST /collections/{collection_id}/verify read Actively verify collection correctness without repair.

GET /collections/{collection_id}/diagnostics read Return sanitized checks and recommended actions.

PATCH /collections/{collection_id} manage Update logical configuration or set the default collection.

DELETE /collections/{collection_id} manage Delete the collection and its managed resources after UUID confirmation. A new_table source is preserved while another collection references it.

POST /collections/{collection_id}/reindex manage Rebuild the current default vector’s Polygres-owned HNSW index.

POST /collections/{collection_id}/vectors manage Add a named vector. index_kind: hnsw creates a managed index; none uses exact scan without HNSW.

Collection creation accepts three source modes:

existing registers an existing table and native pgcontext.vector(n) NOT NULL column, or converts a compatible public.vector(n) column in place before registration.

add_column adds a vector column to an empty existing table. The application populates embeddings.

new_table creates a managed source table. Deleting the collection also deletes that table and its rows when no other collection references it. A shared source table is preserved and becomes user-managed. Collections created with existing or add_column preserve their source tables.

Collection creation always defines one initial vector, which becomes the

collection default. Later vector-add operations attach more named vectors to

the same source table. Collection responses expose vectors and

default_vector_name . Updating default_vector_name changes the fallback used

by ranked retrieval. The project’s default collection remains independently

configurable.

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

POST /points/bulk-upsert manage Upsert point mappings in bounded batches.

POST /points/bulk-delete manage Delete point mappings in bounded batches.

POST /points/backfill manage Backfill source rows into point mappings in bounded batches.

PUT /points/payload manage Set registered payload fields for selected source keys.

POST /points/payload/delete manage Delete selected registered payload fields.

POST /points/payload/clear manage Clear registered payload fields for selected source keys.

Point scrolling returns point_id and the canonical source_key . Source-table

row-level security filters every result. A page can be empty while has_more

is true when the policy filters rows; continue with next_cursor through the

final page. Source verification and enforceable access rules are prerequisites,

with a 409 response guiding callers to restore them.

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

Index health, telemetry, and embedding lifecycle

These routes scope operational insight to one named collection. Index routes

also select one exact index name, giving dashboards and automation a precise

resource identity.

Method Path Permission Purpose

GET /collections/by-name/{collection_name}/indexes/{index_name}/status read Read index lifecycle status.

GET /collections/by-name/{collection_name}/indexes/{index_name}/diagnostics read Read index diagnostics and actionable checks.

GET /collections/by-name/{collection_name}/indexes/{index_name}/memory-estimate read Estimate index memory requirements.

GET /collections/by-name/{collection_name}/indexes/{index_name}/vacuum-advice read Read vacuum guidance for the index.

GET /collections/by-name/{collection_name}/index-advisor read Read filter-index recommendations.

GET /collections/by-name/{collection_name}/optimization-status read Read collection optimization readiness.

GET /collections/by-name/{collection_name}/telemetry read Read collection-scoped telemetry rollups.

GET /collections/by-name/{collection_name}/query-cohort-stats read Read query cohort statistics.

GET /collections/by-name/{collection_name}/query-execution-stats read Read query execution statistics.

GET /collections/by-name/{collection_name}/model-versions read List registered embedding model versions.

POST /collections/by-name/{collection_name}/model-versions manage Register an embedding model version.

GET /collections/by-name/{collection_name}/embedding-migrations read List embedding migrations.

POST /collections/by-name/{collection_name}/embedding-migrations manage Create an embedding migration record.

PATCH /collections/by-name/{collection_name}/embedding-migrations/{migration_id} manage Update migration progress and status.

Aggregates and retrieval

Method Path Permission Purpose

POST /count read Count active, source-visible points with an optional filter.

POST /facets read Count values for a registered filter key.

POST /search read Run dense pgContext retrieval.

POST /search/raw read Score an explicit array of point IDs and dense vectors.

POST /search/candidates read Search within explicit candidate point IDs.

POST /recommend read Recommend points from positive and negative examples.

POST /search/discover read Discover points from contextual point IDs.

POST /explore read Explore points from contextual point IDs.

POST /grouped-search read Group dense results by a registered filter key.

POST /recall-check read Compare HNSW and exact top-K result sets.

POST /query/execute read Execute a validated typed query plan.

POST /query/explain read Explain the stable dense plus full-text collection query.

POST /hybrid/text read Combine dense and full-text rankings.

POST /hybrid/graph-first read Expand a graph neighborhood, then rank Context points.

POST /hybrid/vector-first read Retrieve Context points, then enrich with graph evidence.

POST /hybrid/rank-fusion read Fuse independent Context and graph rankings with weights.

POST /hybrid/joint read Run coupled pgContext retrieval, graph expansion, combined-pool rescoring, and one final fusion.

The collection request field accepts a collection UUID or exact unique name.

Every ranked request can include an exact vector_name ; omitting it selects

the collection’s default_vector_name . Every embedding must contain finite

JSON numbers and match the selected vector’s configured dimensions. Ranked

responses preserve server order and scores in one bounded result set.

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

Resolve application entities before the Joint request and send them through

starts . Apply application-specific temporal boosts, structured-fact

hydration, and answer synthesis in the application layer.

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
