source: https://docs.evokoa.com/polygres/cli/command-reference
title: CLI command reference | Polygres
source_hash: cdd4b2222d7063caf94644f1e3644c662e842872cdfbf2a9e67f6849ba5f9934
discovered_from: https://docs.evokoa.com/polygres

# CLI command reference | Polygres

Command reference

This is the public command surface verified against the PyPI polygres-cli 0.1.2 wheel.

Area Commands

Authentication login , logout , whoami

Projects projects list , projects use , projects create , projects status

Connection env , db info , db psql

API keys keys create , keys list , keys revoke

Data import csv , import status , migrations list , migrations apply

Graph graph discover , graph config export , graph config apply , graph build , graph status

Vector vector configs list , vector configs create , vector configs delete , vector reindex

Text text configs list , text configs create-tsvector , text configs create-fuzzy , text configs delete

Status and local configuration ready , config path

There is no CLI command for project deletion or organization switching. There are no CLI graph query commands. Use polygres <command> --help for arguments specific to a command, and put global flags before the command.
