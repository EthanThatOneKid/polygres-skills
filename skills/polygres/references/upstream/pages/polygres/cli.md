source: https://docs.evokoa.com/polygres/cli
title: Polygres CLI | Polygres
source_hash: 2c04ecea2ea95c1ac0de890491123f0dd29c56791942561deb970524249fe50d
discovered_from: https://docs.evokoa.com/polygres

# Polygres CLI | Polygres

Polygres CLI

The public CLI is shipped with PyPI package polygres-cli . Use it for project setup, migrations, imports, retrieval configuration, API keys, and connection details. Use the Python SDK for retrieval queries in application code. If you previously installed the combined polygres 0.2.x package, follow the package split migration before following the workflows below.

CLI setup requires an existing approved Polygres account. Signup, organization onboarding, password management, organization switching, and project deletion remain dashboard workflows.

First project from a terminal

Copy this workflow after your account has been approved. projects create waits for provisioning, but does not select the new project .

pipx install "polygres-cli==0.1.0"

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

Command reference
