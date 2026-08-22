source: https://docs.evokoa.com/polygres/reference/graph-retrieval-api
title: Graph Retrieval API | Polygres
source_hash: f7a5d9df27c1dd832d10c573170c78f9eeeae0409ce942e2e1c715347578650d
discovered_from: https://docs.evokoa.com/polygres

# Graph Retrieval API | Polygres

Graph Retrieval API

Graph retrieval follows relationships that you registered in the project’s graph configuration. Use it when the connections between records determine relevance, such as customers linked to tickets, orders linked to products, or documents linked by citations.

Before querying, configure and build the graph in the dashboard or with the graph CLI workflow . The graph must report Ready . Copy the project Runtime API URL and a Runtime API key from Connect > API & SDK .

Choose a method

Method Use it to

related Retrieve immediate neighbors. The Python SDK fixes the traversal depth at one. REST callers should send max_depth: 1 .

expand Traverse one or more hops and receive a flat, ranked result page.

neighborhood Traverse one or more hops and also receive page-level counts grouped by depth and table.

path Find a path between one source and one target.

connection Find a path for each consecutive pair in a list of two to ten entities.

An entity reference always contains the registered table and row ID:

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" }

Traversal controls

All five methods accept relationship_types and direction :

relationship_types limits traversal to the named, registered relationship types. An empty or omitted list allows any registered relationship type.

direction: "out" follows relationships from their configured source to destination.

direction: "in" follows them from destination to source.

direction: "any" or "both" follows either direction. The Python SDK accepts both names and sends "any" for "both" .

Path and connection queries enforce these controls. If a target is reachable only through a relationship type or direction that the request excludes, paths is empty for a path query. A connection query returns an empty path for that consecutive entity pair.

Keep max_depth small for interactive requests. The request contract permits 1..20 , but the project’s effective limit may be lower. See Limits .

Expand, related, and neighborhood

These routes share one request shape:

{

"start" : { "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

"relationship_types" : [ "opened_by_customer" ],

"direction" : "out" ,

"max_depth" : 2 ,

"filters" : { "status" : "open" },

"target_table" : { "schema" : "public" , "table" : "support_tickets" },

"limit" : 25 ,

"cursor" : null

}

target_table identifies the table to which filters apply. It does not change the start entity. Omit both filters and target_table when no result filtering is needed.

REST defaults are max_depth: 2 , direction: "both" , limit: 25 , an empty relationship list, and no filters. For a one-hop REST /graph/related request, set max_depth: 1 explicitly.

REST example

curl " $POLYGRES_RUNTIME_URL /graph/expand" \

--request POST \

--header "Authorization: Bearer $POLYGRES_API_KEY " \

--header "Content-Type: application/json" \

--data '{

"start": {"schema": "public", "table": "customers", "id": "cus_123"},

"relationship_types": ["opened_by_customer"],

"direction": "out",

"max_depth": 2,

"filters": {"status": "open"},

"target_table": {"schema": "public", "table": "support_tickets"},

"limit": 25

}'

An expand or related response contains a result page. The example omits the

route’s sql_plan diagnostic field:

{

"request_id" : "req_abc123" ,

"results" : [

{

"node" : { "schema" : "public" , "table" : "support_tickets" , "id" : "ticket_42" },

"depth" : 1 ,

"rank" : 1 ,

"path" : [

{ "table" : "public.customers" , "id" : "cus_123" },

{ "table" : "public.support_tickets" , "id" : "ticket_42" }

],

"edge_path" : [ "opened_by_customer" ],

"readable_path" : "customers:cus_123 --opened_by_customer--> support_tickets:ticket_42" ,

"properties" : { "status" : "open" , "subject" : "Cannot sign in" },

"graph_score" : 0.5

}

],

"next_cursor" : null ,

"has_more" : false

}

Use node as the record identity, properties for returned columns, depth for hop count, and readable_path when showing how the result was reached. rank is the result order and graph_score decreases with depth.

sql_plan describes the query plan selected by Polygres. Applications normally consume results , pagination fields, and request_id rather than interpreting the plan.

Neighborhood groups

POST /graph/neighborhood returns the same page plus groups :

{

"groups" : [

{ "depth" : 1 , "table" : "support_tickets" , "count" : 2 },

{ "depth" : 2 , "table" : "messages" , "count" : 5 }

]

}

Each group describes the returned nodes with that actual depth and table. Counts apply only to the current result page, not the complete traversal. Groups retain the order in which each depth and table combination first appears in results .

Python SDK examples

The Python SDK provides task-oriented defaults:

Method Depth Direction Limit

project.graph.related() 1 any 20

project.graph.neighborhood() radius=2 any 100

project.graph.expand() 5 out 50

start = { "schema" : "public" , "table" : "customers" , "id" : "cus_123" }

page = project.graph.related(

start,

relationship_types = [ "opened_by_customer" ],

direction = "out" ,

filters = { "status" : "open" },

target_table = { "schema" : "public" , "table" : "support_tickets" },

limit = 20 ,

)

