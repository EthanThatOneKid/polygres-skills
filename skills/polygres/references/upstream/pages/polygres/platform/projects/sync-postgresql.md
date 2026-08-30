source: https://docs.evokoa.com/polygres/platform/projects/sync-postgresql
title: Create a Synced PostgreSQL Project | Polygres
source_hash: 2faa674b1c83f25c97c3618714a10d6a1547865695a6462e09fa3a9c9311ebef
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

A synchronized project can use the Free Nano workflow or, when offered for your

organization, the Paid Basic workflow. Polygres activates Basic automatically

after it establishes the initial synchronization. See Free and Paid

projects for availability, pricing,

capacity, and payment details.

Understand the operating model

A synced project keeps an existing PostgreSQL database as the source of truth

and continuously copies selected public schema tables into Polygres.

Make row changes, schema changes, and embedding updates in the source database.

Use Polygres for graph, text, vector, hybrid, and AI Context retrieval over synchronized data.

Select tables with a stable primary key or eligible unique key.

Update the selected tables from Configure sync after the project reaches Streaming .

After Synced Basic is ready, the overview shows stable hostnames for its

isolated Polygres database. Keep making changes to synchronized rows and

schemas in the source database.

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

Choose Free or, when offered for your organization, Paid .

Choose Supabase , Neon , PlanetScale , or Postgres Database .

Add the displayed regional egress addresses to the source allowlist when required.

Enter the complete PostgreSQL connection URL or choose Use structured connection fields .

Continue to the source checks and select eligible tables from the public schema.

For Paid, review estimated Context usage, configure capacity, select Review payment , and confirm with Create Project . For Free, select Create and sync .

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

explicit selection. The CLI creates a Free Nano synchronized project and

uses the organization’s one Free project slot. Use the dashboard for a

Paid synchronized project.

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

estimated Context points from selected embedding tables when creating a Paid project;

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

Understand Paid synchronized creation

An organization owner or admin with an eligible subscription can create a Paid

synchronized project. The payment review shows the estimated first-cycle total,

the available-credit portion, the payment-method portion, and the maximum

charge. Creation works with any available credit balance, including zero.

While setup is in progress, Polygres temporarily sets aside only the

available-credit portion shown in the review. The hold remains part of the

organization balance and is reserved for this project until activation finishes

or setup stops.

Polygres establishes the synchronization, confirms that source changes are

flowing, and completes the move to Basic automatically. Near completion,

Polygres may pause writes for up to 30 minutes while it applies the latest

source changes. Reads may also pause briefly.

The first charge is collected when Basic is ready and is prorated through the

organization’s next subscription billing date. Polygres uses available credits

first and charges the remainder through Stripe. The final amount cannot exceed

the displayed maximum when capacity and pricing have not changed. The temporary

credit hold is removed when the project activates or if setup cannot be

completed.

Continue using the external PostgreSQL database for application SQL and writes.

After Synced Basic is ready, the project overview shows stable pooled and direct

hostnames for the isolated Polygres database. The connection details shown

there are limited to those hostnames. Keep the source database authoritative

for synchronized rows and schemas.

Upgrade an existing synced Nano project

Open the project’s Upgrade page, choose Basic capacity, and review the

maximum first-cycle charge. Polygres prepares a fresh Basic copy while the Nano

project remains active. Near the final switch, writes may pause for up to 30

minutes and reads may be briefly unavailable.

The charge is collected only after Basic activates. If the dashboard says the

upgrade needs attention, follow the saved progress and contact support with the

displayed error code before starting another upgrade.

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
