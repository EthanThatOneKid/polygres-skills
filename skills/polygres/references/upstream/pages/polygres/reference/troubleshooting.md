source: https://docs.evokoa.com/polygres/reference/troubleshooting
title: Troubleshooting | Polygres
source_hash: 4edf4d4c611d74879346a549974cef0fd905dc6d86d4eff8e616b24f45cbd730
discovered_from: https://docs.evokoa.com/polygres

# Troubleshooting | Polygres

Troubleshooting

Start with the symptom. Capture the stable error code , optional variant ,

request_id , exact route, project ID, and a timestamp with timezone before

retrying. For gateway-proxied requests, also capture X-Request-ID and

X-Polygres-Upstream-Request-ID . Do not include credentials or sensitive data

in diagnostic logs. See Handle API errors for

the response format and retry guidance.

Scheduled maintenance

Symptom Check Action

Writes return MAINTENANCE_READ_ONLY Read the dashboard banner or GET /v1/maintenance ; confirm the mode and phase. Pause writes and background mutations. Reads remain available. Resume only after maintenance returns to normal.

API calls return MAINTENANCE_FULL or the dashboard shows its maintenance page Check maintenance status rather than project-specific readiness. Stop immediate retries. Wait for normal service, then reconnect and retry with the original idempotency safeguards.

PostgreSQL is unavailable during full maintenance Confirm the active maintenance notice. Pause new database work, let connection pools back off, and reconnect after service is restored. Verify the outcome of any interrupted transaction before retrying it.

Organization, invitation, and access issues

Symptom Check Action

Organization page or API returns ORG_NOT_FOUND Call GET /me ; verify the expected organization and an active membership. The response also hides inactive or inaccessible organizations as not found. Sign in to the correct account. Ask an owner/admin to restore membership when appropriate.

Members or invitations return ORG_PERMISSION_DENIED All active roles can list active members. Invitation listing and membership mutations require owner or admin . Use an owner/admin session for the restricted action. Do not retry with a project API key.

Invitation says email mismatch Compare the signed-in email with the invited email. Sign out and accept with the invited account, or ask an owner/admin to issue a replacement invitation.

Several invitations appear after sign-in The dashboard loads every pending, unexpired organization invitation for the authenticated email. Select the one organization to join. Verification activates that membership and closes the others.

Invitation selection is waiting on verification Confirm the verification page shows the intended account email. Use the newest verification email, or choose Cancel invitation to decline the pending invitations and continue with normal organization setup.

Invitation email was not delivered Confirm a pending invitation still exists and whether the dashboard offers replacement. An owner/admin can use Send new invite to refresh the role, expiry, and delivery attempt.

Invitation is expired or not found Confirm the link is the latest invitation and has not been revoked or replaced. Request a new invitation.

Invitation cannot be generated Look for DASHBOARD_PUBLIC_BASE_URL_INVALID or DASHBOARD_PUBLIC_BASE_URL_REQUIRED . Contact support; these are service-configuration errors.

Access disappeared after previously working Check membership status, organization selection, account lifecycle state, and project organization. Restore an active membership or complete verification or approval. Ask an administrator or support to resolve a missing tier assignment. Escalate if GET /me is inconsistent with the dashboard.

API key works for retrieval but not a control-plane route Check for AUTH_MODE_NOT_ALLOWED . Use the project API key for Runtime retrieval and pgContext management. Use a dashboard session or CLI login for organizations, projects, SQL, imports, migrations, key lifecycle, and database credentials.

Billing and Paid-project issues

Only organization owners and admins can open Billing or submit Paid-project

actions. Billing is the place to check the account category, credit balance,

payment method, next billing date, project charges, and invoices.

Symptom Check Action

Returned from payment-method setup but the project has not continued Stripe confirmation may still be pending. Keep the project page open or return shortly. Polygres continues with the saved project selection after the payment method is confirmed.

Returned from a top-up but credits are missing Billing may still show Payment pending while Stripe confirms the purchase. Wait for the payment status to update, then refresh Billing.

Billing is unavailable Check for a maintenance notice. Try again later. Contact support if Billing remains unavailable.

Payment methods and invoices will not open Refresh Billing and try the action again. Try again later or contact support.

