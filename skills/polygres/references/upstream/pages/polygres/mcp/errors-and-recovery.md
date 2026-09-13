source: https://docs.evokoa.com/polygres/mcp/errors-and-recovery
title: MCP errors and recovery | Polygres
source_hash: d0077c12d3adcf03b76227bf3c6ac27627df2922fffe55000b9bc8a12297a7e3
discovered_from: https://docs.evokoa.com/polygres

# MCP errors and recovery | Polygres

MCP errors and recovery

Polygres MCP returns stable error information that helps you choose the next

step and share a request reference with support.

Read an error

A public tool error includes this information:

For example, calling search_docs with limit: 11 returns an error like:

{

"error" : {

"code" : "MCP_VALIDATION_ERROR" ,

"variant" : "argument_at_most" ,

"message" : "The limit argument must be at most 10. Adjust it and try again." ,

"retryable" : false ,

"details" : {

"field" : "limit" ,

"constraint" : "le" ,

"limit" : 10

}

},

"request_id" : "req_example"

}

code identifies the condition. An optional variant identifies the specific

condition and recovery instructions. Match codes and variants rather than

message text in automation.

message explains what went wrong and what to do next. When safe context is

available, it names the field, limit, project, or operation involved.

Optional details supplies that context as structured data. It does not

contain rejected input values, credentials, or raw upstream exceptions.

retryable: false means the client should follow the correction or recovery

instructions instead of automatically repeating the unchanged request.

request_id connects the client result to Polygres support and diagnostics.

Keep the complete error and request ID when asking for help. The

complete error catalog lists MCP messages and

variants. When context is unavailable, the error uses its complete fallback

message instead of displaying an unresolved parameter.

Correct tool arguments

Variant What to change

argument_required Supply the field named in details.field .

argument_unexpected Remove arguments that are not listed in the tool input schema.

argument_type Use the type named in details.expected_type , such as an integer or an array.

argument_at_most , argument_at_least , argument_less_than , argument_greater_than Adjust the field to satisfy the bound named in the message and details.limit .

argument_minimum_length , argument_maximum_length Adjust the field’s length to the limit shown.

argument_multiple_of Use a value that is a multiple of details.limit .

argument_format Use the format or allowed choice shown for the field in the tool input schema.

provide_exactly_the_payload_matching_mode Supply details.required_payload and remove other mode payloads.

details.field is a dotted path such as arguments.limit . A * in a path

represents a dictionary key or path segment that is not disclosed. Check that

part of your own request; the error does not echo arbitrary dictionary keys

or rejected values.

Handle request and response limits

MCP bounds JSON exchanges to 1 MiB, 12 levels of nesting, 512 fields per object,

10,000 items per array, and 100,000 characters per string. An individual tool

can impose smaller limits. The byte limit counts compact JSON with non-ASCII

characters escaped.

Error context Recovery

details.direction: "input" Correct the indicated request field. Reduce optional data only when doing so preserves the intended operation. If the complete value is required, contact support.

A payload variant ending in _read The tool returned too much data without a verified smaller-result correction for this error. Contact support with the request ID.

A payload variant ending in _page Reduce the result-limit argument named in the message. For read_table_rows , this is arguments.limit ; for search_docs , it is limit . If one result still exceeds the bound, contact support.

A payload variant ending in _write The change may already have completed. Check the affected record or operation status before submitting the change again.

output_invalid The tool returned an unexpected response format. Contact support; if the request changed data, check its result before resubmitting.

Do not split a write or complete configuration into multiple requests unless

that tool supports the intended operation in independent batches. A smaller

request must still express the action you intend. If you change a reviewed

action’s arguments, obtain a new action proposal and confirmation.

A failed or oversized response does not prove that a write failed. For a

supported replay of the same intended action, preserve its original

idempotency key. Do not generate a new key merely because the response was

unavailable.

Restore the workflow

What the client reports Recommended next step

Connection or sign-in issue Reconnect through Polygres and complete browser approval.

Permission or project-access issue Confirm the organization, project, and your current Polygres role.

Tool outside the current catalog Create a connection with the matching project boundary, access level, and feature group.

Project-type mismatch Use standard-project tools for rows and imports, synchronized-project tools for sync, and retrieval tools supported by the selected project.

Project-state condition Read get_project_status or the matching operation status and choose the lifecycle action offered for that state.

Request validation issue Correct the named field or constraint, then retry with the corrected arguments.

Rate limit Wait for the returned retry period, then continue at a lower request rate.

Temporary service condition with retryable: true Retry the same intended call after a bounded delay. Preserve its idempotency key.

An action proposal belongs to one exact tool, project, and argument set. When

you revise any of those values, request a fresh proposal and review its new

digest.

Recover specific connection and tool errors

What happened What to do

Authentication is required or the token lacks valid connection information Reconnect and complete browser sign-in. If reauthorization does not resolve it, contact support with the request ID.

The connection URL differs from the authorized installation Restore the original URL or create and authorize a new connection with the required project and access settings.

The connection URL or its parameters are invalid Copy the complete URL from the dashboard for the intended project and access level, then reconnect.

A fixed-project connection receives a different project ID Use the project ID named in the message and details.fixed_project_id , or use another authorized connection.

A local project is not enabled Choose an enabled project or ask the local service operator to enable it.

A local tool or operation needs an access token Ask the local service operator to configure local authentication. Hosted connections instead use browser sign-in.

The requested document does not exist Call search_docs , then pass a returned document_id to get_doc .

A generic operation action is unsupported Use get_operation or wait_for_operation to inspect the operation. Use a supported domain action only when its status permits it.

An existing import cannot be retried Inspect the failure, correct the problem, and check for data already imported before starting a new dashboard import.

A project is missing a required database access role Contact support with the project and request IDs. Changing tool arguments does not create the missing role.

Follow durable operations

Keep the operation kind, operation ID, project ID, request ID, latest status,

progress, and timestamp. Use get_operation , wait_for_operation , or the

matching domain status tool to read current progress.

Operation Follow progress Available recovery path

AI Search get_operation , wait_for_operation , and Context status tools Use retry_operation for an eligible Context failure or cancel_operation for an eligible active operation.

Import list_imports , get_import , get_operation , or wait_for_operation Use cancel_import or cancel_operation for an eligible active import. Start a reviewed replacement from the Import page when needed.

Graph get_graph_status , get_operation , or wait_for_operation Review the current graph status, then prepare the appropriate build or maintenance action.

Synchronization get_synchronization_status , get_operation , or wait_for_operation Use pause, resume, retry, or resnapshot when the current synchronization state offers that action.

Each wait_for_operation call watches for up to 30 seconds. The returned state

shows the latest observed progress, and another status call can continue the

watch.

Recover an uncertain row write

Keep the original request and idempotency key. Read the record through a stable

business key and use the observed result to decide the next step. Repeating the

same intended Context-backed write with its original idempotency key lets

Polygres return the earlier result during the supported replay window. A fresh

write intent receives a fresh idempotency key.

MCP resolves recognized upstream codes and variants through the shared catalog.

Unknown upstream errors use a safe fallback. Raw upstream messages, credentials,

and operator-only configuration details are not returned in tool errors.
