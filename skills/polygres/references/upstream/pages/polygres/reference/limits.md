source: https://docs.evokoa.com/polygres/reference/limits
title: Limits | Polygres
source_hash: f7574ce99e1855760d2af973f5c9bc706e549420d9183ab7136cb11be5a2e6f6
discovered_from: https://docs.evokoa.com/polygres

# Limits | Polygres

Limits

The effective limit is the most restrictive applicable value: request validation,

the project’s applied tier, a saved retrieval configuration, and the route’s rate

windows can all apply at once.

Use the project dashboard for a Basic project’s configured capacity. Use

GET /tiers for the shared and legacy tiers returned to your account, and use

GET /projects/{project_id}/status for the project’s current storage measurement

and read-only reason. The values below are the limits present in the current

references; a deployment’s live responses are authoritative.

Tier limits

Project resources

The self-service creation flow starts with the exact Free values. Increasing

Storage, Context, or Graph switches all three controls to at least the Basic

minimum. The project tier and limits shown by the project and Billing pages are

authoritative.

Limit Shared Nano (Free) Basic (Paid) Where to verify

Organization project allowance 1 Free project Paid projects leave the Free slot available Project list and Billing

Included storage 500 MiB 2 GiB configured capacity limits.storage_bytes ; compare with project status

Direct database connections 10 25 project-owner connections Live tier limits

Pooled database connections 10 50 limits.pooled_connection_limit

Concurrent imports per project 3 3 limits.import_concurrency

The one Free slot is shared across hosted and synchronized project modes. Paid

Basic projects leave the slot available. Existing organizations with more than

one Nano project can continue using those projects. They can create another

Free project after the organization no longer has a Nano project.

The exact Free selection is 500 MiB Storage, 100,000 Context points, and

100,000 Graph units. Increasing any of the three switches the selection to at

least the Basic minimum shown below. Use Use free capacity in the

new-project form to return all three values to the Free selection.

Starter and Pro are retained only for historical projects and are unavailable

for new assignment. Other legacy tier records can also remain visible in live

responses. Do not use them as current self-service choices.

The user-facing gateway can be more restrictive. Statement timeouts, temporary-file limits, retrieval limits, and feature flags also vary by tier. Read them from the live tier response instead of inferring them from a display name.

Graph capacity

Limit Shared Nano Basic

Graph memory 256 MB 1,024 MB base value

Default maximum depth 3 Live tier value

Maximum depth 5 Live tier value

Graph build batch size 1,000 Live tier value

Graph edge buffer Live tier value 500,000

Graph sync batch size Live tier value 125

Shared Nano caps graph nodes, frontier, and exact path count at 10,000. Basic

has a separate configured Graph capacity measured in weighted units:

weighted Graph units = active nodes + (active edges / 10)

Each active node therefore consumes 1 unit and each active edge consumes 0.1

unit. Execution limits still come from live project and graph-system responses.

Graph builds on Basic projects run synchronously. When calling the graph-build

API directly, set concurrent to false .

Read effective graph settings and caps from

GET /projects/{project_id}/graph/system rather than assuming every setting uses the

tier maximum.

Project limits

Limit area Behavior

Project count The organization shares one Nano slot. Paid projects leave that slot available.

Storage The latest measured bytes and read_only_reason are returned by project status. The storage quota is the tier’s storage_bytes , not the provisioned volume size.

Connections Direct and pooled connection counts have separate tier caps. Use pooling for ordinary application traffic.

SQL resources Statement timeout and temporary-file limits are applied from the project tier.

Feature availability Check the options shown by the dashboard and the project’s capability responses; do not infer availability from the tier name.

Paid-project Storage, Context, and Graph limits

Limit Included Creation maximum Increment Additional monthly price

Storage 2 GiB 128 GiB 1 GiB $2

Context 200,000 points 4,000,000 100,000 $3

Graph 200,000 weighted units 4,000,000 100,000 $1

The Basic project base price is $16 per month. The dashboard shows whether the

selected limits are currently available before you create the project.

