source: https://docs.evokoa.com/polygres/platform/load-and-manage-data
title: Load and manage data | Polygres
source_hash: 4a33723a1d3dd5bf0e03de0e929803876a30e6a98fabd7615cfc7130f23acbcf
discovered_from: https://docs.evokoa.com/polygres

# Load and manage data | Polygres

Load and manage data

Wait until the project is Ready before starting a write operation. If Settings > Runtime shows Read-only , browsing and read queries may still work, but imports, migrations, row edits, and schema changes can fail until the displayed cause is resolved.

Choose the right dashboard tool

Need Dashboard tool

Inspect rows or make a small targeted change Tables ( /{organization}/{project_id}/tables )

Explore data or run an ad hoc statement SQL Editor ( /{organization}/{project_id}/sql )

Upload CSV, SQL, or pg_dump data Import ( /{organization}/{project_id}/import )

Apply an ordered, repeatable schema change Migrations ( /{organization}/{project_id}/migrations )

Browse and edit tables

Open Tables and select a schema and table from the sidebar.

Browse rows

Search within the displayed table and page through results.

Choose a page size of 50, 100, 250, or 500 rows.

Inspect a cell in detail or copy a row as JSON.

For vector columns, use Load Full Vector Data when you specifically need the stored values. Vector cells are omitted initially to keep browsing responsive.

Loading a full vector value requires a stable primary key so the dashboard can identify the row again.

Insert, update, or delete rows

Use the table actions to insert a row, edit supported cells, delete one row, or select and delete multiple rows. Updates and deletes require a primary key. When a table has no primary key, the dashboard cannot reliably target a row and blocks those actions.

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

Select the file. The dashboard previews sample rows and infers column names, data types, and nullability.

Choose whether to create a new table or append to an existing table.

Select the target schema and table name, then review or adjust column mapping.

Start the import and monitor it in Import history .

Review inferred types before importing. An identifier with leading zeros, a mixed-format date column, or a mostly empty field can be inferred differently from what the application expects. For append mode, each source column must map to a compatible destination column.

Only one import can be active for a project at a time.

Import a SQL file

Choose SQL when the source is a plain SQL file or SQL body.

Select or paste the SQL source.

Review the file and tier upload limit.

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

Apply forward-only migrations

Use Migrations for versioned, repeatable schema changes.

Select New migration .

Give it a descriptive name of up to 120 characters.

Enter the SQL and save the migration as a draft.

Review its version and checksum.

Apply the draft. Polygres runs migrations over the direct database connection.

Wait for Applied or inspect a Failed migration.

Migration statuses include Draft , Applying , Applied , and Failed . The dashboard refreshes while a migration is applying. SQL is policy-checked, and the saved checksum protects the migration definition from silent changes.

Migrations are forward-only. There is no rollback button. To undo a change, create and apply a new migration that safely reverses it.

Resolve common failure states

Failure What to check

Project not ready Wait for project, database, and pooler readiness before retrying.

Project is read-only Open Settings > Runtime , read the reason, and pause all write operations.

Another import is active Wait for it to finish or cancel it if the job is still queued or running.

Upload exceeds the tier limit Split or reduce the file, or use a tier with a sufficient import limit.

CSV preview or mapping is invalid Correct headers, inferred types, target table, and column mapping.

SQL import is blocked Remove unsupported statements and use dashboard-supported schema or data operations.

pg_dump restore fails Check dump format, target compatibility, referenced roles or extensions, and the job error.

Migration fails Read the database error, correct the problem in a new or still-editable draft, and do not assume a rollback occurred.

Platform error has a request ID Keep the request ID and include it when contacting support.

After loading data, continue with Configure retrieval .
