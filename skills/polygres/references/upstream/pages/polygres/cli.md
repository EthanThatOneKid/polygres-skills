source: https://docs.evokoa.com/polygres/cli
title: Polygres CLI | Polygres
source_hash: 076195ffdd76a8d346862de2fe58f55faf97b8ef287e0795434236f469fb4977
discovered_from: https://docs.evokoa.com/polygres

# Polygres CLI | Polygres

Polygres CLI

The public CLI is shipped with PyPI package polygres-cli . Use it for project

setup, migrations, imports, single-row writes, retrieval configuration, API

keys, connection details, and pgContext AI Search collection workflows. Use the

Python SDK for retrieval queries and backend-owned pgContext

automation in application code. If you previously installed the combined

polygres 0.2.x package, follow the package split

migration

before following the workflows below.

CLI setup requires an existing active Polygres account. Signup, organization onboarding, email verification, password management, organization switching, and project deletion remain dashboard workflows.

First standard project from a terminal

Use this workflow when Polygres should host the primary PostgreSQL database. It

creates a standard project, applies a migration, configures text retrieval, and

creates a Runtime API key. Project creation waits for readiness, while project

selection remains an explicit step.

pipx install "polygres-cli==0.4.1"

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

AI Search with pgContext

Generic API routes

Command reference
