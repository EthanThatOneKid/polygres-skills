source: https://docs.evokoa.com/polygres/cli/troubleshooting
title: CLI troubleshooting | Polygres
source_hash: d0ef23aad4f2a9ecbe3fd406974dc2005b1b8c714ad1d15b35be5c80a1c01124
discovered_from: https://docs.evokoa.com/polygres

# CLI troubleshooting | Polygres

CLI troubleshooting

Symptom Action

polygres --version is older than 0.3.0 Upgrade with pipx install "polygres-cli==0.3.0" --force , or pip install --force-reinstall "polygres-cli==0.3.0" in your app venv. See package split migration .

Exit 3 or “Run polygres login ” Run polygres login , then confirm with polygres --json whoami .

Project is not selected Run polygres projects use "Project Name" , or use --project before the command.

Name is ambiguous Use the project ID from polygres projects list .

Project is still provisioning Run polygres projects status ; use the dashboard if provisioning fails.

db psql exits 9 Install PostgreSQL client tools, then rerun polygres db psql .

Text or vector query is not ready Check text configs list , vector configs list , and polygres ready .

pgContext setup is blocked Run polygres context capabilities , then polygres context sources preflight --file <request.json> for the intended source contract. add-column is valid only for an empty table.

A pgContext collection needs review Use polygres --json context collections get <collection-uuid> , then run status , verify , and diagnostics with that UUID. Inspect polygres context points status <collection-uuid> and polygres context operations list --collection-id <collection-uuid> .

Collection vectors or a deletion preview look incomplete Use global --json . The current human collection and deletion renderers lag the multi-vector response fields. For deletion, inspect collection.source_mode and collection.owns_source_table ; an owned new_table source is deleted with the collection.

A durable Context operation is still running Use polygres context operations get <operation-uuid> or polygres context operations wait <operation-uuid> and retain its request ID. A local timeout or Ctrl-C does not cancel it.

An import wait timed out Run polygres --json import status <job-uuid> before resubmitting. Exit 8 stops local polling but does not cancel the import.

A command returns MAINTENANCE_READ_ONLY or MAINTENANCE_FULL Stop immediate retries and read the dashboard maintenance notice. Read-only maintenance permits reads but blocks writes; full maintenance blocks normal API and database access.

You need to delete a project Use the dashboard project lifecycle controls , not the CLI.

For a request failure, preserve the request ID from JSON or error output when

contacting support. Preserve collection and operation UUIDs for pgContext

workflows. See reference troubleshooting for

dashboard and runtime guidance.
