source: https://docs.evokoa.com/polygres/cli/projects
title: CLI projects | Polygres
source_hash: cc450404500ae6d7ca9314434a3e6ad966e1fda7d503a1e43b0aa6df54616341
discovered_from: https://docs.evokoa.com/polygres

# CLI projects | Polygres

Projects

The CLI supports standard projects hosted by Polygres and synced projects

connected to an existing PostgreSQL database.

List and select projects

polygres projects list

polygres projects use "Support Search"

polygres projects status

Project names are exact and case-sensitive. Use the project ID when multiple

projects have the same name.

Project selection is explicit. After creating a project, run projects use to

make it the default for later commands. Use the global --project option to

target one command while keeping the current selection.

polygres projects use "Support Search"

polygres --project "Support Search" projects status

polygres config path

Create a standard project

Use a standard project when Polygres should host the primary PostgreSQL

database:

polygres projects create standard "Support Search"

Creation waits up to 600 seconds for readiness. You can adjust that behavior:

polygres projects create standard "Support Search" --timeout 900

polygres projects create standard "Support Search" --no-wait

Create a synced PostgreSQL project

Use a synced project when an existing PostgreSQL database remains the source

of truth.

The interactive workflow securely prompts for the PostgreSQL connection URL,

checks the source, lists eligible public tables, and lets you choose what to

synchronize:

polygres projects create sync "Support Search"

For automation, place the connection URL in an environment variable and pass

its name:

export SOURCE_DATABASE_URL = "postgresql://..."

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--all-eligible \

--yes

--connection-env accepts the name of the environment variable. The

connection URL remains in your environment.

You can also provide structured connection details:

export SOURCE_DATABASE_PASSWORD = "..."

polygres projects create sync "Support Search" \

--host db.example.com \

--port 5432 \

--database app \

--username polygres_sync \

--password-env SOURCE_DATABASE_PASSWORD \

--table public.customers \

--table public.orders \

--yes

Port 5432 is used when --port is omitted.

Select source tables

Choose one table-selection method.

Select specific tables from public or custom application schemas:

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--table public.customers \

--table app.orders \

--yes

Select every eligible table in the public schema:

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--all-eligible \

--yes

Use --table schema.table or a selection file to select tables from custom

schemas. Polygres keeps each table’s source schema and name. See

Choose tables for supported

schemas and source requirements.

Use a selection file

Save your table choices in sync-tables.json , then pass the file with --file :

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--file sync-tables.json \

--yes

The JSON file can contain a table array directly:

[

{

"schema_name" : "public" ,

"table_name" : "customers"

},

{

"schema_name" : "public" ,

"table_name" : "orders" ,

"included_columns" : [ "id" , "customer_id" , "status" , "created_at" ]

}

]

It can also use a top-level tables property:

{

"tables" : [

{

"schema_name" : "public" ,

"table_name" : "customers"

}

]

}

Choose a primary key in a selection file

Use destination_key_index_name to choose the primary key for a copied table.

Set it to an eligible index name returned by the source checks. The index’s

columns become the primary key in Polygres, while your source table keeps its

existing keys and replication settings.

For example, if the source checks list orders_pkey as an eligible key for

app.orders , save this selection in sync-tables.json :

{

"tables" : [

{

"schema_name" : "app" ,

"table_name" : "orders" ,

"destination_key_index_name" : "orders_pkey"

}

]

}

Run the command above with --file sync-tables.json . When a table offers

several eligible keys, the CLI asks you to make this choice in a selection

file. With one eligible key, the choice is automatic.

Each table entry supports these fields:

Field What to provide

schema_name The source schema, such as public or app .

table_name The source table name.

destination_key_index_name An eligible index whose columns will form the copied table’s primary key. Choose one explicitly when several keys are available.

included_columns The columns to synchronize when the source checks offer a partial selection. Include every column used by the source’s replication key and your chosen Polygres primary key.

sync_key_index_name Optional: the source’s existing replication-key index, exactly as returned by the source checks. This field refers to the source key; use destination_key_index_name for your Polygres primary-key choice.

Control creation behavior

Use these options as needed:

Option Purpose

--yes Confirms the reviewed source and table selection for automation.

--no-wait Returns after project creation has been submitted.

--timeout <seconds> Sets the maximum time for the creation workflow.

--idempotency-key <key> Gives a repeatable automation workflow a stable creation key.

Keep the idempotency key with your automation logs. Reuse the same key when

resuming the same creation attempt.

Work with a synced project

After synchronization reaches Streaming , use Polygres graph, text, vector,

hybrid, and AI Context retrieval over the synchronized tables.

Make application data changes in the source PostgreSQL database. Polygres

continuously brings those changes into the synced project.

Use the dashboard to update the selected tables and to access the sync actions

currently available for the project.
