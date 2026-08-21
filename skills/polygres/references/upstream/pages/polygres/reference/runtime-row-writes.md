source: https://docs.evokoa.com/polygres/reference/runtime-row-writes
title: Runtime Row Writes | Polygres
source_hash: 3df55694c85e8b4072e0672f456d478dd677bca9f0c8ea0759a6d2037a45cc17
discovered_from: https://docs.evokoa.com/polygres

# Runtime Row Writes | Polygres

Runtime Row Writes

Runtime row writes let an application save one row from a JSON object without

opening a PostgreSQL connection. They are a good fit for event capture, agent

memory, and other application flows that write one record at a time.

Use the project Runtime API URL shown in Connect > API & SDK . The examples

below assume that the URL, including its /v1 suffix, is stored in

POLYGRES_RUNTIME_URL .

Choose the write mode

Mode What it does Required options

insert Adds a row. A conflicting unique value returns an error. None

upsert Adds the row, or updates it when the chosen primary or unique constraint matches. conflict_columns

ignore Adds the row, or leaves the existing row unchanged when the chosen constraint matches. conflict_columns

For upsert and ignore , conflict_columns must match the columns of exactly

one non-deferrable primary-key or unique constraint. Column order does not

matter, but every conflict column must also appear in row .

An upsert updates every writable, non-conflict column present in row by

default. Set update_columns when you want a smaller update. Each selected

column must appear in row , and an empty update_columns list is not accepted.

Validate before writing

Validation checks the table, columns, values, conflict constraint, return

columns, and optional Context collection. It does not write anything. This is

useful when testing a new integration or checking a payload before it enters a

write queue.

curl " $POLYGRES_RUNTIME_URL /tables/public/memories/rows/validate" \

--request POST \

--header "Authorization: Bearer $POLYGRES_API_KEY " \

--header "Content-Type: application/json" \

--data '{

"mode": "upsert",

"row": {

"id": "memory_123",

"content": "Remember the deployment window."

},

"conflict_columns": ["id"],

"returning": ["id"]

}'

A successful validation names the matched constraint and the columns that

would be written:

{

"valid" : true ,

"operation" : "upsert" ,

"schema" : "public" ,

"table" : "memories" ,

"writable_columns" : [ "id" , "content" ],

"conflict_constraint" : "memories_pkey" ,

"context" : null ,

"request_id" : "req_abc123"

}

The Python SDK provides the same check:

validation = project.rows.validate(

schema = "public" ,

table = "memories" ,

mode = "upsert" ,

row = {

"id" : "memory_123" ,

"content" : "Remember the deployment window." ,

},

conflict_columns = [ "id" ],

returning = [ "id" ],

)

print (validation.conflict_constraint)

Write a row

Send all three modes to the same route. The mode field selects the behavior.

curl " $POLYGRES_RUNTIME_URL /tables/public/memories/rows" \

--request POST \

--header "Authorization: Bearer $POLYGRES_API_KEY " \

--header "Content-Type: application/json" \

--data '{

"mode": "upsert",

"row": {

"id": "memory_123",

"content": "Remember the deployment window."

},

"conflict_columns": ["id"],

"update_columns": ["content"],

"returning": ["id", "content"]

}'

{

"operation" : "upserted" ,

"schema" : "public" ,

"table" : "memories" ,

"returned" : {

"id" : "memory_123" ,

"content" : "Remember the deployment window."

},

"status" : "completed" ,

"row_committed" : true ,

"context" : null ,

"idempotency_key" : null ,

"request_id" : "req_def456"

}

The Python SDK has a method for each mode:

inserted = project.rows.insert(

schema = "public" ,

table = "events" ,

row = { "id" : "event_123" , "kind" : "deployment_started" },

returning = [ "id" ],

)

upserted = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Deployment moved to Friday." },

conflict_columns = [ "id" ],

update_columns = [ "content" ],

returning = [ "id" , "content" ],

)

ignored = project.rows.ignore(

schema = "public" ,

table = "events" ,

row = { "id" : "event_123" , "kind" : "deployment_started" },

conflict_columns = [ "id" ],

)

operation is inserted , upserted , or ignored . An ignore request returns

ignored with an empty returned object when it finds a conflict. If it inserts

a new row, the operation is inserted .

Return selected columns

Use returning to receive values from the committed row, including generated

defaults such as IDs or timestamps:

{

"mode" : "insert" ,

"row" : { "content" : "Prepare the release notes." },

"returning" : [ "id" , "created_at" ]

}

Omitting returning , or sending an empty list, produces an empty returned

object. You can request up to 32 distinct columns, and the serialized

returned object must be no larger than 64 KiB. Ask only for values the caller

needs.

When a returned column uses PostgreSQL json or jsonb , its value remains a

JSON object, array, string, number, boolean, or null in returned . Do not

parse it a second time as a JSON-encoded string.

Keep pgContext in sync

Add context: {"reconcile": true} when the saved row should also become a

point in a ready pgContext collection. If exactly one ready, user-managed

collection is configured for the target table, Polygres selects it. If the

