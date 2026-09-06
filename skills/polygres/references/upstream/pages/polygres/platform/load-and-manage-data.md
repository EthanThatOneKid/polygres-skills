source: https://docs.evokoa.com/polygres/platform/load-and-manage-data
title: Load and manage data | Polygres
source_hash: ff9e58fbae85b282fc2fc68dbdcd409677a990384881d1301ac159f618e66099
discovered_from: https://docs.evokoa.com/polygres

# Load and manage data | Polygres

Load and manage data

The database tools on this page apply only to managed database projects created with Host with Polygres . Synced projects do not provide the Tables mutation surface, SQL Editor, imports, migrations, psql , or other direct SQL access. Browse or change synchronized rows in the source PostgreSQL database instead.

Wait until the project is Ready before starting a write operation. If Settings > Runtime shows Read-only , browsing and read queries may still work, but imports, migrations, row edits, and schema changes can fail until the displayed cause is resolved.

You can load data and apply migrations from the dashboard or from the Polygres CLI . The CLI launch surface covers CSV import and SQL migrations. SQL file import, pg_dump restore, and import cancellation remain dashboard workflows.

Choose the right dashboard tool

Need Dashboard tool

Inspect rows or make a small targeted change Tables ( /{organization}/{project_id}/tables )

Explore data or run an ad hoc statement SQL Editor ( /{organization}/{project_id}/sql )

Upload CSV, SQL, or pg_dump data Import ( /{organization}/{project_id}/import )

Apply an ordered, repeatable schema change Migrations ( /{organization}/{project_id}/migrations )

From a terminal, use polygres import csv and polygres migrations apply . See CSV imports and Migrations .

Build a repeatable pipeline with an agent

Use the polygres-data-pipeline Agent Skill

when you want more than a one-time import. It can inspect a small sample from a

file, API, database, conversation export, or existing Polygres project and

recommend how to store and retrieve it.

You can start with a simple request:

Look at this data and set up the smallest useful Polygres pipeline.

The agent can reuse an existing table or propose a new schema, choose between

relational, text, pgContext, and graph retrieval, and prepare the source adapter,

privacy filter, writer, resume checkpoints, retrieval code, and tests needed for

the selected workflow. If semantic search is useful, it also explains the

local and hosted embedding options. Polygres stores and searches embeddings;

the pipeline is responsible for generating them.

Before uploading data or changing the project, the agent shows you one review

with the target project, data scope, schema and retrieval changes, external

services, costs, and destructive effects. After approval, it verifies a small

end-to-end example before continuing with a full backfill or ongoing capture.

Use the dashboard for quick, hands-on imports and edits. Use the pipeline skill

when the process needs to be repeatable, resumable, privacy-filtered, or

connected to an application or agent memory workflow.

For a single JSON record or runtime event, have the pipeline validate and use

the Runtime row-write workflow instead of

turning it into an import. Use imports for datasets and backfills. When an

import feeds a pgContext collection, reconcile the imported source rows before

serving semantic retrieval. Deleting a source row also requires cleanup of its

Context points and any other derived retrieval evidence.

Browse and edit tables

Open Tables and select a schema and table from the sidebar.

Browse rows

Filter the rows currently loaded in the browser and page through database results.

Choose a page size of 10 or 20 rows. The default is 20.

Inspect a cell in detail or copy a row as JSON.

For vector columns, use Load Full Vector Data when you specifically need the stored values. Vector cells are omitted initially to keep browsing responsive.

Loading a full vector value requires a primary key so the dashboard can identify the row again. For a composite primary key, the lookup uses every key column and its value from the loaded row.

Insert, update, or delete rows

Use the table actions to insert a row, edit supported cells, delete one row, or select and delete multiple rows. Updates and deletes require a primary key. When a table has no primary key, the dashboard cannot reliably target a row and blocks those actions.

For inserts, generated columns and IDENTITY ALWAYS columns are disabled and omitted so PostgreSQL computes them. An IDENTITY BY DEFAULT column can accept an explicit value; leave it blank to let PostgreSQL advance the identity sequence.

For production data, prefer a migration or reviewed SQL statement for broad changes. Inline editing is best for small corrections and development work.

Inspect and change the schema

Use the schema panel to review:

column names and data types,

primary-key and nullability indicators,

defaults,

foreign keys, and

enums.

The available schema actions can add, edit, or drop columns, change nullability, and manage foreign keys or enum definitions. Treat drop and type-changing actions as destructive. Confirm dependent application code and retrieval configurations before applying them.

Run SQL in the dashboard

Open SQL Editor , enter SQL, and select Run . You can also use Command+Enter on macOS or Control+Enter on Windows and Linux.

The editor runs with the project’s database role and remains subject to project state, tier limits, and SQL safety policy. Results show the returned columns and types, row count, elapsed time, and database notices when present.

The dashboard can run a single statement or a parameterless multi-statement

script. If a script contains several result-producing statements, the result

grid shows the last result set. If a script only changes schema or data, the

editor shows command success metadata instead of rows.

Scripts are not wrapped in an automatic transaction. Add explicit BEGIN and

COMMIT when all statements must succeed or fail together. Without an explicit

transaction, statements that completed before a later failure may remain applied.

Use the result actions to:

copy CSV, Markdown, or raw JSON,

download CSV or Markdown, and

