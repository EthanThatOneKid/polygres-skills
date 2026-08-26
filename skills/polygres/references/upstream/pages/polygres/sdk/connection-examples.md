source: https://docs.evokoa.com/polygres/sdk/connection-examples
title: Database client examples | Polygres
source_hash: fab24ec98e3d0f8fad889db759365a0e7226dbf289b602eba6fbf13dcfa64438
discovered_from: https://docs.evokoa.com/polygres

# Database client examples | Polygres

Database client examples

These examples apply only to managed database projects created with Host with Polygres . Polygres exposes a pooled PostgreSQL endpoint and a direct PostgreSQL endpoint for those projects, and both use the native PostgreSQL username and password revealed in the dashboard.

Synced projects do not expose pooled or direct endpoints, native database credentials, psql , the SQL Editor, or other direct SQL access. Connect to the source PostgreSQL database when you need SQL access to synchronized data.

DATABASE_URL=postgresql://<username>:<password>@<pooled_host>:5432/<database>?sslmode=verify-full&sslrootcert=system

DIRECT_URL=postgresql://<username>:<password>@<direct_host>:5432/<database>?sslmode=verify-full&sslrootcert=system

Store both URLs in a secret manager and keep them in trusted server-side

environments. These examples use libpq 16 system certificates. For another

client or certificate store, apply that client’s equivalent CA and hostname

verification settings.

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

A service can use both: pooled for runtime queries and direct for migrations or maintenance. Prisma is a current exception: the public direct TLS endpoint is not production-safe for Prisma migration or CLI workflows.

Copy connection metadata from the dashboard

Use Connect > Database to copy safe host and URL templates. These strings contain

<password> placeholders until an authorized user reveals the native database password

in the dashboard.

Reveal the real password only when a trusted destination is ready. Store completed

connection URLs in a secret manager or protected server-side environment.

Prisma

Use a Prisma-specific pooled URL with the PgBouncer hint only for application

runtime queries:

PRISMA_DATABASE_URL=postgresql://<username>:<password>@<pooled_host>:5432/<database>?pgbouncer=true&sslmode=verify-full&sslrootcert=system

// schema.prisma

datasource db {

provider = "postgresql"

url = env ( "PRISMA_DATABASE_URL" )

}

generator client {

provider = "prisma-client-js"

}

npx prisma generate

Prisma runtime access may require compatibility handling. Do not run Prisma

migrations or other Prisma CLI database workflows against the current public

direct endpoint, and do not add directUrl = env("DIRECT_URL") as though it

makes those workflows supported. Use another supported migration path until

the dashboard’s Prisma limitation is removed.

Application code uses the generated client normally:

import { PrismaClient } from "@prisma/client" ;

export const prisma = new PrismaClient ();

Node pg

Create one process-level pool from DATABASE_URL . Remove the Prisma-only

pgbouncer=true hint if the URL came from the dashboard:

import { Pool } from "pg" ;

const databaseUrl = process.env. DATABASE_URL ;

if ( ! databaseUrl) {

throw new Error ( "DATABASE_URL is required" );

}

const pooledUrl = new URL (databaseUrl);

pooledUrl.searchParams. delete ( "pgbouncer" );

export const pool = new Pool ({

connectionString: pooledUrl. toString (),

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

pooled_url = (

os.environ[ "DATABASE_URL" ]

.replace( "pgbouncer=true&" , "" )

.replace( "&pgbouncer=true" , "" )

.replace( "?pgbouncer=true" , "" )

)

engine = create_engine(

pooled_url,

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

pooled_url = (

os.environ[ "DATABASE_URL" ]

.replace( "pgbouncer=true&" , "" )

.replace( "&pgbouncer=true" , "" )

.replace( "?pgbouncer=true" , "" )

)

with psycopg.connect(pooled_url) as connection:

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

password for the examples on this page and a Project API Key for Runtime retrieval

examples in Retrieval integration patterns .
