source: https://docs.evokoa.com/polygres/reference/error-codes
title: Error codes | Polygres
source_hash: 0c587c5f735f6a3cf6b1473881c4558f13613dd8d8bc2cb7c0faefdb5d126982
discovered_from: https://docs.evokoa.com/polygres

# Error codes | Polygres

Error codes

Error responses use this shape:

{

"request_id" : "req_xxx" ,

"error" : {

"code" : "ERROR_CODE" ,

"message" : "Description" ,

"details" : {}

}

}

Record request_id , the HTTP status, and safe values from details . Statuses below

are listed only when the referenced route fixes them explicitly; — means to use the

status returned with the response.

Authentication and access

Code Status Meaning First action

AUTH_REQUIRED 401 The bearer header is missing or the dashboard token cannot be validated. Sign in again and send a current bearer token.

NO_SESSION Client The dashboard client has no session token. Sign in before retrying.

INVALID_TOKEN / TOKEN_EXPIRED / SESSION_EXPIRED 401 or client The dashboard session is no longer usable. Refresh or reauthenticate; do not retry with the same token indefinitely.

AUTH_MODE_NOT_ALLOWED 403 A Polygres API key was used on a dashboard-only route. Use a dashboard session.

AUTH_NOT_CONFIGURED 503 Dashboard JWT validation is unavailable or misconfigured. Retry once; contact support if it persists.

AUTH_ACTION_INVALID / AUTH_ACTION_EXPIRED 400 An email sign-in, verification, invitation, or recovery action is malformed, already consumed, or expired. Start the flow again and use the newest email.

AUTH_INVALID_CREDENTIALS 401 The email or password is incorrect. Correct the credentials or use the passwordless sign-in flow.

EMAIL_NOT_VERIFIED 403 The requested account or project action requires a verified email address. Use the dashboard verification flow and the newest verification message.

APPROVAL_REQUIRED 403 The user profile is not active. Follow the current dashboard account gate for verification, account setup, capacity, or tier selection.

LEGAL_ACCEPTANCE_REQUIRED 422 The account has no current durable acceptance of the Terms of Service and Privacy Policy. Return to signup or the account gate and record the required acceptance.

EMAIL_VERIFICATION_PROFILE_NOT_FOUND 404 Verification cannot find the account profile. Sign out and start signup or sign-in again; contact support if the account is otherwise visible.

EMAIL_VERIFICATION_LINK_FAILED 503 Polygres could not create or deliver a verification link. Retry once from Resend verification email , then contact support with the request ID.

EMAIL_VERIFICATION_EVIDENCE_MISMATCH 403 The verification continuation does not match the authenticated account. Sign out, use the intended account, and open a newly requested verification message.

ONBOARDING_INVALID 400 Account setup or a legacy onboarding payload contains an unsupported value. Submit the organization name and other values offered by the current account-setup form.

ONBOARDING_ALREADY_FINAL 409 Account setup is already active, rejected, or suspended and can no longer be resubmitted. Follow the current account state; contact support when review is required.

API_KEY_INVALID — The API key is malformed, unknown, or revoked. Check the key source and project; create and deploy a replacement if needed.

NETWORK_ERROR Client The dashboard could not reach the API. Check network access and API availability, then retry.

Projects

Code Status Meaning First action

PROJECT_ID_INVALID 422 The external project ID does not match p[a-z0-9]{23} . Copy the ID from the project page or API response.

PROJECT_NOT_FOUND 404 The project does not exist, is deleted, or is not visible to the current user. Verify the project ID, organization membership, and selected account.

PROJECT_NOT_READY 409 The route requires project status ready . Check project status and resolve provisioning, deletion, suspension, or read-only state.

TIER_REQUIRED 403 No effective tier is assigned. Select or restore the organization/account tier.

TIER_NOT_FOUND 404 The assigned tier is missing or inactive. Refresh tier state; contact support if the assigned tier remains unavailable.

PROVISIONING_NOT_CONFIGURED 503 The environment cannot provision or delete project runtimes. Contact support; repeated client retries do not fix this configuration error.

PROVISIONING_RETRY_UNAVAILABLE 409 Manual retry is not valid for the current state, retry count, or retry window. Retry only when project status is failed and can_retry_provisioning is true.