table has more than one eligible collection, include collection_id to choose

one.

The row must include the collection’s source-key column. Supported source keys

are UUID, small integer, integer, bigint, text, and character-varying values.

curl " $POLYGRES_RUNTIME_URL /tables/public/memories/rows" \

--request POST \

--header "Authorization: Bearer $POLYGRES_API_KEY " \

--header "Idempotency-Key: memory-123-v1" \

--header "Content-Type: application/json" \

--data '{

"mode": "upsert",

"row": {

"id": "memory_123",

"content": "Remember the deployment window."

},

"conflict_columns": ["id"],

"returning": ["id"],

"context": {

"reconcile": true,

"collection_id": "2e172638-bd77-4a2c-bc42-406f4f2938d7"

}

}'

Context reconciliation happens after the database row commits. The response

always makes that boundary clear:

status Meaning

completed The row committed and the Context point is ready.

pending The row committed and Context work is still running. The HTTP status is 202 .

partial_failed The row committed, but Context reconciliation failed. Use the Context error and operation ID to recover.

row_committed: true means you must not repeat the database mutation as a new

write. The context object includes the collection ID, operation ID, operation

status, retry timing, and a structured error when one is available.

With the Python SDK, set reconcile_context=True or provide a

context_collection_id . Set wait_for_context=True when the caller can wait

for a pending operation to finish:

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = {

"id" : "memory_123" ,

"content" : "Remember the deployment window." ,

},

conflict_columns = [ "id" ],

returning = [ "id" ],

context_collection_id = "2e172638-bd77-4a2c-bc42-406f4f2938d7" ,

idempotency_key = "memory-123-v1" ,

wait_for_context = True ,

wait_timeout = 300 ,

)

If the wait times out, the SDK returns the pending result. The row is still

committed, and result.context.operation_id identifies the Context work.

Idempotency and safe recovery

Context-backed writes require an Idempotency-Key header. The Python SDK calls

this idempotency_key . Use a stable key for one logical write, with 1 to 128

printable ASCII characters.

The key covers the target schema, table, and complete request body. Repeating

the exact request with the same key returns or resumes the saved result without

writing the row a second time. Reusing the key with a different request returns

ROW_CONTEXT_IDEMPOTENCY_CONFLICT . The replay window is 24 hours. After that

window, an old key can return

ROW_CONTEXT_IDEMPOTENCY_EXPIRED .

Idempotency keys are intentionally limited to Context-backed writes. Do not

send one for a row-only request.

When the write outcome is unknown

A lost connection or commit acknowledgement can leave the caller unsure whether

the database accepted a write. The API reports this as

ROW_WRITE_OUTCOME_AMBIGUOUS , and the Python SDK raises

PolygresAmbiguousWriteError . It never retries a row write automatically.

Recover according to the request type:

For a Context-backed write, resend the exact same request with the same

idempotency key. Do this within the 24-hour replay window. This is also

the safe way to resume a pending or partial_failed Context result.

For a row-only write, do not immediately retry. Read the table using your

stable business key or another database connection, then decide whether a

new write is needed.

If an idempotency record has expired, verify the row and Context point before

choosing a new key. A new key represents a new logical write and is not a

replay of the original request.

Keep request_id , idempotency_key , and context.operation_id in your logs.

Include them when contacting support.

For a pending Context operation, check

GET /context/operations/{operation_id} . Once it reaches a terminal state,

replay the original row request with the same idempotency key. A successful

operation returns the combined result, while a failed operation is resumed

without writing the row again.

Authentication

Both row routes are called directly on the project Runtime API. They accept:

A project Runtime API key with project_full access.

A short-lived delegated Runtime token with the exact rows:write scope. The

caller requesting that token must have permission to execute project SQL.

Gateway Runtime tokens used by dashboard retrieval calls cannot access row

writes. Send the credential as Authorization: Bearer <credential> .

Request rules and limits

The request body is limited to 256 KiB.

row must contain 1 to 128 columns.

conflict_columns accepts up to 16 columns.

update_columns accepts up to 128 columns when supplied.

returning accepts up to 32 columns, with a 64 KiB response cap.

Schema, table, and column names use portable PostgreSQL identifiers:

[A-Za-z_][A-Za-z0-9_]* , up to 63 bytes.

Write statements have a 5-second maximum timeout and a 1-second maximum lock

wait. A project’s applied limits may be lower.

Validation is limited to 120 requests per minute for each applicable user and

project, API key, and project window, plus 1,000 per minute per IP.

Writes are limited to 60 requests per minute for each applicable user and

project, API key, and project window, plus 600 per minute per IP.

Supported JSON values include booleans, finite numbers, strings, null , arrays,

objects for JSON columns, and numeric arrays for vector columns. Send UUIDs,

dates, and timestamps as strings. Timestamps with time zone need an offset or

Z ; timestamps without time zone must not include one.

The target must be a project-owned table or partitioned table. Protected system

schemas, extension-owned relations, generated columns, identity-always columns,

and tables with forced row-level security are not writable through this API.

See Limits for a compact limits table and

Handle API errors for the shared error

response format.
