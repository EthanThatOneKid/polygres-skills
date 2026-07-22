source: https://docs.evokoa.com/polygres/agent-skills
title: Polygres Agent Skills | Polygres
source_hash: b85cdc77ef05357bd263c70210136eeb42c93b18d8221fa07bd4497a69a4fe5c
discovered_from: https://docs.evokoa.com/polygres

# Polygres Agent Skills | Polygres

Polygres Agent Skills

The Polygres plugin includes four independently triggered Agent Skills:

polygres-cli operates Polygres through the public CLI, including login,

project selection, imports, migrations, keys, retrieval setup, and recovery;

polygres-sdk builds Python application retrieval with graph, vector, text,

hybrid, pagination, typed models, and grounded RAG workflows;

polygres-retrieval-design produces a reviewable retrieval plan without

changing a project;

polygres-troubleshooting diagnoses failures from public read-only CLI and

SDK evidence.

The skills do not include the Python packages. Install the component required

by the task, then install the skill repository:

pipx install "polygres-cli==0.1.2"

python -m pip install "polygres-sdk==0.1.0"

npx skills add Evokoa/polygres-skills

The public skill source is

Evokoa/polygres-skills . Review the

repository before installation if your organization requires third-party code

approval.

Choose an installation method

Compatible Agent Skills installers

Install only the operational skill into the current project:

npx skills add Evokoa/polygres-skills --skill polygres-cli

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

Polygres plugin. Adding a marketplace makes its catalog available but does not

install the plugin by itself. Start a new task after installation.

Claude Code plugin marketplace

Inside Claude Code, run:

/plugin marketplace add Evokoa/polygres-skills

/plugin install polygres@polygres

/reload-plugins

Compatible agents can activate the appropriate skill automatically from the

request. Invoke a skill explicitly when you need to select the CLI or SDK

workflow yourself:

/polygres:polygres-cli

/polygres:polygres-sdk

/polygres:polygres-retrieval-design

/polygres:polygres-troubleshooting

Use the skill

Describe the result you want. The agent should select the relevant CLI

workflow, resolve the target project, and ask before destructive or

secret-producing operations.

Example prompts:

Log me into Polygres and help me select the correct project.

Import customers.json into public.customers. Inspect it first, explain any

conversion choices, and ask before changing data.

Review this SQL migration and ask before applying it to my selected project.

Configure cosine vector retrieval for documents.embedding with 1536

dimensions and verify readiness.

Use the Polygres SDK to find semantically similar documents, expand their

citations, and build deduplicated RAG context with source provenance.

Design a reviewable retrieval plan for this schema without changing the

project. Compare relational, graph, vector, text, and hybrid approaches.

Diagnose this failed import from public read-only evidence. Preserve request

and job IDs and recommend a safe corrective action.

The installed polygres --help output remains authoritative if the local CLI

version differs from the skill examples.

Build with the Python SDK

Use polygres-sdk for application retrieval, not project administration. The

skill distinguishes the per-project Runtime API URL from the control-plane and

Postgres URLs, keeps the API key in server-side environment configuration, and

uses passwordless connection metadata.

The SDK skill covers:

graph.expand , graph.neighborhood , graph.related , graph.path , and

graph.connection with real row IDs and bounded traversal;

vector search and row similarity with dimension and threshold validation;

TSVector and fuzzy text retrieval, including empty and ambiguous input;

graph-first, vector-first, and joint hybrid retrieval;

cursor and automatic pagination, typed results, request IDs, and SDK

exceptions;

anchor-first and semantic-first RAG with provenance, deduplication, and

application token budgets.

Filters narrow retrieval but do not replace application authorization. Use the

CLI skill when retrieval resources need to be configured or rebuilt.

Design retrieval before implementation

Use polygres-retrieval-design when strategy or data modeling is unresolved.

It maps stable row IDs, relationships, graph bounds, embedding dimensions,

text configuration, hybrid stages, authorization, provenance, deduplication,

token budgets, readiness, and validation into a reviewable plan. After user

approval, it delegates project setup to polygres-cli and application code to

polygres-sdk ; it never mutates a project directly.

Diagnose with public evidence

Use polygres-troubleshooting for authentication, project context,

provisioning, database, pooler, Runtime API, import, migration, retrieval,

pagination, timeout, and partial-failure symptoms. It uses installed CLI help,

public status commands, SDK readiness and exception types, and retained

request or job IDs. It does not use private endpoints or internal observability

and does not perform corrective mutations during diagnosis.

Import CSV, TSV, JSON, and JSONL

The CLI imports CSV. For TSV, JSON arrays, and JSONL or NDJSON, the skill can

run its bundled local converter to create a reviewed CSV before invoking

polygres import csv .

The converter:

makes no network requests;

never uploads the original non-CSV file;

reports row count, columns, key mappings, nesting, and conversion warnings;

requires an explicit choice before flattening or stringifying nested JSON;

detects when null and empty-string values cannot remain distinct;

writes the converted CSV atomically and reports source and output hashes.

Excel, Parquet, Avro, ORC, XML, YAML, SQL dumps, and pg_dump archives are not

automatically converted. Export those sources to CSV or JSONL first.

Update

Update a skill installed with the generic installer:

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

The skill uses the public polygres CLI and does not call private Polygres

control-plane routes directly.

Login uses browser approval. Do not give an agent a username, password, or

POLYGRES_ACCESS_TOKEN .

Database passwords are never retrieved or placed in command arguments. Let

psql prompt interactively.

Runtime API-key secrets are displayed once. Run key creation in your own

terminal when agent-transcript exposure is unacceptable.

Replacement imports, migrations, revocations, deletes, and schema mutations

require explicit approval.

Continue with the Polygres CLI guide for command behavior and exit

codes, or connect your application after the project is

ready.