PROJECT_RUNTIME_NOT_FOUND 409 The project’s runtime version record is missing. Refresh runtime status; contact support with the project and request IDs.

ID_INVALID 422 A UUID-like resource ID, such as a job, migration, or key ID, is malformed. Copy the ID from its list or detail response.

Organizations and invitations

Code Status Meaning First action

ORG_NOT_FOUND 404 The organization is missing or the user is not an active member. Verify the organization ID and membership returned by GET /me .

ORG_PERMISSION_DENIED 403 The current role cannot manage members or invitations. Use an owner or admin account for current member-management routes.

ORG_SELF_INVITE_NOT_ALLOWED 400 The caller tried to invite their own email. Invite a different email address.

ORG_SELF_REMOVE_NOT_ALLOWED 400 The caller tried to remove their own membership. Have another owner or admin perform the intended membership change.

INVITATION_NOT_FOUND / ORG_INVITATION_NOT_FOUND — The invitation ID is unknown or no longer available. Sign in with the invited email, open the latest invitation link, or request a new invitation.

INVITATION_NOT_PENDING 409 The invitation was already accepted, declined, revoked, expired, or replaced. Refresh the invitation list; request a new invitation when access is still needed.

INVITATION_EMAIL_MISMATCH / ORG_INVITATION_EMAIL_MISMATCH — The signed-in email does not match the invitation. Sign in with the invited email address.

INVITATION_EXPIRED / ORG_INVITATION_EXPIRED — The invitation or its email action is past its expiry. Ask an owner or admin to send a new invitation.

INVITATION_DELIVERY_FAILED 503 The durable invitation exists, but email delivery failed. An owner or admin can replace or resend the pending invitation; preserve the request ID if delivery repeatedly fails.

ORG_MEMBERSHIP_LIMIT_EXCEEDED — Accepting the invitation would exceed the supported membership constraint. Review current membership and tier state; contact support if no limit is visible.

DASHBOARD_PUBLIC_BASE_URL_INVALID / DASHBOARD_PUBLIC_BASE_URL_REQUIRED 503 Invitation link generation cannot resolve the dashboard origin. Contact support.

Imports

Code Status Meaning First action

IMPORT_LIMIT_EXCEEDED 413 The declared file size exceeds the effective tier cap. Check GET /tiers ; split or reduce the file.

IMPORT_CONCURRENCY_LIMIT 409 Another import is queued or running for the project. Wait for or cancel the active job.

IMPORT_FILE_INVALID 400 The staged job or CSV metadata does not match the requested import. Recreate the preview and verify headers, types, mapping, and job ID.

IMPORT_CANCELLED 409 A cancelled preview job was submitted for execution. Create a new preview or import job.

IMPORT_SQL_EMPTY — The SQL import body is empty. Submit a non-empty SQL file or body.

IMPORT_JOB_NOT_FOUND — The job ID is unknown for the project. Confirm both project ID and job ID.

IMPORT_NOT_CANCELLABLE — The job is terminal or cannot be cancelled in its current phase. Refresh the job and act on its current status.

IMPORT_RUNTIME_NOT_CONFIGURED — Import execution is unavailable for the runtime. Retry once; contact support if it persists.

Migrations

Code Status Meaning First action

MIGRATION_NOT_FOUND — The migration ID is unknown for the project. Confirm both project ID and migration ID.

MIGRATION_LOCK_BUSY — Another migration operation holds the project lock. Wait for the active operation to finish before retrying.

MIGRATION_SQL_CHECKSUM_MISMATCH 409 Stored SQL no longer matches the migration checksum. Do not bypass the check; contact support.

MIGRATION_SQL_BLOCKED 400 The migration contains a statement denied by SQL safety policy. Use the policy details to rewrite the migration.

MIGRATION_RUNTIME_NOT_CONFIGURED — Migration execution is unavailable for the runtime. Retry once; contact support if it persists.

SQL and validation

Code Status Meaning First action

SQL_QUERY_BLOCKED 400 SQL editor policy rejected a statement. Review the denied statement and policy details.

SQL_IMPORT_BLOCKED Job or 400 SQL import policy rejected a statement. Inspect the failed job’s error_code , error_message , and validation details.

SQL_QUERY_FAILED 400 PostgreSQL executed the request but returned an error. Use sqlstate , detail , hint , and position from details .

