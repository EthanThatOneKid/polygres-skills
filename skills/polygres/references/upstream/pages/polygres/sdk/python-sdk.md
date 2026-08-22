source: https://docs.evokoa.com/polygres/sdk/python-sdk
title: Python SDK | Polygres
source_hash: e378089a54c9db6fdf2543bc40b6c49ab03c217e09710eaee07bb0bbcc2dc542
discovered_from: https://docs.evokoa.com/polygres

# Python SDK | Polygres

Python SDK

The Polygres Python SDK is the official synchronous client for managing and querying retrieval through your project’s Runtime API. It connects securely using your Project API Key and Runtime API URL without exposing native database passwords.

Installation

Install the package via pip:

pip install "polygres-sdk==0.4.0"

To upgrade an existing environment:

pip install --upgrade "polygres-sdk==0.4.0"

Quick Start

Create a Project API Key from Project Settings > Project API Key , and

find the Runtime API URL under Connect > API & SDK .

Store these in your environment variables, then initialize the client:

import os

from polygres import Polygres

client = Polygres(

api_key = os.environ[ "POLYGRES_API_KEY" ],

runtime_url = os.environ[ "POLYGRES_RUNTIME_URL" ],

)

# Bind the client to your active project

project = client.project()

# Check legacy graph, vector, and hybrid readiness

readiness = project.readiness()

print (readiness.graph, readiness.vector, readiness.hybrid)

# Check AI Context capabilities separately

context_capabilities = project.context.get_capabilities()

print (context_capabilities.setup, context_capabilities.dense_search)

project.readiness() covers graph, previously registered pgvector, and legacy

hybrid retrieval. For AI Context readiness, check the capability for the

intended method, then inspect collection status and verification for the

selected named vector.

Running Queries

The SDK supports all retrieval modes. The integration patterns guide provides copyable examples for the most common application workflows:

pgContext semantic retrieval ( project.context.search , project.context.recommend )

Text Retrieval ( project.text.tsvector , project.text.fuzzy )

Graph Retrieval ( project.graph.expand , project.graph.related )

pgContext hybrid retrieval ( project.context.graph_first , project.context.vector_first , project.context.rank_fusion , project.context.joint )

pgContext query plans ( project.context.query_* , project.context.execute_query )

Head over to Retrieval Integration Patterns to copy the Python code for your specific workflow.

Vector and Hybrid migration guidance

project.vector and project.hybrid are deprecated compatibility namespaces.

They remain available for applications with existing pgvector registrations.

For new development, create a pgContext collection and use project.context :

Deprecated compatibility method Recommended pgContext method

project.vector.search() project.context.search() or query_nearest() with execute_query()

project.vector.similar_to() project.context.recommend() with a known positive point

project.hybrid.graph_first() project.context.graph_first()

project.hybrid.vector_first() project.context.vector_first()

project.hybrid.joint() project.context.joint()

The pgContext path adds named vectors, registered filters, point and payload

synchronization, text composition, query plans, diagnostics, telemetry, and

embedding migration tracking in one collection-centered API.

To validate, insert, upsert, or ignore one record through the Runtime API, see

Write rows with Python . The guide also covers optional

pgContext reconciliation, waiting, idempotency, and recovery after an uncertain

write.

Deprecated Vector result metrics

Existing project.vector integrations return VectorResult values.

VectorResult.distance , VectorResult.score , and VectorResult.similarity can

be None when a metric is undefined, such as cosine distance for a zero

vector. Use present values for display and additional ranking.

for result in project.vector.search(query_embedding).results:

if result.score is None :

continue

print (result.id, result.distance, result.similarity, result.score)

The SDK maps catalog errors to its stable exception hierarchy and renders the

exception message from the catalog instead of trusting server-supplied prose.

PolygresAPIError exposes code , status_code , request_id , and safe

details . Branch on code rather than matching the exception string. The SDK

raises PolygresMaintenanceError when scheduled maintenance blocks a request.

Pause the affected operation and retry after service returns to normal. See the

API error-handling guide for integration

patterns and the complete error catalog for exact

messages and retry classes.

SDK update notices

As SDK requests complete, the client processes applicable notices returned by

the Runtime API and periodically checks Polygres for release notices. It emits

PolygresVersionWarning when a newer version is recommended. A

notice is a Python warning, not a request failure. If the notice check cannot

reach Polygres or receives an invalid response, your application request still

succeeds or fails according to its own response.

Each notice is emitted at most once per Python process, including notices

returned with a Runtime API response. Follow the HTTPS link in the warning or

review the changelog before upgrading. To install the

recommended release:

pip install --upgrade polygres-sdk

You can handle or filter PolygresVersionWarning with Python’s standard

warnings module if your

application has a centralized warning policy.

pgContext collections and operations

All pgContext methods live directly under project.context . Collection and

operation objects are typed data; explicit namespace methods perform network

actions.

SDK 0.4.0 pgContext alignment

SDK 0.4.0 adds 54 public methods aligned with the stable pgContext 0.2.0

vocabulary. Every method lives on project.context , giving applications one

typed namespace for collection management, point synchronization, retrieval,

query plans, diagnostics, telemetry, and embedding migrations.

Goal SDK 0.4.0 methods

Use pgContext names for established workflows register_vector() , register_filter_column() , register_jsonb_path() , drop_collection() , facet() , query() , scroll()

Manage aliases and collection settings create_collection_alias() , collection_aliases() , drop_collection_alias() , collection_info() , collection_limits() , configure_collection_limits() , collection_vectors() , configure_vector()

