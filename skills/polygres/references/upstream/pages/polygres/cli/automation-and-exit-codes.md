source: https://docs.evokoa.com/polygres/cli/automation-and-exit-codes
title: CLI automation and exit codes | Polygres
source_hash: 8322ebbe6d7c4978598c11313945e6a9be717ce086850f53436418bef56d3833
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
