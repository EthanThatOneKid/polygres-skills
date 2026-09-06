source: https://docs.evokoa.com/polygres/agent-skills
title: Polygres Agent Skills | Polygres
source_hash: 1646f336f422ead5bf9eec6aa3e95726d7046d6f016ae8d3f7f68ac5bc84cace
discovered_from: https://docs.evokoa.com/polygres

# Polygres Agent Skills | Polygres

Polygres Agent Skills

Polygres Agent Skills help coding agents understand your data, use the Polygres

MCP connection, recommend a useful setup, and build or operate it with you. The

plugin includes five skills:

polygres-data-pipeline uses available MCP tools to turn files, databases, APIs, conversations, or

existing Polygres data into a managed PostgreSQL sync or working custom

ingestion and retrieval pipeline;

polygres-cli uses MCP for compatible interactive operations and the CLI for signing in, creating standard or synchronized

projects, selecting projects, importing standard-project data, applying

migrations, managing keys, and configuring retrieval;

polygres-sdk uses MCP for interactive grounded answers and helps you add

pgContext, graph, vector, text, and hybrid retrieval to a Python application;

polygres-retrieval-design uses read-only MCP evidence to compare retrieval

options and prepare a project design;

polygres-troubleshooting investigates MCP connections, projects, imports,

retrieval, and Context operations using read-only checks.

Install the CLI or SDK when your workflow uses it, then add the skill repository:

Install the current CLI and SDK, then add Polygres Agent Skills 0.6.0 :

pipx install "polygres-cli==0.4.1"

python -m pip install "polygres-sdk==0.4.1"

npx skills add Evokoa/polygres-skills

Agent Skills 0.6.0 , MCP catalog 1.0 , CLI 0.4.1 , and SDK 0.4.1 form the current coordinated

release set.

The public skill source is

Evokoa/polygres-skills . Review the

repository before installation if your organization requires third-party code

approval.

Choose an installation method

Compatible Agent Skills installers

Install only the operational skill into the current project:

npx skills add Evokoa/polygres-skills --skill polygres-cli

Install only the guided pipeline skill:

npx skills add Evokoa/polygres-skills --skill polygres-data-pipeline

Install only the application-development skill:

npx skills add Evokoa/polygres-skills --skill polygres-sdk

Install the advisory design or diagnostic skill:

npx skills add Evokoa/polygres-skills --skill polygres-retrieval-design

npx skills add Evokoa/polygres-skills --skill polygres-troubleshooting

Install globally for Codex and Claude Code:

npx skills add Evokoa/polygres-skills \

--global \

--agent codex \

--agent claude-code \

--yes

Project scope is the default. Use --global when the skill should be available

across all of your repositories.

Codex plugin marketplace

Add the marketplace source:

codex plugin marketplace add Evokoa/polygres-skills

Start Codex, open /plugins , select the Polygres marketplace, and install the

Polygres plugin. The plugin adds the production MCP connection and the five

skills. Start a new task so Codex loads both.

The plugin MCP address covers All accessible projects . For a focused

one-project connection, open that project’s Connect → MCP page and use its

generated setup instructions.

Claude Code plugin marketplace

Inside Claude Code, run:

/plugin marketplace add Evokoa/polygres-skills

/plugin install polygres@polygres

/reload-plugins

Compatible agents can activate the appropriate skill automatically from the

request. Invoke a skill explicitly when you need to select the CLI or SDK

workflow yourself:

/polygres:polygres-data-pipeline

/polygres:polygres-cli

/polygres:polygres-sdk

/polygres:polygres-retrieval-design

/polygres:polygres-troubleshooting

Ask in your own words

Describe the result you want in your own words. The agent can select the skill,

schema, and retrieval method, inspect the relevant parts of your

workspace and selected project, recommend an approach, and ask for approval

before it uploads data or changes a project.

Example prompts:

Use Polygres MCP to inspect this project and recommend the next useful setup step.

Use Polygres MCP to answer this question from my support collection and cite the returned records.

Look at my data and use $polygres-data-pipeline to set up a Polygres data pipeline.

Look at this project and tell me what I could do with Polygres.

Turn these support conversations into searchable agent memory. Keep customer

secrets out and show me what will be stored before uploading anything.

Build a repeatable pipeline from this API. I need exact search for product

codes and semantic search for customer questions.

Sync my Supabase, Neon, or PostgreSQL database into Polygres and configure

retrieval over the selected tables.

Log me into Polygres and help me select the correct project.

Import customers.json into public.customers. Inspect it first, explain any

conversion choices, and ask before changing data.

Review this SQL migration and ask before applying it to my selected project.

Configure a cosine pgContext collection for documents.embedding with 1536

dimensions, preflight the source, and verify readiness.

Set up a pgContext collection over public.documents. Preflight it first,

