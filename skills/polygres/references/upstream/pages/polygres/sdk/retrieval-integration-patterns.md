source: https://docs.evokoa.com/polygres/sdk/retrieval-integration-patterns
title: Retrieval integration patterns | Polygres
source_hash: 9a0905648deb5a022756d170d77e60b6fd213da5d404d49a143f649657c03c1d
discovered_from: https://docs.evokoa.com/polygres

# Retrieval integration patterns | Polygres

Retrieval integration patterns

Choose the retrieval mode that matches the signal your application already has.

Application need Recommended method

Search by meaning from an embedding context.search for new setup; vector.search for a previously registered configuration

Find records similar to a known row vector.similar_to for a previously registered configuration

Search document language and keywords text.tsvector

Tolerate misspellings in short fields text.fuzzy

Find directly related records graph.related

Traverse a multi-hop neighborhood graph.expand

Combine semantic similarity with graph context Hybrid retrieval

Search one collection with semantic, lexical, filter, graph, or Joint evidence context AI Search

Generate or refresh embeddings in bulk Direct PostgreSQL background job

All examples assume the project and named resources are ready. Test graph,

vector, text, and Hybrid shapes in Query from the

dashboard . For pgContext, verify the collection

with the CLI workflow , then exercise the intended method through

the CLI, API, or SDK.

Semantic search

For new semantic-search setup, create a pgContext collection and use

project.context.search() as shown in pgContext AI

Search . New pgvector configuration registration is

retired.

The following project.vector example applies only when the project already has

a previously registered vector configuration. Generate query embeddings with

the same model and dimensions as that saved configuration.

query_embedding = embed_text( "How do I request a refund?" )

page = project.vector.search(

query_embedding,

config = "documents_default" ,

filters = { "status" : "published" },

min_similarity = 0.75 ,

limit = 10 ,

)

matches = [

{

"id" : result.id,

"score" : result.score,

"title" : result.properties.get( "title" ),

}

for result in page.results

]

embed_text is supplied by your application; Polygres retrieval accepts an embedding rather than generating one from text.

Use exact-match filters for lifecycle or result-scoping constraints registered

in the vector configuration. Authorize the request in your backend before

retrieval; a Polygres filter is not an authorization boundary.

When the query is a known record rather than free text, avoid regenerating its embedding:

page = project.vector.similar_to(

"doc_123" ,

config = "documents_default" ,

filters = { "status" : "published" },

limit = 10 ,

)

This pattern works well for “more like this,” related products, duplicate detection, and content recommendations.

Full-text search

Use PostgreSQL full-text search when users type words, phrases, or web-search-style terms and lexical relevance matters.

page = project.text.tsvector(

'refund policy -expired' ,

config = "documents_body_tsv" ,

filters = { "status" : "published" },

limit = 20 ,

)

for result in page.results:

print (result.id, result.score, result.properties.get( "title" ))

Full-text search is often a better fit than vector search for exact terminology, identifiers embedded in prose, product names, policy terms, and queries where tokenization and stemming are useful.

The saved configuration controls the tsvector column and PostgreSQL language. The request supplies only the query, configuration, exact-match filters, limit, and optional cursor.

Fuzzy lookup

Use fuzzy text search for misspellings and short fields where trigram-style similarity is useful:

page = project.text.fuzzy(

"acme corpration" ,

config = "customer_name_fuzzy" ,

filters = { "status" : "active" },

limit = 10 ,

)

for result in page.results:

print (result.id, result.similarity, result.properties.get( "name" ))

Common uses include customer names, titles, tags, city names, product labels, and human-entered codes. The saved configuration controls the similarity threshold, so application code should rank by result.score and treat result.similarity as supporting detail.

A practical lookup flow can combine exact application matching first, then fuzzy retrieval only when the exact lookup returns no result.

Related-record lookup

Use graph retrieval when relationships, not semantic similarity, define relevance.

For immediate neighbors:

page = project.graph.related(

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

relationship_types = [ "opened_by_customer" ],

direction = "any" ,

filters = { "status" : "open" },

limit = 50 ,

)

For a wider neighborhood:

page = project.graph.expand(

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

max_depth = 3 ,

direction = "any" ,

limit = 100 ,

)

for result in page.results:

