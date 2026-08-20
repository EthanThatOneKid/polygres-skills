source: https://docs.evokoa.com/polygres/reference/handling-api-errors
title: Handle API errors | Polygres
source_hash: 9ffcd2ed61eb5a84d377be00ae1db2cb840f50984f9b4b27f9b5990d3ba14345
discovered_from: https://docs.evokoa.com/polygres

# Handle API errors | Polygres

Handle API errors

Polygres returns structured errors so your application can decide what to do

without parsing human-readable messages.

Error response format

An API error has a top-level request ID and an error object:

{

"request_id" : "req_xxx" ,

"error" : {

"code" : "LIMIT_OUT_OF_RANGE" ,

"variant" : "graph_depth_exceeds_runtime_limit" ,

"message" : "max_depth exceeds this project's runtime limit. Reduce max_depth and retry." ,

"details" : {

"field" : "max_depth" ,

"max" : 5

}

}

}

Use the fields as follows:

code is the stable identifier for application logic.

variant is optional. It identifies a more specific condition when one code

covers several messages or HTTP statuses.

message is safe to display to a user, but it can change. Do not match or

parse it in application code.

details contains only fields approved for that error. Use it for documented

corrective actions, such as lowering a limit to details.max .

request_id identifies this request. Preserve it when contacting support.

Branch on code first. Check variant only when your application needs to

distinguish conditions within that code:

response = client.post(url, json = payload)

body = response.json()

if response.is_error:

error = body[ "error" ]

if (

error[ "code" ] == "LIMIT_OUT_OF_RANGE"

and error.get( "variant" ) == "graph_depth_exceeds_runtime_limit"

):

corrected_limit = error.get( "details" , {}).get( "max" )

elif error[ "code" ] == "IMPORT_FILE_INVALID" :

invalid_condition = error.get( "variant" )

See Error codes for the complete list of codes,

variants, HTTP statuses, and retry guidance.

Retry safely

Retry only when the request and error are retryable. In particular:

On HTTP 429 , wait for Retry-After when the header is present, then retry

with backoff.

For HTTP 408 , 500 , 502 , 503 , and 504 , use a bounded number of

attempts with exponential backoff and jitter.

Correct authentication, permissions, validation, configuration, and resource

state errors before retrying.

Preserve idempotency safeguards for requests that create or change data.

Do not start a duplicate asynchronous job because local polling timed out.

Read the original job by ID first.

The retry class in the error-code reference

summarizes the expected action for each error identity. The Python SDK retries

eligible transient requests up to its configured max_retries value and honors

Retry-After . An SDK exception means its retry budget was exhausted or the

error was not eligible for an automatic retry.

Handle Python SDK exceptions

Catch the most specific SDK exception that changes your application’s action,

and use PolygresAPIError as the common API-error fallback:

from polygres import Polygres

from polygres.errors import (

PolygresAPIError,

PolygresAuthError,

PolygresRateLimitError,

)

try :

with Polygres( api_key = api_key, runtime_url = runtime_url) as client:

results = client.project().vector.search(embedding, limit = 10 )

except PolygresAuthError:

refresh_project_credentials()

except PolygresRateLimitError as exc:

logger.warning( "Polygres rate limit" , extra = { "request_id" : exc.request_id})

except PolygresAPIError as exc:

logger.error(

"Polygres request failed" ,

extra = {

"code" : exc.code,

"status_code" : exc.status_code,

"request_id" : exc.request_id,

},

)

PolygresAPIError and its subclasses expose code , status_code ,

request_id , and safe details . The SDK uses a returned variant to select the

canonical message and status, while the stable base code remains available as

exc.code .

Local request validation raises PolygresValidationError before a request is

sent. Network failures and exhausted transient retries raise

PolygresRuntimeError . Maintenance responses raise

PolygresMaintenanceError .

Diagnose failed jobs and migrations

Imports, migrations, and other asynchronous operations can fail after the

request that started them has succeeded. Read the operation again by ID and

inspect:

error_code , the stable failure identity;

error_variant , when a more specific condition is available;

error_message , a readable description of that occurrence; and

progress or database context included with the operation.

Use the code and optional variant for application logic. Treat the stored

message as explanatory text. Correct the documented cause before creating a

new job or applying another migration. If a polling timeout occurs, keep the

operation ID and confirm its current status before retrying anything.

Log only what you need

For routine diagnostics, log the error code, optional variant, HTTP status,

request ID, route, operation ID, project ID, and timestamp. Although error

details are filtered for public responses, review them before forwarding them

to another logging or monitoring system.

Never log API keys, dashboard sessions, database passwords, authorization

headers, full SQL containing sensitive values, uploaded file contents, or

personal data. For a gateway-proxied request, preserve both X-Request-ID and

X-Polygres-Upstream-Request-ID when present.