explain ownership and schema changes, and ask before mutating the project.

Use the Polygres SDK to find semantically similar documents, expand their

citations, and build deduplicated RAG context with source provenance.

Use project.context.joint() to combine semantic, lexical, and graph evidence

while preserving typed provenance and request IDs.

Design a reviewable retrieval plan for this schema using read-only project

inspection. Compare relational, graph, pgvector, text, hybrid, and pgContext

approaches.

Diagnose why this pgContext collection is blocked from public read-only

evidence. Preserve collection, operation, and request IDs and recommend a safe

corrective action.

The installed polygres --help output remains authoritative if the local CLI

version differs from the skill examples.

Set up a data pipeline from one prompt

You can start with a broad request such as “Look at my data and set up

Polygres.” If you are still exploring, ask “What could I do with Polygres?”

The agent will inspect a small, read-only sample of the data and the relevant

parts of your project, then suggest the outcome most likely to help. This

recommendation phase stays read-only.

Once you ask it to proceed, the agent works through the setup with you:

It checks the source shape, existing schema, ownership fields, and current

retrieval setup. Inspection stays limited to what is needed for the task.

It recommends the smallest useful design. That might reuse an existing

table, choose managed PostgreSQL sync, add a purpose-built table to a

standard project, start with text search, add pgContext for semantic recall,

or use graph retrieval when real relationships make the results better.

It prepares runnable, source-specific code for the parts you need, such as a

source adapter, privacy filter, safe writer, resume checkpoints, retrieval

function, and focused tests.

Before the first upload or project change, it shows one review covering the

target project, data being stored, schema changes, retrieval setup, external

services, costs, and anything destructive or difficult to reverse.

After you approve that review, it applies the covered changes and tests a

small end-to-end example before continuing with a larger import or ongoing

integration.

The result is more than a schema suggestion. You receive the local code and

operator instructions needed to run the selected workflow, plus a clear report

of what was verified. The final report labels any remaining setup as partial or

blocked and describes the next step needed to complete it.

Synchronized PostgreSQL projects

For an eligible Supabase, Neon, or PostgreSQL source, the pipeline skill can

create a synchronized project and configure retrieval over selected tables.

The source remains the system of record, while Polygres maintains a current

copy for retrieval.

The skill can use either supported setup path:

the dashboard for a guided visual workflow; or

polygres projects create sync for an interactive or automated CLI workflow.

For CLI automation, the skill keeps the connection value in an environment

variable and passes its name through --connection-env . It can select explicit

public tables, use a reviewed selection file, or select all eligible tables.

After creation, the dashboard provides synchronized-table configuration and

the lifecycle actions available for the project’s current state.

For a synced project, the skills route application writes, schema changes, and

embedding generation to the source database. They use Polygres Runtime APIs for

graph, text, vector, hybrid, AI Context, catalog, and readiness workflows.

Route each write to the right interface

For a standard project, the skill chooses the write surface from the workload:

Workload Recommended interface

One JSON record or runtime event for an eligible existing table Validate, then use the Runtime rows surface.

Dataset or bounded backfill Use the reviewed import workflow. If it feeds a pgContext collection, reconcile the imported source rows before declaring retrieval ready.

Source-row deletion Use an approved deletion path, then remove or invalidate the matching Context points and other derived retrieval evidence.

For a Context-backed row write, the skill preserves the exact request and

idempotency key so it can safely resume the Context step during the 24-hour

replay window. For a row-only write, the skill checks a stable business key

before deciding whether another write is necessary.

Embeddings and semantic search

When semantic search or memory would help, the agent checks your existing

embedding setup first. It can recommend a compatible local model and a hosted

alternative, including the privacy, hardware, and cost tradeoffs that matter

for your source. You choose between the reviewed options before data is sent to

an external model.

Polygres stores and searches embeddings. The pipeline creates embeddings before

writing source records and uses the same compatible model for search queries.

The agent can also start with relational or text retrieval and add semantic

search when embeddings are ready.

Capture conversations and build agent memory

The pipeline skill can turn conversations or agent activity into

pgContext-backed memory. It can add capture, recall, or both, depending on what

you want the agent to remember. Captured records keep stable source IDs and

provenance so updates, retries, and deletions can be handled safely.

Privacy filters run before content is stored or embedded. By default, they keep

system instructions, credentials, retrieved context, attachments, and tool

output outside captured memory. You can explicitly select additional content.

Your application’s authorization rules remain the source of truth, while

search filters narrow eligible results.

If you approve an agent integration, the skill can append clearly marked

capture and recall guidance to that agent’s existing instruction file. For

reliable ongoing capture, it also needs a tested

application hook, wrapper, queue, or worker. The final report tells you whether

capture is automatic, retryable, best effort, or manual.

Credentials stay local