When a change raises the monthly price, Polygres collects the prorated amount

due and activates the higher limits immediately after payment succeeds. When a

change lowers the monthly price, Polygres schedules the lower limits and price

for the next organization billing date.

Graph prices and limits use the weighted formula above. For example, 100,000

active nodes and 1,000,000 active edges consume 200,000 weighted Graph units.

Context and Graph capacity states

Basic projects enforce configured Context and weighted Graph capacity using the

same state boundaries:

State Usage Behavior

Healthy More than 20,000 units below the configured limit Context or Graph work proceeds normally.

Approaching Within 20,000 units below the configured limit The dashboard warns that the project is approaching capacity.

Grace At the limit and up to 49,999 units above it Existing data remains available, but the dashboard asks you to increase capacity or reduce usage.

Paused 50,000 units or more above the configured limit Work that would consume more of the affected capacity is paused.

After Context or Graph enters Paused , the warning remains visible until

usage falls below the configured limit or a higher capacity takes effect.

Use the project’s Upgrade page to add capacity immediately or schedule a

lower limit for the next billing date. Current usage and active work must fit

within every lower limit. Polygres confirms this when you submit the change and

again before a scheduled decrease takes effect.

Import caps

CSV file admission equals the effective active tier’s contractual

limits.storage_bytes . The file is still admitted by source size, independently

of current free space and possible database expansion. Use live GET /tiers

output for current values; this page does not duplicate them.

SQL and pg_dump retain their independent tier upload fields. Read those live

fields from GET /tiers rather than relying on copied plan values.

Additional import constraints:

Constraint Value or behavior

Active jobs Current tiers allow three queued or running imports per project.

Filename 1–255 characters; must start with an alphanumeric character and cannot contain / or \\ .

CSV identifiers Header, schema, table, column, and mapping names must match [A-Za-z_][A-Za-z0-9_]* .

CSV modes create_table , append_existing , or replace_existing . Replace mode truncates the target before loading the staged rows.

An oversized CSV returns HTTP 413 with IMPORT_LIMIT_EXCEEDED ; the CLI exits 2,

preserves the error details and request ID, and does not retry. An occupied

import slot returns IMPORT_CONCURRENCY_LIMIT .

Retrieval and data-tool limits

Input Limit

Table viewer limit 1..500

Retrieval request fields named limit Request-shape range 1..1000 ; the effective project cap can be lower.

Hybrid retrieval vector_limit Request-shape range 1..1000

Graph max_depth 1..20

Graph connection entities 2..10

Vector dimensions 1..2000

Text query length 1..2000 characters after trimming

Fuzzy similarity threshold 0..1

Exact-match filters Scalar values only; arrays and objects are rejected.

The 1..1000 range above is the API contract ceiling, not a guarantee that every

project can return 1,000 results. Runtime API routes enforce the project’s live

retrieval_max_limit against result fields named limit . Read the project’s

applied tier from project status, then read limits.retrieval_max_limit from

GET /tiers . Always use this live value rather than a copied plan value. A

selected vector or text configuration’s max_limit can lower the number of

results returned further.

For hybrid retrieval, vector_limit controls how many vector candidates are

considered before graph processing and final ranking. limit controls how many final

results are returned. vector_limit is bounded by the 1..1000 request contract;

it is not the result limit advertised by limits.retrieval_max_limit . Choose a

candidate count appropriate for your workload and keep limit at or below the

live project maximum. A vector request may supply max_distance or

min_similarity , but not both.

When a result limit exceeds the live project maximum, the Runtime API returns

HTTP 400 LIMIT_OUT_OF_RANGE with the effective min and max in details .

Correct the value before retrying. Do not send the same invalid value to a

fallback route, because that produces another validation failure. Values outside

the request-shape range are rejected during request validation.

Tier graph-capacity values can constrain graph execution independently of request

shape. Check GET /tiers and graph system settings when a valid request still exceeds

runtime capacity.

pgContext limits

Read GET /context/capabilities on the project Runtime API, or

