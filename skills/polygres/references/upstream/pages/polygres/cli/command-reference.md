source: https://docs.evokoa.com/polygres/cli/command-reference
title: CLI command reference | Polygres
source_hash: 6807445b143d511146723ddd06716fa00cc6a47a0ec0ecdd0d247f6dd52c658e
discovered_from: https://docs.evokoa.com/polygres

# CLI command reference | Polygres

Command reference

This is the public command surface in the repository build.

Area Commands

Authentication login , logout , whoami

Projects projects list , projects use , projects create standard , projects create sync , projects status

Connection env , db info , db psql (standard projects provide native database connections and psql )

API keys keys create , keys list , keys revoke

Data import csv , import status , migrations list , migrations apply

Rows rows validate , rows insert , rows upsert , rows ignore

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

Project creation

Create a standard project hosted by Polygres:

polygres projects create standard NAME

Create a project synchronized from an existing PostgreSQL database:

polygres projects create sync NAME

Synced project creation accepts:

a securely prompted PostgreSQL URL;

--connection-env NAME ;

structured --host , --port , --database , --username , and

--password-env fields;

repeatable --table schema.table ;

--file selection.json ;

--all-eligible ;

--yes ;

--no-wait ;

--timeout <seconds> ; and

--idempotency-key <key> .

The sync creation workflow includes source checks, table discovery, selection,

and project creation.

vector configs create is retained as a migration command and always returns

VECTOR_CREATION_RETIRED . Create a pgContext collection for new vector setup.

The other vector commands continue to manage configurations registered before

creation was retired.

The generic API surface supports the versioned public routes included with the

installed CLI. Prefer dedicated commands for documented workflows because they

provide task-specific validation, output, and recovery guidance. Graph queries

are available through application APIs and the pgContext composition commands.

Use polygres <command> --help for command-specific arguments, and place global

flags before the command.

Row command options

All row commands require --table and --file <path|-> . They default to

--schema public . Repeat --returning to select returned columns.

rows validate accepts --mode insert|upsert|ignore . Upsert and ignore require

one or more --conflict-column values. Upsert also accepts repeatable

--update-column values.

Execution commands accept --wait (the default), --no-wait , and

--timeout <seconds> . Add either --reconcile-context or

--context-collection <uuid> to reconcile one pgContext collection. Context

reconciliation supports --idempotency-key <key> ; the CLI generates a key for

an executing command when one is not supplied.

See Write rows for complete examples and safe recovery guidance.
