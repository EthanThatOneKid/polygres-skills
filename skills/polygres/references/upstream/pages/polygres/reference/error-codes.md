source: https://docs.evokoa.com/polygres/reference/error-codes
title: Error codes | Polygres
source_hash: 4a25d3f3b966b507494d96c7828654d84225c5e4f78f049c577248c98f57fea0
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

Record request_id , the HTTP status, and safe values from details . Statuses below are listed only when the referenced route fixes them explicitly; — means to use the status returned with the response.

Platform maintenance

Code Status Meaning First action

MAINTENANCE_READ_ONLY 503 Scheduled maintenance is active and the requested operation is a write. Reads remain available. Pause writes and wait for the dashboard or maintenance endpoint to report normal service.

MAINTENANCE_FULL 503 Full maintenance blocks normal dashboard, API, Runtime, and PostgreSQL access. Stop immediate retries, wait for normal service, then reconnect and verify any interrupted work before resubmitting it.

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

APPROVAL_REQUIRED 403 The user profile is not active. Follow the current dashboard account gate for verification, account setup, or manual approval.

LEGAL_ACCEPTANCE_REQUIRED 422 The account has no current durable acceptance of the Terms of Service and Privacy Policy. Return to signup or the account gate and record the required acceptance.

EMAIL_VERIFICATION_PROFILE_NOT_FOUND 404 Verification cannot find the account profile. Sign out and start signup or sign-in again; contact support if the account is otherwise visible.

EMAIL_VERIFICATION_LINK_FAILED 503 Polygres could not create or deliver a verification link. Retry once from Resend verification email , then contact support with the request ID.

EMAIL_VERIFICATION_EVIDENCE_MISMATCH 403 The verification continuation does not match the authenticated account. Sign out, use the intended account, and open a newly requested verification message.

API_KEY_INVALID — The API key is malformed, unknown, or revoked. Check the key source and project; create and deploy a replacement if needed.

NETWORK_ERROR Client The dashboard could not reach the API. Check network access and API availability, then retry.

Projects

Code Status Meaning First action

PROJECT_ID_INVALID 422 The external project ID does not match p[a-z0-9]{23} . Copy the ID from the project page or API response.

PROJECT_NOT_FOUND 404 The project does not exist, is deleted, or is not visible to the current user. Verify the project ID, organization membership, and selected account.

PROJECT_NOT_READY 409 The route requires project status ready . Check project status and resolve provisioning, deletion, suspension, or read-only state.

TIER_REQUIRED 403 No effective tier is assigned. Ask an administrator or Polygres support to restore the account’s tier assignment. There is no self-service tier-selection route.

TIER_NOT_FOUND 404 The assigned tier is missing or inactive. Refresh tier state; contact support if the assigned tier remains unavailable.

PROVISIONING_NOT_CONFIGURED 503 The environment cannot provision or delete project runtimes. Contact support; repeated client retries do not fix this configuration error.

PROVISIONING_RETRY_UNAVAILABLE 409 Manual retry is not valid for the current state, retry count, or retry window. Retry only when project status is failed and can_retry_provisioning is true.

PROJECT_RUNTIME_NOT_FOUND 409 The project’s runtime version record is missing. Refresh runtime status; contact support with the project and request IDs.

ID_INVALID 422 A UUID-like resource ID, such as a job, migration, or key ID, is malformed. Copy the ID from its list or detail response.

Organizations and invitations

Code Status Meaning First action

ORG_NOT_FOUND 404 The organization is missing or the user is not an active member. Verify the organization ID and membership returned by GET /me .

ORG_PERMISSION_DENIED 403 The current role cannot perform the requested member or invitation action. Every active role can list active members. Use an owner or admin account for invitations and membership changes.

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

IMPORT_CONCURRENCY_LIMIT 409 The project has reached its active import-job limit. Wait for or cancel one of the queued or running jobs before submitting another.

IMPORT_FILE_INVALID 400 The staged job or CSV metadata does not match the requested import. Recreate the preview and verify headers, types, mapping, and job ID.

