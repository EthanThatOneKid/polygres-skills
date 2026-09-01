source: https://docs.evokoa.com/polygres/sdk/connect-your-app
title: Dashboard connection setup | Polygres
source_hash: aa863d52db5d53300018dd3ac11c6065ace4d96eee0bff65dd28260f7725e34e
discovered_from: https://docs.evokoa.com/polygres

# Dashboard connection setup | Polygres

Dashboard connection setup

This guide applies to projects created with Host with Polygres . For a

synchronized project, query and change synchronized data through the source

PostgreSQL database and use Polygres for retrieval.

Open connection details

Confirm that this is a managed database project and that the project, database, and pooler show Ready on the project overview.

Open Connect ( /{organization}/{project_id}/connect ).

Choose the CLI , API & SDK , Database , or Frameworks tab.

The Database tab contains Manual database connection and Environment

variables sections. It shows the host, port, database, username, connection

string, and a generated psql command. Connection strings initially contain

the placeholder <password> so that opening the page does not expose the native

database password.

Choose pooled or direct

Connection Use it for Avoid using it for

Pooled connection Web applications, serverless functions, high-concurrency clients, and ordinary runtime reads and writes. Schema migrations, long administrative sessions, bulk import or export, and tools that require direct session behavior.

Direct connection Migrations, schema definitions, bulk import or export, administrative database tools, and clients that are incompatible with pooling. High-concurrency application traffic that benefits from the pooler.

A common application setup stores both values:

DATABASE_URL = "<pooled connection string>"

DIRECT_URL = "<direct connection string>"

Use DATABASE_URL for normal application traffic and configure your migration tool to use DIRECT_URL when it supports a separate direct URL.

The current public direct TLS endpoint is not production-safe for Prisma

migration and Prisma CLI workflows. Prisma runtime access may work with

compatibility handling on the pooled endpoint, but do not infer that

DIRECT_URL makes Prisma migrations supported. Use a supported migration path

or another compatible Postgres client until the dashboard removes this warning.

Understand pgbouncer=true

The dashboard’s pooled connection string includes pgbouncer=true for

Prisma-style ORMs. For psycopg, SQLAlchemy, psql , and other libpq clients,

create a client-specific copy of the same pooled URL with that Prisma hint

removed. This keeps application traffic on the pooled endpoint. Use the direct

URL for migrations, bulk work, and workflows that need direct session behavior.

The dashboard-generated Python, SQLAlchemy, and psql examples prepare the

appropriate client-specific URL automatically. When copying the pooled URL into

another non-Prisma client, remove the hint yourself.

Reveal the native database password only when needed

Decide which connection block or example you are about to configure.

Select Reveal Password in that section.

Copy the completed URL or command directly into a trusted secret manager or protected server-side environment.

Select Hide Password when finished, or leave the page. The revealed value is kept only in the current page state.

Reveal the password when you are actively configuring a trusted backend, migration runner, or database client. Do not reveal it for screenshots, documentation, chat messages, browser-side code, or a public build log.

The database password authenticates native Postgres access. It is not the same credential as a dashboard login or a Project API Key.

If you reset the database password in Settings, the old password stops working for direct and pooled database connections. The reset does not email the new password or return it automatically. Reveal the new password from the dashboard only when you are ready to update trusted application secrets or database clients.

Use Frameworks

Open Frameworks to copy language- or tool-oriented setup that mirrors the selected project connection information. The examples reference environment variables rather than embedding a secret in source code.

Before running an example:

Put the pooled and, when needed, direct URLs in the application’s secret store.

Confirm that the application runs on a trusted server or private development machine.

Test a small connection or read before starting a migration or large import.

Check Settings > Runtime if the connection fails even though the copied values are unchanged.

Use API & SDK for retrieval, not database sessions

The API & SDK tab is for Polygres retrieval calls and shows the Project ID,

Runtime API URL, key commands, and environment variables. Those calls use a

Project API Key , which you create in Project Settings > Project API Key

( /{organization}/{project_id}/settings?tab=api-keys ). A Project API Key does

not open a native Postgres connection, and the database password does not

replace it in generated retrieval examples.

You can also create a Project API Key and print connection URLs from the terminal with the Polygres CLI :

polygres env # prints DATABASE_URL, DIRECT_URL, and POLYGRES_RUNTIME_URL

polygres keys create my-key # creates and prints a new Runtime API key (shown once)

See Security basics for the credential boundary and Retrieval integration patterns for retrieval examples.

Configure database TLS

Polygres direct and pooled database endpoints support encrypted transport with certificate authority and hostname verification. Configure your client to use sslmode=verify-full with a trusted CA store. For libpq 16 or later:

sslmode=verify-full&sslrootcert=system

Keep TLS enabled. Do not work around a TLS error by disabling SSL.

Connection checklist

The project, database, and pooler are Ready .

The application uses Pooled connection for ordinary runtime traffic.

Migrations and bulk tools use Direct connection .

Secrets are stored server-side and are absent from source control.

The native database password and Project API Key are not confused or interchanged.

Connection URLs and API keys were obtained from Connect or with polygres env and polygres keys create .

Prisma direct migration and CLI workflows were not configured against the current public direct endpoint.