for result in page.results:

print (result.node.table, result.node.id, result.depth, result.readable_path)

Use project.graph.neighborhood() when you also need groups. They are available in the page metadata because the SDK preserves route-specific response fields:

page = project.graph.neighborhood(start, radius = 2 , direction = "any" , limit = 100 )

for group in page.metadata.get( "groups" , []):

print (group[ "depth" ], group[ "table" ], group[ "count" ])

Filter scope

Graph filters are exact matches against columns registered as filters in the graph configuration. All filters in one request must resolve to one common target table.

When a filter name is registered on more than one table, select the intended owner:

page = project.graph.expand(

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

filters = { "status" : "open" },

target_table = { "schema" : "public" , "table" : "support_tickets" },

)

filters and target_table are supported by expand , related , and neighborhood . They are not request fields for path or connection .

Common filter errors tell you how to correct the request:

Code Corrective action

GRAPH_FILTER_NOT_REGISTERED Register the named column as a graph filter, or remove it from the request.

GRAPH_FILTER_SCOPE_REQUIRED Choose one table from details.candidate_tables and send it as target_table .

GRAPH_FILTER_SCOPE_INVALID Put all filters on one common registered target table, and ensure target_table is a registered graph table.

GRAPH_FILTER_SCOPE_UNSAFE Do not query a filter name registered with conflicting types across graph tables. Rename or correct the graph filter configuration.

Filters narrow retrieval results. They are not an authorization boundary. Authorize the request in your application before querying.

Paths

POST /graph/path accepts a source, target, maximum depth, relationship types, and direction. REST defaults are max_depth: 4 and direction: "any" . The Python SDK default depth is 5.

curl " $POLYGRES_RUNTIME_URL /graph/path" \

--request POST \

--header "Authorization: Bearer $POLYGRES_API_KEY " \

--header "Content-Type: application/json" \

--data '{

"source": {"schema": "public", "table": "customers", "id": "cus_123"},

"target": {"schema": "public", "table": "orders", "id": "ord_456"},

"max_depth": 4,

"relationship_types": ["placed_by"],

"direction": "out"

}'

The Python equivalent is:

response = project.graph.path(

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

{ "schema" : "public" , "table" : "orders" , "id" : "ord_456" },

max_depth = 4 ,

relationship_types = [ "placed_by" ],

direction = "out" ,

)

for path in response.paths:

print (path[ "readable_path" ])

for step in path[ "steps" ]:

print (step[ "step" ], step[ "node" ], step[ "edge_label" ], step[ "properties" ])

A found path includes source , target , depth , path , steps , and readable_path . Each step contains its zero-based step , node identity, incoming edge_label (null on the first step), and returned properties . A valid query with no path returns "paths": [] . If the target row cannot be found, the API returns GRAPH_NODE_NOT_FOUND .

Connections among several entities

POST /graph/connection accepts entities with 2 to 10 items. It evaluates each consecutive pair in order. REST defaults are max_depth: 4 and direction: "any" ; the Python SDK default depth is 5.

response = project.graph.connection(

[

{ "schema" : "public" , "table" : "customers" , "id" : "cus_123" },

{ "schema" : "public" , "table" : "orders" , "id" : "ord_456" },

{ "schema" : "public" , "table" : "products" , "id" : "prod_789" },

],

max_depth = 4 ,

relationship_types = [ "placed_by" , "contains" ],

direction = "out" ,

)

for connection in response.connections:

if connection[ "path" ]:

print (connection[ "readable_path" ])

else :

print ( "No connection" , connection[ "source" ], connection[ "target" ])

Each item in connections has the path shape described above. When a consecutive pair has no permitted path, its item has depth: null , empty path and steps arrays, and readable_path: null .

Pagination

Expand, related, and neighborhood responses contain has_more and next_cursor . When has_more is true, send the returned cursor with the same traversal options to fetch the next page. Treat the cursor as opaque.

page = project.graph.expand(start, max_depth = 3 , limit = 50 )

for result in page.auto_paging_iter():

process(result)

auto_paging_iter() follows cursors until the server reports no more pages. Path and connection responses are not paginated.

Readiness and query errors

GRAPH_CONFIGURATION_EMPTY means no graph tables are registered. Configure and build the graph before retrying.

GRAPH_NOT_READY means the current build is not Ready. Check graph status and wait for or correct the build.

GRAPH_NODE_NOT_FOUND means a requested start, source, or target entity is

absent from its stated schema and table. Verify all three entity fields. This

applies to expand, related, and neighborhood traversal as well as path and

connection queries.

GRAPH_RELATIONSHIP_TYPE_NOT_FOUND means one or more requested

relationship_types are not registered in the graph. Remove the name or

correct it to match the configured relationship type before retrying.

LIMIT_OUT_OF_RANGE or a depth limit error means the request exceeds the effective project limits. Read the returned error details and live limit guidance before retrying.

Preserve request_id when reporting a failure. See Error codes for the complete error reference.
