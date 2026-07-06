source: https://docs.evokoa.com/polygres/getting-started/quickstart
title: Quickstart | Polygres
source_hash: e752293c0a6d6fdc12cb3b3644fa337ab2fa600af87a9003d65d120a53d70c1a
discovered_from: https://docs.evokoa.com/polygres

# Quickstart | Polygres

Quickstart

This tutorial will guide you through building a simple Text Search for support tickets. In less than 3 minutes, you will go from a fresh project to running queries locally using the Python SDK.

1. Create your Project

Sign up or log in to Polygres.

If prompted, join or create your organization.

Open New project ( /{organization}/new ), name it Support Search , and click create.

Wait until the project overview reports that your database is ready before continuing.

2. Add Sample Data

We need some data to search. Here are some options:

Connect your application using the DATABASE_URL to run your ORM migrations.

Load data from a CSV, SQL file, or pg_dump .

Alternatively, you can import this minimal test dataset directly in the dashboard SQL Editor ( /{organization}/{projectId}/sql ) to try everything out. This dataset provides everything you need to test Text, Vector, and Graph retrieval:

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE accounts (

id text primary key ,

name text

);

CREATE TABLE documents (

id text primary key ,

account_id text references accounts(id),

title text ,

body text ,

embedding vector( 8 )

);

INSERT INTO accounts (id, name ) VALUES ( 'acct_1' , 'Acme Corp' );

INSERT INTO documents (id, account_id, title, body, embedding) VALUES

( 'doc_1' , 'acct_1' , 'Refund Request' , 'I need a refund for my recent purchase.' , '[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]' ),

( 'doc_2' , 'acct_1' , 'Login Issue' , 'Password reset is not working.' , '[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]' );

3. Configure Retrieval

Now we will tell Polygres how to search your data. With our minimal dataset, you can explore any mode:

Text Search : Choose TSVector on documents.body .

Vector Search : Select documents.embedding .

Graph Search : Connect accounts to documents via account_id .

For this tutorial, let’s configure the easiest mode: Text Search .

Open Text search setup ( /{organization}/{projectId}/workspace/text-search ) from your workspace.

Choose TSVector (Full-text search).

Select the documents table.

Name the configuration documents_body_tsv .

Click Save and confirm that the configuration’s index is ready.

4. Test in the Dashboard

Let’s make sure it works before writing any code.

Open the Query Workbench ( /{organization}/{projectId}/workspace/query ).

Select your documents_body_tsv configuration.

Type "refund" into the search bar.

You should instantly see your “Refund Request” document returned.

5. Query from Python

Now let’s run that exact same query from your local machine.

Go to Settings ( /{organization}/{projectId}/settings ) and generate a Project API Key .

Go to Connect ( /{organization}/{projectId}/connect ) and copy your Runtime API URL .

Store both values in your environment:

export POLYGRES_API_KEY = "poly_live_..."

export POLYGRES_RUNTIME_URL = "https://{project_id}.api.db.polygres.com/v1"

Install the Python SDK:

pip install polygres

Run this Python script to query your database:

import os

from polygres import Polygres

client = Polygres(

api_key = os.environ[ "POLYGRES_API_KEY" ],

runtime_url = os.environ[ "POLYGRES_RUNTIME_URL" ],

)

# Connect to your project

project = client.project()

# Query the Text Search configuration you just built

page = project.text.tsvector(

"refund" ,

config = "documents_body_tsv" ,

limit = 5 ,

)

for result in page.results:

print ( f "ID: { result.id } , Score: { result.score } " )

print ( f "Properties: { result.properties } " )

🎉 Congratulations! You just created a project, seeded data, configured an index, and queried it from an application.

Once you are comfortable with Text Search, you can use this exact same test dataset to configure a Vector index on the embedding column and run semantic queries!

Next steps

Product Guides

Python SDK

Connect and credentials

Load and manage data

Configure and query retrieval

Retrieval integration patterns

Reference

Routes

Error codes
