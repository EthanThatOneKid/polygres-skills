source: https://docs.evokoa.com/polygres/cli/imports-and-migrations
title: CLI imports and migrations | Polygres
source_hash: 50865b51afc73ef4d369ca48afbb8d9525275a701bfa32839cc4241194b0192a
discovered_from: https://docs.evokoa.com/polygres

# CLI imports and migrations | Polygres

Imports and migrations

CSV imports

polygres import csv ./documents.csv --table documents

polygres import csv ./documents.csv --table documents --mode append_existing

polygres import csv ./documents.csv --table documents --mode replace_existing --wait

polygres import status

CSV modes are create_table , append_existing , and replace_existing . Useful options are --schema , --encoding utf-8|utf-8-sig , --delimiter , --quote-char , --escape-char , --no-header , --wait , and --timeout .

Starting with CLI 0.1.2, the CLI requests a short-lived upload session and

streams the file directly to private Azure Blob staging in bounded blocks. The

file does not pass through the public API ingress. The CLI then requests a

preview and confirms the staged import without resending it.

CSV admission follows the project’s effective tier storage allowance; use

GET /tiers for current values. If the upload is too large, the CLI reports

IMPORT_LIMIT_EXCEEDED , preserves the request ID and limit details, exits 2,

and does not submit the final import. Retry after choosing a smaller file or

after the project’s effective tier policy changes.

SQL migrations

polygres migrations list

polygres migrations apply --file ./migrations/001_create_documents.sql --name create_documents

If omitted, --name is derived from the file name. A duplicate migration name can exit 6.
