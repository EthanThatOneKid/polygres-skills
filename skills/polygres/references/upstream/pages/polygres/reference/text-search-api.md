source: https://docs.evokoa.com/polygres/reference/text-search-api
title: Text Search API | Polygres
source_hash: 109129b409d34fc12f32890e7d2a207cf7f0bf2f1a02c5c62f943ef7edb1a203
discovered_from: https://docs.evokoa.com/polygres

# Text Search API | Polygres

Text Search API

Text search has two modes:

TSVector Search uses PostgreSQL full-text search for words, phrases, and language-aware ranking.

Fuzzy Search uses PostgreSQL trigram similarity for misspellings and close text matches.

Both modes use a saved configuration. Configuration setup creates and verifies

the required PostgreSQL index before it returns success.

Base URLs and authentication

The same route suffixes are available through two project-bound surfaces:

Surface Base URL Credential

Gateway https://api.polygres.com/v1/projects/{project_id}/text Dashboard or CLI bearer credential with project access

Runtime {project_runtime_url}/text Project Runtime API key

The project Runtime URL already ends in /v1 . Copy it from Connect > API &

SDK . Read and query calls require text:read ; configuration changes and

reindexing require text:manage .

Endpoints

Method Route suffix Purpose

GET /configurations List saved TSVector and Fuzzy configurations.

POST /configurations Create a configuration and its index. It can also generate a stored TSVector column.

GET /configurations/{config_id} Get one configuration by ID or name.

PATCH /configurations/{config_id} Update supported configuration fields and rebuild the index when its target changes.

DELETE /configurations/{config_id} Delete the configuration and its managed index.

GET /configurations/{config_id}/diagnostics Compare saved index state with the physical PostgreSQL index.

POST /configurations/{config_id}/reindex Rebuild and verify the managed text index.

POST /tsvector Query a ready TSVector configuration.

POST /fuzzy Query a ready Fuzzy configuration.

POST /configurations is the existing configuration endpoint. The nested

tsvector input shown below is an additive extension, not a replacement route.

Generate a TSVector column in one request

Set the Text base URL for either surface:

TEXT_URL = "https://api.polygres.com/v1/projects/p0123456789abcdef0123456/text"

Then create the generated column, GIN index, and saved configuration together:

curl -X POST " $TEXT_URL /configurations" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{

"name": "documents_search",

"search_kind": "tsvector",

"schema_name": "public",

"table_name": "documents",

"row_id_columns": ["id"],

"tsvector": {

"mode": "generate",

"source_columns": ["title", "content"],

"generated_column": "search_vector",

"language": "english"

},

"metadata_columns": ["title", "url"],

"filter_columns": ["status"],

"default_limit": 10,

"max_limit": 100

}'

Polygres checks the table, stable row key, source columns, output name,

metadata columns, filters, and language before changing the table. It then

creates a stored generated tsvector column, creates a GIN index, verifies the

index, and saves the configuration. PostgreSQL automatically refreshes the

generated value whenever a source column changes.

If setup fails after creating the column, Polygres tries to remove the new

index, configuration record, and generated column. A

TEXT_GENERATION_CLEANUP_FAILED response means this cleanup was incomplete and

the table must be inspected before retrying.

This workflow does not create or apply a Polygres migration. Migrations remain

available for general, versioned database changes, but they are not required

to configure text search.

Use an existing TSVector column

If the table already has a compatible tsvector column, register it without

changing the table:

{

"name" : "documents_search" ,

"search_kind" : "tsvector" ,

"schema_name" : "public" ,

"table_name" : "documents" ,

"row_id_columns" : [ "id" ],

"tsvector" : {

"mode" : "existing" ,

"column" : "search_vector" ,

"language" : "english"

},

"metadata_columns" : [ "title" , "url" ],

"filter_columns" : [ "status" ]

}

Backwards compatibility

Existing clients can continue sending the flat tsvector_column field:

{

"name" : "documents_search" ,

"search_kind" : "tsvector" ,

"schema_name" : "public" ,

"table_name" : "documents" ,

"row_id_column" : "id" ,

"tsvector_column" : "search_vector" ,

"language" : "english"

}

That field is deprecated only as a create-request input. The endpoint and the

stored response field remain available, so existing integrations do not need

an immediate change. New integrations should use tsvector.mode: "existing" .

Create a Fuzzy configuration

Fuzzy setup uses a normal text column. It creates and verifies the trigram

index, but it does not create a TSVector column:

{

"name" : "customer_name_fuzzy" ,

"search_kind" : "fuzzy" ,

"schema_name" : "public" ,

"table_name" : "customers" ,

"row_id_columns" : [ "id" ],

"text_column" : "name" ,

"similarity_threshold" : 0.3 ,

"metadata_columns" : [ "name" ],

"filter_columns" : [ "status" ]

}

A higher threshold is stricter. A lower threshold allows looser matches.

Query a configuration

Call the route that matches the saved search_kind :

curl -X POST " $TEXT_URL /tsvector" \

-H "Authorization: Bearer <token-or-runtime-api-key>" \

-H "Content-Type: application/json" \

-d '{

"query": "refund policy",

"config": "documents_search",

"filters": {"status": "published"},

"limit": 20

}'

Fuzzy search uses the same request shape at POST /fuzzy . Filters are exact

matches and must name registered filter_columns . A filter value of null

matches SQL NULL .

The response contains mode , results , next_cursor , and has_more . Each

result contains schema , table , id , key , properties , score , and

similarity . key carries all row-key values for a compound key. Treat

next_cursor as opaque and send it back unchanged as cursor .

Maintenance behavior

Use diagnostics when saved status and the physical index appear to disagree.

Use reindex after a failed or stale index, or after correcting its database target.

Updating a target column through PATCH rebuilds the index. It does not generate a new TSVector column.

Deleting a generated-column configuration removes its managed index and configuration. It does not drop the generated table column.

Keep default_limit at or below max_limit . Query limits are also capped by project limits.
