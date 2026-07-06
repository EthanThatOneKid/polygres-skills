source: https://docs.evokoa.com/polygres/reference/troubleshooting
title: Troubleshooting | Polygres
source_hash: cffbdf77d9ddd0e332083a1fc3fa1195378a31117c55fe7602ac949d96b293b4
discovered_from: https://docs.evokoa.com/polygres

# Troubleshooting | Polygres

Troubleshooting

Start with the symptom. Capture the request_id , exact route, project ID, and a

timestamp with timezone before retrying. Do not include credentials or sensitive data

in diagnostic logs.

Organization, invitation, and access issues

Symptom Check Action

Organization page or API returns ORG_NOT_FOUND Call GET /me ; verify the expected organization and an active membership. The response also hides inactive or inaccessible organizations as not found. Sign in to the correct account. Ask an owner/admin to restore membership when appropriate.

Members or invitations return ORG_PERMISSION_DENIED Current member-management routes require organization role owner or admin . Use an owner/admin session. Do not retry with a project API key.

Invitation says email mismatch Compare the signed-in email with the invited email. Sign out and accept with the invited account, or ask an owner/admin to issue a replacement invitation.

Invitation is expired or not found Confirm the link is the latest invitation and has not been revoked or replaced. Request a new invitation.

Invitation cannot be generated Look for DASHBOARD_PUBLIC_BASE_URL_INVALID or DASHBOARD_PUBLIC_BASE_URL_REQUIRED . Contact support; these are service-configuration errors.

Access disappeared after previously working Check membership status, organization selection, account lifecycle state, and project organization. Restore an active membership or complete verification/approval/tier selection. Escalate if GET /me is inconsistent with the dashboard.

API key works for retrieval but not setup routes Check for AUTH_MODE_NOT_ALLOWED . Use a dashboard session for account, organization, project mutation, SQL, imports, migrations, configuration, key lifecycle, and password reveal.

Connection issues

Symptom Check Action

Hostname or connection URL fails Fetch current connection metadata from Connect or GET /connection-info on the project Runtime API; compare host, port, database, username, and sslmode=require . Check project status. Replace cached connection metadata. Escalate when both current direct and pooled hosts are unreachable for a ready project.

Password authentication fails Confirm the credential is the native project-owner password, not a dashboard token or Polygres API key. Reveal the current password through the dashboard and update the server-side secret. Never paste it into logs or support requests.

Pooled connection rejects a session-dependent operation Check whether the operation requires stable session state, schema changes, COPY , or bulk loading. Use the direct URL for that operation; keep the pooled URL for ordinary short application queries.

Too many database connections Compare active client pools with the direct and pooled tier limits from GET /tiers . Reduce pool sizes, close leaked connections, or use the pooled endpoint.

API-key connection-info request fails Verify Authorization: Bearer poly_live_... is sent to the project Runtime API URL copied from Connect > API access . Correct the runtime URL/key pair or replace a revoked key. API keys never receive a password.

Connection works but writes fail Check project status for read_only , storage bytes, and read_only_reason . Stop write retries; reduce storage or change tier/storage, then wait for status to clear. Retrieval may still work.

Project provisioning

Symptom Check Action

Project remains provisioning Read project detail/status and inspect provisioning error fields, retry metadata, and runtime health. Avoid creating duplicates. Escalate when status does not progress and no retry/error field explains why.

Project is failed Inspect provisioning_error , error code, can_retry_provisioning , and any next retry timestamp. Call retry only when can_retry_provisioning is true. Preserve the failed request ID.

Retry returns PROVISIONING_RETRY_UNAVAILABLE Project is not eligible, the retry window has not elapsed, or retry count is exhausted. Follow the current can_retry_provisioning and retry timestamp; otherwise contact support.

Retry or creation returns PROVISIONING_NOT_CONFIGURED Runtime provisioning is unavailable in the environment. Contact support; client-side retries do not correct this condition.

Project is suspended Check account, organization, billing/tier, and project status messaging. Resolve the indicated account or organization condition; contact support when no reason is visible.

Project is deleting or deleted Confirm that deletion was intended. Do not use its old hosts, IDs, jobs, or configurations. A deleted project is not recoverable through user-facing routes.

Project is read_only Inspect the latest storage measurement and reason. See Limits ; avoid writes until status returns to ready .

Import issues

Symptom Check Action

Upload rejected with IMPORT_LIMIT_EXCEEDED Compare declared file size with the import-type cap in GET /tiers . Split or reduce the file, or use an available tier with a sufficient cap.

Start rejected with IMPORT_CONCURRENCY_LIMIT List imports and find any queued or running job. Wait for or cancel the active job. Current tiers allow three active imports per project.

CSV start returns IMPORT_FILE_INVALID Verify the job_id came from the current CSV preview and that type, headers, mapping, schema, and table identifiers still match. Create a new preview and submit its confirmed mapping.

CSV start returns IMPORT_CANCELLED The preview job was cancelled. Create a new CSV preview; cancelled jobs cannot resume.

SQL import says empty Check for IMPORT_SQL_EMPTY and verify the uploaded body is non-empty. Submit a non-empty SQL body.

Job is failed Read error_code , error_message , and progress ; also verify project is not read-only. Correct the input/runtime cause and create a new job. Escalate non-actionable or repeated failures.