A Paid action needs a payment method Compare the amount due with the available credit balance and check the payment state in Billing. Add or update the payment method, then return to the saved project action.

Billing shows Launch unexpectedly Launch is derived from active Paid projects. Review the Paid projects list. If no active Paid project explains the category, refresh Billing and contact support.

An invoice is past due or needs payment confirmation Open invoice history or the Stripe invoice portal and review the payment status. Complete the action requested by Stripe, then return to Billing and wait for the status to update.

A top-up is still pending Open the purchase in top-up history and review its status. Wait for Stripe to confirm payment. Contact support if the purchase remains pending or moves to support review.

Top-up purchase cannot be found Refresh top-up history and confirm the organization in the dashboard URL. Open the purchase from the current history. Contact support with the Checkout reference if a paid purchase remains missing.

Project limits are rejected Check Storage, Context, and Graph against the minimum, maximum, and increment shown in the dashboard. Choose supported values. Context and Graph change in exact 100,000-unit increments.

A Paid project reports PAID_PROJECT_PRICE_CHANGED The price changed after the payment preview was prepared. Review the updated monthly price and first-cycle maximum, then confirm again.

A capacity increase reports CAPACITY_PAYMENT_FAILED The credit and Stripe payment could not be completed. The current capacity remains active. Check the payment method in Billing, then retry the capacity increase from the project’s Upgrade page.

Context or Graph shows Approaching or Grace Compare current usage with the configured limit and the 50,000-unit grace ceiling. Graph usage counts each node as 1 unit and each edge as 0.1 unit. Increase capacity from the project’s Upgrade page or reduce usage before the capability becomes paused.

Context or Graph reports CAPACITY_CAPABILITY_PAUSED Usage has reached the temporary allowance above the configured limit. Increase capacity or reduce usage below the configured limit, then wait for the dashboard status to update.

A change reports CAPACITY_GRACE_CEILING_EXCEEDED The change would use more than the project’s temporary capacity allowance. Reduce the size of the change, remove unused data, or increase capacity from the project’s Upgrade page before trying again.

A Context or Graph action reports CAPACITY_STATE_UNAVAILABLE Polygres is still updating the project’s capacity status. After a successful increase payment, this can mean activation still needs to finish. Retry from the Upgrade page. A previously accepted payment is reused rather than charged again. Contact support if the status does not update.

A lower capacity reports CAPACITY_DECREASE_REQUIRES_CLEANUP Current usage and active work do not fit within the selected limit. Remove at least the amount shown, let active work finish, and apply the lower capacity again.

Paid project creation is unavailable PROJECT_TIER_UNAVAILABLE means the selected limits are not currently available. Also check your organization role, payment state, and any maintenance notice. Use an owner or admin account, complete the payment step shown, or choose supported limits.

Free project creation reports the project limit TIER_PROJECT_LIMIT_EXCEEDED means the organization already uses its one Free Nano slot, including any hosted or synchronized Nano project. Delete the existing Free project before creating another Free project. A new Paid project does not consume the Free slot.

An upgrade to Basic needs attention Read the saved progress on the project’s Upgrade page and confirm that Nano remains active. Follow the displayed recovery guidance. Contact support with the operation and request IDs before trying again.

Connection issues

Symptom Check Action

Hostname or connection URL fails Fetch current connection metadata from Connect or GET /connection-info on the project Runtime API; compare host, port, database, username, and sslmode=verify-full . Check project status. Refresh cached connection metadata and confirm the trusted CA configuration. Escalate when both current direct and pooled hosts remain unavailable for a ready project.

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

Job is failed Read error_code , optional error_variant , error_message , and progress ; also verify the project is not read-only. Use the code and variant to identify the cause, then correct it before creating a new job. Escalate non-actionable or repeated failures with the job and request IDs.

Job appears stuck Compare status , progress , and updated_at across refreshes. Do not start parallel imports. Escalate with job ID and timestamps when there is no progress or error.

Cancel returns IMPORT_NOT_CANCELLABLE Refresh the job; it may already be terminal or beyond a cancellable phase. Act on the current state. Do not expect a succeeded, failed, or cancelled job to resume.

Import reports a runtime configuration error Read the returned import error and current project status. Retry once, then contact support with the job and request IDs if the message remains.

