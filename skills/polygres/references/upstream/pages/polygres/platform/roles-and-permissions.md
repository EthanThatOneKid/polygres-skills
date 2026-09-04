source: https://docs.evokoa.com/polygres/platform/roles-and-permissions
title: Roles and permissions | Polygres
source_hash: 1a6ad7ff8494f9b4f0674d68a1d617fa40b7e141a3326cfdb0029ab0db1da232
discovered_from: https://docs.evokoa.com/polygres

# Roles and permissions | Polygres

Roles and permissions

Polygres provides four fixed organization roles: owner , admin , developer ,

and viewer . Each role carries a consistent permission set across the

dashboard and API.

An organization admin is not the same as a Polygres platform operator. Platform

operator access is controlled separately by the user profile’s operator type.

Organization member management

Behavior Owner Admin Developer Viewer

List organization members Yes Yes Yes Yes

List pending organization invitations Yes Yes No No

Add a member directly Yes Yes No No

Invite a member Yes Yes No No

Revoke an invitation Yes Yes No No

Change a member role Yes Yes No No

Remove another member Yes Yes No No

Invite the owner role by email No No No No

Additional current constraints:

Email invitations can assign admin , developer , or viewer . A signed-in user

whose email matches a pending invitation can accept it; acceptance is not gated by an

existing role in the target organization.

Direct member-add and role-update requests accept all four role values.

A caller cannot invite their own email or remove their own membership.

Listing active members requires an active organization membership. Missing

or inactive membership is returned as ORG_NOT_FOUND .

Member and invitation mutations require an owner or admin. Developer and

viewer attempts to use those administrative routes return

ORG_PERMISSION_DENIED .

Project permissions

For each project action, Polygres resolves the active organization membership

and checks the corresponding named permission.

Permission used by current routes Representative operations

project:create Create an eligible Free project. Owners and admins can also create Paid projects.

project:read Read project metadata/status, connection metadata, API-key metadata, tables, and rows.

runtime:read Read project runtime version and visible update paths.

project:update Rename a project, reveal its database password, and manage API keys.

project:sql:execute Run SQL through the project SQL surface.

project:delete Delete a project.

project:retry_provisioning Retry eligible failed provisioning.

graph:read Discover graph candidates, read graph status/system settings, and run graph retrieval with a dashboard session.

graph:manage Save, build, maintain, or change graph configuration/system settings.

vector:read Discover vectors and read vector configuration metadata.

vector:manage Update, delete, or index previously registered vector configurations; current dashboard-session vector and hybrid query routes also request this permission. New vector setup uses context:manage .

text:read Read text configuration metadata.

text:manage Create, update, or delete text configurations.

context:read Read Context capabilities, sources, collections, status, diagnostics, points, operations, aggregates, and retrieval results.

context:manage Create and update collections, filters, points, indexes, reconciliation jobs, and eligible operation actions.

imports:read List and inspect import jobs.

imports:manage Preview, start, and cancel imports.

migrations:read List and inspect migrations.

migrations:manage Create and apply migrations.

Role permission summary

Owners and admins receive every organization and project permission.

Developers receive day-to-day project permissions, including SQL, imports,

migrations, graph, vector, text, pgContext, and runtime access.

Viewers receive read access to projects, imports, migrations, graph, vector,

text, pgContext, and runtime status.

The dashboard uses the backend’s effective permissions for the active member

and project.

Billing and Paid projects

Billing belongs to the organization. Owners and admins manage it from the

organization’s Billing page.

Action Owner Admin Developer Viewer

View billing and credit history Yes Yes No No

Add or update the organization payment method Yes Yes No No

Purchase credit top-ups Yes Yes No No

Create a Paid project or upgrade Nano to Basic Yes Yes No No

Increase limits now or schedule lower limits for a Paid project Yes Yes No No

Create an eligible Free project Yes Yes Yes No

Developers and viewers who encounter a Paid-project control can see why the

action is unavailable. An owner or admin can make the billing change. See

Billing and credits for the organization workflow.

Synced-project permissions

Action Owner Admin Developer Viewer

View sync status, progress, tables, and retrieval readiness Yes Yes Yes Yes

Create a synced project Yes Yes Yes No

Update the synchronized table selection Yes Yes Yes No

Pause, resume, or retry synchronization when the action is shown Yes Yes Yes No

Delete a synced project Yes Yes No No

The project overview presents the actions available to the signed-in member for

the project’s current synchronization state.

Diagnosing a permission denial

Call GET /me and verify the expected organization and an active membership.

Confirm that the project belongs to that organization.

Any active member can list active organization members. For pending invitations or membership changes, use an owner or admin session.

For a project route, record the route, project ID, returned error code, and request ID.

Do not retry a 403 with an API key when the route is dashboard-only.
