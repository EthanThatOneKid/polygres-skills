source: https://docs.evokoa.com/polygres/cli/troubleshooting
title: CLI troubleshooting | Polygres
source_hash: 39353dc4a531e0790004585baebf1469ed9dc29e569e0fe4cd86605470b87f89
discovered_from: https://docs.evokoa.com/polygres

# CLI troubleshooting | Polygres

CLI troubleshooting

Symptom Action

You need the embedding commands Install CLI 0.5.0 with pipx install "polygres-cli==0.5.0" --force , or pip install --upgrade "polygres-cli==0.5.0" in your app virtual environment. Check the version with polygres --version . See upgrade guidance .

Exit 3 or “Run polygres login ” Run polygres login , then confirm with polygres --json whoami .

Project is not selected Run polygres projects use "Project Name" , or use --project before the command.

Name is ambiguous Use the project ID from polygres projects list .

Project is still provisioning Run polygres projects status ; use the dashboard if provisioning fails.

A synced-project workflow needs SQL access Open the source PostgreSQL database with its usual database tools. Use Polygres CLI commands for synchronized retrieval workflows.

db psql exits 9 for a managed database project Install PostgreSQL client tools, then rerun polygres db psql .

Text or vector query is not ready Check text configs list , vector configs list , and polygres ready .

pgContext setup is blocked Run polygres context capabilities , then polygres context sources preflight --file <request.json> for the intended source contract. add-column is valid only for an empty table.

A pgContext collection needs review Use polygres --json context collections get <collection-uuid> , then run status , verify , and diagnostics with that UUID. Inspect polygres context points status <collection-uuid> and polygres context operations list --collection-id <collection-uuid> .

You want full vector or deletion details Add global --json to see all collection fields. Before deleting, review collection.source_mode and collection.owns_source_table : deleting a collection that owns its new_table source also deletes that table.

A durable Context operation is still running Use polygres context operations get <operation-uuid> or polygres context operations wait <operation-uuid> and retain its request ID. A local timeout or Ctrl-C does not cancel it.

A durable Context operation failed Preserve the displayed error_code , failure_stage , and operation_id . Read the operation by ID and follow the durable AI Context recovery guidance before retrying.

An import wait timed out Run polygres --json import status <job-uuid> before resubmitting. Exit 8 stops local polling but does not cancel the import.

A command returns MAINTENANCE_READ_ONLY or MAINTENANCE_FULL Stop immediate retries and read the dashboard maintenance notice. Read-only maintenance permits reads but blocks writes; full maintenance blocks normal API and database access.

You need to delete a project Use the dashboard project lifecycle controls .

Text queries

Use these steps to check your text-query setup or retry a request:

Task Action

Use --text Check polygres --version and upgrade to CLI 0.5.0. Search with polygres context search COLLECTION --text "your question" .

Choose the query input Choose one of --text , --text-file , --embedding-json , or --embedding-file . With --request , put the query fields in the JSON file.

Check embedding setup Inspect the collection with polygres --json context collections get COLLECTION_ID . In the dashboard, confirm that its selected vector uses your configured embeddings.

Choose a vector Choose a name listed on the collection, or omit --vector-name to use its default.

Continue after reaching an allowance Run polygres embeddings usage to check usage and available allowance. An organization owner or administrator can enable more spending. Add --use-credits to use those credits, or retry after the allowance renews.

Retry after a timeout Retry with the same --idempotency-key you supplied for the original query and, if needed, a longer --timeout . Generation may have completed while the CLI was waiting; keeping the same key lets Polygres reuse that work.

Send text through api request Use CLI 0.5.0 for text input. CLI 0.4.1 accepts a query vector through embedding .

Check Runtime support Use CLI 0.5.0 with a Runtime that supports query embedding generation. Queries with your own vectors also remain available.

See Context retrieval for input examples and

quota and credits for spending

permissions and allowance renewal.

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