Migration issues

Symptom Check Action

Draft cannot be created or applied Inspect MIGRATION_SQL_BLOCKED or request validation details. Migration names must be valid SQL identifiers and at most 120 characters. Top-level transaction commands are not allowed because Polygres manages the transaction. Rewrite the denied SQL or name; do not bypass the safety response. Transaction keywords inside a dollar-quoted function, procedure, or DO body remain valid.

Apply returns MIGRATION_LOCK_BUSY Another migration is already running. Your migration is unchanged. Wait for the active migration to finish, then retry.

Apply returns checksum mismatch MIGRATION_SQL_CHECKSUM_MISMATCH means stored SQL and checksum disagree. Stop retrying and contact support; do not alter or bypass the record.

Migration becomes failed PostgreSQL executed the migration and returned an error. Changes made earlier in that migration were rolled back. Read error_code , optional error_variant , error_message , and the available database context. Use the code and variant to identify the cause. Correct bad SQL with a new forward migration, or retry the same migration only when its SQL remains intended and the cause was transient.

Migration remains applying Refresh the detail and check the last update time. Avoid concurrent apply calls; escalate when it does not transition and no active operation is visible.

Runtime execution unavailable Look for MIGRATION_RUNTIME_NOT_CONFIGURED . Retry once, then contact support.

Need to undo an applied migration The current API has no rollback, edit, or delete operation. Create a new forward migration that performs the corrective change.

Retrieval readiness

Symptom Check Action

GRAPH_NOT_READY GET .../graph/status : build_status , needs_rebuild , and graph configuration invalid_reason . Build or rebuild until status is exactly ready . Correct failed configuration before retrying.

GRAPH_CONCURRENT_BUILD_UNAVAILABLE A Basic project received a concurrent graph-build request. Retry the graph build synchronously with concurrent set to false .

VECTOR_CONFIGURATION_NOT_FOUND Requested config , persisted configurations, and whether an effective default exists. Pass an existing persisted Ready registration. For a new source, create a pgContext collection; retired routes cannot register or re-enable a physical-only pgvector index.

VECTOR_NOT_READY Selected config’s index_kind , index_status , verification differences, and index_error . For HNSW, reindex and wait for the exact physical index to become ready . An existing exact-scan index_kind: none registration can be effectively Ready without HNSW.

TEXT_CONFIGURATION_NOT_READY Text configuration’s search_kind , index_status , and index_error . Correct/rebuild until status is ready . Text status is not returned by the retrieval-readiness route.

Hybrid is not ready Read graph readiness, ready_config_count , default_config , and selection_required . Make graph ready and ensure at least one persisted Legacy registration is effectively Ready. If selection is required, pass an exact configuration.

Readiness says false after a change Confirm the request used the intended project and refresh the underlying config/status. Wait for active build/index work; escalate if underlying states are ready but the computed flag remains false.

Vector and text configuration issues

Symptom Check Action

Existing Legacy vector update fails validation Verify the persisted registration, table, row ID, fixed-dimension vector(n) column, dimensions 1..2000 , metric, metadata columns, filter columns, and limits. Correct the existing registration. Use pgContext for new vector setup; creation and re-enabling through Legacy routes are retired.

Vector query rejects embedding Compare embedding length with configuration dimensions ; verify all values are finite. Generate the correct fixed-length embedding. Send either max_distance or min_similarity , not both.

Vector or hybrid query returns LIMIT_OUT_OF_RANGE Compare the final result limit with details.max . Its effective maximum comes from the project tier’s retrieval_max_limit and can be lower than the 1..1000 request-shape ceiling. Hybrid vector_limit has its own 1..1000 request-shape range. Reduce limit to the effective maximum. Correct vector_limit only when it is outside its request-shape range. Do not retry a fallback route with the same invalid value.

Vector index is failed or stale Read index_error ; inspect recent target, metric, or schema changes. Correct the target and reindex. Escalate repeated failures with config name and request ID.

Text route reports kind mismatch Compare route with search_kind . Use /text/tsvector for tsvector configs and /text/fuzzy for fuzzy configs.

Generated TSVector setup is rejected Check the source columns, generated-column name, language, stable row key, metadata columns, and filter columns. The generated name must not already exist. Correct the one-call tsvector.mode: "generate" request and retry. A separate migration is not required.

