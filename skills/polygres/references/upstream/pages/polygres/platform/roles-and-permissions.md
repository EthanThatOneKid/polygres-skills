source: https://docs.evokoa.com/polygres/platform/roles-and-permissions
title: Roles and permissions | Polygres
source_hash: f396e94651e6829c344143dd33718a586a48a132ebf7f9d93f7b7d75d0baf3c3
discovered_from: https://docs.evokoa.com/polygres

# Roles and permissions | Polygres

Roles and permissions

Polygres organization roles are fixed: owner , admin , developer , and viewer .

The current implementation does not support custom roles, editable permission sets,

or per-member overrides.

An organization admin is not the same as a Polygres platform operator. Platform

operator access is controlled separately by the user profile’s operator type.

Behavior confirmed by the current routes

Behavior Owner Admin Developer Viewer

List organization members Yes Yes No No

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

Member-management routes require an active membership. Missing or inactive

membership is returned as ORG_NOT_FOUND ; developer and viewer access returns

ORG_PERMISSION_DENIED .

Project permissions

Project routes do not authorize by comparing a role name in the route handler. They

request a named permission from the backend after resolving the project’s

organization and the user’s active membership.

Permission used by current routes Representative operations

project:create Create a project within the organization tier limit.

project:read Read project metadata/status, connection metadata, API-key metadata, tables, and rows.

runtime:read Read project runtime version and visible update paths.

project:update Rename a project, reveal its database password, manage API keys, and run SQL in the current route implementation.

project:delete Delete a project.

project:retry_provisioning Retry eligible failed provisioning.

graph:read Discover graph candidates, read graph status/system settings, and run graph retrieval with a dashboard session.

graph:manage Save, build, maintain, or change graph configuration/system settings.

vector:read Discover vectors and read vector configuration metadata.

vector:manage Create, update, delete, or index vector configurations; current dashboard-session vector and hybrid query routes also request this permission.

text:read Read text configuration metadata.

text:manage Create, update, or delete text configurations.

imports:read List and inspect import jobs.

imports:manage Preview, start, and cancel imports.

migrations:read List and inspect migrations.

migrations:manage Create and apply migrations.

The supplied current-implementation references do not expose a complete

role-to-named-permission matrix for project actions. Do not assume that a role has an

action solely from its label. Use the controls shown in the dashboard or the API’s

permission result as the effective behavior for that organization and deployment.

Diagnosing a permission denial

Call GET /me and verify the expected organization and an active membership.

Confirm that the project belongs to that organization.

For member or invitation routes, use an owner or admin session.

For a project route, record the route, project ID, returned error code, and request ID.

Do not retry a 403 with an API key when the route is dashboard-only.