print (result.node.table, result.node.id, result.depth, result.readable_path)

Use graph.path when the product needs to explain how two records connect, and graph.connection when investigating connections across several entities.

Keep depth and result limits small in request-time paths. A depth of one or two is easier to reason about and less likely to produce an overly broad candidate set.

pgContext AI Search

Use pgContext when the application benefits from a named collection with

collection-specific capabilities, registered filters, point synchronization,

several retrieval modes, and one or more named vectors over the same source

rows. Every collection has a default vector. Use another vector when the same

records need a distinct embedding model or input representation without

duplicating the collection’s source, filters, or result-column configuration.

Check the capability for the exact method before serving traffic:

capabilities = project.context.get_capabilities()

if not capabilities.dense_search:

raise RuntimeError (capabilities.dense_search_blocker)

Capabilities describe whether the Runtime supports the method. They do not say

that a particular collection or named vector is ready. Before serving traffic,

also inspect project.context.get_collection_status(collection_id) and

project.context.verify_collection(collection_id) , including the selected

vector’s index status.

Dense retrieval accepts an embedding that matches the selected vector’s dimensions.

After independently authorizing the request from trusted backend identity,

derive a retrieval filter for the rows that request may see:

tenant_filter = {

"must" : [{ "key" : "tenant_id" , "match" : authorized_tenant_id}],

}

response = project.context.search(

"support_docs" ,

embed_text( "How do I rotate a signing key?" ),

vector_name = "title_semantic" ,

filter = tenant_filter,

limit = 10 ,

)

for result in response.results:

print (result.source.id, result.score, result.properties.get( "title" ))

vector_name is optional on ranked retrieval. Omit it to use the collection’s

default vector. When supplied, it must exactly match a vector registered in

that collection, and the query embedding must match that vector’s dimensions.

The same registered filter can scope counts and facets:

matching = project.context.count( "support_docs" , filter = tenant_filter)

categories = project.context.facets(

"support_docs" ,

"category" ,

filter = tenant_filter,

limit = 20 ,

)

Use text hybrid when the collection has a configured text column:

response = project.context.text_hybrid(

"support_docs" ,

embed_text( "reset password" ),

query = "reset password" ,

limit = 10 ,

)

Use Joint retrieval when semantic, lexical, and graph evidence should cooperate

in one bounded query:

response = project.context.joint(

"support_docs" ,

embed_text( "Which deployment guidance applies to this account?" ),

query = "deployment guidance" ,

starts = [{ "schema" : "public" , "table" : "accounts" , "id" : "acct_123" }],

relationship_types = [ "account_document" ],

semantic_weight = 0.5 ,

lexical_weight = 0.2 ,

graph_weight = 0.3 ,

limit = 12 ,

)

After committed source-row inserts or changes, upsert their stable source keys.

After bulk or uncertain changes, start a reconciliation operation. Persist a

caller-owned idempotency key when an operation may resume across processes.

These filters narrow retrieval but do not replace database or application

authorization.

Graph plus vector RAG

Hybrid retrieval is useful when a RAG system needs both semantic relevance and relational context.

Anchor-first RAG

When the application knows the current customer, account, case, or document, traverse its graph neighborhood before semantic scoring:

query_embedding = embed_text( "What prior incidents mention login failures?" )

page = project.hybrid.graph_first(

{ "schema" : "public" , "table" : "accounts" , "id" : "acct_123" },

query_embedding,

config = "knowledge_default" ,

max_depth = 2 ,

relationship_types = [ "belongs_to_account" , "references" ],

filters = { "status" : "published" },

limit = 12 ,

)

This keeps retrieved context close to the known business entity.

Semantic-first RAG

When there is no reliable anchor, find semantic candidates first and then add graph context:

page = project.hybrid.vector_first(

query_embedding,

config = "knowledge_default" ,

vector_limit = 50 ,

max_depth = 1 ,

filters = { "status" : "published" },

limit = 12 ,

)

This pattern is useful for global knowledge search where related records improve context after the initial semantic match.

Joint ranking

Use joint retrieval when both a semantic query and an anchor should independently contribute to rank:

page = project.hybrid.joint(

query_embedding,

{ "schema" : "public" , "table" : "accounts" , "id" : "acct_123" },

config = "knowledge_default" ,

max_depth = 2 ,

limit = 12 ,

)

