source: https://docs.evokoa.com/polygres/platform/projects/postgresql-source-setup
title: PostgreSQL Sync Setup Guides | Polygres
source_hash: 7784970d50602d98e3bac729b18f45be8faca8b657c18edb6d31ddeee8ca32d4
discovered_from: https://docs.evokoa.com/polygres

# PostgreSQL Sync Setup Guides | Polygres

PostgreSQL Sync Setup Guides

Choose your source below for the exact setup steps and connection details to copy into Polygres. Complete the relevant guide before opening the synced-project wizard .

Your source Follow this guide

Self-hosted PostgreSQL or another managed provider Standard PostgreSQL

Neon Neon

Supabase Supabase

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
