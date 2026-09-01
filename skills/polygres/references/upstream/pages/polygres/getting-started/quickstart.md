source: https://docs.evokoa.com/polygres/getting-started/quickstart
title: Quickstart | Polygres
source_hash: fa8a47332b9249285225895f1a269b60c8a564c12f8c02b523101a7fc118f137
discovered_from: https://docs.evokoa.com/polygres

# Quickstart | Polygres

Quickstart

This guided outcome takes you from an active account to a verified text-retrieval query in the Python SDK. It uses dashboard and CLI alternatives for setup, then the same SDK query.

To connect an existing PostgreSQL database, follow

Create a synced PostgreSQL project .

This workflow uses a standard project created with Host with Polygres so it

can apply SQL and migrations. For synchronized data, use the synced-project

guide linked above and keep SQL workflows in the source PostgreSQL database.

Prerequisites

An active Polygres account. Signup, organization setup, and any required email verification happen in the dashboard .

Python 3.10 or newer.

For the CLI path, install polygres-cli==0.4.1 .

For SDK calls, install polygres-sdk==0.4.1 in your application virtual environment.

1. Create and select a project

Dashboard CLI

Dashboard

Sign in, choose Host with Polygres , create Default Project , rename it to Support Search from Settings, and wait until the managed database project is ready.

CLI

The CLI path begins with an existing active account:

polygres login

polygres projects create standard "Support Search"

polygres projects use "Support Search"

projects create standard waits for provisioning. Run projects use

afterward to select the project for later commands.

2. Add schema and data

Save the following as seed.sql . The eight-dimensional vectors are toy placeholders for schema demonstrations. They are not model-generated semantic embeddings.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (id text primary key , title text , body text , embedding vector( 8 ));

INSERT INTO documents VALUES

( 'doc_1' , 'Refund Request' , 'I need a refund for my recent purchase.' , '[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]' ),

( 'doc_2' , 'Login Issue' , 'Password reset is not working.' , '[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]' );

Dashboard CLI

Dashboard

Open the dashboard SQL Editor and paste the SQL.

CLI

polygres migrations apply --file ./seed.sql --name seed_documents

Or run polygres db psql , then paste the SQL at the psql prompt.

3. Configure text retrieval and wait for readiness

Dashboard CLI

Dashboard

Create a TSVector configuration for documents.body in Text Search setup and wait for it to become ready.

CLI

polygres text configs create-tsvector documents_body_tsv --table documents --text-column body --generated-column body_tsv --yes

polygres text configs list

The first command creates the generated column, index, and configuration

through one configuration API request. It does not apply a migration.

Continue only when index_status is ready .

4. Create credentials and set environment variables

Dashboard CLI

Dashboard

Create a Project API Key in Settings and copy the Runtime API URL from Connect.

CLI

polygres keys create quickstart-key

polygres env

Save the key shown once. Copy and run the POLYGRES_RUNTIME_URL export line from polygres env .

export POLYGRES_API_KEY = "poly_live_..."

export POLYGRES_RUNTIME_URL = "https://{project_id}.api.db.polygres.com/v1"

5. Query with the Python SDK

In your application virtual environment:

pip install "polygres-sdk==0.4.1"

import os

from polygres import Polygres

project = Polygres(

api_key = os.environ[ "POLYGRES_API_KEY" ],

runtime_url = os.environ[ "POLYGRES_RUNTIME_URL" ],

).project()

page = project.text.tsvector( "refund" , config = "documents_body_tsv" , limit = 5 )

for result in page.results:

print (result.id, result.score, result.properties)

You now have a project, selected project context, schema and data, ready text

retrieval, a Runtime API key and URL, and a first SDK query. For real vector

search, create a pgContext collection and

populate its vector column with embeddings from the same model used for query

embeddings. New legacy pgvector configuration registration is retired.