Generated setup files use an empty .env.example and an ignored .env file.

Add values directly to .env on your computer. Credential checks report a

simple readiness status for each required value while keeping the value private.

Build with the Python SDK

Use polygres-sdk for application retrieval and explicit backend-owned

pgContext automation. Control-plane project administration remains a dashboard

or CLI workflow. The skill distinguishes the per-project Runtime API URL from

the control-plane and Postgres URLs, keeps the API key in server-side

environment configuration, and uses passwordless connection metadata.

The SDK skill covers:

pgContext capabilities, collection setup, point synchronization, durable

operations, filters, dense and grouped retrieval, text and graph composition,

recall checks, rank fusion, and coupled Joint retrieval;

graph.expand , graph.neighborhood , graph.related , graph.path , and

graph.connection with real row IDs and bounded traversal;

vector search and row similarity with dimension and threshold validation;

TSVector and fuzzy text retrieval, including empty and ambiguous input;

graph-first, vector-first, and joint hybrid retrieval;

cursor and automatic pagination, typed results, request IDs, and SDK

exceptions;

anchor-first and semantic-first RAG with provenance, deduplication, and

application token budgets.

Filters narrow retrieval while the application remains responsible for

authorization. pgContext collections and pgvector configurations are distinct

resources. Use the CLI skill for interactive, human-reviewed setup,

reconciliation, and rebuilds. Use the SDK skill for explicit backend-owned

pgContext automation and application retrieval.

Design retrieval before implementation

Use polygres-retrieval-design when strategy or data modeling is unresolved.

It maps stable row IDs, relationships, graph bounds, embedding dimensions,

text configuration, hybrid stages, authorization, provenance, deduplication,

token budgets, readiness, and validation into a reviewable plan. After user

approval, it delegates project setup to polygres-cli and application code to

polygres-sdk . Its own work stays read-only.

Diagnose with public evidence

Use polygres-troubleshooting for authentication, project context,

provisioning, database, pooler, Runtime API, import, migration, retrieval,

pagination, timeout, and partial-failure symptoms. It uses installed CLI help,

public status commands, SDK readiness and exception types, and retained

request or job IDs. Diagnosis stays on documented public interfaces and remains

read-only until you approve a separate repair workflow.

Import CSV, TSV, JSON, and JSONL

The CLI imports CSV. For TSV, JSON arrays, and JSONL or NDJSON, the skill can

run its bundled local converter to create a reviewed CSV before invoking

polygres import csv .

The converter:

runs locally;

keeps the original source file on your computer;

reports row count, columns, key mappings, nesting, and conversion warnings;

requires an explicit choice before flattening or stringifying nested JSON;

highlights conversions where null and empty-string values would merge;

writes the converted CSV atomically and reports source and output hashes.

For Excel, Parquet, Avro, ORC, XML, YAML, SQL dumps, and pg_dump archives,

export the source to CSV or JSONL before import.

Update

Update a skill installed with the generic installer:

npx skills update polygres-data-pipeline

npx skills update polygres-cli

npx skills update polygres-sdk

npx skills update polygres-retrieval-design

npx skills update polygres-troubleshooting

Refresh the Codex marketplace:

codex plugin marketplace upgrade polygres

Then open /plugins to update or reinstall the Polygres plugin if prompted.

Update the Claude Code marketplace and plugin:

/plugin marketplace update polygres

/plugin update polygres@polygres

/reload-plugins

Uninstall

Remove a global generic installation:

npx skills remove --global polygres-data-pipeline

npx skills remove --global polygres-cli

npx skills remove --global polygres-sdk

npx skills remove --global polygres-retrieval-design

npx skills remove --global polygres-troubleshooting

For Codex, uninstall Polygres through /plugins . Remove the marketplace source

only when no other plugin from it is needed:

codex plugin marketplace remove polygres

For Claude Code:

/plugin uninstall polygres@polygres

/plugin marketplace remove polygres

/reload-plugins

Removing a Claude marketplace also uninstalls plugins installed from it.

Security boundaries

The skill uses the public polygres CLI and documented Polygres interfaces.

Login uses browser approval, keeping your username, password, and

POLYGRES_ACCESS_TOKEN within the authentication flow.

Database passwords stay out of command arguments. For a managed database

project, let psql prompt interactively. Synced-project data operations use

the Runtime API and source database.

Runtime API-key secrets are displayed once. Run key creation in your own

terminal when you want the secret to stay outside the agent transcript.

Store local runtime credentials in an ignored .env so chat, source files,

commands, and generated plans stay free of credentials.

Local embedding installation, model download, or service startup requires

explicit approval after the device feasibility check.

Replacement imports, migrations, revocations, deletes, and schema mutations

require explicit approval.

Continue with the Polygres CLI guide for command behavior and exit

codes, or connect your application after the project is

ready.
