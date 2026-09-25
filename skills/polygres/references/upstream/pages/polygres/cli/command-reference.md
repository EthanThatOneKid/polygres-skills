source: https://docs.evokoa.com/polygres/cli/command-reference
title: CLI command reference | Polygres
source_hash: bc360d4d37bade4a0acef0c32eea0db03393fc6164b0792d713148461425610e
discovered_from: https://docs.evokoa.com/polygres

# CLI command reference | Polygres

Command reference

Find commands by task, then use polygres <command> --help for detailed options.

Area Commands

Authentication login , logout , whoami

Projects projects list , projects use , projects create standard , projects create sync , projects status

Connection env , db info , db psql (standard projects provide native database connections and psql )

API keys keys create , keys list , keys revoke

Data import csv , import status , migrations list , migrations apply

Rows rows validate , rows insert , rows upsert , rows ignore

Embedding setup and status embeddings sources , embeddings models , embeddings usage , embeddings list , embeddings get , embeddings preview

Embedding generation embeddings create , embeddings update , embeddings remove , embeddings run , embeddings pause , embeddings resume , embeddings retry , embeddings reconcile , embeddings recover-oversized

Embedding search setup embeddings context

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

Context query options

context search , grouped-search , graph-first , vector-first , rank-fusion ,

and joint accept either text or your own query vector. text-hybrid can also

generate an embedding from --query so the same wording serves both semantic

and text search.

Option What it does

--embedding-json ARRAY or --embedding-file PATH Search with your own query vector

--text TEXT or --text-file PATH Generate the query vector with your configured model; use --text-file - to read standard input

--vector-name NAME Choose a vector by name, or omit this option to use the collection’s default

--request PATH Read query fields from a JSON file; use - to read standard input

--use-credits Allow additional credit usage when project spending is enabled; off by default

--idempotency-key KEY Keep the same key when retrying a query to reuse its generated embedding

--timeout SECONDS Set how long the request may take; text queries default to 130 seconds

Choose one text or vector input. Use --query for text search terms in

text-hybrid and joint . Filters, grouping, graph settings, and weights work

with either input. For recall-check , supply a vector and optionally select its

name with --vector-name .

See Context retrieval for examples.

Embedding command options

Use CLI 0.6.0 for all commands and options below. The original embedding

commands also work in CLI 0.5.0. Select a project first or use

polygres --project PROJECT embeddings COMMAND .

Command What it does

sources Find tables and text columns you can use for embeddings

models List available models, supported dimensions, and input token limits

usage Check your remaining allowances, spending, and token usage by model

list List your embedding configurations

get ID View settings and generation progress

preview --file CONFIG Check a JSON configuration and estimate usage before generating embeddings

create --file CONFIG Set up a configuration and start generating embeddings; accepts --idempotency-key KEY

update ID --file CHANGES Change the name, update mode, or permission to use credits; JSON must include expected_version

remove ID Remove a configuration using --expected-version N ; choose either --keep-output or --delete-output

run ID Process pending text changes

pause ID , resume ID Pause or resume generation

retry ID Retry work after resolving the issue shown in its status

reconcile ID Check previous processing attempts and recover saved results

recover-oversized ID Enable automatic chunking and retry rows that failed because their text was too long; use --preview to review first

context ID Get the source details to use when setting up a Context search collection

Use the configuration ID shown by embeddings list wherever a command takes

ID . For JSON input, --file - reads from standard input. When retrying the same

creation request, reuse its --idempotency-key so Polygres can recognize

the request. Use a new key when the request changes.

For update and remove , read the current version from embeddings get ID

and supply it as expected_version or --expected-version . This prevents an

older request from overwriting newer changes. The recover-oversized command

checks the version for you.

To change the model, source, dimensions, or custom chunk settings, create a new

configuration. To enable automatic chunking after rows fail because their text

is too long, use recover-oversized on the existing configuration.

Use context search with --text or an explicit query vector. Both support

