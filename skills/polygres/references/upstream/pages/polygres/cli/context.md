source: https://docs.evokoa.com/polygres/cli/context
title: CLI AI Search with pgContext | Polygres
source_hash: 86a0a427bcfea81a79e0a609bca97298944a928b5c2dc250b9c82e84838bcf30
discovered_from: https://docs.evokoa.com/polygres

# CLI AI Search with pgContext | Polygres

AI Search with pgContext

AI Search is the collection-based retrieval product backed by pgContext Preview. It is separate from the pgvector-backed polygres vector namespace.

Install the current CLI and confirm the version before using the Context namespace:

pipx install "polygres-cli==0.4.1"

polygres --version

polygres context capabilities --help

If context is not listed, replace the older standalone CLI installation as described in CLI installation and authentication .

Context commands use the selected project and the existing CLI login:

polygres login

polygres projects use "Support Search"

polygres context capabilities

Global flags precede context :

polygres --project p0123456789abcdef0123456 --json context capabilities

Gateway users need context:read for inspection and retrieval, including collection reads, filter listing, and point status. Collection and filter mutations, point mutations and scrolling, cancellation, and retry need context:manage .

Runtime prerequisites

Availability is determined by context capabilities , not inferred from a

PostgreSQL or extension version. Collection creation with --source existing

can convert a compatible public.vector(n) column in place to

pgcontext.vector(n) . This is a schema mutation, not a bridge. context init

is a guided onboarding front end to that same ordinary collection-creation

request. It discovers candidates only when the certified compatibility

extension is installed, but it does not activate the Runtime’s internal legacy

same-column binding. Human capability output shows the server’s actionable

blocker message. Add global --verbose to also show the stable blocker code

used by automation.

The corresponding HTTP surface is documented in the pgContext API reference .

Guided onboarding from a legacy registration

Run the one-time onboarding command after selecting a project:

polygres context init

If one Ready pgvector configuration is compatible, the CLI shows the exact table, column, dimensions, and metric and asks whether to use it as the source for a native collection. Candidate discovery requires a persisted configuration whose row ID column is id , a compatible non-generated public.vector(n) column, a Ready physical index, and the certified compatibility extension. It cannot adopt an unregistered physical index.

Pass --candidate <configuration-uuid> when more than one source is eligible. Use --name <collection-name> to override the generated <table>_context name. --refresh explicitly reruns eligibility discovery after a prior dismissal or ineligible result. --yes is required for intentional non-interactive creation and can be combined with the durable-operation flags:

polygres context init \

--candidate 123e4567-e89b-12d3-a456-426614174000 \

--name support_docs \

--yes \

--idempotency-key context-init-support-docs

The decision is saved per project. Successful collection creation marks

onboarding complete in the same database transaction. Later Context commands

and retrieval calls do not rerun discovery or validate onboarding.

context init then submits an ordinary source.mode: "existing" collection

request. It takes the same conversion path described below: dependent

non-constraint indexes, including the old pgvector HNSW index, can be dropped;

the column is converted to pgcontext.vector(n) NOT NULL ; and a new managed

pgContext index is built. The command does not delete the persisted legacy

registration, register a new legacy configuration, or re-enable one. After the

conversion, legacy retrieval is usable only if its persisted registration still

has a matching Ready physical index, which this conversion does not preserve.

Discover and preflight a source

polygres context sources discover

polygres context sources discover --schema public --schema app

polygres context sources preflight --file collection.json

polygres context sources preflight --file -

Discovery is catalog-only and does not mutate a source. Preflight accepts one strict UTF-8 JSON object. - reads standard input. YAML, JSONL, duplicate object keys, unknown fields, trailing content, and non-object roots are rejected.

Discovery can report both native pgcontext.vector(n) columns and compatible

public.vector(n) columns. For a pgvector source, preflight checks the declared

dimensions and the stored rows. A declared nullable column remains eligible

when no row contains NULL ; actual NULL vectors block conversion.

Collection lifecycle

Create from an existing compatible pgContext or certified pgvector column:

polygres context collections create support_docs \

--source existing \

--schema public \

--table articles \

--vector-column embedding \

--dimensions 768 \

--metric cosine \

--text-column content \

--result-column title \

--filter-column tenant_id

For a pgvector source, this operation takes an ACCESS EXCLUSIVE table lock,

drops indexes that depend on the vector column, converts the column through

real[] to pgcontext.vector(n) , sets it NOT NULL , and creates the pgContext

collection and its managed index in one database transaction. A

constraint-backed dependent index blocks conversion with

CONTEXT_INDEX_CONFLICT . Review this mutation and obtain approval before

creating the collection.

Create a minimal new source table:

polygres context collections create support_docs \

--source new-table \

--schema public \

--table support_docs \

--dimensions 768

Add a native pgContext vector column to an existing source table:

polygres context collections create support_docs \

--source add-column \

--schema public \

--table articles \

--vector-column embedding \

--dimensions 768 \

--metric cosine

add-column is restricted to an empty source table because the new vector

