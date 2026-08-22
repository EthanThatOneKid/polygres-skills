source: https://docs.evokoa.com/polygres/platform/organizations
title: Organizations | Polygres
source_hash: dcbdc3fe9adfac487a7000139a919b7a527d0c5a840e3a2a3eda6792000c46e8
discovered_from: https://docs.evokoa.com/polygres

# Organizations | Polygres

Organizations

Every Polygres project belongs to an organization. Organizations define project ownership, membership, roles, billing status, and the tier used when projects are created.

Create and activate your account

Open Sign up and register with the email address you intend to use for Polygres. Enter and confirm a password of at least eight characters, then accept the Terms of Service and acknowledge the Privacy Policy.

If an organization invitation exists for that authenticated address, review the available invitations before creating a new organization.

Otherwise, Polygres completes the normal self-service setup automatically. It creates an organization, assigns the current self-service tier ( Shared Nano ), and opens the dashboard.

If the account reaches Onboarding instead of the organization dashboard, setup is incomplete. Follow the support guidance on that page.

You can also choose Continue with email on the login page. Its secure link can sign in an existing account or begin a new passwordless account. If password signup detects an existing account, Polygres sends the same privacy-preserving sign-in link instead of disclosing account details.

Join an organization through an invitation

An invitation is tied to an email address and an organization role.

Open the invitation link from your email. The link opens Polygres signup; it does not authenticate you by itself.

Sign in with the invited email address, or create an account with that same address.

Review the pending organization invitations for the authenticated address. If several exist, select the one organization you intend to join.

Select Accept invitation . If the address is not verified, use the verification message Polygres sends and finish from the link in that message.

If the email was already verified, acceptance completes immediately. Otherwise, verification activates the selected membership. In either case, Polygres closes the other pending invitations for that email and opens the selected organization.

You do not need to enter an invitation code in the Members page. The dashboard resolves invitations from the authenticated email. When an invitation does not appear, confirm that the signed-in email exactly matches the invited address and that the invitation has not expired, been revoked, or been replaced.

If you change your mind after selecting an invitation but before verifying, choose Cancel invitation on the verification page. This declines the pending invitations for that email and returns the account to normal organization setup.

Understand account status pages

Dashboard state What it means What to do

Verify email A selected organization invitation or project-creation flow requires proof of the account email. Use the newest verification email. If an invitation is selected, you can cancel it from this page.

Onboarding Automatic account or organization setup did not complete. Follow the support guidance on the page.

Pending approval The account or organization requires an administrative decision. Keep using the same account and follow the guidance shown on the page.

Rejected The account was not approved. Follow the contact guidance shown on that page.

Suspended Access has been paused. Follow the support guidance shown on that page. Project access remains blocked while suspended.

Treat the organization as the ownership boundary

The organization slug is part of every organization-scoped project link. For example, a project’s Tables page is /{organization}/{project_id}/tables .

Open the organization overview ( /{organization} ) to see its name, organization ID, billing status, tier, and project count. Open Projects ( /{organization}/projects ) to work with the projects it owns.

Membership changes affect access to organization-owned projects. They do not transfer a project to a different organization.

Understand the roles

Polygres uses four organization roles:

Role Membership behavior in the dashboard

Owner Organization steward. Owners can administer membership. The current Members workflow protects the owner from routine role changes and removal.

Admin Can administer members and pending invitations alongside the owner.

Developer Intended for builders working with organization projects. Developers can list active members but cannot administer membership or invitations.

Viewer Intended for teammates who need a more limited, viewing-oriented role. Viewers can list active members but cannot administer membership or invitations.

Every active organization member can view the active-member list. Only Owner and Admin can view pending invitations or perform membership-management actions. Project actions remain subject to the permissions attached to each role.

Invite a member

Open Members ( /{organization}/members ).

Select Invite member .

Enter the teammate’s email address.

Choose Admin , Developer , or Viewer . Developer is selected by default. The invitation flow does not assign the Owner role.

Send the invitation.

You cannot invite your own signed-in email address. A new invitation appears in the pending invitations area with its role and expiration.

Replace an existing pending invitation

When the same email already has a pending invitation, the dashboard asks whether to replace it. Choose Send new invite to refresh the invitation, selected role, expiration, and delivery attempt.

Accept an invitation

The recipient should open the email link and sign in or register with the exact invited email address. The invitation email opens signup and does not authenticate the recipient. After authentication, the dashboard lists every pending organization invitation for that address. The recipient chooses one, then verifies the address if prompted.

An invitation may be pending , accepted , declined , expired , or revoked . If an expired or revoked link is opened, an owner or admin must send a new invitation.

Change a member’s role

Open Members ( /{organization}/members ).

Find the active member.

Use the role control to select Admin , Developer , or Viewer .

Confirm that the updated role appears in the member row.

The Members workflow does not use routine role changes to transfer ownership. It also prevents a signed-in administrator from changing their own role through the row action.

Revoke an invitation or remove a member

Use the remove or trash action beside a pending invitation to revoke it. The invitation can no longer be accepted. Send a new invitation if access is needed later.

Use the corresponding action beside an active member to remove their organization access. The dashboard prevents removing yourself and protects the organization owner from the routine remove action. Reassign ongoing work before removing a developer or admin.

Recognize member states

Active membership rows can reflect states such as active , invited , or suspended . Pending invitations are managed separately from active members. When access does not match expectations, check both the member’s role and state before sending another invitation.

Continue administering the organization

Create and manage projects owned by this organization.

Review roles and permissions before assigning access.

Review security basics before granting production access.
