source: https://docs.evokoa.com/polygres/platform/security-basics
title: Security basics | Polygres
source_hash: 137e096390d9e6bd273dd9a73e623cee669a1d89ea527c4398ffb044c78e1b64
discovered_from: https://docs.evokoa.com/polygres

# Security basics | Polygres

Security basics

Polygres uses distinct access mechanisms for people, standard databases,

synchronized sources, and application retrieval. Each credential has a focused

purpose and a trusted storage location.

Use each credential for its purpose

Access mechanism What it authenticates Where it belongs Where it does not belong

Dashboard session A person using the Polygres dashboard, including their organization membership and role. The signed-in user’s browser session. Application environment variables, database clients, copied SDK examples, or shared automation.

Native database password Direct or pooled Postgres access to one standard project. A trusted backend, migration runner, approved database tool, or secret manager as part of a database URL. Browser-side application code, public repositories, screenshots, support chats, or retrieval API headers.

Source PostgreSQL credential Connects Polygres to the PostgreSQL database used by a synced project. The synced-project setup flow, a protected environment variable, or a secret manager. Frontend code, source control, screenshots, terminal history, logs, documentation, or support messages.

Project API Key Server-side retrieval and pgContext Runtime resource management for one project. A backend or trusted worker secret store; generated SDK and API examples reference it through an environment variable. Native Postgres clients, frontend bundles, documentation, or a person’s dashboard login.

An organization role controls what a signed-in person can do in the dashboard. It does not turn that person’s dashboard session into an application credential.

Keep the boundaries clear

The safest default is to treat each Polygres credential as single-purpose:

Dashboard session for people operating the SaaS workspace.

Native database password for pooled or direct PostgreSQL access to a managed database project. Synced projects do not issue one.

Project API key for backend retrieval and explicit pgContext collection workflows.

If a workflow seems to require reusing one credential for another job, that is usually a sign the wrong surface is being used.

Protect the dashboard session

Use an individual account rather than sharing one login among teammates.

Verify that the account is in the intended organization before changing members, projects, or credentials.

Assign organization roles from Members ( /{organization}/members ); only owners and admins should perform membership administration.

Sign out on shared or temporary computers.

Treat browser-local SQL and query history as potentially sensitive, even though it is not a shared organization log.

Never copy browser session material into an application. Create a purpose-built Project API Key or use a native database connection instead.

Handle the native database password

This section applies only to managed database projects. The Connect ( /{organization}/{project_id}/connect ) page initially shows <password> in connection strings for those projects. Synced projects do not show native connection strings or support direct SQL access.

Select Reveal Password only when a trusted destination is ready.

Copy the completed pooled or direct URL into a secret manager or protected local environment.

Select Hide Password or leave the page when finished.

Keep the URL out of source control, issue trackers, screenshots, analytics, and client-side bundles.

Use the Pooled connection for normal application traffic and the Direct connection for migrations, schema work, bulk operations, and incompatible tools. Both use the same class of native database credential and must be protected accordingly.

The revealed password can be requested again by an authorized dashboard user; it is not a one-time display. That makes access to the Connect page itself sensitive.

When you reset the native database password from Settings, Polygres rotates the password immediately and existing direct or pooled connections that use the old password stop working. The reset action does not display the new password automatically and Polygres does not email database passwords. After a reset, use the normal Reveal Password flow from the dashboard to view the new password, then update the affected application secrets and database tools.

Protect a synchronized source credential

A synced project uses a source PostgreSQL credential during setup and ongoing

synchronization.

For interactive CLI setup, use the hidden connection prompt:

polygres projects create sync "Support Search"

For automation, store the complete URL in a protected environment variable:

export SOURCE_DATABASE_URL = "postgresql://..."

polygres projects create sync "Support Search" \

--connection-env SOURCE_DATABASE_URL

--connection-env receives the environment-variable name, keeping the

connection value in the protected environment.

Use a dedicated source role with access to the selected public tables and the

logical-replication capabilities described in the

PostgreSQL sync setup guides .

When the source credential changes, rotate it with the source provider and

contact Polygres support to update the synchronized connection.

Create and protect a Project API Key

Open Settings ( /{organization}/{project_id}/settings ) and select Project API Key .

Select New Project API Key .

Use a name that identifies one environment or service, such as staging-worker or production-backend .

Copy the full key to a secret manager when it is displayed.

Close the dialog only after the value is stored and recoverable by the intended service owner.

The full Project API Key is shown only once. The dashboard later shows identifying information such as its name and prefix, not the secret value. If the key is lost, revoke it and create a replacement.

Prefer a separate key for each environment or service. This makes revocation targeted and helps the key name explain where it is used.

Revoke access cleanly

When a teammate leaves

Reassign ongoing organization and project work.

Remove the member from Members ( /{organization}/members ), or revoke a still-pending invitation.

Review Project API Keys and database secrets that the person could access outside the dashboard.

Revoke and replace any credential whose confidentiality is uncertain.

Removing organization membership does not automatically erase a secret that was previously copied into an external system.

When a Project API Key may be exposed

Revoke it from Settings > Project API Key .

Create a new named key.

Update the affected server-side service.

Confirm successful retrieval calls, then remove stale copies from deployment systems.

When a database URL may be exposed

Open project Settings and reset the native database password.

Reveal the new password from the Connect page and update each trusted

application, migration runner, and database tool.

Remove the previous URL from repositories, logs, tickets, and deployment

systems.

Confirm that applications connect with the rotated credential, then contact

the Polygres operational channel if your team wants additional assistance.

Keep secrets server-side

Runtime API and SDK examples reference a Project API Key from environment variables. Follow that pattern. A frontend application should call your own backend, and the backend should call Polygres with its secret.

Likewise, a browser application should not receive the native Postgres URL. Put database access behind a trusted server, API, or controlled data-access layer.

Use encrypted database transport

Polygres direct and pooled database endpoints support encrypted transport with certificate authority and hostname verification. Configure your client to use sslmode=verify-full with a trusted CA store.

For libpq 16 or later, use:

sslmode=verify-full&sslrootcert=system

Do not resolve a TLS error by disabling SSL.

Pre-deployment checklist

Every person has an individual dashboard account and the least-powerful suitable organization role.

The application uses a named Project API Key or native database credential for its specific job, never a dashboard session.

The pooled and direct database URLs are stored only in protected server-side environments.

Project API Keys are separated by environment or service and have recognizable names.

No secret appears in source control, frontend bundles, screenshots, SQL text, query history, or documentation.

The team knows how to revoke a Project API Key and how to remove a member or pending invitation.

Production connections keep encrypted transport enabled.

Synced-project source credentials are stored in a protected environment or secret manager.

CLI automation passes source credentials through --connection-env or --password-env .

The source role is scoped to the selected database and synchronization requirements.
