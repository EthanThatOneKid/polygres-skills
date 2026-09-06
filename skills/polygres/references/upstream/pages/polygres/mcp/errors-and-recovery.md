source: https://docs.evokoa.com/polygres/mcp/errors-and-recovery
title: MCP errors and recovery | Polygres
source_hash: 8b45ef802b76d002431a30063694660a9c5f27212507bfdd2be69f8dd778aeff
discovered_from: https://docs.evokoa.com/polygres

# MCP errors and recovery | Polygres

MCP errors and recovery

Polygres MCP returns stable error information that helps you choose the next

step and share a request reference with support.

Read an error

A public tool error includes this information:

{

"error" : {

"code" : "<stable error code>" ,

"retryable" : false

},

"request_id" : "<request reference>"

}

code identifies the condition.

retryable tells the client whether the same request can succeed after a

temporary condition clears.

request_id connects the client result to Polygres support and diagnostics.

Keep the complete error and request ID when asking for help.

Restore the workflow

What the client reports Recommended next step

Connection or sign-in issue Reconnect through Polygres and complete browser approval.

Permission or project-access issue Confirm the organization, project, and your current Polygres role.

Tool outside the current catalog Create a connection with the matching project boundary, access level, and feature group.

Project-type mismatch Use standard-project tools for rows and imports, synchronized-project tools for sync, and retrieval tools supported by the selected project.

Project-state condition Read get_project_status or the matching operation status and choose the lifecycle action offered for that state.

Request validation issue Correct the named field, value, or request size before sending a fresh call.

Rate limit Wait for the returned retry period, then continue at a lower request rate.

Temporary service condition with retryable: true Retry the same intended call after a bounded delay. Preserve its idempotency key.

An action proposal belongs to one exact tool, project, and argument set. When

you revise any of those values, request a fresh proposal and review its new

digest.

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
