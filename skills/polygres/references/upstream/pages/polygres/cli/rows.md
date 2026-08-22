source: https://docs.evokoa.com/polygres/cli/rows
title: Write rows | Polygres
source_hash: 546ae1a3ab79d37a2abd00035b7b91a7daa1645b9d2e7b788e809adeb09181dd
discovered_from: https://docs.evokoa.com/polygres

# Write rows | Polygres

Write rows from the CLI

Use polygres rows when you want to write one JSON object to a table from a

script or terminal. You can check a row first, choose how unique conflicts are

handled, return selected columns, and keep a pgContext collection in sync as

part of the same workflow.

This command is designed for one record at a time. For CSV files, backfills, or

other bulk work, use the import workflow or a

native Postgres client.

Install or upgrade

Row commands require CLI 0.3.0 or newer:

pipx install "polygres-cli==0.4.0" --force

polygres --version

Sign in and select the project before writing:

polygres login

polygres projects use "Support Search"

Prepare one JSON object

Save the row as a UTF-8 JSON object. For example, memory.json might contain:

{

"id" : "memory_123" ,

"content" : "The user prefers concise answers." ,

"status" : "active"

}

The file must contain one non-empty object. Column names must be portable

PostgreSQL identifiers. The CLI does not accept a JSON array, JSONL, or several

rows in one request.

Use --file - to read the object from standard input once:

printf '%s' '{"id":"memory_123","content":"Keep answers concise."}' | \

polygres rows insert --table memories --file -

Check the row without writing it

Validation checks the table, columns, values, conflict target, and requested

Context collection without changing your data:

polygres rows validate \

--schema public \

--table memories \

--file memory.json \

--returning id

You can also validate an upsert or ignore request before running it:

polygres rows validate \

--table memories \

--file memory.json \

--mode upsert \

--conflict-column id \

--update-column content \

--update-column status

Validation is useful during setup, but it is not a reservation. The table can

still change between validation and the write.

Insert a new row

polygres rows insert \

--table memories \

--file memory.json \

--returning id

The default schema is public . Repeat --returning when you need more than

one value. Put the global --json option before rows to receive the returned

values as structured output:

polygres --json rows insert \

--table memories \

--file memory.json \

--returning id \

--returning created_at

With --json , returned json and jsonb columns remain structured JSON in

the returned object. They are not JSON-encoded strings.

If a selected column has a database default, leave it out of the JSON object so

Postgres can apply that default.

Insert or update on a unique conflict

Use upsert when a primary key or unique constraint identifies the same

logical record:

polygres rows upsert \

--table memories \

--file memory.json \

--conflict-column id \

--update-column content \

--update-column status \

--returning id

Every --conflict-column must match a real primary key or unique constraint.

For a compound constraint, repeat the option for each column. When you omit

--update-column , the write updates the supplied non-conflict columns. When you

provide it, only those named columns are updated.

Ignore an existing row

Use ignore when an existing unique key should be treated as a successful

no-op:

polygres rows ignore \

--table memories \

--file memory.json \

--conflict-column id \

--returning id

ignore requires at least one conflict column and does not accept update

columns.

Keep pgContext in sync

A normal row command changes only the source table. Add Context reconciliation

when the row belongs to a pgContext collection and its point mapping should be

created or refreshed too.

If exactly one ready collection uses the table, let Polygres select it:

polygres rows upsert \

--table memories \

--file memory.json \

--conflict-column id \

--reconcile-context \

--idempotency-key memory-123-v1

If several collections use the table, select one by UUID:

polygres rows upsert \

--table memories \

--file memory.json \

--conflict-column id \

--context-collection 2e172638-bd77-4a2c-bc42-406f4f2938d7 \

--idempotency-key memory-123-v1

Choose a stable key that identifies this exact intended write. The CLI creates

a key when you omit it, but supplying your own key makes recovery easier across

processes and machines. Reusing a key with different row data or options is

rejected.

The CLI waits for Context reconciliation by default, for up to 1,800 seconds.

Change the limit with --timeout , or return as soon as the durable Context

operation starts with --no-wait :

polygres --json rows upsert \

--table memories \

--file memory.json \

--conflict-column id \

--reconcile-context \

--idempotency-key memory-123-v1 \

--no-wait

A pending response includes a Context operation ID. Save it with the

idempotency key, then check it later:

polygres context operations get < operation-uui d >

polygres context operations wait < operation-uui d >

Do not follow a Context-backed row write with context points upsert . The row

command has already completed or started the required reconciliation. See

AI Search with pgContext for point maintenance

after writes made outside this row workflow.

Recover safely after an uncertain result

Row writes are never retried automatically. If the connection drops or the

server cannot confirm whether the database committed, the CLI exits with code

8 and reports that the outcome is unknown.

For a Context-backed write:

Save the displayed idempotency key, request ID, and Context operation ID if

one is present.

Inspect the operation with polygres context operations get when an

operation ID is available.

To resume, run the exact same row command with the same JSON content,

options, and idempotency key.

For a row-only write, --idempotency-key is not accepted. Check the table using

the record’s primary key or another unique identifier before deciding whether

to run the command again. A blind retry could create a duplicate row.

If the result says partial_failed , the source row committed but Context

reconciliation did not finish. Use the returned operation ID to inspect the

failure. Retry a failed Context operation only when its error says it is

retryable, or resume the exact row request with its original idempotency key.

For stable exit codes and machine-readable error handling, see

Automation and exit codes . For API error

meanings, see the error catalog .