GET /projects/{project_id}/context/capabilities through the Gateway, for the

effective Context limits. These values are authoritative because project

runtime support can be more restrictive than request-shape validation.

Input Contract maximum or behavior

Vector dimensions 1..16000 , further limited by max_dimensions

Ranked result limit 1..1000 , further limited by the collection and max_search_limit

Result columns per collection 32

Initial column and JSONB filters 32 of each

JSONB filter path segments 16

Point keys per upsert or delete 1..10000

Synchronous point mutation Up to 1,000 keys; larger valid requests return a durable operation

Source key after canonical conversion 1,024 bytes

Relationship types per graph request 32

Capabilities also report effective graph depth and candidate limits, filter

bytes, depth, nodes, and value limits, reconciliation batch limits, and

feature-specific blockers. Do not infer these values from the pgContext

extension version.

A collection is created with one initial vector and can contain multiple named

vectors over the same source table. Exactly one vector is the collection

default. Ranked retrieval uses that vector when vector_name is omitted; when

present, vector_name must exactly match a vector in the collection. The

project also has at most one default collection, independently of each

collection’s default vector.

Runtime row-write limits

Input or execution limit Maximum

Request body 256 KiB

Columns in row 128

conflict_columns 16

update_columns 128

returning columns 32

Serialized returned object 64 KiB

Statement timeout 5 seconds

Lock wait 1 second

Context idempotency key 1 to 128 printable ASCII characters

Context idempotency retention 24 hours

The statement and lock values are ceilings. A project’s applied values may be

lower. Context idempotency is available only when the row request also asks for

pgContext reconciliation.

Vector and text configuration limits

Constraint Vector Text

Name length Up to 80 characters Up to 80 characters

default_limit and max_limit Each 1..1000 ; default must not exceed max Each 1..1000 ; default must not exceed max

Default selection At most one default vector configuration per project No explicit is_default field; project status reports one listed text configuration

Index state A persisted enabled registration must be effectively Ready. HNSW requires its exact physical index to be ready ; an existing index_kind: none registration can be Ready for exact scan without HNSW. missing , creating , ready , stale , or failed

Count cap No tier count cap No tier count cap

New vector configuration creation and re-enabling are retired. These vector

constraints describe previously registered configurations. A physical

pgvector index without a persisted enabled registration is not usable through

legacy retrieval. For new vector setup, use the pgContext collection limits

above. List existing text configurations before creating another one if you

need to avoid duplicates.

Route rate limits

All applicable windows are enforced concurrently. For example, an API-key retrieval

request can consume the API-key, project, and IP windows. — means that scope does not

apply to the route. Values are written as requests per time window.

Account, organization, project, and credentials

Route or operation User User + project API key Project IP

GET /me ; list/get projects 120/min — — — 2,000/min

POST /onboarding 5/day — — — 300/hour

GET /tiers — — — — 300/min

List organization members 120/min — — — 2,000/min

List invitations for the authenticated email 120/min — — — 1,000/min

Add/invite/revoke/update/remove organization member 30/min — — — 500/min

Select, accept, decline, or cancel organization invitation 20/hour — — — 300/hour

Request email verification 5/hour — — — 30/hour

Complete email verification 20/hour — — — 120/hour

Update organization settings 30/min — — — 500/min

Create project 10/hour — — — 300/hour

Create synchronized-project preflight 10/hour — — — 300/hour

Read billing, credits, project quotes, or top-up history 120/min — — — 2,000/min

Set up payment, buy a top-up, create a Paid project, or change project limits 30/min — — — 500/min

Project status — 120/min — 600/min 2,000/min

Project runtime — 60/min — 300/min 2,000/min

Start a Basic upgrade — 6/hour — 12/hour 300/hour

Read Basic upgrade progress — 60/min — 300/min 2,000/min

Retry provisioning — 6/hour — 12/hour 300/hour

Rename project — 60/min — 120/min 2,000/min

Delete project 10/hour 10/hour — 10/hour 300/hour

List API keys — 60/min — 120/min 2,000/min

