source: https://docs.evokoa.com/polygres/platform/projects
title: Projects | Polygres
source_hash: 78e83b7bac37297b0b2edb3a5c57c723d41a060a3e0aaebf94c5b90922bea9d1
discovered_from: https://docs.evokoa.com/polygres

# Projects | Polygres

Projects

Every project belongs to an organization . Use a standard project when Polygres owns the primary database, or create a synced project when an existing PostgreSQL database remains the source of truth.

Choose a project type

Data source Use it when Access model

Supabase You want selected tables from an existing Supabase project copied continuously into Polygres. The synced-project access model applies. Query and modify rows in Supabase.

Neon You want selected tables from an existing Neon database copied continuously into Polygres. The synced-project access model applies. Query and modify rows in Neon.

PlanetScale You want selected tables from a PlanetScale Postgres database copied continuously into Polygres. The synced-project access model applies. Query and modify rows in PlanetScale.

Postgres Database You want selected tables from another PostgreSQL database copied continuously into Polygres. The synced-project access model applies. Query and modify rows in the source database.

Host with Polygres You want a new Polygres-managed PostgreSQL database. Native database credentials, pooled and direct connection URLs, psql , the SQL Editor, imports, migrations, and Runtime API access are available.

For the complete workflow and operating model, see Create a synced PostgreSQL project . Before opening the wizard, follow the PostgreSQL sync setup guides for standard PostgreSQL, Neon, Supabase, or PlanetScale.

Before choosing a source, review Free and Paid projects . A Free project uses the shared Nano tier. A Paid project uses the isolated Basic tier and is available only to eligible organizations when the dashboard offers it.

Create a project in an organization

Create each project inside the organization that should own it. Confirm the organization slug in the dashboard URL before you begin.

Open New project ( /{organization}/new ) from the target organization.

Choose Free or, when offered for your organization, Paid .

Choose the data source.

For any Paid project, configure Storage, Context, and Graph capacity. A Paid synchronized project does this after source checks and table selection.

Confirm the creation action shown. Paid synchronized projects include a separate Review payment step before Create Project . New projects are named Default Project .

The dashboard opens the organization-scoped project overview while Polygres provisions the selected project type. You can change the name later in the project’s Settings page.

Free projects use the shared Nano tier. Each organization has one Free slot across hosted and synchronized projects. Paid Basic projects leave that slot available. Existing organizations with multiple Nano projects can keep them and can create another Free project after the current Nano projects are removed.

Paid projects use the isolated Basic tier and start at $10 per month. An owner or admin with an eligible organization subscription can create one with Host with Polygres or, when offered, an external PostgreSQL source. The dashboard applies available credits to the estimated first-cycle charge and shows any remainder paid through Stripe. During Paid synced setup, Polygres temporarily sets aside only the available-credit portion shown in the payment review.

A managed database project receives complete connection details and a Runtime API URL. For a synced project, use the source database for SQL and writes. After Synced Basic is ready, the overview shows stable pooled and direct hostnames for its isolated database; the connection details shown there are limited to those hostnames. When creation needs attention, the dashboard explains the permission, subscription, payment, or availability step to complete.

Follow provisioning

While the project shows Provisioning , keep the overview open or return to it later. The dashboard refreshes status while the database, pooler, and project runtime come online.

Project state What it means Recommended action

Provisioning Infrastructure is still being created or retried. Wait for the automatic status refresh before starting imports or migrations.

Syncing The synced project is copying its initial table selection or catching up with source changes. Follow synchronization progress from the project overview.

Ready Provisioning is complete. Standard projects have database access; synced projects have completed their initial synchronization and continue receiving source changes. Continue with the workflows available for the selected project type.

Read-only Reads may continue, but writes are restricted for the reason shown in Runtime. Pause imports, migrations, schema changes, and configuration writes; address the displayed cause.

Failed Provisioning did not complete. Review the failure and retry availability described below.

Deleting Permanent deletion is in progress. Do not attempt new project work.

Deleted The project and its associated resources have been removed. Create a new project if a replacement is required.

For a standard project, the overview reports Database and Pooler status

alongside the project status. For a synced project, the overview reports

synchronization state, progress, table status, and freshness.

Recover from a provisioning failure

Polygres automatically retries failures that are classified as retryable. A failed project may therefore move back into Provisioning without manual action.

When the dashboard makes a manual retry available:

Review the failure message and any next-retry time.

