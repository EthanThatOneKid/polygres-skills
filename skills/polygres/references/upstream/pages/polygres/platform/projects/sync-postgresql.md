source: https://docs.evokoa.com/polygres/platform/projects/sync-postgresql
title: Create a Synced PostgreSQL Project | Polygres
source_hash: af0e993923abcd2a751c043568223d6f88d8d738aafaf3f6a55c61b3ca34713a
discovered_from: https://docs.evokoa.com/polygres

# Create a Synced PostgreSQL Project | Polygres

Create a Synced PostgreSQL Project

A synced project copies selected tables from an existing PostgreSQL database

into Polygres. Polygres takes an initial snapshot and then applies ongoing

changes through PostgreSQL logical replication. Your source database remains

the system of record.

Use this project type when you already run PostgreSQL and want Polygres

retrieval features over that data while application writes continue through

the source.

Understand the operating model

A synced project keeps an existing PostgreSQL database as the source of truth

and continuously copies selected public schema tables into Polygres.

Make row changes, schema changes, and embedding updates in the source database.

Use Polygres for graph, text, vector, hybrid, and AI Context retrieval over synchronized data.

Select tables with a stable primary key or eligible unique key.

Update the selected tables from Configure sync after the project reaches Streaming .

Use standard projects for Polygres-hosted PostgreSQL connections, SQL tools, imports, and migrations.

Check the source requirements

Prepare a PostgreSQL source that:

runs PostgreSQL 14 through 18;

provides a direct PostgreSQL connection, typically on port 5432 ;

supports encrypted connections with a trusted hostname certificate;

has logical replication enabled with available replication capacity;

gives the selected role access to connect, inspect the catalog, and read the selected public tables; and

gives every selected table a stable primary key or eligible unique key.

When the source uses a network allowlist, add the regional egress addresses

shown by Polygres. Choose a source endpoint whose address family matches the

egress addresses displayed during setup.

For provider-specific setup, see the

PostgreSQL sync setup guides .

Create the project

Dashboard CLI

Dashboard

Open New project from the organization that should own the project.

Choose Supabase , Neon , PlanetScale , or Postgres Database .

Add the displayed regional egress addresses to the source allowlist when required.

Enter the complete PostgreSQL connection URL or choose Use structured connection fields .

Continue to the source checks.

Select eligible tables from the public schema.

Review the selection and choose Create and sync .

CLI

Start an interactive setup:

polygres projects create sync "Support Search"

Or use an environment variable for automation:

export SOURCE_DATABASE_URL = "postgresql://..."

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--all-eligible \

--yes

Use repeatable --table public.TABLE_NAME options when you want an

explicit selection.

Store the source connection URL in a protected environment or secret manager.

For CLI automation, pass the environment-variable name through

--connection-env .

Understand the source checks

Polygres checks the source before table selection:

Check What Polygres verifies

Network The source hostname and port are reachable from the selected region.

Authentication The submitted username and password open the PostgreSQL connection.

TLS The source presents a trusted certificate for its hostname.

Server version The PostgreSQL major version is qualified for synchronization.

Logical replication The source can provide ongoing logical changes.

Replication capacity The source has capacity for this synchronized project.

Catalog access Polygres can inspect tables, columns, keys, constraints, and estimated size.

Choose tables

Polygres shows the synchronization eligibility of each discovered public

schema table.

A table is ready for selection when it has:

a stable primary key or eligible unique key;

supported columns for the selected synchronization scope;

a regular persistent table structure; and

source-role access that provides a consistent view of its rows.

For a table with eligible and ineligible columns, Polygres can offer an

included-column selection when the complete synchronization key remains

available.

Review:

the selected synchronization key;

included columns;

estimated rows and storage;

related tables used by graph relationships; and

the storage available for the organization.

Select both sides of a foreign-key relationship when you want pgGraph to use

that relationship.

Follow synchronization progress

A synced project moves through these synchronization states:

State What it means

Initializing Polygres is preparing the synchronized project.

Snapshotting The initial selected rows are being copied.

Catching up Changes made during the snapshot are being applied.

Streaming The initial copy is complete and ongoing changes are flowing.

Resyncing A selected table is receiving a refreshed copy.

Paused Synchronization is waiting for the action shown in the project overview.

Failed Synchronization needs attention using the guidance shown in the project overview.

The project overview shows table progress, freshness, storage, and the actions

currently available. Retrieval becomes available as the required synchronized

tables and retrieval configuration reach readiness.

Update selected tables

After the project reaches Ready and synchronization reaches Streaming :

Open the project and select Configure sync .

Refresh the source inspection.

Review table eligibility, synchronization keys, included-column options, and storage estimates.

Select the tables to keep synchronized.

Save the configuration.

Newly selected and materially changed tables move through Resyncing before

returning to Streaming . Tables removed from the selection finish their

synchronization lifecycle.

Review graph, text, vector, and AI Context configurations that use a changed

table, column, relationship, key, or embedding.

Operate synchronization

The project overview presents actions that match the current synchronization

state.

Pause holds ongoing synchronization while preserving the project’s current synchronized data.

Resume continues synchronization from a paused state.

Retry starts another attempt after the displayed source or synchronization issue has been resolved.

Configure sync updates the selected source tables.

Use the status message beside each action to confirm the recommended next step.

Resolve source-check results

Result Recommended action

Network connection Confirm the direct hostname, port, address family, and source allowlist.

Authentication Verify the database name, username, password, and connection URL encoding.

TLS verification Use the provider’s direct endpoint and its hostname-verified certificate.

PostgreSQL version Use a PostgreSQL 14 through 18 source.

Logical replication Enable logical replication and make replication capacity available.

Catalog access Grant the selected role access to inspect and read the chosen public tables.

Table eligibility Add or select a stable key and use the eligible columns shown by Polygres.

Storage estimate Select a smaller table set or choose a tier with suitable capacity.

After updating the source, run the check again and continue with table

selection.

See the

PostgreSQL sync setup guides for

standard PostgreSQL, Neon, Supabase, and PlanetScale instructions.
