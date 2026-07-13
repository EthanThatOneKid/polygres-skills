source: https://docs.evokoa.com/polygres/sdk/connect-your-app
title: Connect your app | Polygres
source_hash: 2302a2c912cd9e51fac589c8178b1f41d6ef2e1f3c806da386093b4e81ef2e44
discovered_from: https://docs.evokoa.com/polygres

# Connect your app | Polygres

Connect your app

Open connection details

Confirm that the project, database, and pooler show Ready on the project overview.

Open Connect ( /{organization}/{project_id}/connect ).

Use the Database , Client examples , and API access tabs according to what you are connecting.

The Database tab shows the host, port, database, username, connection string, and a generated psql command. Connection strings initially contain the placeholder <password> so that opening the page does not expose the native database password.

Choose pooled or direct

Connection Use it for Avoid using it for

Pooled connection Web applications, serverless functions, high-concurrency clients, and ordinary runtime reads and writes. Schema migrations, long administrative sessions, bulk import or export, and tools that require direct session behavior.

Direct connection Migrations, schema definitions, bulk import or export, administrative database tools, and clients that are incompatible with pooling. High-concurrency application traffic that benefits from the pooler.

A common application setup stores both values:

DATABASE_URL = "<pooled connection string>"

DIRECT_URL = "<direct connection string>"

Use DATABASE_URL for normal application traffic and configure your migration tool to use DIRECT_URL when it supports a separate direct URL.

Understand pgbouncer=true

The pooled connection string includes pgbouncer=true . Prisma-style ORMs use this hint to adapt to pooled behavior. Standard command-line and database clients may reject that query parameter, so the dashboard-generated psql command removes it automatically.

Do not remove the parameter from the pooled URL merely because a CLI rejects it. Use the direct URL or the generated psql command for that tool instead.

Reveal the native database password only when needed

Decide which connection block or example you are about to configure.

Select Reveal Password in that section.

Copy the completed URL or command directly into a trusted secret manager or protected server-side environment.

Select Hide Password when finished, or leave the page. The revealed value is kept only in the current page state.

Reveal the password when you are actively configuring a trusted backend, migration runner, or database client. Do not reveal it for screenshots, documentation, chat messages, browser-side code, or a public build log.

The database password authenticates native Postgres access. It is not the same credential as a dashboard login or a Project API Key.

If you reset the database password in Settings, the old password stops working for direct and pooled database connections. The reset does not email the new password or return it automatically. Reveal the new password from the dashboard only when you are ready to update trusted application secrets or database clients.

Use Client examples

Open Client examples to copy language- or tool-oriented setup that mirrors the selected project connection information. The examples reference environment variables rather than embedding a secret in source code.

Before running an example:

Put the pooled and, when needed, direct URLs in the application’s secret store.

Confirm that the application runs on a trusted server or private development machine.

Test a small connection or read before starting a migration or large import.

Check Settings > Runtime if the connection fails even though the copied values are unchanged.

Use API access for retrieval, not database sessions

The API access tab is for Polygres retrieval calls. Those calls use a Project API Key , which you create in Settings ( /{organization}/{project_id}/settings ) under Project API Key . A Project API Key does not open a native Postgres connection, and the database password does not replace it in generated retrieval examples.

You can also create a Project API Key and print connection URLs from the terminal with the Polygres CLI :

polygres env # prints DATABASE_URL, DIRECT_URL, and POLYGRES_RUNTIME_URL

polygres keys create my-key # creates and prints a new Runtime API key (shown once)

See Security basics for the credential boundary and Query from the dashboard for generated retrieval code.

TLS compatibility during beta

Dashboard connection strings use encrypted transport with sslmode=require . During the current beta compatibility mode, certificate hostname verification is not enabled. Clients that require CA-strict or hostname-verified TLS may reject the connection until configured for the supported mode.

Keep encryption enabled. Do not work around a TLS error by disabling SSL entirely; use the dashboard-provided string and the client’s supported sslmode=require configuration.

Connection checklist

The project, database, and pooler are Ready .

The application uses Pooled connection for ordinary runtime traffic.

Migrations and bulk tools use Direct connection .

Secrets are stored server-side and are absent from source control.

The native database password and Project API Key are not confused or interchanged.

Connection URLs and API keys were obtained from the dashboard or with polygres env and polygres keys create .