Select Retry provisioning only after the action becomes available.

Keep the overview open while the project returns to Provisioning .

Confirm that the project, database, and pooler all reach Ready .

Manual retries are limited and can have a cooldown. When retry is unavailable, wait until the displayed retry time rather than creating duplicate projects. For a non-retryable failure or exhausted retries, preserve the request ID or error details shown in the dashboard and contact Polygres support.

Use the project overview as the launch point

After the project is ready, its organization-scoped pages cover the main product workflows:

Connect ( /{organization}/{project_id}/connect ) for API access and, for managed database projects, database URLs and client examples.

Upgrade ( /{organization}/{project_id}/upgrade ) to move a Nano project to Basic or change an active Basic project’s capacity.

For managed database projects, Tables ( /{organization}/{project_id}/tables ), SQL Editor ( /{organization}/{project_id}/sql ), Import ( /{organization}/{project_id}/import ), and Migrations ( /{organization}/{project_id}/migrations ) provide database work surfaces. Synced projects do not expose direct SQL, import, or migration surfaces.

Workspace ( /{organization}/{project_id}/workspace ) for the visual graph-centered project view.

Graph ( /{organization}/{project_id}/workspace/graph ), AI Context (Vector) ( /{organization}/{project_id}/workspace/context ), and Text Search ( /{organization}/{project_id}/workspace/text-search ) for retrieval setup. The AI Context (Vector) page adds a Legacy submenu for standard projects with existing registrations.

Settings ( /{organization}/{project_id}/settings ) for rename, Project API Key, Runtime, and deletion.

Review runtime and version status

The overview can show update notices for the project’s pgGraph or pgvector component. An Update available notice includes a target version and a Review update action that leads to project settings. Runtime changes are operational actions, not a prerequisite for ordinary data browsing unless the dashboard says otherwise.

Use Settings > Runtime to check project, database, and pooler state, tier, hosts, storage usage, measurement time, and any read-only reason. See Project settings and operations for the full operational workflow.

Rename or delete a project

Renaming changes the dashboard display name but not the project ID used in links and application configuration. Deletion permanently destroys the database, indexes, and Project API Keys. Perform either action from Settings ( /{organization}/{project_id}/settings ), following Project settings and operations .

Project deletion allows up to 30 authenticated attempts in a rolling 24-hour window. Separate limits apply to the user, the user and project together, and the project across all users. The most restrictive applicable limit is enforced. An authenticated request consumes quota before the deletion handler runs, so a request that later fails can still count. If the API returns RATE_LIMITED , wait for the duration in the Retry-After response header before trying again.

Project settings and operations

Open Settings ( /{organization}/{project_id}/settings ). The page is divided into General , Project API Key , and Runtime .

Rename a project

Open General .

Edit Project name . The value must contain 1 to 80 characters.

Select Save .

The new name appears throughout the dashboard. The project ID does not change, so organization-scoped links and existing application configuration continue to identify the same project.

Use the project ID shown under the name when you need an unambiguous support or configuration reference.

Reset the database password

Use the database-password reset action in Settings when rotating application credentials:

Confirm that each application, migration runner, and database tool can be updated immediately after rotation.

Select Reset database password , enter RESET , and confirm the reset.

Select Reveal new password in the reset dialog to view the new password.

Update the pooled and direct URLs in trusted secret stores.

Confirm application and migration connections with the rotated credential.

The new password takes effect immediately for both pooled and direct database connections. You can also reveal the current password later from Connect.

Inspect Runtime

Open Runtime to review the operational fields that matter before a deployment, import, or migration:

Field How to use it

Project status Confirms the overall lifecycle state, such as provisioning, ready, read-only, failed, or deleting.

Database Confirms whether native Postgres is available.

Pooler Confirms whether pooled application connections are available.

Tier Identifies the active tier whose project, storage, import, and retrieval limits apply.

Pooled host Matches the host used for ordinary application traffic.

Direct host Matches the host used for migrations, bulk tools, and direct sessions.

Storage Shows measured usage, the tier limit when available, and when the measurement was checked.

Read-only reason Explains why writes are currently restricted.

Runtime versions Shows Postgres, pgGraph, pgvector, and pgContext versions. pgContext shows Not installed when the runtime has no version metadata.

For a standard project, application database access begins when the required

Project, Database, and Pooler components are Ready .

For a synced project, retrieval begins when the project is Ready , the