column is created as NOT NULL . It does not backfill embeddings into existing

rows. Run source preflight first and review the proposed DDL and ownership plan

before using add-column or new-table .

Create also accepts --file <path|-> ; file mode cannot be mixed with configuration flags, and the positional name remains authoritative.

Inspect and manage collections:

polygres context collections list

polygres context collections get < collection-uui d >

polygres context collections status < collection-uui d >

polygres context collections verify < collection-uui d >

polygres context collections diagnostics < collection-uui d >

polygres context collections update < collection-uui d > --max-search-limit 500

polygres context collections set-default < collection-uui d >

polygres context collections reindex < collection-uui d >

polygres context collections delete < collection-uui d >

status is a cheap saved-state view. verify actively checks correctness without mutation. diagnostics adds sanitized troubleshooting evidence and recommendations without running a repair.

Use global --json for collection list, get, and status output. The current

human renderer still reads the former single-vector summary fields and can omit

or mislabel named-vector details. In JSON, inspect collection.vectors ,

collection.default_vector_name , and each vector’s index_status .

Every collection contains one or more named vectors and has exactly one default

vector. The initial vector becomes the default at creation. The project default

collection is a separate setting changed by collections set-default ; changing

it does not change any collection’s default vector. The current CLI does not

provide commands to add another vector or change a collection’s default vector.

Use the dashboard’s Add vector and Make default actions, the public API,

or the Python SDK for those operations.

collections reindex rebuilds only the collection’s current default vector

index. It does not reindex every named vector in the collection and does not

accept a vector name.

Deletion first retrieves the collection and a server deletion plan. Do not rely

on the current human deletion preview: its field names lag the structured

response and can omit owned indexes and columns. Before approval, run

polygres --json context collections get <collection-uuid> and inspect the

collection’s source_mode , owns_source_table , vectors, and deletion plan.

The current deletion plan can also describe source preservation for an owned

new_table source, so treat the collection ownership fields as authoritative.

Deleting an existing or add_column collection preserves its source table

and rows. Deleting an owned new_table collection permanently deletes the

table and its rows after the Runtime verifies the stored table identity and

confirms that no other collection references it. When another collection uses

the same table, deletion removes only the requested collection and preserves

the table as user-managed. Interactive use accepts y or yes ;

non-interactive and JSON use require --yes .

Filter registration

polygres context filters list < collection-uui d >

polygres context filters add-column < collection-uui d > \

--key tenant_id \

--column tenant_id

polygres context filters add-jsonb-path < collection-uui d > \

--key topic \

--column metadata \

--path topic

JSONB --path is repeatable and ordered. These commands register filter sources with pgContext. They do not create PostgreSQL indexes or accept SQL.

Point maintenance

polygres context points upsert < collection-uui d > doc_1 doc_2

polygres context points delete < collection-uui d > doc_1

polygres context points status < collection-uui d >

polygres context points reconcile < collection-uui d >

polygres context points scroll < collection-uui d > --limit 50

Upsert and delete accept 1 through 10,000 source keys and preserve them as text. Batches up to the server synchronous threshold can complete immediately; larger batches return durable operations. reconcile adds missing mappings and removes mappings for deleted rows. If the source table uses row-level security, it does not remove orphan mappings because a hidden row may still exist. The result reports orphan_cleanup_skipped_reason: "source_rls_enabled" ; delete keys explicitly when you know their source rows were removed. There are no public backfill or sync aliases.

After a point upsert or delete, the collection’s reported mapped-point count is

updated with the same operation. Use points status or collections verify to

investigate a stale reconciliation state, then run points reconcile when the

source table and active point mappings need to be brought back into agreement.

Point scrolling respects row-level security. A page can be empty and still return has_more: true when hidden rows were skipped, so continue until has_more is false. Ranked retrieval never has a cursor.

Durable operations

Mutations wait by default and accept:

--no-wait

--timeout <seconds>

--idempotency-key <key>

The CLI generates a UUIDv4 idempotency key when omitted and reuses it for eligible transport retries in the same invocation. For automation and any workflow that may resume in a later process, generate a stable key first, persist it with the job record, and pass it on the initial command:

polygres context collections reindex < collection-uui d > \

--idempotency-key reindex-2026-08-05-support-docs

Reuse that same key when resuming the same intended mutation.

Inspect and control operations:

polygres context operations list

polygres context operations get < operation-uui d >

polygres context operations wait < operation-uui d >

polygres context operations wait < operation-uui d > --poll-interval 2 --timeout 1800

polygres context operations cancel < operation-uui d >

polygres context operations retry < operation-uui d >

Waiting reports real stage and committed-count changes. It uses an adaptive poll interval unless a fixed interval is supplied, honors Retry-After , and uses one monotonic timeout. A timeout or Ctrl-C stops local waiting but does not cancel the server operation.

Failed operations

CLI 0.4.1 includes the stable error code, failure stage, and operation ID in

human-readable output when a durable operation fails:

Context collection sync failed. Retry the operation. (error_code:

CONTEXT_COLLECTION_SYNC_FAILED, failure_stage: syncing_points, operation_id:

00000000-0000-0000-0000-000000000001)