DATA_PLANE_SQL_FAILED — Import or migration SQL failed in the project runtime. Inspect the job or migration error and failed statement context.

IDENTIFIER_INVALID 400 A schema, table, column, relationship, filter, or language identifier is invalid. Use an identifier matching [A-Za-z_][A-Za-z0-9_]* .

LIMIT_OUT_OF_RANGE 400 The table viewer limit is outside 1..500 . Send a valid limit.

VALIDATION_ERROR 422 The request body or parameter shape is invalid. Compare the request with the route contract and remove unknown fields.

Retrieval

Graph

Code Status Meaning First action

GRAPH_CONFIGURATION_EMPTY 409 No graph tables are registered. Save a non-empty graph configuration.

GRAPH_CONFIGURATION_INVALID 400 The graph table or ID-column definition is inconsistent. Supply exactly one id_column or non-empty id_columns per registered table.

GRAPH_BUILD_FAILED 400 Graph registration or build failed. Inspect invalid_reason and retry after correcting the configuration.

GRAPH_NOT_READY 409 Graph build status is not ready . Check graph status; build or rebuild as needed.

GRAPH_FILTER_INVALID 400 A graph filter key or value is invalid. Use registered filter columns and scalar exact-match values.

GRAPH_COLUMN_NOT_SYNCABLE — A selected graph column cannot be synchronized. Remove or correct the columns listed in details.columns .

Vector

Code Status Meaning First action

VECTOR_CONFIGURATION_NOT_FOUND 404 The named/default vector configuration does not exist. Pass a valid configuration name or create/set a default.

VECTOR_NOT_READY 409 An HNSW configuration’s index is not ready . Reindex and check index_status and index_error .

VECTOR_INDEX_FAILED 400 Vector index creation, update, or reindex failed. Verify table, column, dimensions, metric, and index error; retry after correction.

VECTOR_SEARCH_INVALID 400 Conflicting vector bounds were supplied. Send either max_distance or min_similarity , not both.

VECTOR_FILTER_INVALID 400 A vector or hybrid filter key/value is invalid. Use configured filter columns and scalar exact-match values.

Text

Code Status Meaning First action

TEXT_CONFIGURATION_NOT_FOUND 404 The named text configuration does not exist. Use a valid configuration name.

TEXT_CONFIGURATION_NOT_READY 409 The text index status is not ready . Correct and update or recreate the configuration.

TEXT_CONFIGURATION_KIND_MISMATCH 400 A fuzzy configuration was used on the tsvector route or vice versa. Call the route matching search_kind .

TEXT_CONFIGURATION_INVALID 400 The configuration’s columns do not match its search kind. For tsvector , set only tsvector_column ; for fuzzy, set only text_column .

TEXT_INDEX_FAILED 400 Text index creation or rebuild failed. Verify the table and selected columns, then update or recreate the configuration.

TEXT_QUERY_EMPTY 400 The query is empty after trimming. Send a non-empty query of at most 2,000 characters.

TEXT_FILTER_INVALID 400 A text filter key/value is invalid. Use configured filter columns and scalar exact-match values.

Hybrid warning

HYBRID_WEIGHTS_IGNORED is a warning, not a failed request. Joint ranking uses

Reciprocal Rank Fusion, so supplied weights are currently ignored.

Rate limits

Response Meaning First action

HTTP 429 One of the applicable IP, user, user-project, API-key, or project windows is exhausted. Honor Retry-After when present and retry with backoff. Do not fan out immediate retries.

The current references do not define a stable user-facing error-code string for every

429 ; branch on the HTTP status.

Runtime and service configuration

Code Status Meaning First action

DATA_PLANE_NOT_CONFIGURED 503 Query execution is unavailable for the project runtime. Confirm the project is operational, retry once, then contact support.

PROVISIONING_NOT_CONFIGURED 503 Runtime provisioning/deletion is unavailable in the environment. Contact support.

AUTH_NOT_CONFIGURED 503 Dashboard authentication validation is unavailable. Contact support if a retry does not recover.

DASHBOARD_PUBLIC_BASE_URL_INVALID / DASHBOARD_PUBLIC_BASE_URL_REQUIRED 503 Organization invitation URL generation is misconfigured. Contact support.

PROJECT_RUNTIME_NOT_FOUND 409 Runtime catalog metadata for the project is missing. Contact support with the project and request IDs.