load a recent query from browser-local history.

Query history is stored in the current browser, not as a shared organization audit log. Clear it before handing a shared workstation to another person.

When SQL fails, the error panel can include the message, SQLSTATE, detail, hint,

statement index, and request ID. Keep the request ID when escalating a platform

failure.

Import a CSV file

Open Import ( /{organization}/{project_id}/import ) and choose CSV .

Select the file. The dashboard previews sample rows and infers column names and data types. Columns in a newly created table default to nullable because a preview sample cannot prove that every row contains a value.

Choose Create new table , Append to existing , or Replace existing .

Select the target schema and table name, then review or adjust column mapping. Replace existing empties the selected table before loading the new rows and requires destructive confirmation.

Start the import and monitor it in Import history .

Review inferred types before importing. An identifier with leading zeros, a mixed-format date column, or a mostly empty field can be inferred differently from what the application expects. For append mode, each source column must map to a compatible destination column.

Import admission is limited by the project’s applied tier. Current tier records allow up to three queued or running jobs per project, although a deployment can expose a lower effective limit. Check GET /tiers and Import history before starting parallel work.

Import a SQL file

Choose SQL when the source is a plain .sql file.

Select the .sql file to upload.

Review its name, size, warning, and the tier upload limit.

Start the import.

Monitor the job until it reaches Succeeded or Failed .

Polygres checks SQL imports against the dashboard’s SQL policy before execution. When a statement is blocked, remove or replace the unsupported operation rather than repeatedly resubmitting the same file.

Restore a pg_dump file

Choose pg_dump for a PostgreSQL dump. The importer supports plain SQL dumps and custom-format dumps created with pg_dump -Fc .

Use a dump that is compatible with the target project and includes only the objects you intend to restore. Large restores are asynchronous; use Import history instead of keeping the upload dialog open as a progress indicator.

For a manual restore or a tool that needs a native database session, use the Direct connection .

Monitor and manage import jobs

Import history shows each job’s type, file, size, target, status, and last update. Statuses include:

Queued — accepted and waiting to start.

Running — actively importing or restoring.

Succeeded — completed successfully.

Failed — stopped with an error that needs review.

Cancelled — stopped before completion.

The page refreshes active jobs automatically. You can cancel a Queued or Running job. A finished job cannot be cancelled, and cancelling does not imply that every already-applied statement or row was rolled back.

When a job is Failed , open its details and record the stable error code,

optional variant, message, progress, job ID, and request ID. Use the code and

variant to identify the corrective action; do not build automation around the

message text. Correct the cause before starting another import. A local timeout

or closed browser does not mean the server-side job stopped, so refresh the

same job before submitting the file again.

Apply forward-only migrations

Use Migrations for versioned, repeatable schema changes.

Select New migration .

Give it a descriptive name of up to 120 characters.

Enter and review the SQL carefully, then save the migration as a draft.

Review its assigned version and checksum. The saved name and SQL are immutable; if either is wrong, create a new forward migration.

Apply the draft. Polygres runs it against your project’s PostgreSQL database.

Wait for Applied or inspect a Failed migration.

Migration statuses include Draft , Applying , Applied , and Failed . The dashboard refreshes while a migration is applying. SQL is checked when you save it and again before it runs. The saved checksum protects the migration definition from silent changes.

Each migration is atomic

Polygres runs the complete SQL body in one database transaction. If PostgreSQL

reports an error, changes made earlier in that migration are rolled back before

the migration is marked Failed .

Do not add top-level transaction commands to migration SQL. Polygres rejects

BEGIN , START TRANSACTION , COMMIT , END , ROLLBACK , ABORT , and

PREPARE TRANSACTION because they could end the managed transaction early.

The same words remain valid inside a function, procedure, or DO block when

they are part of a dollar-quoted body.

If another migration is running

Only one migration can run for a project at a time. If another migration is

already running, Polygres leaves your draft unchanged and tells you to try

again. Wait for the active migration to finish, then apply the same draft.

Migrations are forward-only. There is no rollback button. To undo a change, create and apply a new migration that safely reverses it.

Resolve common failure states

Failure What to check

Project not ready Wait for project, database, and pooler readiness before retrying.

Project is read-only Open Settings > Runtime , read the reason, and pause all write operations.

The active import limit is reached Wait for a queued or running job to finish, or cancel an eligible job.

Upload exceeds the tier limit Split or reduce the file, or use a tier with a sufficient import limit.

CSV preview or mapping is invalid Correct headers, inferred types, target table, and column mapping.

SQL import is blocked Remove unsupported statements and use dashboard-supported schema or data operations.

pg_dump restore fails Check dump format, target compatibility, referenced roles or extensions, and the job error.

Migration fails Read the stable error code, optional variant, message, and available database context. Polygres rolls back database changes from the failed migration. Saved migrations are immutable, so correct bad SQL in a new forward migration; retry the same migration only when the cause was transient.

Migration apply returns MIGRATION_LOCK_BUSY Another migration is already running. Your draft is unchanged. Wait for the active migration to finish, then retry the same draft.

Platform error has a request ID Keep the request ID and include it when contacting support.

After loading data, continue with Configure retrieval or the Polygres CLI retrieval setup commands.

For the shared error format and guidance on retries, request IDs, and safe

logging, see Handle API errors .