IMPORT_CANCELLED 409 A cancelled preview job was submitted for execution. Create a new preview or import job.

IMPORT_SQL_EMPTY — The SQL import body is empty. Submit a non-empty SQL file or body.

IMPORT_JOB_NOT_FOUND — The job ID is unknown for the project. Confirm both project ID and job ID.

IMPORT_NOT_CANCELLABLE — The job is terminal or cannot be cancelled in its current phase. Refresh the job and act on its current status.

IMPORT_RUNTIME_NOT_CONFIGURED — Import execution is unavailable for the runtime. Retry once; contact support if it persists.

Migrations

Code Status Meaning First action

MIGRATION_NOT_FOUND — The migration ID is unknown for the project. Confirm both project ID and migration ID.

MIGRATION_LOCK_BUSY 409 Another migration is already running. Your migration is unchanged. Wait for the active migration to finish, then retry.

MIGRATION_SQL_CHECKSUM_MISMATCH 409 Stored SQL no longer matches the migration checksum. Do not bypass the check; contact support.

MIGRATION_SQL_BLOCKED 400 The migration contains a statement denied by SQL safety policy, including a top-level transaction command. Use the policy details to rewrite the migration. Let Polygres manage the transaction.

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

GRAPH_CONFIGURATION_INVALID 400 The graph table or ID-column definition is inconsistent. Supply non-empty id_columns per registered table. Legacy id_column is accepted only when id_columns is absent.

GRAPH_SCHEMA_NOT_ALLOWED 400 The graph configuration references a system or extension schema. Register public.* or an explicitly selected non-system schema table.

GRAPH_BUILD_FAILED 400 Graph build failed. Inspect invalid_reason ; correct the configuration if indicated, then retry the build. Contact support if the error does not identify a configuration fix.

GRAPH_NOT_READY 409 Graph build status is not ready . Check graph status; build or rebuild as needed.

GRAPH_FILTER_INVALID 400 A graph filter key or value is invalid. Use registered filter columns and scalar exact-match values.

GRAPH_COLUMN_NOT_SYNCABLE — A selected graph column cannot be synchronized. Remove or correct the columns listed in details.columns .

Vector

Code Status Meaning First action

VECTOR_CREATION_RETIRED 410 New pgvector configuration registration is retired. Create a pgContext collection with a native pgcontext.vector(n) column.

VECTOR_CONFIGURATION_NOT_FOUND 404 The named/default vector configuration does not exist. Pass a previously registered configuration name, or create and query a pgContext collection for new setup.

VECTOR_NOT_READY 409 The selected persisted Legacy configuration is not effectively Ready. Check index_kind , index_status , verification differences, and index_error . Reindex a mismatched or failed HNSW configuration.

VECTOR_INDEX_FAILED 400 Vector index creation, update, or reindex failed. Verify table, column, dimensions, metric, and index error; retry after correction.

VECTOR_SEARCH_INVALID 400 Conflicting vector bounds were supplied. Send either max_distance or min_similarity , not both.

VECTOR_FILTER_INVALID 400 A vector or hybrid filter key/value is invalid. Use configured filter columns and scalar exact-match values.

Text

Code Status Meaning First action

TEXT_CONFIGURATION_NOT_FOUND 404 The named text configuration does not exist. Use a valid configuration name.

TEXT_CONFIGURATION_NOT_READY 409 The text index status is not ready . Correct and update or recreate the configuration.

TEXT_CONFIGURATION_KIND_MISMATCH 400 A fuzzy configuration was used on the tsvector route or vice versa. Call the route matching search_kind .

TEXT_CONFIGURATION_INVALID 400 The configuration fields conflict or do not match its search kind. Use nested tsvector.mode: "generate" or "existing" for TSVector setup; use text_column only for fuzzy setup.

TEXT_GENERATED_COLUMN_EXISTS 409 Generated TSVector setup would overwrite an existing column. Choose a new generated-column name, or register an existing compatible TSVector column.

