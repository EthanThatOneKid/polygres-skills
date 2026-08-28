source: https://docs.evokoa.com/polygres/sdk/write-rows
title: Write rows with Python | Polygres
source_hash: d026dcdd822b62b5a21ed19b1686848b714c2ed6a40d625f3f17589e816ad24e
discovered_from: https://docs.evokoa.com/polygres

# Write rows with Python | Polygres

Write rows with the Python SDK

Use project.rows for backend code that captures one record at a time through

the Runtime API. The SDK can validate, insert, upsert, or ignore a row. It can

also keep one pgContext collection in sync with the source row.

For bulk loads, migrations, or multi-row transactions, use a native Postgres

driver or the CLI import workflow instead.

Install or upgrade

The row-writing methods require SDK 0.3.0 or newer:

pip install --upgrade "polygres-sdk==0.4.1"

Create the client with the Project API Key and Runtime API URL shown under

Connect > API & SDK :

import os

from polygres import Polygres

client = Polygres(

api_key = os.environ[ "POLYGRES_API_KEY" ],

runtime_url = os.environ[ "POLYGRES_RUNTIME_URL" ],

)

project = client.project()

Keep this code in a trusted backend. Do not put a Project API Key in a browser

or mobile application.

Check a row without writing it

Call validate() to check the request against the current table without

changing data:

check = project.rows.validate(

schema = "public" ,

table = "memories" ,

row = {

"id" : "memory_123" ,

"content" : "The user prefers concise answers." ,

"status" : "active" ,

},

mode = "upsert" ,

conflict_columns = [ "id" ],

update_columns = [ "content" , "status" ],

returning = [ "id" ],

)

print (check.valid, check.writable_columns, check.conflict_constraint)

Validation is useful while building an integration, but it does not reserve a

row or lock the table for the later write.

Insert, upsert, or ignore

Insert a new row:

result = project.rows.insert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

returning = [ "id" , "created_at" ],

)

Insert or update when a real primary key or unique constraint matches:

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = {

"id" : "memory_123" ,

"content" : "Keep answers concise." ,

"status" : "active" ,

},

conflict_columns = [ "id" ],

update_columns = [ "content" , "status" ],

returning = [ "id" ],

)

Insert only when the key is not already present:

result = project.rows.ignore(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

conflict_columns = [ "id" ],

returning = [ "id" ],

)

Each method accepts one non-empty dictionary containing JSON-native values.

Convert values such as datetime , Decimal , and custom objects before calling

the SDK. Omitted columns remain omitted, so database defaults can still apply.

The result is a RowWriteResult :

print (result.operation) # inserted, upserted, or ignored

print (result.status) # completed, pending, or partial_failed

print (result.row_committed)

print (result.returned)

print (result.request_id)

Values from json and jsonb columns remain structured Python values in

result.returned . An object or array does not need a second JSON decode.

Keep pgContext in sync

A row write does not touch pgContext unless you request reconciliation. If

exactly one ready collection uses the table, set reconcile_context=True :

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

conflict_columns = [ "id" ],

returning = [ "id" ],

reconcile_context = True ,

idempotency_key = "memory-123-v1" ,

)

When several collections use the table, select one explicitly:

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

conflict_columns = [ "id" ],

context_collection_id = "2e172638-bd77-4a2c-bc42-406f4f2938d7" ,

idempotency_key = "memory-123-v1" ,

)

Context-backed writes require an idempotency key. Create and store a stable key

for the exact logical write before making the request. Reusing that key with

different row data or options is rejected.

By default, the SDK returns when the row response arrives. If reconciliation

continues in the background, result.status is "pending" and

result.context.operation_id identifies the durable operation:

if result.status == "pending" and result.context is not None :

completed = project.context.wait_for_operation(

result.context.operation_id,

timeout = 300 ,

)

print (completed.status)

For a convenient blocking call, ask the row method to wait:

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

conflict_columns = [ "id" ],

reconcile_context = True ,

idempotency_key = "memory-123-v1" ,

wait_for_context = True ,

wait_timeout = 300 ,

)

If the wait reaches its timeout, the SDK returns the pending result. It does not

cancel the Context operation. Save the operation ID and idempotency key so a

later worker can continue checking it.

Do not call project.context.upsert_points() after a Context-backed row write.

The row request has already completed or durably started the point

reconciliation. Use point maintenance only after source rows are changed

outside this workflow. See pgContext collections and operations .

Recover safely from an uncertain write

The SDK sends each insert , upsert , or ignore request once. It does not

automatically retry a write after a timeout, connection loss, or uncertain

server response.

from polygres import PolygresAmbiguousWriteError

try :

result = project.rows.upsert(

schema = "public" ,

table = "memories" ,

row = { "id" : "memory_123" , "content" : "Keep answers concise." },

conflict_columns = [ "id" ],

reconcile_context = True ,

idempotency_key = "memory-123-v1" ,

)

except PolygresAmbiguousWriteError as exc:

save_for_recovery(

idempotency_key = "memory-123-v1" ,

request_id = exc.request_id,

details = exc.details,

)

For a Context-backed write, recover by inspecting the saved operation ID when

one is available, or repeat the exact request with the same row, options, and

idempotency key. Do not change the payload while reusing the key.

For a row-only write, inspect the table by primary key or another unique

identifier before deciding whether to retry. A blind retry can duplicate an

insert because row-only writes do not accept an idempotency key.

When result.status == "partial_failed" , the source row committed but Context

reconciliation failed or was cancelled. Inspect result.context.error and the

operation ID. Retry a Context operation only when the error marks it as

retryable, or resume the exact row request with its original idempotency key.

Store the idempotency key, row request ID, Context operation ID, and final

status with your job record. Advance your source cursor only after the required

work finishes, or after you have saved enough information for another worker

to resume it safely.

For the SDK exception hierarchy, see Python SDK error handling .

For stable server error codes, see the error catalog .
