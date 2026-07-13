source: https://docs.evokoa.com/polygres/agent-skills
title: Polygres Agent Skills | Polygres
source_hash: d9fe11093da498cc5ff357df1b187080d705669a62cde793659cb35d498486b6
discovered_from: https://docs.evokoa.com/polygres

# Polygres Agent Skills | Polygres

Polygres Agent Skills

The polygres-cli Agent Skill teaches compatible coding agents how to operate

Polygres through the public CLI. It covers browser login, project selection,

database access, Runtime API keys, data imports, migrations, retrieval setup,

readiness checks, and failure recovery.

The skill does not include the CLI. Install both components:

pipx install "polygres-cli==0.1.0"

npx skills add Evokoa/polygres-skills --skill polygres-cli

The public skill source is

Evokoa/polygres-skills . Review the

repository before installation if your organization requires third-party code

approval.

Choose an installation method

Compatible Agent Skills installers

Install interactively into the current project:

npx skills add Evokoa/polygres-skills --skill polygres-cli

Install globally for Codex and Claude Code:

npx skills add Evokoa/polygres-skills \

--skill polygres-cli \

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

Invoke the bundled skill explicitly with:

/polygres:polygres-cli

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

The installed polygres --help output remains authoritative if the local CLI

version differs from the skill examples.

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
