source: https://docs.evokoa.com/polygres/cli/imports-and-migrations
title: CLI imports and migrations | Polygres
source_hash: 19c8fdbb738a8aa0926c0f4b649e533b8e94476188c4eac8d5f13f8054e9453c
discovered_from: https://docs.evokoa.com/polygres

# CLI imports and migrations | Polygres

Imports and migrations

CSV imports

polygres import csv ./documents.csv --table documents

polygres import csv ./documents.csv --table documents --mode append_existing

polygres import csv ./documents.csv --table documents --mode replace_existing --wait

polygres import status

CSV modes are create_table , append_existing , and replace_existing . Useful options are --schema , --encoding utf-8|utf-8-sig , --delimiter , --quote-char , --escape-char , --no-header , --wait , and --timeout .

create_table creates a destination table from the uploaded CSV.

append_existing keeps current rows and appends the uploaded rows.

replace_existing replaces every row in the selected destination table with

the uploaded data. Confirm the selected project, schema, table, file shape,

and backup or recovery plan before running this mode.

Starting with CLI 0.1.2, the CLI requests a short-lived upload session and

streams the file directly to private Azure Blob staging in bounded blocks. The

file does not pass through the public API ingress. The CLI then requests a

server-side preview and starts the staged import without resending it. The

preview is used to derive and validate the column mapping, but the current CLI

does not display it or ask for interactive confirmation before starting the

job. In particular, replace_existing has no confirmation prompt, so review

the file and target before invoking the command.

Without --wait , the command can return successfully while the job is still

queued or running. With --wait , a timeout stops only the local poll and exits

8; it does not cancel the server job. Preserve the job ID from JSON or the

timeout details, then inspect that exact job before deciding whether to retry:

polygres --json import status < job-uui d >

Do not submit the CSV again merely because local waiting timed out. If the job

ID was not retained, polygres --json import status selects the latest visible

import, which is less safe when several imports are active.

CSV admission follows the project’s effective tier storage allowance; use

GET /tiers for current values. If the upload is too large, the CLI reports

IMPORT_LIMIT_EXCEEDED , preserves the request ID and limit details, exits 2,

and does not submit the final import. Retry after choosing a smaller file or

after the project’s effective tier policy changes.

SQL migrations

polygres migrations list

polygres migrations apply --file ./migrations/001_create_documents.sql --name create_documents

If omitted, --name is derived from the file name. A duplicate migration name can exit 6.

Repeating the command with the same name and unchanged SQL is safe. Polygres

reuses the existing migration instead of creating another version.

Polygres manages the database transaction for the complete SQL file. Do not

wrap the file in BEGIN and COMMIT , and do not use another top-level

transaction command such as END , ROLLBACK , ABORT , or

PREPARE TRANSACTION . If a statement fails, earlier changes from that

migration are rolled back and the command exits 1.

If another migration is already running, the command reports

MIGRATION_LOCK_BUSY and exits 6. Your migration is unchanged. Wait for the

other migration to finish, then run the same command again.
