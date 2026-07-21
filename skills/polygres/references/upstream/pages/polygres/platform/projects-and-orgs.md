source: https://docs.evokoa.com/polygres/platform/projects-and-orgs
title: Projects and Organizations | Polygres
source_hash: 69c39f256603ce2311d7d0ae565f0f488436742fe8361ca241437ef70393fe20
discovered_from: https://docs.evokoa.com/polygres

# Projects and Organizations | Polygres

Projects and Organizations

Account onboarding

Create and activate your account

Open Sign up and register with the email address you intend to use for Polygres. Enter and confirm a password of at least eight characters, then accept the Terms of Service and acknowledge the Privacy Policy.

If an organization invitation exists for that authenticated address, review the available invitation or invitations before creating a new organization.

Otherwise, complete account setup by entering your organization name. A display name is optional.

Submit the form. When shared-tier capacity is available, Polygres creates the organization and opens its dashboard.

If shared-tier capacity is unavailable, the dashboard shows Pending approval until capacity becomes available.

You can also choose Continue with email on the login page. Its secure link can sign in an existing account or begin a new passwordless account. If password signup detects an existing account, Polygres sends the same privacy-preserving sign-in link instead of disclosing account details.

Join an organization through an invitation

An invitation is tied to an email address and an organization role.

Open the invitation link from your email. The link opens Polygres signup; it does not authenticate you by itself.

Sign in with the invited email address, or create an account with that same address.

Review the pending organization invitations for the authenticated address. If several exist, select the one organization you intend to join.

Select Accept invitation . If the address is not verified, use the verification message Polygres sends and finish from the link in that message.

If the email was already verified, acceptance completes immediately. Otherwise, verification activates the selected membership. In either case, Polygres closes the other pending invitations for that email and opens the selected organization.

You do not need to enter an invitation code in the Members page. The dashboard resolves invitations from the authenticated email, not from the editable email shown in a signup URL. When an invitation does not appear, first confirm that the signed-in email exactly matches the invited address and that the invitation has not expired, been revoked, or been replaced.

If you change your mind after selecting an invitation but before verifying, choose Cancel invitation on the verification page. This declines the pending organization invitations for that email and returns the account to normal organization setup.

Understand account status pages

Dashboard state What it means What to do

Verify email A selected organization invitation or project-creation flow requires proof of the account email. Use the newest verification email. If an invitation is selected, you can cancel it from this page.

Onboarding Account setup still needs an organization name. Complete and submit the account-setup form.

Pending approval Account setup is complete, but shared-tier capacity is currently unavailable. Keep using the same account; the organization becomes available when capacity is restored.

Choose tier The account is active but does not yet have an active tier. Select a tier to continue to projects.

Rejected The account was not approved. Follow the contact guidance shown on that page.

Suspended Access has been paused. Follow the support guidance shown on that page; project access remains blocked while suspended.

After onboarding

Your next destination depends on how you joined:

A new account can open its organization overview and create a project .

An invited account can open Members ( /{organization}/members ) to confirm its role, then use the projects owned by that organization.

An organization administrator can continue with members, roles, and invitations .

Organizations, members, and roles

Treat the organization as the ownership boundary

Every Polygres project belongs to an organization. The organization is where you manage members and roles, and its slug is part of every organization-scoped project link. For example, a project’s Tables page is /{organization}/{project_id}/tables .

Open the organization overview ( /{organization} ) to see organization details such as its name, organization ID, billing status, tier, and project count. Open Projects ( /{organization}/projects ) to work with the projects that organization owns.

Membership changes affect access to organization-owned projects. They do not transfer a project to a different organization.

Understand the roles

Polygres uses four organization roles:

Role Membership behavior in the dashboard

Owner Organization steward. Owners can administer membership. The current Members workflow protects the owner from routine role changes and removal.

Admin Can administer members and pending invitations alongside the owner.

Developer Intended for builders working with organization projects. It does not grant access to membership administration.

Viewer Intended for teammates who need a more limited, viewing-oriented role. It does not grant access to membership administration.

On the Members page, only Owner and Admin can view and perform membership-management actions. Project actions remain subject to the permissions attached to each role.

Invite a member

Open Members ( /{organization}/members ).

Select Invite member .

Enter the teammate’s email address.

Choose Admin , Developer , or Viewer . Developer is selected by default. The invitation flow does not assign the Owner role.

Send the invitation.

You cannot invite your own signed-in email address. A new invitation appears in the pending invitations area with its role and expiration.

Replace an existing pending invitation

When the same email already has a pending invitation, the dashboard asks whether to replace it. Choose Send new invite to refresh the invitation, selected role, expiration, and delivery attempt. This is useful when the first message was lost, delivery failed, or the intended role changed.

Accept an invitation

The recipient should open the email link and sign in or register with the exact invited email address. The invitation email opens signup and does not authenticate the recipient. After authentication, the dashboard lists every pending organization invitation for that address. The recipient chooses one, then verifies the address if prompted. Acceptance activates the membership immediately for an already verified address; otherwise verification activates it. Polygres then closes the other pending invitations for the same email. See Account onboarding for the complete sequence.

An invitation may be pending , accepted , declined , expired , or revoked . If an expired or revoked link is opened, an owner or admin must send a new invitation.

Change a member’s role

Open Members ( /{organization}/members ).

Find the active member.

Use the role control to select Admin , Developer , or Viewer .

Confirm that the updated role appears in the member row.

