source: https://docs.evokoa.com/polygres/sdk/python-sdk
title: Python SDK | Polygres
source_hash: a2faecca6d71e5a4883c51524a463a74974ce415086f34a938804b1c3966c11f
discovered_from: https://docs.evokoa.com/polygres

# Python SDK | Polygres

Python SDK

The Polygres Python SDK is the official synchronous client for managing and querying retrieval through your project’s Runtime API. It connects securely using your Project API Key and Runtime API URL without exposing native database passwords.

Installation

Install the package via pip:

pip install polygres-sdk

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

hybrid retrieval. It does not establish that an AI Context collection or a

specific named vector is ready. For AI Context, check the capability for the

intended method, then inspect collection status and verification.

Running Queries

The SDK supports all retrieval modes. The integration patterns guide provides copyable examples for the most common application workflows:

Vector Retrieval ( project.vector.search )

Text Retrieval ( project.text.tsvector , project.text.fuzzy )

Graph Retrieval ( project.graph.expand , project.graph.related )

Hybrid Retrieval ( project.hybrid.graph_first , project.hybrid.joint )

pgContext AI Search ( project.context.search , project.context.text_hybrid , project.context.joint )

Head over to Retrieval Integration Patterns to copy the Python code for your specific workflow.

Vector result metrics

VectorResult.distance and VectorResult.score can be None when a metric cannot be calculated, such as cosine distance for a zero vector. similarity can also be None . Check these values before displaying or using them for additional ranking; do not replace them with a made-up score.

for result in project.vector.search(query_embedding).results:

if result.score is None :

continue

print (result.id, result.distance, result.similarity, result.score)

The SDK raises PolygresMaintenanceError when scheduled maintenance blocks a request. Pause the affected operation and retry after service returns to normal.

pgContext collections and operations

All pgContext methods live directly under project.context . Collection and operation objects are typed data and do not perform network actions.

To build a custom onboarding UI, call get_onboarding() first. An unassessed project can be evaluated once with evaluate_onboarding() . Use acknowledge_onboarding() or dismiss_onboarding() for the user’s decision, and reserve refresh_onboarding() for an explicit retry. These calls are never made automatically by retrieval methods.

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

add_operation = project.context.add_vector(

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

This example assumes documents.title_embedding already exists and contains

768-dimensional values because mode="existing" does not create or populate

the column.

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

Mutations return immediately and never wait implicitly. Collection, filter, and

point administration methods use collection UUIDs; operation methods use

operation UUIDs. Counts, facets, and ranked retrieval accept a collection UUID

or exact name. project.context.joint() is coupled pgContext true hybrid and is

separate from Context rank fusion and the existing pgvector Hybrid namespace.

Choosing your access method

Task Use

Runtime retrieval and pgContext collection operations in backend application code Python SDK

Project setup, credential output, CSV imports, migrations, and interactive retrieval configuration Polygres CLI

Visual project management, SQL editor, query workbench Dashboard

Direct database connections for ORMs, migration tools, bulk inserts Native Postgres driver ( psycopg , SQLAlchemy, etc.)

Direct database connections

The Polygres Python SDK is for the project Runtime API, including pgContext management and retrieval. It does not bundle Postgres drivers like asyncpg or psycopg , and it is not meant for database migrations, bulk background inserts, or raw SQL execution.

If your backend application needs to establish a pooled database connection

(for example, via SQLAlchemy or psycopg), bypass the SDK and use native database

credentials. See the Database Client Examples

guide for Python setup instructions.