collection filters. See Context retrieval for

text files, named vectors, credit usage, and retry options.

See automatic embeddings for a complete setup

example, processing options, and usage guidance.

Automatic chunking and selective recovery (CLI 0.6.0)

New generation configurations default to "chunking": {"mode": "automatic"} .

Polygres checks the text in each row against the selected model’s token limit.

Text that fits gets one embedding; longer text is split into chunks. The same

setting applies to later changes to the text.

Use "mode": "custom" with size_tokens and overlap_tokens to choose your own

chunk size, or "mode": "off" to keep one embedding per row. See

chunking settings

for help choosing. Existing configurations keep their saved settings. Copying

existing vectors defaults to chunking off.

Retry rows whose text is too long

Use this flow when generation has failed because text exceeds the model’s limit.

It enables automatic chunking on the configuration and retries the failed rows

that chunking can fix.

First, find the configuration ID:

polygres --project PROJECT embeddings list

Replace PROJECT with your project ID and CONFIGURATION_ID with the returned

configuration ID. Preview the affected rows:

polygres --project PROJECT embeddings recover-oversized CONFIGURATION_ID --preview

The preview shows how many rows can be retried, any rows chunking cannot fix,

the model’s token limit, and sample chunk counts. It does not change settings

or start generation.

To apply the change, run the command without --preview and confirm the prompt:

polygres --project PROJECT embeddings recover-oversized CONFIGURATION_ID

After confirmation:

Automatic chunking is enabled for future text changes.

The failed rows shown as recoverable are queued for generation. Rows are

checked again when you confirm, so the final count can change.

Completed embeddings are kept. Requests already awaiting recovery or

investigation are excluded from this retry.

If the configuration is paused, it stays paused. Run

polygres --project PROJECT embeddings resume CONFIGURATION_ID when ready.

Use progress monitoring to check when the queued

rows finish. If the preview finds no rows it can retry, the command exits without

changing settings. Review the row limits

for text that chunking cannot process. Configurations that copy existing vectors

cannot use this recovery command.

Use recovery in a script

Add --yes to apply the change without a prompt. For JSON output, put --json

before the command:

polygres --json --project PROJECT embeddings recover-oversized CONFIGURATION_ID --yes

If someone changes the configuration while you are reviewing it, interactive

recovery asks you to review and confirm again. Scripts stop and report the

conflict. If a request times out without confirming whether the change was

applied, check configuration progress and run a new preview before trying again.

Watch generation progress

For a single progress check:

polygres --project PROJECT embeddings get CONFIGURATION_ID --summary

To keep checking until processing finishes:

polygres --project PROJECT embeddings get CONFIGURATION_ID --watch --timeout 600

This waits for up to 10 minutes. It checks both generation and pending updates to

any connected Context collection. Generating embeddings does not create a Context

collection; follow search setup

if you have not created one.

If processing is paused or needs attention, the command stops with an explanation.

Resolve the issue, then run it again. A timeout or Ctrl-C stops watching and leaves

server processing running. Watching does not resume paused work or retry failures.

The --summary option is available on get , list , preview , create , run ,

pause , resume , retry , and reconcile . Without --summary , these commands

keep their existing JSON output. Global --json overrides --summary ; with

--watch , it returns one final JSON result or error. Missing progress values are

shown as not reported.

Batching and compatibility

Polygres groups text from rows in the same configuration into batches and runs up

to four model requests at once per configuration. Polygres manages the batch

sizes. Pausing stops new requests; requests already running can finish.

retry tries failed work again using the current settings. It does not enable

chunking. reconcile checks previous attempts for saved results. Follow the

reported status when a request needs investigation.

Existing commands, JSON output, and saved sign-in continue to work after upgrading.

The CLI also accepts older chunking JSON using enabled , size_tokens , and

overlap_tokens . Automatic chunking and recover-oversized need server support.

If the CLI reports that a server upgrade is required, contact Polygres support.
