source: https://docs.evokoa.com/polygres/cli/automation-and-exit-codes
title: CLI automation and exit codes | Polygres
source_hash: 36869702032bcd9e8134b313e899765cf2212664463c843f7cb6055b2074f2e1
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

Permissions are enforced by the authenticated user’s active organization role. Common required scopes are project:read , project:create , project:update , imports:manage , migrations:manage , graph:manage , vector:manage , and text:manage . See roles and permissions .
