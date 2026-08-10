source: https://docs.evokoa.com/polygres/cli/imports-and-migrations
title: CLI imports and migrations | Polygres
source_hash: 8607e98706cc488fe534eccc1f93a5082493ade5a41ad6ee7aff4eb479e05e7c
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
