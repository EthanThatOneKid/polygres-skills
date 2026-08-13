source: https://docs.evokoa.com/polygres/cli
title: Polygres CLI | Polygres
source_hash: 5611f118735b25fdcbbd2e4847b06bc7f2532fa1a778560849451e036f58cc94
discovered_from: https://docs.evokoa.com/polygres

# Polygres CLI | Polygres

Polygres CLI

The public CLI is shipped with PyPI package polygres-cli . Use it for project

setup, migrations, imports, retrieval configuration, API keys, connection

details, and pgContext AI Search collection workflows. Use the Python

SDK for retrieval queries and backend-owned pgContext

automation in application code. If you previously installed the combined

polygres 0.2.x package, follow the package split

migration

before following the workflows below.

CLI setup requires an existing active Polygres account. Signup, organization onboarding, email verification, password management, organization switching, and project deletion remain dashboard workflows.

First project from a terminal

Copy this workflow after your account is active. projects create waits for provisioning, but does not select the new project .

pipx install "polygres-cli==0.2.2"

polygres login

polygres projects create "Support Search"

polygres projects use "Support Search"

polygres migrations apply --file ./seed.sql --name seed_documents

polygres text configs create-tsvector documents_body_tsv --table documents --text-column body --generated-column body_tsv --yes

polygres text configs list

polygres keys create local-dev

polygres env

Wait until text configs list reports ready , save the one-time API-key secret, and use the POLYGRES_RUNTIME_URL line from polygres env with the Python SDK.

Navigation

Install and authenticate

Projects

Database and environment

API keys

Imports and migrations

AI Search with pgContext

Generic API routes

Command reference
