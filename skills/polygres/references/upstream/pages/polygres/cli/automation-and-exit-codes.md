source: https://docs.evokoa.com/polygres/cli/automation-and-exit-codes
title: CLI automation and exit codes | Polygres
source_hash: 17b22a2d1c97bb120309a43b193db4707d165e32b9fba56e21132ee580809453
discovered_from: https://docs.evokoa.com/polygres

# CLI automation and exit codes | Polygres

Automation and exit codes

Global options must precede the resource command:

polygres --json whoami

polygres --project "Support Search" db info

polygres --quiet ready

--json emits machine-readable results on stdout. Error JSON is also written to stdout, while human errors and --verbose traces use stderr. The available global options are --version , --json , --project , --no-color , --quiet , and --verbose .

Code Meaning

0 Success

1 General failure

2 Usage or validation failure

3 Authentication failure

4 Permission denied

5 Not found

6 Conflict, including an ambiguous project name

7 Rate limited

8 Unavailable or operation timeout

9 Missing local dependency, such as psql

CLI login is authorized with project permissions derived from the authenticated

user’s active organization role. These are permissions, not Runtime API-key

scopes. Read and mutation permissions are separate:

Area Read Mutate

Projects project:read project:create , project:update , project:delete , project:sql:execute , or project:retry_provisioning , depending on the command

Imports imports:read imports:manage

Migrations migrations:read migrations:manage

Graph graph:read graph:manage

Legacy vector vector:read vector:manage

Text text:read text:manage

pgContext context:read context:manage

Runtime metadata runtime:read Not applicable

Point scrolling and onboarding inspection are notable pgContext exceptions that

require context:manage even though they are reads. Under the current fixed

role matrix, owners and admins have all non-platform permissions, developers

have the project, import, migration, graph, legacy-vector, text, and Runtime

permissions listed for that role, and viewers have read-only permissions.

Context permissions are not currently granted to the fixed developer or viewer

roles. See roles and permissions .

CLI 0.7.0 exit-code changes

CLI 0.7.0 aligns the following errors with

their current error categories. Update scripts that branch on these exit codes

when upgrading from CLI 0.6.0.

Error CLI 0.6.0 CLI 0.7.0

PROJECT_ARCHIVED 6 8

PROJECT_ARCHIVE_CONFLICT 6 8

PROJECT_ARCHIVE_UNSUPPORTED 6 8

PROJECT_EXPORT_EXPIRED 2 8

PROJECT_EXPORT_NOT_FOUND 5 8

PROJECT_EXPORT_NOT_READY 6 8

PROJECT_EXPORT_NOT_SUPPORTED 6 8

EMBEDDING_CONNECTION_CONFLICT 2 4

EMBEDDING_MODEL_PROBE_REQUIRED 2 4

EMBEDDING_TOKENIZER_UNAVAILABLE 2 4

Use the error’s code to choose a specific recovery action. For

PROJECT_ARCHIVED , restore the project

before retrying database commands. Successfully checking project status exits

with code 0 .

The updated Runtime also identifies an archived project with HTTP 409

PROJECT_ARCHIVED , where earlier Runtime versions returned HTTP 404

RUNTIME_PROJECT_NOT_FOUND . With CLI 0.6.0, that server change moves the Runtime

error’s exit code from 5 to 6 . Central API archive errors already use HTTP

409 . See API error handling .