TEXT_GENERATION_CLEANUP_FAILED 500 Generated setup failed and automatic cleanup was incomplete. Inspect the generated column, managed index, and saved configuration before retrying.

TEXT_INDEX_FAILED 400 Text index creation or rebuild failed. Verify the table and selected columns, inspect diagnostics, then retry reindexing.

TEXT_INDEX_VERIFICATION_FAILED 409 The created physical index could not be verified as valid and ready. Inspect diagnostics, correct the database target, and reindex.

TEXT_INDEX_DELETE_FAILED 409 The managed index could not be removed, so the configuration was retained. Correct the database problem and retry deletion.

TEXT_LANGUAGE_NOT_FOUND 400 PostgreSQL does not recognize the requested text-search configuration. Use an installed language such as english or simple .

TEXT_QUERY_EMPTY 400 The query is empty after trimming. Send a non-empty query of at most 2,000 characters.

TEXT_FILTER_INVALID 400 A text filter key/value is invalid. Use configured filter columns and scalar exact-match values.

Hybrid ranking

Hybrid Joint ranking uses weighted Reciprocal Rank Fusion. The supplied vector_weight and graph_weight values control the contribution of each ranking lane, and the response reports the applied weights.

Code Status Meaning First action

HYBRID_WEIGHTS_INVALID 400 Hybrid weights contain an unsupported key or a value outside the accepted finite, non-negative shape. Send vector and graph weights as finite values of at least zero, with at least one positive value.

Common pgContext errors

Code Status Meaning First action

CONTEXT_REQUEST_INVALID 400 The strict request body or field combination is invalid. Compare with the pgContext API and remove unknown or conflicting fields.

CONTEXT_VECTOR_NULLABLE 400 The selected pgvector source contains at least one NULL vector. Populate or remove every affected row, then run preflight again. A nullable declaration alone is allowed when no stored value is NULL .

CONTEXT_VECTOR_DIMENSION_INVALID 400 The selected pgvector dimensions do not match the requested collection dimensions. Use the column’s declared dimensions or choose a matching vector column.

CONTEXT_INDEX_CONFLICT 409 An index that depends on the pgvector column backs a database constraint, so in-place conversion cannot drop it safely. Choose another column or redesign the constraint before retrying conversion.

CONTEXT_EMBEDDING_INVALID 400 The embedding is empty, non-finite, zero for cosine, or has the wrong dimensions. Supply finite numbers matching the selected vector’s dimensions and metric requirements.

CONTEXT_FILTER_INVALID 400 The filter grammar or registered filter key is invalid. Use a registered key and one supported condition per filter node.

CONTEXT_DELETE_CONFIRMATION_INVALID 400 The deletion body does not repeat the collection UUID from the path. Send confirm_collection_id equal to the path UUID.

CONTEXT_POINT_CURSOR_INVALID 400 The point-scrolling cursor is malformed or no longer valid. Restart point scrolling without a cursor.

CONTEXT_COLLECTION_NOT_FOUND 404 The collection UUID or exact name is not visible in this project. List collections and verify the selected project.

CONTEXT_VECTOR_NOT_FOUND 404 The requested exact vector_name is not registered in the selected collection. List the collection’s vectors and use an exact name. Omit vector_name only when the collection default is intended.

CONTEXT_OPERATION_NOT_FOUND 404 The operation UUID is not visible in this project. List operations and verify the selected project.

CONTEXT_COLLECTION_NOT_READY 409 The collection cannot serve the requested operation in its current state. Check collection status, then inspect verification or diagnostics.

CONTEXT_CAPABILITY_UNAVAILABLE 409 The project capability response reports the requested feature as unavailable. Read /context/capabilities and follow its blocker message.

CONTEXT_LIMIT_EXCEEDED 400 A Context request exceeds an effective size, dimension, filter, graph, or point limit. Read capabilities and split or reduce the request.

