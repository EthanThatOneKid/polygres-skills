source: https://docs.evokoa.com/polygres/cli
title: Polygres CLI | Polygres
source_hash: 4670c2b7aa233e817e7cb45f5d0288e05ee931323b22b893a9279c240a48f566
discovered_from: https://docs.evokoa.com/polygres

# Polygres CLI | Polygres

Polygres CLI

Use the Polygres CLI to create projects, import and update data, generate

embeddings, and set up search from your terminal. It also provides commands for

database migrations, API keys, and connection details.

Install the polygres-cli package to get started, then follow the

search examples to query with text or your own

vectors. For search and automation in your application, use the

Python SDK . If you use the older

combined polygres 0.2.x package, follow the migration steps .

Start with an active Polygres account. Use the dashboard to create your account, manage your profile, and switch organizations.

First standard project from a terminal

Use this workflow when Polygres should host the primary PostgreSQL database. It

creates a standard project, applies a migration, configures text search, and

creates a Runtime API key. Once the project is ready, projects use selects it

for the following commands.

pipx install "polygres-cli==0.5.0"

polygres login

polygres projects create standard "Support Search"

polygres projects use "Support Search"

polygres migrations apply --file ./seed.sql --name seed_documents

polygres text configs create-tsvector documents_body_tsv --table documents --text-column body --generated-column body_tsv --yes

polygres text configs list

polygres keys create local-dev

polygres env

Wait until text configs list reports ready , save the one-time API-key secret, and use the POLYGRES_RUNTIME_URL line from polygres env with the Python SDK.

First synced project from a terminal

Use this workflow when an existing PostgreSQL database remains the source of

truth:

export SOURCE_DATABASE_URL = "postgresql://..."

polygres login

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL \

--all-eligible \

--yes

polygres projects use "Support Search"

polygres projects status

For an interactive setup, run:

polygres projects create sync "Support Search"

The CLI securely prompts for the connection URL and table selection. After the

project reaches Streaming , configure retrieval over the synchronized

tables. Application writes continue through the source PostgreSQL database.

Navigation

Install and authenticate

Projects

Database and environment

API keys

Imports and migrations

Write rows

Generate embeddings

AI Search with pgContext

Generic API routes

Command reference
