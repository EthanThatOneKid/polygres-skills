source: https://docs.evokoa.com/polygres/platform/projects/postgresql-source-setup
title: PostgreSQL Sync Setup Guides | Polygres
source_hash: 1ca6c6981b920aaa6c5f8b8a92e3ab370b8e5880e05a1074fe38674416066b29
discovered_from: https://docs.evokoa.com/polygres

# PostgreSQL Sync Setup Guides | Polygres

PostgreSQL Sync Setup Guides

Choose your source below for the exact setup steps and connection details to copy into Polygres. Complete the relevant guide before opening the synced-project wizard .

Your source Follow this guide

Self-hosted PostgreSQL or another managed provider Standard PostgreSQL

Neon Neon

Supabase Supabase

PlanetScale Postgres PlanetScale

Polygres uses a direct PostgreSQL connection for logical replication. Choose

the provider’s direct database endpoint; transaction poolers and serverless

database APIs serve other application traffic.

Prepare the source connection

Use a direct PostgreSQL connection:

postgresql://USERNAME:PASSWORD@HOST:5432/DATABASE

Prepare:

the direct database hostname;

port 5432 , or the direct port provided by the database provider;

the database name;

a username with logical-replication and selected-table access; and

its password.

In the dashboard, enter the complete URL or use structured connection fields.

For CLI automation, store the URL in an environment variable and pass the

variable name:

export SOURCE_DATABASE_URL = "postgresql://..."

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL

Provider dashboards may also show pooled URLs, API endpoints, and command-line

examples. Choose the direct PostgreSQL URL for synchronization.

Standard PostgreSQL

Configure wal_level = logical on the source and restart PostgreSQL if the setting change requires it.

Ensure max_wal_senders and max_replication_slots each have at least one free entry for Polygres.

Use a role that can connect to the database, inspect the catalog, read the selected public tables, and support logical replication.

Give each selected table a primary key or another eligible unique, non-null replica-identity index.

Permit inbound TCP connections from the Polygres regional egress addresses shown in the wizard if a firewall or database allowlist is active.

Copy the direct connection URL into Polygres and run the checks.

Neon

Enable logical replication

Open the Neon Console and select the source project.

Open Settings , then Logical Replication .

Select Enable and allow Neon to restart the project’s computes.

In Neon’s SQL Editor, run SHOW wal_level; and confirm that it returns logical .

Neon notes that an active logical-replication subscriber prevents the source compute from scaling to zero. It also removes inactive replication slots after approximately 40 hours under the conditions described in Neon’s logical replication guide .

Copy the Neon connection URL

Return to the Neon project dashboard and select Connect .

Select the branch, database, and role that Polygres should use.

Turn Connection pooling off. Choose the direct hostname, which omits -pooler , for logical replication.

Choose Connection string and copy the complete direct URL. It resembles:

postgresql://ROLE:PASSWORD@ep-example-123456.us-east-2.aws.neon.tech/DATABASE?sslmode=require

Paste that URL into PostgreSQL connection URL in Polygres.

Use a role created through the Neon Console, CLI, or API so it inherits Neon’s

replication capability. See

Logical replication in Neon .

Configure Neon IP Allow when enabled

When IP Allow is enabled, copy every regional egress address displayed by

Polygres into the Neon project’s IP Allow list before testing. Other Neon

projects can continue directly to the source check.

PlanetScale

Enable logical replication

Open the PlanetScale database and select Clusters .

Open Parameters for the source cluster.

Set wal_level to logical .

Set max_replication_slots and max_wal_senders high enough to leave at least one slot and sender available to Polygres. PlanetScale recommends twice the number of subscribers as a starting point.

Set max_slot_wal_keep_size above 4 GB and monitor retained WAL against the source change rate and available disk.

Set hot_standby_feedback and sync_replication_slots to on . PlanetScale requires both settings to synchronize logical slots to standbys during failover.

Apply the queued parameter changes before testing the connection.

Create a dedicated replication role

Select Connect on the PlanetScale database branch.

Choose User-defined role and give the role a recognizable name such as polygres-sync-main .

Select the inherited postgres role.

Enable WITH REPLICATION .

Create the role. pg_create_subscription is not required because Polygres consumes the source WAL directly.

PlanetScale requires the inherited postgres role before its managed role

builder enables WITH REPLICATION . The resulting role can create the

filtered publication and replication slot that Polygres manages.

Copy the PlanetScale connection URL

In the connection panel, choose General PostgreSQL .

Copy the direct URL on port 5432 . Do not use the PgBouncer endpoint on port 6432 .

Store the password immediately because PlanetScale displays it only once.

Paste the complete URL into PostgreSQL connection URL in Polygres. It resembles:

postgresql://ROLE.BRANCH-ID:PASSWORD@REGION.pg.psdb.cloud:5432/postgres?sslmode=verify-full&sslrootcert=system

Polygres accepts PlanetScale’s sslrootcert=system option and uses the system

certificate-authority store with full hostname verification. Arbitrary

customer-provided certificate paths remain unsupported.

Protect the replication slot during failover

PlanetScale cannot register a Polygres slot until the first capture creates it. Immediately after the capture starts:

Copy the exact pgres_cdc_... slot name from PlanetScale’s logical replication warning or from pg_replication_slots .

Open Clusters , Parameters , then the Failover section.

Confirm that hot_standby_feedback and sync_replication_slots are both on .

Add the slot name under Logical slot name . Use Add another value for every additional active Polygres slot.

Queue and apply the parameter changes, then confirm that PlanetScale’s logical replication warning clears.

An unregistered slot can be removed during a switchover or cluster change, forcing the subscriber to be recreated and fully synchronized. Monitor replication lag and remove a registered slot only after its Polygres project no longer uses it.

Supabase

Copy the Supabase direct connection URL

Open the Supabase project dashboard.

Select Connect at the top of the project.

Find Direct connection and copy its URI. This is the connection type that supports logical replication.

Replace [YOUR-PASSWORD] in the copied URI with the database password. The result resembles:

postgresql://postgres:YOUR-PASSWORD@db.PROJECT-REF.supabase.co:5432/postgres

Paste the completed direct URL into PostgreSQL connection URL in Polygres.

Supabase direct connections commonly use IPv6. The Supabase IPv4 add-on

provides an IPv4 direct endpoint. During Polygres setup, choose the source

endpoint whose address family matches the regional egress addresses shown. See

Supabase database connections

and the

manual replication FAQ .

Configure Supabase Network Restrictions when enabled

When network restrictions are active:

Open Database Settings in Supabase.

Find Network Restrictions .

Copy the Polygres IPv4 egress address shown in the wizard and add /32 when Supabase expects CIDR notation.

Copy the Polygres IPv6 egress address and add /128 .

Keep every existing allowed CIDR. Supabase CLI updates replace the list unless you explicitly append.

Apply the restrictions before testing the connection in Polygres.

Supabase applies restrictions to direct and pooled database routes. Its HTTPS APIs are unrelated to this database allowlist. See Supabase Network Restrictions .

Confirm replication capacity

Polygres checks logical replication permissions and replication capacity during

source setup. Supabase recommends the postgres user for logical replication.

PostgreSQL 17 and newer can use a separately granted replication user under

Supabase’s documented rules. See

Set up manual replication .

Protect the source connection

Store the source URL or structured password in a secret manager or protected environment.

Use the hidden CLI prompt for interactive setup.

Use --connection-env or --password-env for automation.

Keep connection values out of screenshots, terminal history, source control, logs, and support messages.

When a source credential changes, rotate it with the database provider and contact Polygres support to update the synchronized connection.
