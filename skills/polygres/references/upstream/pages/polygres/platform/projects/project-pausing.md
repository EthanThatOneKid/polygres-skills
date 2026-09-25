source: https://docs.evokoa.com/polygres/platform/projects/project-pausing
title: Project pausing | Polygres
source_hash: 5839ac22d1040fef2217252d5f7fcadc9c60a7579801f7175a01e79ea50ca0a1
discovered_from: https://docs.evokoa.com/polygres

# Project pausing | Polygres

Project pausing

Free Nano projects may be paused after at least 14 days of inactivity to conserve

cloud resources. This applies to both hosted and synced projects.

When a project is paused, its data and configuration are preserved, but its

database and search features are unavailable until you restore it. Paused

projects appear as Archived in the dashboard.

What counts as activity?

Activity means using your project’s database. This includes:

Reading or writing data, such as browsing a table or running a SQL query.

Making database requests through your application, API, SDK, CLI, or MCP.

Running searches, importing data, or generating embeddings.

Syncing data changes from an external PostgreSQL database.

Your application’s database usage counts even when you aren’t signed in to the

dashboard. Simply signing in, opening a project page, or leaving a connection

open does not count as database activity. Background health checks and an idle

sync connection do not keep a project active either.

Before your project is paused

The organization owner receives a warning email before the project is paused

and a confirmation email once pausing is complete.

If you receive a warning and want to keep the project active, use its database.

You can open the project in the dashboard and browse a

table or run a query, or make database requests through your connected application.

For a synced project, changes applied from your source database also count as

activity.

Restore a paused project

Open your project in the dashboard .

Select Restore project .

Wait for restoration to finish before reconnecting your application.

Restoration takes time and depends on available capacity. You can leave the

page and return later to check progress. If you don’t have permission to restore

the project, ask your organization owner or administrator.

Your saved data, configuration, and API keys are retained through restoration.

Once the project is ready, you can use its database and search features again.

For synced projects, restoration also takes a fresh snapshot of your external

PostgreSQL database and resumes syncing changes. Existing embeddings are

preserved. Wait for synchronization to catch up before using search results.

See restoring a synced project .

If restoration fails, contact Polygres support

and include the request ID shown with the error.

Applications and command-line tools

Requests to a paused project return an archive-related error. Restore the

project from the dashboard before retrying. See:

CLI project status .

Python SDK archive errors .

API archive responses .
