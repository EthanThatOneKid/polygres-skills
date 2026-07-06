source: https://docs.evokoa.com/polygres/platform/security-basics
title: Security basics | Polygres
source_hash: 91f7448783b54be9b6294d95489804e0dcc9ac65af2bbc8dd1b32a196582b204
discovered_from: https://docs.evokoa.com/polygres

# Security basics | Polygres

Security basics

Polygres uses three distinct access mechanisms. They are not interchangeable.

The boundary is intentional: setup and administration happen in the dashboard, operational reads and writes happen through PostgreSQL, and retrieval happens through the project API key.

Separate the three credentials

Access mechanism What it authenticates Where it belongs Where it does not belong

Dashboard session A person using the Polygres dashboard, including their organization membership and role. The signed-in user’s browser session. Application environment variables, database clients, copied SDK examples, or shared automation.

Native database password Direct or pooled Postgres access to one project database. A trusted backend, migration runner, approved database tool, or secret manager as part of a database URL. Browser-side application code, public repositories, screenshots, support chats, or retrieval API headers.

Project API Key Server-side Polygres retrieval calls for a project. A backend or trusted worker secret store; generated SDK and API examples reference it through an environment variable. Native Postgres clients, frontend bundles, documentation, or a person’s dashboard login.

An organization role controls what a signed-in person can do in the dashboard. It does not turn that person’s dashboard session into an application credential.

Keep the boundaries clear

The safest default is to treat each Polygres credential as single-purpose:

Dashboard session for people operating the SaaS workspace.

Native database password for pooled or direct PostgreSQL access.

Project API key for backend retrieval calls.

If a workflow seems to require reusing one credential for another job, that is usually a sign the wrong surface is being used.

Protect the dashboard session

Use an individual account rather than sharing one login among teammates.

Verify that the account is in the intended organization before changing members, projects, or credentials.

Assign organization roles from Members ( /{organization}/members ); only owners and admins should perform membership administration.

Sign out on shared or temporary computers.

Treat browser-local SQL and query history as potentially sensitive, even though it is not a shared organization log.

Never copy browser session material into an application. Create a purpose-built Project API Key or use a native database connection instead.

Handle the native database password

The Connect ( /{organization}/{project_id}/connect ) page initially shows <password> in connection strings.

Select Reveal Password only when a trusted destination is ready.

Copy the completed pooled or direct URL into a secret manager or protected local environment.

Select Hide Password or leave the page when finished.

Keep the URL out of source control, issue trackers, screenshots, analytics, and client-side bundles.

Use the Pooled connection for normal application traffic and the Direct connection for migrations, schema work, bulk operations, and incompatible tools. Both use the same class of native database credential and must be protected accordingly.

The revealed password can be requested again by an authorized dashboard user; it is not a one-time display. That makes access to the Connect page itself sensitive.

When you reset the native database password from Settings, Polygres rotates the password immediately and existing direct or pooled connections that use the old password stop working. The reset action does not display the new password automatically and Polygres does not email database passwords. After a reset, use the normal Reveal Password flow from the dashboard to view the new password, then update the affected application secrets and database tools.

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

Stop distributing the exposed value, remove it from logs or repositories where possible, and contact the appropriate Polygres operational channel for credential remediation. Do not attempt to compensate by using a Project API Key in the database URL.

Keep secrets server-side

Generated code in Query Helper > Code references a Project API Key from environment variables. Follow that pattern. A frontend application should call your own backend, and the backend should call Polygres with its secret.

Likewise, a browser application should not receive the native Postgres URL. Put database access behind a trusted server, API, or controlled data-access layer.

Use encrypted database transport

Dashboard-generated database URLs use sslmode=require . Keep SSL enabled. During beta, the connection mode encrypts traffic but does not enable certificate hostname verification. A client that requires strict CA and hostname verification may need a supported compatibility configuration; do not resolve that error by disabling SSL.

Pre-deployment checklist

Every person has an individual dashboard account and the least-powerful suitable organization role.

The application uses a named Project API Key or native database credential for its specific job, never a dashboard session.

The pooled and direct database URLs are stored only in protected server-side environments.

Project API Keys are separated by environment or service and have recognizable names.

No secret appears in source control, frontend bundles, screenshots, SQL text, query history, or documentation.

The team knows how to revoke a Project API Key and how to remove a member or pending invitation.

Production connections keep encrypted transport enabled.