CONTEXT_PREFLIGHT_BLOCKED 409 Collection creation did not pass its source and ownership checks. Run preflight and correct its blockers before creating.

CONTEXT_COLLECTION_NAME_CONFLICT 409 Another collection already uses the requested name. Choose a unique name or use the existing collection.

CONTEXT_OPERATION_CONFLICT 409 Conflicting durable work is already active for the collection. Poll or cancel the existing operation before retrying.

CONTEXT_OPERATION_STATE_CONFLICT 409 Cancel or retry is incompatible with the operation’s current or terminal state. Refresh the operation and act on its current status; do not retry the same invalid transition.

CONTEXT_OPERATION_NOT_RETRYABLE 409 The operation is outside its eligible retry state, attempt allowance, or retry window. Retry a failed or cancelled operation while attempts remain and retry_until is current.

CONTEXT_IDEMPOTENCY_CONFLICT 409 An idempotency key was reused for a different canonical request. Retry with the original request or a new key, never a changed request with the old key.

CONTEXT_GRAPH_NOT_READY 409 A graph-composition mode cannot use the current graph state. Check graph readiness and rebuild or correct its configuration.

CONTEXT_SOURCE_KEY_ALIGNMENT_INVALID 409 Context source identities cannot align with graph candidates. Align the registered graph table and collection source key.

CONTEXT_READER_ACCESS_REQUIRED 409 Polygres cannot access the source table with the permissions required for safe point listings. Correct the source-table permissions and run preflight again.

CONTEXT_POINT_SCROLL_RLS_UNSAFE 409 Polygres cannot guarantee that point listings will respect the source table’s row-level security. Run verification and diagnostics, then correct the reported permission or policy issue.

CONTEXT_SOURCE_UNAVAILABLE 409 The collection’s source table is missing or has been replaced. Restore the intended table or recreate the collection against the current source. Start pagination again without the old cursor.

CONTEXT_SOURCE_OWNERSHIP_MISMATCH 409 Polygres cannot confirm that a managed source table still belongs only to this collection. Stop deletion and review the collection’s source table. Contact support if the ownership information is incorrect.

CONTEXT_RECALL_UNAVAILABLE 409 Recall checking is unavailable for this collection or index state. Check collection status, index kind, and capabilities.

CONTEXT_MEMORY_PRESSURE 409 Heavy Context work is temporarily blocked by project memory pressure. Let current work settle, then retry with backoff. Retrieval and lightweight reads can remain available.

CONTEXT_INLINE_CAPACITY_EXCEEDED 429 Too many synchronous Context mutations are active. Retry with backoff.

RUNTIME_CONTEXT_PROXY_FAILED 502 The Gateway could not complete its request to the project Runtime API. Check project readiness, retry once, then report the request ID if it persists.

A failed collection verification or recall threshold still returns HTTP 200. Inspect verified or the recall status in the response instead of branching on HTTP status alone.

Rate limits

Response Meaning First action

HTTP 429 One of the applicable IP, user, user-project, API-key, or project windows is exhausted. Honor Retry-After when present and retry with backoff. Do not fan out immediate retries.

Rate-limit responses use the stable RATE_LIMITED code. Branch on HTTP 429 , retain the code and request ID for diagnostics, and follow Retry-After .

Runtime and service configuration

Code Status Meaning First action

DATA_PLANE_NOT_CONFIGURED 503 Query execution is unavailable for the project runtime. Confirm the project is operational, retry once, then contact support.

PROVISIONING_NOT_CONFIGURED 503 Runtime provisioning/deletion is unavailable in the environment. Contact support.

AUTH_NOT_CONFIGURED 503 Dashboard authentication validation is unavailable. Contact support if a retry does not recover.

DASHBOARD_PUBLIC_BASE_URL_INVALID / DASHBOARD_PUBLIC_BASE_URL_REQUIRED 503 Organization invitation URL generation is misconfigured. Contact support.

PROJECT_RUNTIME_NOT_FOUND 409 Runtime catalog metadata for the project is missing. Contact support with the project and request IDs.
