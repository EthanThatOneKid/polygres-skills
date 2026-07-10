source: https://docs.evokoa.com/polygres/cli/imports-and-migrations
title: CLI imports and migrations | Polygres
source_hash: 629f77183354a1fcd6f3dc4a50ba63aa9b0d115b0c21800df051797659d57e4c
discovered_from: https://docs.evokoa.com/polygres

# CLI imports and migrations | Polygres

Imports and migrations

CSV imports

polygres import csv ./documents.csv --table documents

polygres import csv ./documents.csv --table documents --mode append_existing

polygres import csv ./documents.csv --table documents --mode replace_existing --wait

polygres import status

CSV modes are create_table , append_existing , and replace_existing . Useful options are --schema , --encoding utf-8|utf-8-sig , --delimiter , --quote-char , --escape-char , --no-header , --wait , and --timeout . The local upload maximum is 1 GiB, while a backend tier can impose a lower limit.

SQL migrations

polygres migrations list

polygres migrations apply --file ./migrations/001_create_documents.sql --name create_documents

If omitted, --name is derived from the file name. A duplicate migration name can exit 6.
