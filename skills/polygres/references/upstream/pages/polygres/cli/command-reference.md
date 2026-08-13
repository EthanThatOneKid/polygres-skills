source: https://docs.evokoa.com/polygres/cli/command-reference
title: CLI command reference | Polygres
source_hash: 6ab8d3f7fa479ef6792b28c490ca947141166e3b4025bea7be2bd7944eb257fe
discovered_from: https://docs.evokoa.com/polygres

# CLI command reference | Polygres

Command reference

This is the public command surface in the repository build.

Area Commands

Authentication login , logout , whoami

Projects projects list , projects use , projects create , projects status

Connection env , db info , db psql

API keys keys create , keys list , keys revoke

Data import csv , import status , migrations list , migrations apply

Graph graph discover , graph config export , graph config apply , graph build , graph status

Vector vector configs list , vector configs create , vector configs set-default , vector configs delete , vector reindex

Text text configs list , text configs get , text configs create-tsvector , text configs create-fuzzy , text configs update , text configs diagnostics , text configs reindex , text configs delete

Context inspection and onboarding context capabilities , context init , context sources discover , context sources preflight

Context collections context collections list , context collections get , context collections status , context collections verify , context collections create , context collections update , context collections set-default , context collections diagnostics , context collections reindex , context collections delete

Context filters and points context filters list , context filters add-column , context filters add-jsonb-path , context points upsert , context points delete , context points status , context points reconcile , context points scroll

Context operations context operations list , context operations get , context operations wait , context operations cancel , context operations retry

Context retrieval context search , context text-hybrid , context graph-first , context vector-first , context rank-fusion , context joint , context grouped-search , context recall-check , context count , context facets

Generic API api routes , api request

Notices notices

Status and local configuration ready , config path

vector configs create is retained as a migration command and always returns

VECTOR_CREATION_RETIRED . Create a pgContext collection for new vector setup.

The other vector commands continue to manage configurations registered before

creation was retired.

The generic API surface can invoke versioned routes included with the CLI,

subject to the caller’s server-side permissions. Graph queries are available

through application APIs and the pgContext composition commands. Use

polygres <command> --help for command-specific arguments, and place global

flags before the command.
