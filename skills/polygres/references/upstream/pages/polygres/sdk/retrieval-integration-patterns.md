source: https://docs.evokoa.com/polygres/sdk/retrieval-integration-patterns
title: Retrieval integration patterns | Polygres
source_hash: 2b6015ea416ccd198f9f906c2f6e7cb07d5e472f7a6bbbee147ca86cfb9275a6
discovered_from: https://docs.evokoa.com/polygres

# Retrieval integration patterns | Polygres

Retrieval integration patterns

Choose the retrieval mode that matches the signal your application already has.

Application need Recommended method

Search by meaning from an embedding vector.search

Find records similar to a known row vector.similar_to

Search document language and keywords text.tsvector

Tolerate misspellings in short fields text.fuzzy

Find directly related records graph.related

Traverse a multi-hop neighborhood graph.expand

Combine semantic similarity with graph context Hybrid retrieval

Generate or refresh embeddings in bulk Direct PostgreSQL background job

All examples assume the project and named configurations are already ready. Use them

after you have tested the same retrieval shape in

Query from the dashboard .

Semantic search

Use semantic search when the application can generate an embedding for the user’s query with the same model and dimensions as the saved vector configuration.

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

Use exact-match filters for authorization or lifecycle constraints that are registered in the vector configuration. Keep user-specific authorization in your backend even when a Polygres filter narrows the result set.

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

Current joint ranking uses reciprocal rank fusion. Do not tune vector_weight or graph_weight expecting them to change the current ranking; supplied weights are accepted but reported as ignored.

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

The API does not provide a single text-plus-vector endpoint. An application can run full-text and vector searches independently, then combine IDs in its own ranking layer.

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

Use this only when your application needs lexical and semantic fusion. Graph-plus-vector fusion is already available through the hybrid endpoints.

Background enrichment jobs

Embedding generation and data mutation happen through PostgreSQL, not through the retrieval SDK. Use DIRECT_URL for sustained or bulk enrichment work.

This minimal psycopg job selects rows without embeddings, calls an application embedding function, and writes vectors with parameterized SQL:

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
