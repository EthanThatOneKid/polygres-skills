source: https://docs.evokoa.com/polygres/cli/api
title: Generic API routes | Polygres
source_hash: b418fa575dce84e17a1af9d5e051f5fad21fc83c75d0d7bc8d1d9aead6178c8c
discovered_from: https://docs.evokoa.com/polygres

# Generic API routes | Polygres

Generic API routes

The polygres api namespace gives scripts a generic path to versioned

control-plane operations alongside the dedicated high-level commands.

Use dedicated commands such as projects create , import csv , and

context search for their task-specific workflows. Use api routes and

api request when a script needs another route published with the installed

CLI version.

List routes

List every bundled operation:

polygres api routes

Filter by HTTP method or consume a stable JSON envelope:

polygres --json api routes --method GET

Human output includes the CLI-relative route template, method, OpenAPI

operationId , and summary. JSON output also includes the route tags. Routes

beginning with /v1 in the FastAPI document are displayed relative to the

CLI’s configured /v1 base URL.

Inspect a schema

Pass either a route template or its exact operationId :

polygres --json api request /projects/{project_id} \

--method GET \

--schema

Schema output includes declared parameters, request-body content, responses,

security metadata, and all transitively referenced component schemas. Schema

inspection reads the local snapshot and makes no API request.

If a path supports more than one method, --method is required. For an

operationId , the method can be omitted because the identifier selects one

operation.

Parameters

Supply only parameters declared for the selected operation:

polygres --json api request \

/projects/{project_id}/tables/{schema_name}/{table_name}/rows \

--method GET \

--param project_id= < project-i d > \

--param schema_name=public \

--param table_name=documents \

--param limit= 25

The selected project fills a missing project_id path parameter automatically:

polygres --json --project < project-i d > api request \

/projects/{project_id}/status \

--method GET

Use path:name=value , query:name=value , or header:name=value when the same

name is declared in more than one location. Repeat --param for array values.

Parameter values are converted and validated with their OpenAPI schemas.

Path parameters cannot contain separators, dot segments, query delimiters, or

fragments. Query strings belong in declared --param options, not in the route

argument.

JSON bodies

Use an inline JSON value:

polygres --json api request /projects \

--method POST \

--body '{"name":"Support Search"}'

Or read a UTF-8 JSON document from a file or standard input:

polygres --json api request /projects \

--method POST \

--body-file ./create-project.json

polygres --json api request /projects \

--method POST \

--body-file -

The CLI rejects a missing required body, a body on an operation that does not

declare one, non-JSON content types, unknown object fields when the schema

forbids them, and values that do not satisfy declared types or constraints.

The API still performs authoritative validation and authorization.

Review and execute a request

Start with --dry-run to validate and render the method, path, query

parameters, declared header parameters, and body:

polygres --json --project < project-i d > api request \

/projects/{project_id} \

--method GET \

--dry-run

The route argument cannot be a URL and cannot contain a query string or

fragment. Before the HTTP client runs, the CLI requires an exact bundled path

template or operationId , an allowed method for that route, declared

parameters, safe path substitutions, and a compatible JSON body. Server-side

permissions continue to apply to every request, including admin operations

listed in the snapshot.

The dry-run plan keeps credentials and transport defaults private. After

reviewing the plan, run the same command without --dry-run to execute it.

For POST , PATCH , PUT , and DELETE operations, confirm the target project,

route, parameters, and body before execution. The generic API command executes

the reviewed operation directly, while dedicated high-level commands provide

their command-specific prompts and previews.
