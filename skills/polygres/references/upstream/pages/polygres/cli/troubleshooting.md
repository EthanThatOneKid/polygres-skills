source: https://docs.evokoa.com/polygres/cli/troubleshooting
title: CLI troubleshooting | Polygres
source_hash: b758edd3347ddee30ecba49f6f43521afc0a341898df0115ac001aae32007440
discovered_from: https://docs.evokoa.com/polygres

# CLI troubleshooting | Polygres

CLI troubleshooting

Symptom Action

polygres --version is older than 0.4.0 Upgrade with pipx install "polygres-cli==0.4.0" --force , or pip install --force-reinstall "polygres-cli==0.4.0" in your app venv. See package split migration .

Exit 3 or “Run polygres login ” Run polygres login , then confirm with polygres --json whoami .

Project is not selected Run polygres projects use "Project Name" , or use --project before the command.

Name is ambiguous Use the project ID from polygres projects list .

Project is still provisioning Run polygres projects status ; use the dashboard if provisioning fails.

A synced-project workflow needs SQL access Open the source PostgreSQL database with its usual database tools. Use Polygres CLI commands for synchronized retrieval workflows.

db psql exits 9 for a managed database project Install PostgreSQL client tools, then rerun polygres db psql .

Text or vector query is not ready Check text configs list , vector configs list , and polygres ready .

pgContext setup is blocked Run polygres context capabilities , then polygres context sources preflight --file <request.json> for the intended source contract. add-column is valid only for an empty table.

A pgContext collection needs review Use polygres --json context collections get <collection-uuid> , then run status , verify , and diagnostics with that UUID. Inspect polygres context points status <collection-uuid> and polygres context operations list --collection-id <collection-uuid> .

Collection vectors or a deletion preview look incomplete Use global --json . The current human collection and deletion renderers lag the multi-vector response fields. For deletion, inspect collection.source_mode and collection.owns_source_table ; an owned new_table source is deleted with the collection.

A durable Context operation is still running Use polygres context operations get <operation-uuid> or polygres context operations wait <operation-uuid> and retain its request ID. A local timeout or Ctrl-C does not cancel it.

An import wait timed out Run polygres --json import status <job-uuid> before resubmitting. Exit 8 stops local polling but does not cancel the import.

A command returns MAINTENANCE_READ_ONLY or MAINTENANCE_FULL Stop immediate retries and read the dashboard maintenance notice. Read-only maintenance permits reads but blocks writes; full maintenance blocks normal API and database access.

You need to delete a project Use the dashboard project lifecycle controls .

Synced project setup

Result Recommended action

Source connection times out Confirm the direct hostname, port, address family, and source network allowlist.

Authentication needs attention Verify the database name, username, password, and URL encoding.

TLS verification needs attention Use the provider’s direct hostname and its verified server certificate.

Logical replication needs attention Enable logical replication and make replication capacity available at the source.

A table needs selection review Review the displayed eligibility reason, synchronization key, and eligible columns.

Creation ends before readiness Run polygres projects status and reuse the same --idempotency-key when resuming the same creation workflow.

Synchronization is paused Open the project overview and follow the displayed action.

A changed table is resyncing Follow table progress until its state returns to Streaming .

For a request failure, preserve the request ID from JSON or error output when

contacting support. Preserve collection and operation UUIDs for pgContext

workflows. See reference troubleshooting for

dashboard and runtime guidance.
