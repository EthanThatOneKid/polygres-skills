source: https://docs.evokoa.com/polygres/reference/project-exports
title: Project exports | Polygres
source_hash: 64a90346ff92ff3daf1fbad24d654cffe1f23e324b88ba199f67db38807b2ba2
discovered_from: https://docs.evokoa.com/polygres

# Project exports | Polygres

Project exports

Export your project’s tables and data to a PostgreSQL archive you can download

and restore. Polygres prepares the file in the background, so you can keep

working while it runs.

Before you start

Exports are available for standard projects on shared Nano and Basic

when the project is Ready or Read-only .

You can create and download exports as an owner, admin, or developer . Use a

dashboard session token or CLI access token to authenticate requests to

https://api.polygres.com/v1 . Export requests use your account’s access to the

project; application Runtime API keys are for your app’s queries.

Endpoints

Method Path relative to /v1 Result

POST /projects/{project_id}/exports/pg-dump 202 : create an export or return the project’s existing queued/running export.

GET /projects/{project_id}/exports/{export_id} 200 : read export status and metadata.

GET /projects/{project_id}/exports/{export_id}/download 200 : stream the ready archive as application/octet-stream .

Send an empty JSON object or leave the request body empty. Polygres selects the

export settings for you.

1. Request an export

Set PROJECT_ID to your project ID and POLYGRES_ACCESS_TOKEN to your dashboard

session token or CLI access token.

curl --fail-with-body --silent --show-error \

-X POST "https://api.polygres.com/v1/projects/${ PROJECT_ID }/exports/pg-dump" \

-H "Authorization: Bearer ${ POLYGRES_ACCESS_TOKEN }" \

-H 'Content-Type: application/json' \

--data '{}'

Example response:

{

"request_id" : "req_example" ,

"export" : {

"id" : "04a67061-2e12-455b-8a27-d747cd1a620e" ,

"scope" : "user_database" ,

"format" : "postgres_custom" ,

"status" : "queued" ,

"created_at" : "2026-09-22T12:00:00Z" ,

"expires_at" : "2026-09-23T12:00:00Z"

}

}

If an export is already in progress, this request returns its details. Once it

finishes, you can request a fresh export.

2. Check progress

Set EXPORT_ID to the returned export.id . Check this endpoint every few seconds

until status is ready :

curl --fail-with-body --silent --show-error \

"https://api.polygres.com/v1/projects/${ PROJECT_ID }/exports/${ EXPORT_ID }" \

-H "Authorization: Bearer ${ POLYGRES_ACCESS_TOKEN }"

Status Next step

queued Your export is waiting to start.

running Polygres is preparing your file. Check again in a few seconds.

ready Download before expires_at . The response includes size_bytes and sha256 .

failed Check error_code ; request a new export or contact support with the export and request IDs.

expired Request a new export.

Your download is available until expires_at , 24 hours after the export was

requested . Use the status field to follow its progress.

3. Download and verify

When the status is ready , save the archive:

curl --fail --silent --show-error \

"https://api.polygres.com/v1/projects/${ PROJECT_ID }/exports/${ EXPORT_ID }/download" \

-H "Authorization: Bearer ${ POLYGRES_ACCESS_TOKEN }" \

--output project.dump

shasum -a 256 project.dump

Compare the checksum with export.sha256 and the file size with

export.size_bytes to confirm the download is complete. Downloads are private

and use the same authentication as the export request.

What you get

The file contains your database schema and data, including tables in public

and custom schemas, in PostgreSQL custom format. You can restore it with

pg_restore or upload it through the Polygres dashboard.

The export focuses on your application data. Polygres-managed schemas, Graph and

Context state, and project settings stay with the original project. Keep your

Graph and Context configuration separately so you can recreate collections and

rebuild indexes after restoring your tables.

Database ownership, permissions, replication settings, and security labels are

omitted so you can configure access for the destination. Install any PostgreSQL

extensions your tables need before restoring.

Restore an archive

Use a compatible PostgreSQL 17 pg_restore client and a new or empty destination

database. Set RESTORE_DATABASE_URL to its direct connection URL, then inspect

and restore the archive:

pg_restore --list project.dump

pg_restore --no-owner --no-acl --exit-on-error \

--dbname= " $RESTORE_DATABASE_URL " project.dump

To restore into Polygres through the dashboard, use Import > pg_dump and

select the custom format. See Restore a pg_dump file

for the import workflow and target compatibility requirements.

Using pg_dump

For standard Nano and Basic projects, use the export endpoint to create your

archive. Polygres runs pg_dump for you and selects your application data.

You can continue using PostgreSQL’s pg_restore tools with the downloaded file.

If you run pg_dump directly and see a permission message with an export hint,

follow the steps above to download your archive.

Help with exports

Code HTTP status Action

PROJECT_EXPORT_NOT_SUPPORTED 409 Choose a standard Nano project on shared infrastructure or a standard Basic project.

PROJECT_EXPORT_UNAVAILABLE 503 Wait for your project to finish any upgrade or move, then request a fresh export. Contact support if this continues.

PROJECT_EXPORT_NOT_FOUND 404 Check that the export ID belongs to the selected project.

PROJECT_EXPORT_NOT_READY 409 Check progress and download when the status is ready .

PROJECT_EXPORT_EXPIRED 410 Request a fresh export to get a new download.

If export.error_code is PROJECT_EXPORT_FAILED , try a fresh export. For help

from support, include the export ID and request_id . See

Handle API Errors for authentication and other

API responses.