required tables have completed synchronization, and the selected retrieval

configuration is ready.

Respond to provisioning status

During Provisioning , the overview refreshes status every few seconds while the database, pooler, and project runtime come online. Avoid imports, migrations, and application cutover until all required components are ready.

Polygres can automatically retry retryable provisioning failures. When a project remains Failed and the dashboard offers Retry provisioning :

Read the failure message and next-retry time.

Wait for any cooldown to end.

Select the retry action once.

Follow the project back through Provisioning .

Confirm the database and pooler reach Ready .

The retry action is not always available. Manual retries are limited, and some failure classes require support. Keep the dashboard’s request ID and failure details when escalation is needed.

Work with read-only mode

A Read-only mode alert appears on the project overview and the reason appears in Runtime . While it is active:

continue only with reads that the dashboard permits,

pause CSV, SQL, and pg_dump imports,

pause row edits and schema changes,

do not apply migrations,

do not assume a retrieval configuration change or index rebuild will succeed, and

review storage usage and the exact displayed reason before retrying writes.

Read-only mode protects project integrity. Repeated writes do not clear it and can obscure the original problem.

Respond to scheduled platform maintenance

The dashboard displays a notice before scheduled maintenance begins.

During read-only maintenance , you can continue viewing project data, but imports, migrations, configuration changes, and other updates are paused.

During full maintenance , the dashboard, API, and database may be temporarily unavailable.

Wait for the maintenance notice to clear before resuming work. Applications should retry with backoff, reconnect after service is restored, and confirm the outcome of any interrupted transaction before submitting it again.

Review runtime and extension versions

The project overview can show separate Update available notices for pgGraph and pgvector . Each notice identifies the available target version and provides Review update .

Treat an update notice as an operational review item:

Record the component and target version.

Review application, migration, and retrieval dependencies.

Open project settings from Review update .

During beta, coordinate the actual runtime update with Polygres support; the dashboard does not present it as an ordinary self-service schema action.

After an update, retest representative graph, vector, and hybrid queries.

An update notice does not mean the current runtime is automatically unusable. Follow any urgency or compatibility message shown with the notice.

Manage the Project API Key

Open Project API Key to create and revoke credentials for server-side retrieval and pgContext Runtime resource management.

Select New Project API Key .

Give the key a name that identifies its use, such as production-backend .

Select Create Project API Key .

Copy the full value immediately into a secret manager. It is shown only once and cannot be retrieved again.

To revoke a key, select Revoke , read the immediate-impact warning, type the exact displayed key prefix, and confirm. Applications using that key lose access immediately.

A Project API Key is not the database password. See Security basics before distributing either credential.

Delete a project permanently

Deletion permanently removes the Polygres project, its indexes, retrieval

configuration, and Project API Keys.

For a synced project, the source PostgreSQL tables and their application data

remain in the source database.

Open General and locate Danger zone .

Select Delete project .

Read the deletion warning.

Type the exact project name into the confirmation field.

Confirm deletion.

After the request is accepted, the dashboard returns to the organization’s project list while deletion completes. Before deleting a production project, export any required data, stop connected applications and jobs, and record which credentials and integrations must be retired.

Operational response guide

Symptom First dashboard check Next action

App cannot connect Project, Database, and Pooler status Compare the app’s connection type with Connect your app .

Import or migration will not start Read-only reason and active import jobs Resolve read-only state or wait for/cancel the active job.

Graph query is blocked Graph build status Correct setup and rebuild from Graph.

Legacy vector or hybrid retrieval is blocked Persisted Legacy vector registration and effective readiness Select a persisted enabled Legacy registration that is effectively Ready . HNSW requires its exact physical index to be Ready; index_kind: none can be Ready for exact scan without HNSW.

AI Context retrieval uses an unexpected vector Collection, exact vector name, and default badges Check the selected pgContext collection. An omitted vector name uses that collection’s default vector; this is independent of the project’s default collection.

Text retrieval is blocked Text configuration index status Review the TSVector or Fuzzy configuration and test it through the supported API or SDK surface.

Provisioning failed Retry availability and next-retry time Use the allowed retry or contact support with the failure details.

Storage is near its limit Runtime storage measurement and tier Remove unnecessary data or use an appropriate tier before writes are restricted.

Extension update notice appears Component and target version Review compatibility and coordinate the beta update process.

For data-operation details, see Load and manage data . For retrieval state, see Configure retrieval .
