source: https://docs.evokoa.com/polygres/sdk/connection-examples
title: Connection examples | Polygres
source_hash: d0257b176b3957a78913e3aaeb46907eb8de7122f5b265270e14f2dc2e8b27c6
discovered_from: https://docs.evokoa.com/polygres

# Connection examples | Polygres

Connection examples

Polygres exposes a pooled PostgreSQL endpoint and a direct PostgreSQL endpoint. Both use the native PostgreSQL username and password revealed in the dashboard.

DATABASE_URL=postgresql://<username>:<password>@<pooled_host>:5432/<database>?pgbouncer=true&sslmode=require

DIRECT_URL=postgresql://<username>:<password>@<direct_host>:5432/<database>?sslmode=require

Store both URLs in a secret manager. Do not commit them or send them to a browser.

Choose pooled or direct

Use DATABASE_URL for normal application traffic:

backend request handlers,

ORM queries,

serverless functions,

high-concurrency, short-lived reads and writes.

The pooled endpoint uses PgBouncer transaction pooling and is the default for application runtime traffic.

Use DIRECT_URL for operations that need a direct PostgreSQL session:

migrations and schema changes,

COPY , pg_dump , and restore operations,

bulk ingestion and sustained background writes,

tools that are incompatible with transaction pooling.

A service can use both: pooled for runtime queries and direct for migrations or maintenance.

Copy connection metadata from the dashboard

Use Connect > Database to copy safe host and URL templates. These strings contain

<password> placeholders until an authorized user reveals the native database password

in the dashboard.

Reveal the real password only when a trusted destination is ready. Store completed

connection URLs in a secret manager or protected server-side environment.

Prisma

Use the pooled URL for application queries and the direct URL for Prisma schema operations:

// schema.prisma

datasource db {

provider = "postgresql"

url = env ( "DATABASE_URL" )

directUrl = env ( "DIRECT_URL" )

}

generator client {

provider = "prisma-client-js"

}

npx prisma generate

npx prisma migrate deploy

Application code uses the generated client normally:

import { PrismaClient } from "@prisma/client" ;

export const prisma = new PrismaClient ();

Node pg

Create one process-level pool from DATABASE_URL :

import { Pool } from "pg" ;

export const pool = new Pool ({

connectionString: process.env. DATABASE_URL ,

max: 10 ,

});

const result = await pool. query (

"select id, title from documents where status = $1 limit $2" ,

[ "published" , 20 ],

);

For a migration or bulk job, create a separate client from DIRECT_URL :

import pg from "pg" ;

const client = new pg. Client ({

connectionString: process.env. DIRECT_URL ,

});

await client. connect ();

try {

await client. query ( "select 1" );

} finally {

await client. end ();

}

SQLAlchemy

Use the pooled URL for the application engine:

import os

from sqlalchemy import create_engine, text

engine = create_engine(

os.environ[ "DATABASE_URL" ],

pool_pre_ping = True ,

)

with engine.begin() as connection:

rows = connection.execute(

text( "select id, title from documents where status = :status limit 20" ),

{ "status" : "published" },

)

Configure Alembic or another migration runner with DIRECT_URL rather than reusing the pooled application URL:

migration_engine = create_engine(

os.environ[ "DIRECT_URL" ],

pool_pre_ping = True ,

)

psycopg

Use DATABASE_URL for normal backend work:

import os

import psycopg

with psycopg.connect(os.environ[ "DATABASE_URL" ]) as connection:

with connection.cursor() as cursor:

cursor.execute(

"select id, title from documents where status = %s limit %s " ,

( "published" , 20 ),

)

rows = cursor.fetchall()

Use DIRECT_URL for a migration or bulk-processing process:

with psycopg.connect(os.environ[ "DIRECT_URL" ]) as connection:

with connection.cursor() as cursor:

cursor.execute( "select current_database(), current_user" )

print (cursor.fetchone())

Connection handling

Keep these rules at the application boundary:

Open a shared pool or engine once per process instead of opening a new pool per request.

Set finite application timeouts and bound pool sizes.

Parameterize values rather than interpolating SQL strings.

Use the direct endpoint only where its session behavior is required.

Percent-encode reserved characters if you construct a URL manually; prefer the dashboard-provided template and your platform’s secret tooling.

Log database host and request context when needed, but redact passwords and full URLs containing credentials.

Database connections and retrieval API calls are separate. Use a native PostgreSQL

password for the examples on this page and a Project API Key for generated retrieval

examples in Query from the dashboard and

Retrieval integration patterns .