Use polygres context operations get <operation-uuid> to read the durable

record before retrying. Correct storage, memory, index, or source problems

first when the code requires user action. A timeout or connection failure can

be retried after the dependency is healthy. Preserve the operation ID when

contacting support. See Handle API errors

for the recovery table.

Aggregates

polygres context count support_docs

polygres context facets support_docs status --limit 10

Both accept --filter-json <object> or --filter-file <path> . Facet fields must be registered filter keys.

Ranked retrieval

All ranked modes accept one embedding source:

--embedding-json <json-array>

--embedding-file <path>

Alternatively, --request <path|-> supplies one strict request object. The positional collection remains authoritative, so the object must not contain a collection field. Request-file mode cannot be mixed with request-body flags.

Flag mode does not expose --vector-name , so it always omits vector_name and

uses the collection’s default vector. To select an exact named vector, use a

request object that contains vector_name and the method’s other required

fields. For a three-dimensional test collection, search-request.json can

contain:

{

"embedding" : [ 0.12 , -0.08 , 0.31 ],

"vector_name" : "title_semantic" ,

"limit" : 10

}

Then run:

polygres context search demo_3d --request search-request.json

The name must exactly match a vector in that collection, and the embedding

dimensions must match that vector. If vector_name is omitted, ranked

retrieval uses the collection’s default vector.

Dense:

polygres context search support_docs \

--embedding-file query-embedding.json \

--filter-json '{"must":[{"key":"tenant_id","match":"acme"}]}'

Dense plus full text:

polygres context text-hybrid support_docs \

--embedding-file query-embedding.json \

--query "reset password"

Graph first:

polygres context graph-first support_docs \

--embedding-file query-embedding.json \

--start-schema public \

--start-table accounts \

--start-id acct_123

Vector first:

polygres context vector-first support_docs \

--embedding-file query-embedding.json \

--context-limit 50 \

--graph-limit 200

Independent weighted rank fusion:

polygres context rank-fusion support_docs \

--embedding-file query-embedding.json \

--start-schema public \

--start-table accounts \

--start-id acct_123 \

--context-weight 0.7 \

--graph-weight 0.3

The wire mode is rank_fusion . The joint command below is a separate coupled retrieval algorithm and is not an alias.

Coupled Joint retrieval:

polygres context joint support_docs \

--embedding-file query-embedding.json \

--query "Which deployment guidance is current?" \

--start-json '{"schema":"public","table":"accounts","id":"acct_123"}' \

--relationship-type account_document \

--semantic-weight 0.4 \

--lexical-weight 0.2 \

--graph-weight 0.4

Joint calls only the pgContext /context/hybrid/joint Gateway route. Repeat --start-json for multiple explicit graph anchors, or use --request for the complete strict Joint request body. It is distinct from rank-fusion and does not retry automatically.

Grouped dense search and recall:

polygres context grouped-search support_docs \

--embedding-file query-embedding.json \

--group-by tenant_id \

--group-limit 1

polygres context recall-check support_docs \

--embedding-file query-embedding.json \

--minimum-recall 0.95

Ranked responses have no cursor. The CLI preserves server order and scores; human output uses eight decimal places while JSON retains the API number.

Human and JSON output

Human output uses stable tables and detail views. Wait progress and verbose request traces use stderr. Machine output is the exact API envelope as one sorted JSON object on stdout:

polygres --json context search support_docs \

--embedding-file query-embedding.json

--quiet suppresses human success and wait output but never suppresses JSON or errors.

For collection vectors and deletion review, JSON is required until the human

formatters are updated for the multi-vector response and current deletion-plan

field names. Do not parse human tables in automation.

Exit codes

Context uses the standard CLI codes: 0 success, 1 general failure, 2 local or API request validation, 3 authentication, 4 permission, 5 not found, 6 conflict, cancellation, or unavailable Context state, 7 rate limited, and 8 service unavailable or operation timeout.

Cleaning up synthetic resources

Delete a synthetic collection with its exact UUID and --yes . The server deletion plan identifies the resources that will be removed. Deleting a new_table collection also deletes its managed table and data unless another collection references that table, in which case the table is preserved as user-managed. existing and add_column sources are preserved. If Polygres cannot confirm the stored identity of a managed table, deletion stops with CONTEXT_SOURCE_OWNERSHIP_MISMATCH .

Complete command map

Area Commands

Inspection capabilities ; sources discover ; sources preflight

Collections collections list , get , create , status , verify , update , diagnostics , delete , set-default , reindex

Filters filters list , add-column , add-jsonb-path

Points points upsert , delete , status , reconcile , scroll

Operations operations list , get , wait , cancel , retry

Aggregates count ; facets

Retrieval search ; text-hybrid ; graph-first ; vector-first ; rank-fusion ; joint ; grouped-search ; recall-check

Run polygres context <command> --help for a top-level command, or polygres context <area> <command> --help for a nested command. Global flags such as --json and --project must remain before context .