The Members workflow does not use routine role changes to transfer ownership. It also prevents a signed-in administrator from changing their own role through the row action. Plan owner changes through your organization’s supported administrative process rather than trying to work around those protections.

Revoke a pending invitation

In Members , find the pending invitation.

Select its remove or trash action.

Confirm the revocation.

The invitation can no longer be accepted. Send a new invitation if access is needed later.

Remove a member

In Members , find the active member.

Select the remove or trash action.

Confirm removal.

Removal cuts off that membership’s organization access. The dashboard prevents removing yourself and protects the organization owner from the routine remove action. Reassign ongoing work before removing a developer or admin.

Recognize member states

Active membership rows can reflect states such as active , invited , or suspended . Pending invitations are managed separately from active members. When access does not match expectations, check both the member’s role and state before sending another invitation.

Continue administering the organization

Create and manage projects owned by this organization.

Review security basics before granting production access.

Open Project settings and operations for project-level runtime and credential administration.

Projects

Create a project in an organization

A project cannot exist outside an organization. Confirm the organization slug in the dashboard URL before creating it.

Open New project ( /{organization}/new ) from the target organization.

Enter a project name between 1 and 80 characters.

Select Create project .

The dashboard opens the organization-scoped project overview while Polygres provisions its dedicated Postgres runtime, database, and pooler.

Project creation can be blocked when the organization’s assigned tier has reached its project limit. Delete an unused project or change the applicable tier before trying again.

Follow provisioning

While the project shows Provisioning , keep the overview open or return to it later. The dashboard refreshes status while the database, pooler, and project runtime come online.

Project state What it means Recommended action

Provisioning Infrastructure is still being created or retried. Wait for the automatic status refresh. Do not start imports or migrations yet.

Ready The database and pooler are available for normal project work. Connect an app, load data, and configure retrieval.

Read-only Reads may continue, but writes are restricted for the reason shown in Runtime. Pause imports, migrations, schema changes, and configuration writes; address the displayed cause.

Failed Provisioning did not complete. Review the failure and retry availability described below.

Deleting Permanent deletion is in progress. Do not attempt new project work.

Deleted The project and its associated resources have been removed. Create a new project if a replacement is required.

The project overview also reports Database and Pooler status independently. A project is not ready for an application just because one component is ready.

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

Connect ( /{organization}/{project_id}/connect ) for database URLs, client examples, and API access.

Tables ( /{organization}/{project_id}/tables ), SQL Editor ( /{organization}/{project_id}/sql ), Import ( /{organization}/{project_id}/import ), and Migrations ( /{organization}/{project_id}/migrations ) for data work.

Workspace ( /{organization}/{project_id}/workspace ) for the graph-centered project view.

Graph ( /{organization}/{project_id}/workspace/graph ), Vector ( /{organization}/{project_id}/workspace/vector ), and Text Search ( /{organization}/{project_id}/workspace/text-search ) for retrieval setup.

Query Helper ( /{organization}/{project_id}/workspace/query ) for dashboard testing.

Settings ( /{organization}/{project_id}/settings ) for rename, Project API Key, Runtime, and deletion.

Review runtime and version status

The overview can show update notices for the project’s pgGraph or pgvector component. An Update available notice includes a target version and a Review update action that leads to project settings. Runtime changes are operational actions, not a prerequisite for ordinary data browsing unless the dashboard says otherwise.

Use Settings > Runtime to check project, database, and pooler state, tier, hosts, storage usage, measurement time, and any read-only reason. See Project settings and operations for the full operational workflow.

Rename or delete a project

Renaming changes the dashboard display name but not the project ID used in links and application configuration. Deletion permanently destroys the database, indexes, and Project API Keys. Perform either action from Settings ( /{organization}/{project_id}/settings ), following Project settings and operations .

Project settings and operations

Open Settings ( /{organization}/{project_id}/settings ). The page is divided into General , Project API Key , and Runtime .

Rename a project

Open General .

Edit Project name . The value must contain 1 to 80 characters.

Select Save .

The new name appears throughout the dashboard. The project ID does not change, so organization-scoped links and existing application configuration continue to identify the same project.

Use the project ID shown under the name when you need an unambiguous support or configuration reference.

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

A healthy application path normally requires Project , Database , and Pooler to be Ready . A direct migration may not depend on the pooler in the same way, but it still requires a ready, writable database.

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

Open Project API Key to create and revoke credentials for server-side retrieval calls.

Select New Project API Key .

Give the key a name that identifies its use, such as production-backend .

Select Create Project API Key .

Copy the full value immediately into a secret manager. It is shown only once and cannot be retrieved again.

Revoke a key when its application is retired or the value may be exposed.

A Project API Key is not the database password. See Security basics before distributing either credential.

Delete a project permanently

Deletion destroys the project database, indexes, and Project API Keys. It cannot be undone.

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

Vector or hybrid query is blocked Default vector configuration and HNSW status Populate embeddings, select a default, or reindex.

Text query is blocked Text configuration index status Review and save the TSVector or Fuzzy configuration again.

Provisioning failed Retry availability and next-retry time Use the allowed retry or contact support with the failure details.

Storage is near its limit Runtime storage measurement and tier Remove unnecessary data or use an appropriate tier before writes are restricted.

Extension update notice appears Component and target version Review compatibility and coordinate the beta update process.

For data-operation details, see Load and manage data . For retrieval state, see Configure retrieval .