Create or revoke API key — 20/day — 50/day 300/hour

Get connection info — 120/min 120/min 600/min 3,000/min

Reveal database password — 20/hour — 30/hour 300/hour

Reset database password — 20/hour — 30/hour 300/hour

Data, imports, and migrations

Route or operation User + project Project IP

List tables or read table rows 60/min 300/min 2,000/min

Run SQL query 30/min 150/min 1,000/min

CSV preview 20/min 100/min 1,000/min

Start CSV import 10/min 40/min 1,000/min

Start SQL import 5/min 20/min 1,000/min

Start pg_dump import 3/min 10/min 1,000/min

List or get imports 120/min 600/min 2,000/min

Cancel import 20/min 60/min 1,000/min

List or get migrations 120/min 600/min 2,000/min

Create migration 10/min 30/min 1,000/min

Apply migration 5/min 10/min 1,000/min

Runtime row writes

Route User + project API key Project IP

Validate one row write 120/min 120/min 120/min 1,000/min

Write one row 60/min 60/min 60/min 600/min

Only the scopes that apply to the active credential are charged, and every

applicable window is enforced at the same time.

Retrieval configuration and status

Route or operation User + project Project IP

Graph/vector discovery 20/min 60/min 1,000/min

Read graph config/status/system 120/min 600/min 2,000/min

Save graph config or graph system settings 10/min 30/min 1,000/min

Build graph 3/min 6/min 300/hour

Run graph maintenance 2/min 4/min 300/hour

Read vector configurations 120/min 600/min 2,000/min

Retired vector create route or delete vector configuration 10/min 30/min 1,000/min

Update vector configuration 20/min 60/min 1,000/min

Reindex vector configuration 3/hour 10/hour 300/hour

Read text configurations 120/min 600/min 2,000/min

Create text configuration 20/min 60/min 1,000/min

Delete text configuration 10/min 30/min 1,000/min

Update text configuration 20/min 60/min 1,000/min

pgContext AI Search

Route family User + project API key Project IP

Capabilities, discovery, preflight, collection reads, verification, diagnostics, filters, and point inspection 120/min 240/min 600/min 2,000/min

Search, count, facets, grouped search, recall, text hybrid, graph composition, rank fusion, and Joint 300/min 600/min 1,500/min 3,000/min

Collection updates, filter registration, point batches, and cancellation 20/min 20/min 60/min 1,000/min

Operation listing and polling 600/min 1,200/min 3,000/min 4,000/min

Collection deletion, reindex, reconciliation, and operation retry 20/hour 10/hour 25/hour 300/hour

All applicable scopes are evaluated together. Use the response’s

Retry-After value as the effective retry time for the current project and

route.

Retrieval queries

Route family User + project API key Project IP

Readiness 120/min 120/min 600/min 3,000/min

Graph expand, neighborhood, related 300/min 600/min 1,500/min 3,000/min

Graph path or connection 120/min 240/min 600/min 2,000/min

Vector search or similar-to 300/min 600/min 1,500/min 3,000/min

Text tsvector or fuzzy search 300/min 600/min 1,500/min 3,000/min

Hybrid graph-first, vector-first, or joint 120/min 240/min 800/min 2,000/min

Authentication failures are separately limited to 20 failures in 5 minutes, followed

by a 10-minute lockout. On HTTP 429 , honor Retry-After when present and use

backoff; immediate parallel retries consume the same windows.

Read-only behavior

A project can enter read_only after storage policy enforcement.

Check Expected behavior

Diagnose Read status.project , last_storage_measurement.measured_bytes , checked_at , and read_only_reason from project status.

Writes and imports They may fail while the project remains read-only. Do not repeatedly retry write-like routes.

Retrieval It may continue if the data-plane services and required retrieval indexes are available. Check readiness before relying on it.

Clear the condition Remove data where possible, change the effective tier/storage allocation, or contact support. Wait for a later storage measurement to confirm recovery.

Do not infer that the block is cleared solely because one read succeeds. Confirm that

the project status has left read_only .
