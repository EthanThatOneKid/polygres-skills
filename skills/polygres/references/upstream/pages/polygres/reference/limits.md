source: https://docs.evokoa.com/polygres/reference/limits
title: Limits | Polygres
source_hash: b5a39188121ee0480c49b603e41cf31b317ef362abacf51e6ea0fb58461f1e8d
discovered_from: https://docs.evokoa.com/polygres

# Limits | Polygres

Limits

The effective limit is the most restrictive applicable value: request validation,

the project’s applied tier, a saved retrieval configuration, and the route’s rate

windows can all apply at once.

Use GET /tiers for current plan values. Use

GET /projects/{project_id}/status for the project’s current storage measurement and

read-only reason. The values below are the limits present in the current references;

a deployment’s live responses are authoritative.

Tier limits

Project resources

Shared and dedicated tier records can coexist. A self-service account currently starts on Shared Nano when admission capacity is available. The project’s applied tier in project status, together with GET /tiers , is authoritative.

Limit Shared Nano Shared Small Starter Pro Where to verify

Projects 1 1 1 3 GET /tiers → limits.project_limit

Enforced storage 500 MiB 8 GiB 1 GiB 5 GiB limits.storage_bytes ; compare with project status

Direct database connections 10 10 10 10 limits.direct_connection_limit

Pooled database connections 10 25 50 50 limits.pooled_connection_limit

Concurrent imports per project 3 3 3 3 limits.import_concurrency

The user-facing gateway can be more restrictive. Statement timeouts, temporary-file limits, retrieval limits, and feature flags also vary by tier. Read them from the live tier response instead of inferring them from a display name.

Graph capacity

Limit Shared Nano Shared Small Starter Pro

Graph memory 256 MB 512 MB 1,024 MB 2,048 MB

Default maximum depth 3 5 Live tier value Live tier value

Maximum depth 5 10 Live tier value Live tier value

Graph build batch size 1,000 5,000 Live tier value Live tier value

Graph edge buffer Live tier value Live tier value 500,000 500,000

Graph sync batch size Live tier value Live tier value 125 125

Shared Nano caps graph nodes, frontier, and exact path count at 10,000. Shared Small caps each at 50,000. Dedicated-tier values come from the live tier response.

Read effective graph settings and caps from

GET /projects/{project_id}/graph/system rather than assuming every setting uses the

tier maximum.

Project limits

Limit area Behavior

Project count Project creation is checked against the effective tier’s project_limit .

Storage The latest measured bytes and read_only_reason are returned by project status. The storage quota is the tier’s storage_bytes , not the provisioned volume size.

Connections Direct and pooled connection counts have separate tier caps. Use pooling for ordinary application traffic.

SQL resources Statement timeout and temporary-file limits are applied from the project tier.

Feature availability Tier metadata contains feature flags. Check GET /tiers ; do not infer availability from the tier name.

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

Retrieval request fields named limit 1..1000

Graph max_depth 1..20

Graph connection entities 2..10

Vector dimensions 1..2000

Text query length 1..2000 characters after trimming

Fuzzy similarity threshold 0..1

Exact-match filters Scalar values only; arrays and objects are rejected.

For vector and hybrid retrieval, the selected vector configuration’s max_limit can

lower the request limit. A vector request may supply max_distance or

min_similarity , but not both.

Tier graph-capacity values can constrain graph execution independently of request

shape. Check GET /tiers and graph system settings when a valid request still exceeds

runtime capacity.

Vector and text configuration limits

Constraint Vector Text

Name length Up to 80 characters Up to 80 characters

default_limit and max_limit Each 1..1000 ; default must not exceed max Each 1..1000 ; default must not exceed max

Default selection At most one default vector configuration per project No explicit is_default field; project status reports one listed text configuration

Index state missing , creating , ready , stale , or failed missing , creating , ready , stale , or failed

Count cap No tier count cap No tier count cap

List existing vector or text configurations before creating another one if you need

to avoid duplicates.

Route rate limits

All applicable windows are enforced concurrently. For example, an API-key retrieval

request can consume the API-key, project, and IP windows. — means that scope does not

apply to the route. Values are written as requests per time window.

Account, organization, project, and credentials

Route or operation User User + project API key Project IP

GET /me ; list/get projects 120/min — — — 2,000/min

POST /onboarding 5/day — — — 300/hour

GET /tiers — — — — 300/min

POST /account/tier 10/hour — — — 300/hour

List organization members 120/min — — — 2,000/min

List invitations for the authenticated email 120/min — — — 1,000/min

Add/invite/revoke/update/remove organization member 30/min — — — 500/min

Select, accept, decline, or cancel organization invitation 20/hour — — — 300/hour

Request email verification 5/hour — — — 30/hour

Complete email verification 20/hour — — — 120/hour

Update organization settings 30/min — — — 500/min

Create project 10/day — — — 300/hour

Project status — 120/min — 600/min 2,000/min

Project runtime — 60/min — 300/min 2,000/min

Retry provisioning — 6/hour — 12/hour 300/hour

Rename project — 60/min — 120/min 2,000/min

Delete project 5/day 5/day — 10/day 300/hour

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

Retrieval configuration and status

Route or operation User + project Project IP

Graph/vector discovery 20/min 60/min 1,000/min

Read graph config/status/system 120/min 600/min 2,000/min

Save graph config or graph system settings 10/min 30/min 1,000/min

Build graph 3/min 6/min 300/hour

Run graph maintenance 2/min 4/min 300/hour

Read vector configurations 120/min 600/min 2,000/min

Create or delete vector configuration 10/min 30/min 1,000/min

Update vector configuration 20/min 60/min 1,000/min

Reindex vector configuration 3/hour 10/hour 300/hour

Read text configurations 120/min 600/min 2,000/min

Create or delete text configuration 10/min 30/min 1,000/min

Update text configuration 20/min 60/min 1,000/min

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