Existing TSVector registration is invalid The selected column must exist and have type tsvector . Use tsvector.mode: "existing" , or keep the deprecated flat tsvector_column input in an existing integration.

TEXT_GENERATION_CLEANUP_FAILED Setup failed after changing the table and automatic cleanup was incomplete. Inspect the generated column, managed index, and saved configuration before retrying. Do not create a second column blindly.

Text index is missing or invalid Open configuration diagnostics and compare index_found , index_valid , index_ready , and saved status. Correct the target, then call the reindex endpoint or use Rebuild in the dashboard.

Text query is empty Query trims to no characters or exceeds the supported shape. Send a non-empty query of at most 2,000 characters.

Filter is rejected Verify the filter column is configured and values are scalar exact matches. Remove nested arrays/objects and use valid SQL identifier keys.

pgContext AI Search

When creation from an existing pgvector column is blocked, separate the source

problem from general pgContext capability readiness:

Evidence Meaning Next check

CONTEXT_VECTOR_NULLABLE At least one stored vector is NULL ; the catalog’s nullable flag alone is not the cause. Count rows where the selected column IS NULL , populate or remove them, then rerun preflight.

CONTEXT_VECTOR_DIMENSION_INVALID The request and the fixed-dimension pgvector column disagree. Compare the requested dimensions with the discovered column dimensions.

CONTEXT_INDEX_CONFLICT A dependent index backs a database constraint and cannot be dropped during conversion. Inspect constraints and their indexes; do not remove one without explicit approval and an application-safe migration.

Creation failed after explicit legacy cleanup A separately approved deletion removed the saved Legacy registration before the durable create failed. Neither dashboard creation nor direct creation performs that cleanup automatically. Confirm the original column is still public.vector(n) , then correct the blocker and rerun discovery and preflight before creating again.

Ordinary collection creation converts the selected pgvector column in place.

Do not diagnose it as a same-column bridge or expect the old pgvector index to

remain.

Symptom Check Action

Collection setup is blocked Read Context capabilities and run preflight for the exact source, vector, text, result, and filter plan. Follow the capability or preflight guidance, then submit the reviewed collection definition.

Collection is preparing or needs review Read collection status, verification, and diagnostics in that order. Wait for active work, then use the ordered verification checks to select the next action.

A named vector is unavailable Read the collection’s vectors , default_vector_name , and the requested vector_name . Use an exact registered vector name, or omit it intentionally to use the collection default.

One vector is not Ready Inspect that vector’s durable add operation and per-vector index status. Correct or retry the selected vector workflow without assuming a Ready sibling has the same failure.

Retrieval mode is unavailable Check the capability matching the selected method, such as dense_search , text_hybrid , graph_first , or joint . Choose an available mode or complete the capability guidance shown by the Runtime.

Results are missing expected source rows Compare the committed source-row changes with point status and the application’s synchronization record. Upsert known inserted or restored keys, delete known removed keys, or reconcile after bulk and uncertain changes.

Point listings are unavailable Check the point_scroll capability, then run collection verification and diagnostics. Correct the reported source-table or permission issue and verify again.

A point page is empty but has_more is true Row-level security may have hidden every row in that page. Continue with next_cursor until has_more is false.

Reconciliation reports orphan_cleanup_skipped_reason: source_rls_enabled Row-level security prevents Polygres from knowing whether a hidden row was deleted. Explicitly delete keys for rows you know were removed. Keep row-level security enabled.

Durable operation is active Read the operation status, stage, committed count, attempts, and retry_until . Wait with the operation UUID, or use an eligible cancel or retry action with a persisted idempotency key.

Graph composition needs alignment Check graph readiness, the collection source table and source-key column, start entities, and relationship types. Use verified graph entity IDs and align the graph table identity with the Context source identity.

Recall check is below its target Inspect the selected vector’s index status, exact and approximate result counts, measured recall, and request filters. Review representative embeddings and filters, then reindex or tune that vector workflow and measure again.

The pgContext API reference lists every capability, collection, point, operation, aggregate, and retrieval method. Preserve the collection UUID, operation UUID, and request ID throughout diagnosis.

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