Joint ranking uses weighted reciprocal rank fusion. Tune vector_weight and

graph_weight to express the relative contribution of semantic and graph

rankings, then validate the result distribution with representative queries.

Build model context

Use stable record identifiers and selected properties to construct context. Keep provenance beside each chunk:

context = []

for result in page.results:

body = result.properties.get( "body" )

if not body:

continue

context.append(

{

"source" : f " { result.schema } . { result.table } : { result.id } " ,

"score" : result.score,

"body" : body,

"relationships" : result.relationships,

}

)

Apply an application token budget, deduplicate repeated rows, and keep source IDs so generated answers can link back to records.

Combine lexical and semantic search

For a pgContext collection with a configured text column, use

project.context.text_hybrid() as shown above. For existing pgvector and

TSVector configurations, an application can also run both searches and combine

IDs in its own ranking layer.

A simple approach is reciprocal rank fusion:

def reciprocal_rank_fusion ( * ranked_id_lists: list[ str ], k: int = 60 ) -> list[ str ]:

scores: dict[ str , float ] = {}

for ids in ranked_id_lists:

for rank, row_id in enumerate (ids, start = 1 ):

scores[row_id] = scores.get(row_id, 0.0 ) + 1.0 / (k + rank)

return sorted (scores, key = scores.get, reverse = True )

text_page = project.text.tsvector(

"refund policy" ,

config = "documents_body_tsv" ,

limit = 25 ,

)

vector_page = project.vector.search(

embed_text( "refund policy" ),

config = "documents_default" ,

limit = 25 ,

)

ranked_ids = reciprocal_rank_fusion(

[result.id for result in text_page.results],

[result.id for result in vector_page.results],

)

Use application-side fusion when its ranking policy belongs in your service.

Use pgContext text hybrid for collection-based lexical and semantic retrieval,

and use the Hybrid namespace for graph plus pgvector retrieval.

Background enrichment jobs

Embedding generation and data mutation happen through PostgreSQL, not through the retrieval SDK. Use DIRECT_URL for sustained or bulk enrichment work.

This minimal psycopg job targets a legacy public.vector(n) column, selects

rows without embeddings, calls an application embedding function, and writes

vectors with parameterized SQL:

import os

from collections.abc import Iterable

import psycopg

def vector_literal (values: Iterable[ float ]) -> str :

return "[" + "," .join( str ( float (value)) for value in values) + "]"

def enrich_batch () -> int :

with psycopg.connect(os.environ[ "DIRECT_URL" ]) as connection:

rows = connection.execute(

"""

select id, body

from documents

where embedding is null

order by id

limit 100

"""

).fetchall()

if not rows:

return 0

embeddings = embed_many([body for _, body in rows])

with connection.cursor() as cursor:

cursor.executemany(

"""

update documents

set embedding = %s ::vector

where id = %s and embedding is null

""" ,

[

(vector_literal(embedding), row_id)

for (row_id, _), embedding in zip (rows, embeddings, strict = True )

],

)

return len (rows)

embed_many is your embedding provider integration. The vector length must match the configured column dimensions.

For a native AI Context source column, use the actual

pgcontext.vector(n) type instead of the example’s ::vector cast. After the

transaction commits, call project.context.upsert_points() for the changed

source keys, or reconcile_points() after bulk or uncertain changes, so point

mappings reflect the source table. Direct SQL writes do not trigger either SDK

method automatically.

For production jobs:

process bounded batches,

make updates idempotent,

checkpoint progress by stable row ID or job state,

bound provider and database concurrency,

retry individual batches rather than restarting an entire corpus,

store the embedding model/version alongside data when model changes matter,

run a readiness or test query after large configuration or index changes.

Use the pooled DATABASE_URL for lightweight request-time writes and the direct DIRECT_URL for bulk or session-sensitive work.

Operational checklist

Before shipping a retrieval path:

keep API keys and database credentials server-side,

verify the named configuration and dimensions in each environment,

enforce application authorization before returning results,

cap page size, total results, graph depth, and total retry time,

preserve request_id in logs,

treat filters as defense in depth rather than the only authorization layer,

record source IDs and scores for debugging and RAG provenance.