Job appears stuck Compare status , progress , and updated_at across refreshes. Do not start parallel imports. Escalate with job ID and timestamps when there is no progress or error.

Cancel returns IMPORT_NOT_CANCELLABLE Refresh the job; it may already be terminal or beyond a cancellable phase. Act on the current state. Do not expect a succeeded, failed, or cancelled job to resume.

Import reports runtime configuration failure Look for IMPORT_RUNTIME_NOT_CONFIGURED or a staging service error. Retry once; contact support if it persists.

Migration issues

Symptom Check Action

Draft cannot be created or applied Inspect MIGRATION_SQL_BLOCKED or request validation details. Migration names must be valid SQL identifiers and at most 120 characters. Rewrite the denied SQL or name; do not bypass the safety response.

Apply returns MIGRATION_LOCK_BUSY Check for another migration in applying . Wait for the active operation before retrying.

Apply returns checksum mismatch MIGRATION_SQL_CHECKSUM_MISMATCH means stored SQL and checksum disagree. Stop retrying and contact support; do not alter or bypass the record.

Migration becomes failed Read error_message and inspect the database error context. Correct with a new forward migration, or retry only when the stored SQL remains intended and the cause was transient.

Migration remains applying Refresh the detail and check the last update time. Avoid concurrent apply calls; escalate when it does not transition and no active operation is visible.

Runtime execution unavailable Look for MIGRATION_RUNTIME_NOT_CONFIGURED . Retry once, then contact support.

Need to undo an applied migration The current API has no rollback, edit, or delete operation. Create a new forward migration that performs the corrective change.

Retrieval readiness

Symptom Check Action

GRAPH_NOT_READY GET .../graph/status : build_status , needs_rebuild , and graph configuration invalid_reason . Build or rebuild until status is exactly ready . Correct failed configuration before retrying.

VECTOR_CONFIGURATION_NOT_FOUND Requested config , list of configurations, and whether a default exists. Pass a valid name or create/select the intended default.

VECTOR_NOT_READY Selected config’s index_kind , index_status , and index_error . Reindex HNSW and wait for ready . Exact-scan index_kind: none does not require HNSW readiness, although aggregate vector readiness stays false.

TEXT_CONFIGURATION_NOT_READY Text configuration’s search_kind , index_status , and index_error . Correct/rebuild until status is ready . Text status is not returned by the retrieval-readiness route.

Hybrid is not ready Read both graph readiness and the default vector readiness. Make graph ready and set a default vector config whose index status is ready .

Readiness says false after a change Confirm the request used the intended project and refresh the underlying config/status. Wait for active build/index work; escalate if underlying states are ready but the computed flag remains false.

Vector and text configuration issues

Symptom Check Action

Vector create/update fails validation Verify table, row ID, fixed-dimension vector(n) column, dimensions 1..2000 , metric, metadata columns, filter columns, and limits. Match the saved dimensions to the column and keep default_limit <= max_limit .

Vector query rejects embedding Compare embedding length with configuration dimensions ; verify all values are finite. Generate the correct fixed-length embedding. Send either max_distance or min_similarity , not both.

Vector index is failed or stale Read index_error ; inspect recent target, metric, or schema changes. Correct the target and reindex. Escalate repeated failures with config name and request ID.

Text route reports kind mismatch Compare route with search_kind . Use /text/tsvector for tsvector configs and /text/fuzzy for fuzzy configs.

Text configuration is invalid A tsvector config must use tsvector_column only; fuzzy must use text_column only. Correct or recreate the configuration.

Text query is empty Query trims to no characters or exceeds the supported shape. Send a non-empty query of at most 2,000 characters.

Filter is rejected Verify the filter column is configured and values are scalar exact matches. Remove nested arrays/objects and use valid SQL identifier keys.

Rate limits

Symptom Check Action

HTTP 429 Read Retry-After and identify whether calls fan out by user, API key, project, or IP. Wait for the indicated window and retry with backoff. Reduce polling and concurrency; do not issue immediate parallel retries.

One key is limited while another works The API-key scope may be exhausted even when project/IP windows are not. Reduce traffic for that key; note that all applicable scopes still apply.

All users or keys for one project are limited The project window is likely exhausted. Reduce aggregate project traffic and wait for reset.

Repeated authentication failures are locked out Authentication failures reached 20 within 5 minutes. Stop retries, correct the credential, and wait through the 10-minute lockout.

See Limits for the configured windows.

SQL and data-tool issues

Symptom Check Action

SQL is blocked Inspect SQL_QUERY_BLOCKED , SQL_IMPORT_BLOCKED , or MIGRATION_SQL_BLOCKED details. Rewrite the denied statement for the applicable policy.

SQL ran but failed Use SQL_QUERY_FAILED details such as SQLSTATE, hint, detail, position, and statement index when present. Correct the query or schema assumption. Keep full SQL and sensitive values out of routine logs.

Table rows reject the limit Table viewer accepts only 1..500 . Send a valid limit and follow next_cursor for another page.

Resource ID or identifier is rejected Check project ID, UUID-like resource IDs, and SQL identifier syntax. Copy IDs from API responses and use [A-Za-z_][A-Za-z0-9_]* for identifiers.

Escalate

Contact support when the state or error has no actionable correction, a corrected operation repeatedly fails, or live status contradicts the returned error.
