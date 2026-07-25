source: https://docs.evokoa.com/polygres/cli/command-reference
title: CLI command reference | Polygres
source_hash: 599d0f16eaca1ecde6e8969dc339a4d882b298d43164521375e2d5ea798d5bef
discovered_from: https://docs.evokoa.com/polygres

# CLI command reference | Polygres

Command reference

This is the public command surface for polygres-cli 0.1.3.

Area Commands

Authentication login , logout , whoami

Projects projects list , projects use , projects create , projects status

Connection env , db info , db psql

API keys keys create , keys list , keys revoke

Data import csv , import status , migrations list , migrations apply

Graph graph discover , graph config export , graph config apply , graph build , graph status

Vector vector configs list , vector configs create , vector configs set-default , vector configs delete , vector reindex

Text text configs list , text configs create-tsvector , text configs create-fuzzy , text configs delete

Status and local configuration ready , config path

There is no CLI command for project deletion or organization switching. There are no CLI graph query commands. Use polygres <command> --help for arguments specific to a command, and put global flags before the command.

vector configs set-default is available in CLI 0.1.3 and later.