Synchronize points and payloads bulk_upsert_points() , bulk_delete_points() , backfill_points() , set_payload() , delete_payload() , clear_payload()

Retrieve and compose results candidate_search() , raw_vector_search() , recommend() , discover() , explore() , execute_query() , explain()

Build typed query plans query_nearest() , query_sparse_nearest() , query_full_text() , query_late_interaction() , query_recommend() , query_discover() , query_lookup() , query_prefetch() , query_weight() , query_score_threshold() , query_formula() , query_rerank()

Inspect index and query health index_status() , index_diagnostics() , estimate_index_memory() , vacuum_advice() , index_advisor() , optimization_status() , telemetry() , query_cohort_stats() , query_execution_stats()

Track models and migrations model_versions() , register_model_version() , embedding_migrations() , create_embedding_migration() , update_embedding_migration()

The seven preferred pgContext names share the same Runtime operations as their

SDK 0.3.0 counterparts. Applications can upgrade first and adopt the preferred

names on their own schedule:

Preferred in SDK 0.4.0 Available SDK 0.3.0 name

register_vector() add_vector()

register_filter_column() add_filter_column()

register_jsonb_path() add_jsonb_filter_path()

drop_collection() delete_collection()

facet() facets()

query() text_hybrid()

scroll() scroll_points()

For new application code, start with the preferred names. Existing calls keep

their signatures, request behavior, return types, retry rules, and exception

categories in SDK 0.4.0.

To build a custom onboarding UI, call get_onboarding() first. An unassessed

project can be evaluated once with evaluate_onboarding() . Use

acknowledge_onboarding() or dismiss_onboarding() for the user’s decision,

and reserve refresh_onboarding() for an explicit retry. Application code

controls each onboarding call.

operation = project.context.create_collection(

"support_docs" ,

source = {

"mode" : "existing" ,

"schema_name" : "public" ,

"table_name" : "documents" ,

"source_key_column" : "id" ,

},

vector = { "column_name" : "embedding" , "dimensions" : 768 , "metric" : "cosine" },

)

completed = project.context.wait_for_operation(operation)

collection_response = project.context.get_collection(completed.collection_id)

collection = collection_response.collection

add_operation = project.context.register_vector(

collection.id,

"title_embedding" ,

768 ,

name = "title_semantic" ,

mode = "existing" ,

metric = "cosine" ,

set_default = True ,

)

project.context.wait_for_operation(add_operation)

status = project.context.get_collection_status(collection.id)

verification = project.context.verify_collection(collection.id)

print (status.serving_status, verification.verified)

results = project.context.search(

collection.name,

embed_text( "How do I rotate a signing key?" ),

vector_name = "title_semantic" ,

limit = 10 ,

)

This example uses an existing documents.title_embedding column populated

with 768-dimensional values. Choose mode="add_column" when preparing an

empty table for application-managed embedding writes.

The vector supplied during creation is the collection default. A collection

can contain multiple named vectors over the same source table. Pass

vector_name to ranked retrieval to select one exactly; omit it to use the

collection’s default vector. set_default=True makes a newly added vector the

default after its durable operation succeeds.

The project default collection is independent of a collection’s default

vector. Change an existing collection’s default vector with

update_collection(collection.id, default_vector_name="title_semantic") .

Change the project default collection with

set_default_collection(collection.id) . Both methods return durable operations

that must be waited for explicitly when the caller needs the completed state.

Mutations return immediately, and wait_for_operation() gives callers explicit

control over polling. Collection, filter, and point administration methods use

collection UUIDs; operation methods use operation UUIDs. Counts, facets, and

ranked retrieval accept a collection UUID or exact name.

project.context.joint() provides coupled pgContext true hybrid retrieval,

while Context rank fusion and the pgvector Hybrid namespace remain distinct

retrieval choices.

Build and execute a typed query plan

Query-plan builders validate the plan locally and return typed

ContextQueryPlan values. Compose branches in Python, then send the completed

plan through one execute_query() call:

dense = project.context.query_nearest(

embed_text( "How do I rotate a signing key?" ),

vector_name = "title_semantic" ,

limit = 40 ,

)

lexical = project.context.query_full_text(

"rotate signing key" ,

"content" ,

limit = 40 ,

)

plan = project.context.query_prefetch([

project.context.query_weight(dense, 0.7 ),

project.context.query_weight(lexical, 0.3 ),

])

plan = project.context.query_rerank(plan, limit = 10 )

response = project.context.execute_query( "support_docs" , plan)

for result in response.results:

print (result.point_id, result.score)

Use explain("support_docs", "content") to inspect the collection’s stable

dense plus full-text query. Use query_cohort_stats() ,

query_execution_stats() , and telemetry() to follow collection-scoped query

behavior in production.

Choosing your access method

Task Use

Runtime retrieval and pgContext collection operations in backend application code Python SDK

Project setup, credential output, CSV imports, migrations, and interactive retrieval configuration Polygres CLI

Visual project management, SQL editor, query workbench Dashboard

Direct database connections for ORMs, migration tools, bulk inserts Native Postgres driver ( psycopg , SQLAlchemy, etc.)

Direct database connections

The Polygres Python SDK serves the project Runtime API, including pgContext

management and retrieval. Native Postgres drivers such as asyncpg and

psycopg serve database migrations, bulk background inserts, and raw SQL

execution.

If your backend application needs to establish a pooled database connection

(for example, via SQLAlchemy or psycopg), bypass the SDK and use native database

credentials. See the Database Client Examples

guide for Python setup instructions.
