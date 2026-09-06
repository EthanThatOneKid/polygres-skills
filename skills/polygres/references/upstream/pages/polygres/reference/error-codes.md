source: https://docs.evokoa.com/polygres/reference/error-codes
title: Error codes | Polygres
source_hash: e64763ac725f770afba1201f6063f8866a51dc56a5ec7f50d84090e9adc0553f
discovered_from: https://docs.evokoa.com/polygres

# Error codes | Polygres

Error codes

This page lists all 688 public error codes that can appear in Polygres API responses and asynchronous operation results. Use it to look up an error’s exact message, HTTP status, and retry guidance.

Error response contract

Every API error uses this envelope:

{

"request_id" : "req_xxx" ,

"error" : {

"code" : "ERROR_CODE" ,

"variant" : "specific_condition" ,

"message" : "Catalog-owned message." ,

"details" : {}

}

}

variant is omitted when the base code supplies the message. A variant selects a more specific catalog message and can also select a different HTTP status. Branch on code and, only when needed, variant . Do not parse message .

A failed asynchronous operation can include error_code , optional error_variant , and error_message . Use the code and variant as the stable machine-readable identity, and treat the message as explanatory text.

The API includes only detail fields approved for that code. Preserve request_id when reporting a failure. On HTTP 429 , also honor Retry-After .

For application patterns, SDK exceptions, safe logging, and asynchronous job guidance, see Handle API errors .

Retry classes

Retry class Meaning

never Retrying the same request will not resolve the error.

user_retry Retry only after the user restarts or corrects the current flow.

bounded_retry Retry a limited number of times with backoff.

dependency_retry Retry with backoff after the dependent service has had time to recover.

after_user_action Correct the request, permissions, configuration, or resource state before retrying.

after_delay Wait, honor Retry-After when present, then retry with backoff.

Complete catalog

A row written as CODE/variant is a specific message and status for the base code. API response + Async operation means the identity can appear in both synchronous error responses and asynchronous operation failures.

Analytics

Error identity HTTP Used by Retry Exact message

POSTGRES_ANALYTICS_BODY_TOO_LARGE 413 API response after_user_action The PostgreSQL analytics request is too large.

POSTGRES_ANALYTICS_INVALID_CONTENT_LENGTH 400 API response after_user_action The PostgreSQL analytics request has an invalid Content-Length header.

Authentication

Error identity HTTP Used by Retry Exact message

AUTH_ACTION_EXPIRED 410 API response user_retry This authentication action has expired.

AUTH_ACTION_INVALID 400 API response user_retry This authentication action is invalid.

AUTH_ATOMIC_REPOSITORY_NOT_CONFIGURED 503 API response + Async operation after_delay Atomic account setup is not configured.

AUTH_ATOMIC_REPOSITORY_NOT_CONFIGURED/atomic_invitation_acceptance_not_configured 503 API response + Async operation after_delay Atomic invitation acceptance is not configured.

AUTH_ATOMIC_REPOSITORY_NOT_CONFIGURED/atomic_invitation_selection_not_configured 503 API response + Async operation after_delay Atomic invitation selection is not configured.

AUTH_EMAIL_REQUIRED 401 API response never Your identity provider did not return an email address. Use another sign-in method or allow email access.

AUTH_IDENTITY_CHANGED 500 API response bounded_retry The signed-in identity changed before the operation completed.

AUTH_INTENT_NOT_CONFIGURED 503 API response + Async operation after_delay Email verification evidence is not configured.

AUTH_INTENT_NOT_CONFIGURED/invitation_authentication_intent_signing_not_configured 503 API response + Async operation after_delay Invitation authentication intent signing is not configured.

AUTH_INVALID_CREDENTIALS 401 API response user_retry The email or password is incorrect.

AUTH_LOCKOUT 429 API response after_user_action Too many authentication failures. Try again later.

AUTH_MODE_NOT_ALLOWED 403 API response + Async operation never This credential cannot be used for this operation.

AUTH_MODE_NOT_ALLOWED/api_key_auth_not_allowed 403 API response + Async operation never API key auth is not allowed.

AUTH_MODE_NOT_ALLOWED/cli_auth_not_allowed_operation 403 API response + Async operation never CLI auth is not allowed for this operation.

AUTH_MODE_NOT_ALLOWED/runtime_api_key_scope_not_allowed 403 API response + Async operation never Runtime API key scope is not allowed for Context.

AUTH_MODE_NOT_ALLOWED/gateway_runtime_auth_not_allowed_operation 403 API response + Async operation never Gateway Runtime auth is not allowed for this operation.

AUTH_MODE_NOT_ALLOWED/delegated_runtime_auth_not_allowed_operation 403 API response + Async operation never Delegated Runtime auth is not allowed for this operation.

AUTH_NOT_CONFIGURED 503 API response + Async operation never Authentication is not configured for this service.

AUTH_NOT_CONFIGURED/account_services_temporarily_unavailable_try_again 503 API response + Async operation never Account services are temporarily unavailable. Please try again later.

AUTH_PASSWORD_MODE_MISMATCH 503 API response never Password-change security is not configured consistently.

AUTH_PKCE_EXCHANGE_FAILED 400 API response user_retry The sign-in callback could not be verified. Restart sign-in in the same browser.

AUTH_PKCE_VERIFIER_MISSING 400 API response user_retry This sign-in link must be restarted in the browser that began it.

AUTH_PROVIDER_UNAVAILABLE 503 API response dependency_retry Authentication is temporarily unavailable. Wait a moment and try again.

AUTH_REAUTHENTICATION_INVALID 403 API response user_retry The reauthentication proof is invalid or expired.

AUTH_REAUTHENTICATION_REQUIRED 403 API response user_retry Reauthenticate to continue.

AUTH_RECOVERY_REQUIRED 403 API response user_retry A verified password-recovery session is required.

AUTH_REQUIRED 401 API response + Async operation user_retry Authentication is required.

AUTH_WEAK_PASSWORD 422 API response user_retry The password does not meet the configured security requirements.

CLI_AUTH_DENIED 500 API response user_retry CLI authentication was denied.

CLI_AUTH_EXPIRED 500 API response user_retry The CLI authentication request expired.

CLI_AUTH_NOT_CONFIGURED 503 API response + Async operation never CLI authentication is not configured.

CLI_AUTH_NOT_CONFIGURED/shared_cli_authentication_storage_not_configured 503 API response + Async operation never Shared CLI authentication storage is not configured.

CLI_AUTH_NOT_CONFIGURED/redis_package_required_shared_cli_authentication 503 API response + Async operation never The redis package is required for shared CLI authentication.

CLI_AUTH_RESPONSE_INVALID 500 API response dependency_retry The CLI received an invalid authentication response.

CLI_AUTH_SESSION_CREATE_FAILED 503 API response + Async operation dependency_retry The CLI login session could not be created.

CLI_AUTH_SESSION_CREATE_FAILED/cli_login_session_could_not_be 503 API response + Async operation dependency_retry CLI login session could not be created.

CLI_AUTH_SESSION_INVALID 503 API response + Async operation dependency_retry CLI authentication state is unavailable.

CLI_AUTH_SESSION_INVALID/cli_login_session_storage_invalid 503 API response + Async operation dependency_retry CLI login session storage is invalid.

CLI_AUTH_SESSION_NOT_FOUND 404 API response + Async operation never CLI login session not found.

CLI_AUTH_SESSION_NOT_FOUND/cli_login_session_not_found 404 API response + Async operation never CLI login session was not found.

CLI_AUTH_SESSION_TERMINAL 409 API response never The CLI login session is no longer pending.

CLI_AUTH_SESSION_TERMINAL/cli_login_session_no_longer_pending 409 API response never CLI login session is no longer pending.

CLI_AUTH_TIMEOUT 500 API response dependency_retry CLI authentication timed out.

Billing

Error identity HTTP Used by Retry Exact message

BILLING_IDEMPOTENCY_CONFLICT 409 API response + Async operation after_user_action This billing request was repeated with different details. Refresh your billing information and try again.

BILLING_NOT_CONFIGURED 503 API response after_delay Billing is temporarily unavailable. Try again later.

BILLING_PLAN_CHANGE_INVALID 409 API response + Async operation after_user_action This plan change is not available for the organization’s current subscription.

BILLING_PORTAL_UNAVAILABLE 503 API response after_delay Payment methods and invoices are temporarily unavailable. Try again later.

BILLING_SUBSCRIPTION_CONFLICT 409 API response + Async operation after_user_action This organization already has an active or pending subscription.

BILLING_TOP_UP_PURCHASE_NOT_FOUND 404 API response after_user_action The requested top-up purchase was not found.

CAPACITY_CAPABILITY_PAUSED 409 API response + Async operation after_user_action This project has reached its temporary capacity allowance. Increase capacity or reduce usage before adding more work.

CAPACITY_CONFIGURATION_INVALID 422 API response + Async operation after_user_action Choose capacity values within the limits and increments shown for this project.

CAPACITY_DECREASE_REQUIRES_CLEANUP 409 API response + Async operation after_user_action Reduce current usage before applying this lower capacity.

CAPACITY_GRACE_CEILING_EXCEEDED 409 API response + Async operation after_user_action This change would exceed the project’s temporary capacity allowance.

CAPACITY_PAYMENT_FAILED 402 API response + Async operation after_user_action The capacity upgrade payment could not be completed. No additional capacity was activated.

CAPACITY_STATE_UNAVAILABLE 503 API response + Async operation after_delay Polygres is still updating this project’s capacity status. Try again shortly.

CREDIT_INSUFFICIENT_BALANCE 409 API response + Async operation after_user_action The available organization credit balance is too low for this action.

PAID_PROJECT_PRICE_CHANGED 409 API response + Async operation after_user_action Paid project pricing changed. Review the updated price before confirming again.

pgContext

Error identity HTTP Used by Retry Exact message

CONTEXT_BACKEND_STILL_RUNNING 400 API response + Async operation after_user_action Context backend still running.

CONTEXT_BINDING_CHANGED 409 API response after_user_action The Context compatibility binding changed before retrieval.

CONTEXT_CAPABILITY_UNAVAILABLE 409 API response + Async operation after_user_action Context capability is unavailable.

CONTEXT_CAPABILITY_UNAVAILABLE/context_operation_identity_not_configured 409 API response + Async operation after_user_action Context operation identity is not configured.

CONTEXT_CAPABILITY_UNAVAILABLE/context_actor_identity_unavailable 409 API response + Async operation after_user_action Context actor identity is unavailable.

CONTEXT_CAPABILITY_UNAVAILABLE/context_joint_lexical_retrieval_not_configured 409 API response + Async operation after_user_action Context Joint lexical retrieval is not configured.

CONTEXT_CAPABILITY_UNAVAILABLE/project_s_context_runtime_schema_not 503 API response + Async operation after_user_action The project’s Context runtime schema is not ready.

CONTEXT_CAPABILITY_UNAVAILABLE/context_text_hybrid_not_configured 409 API response + Async operation after_user_action Context text hybrid is not configured.

CONTEXT_CAPABILITY_UNAVAILABLE/context_limits_unavailable 409 API response + Async operation after_user_action Context limits are unavailable.

CONTEXT_CLEANUP_IDENTITY_MISMATCH 409 API response + Async operation after_user_action Compatibility index identity changed; cleanup stopped safely.

CONTEXT_CLEANUP_IDENTITY_MISMATCH/compatibility_collection_identity_changed_cleanup_stopped 409 API response + Async operation after_user_action Compatibility collection identity changed; cleanup stopped safely.

CONTEXT_CLEANUP_IDENTITY_MISMATCH/compatibility_trigger_identity_changed_cleanup_stopped 409 API response + Async operation after_user_action Compatibility trigger identity changed; cleanup stopped safely.

CONTEXT_CLEANUP_IDENTITY_MISMATCH/compatibility_function_identity_changed_cleanup_stopped 409 API response + Async operation after_user_action Compatibility function identity changed; cleanup stopped safely.

CONTEXT_COLLECTION_AMBIGUOUS 409 API response after_user_action More than one Context collection matches this row target.

CONTEXT_COLLECTION_CATALOG_STALE 409 API response + Async operation after_user_action Context collection catalog stale.

CONTEXT_COLLECTION_NAME_CONFLICT 409 API response + Async operation after_user_action Context collection name is already in use.

CONTEXT_COLLECTION_NOT_FOUND 404 API response + Async operation after_user_action Context collection was not found.

CONTEXT_COLLECTION_NOT_READY 409 API response + Async operation after_user_action Context collection is not ready.

CONTEXT_COLLECTION_REQUIRED 400 API response after_user_action An explicit Context collection is required for this row target.

CONTEXT_COLLECTION_SYNC_FAILED 500 API response + Async operation after_delay Context collection sync failed. Retry the operation. If it fails again, contact support with the operation ID.

CONTEXT_COLLECTION_TARGET_MISMATCH 400 API response after_user_action The Context collection does not target the requested table.

CONTEXT_COMPATIBILITY_PAGE_FALLBACK 409 API response after_user_action This legacy page exceeds the pgContext compatibility window.

CONTEXT_COMPATIBILITY_QUERY_FAILED 503 API response + Async operation after_delay Context compatibility query failed.

CONTEXT_COORDINATOR_CUTOVER_BLOCKED 503 API response + Async operation after_delay Context coordinator cutover requires a drained operation journal.

CONTEXT_COSINE_ZERO_VECTOR 409 API response after_user_action Cosine zero vector.

CONTEXT_DELETE_CONFIRMATION_INVALID 400 API response + Async operation after_user_action Collection deletion confirmation is invalid.

CONTEXT_DELETE_CONFIRMATION_INVALID/context_collection_delete_confirmation_invalid 400 API response + Async operation after_user_action Context collection delete confirmation is invalid.

CONTEXT_DISPATCH_ASSIGNMENT_STALE 409 API response + Async operation after_user_action Context coordinator placement requires reconciliation.

CONTEXT_DISPATCH_ASSIGNMENT_STALE/context_dispatch_pool_assignment_no_longer 409 API response + Async operation after_user_action Context dispatch pool assignment is no longer current.

CONTEXT_DISPATCH_ASSIGNMENT_STALE/context_dispatch_authority_no_longer_current 409 API response + Async operation after_user_action Context dispatch authority is no longer current.

CONTEXT_DISPATCH_ASSIGNMENT_STALE/context_dispatch_target_metadata_stale 409 API response + Async operation after_user_action Context dispatch target metadata is stale.

CONTEXT_DISPATCH_BLOCKED 503 API response + Async operation after_delay The Context operation is waiting for runtime capacity and will retry automatically.

CONTEXT_DISPATCH_PROJECT_SLOT_BUSY 409 API response + Async operation after_user_action The project Context operation slot is occupied.

CONTEXT_EMBEDDING_INVALID 400 API response + Async operation after_user_action Context embedding is invalid.

CONTEXT_EXTENSION_UNAVAILABLE 409 API response + Async operation after_user_action Extension unavailable.

CONTEXT_FILTER_COLUMN_INVALID 409 API response + Async operation after_user_action Filter column invalid.

CONTEXT_FILTER_INVALID 400 API response + Async operation after_user_action Context filter is invalid.

CONTEXT_FILTER_REGISTRATION_CONFLICT 409 API response after_user_action The filter key is already registered to a different source.

CONTEXT_FILTER_REGISTRATION_STALE 409 API response + Async operation after_user_action Context filter registration stale.

CONTEXT_GRAPH_CANDIDATES_UNMAPPED 409 API response after_user_action Some graph candidates were skipped because they are not active Context points.

CONTEXT_GRAPH_DIRECTION_INVALID 400 API response after_user_action Graph direction is invalid.

CONTEXT_GRAPH_NOT_READY 409 API response + Async operation after_user_action Graph retrieval is not ready.

CONTEXT_GRAPH_START_REQUIRED 400 API response after_user_action A graph start entity is required.

CONTEXT_HNSW_UNSUPPORTED 409 API response + Async operation after_user_action Hnsw unsupported.

CONTEXT_IDEMPOTENCY_CONFLICT 409 API response + Async operation after_user_action Idempotency key was used for a different request.

CONTEXT_IDENTIFIER_INVALID 400 API response after_user_action Context identifier is invalid.

CONTEXT_INDEX_ATTACHMENT_STALE 409 API response + Async operation after_user_action Context index attachment stale.

CONTEXT_INDEX_CONFLICT 409 API response + Async operation after_user_action Index conflict.

CONTEXT_INDEX_CONFLICT/pgvector_column_used_by_database_constraint 409 API response + Async operation after_user_action The pgvector column is used by a database constraint and cannot be converted safely.

CONTEXT_INDEX_CORRUPT 500 API response + Async operation after_user_action The Context index failed its integrity check. Rebuild the index. If rebuilding fails, contact support with the operation ID.

CONTEXT_INDEX_MEMORY_BUDGET_EXCEEDED 409 API response + Async operation after_user_action The HNSW index needs more build memory than this project currently allows. Contact support with the operation ID to increase the index-build budget, then retry.

CONTEXT_INDEX_MISSING 409 API response + Async operation after_user_action The compatibility index disappeared during reindex.

CONTEXT_INDEX_MISSING/compatibility_index_disappeared_before_attachment 409 API response + Async operation after_user_action The compatibility index disappeared before attachment.

CONTEXT_INDEX_NOT_READY 409 API response + Async operation after_user_action Context index not ready.

CONTEXT_INLINE_CAPACITY_EXCEEDED 429 API response + Async operation after_delay Another inline Context mutation is already running.

CONTEXT_JSONB_FILTER_PATH_INVALID 409 API response + Async operation after_user_action Jsonb filter path invalid.

CONTEXT_LEGACY_SOURCE_KEY_UNSUPPORTED 400 API response + Async operation after_user_action Context legacy source key unsupported.

CONTEXT_LIMIT_EXCEEDED 400 API response + Async operation after_user_action Context request exceeds a limit.

CONTEXT_LIMIT_EXCEEDED/context_exceeds_effective_limit 400 API response + Async operation after_user_action Context request exceeds the effective limit.

CONTEXT_LIMIT_EXCEEDED/context_exceeds_effective_graph_limit 400 API response + Async operation after_user_action Context request exceeds the effective graph limit.

CONTEXT_MEMORY_PRESSURE 409 API response + Async operation after_user_action Memory pressure.

CONTEXT_MEMORY_PRESSURE/context_heavy_work_blocked_by_project 409 API response + Async operation after_user_action Context heavy work is blocked by project memory pressure.

CONTEXT_MEMORY_PRESSURE/context_operation_database_memory_exhausted 503 API response + Async operation after_user_action The Context operation stopped because the project database ran out of available memory.

CONTEXT_ONBOARDING_NOT_AVAILABLE 409 API response after_user_action Onboarding not available.

CONTEXT_ONBOARDING_NOT_AVAILABLE/context_onboarding_cannot_be_dismissed_its 409 API response after_user_action Context onboarding cannot be dismissed in its current state.

CONTEXT_ONBOARDING_NOT_ELIGIBLE 409 API response after_user_action Onboarding not eligible.

CONTEXT_ONBOARDING_NOT_ELIGIBLE/context_onboarding_does_not_eligible_bridge 409 API response after_user_action Context onboarding does not have an eligible bridge candidate.

CONTEXT_OPERATION_AUTHORITY_LOST 409 API response + Async operation after_user_action Inline Context operation authority is no longer current.

CONTEXT_OPERATION_AUTHORITY_LOST/context_operation_execution_authority_no_longer 409 API response + Async operation after_user_action Context operation execution authority is no longer current.

CONTEXT_OPERATION_AUTHORITY_LOST/context_coordinator_state_unavailable 409 API response + Async operation after_user_action Context coordinator state is unavailable.

CONTEXT_OPERATION_AUTHORITY_LOST/context_operation_no_longer_eligible_dispatch 409 API response + Async operation after_user_action Context operation is no longer eligible for dispatch.

CONTEXT_OPERATION_AUTHORITY_LOST/context_operation_commit_outcome_requires_reconciliation 409 API response + Async operation after_user_action Context operation commit outcome requires reconciliation.

CONTEXT_OPERATION_CANCELLED 409 API response + Async operation after_user_action Context operation was cancelled.

CONTEXT_OPERATION_CONFLICT 409 API response + Async operation after_delay Another Context operation owns this resource.

CONTEXT_OPERATION_CONFLICT/legacy_vector_binding_changed_while_context 409 API response + Async operation after_delay The legacy vector binding changed while Context setup was running.

CONTEXT_OPERATION_CONFLICT/context_operation_transition_invalid 409 API response + Async operation after_delay Context operation transition is invalid.

CONTEXT_OPERATION_CONFLICT/legacy_vector_binding_changed_while_its 409 API response + Async operation after_delay The legacy vector binding changed while its operation was reserved.

CONTEXT_OPERATION_CONFLICT/legacy_vector_binding_changed_while_recovery 409 API response + Async operation after_delay The legacy vector binding changed while recovery was running.

CONTEXT_OPERATION_CONFLICT/compatibility_binding_changed_during_reindex 409 API response + Async operation after_delay The compatibility binding changed during reindex.

CONTEXT_OPERATION_CONFLICT/context_vector_name_already_exists 409 API response + Async operation after_delay A Context vector with this name already exists.

CONTEXT_OPERATION_CONFLICT/vector_column_already_registered_collection 409 API response + Async operation after_delay This vector column is already registered in the collection.

CONTEXT_OPERATION_CONFLICT/only_hnsw_context_collections_can_be 409 API response + Async operation after_delay Only HNSW Context collections can be reindexed.

CONTEXT_OPERATION_CONFLICT/existing_context_collection_does_not_match 409 API response + Async operation after_delay The existing Context collection does not match the replayed operation.

CONTEXT_OPERATION_CONFLICT/new_vector_column_can_only_be 409 API response + Async operation after_delay A new vector column can only be added to an empty source table.

CONTEXT_OPERATION_FAILED 500 API response + Async operation after_delay The Context operation could not be completed.

CONTEXT_OPERATION_FAILED/unsupported_operation_kind 500 API response + Async operation after_delay This Context operation type is not supported.

CONTEXT_OPERATION_NOT_CANCELLABLE 409 API response after_user_action Context operation cannot be cancelled.

CONTEXT_OPERATION_NOT_FOUND 404 API response + Async operation after_user_action Context operation was not found.

CONTEXT_OPERATION_NOT_RETRYABLE 409 API response + Async operation after_user_action Context operation cannot be retried.

CONTEXT_OPERATION_NOT_RETRYABLE/context_operation_exhausted_its_retry_attempts 409 API response + Async operation after_user_action Context operation exhausted its retry attempts.

CONTEXT_OPERATION_NOT_RETRYABLE/context_operation_retry_window_expired 409 API response + Async operation after_user_action Context operation retry window has expired.

CONTEXT_OPERATION_RESERVATION_FAILED 503 API response + Async operation after_delay Context operation replay could not be reconstructed.

CONTEXT_OPERATION_RESERVATION_FAILED/context_operation_reservation_could_not_be 503 API response + Async operation after_delay Context operation reservation could not be confirmed.

CONTEXT_OPERATION_RETRY_EXHAUSTED 500 API response + Async operation after_delay The Context operation could not be completed after several attempts.

CONTEXT_OPERATION_RETRY_EXHAUSTED/execution_attempts_exhausted 500 API response + Async operation after_delay The Context operation could not be completed after several execution attempts.

CONTEXT_OPERATION_RETRY_EXHAUSTED/dispatch_attempts_exhausted 500 API response + Async operation after_delay The Context operation could not be scheduled after several attempts.

CONTEXT_OPERATION_TIMED_OUT 504 API response + Async operation after_delay The Context operation exceeded the processing time limit. Retry the operation.

CONTEXT_PGVECTOR_SOURCE 409 API response after_user_action Pgvector source.

CONTEXT_POINT_CURSOR_INVALID 400 API response + Async operation after_user_action Point cursor is invalid.

CONTEXT_POINT_KEY_INVALID 400 API response after_user_action Context point key is invalid.

CONTEXT_POINT_RECONCILIATION_STALE 409 API response + Async operation after_user_action Legacy vector compatibility recovery could not prove point parity.

CONTEXT_POINT_SCROLL_READER_UNAVAILABLE 503 API response + Async operation after_delay Context point scroll reader unavailable.

CONTEXT_POINT_SCROLL_RLS_UNSAFE 409 API response after_user_action Point scrolling is unavailable because source-table authorization cannot be enforced safely.

CONTEXT_PREFLIGHT_BLOCKED 409 API response + Async operation after_user_action Context preflight blocked collection creation.

CONTEXT_PREFLIGHT_BLOCKED/context_collection_preflight_blocked 409 API response + Async operation after_user_action Context collection preflight is blocked.

CONTEXT_PROJECT_ACCESS_INVALID 400 API response + Async operation after_user_action Context project access invalid.

CONTEXT_QUERY_FAILED 500 API response + Async operation after_delay Context Joint retrieval returned an invalid result.

CONTEXT_RANKING_WEIGHTS_INVALID 400 API response after_user_action Rank-fusion weights are invalid.

CONTEXT_READER_ACCESS_REQUIRED 409 API response + Async operation after_user_action The Context reader cannot be granted access to the source table.

CONTEXT_RECALL_UNAVAILABLE 409 API response + Async operation after_user_action Recall checking is unavailable for this collection.

CONTEXT_REINDEX_IDENTITY_MISMATCH 409 API response + Async operation after_user_action The compatibility index identity changed; reindex stopped safely.

CONTEXT_REQUEST_INVALID 400 API response + Async operation after_user_action Context request is invalid.

CONTEXT_REQUEST_INVALID/context_cursor_invalid 400 API response + Async operation after_user_action Context cursor is invalid.

CONTEXT_RESERVED_FILTER_CONFLICT 409 API response after_user_action Reserved filter conflict.

CONTEXT_RESOURCE_NAMESPACE_MISMATCH 400 API response after_user_action The resource belongs to another retrieval namespace.

CONTEXT_RESULT_COLUMN_INVALID 409 API response + Async operation after_user_action Result column invalid.

CONTEXT_RESULT_COLUMN_STALE 409 API response + Async operation after_user_action Context result column stale.

CONTEXT_RETRIEVAL_SMOKE_FAILED 503 API response + Async operation after_delay A Context retrieval check failed. Verify the collection configuration and try again.

CONTEXT_RUNTIME_UNSUPPORTED 409 API response + Async operation after_user_action Runtime unsupported.

CONTEXT_RUNTIME_UPGRADE_REQUIRED 503 API response + Async operation after_delay The Runtime writer generation is older than the project schema.

CONTEXT_RUNTIME_UPGRADE_REQUIRED/runtime_writer_must_be_upgraded_before 503 API response + Async operation after_delay The Runtime writer must be upgraded before Context mutations resume.

CONTEXT_SOURCE_IDENTITY_CHANGED 409 API response after_user_action The Context compatibility source table identity changed.

CONTEXT_SOURCE_IDENTITY_CHANGED/compatibility_source_table_identity_changed_during 409 API response after_user_action The compatibility source table identity changed during reindex.

CONTEXT_SOURCE_INVALID 400 API response after_user_action Context source is invalid.

CONTEXT_SOURCE_KEY_ALIGNMENT_INVALID 409 API response + Async operation after_user_action Context and graph source identities do not align.

CONTEXT_SOURCE_KEY_INVALID 400 API response after_user_action The Context source key is invalid.

CONTEXT_SOURCE_KEY_MISSING 400 API response after_user_action The row must include the Context source-key column.

CONTEXT_SOURCE_KEY_NOT_FOUND 409 API response after_user_action One or more source keys were not found.

CONTEXT_SOURCE_KEY_REQUIRED 409 API response + Async operation after_user_action The source key must be NOT NULL and uniquely constrained.

CONTEXT_SOURCE_KEY_STALE 409 API response + Async operation after_user_action Context source key stale.

CONTEXT_SOURCE_KEY_TEXT_CONSTRAINT_REQUIRED 409 API response + Async operation after_user_action A text source key must reject empty values and enforce the supported byte-length limit.

CONTEXT_SOURCE_KEY_TYPE_UNSUPPORTED 409 API response + Async operation after_user_action The source key uses an unsupported data type. Use UUID, integer, bigint, text, or varchar.

CONTEXT_SOURCE_OWNERSHIP_MISMATCH 409 API response + Async operation after_user_action The owned Context source table identity is invalid.

CONTEXT_SOURCE_OWNERSHIP_MISMATCH/context_source_table_no_longer_matches 409 API response + Async operation after_user_action The Context source table no longer matches its ownership record.

CONTEXT_SOURCE_PRIVILEGE_REQUIRED 409 API response + Async operation after_user_action Polygres does not have the source-table permissions required to read data and install synchronization triggers.

CONTEXT_SOURCE_TABLE_STALE 409 API response + Async operation after_user_action Context source table stale.

CONTEXT_SOURCE_TABLE_UNSUPPORTED 409 API response + Async operation after_user_action The source table does not match the selected source mode. Check whether the table should already exist.

CONTEXT_SOURCE_UNAVAILABLE 409 API response + Async operation after_user_action The Context collection source table is unavailable.

CONTEXT_SOURCE_UNAVAILABLE/context_collection_source_identity_unavailable 409 API response + Async operation after_user_action The Context collection source identity is unavailable.

CONTEXT_SOURCE_VECTOR_INVALID 409 API response + Async operation after_user_action One or more source vectors are invalid.

CONTEXT_STORAGE_PRESSURE 503 API response + Async operation after_user_action The Context operation stopped because the project database ran out of storage.

CONTEXT_SYNC_TRIGGER_UNAVAILABLE 409 API response + Async operation after_user_action The legacy vector synchronization trigger could not be verified.

CONTEXT_TEXT_COLUMN_INVALID 409 API response + Async operation after_user_action Text column invalid.

CONTEXT_TEXT_COLUMN_REQUIRED 409 API response after_user_action The collection does not have a configured text column.

CONTEXT_UNSUPPORTED_VECTOR_TYPE 409 API response after_user_action Unsupported vector type.

CONTEXT_VECTOR_COLUMN_CONFLICT 409 API response + Async operation after_user_action The requested vector column already exists. Choose a different column name or use existing-column mode.

CONTEXT_VECTOR_COLUMN_MISSING 409 API response + Async operation after_user_action Add and populate a native pgContext vector column before creating the collection.

CONTEXT_VECTOR_DIMENSION_INVALID 409 API response + Async operation after_user_action The vector column dimensions do not match the requested collection dimensions.

CONTEXT_VECTOR_NOT_FOUND 404 API response + Async operation after_user_action Context vector was not found.

CONTEXT_VECTOR_NOT_FOUND/collection_does_not_default_vector 409 API response + Async operation after_user_action The collection does not have a default vector.

CONTEXT_VECTOR_NULLABLE 409 API response after_user_action The vector column contains NULL values. Populate every vector before converting the column.

CONTEXT_VECTOR_REGISTRATION_STALE 409 API response + Async operation after_user_action Context vector registration stale.

CONTEXT_VECTOR_TYPE_UNSUPPORTED 409 API response + Async operation after_user_action The vector column type is not supported for this collection. Use a native pgContext vector or a compatible pgvector column.

CONTEXT_VERIFICATION_FAILED 409 API response + Async operation after_user_action Context collection verification failed.

CONTEXT_VERIFICATION_FAILED/legacy_vector_compatibility_recovery_verification_failed 409 API response + Async operation after_user_action Legacy vector compatibility recovery verification failed.

Core platform

Error identity HTTP Used by Retry Exact message

ACCOUNT_CREATE_FAILED 503 API response + Async operation after_delay Account create failed.

ACCOUNT_NOT_ELIGIBLE 403 API response never This account cannot perform the requested action.

ACCOUNT_NOT_ELIGIBLE/account_cannot_accept_invitations 403 API response never This account cannot accept invitations.

ACCOUNT_NOT_ELIGIBLE/account_cannot_select_invitations 403 API response never This account cannot select invitations.

ACCOUNT_SETUP_FAILED 503 API response + Async operation after_delay Account setup did not return a result.

ADMIN_NOT_ALLOWED 403 API response never Administrator access is required.

ADMISSION_CLAIM_FAILED 503 API response + Async operation after_delay Self-service admission did not return a result.

ADMISSION_POLICY_NOT_FOUND 404 API response + Async operation after_user_action Self-service admission policy was not found.

ADMISSION_POLICY_NOT_UPDATED 409 API response + Async operation after_user_action Self-service admission policy was not updated.

ADMISSION_PROFILE_INELIGIBLE 409 API response after_user_action The user profile is not eligible for self-service admission.

ADMISSION_PROFILE_MISSING 503 API response + Async operation after_delay Admitted user profile was not found.

ADMISSION_TIER_UNAVAILABLE 503 API response + Async operation after_delay The self-service admission tier is unavailable.

ALTER_EVENT_TRIGGER_BLOCKED 400 API response + Async operation after_user_action Alter event trigger blocked.

ALTER_FOREIGN_TABLE_BLOCKED 400 API response + Async operation after_user_action Alter foreign table blocked.

ALTER_LANGUAGE_BLOCKED 400 API response + Async operation after_user_action Alter language blocked.

ALTER_OWNER_BLOCKED 400 API response + Async operation after_user_action Alter owner blocked.

ALTER_ROLE_SUPERUSER_BLOCKED 400 API response + Async operation after_user_action Alter role superuser blocked.

ALTER_SERVER_BLOCKED 400 API response + Async operation after_user_action Alter server blocked.

ALTER_USER_MAPPING_BLOCKED 400 API response + Async operation after_user_action Alter user mapping blocked.

API_KEY_INVALID 401 API response + Async operation never The API key is invalid.

API_KEY_INVALID/api_key_invalid 401 API response + Async operation never API key is invalid.

API_KEY_NOT_FOUND 404 API response + Async operation never API key not found.

APPROVAL_EMAIL_NOT_AVAILABLE 409 API response after_user_action Approval email can only be resent for active approved requests.

APPROVAL_REQUIRED 403 API response + Async operation user_retry Account approval is required.

APPROVAL_REQUIRED/approval_required 403 API response + Async operation user_retry Approval is required.

BILLING_REQUIRED 403 API response + Async operation after_user_action A current eligible organization subscription is required.

CATALOG_UNAVAILABLE 503 API response + Async operation after_delay Project catalog is unavailable.

CATALOG_UNAVAILABLE/project_vector_catalog_unavailable 503 API response + Async operation after_delay Project vector catalog is unavailable.

CLI_UPDATE_REQUIRED 426 API response + Async operation after_user_action This CLI version is no longer supported. Upgrade to the latest version and try again.

CONTROL_PLANE_ERROR 503 API response + Async operation after_delay Memory state was not persisted.

CONTROL_PLANE_ERROR/platform_data_could_not_be_completed 503 API response + Async operation after_delay The platform data request could not be completed. Please try again.

CONTROL_PLANE_ERROR/project_secret_refs_not_persisted 503 API response + Async operation after_delay Project secret refs were not persisted.

CONTROL_PLANE_ERROR/storage_measurement_not_persisted 503 API response + Async operation after_delay Storage measurement was not persisted.

CONTROL_PLANE_ERROR/import_job_not_persisted 503 API response + Async operation after_delay Import job was not persisted.

CONTROL_PLANE_ERROR/migration_not_persisted 503 API response + Async operation after_delay Migration was not persisted.

CONTROL_PLANE_ERROR/vector_configuration_not_persisted 503 API response + Async operation after_delay Vector configuration was not persisted.

CONTROL_PLANE_ERROR/text_configuration_not_persisted 503 API response + Async operation after_delay Text configuration was not persisted.

CONTROL_PLANE_ERROR/metric_sample_not_persisted 503 API response + Async operation after_delay Metric sample was not persisted.

CONTROL_PLANE_ERROR/runtime_event_not_persisted 503 API response + Async operation after_delay Runtime event was not persisted.

CONTROL_PLANE_ERROR/audit_event_not_persisted 503 API response + Async operation after_delay Audit event was not persisted.

CONTROL_PLANE_ERROR/bulk_metric_sample_not_persisted 503 API response + Async operation after_delay A bulk metric sample was not persisted.

CONTROL_PLANE_NOT_CONFIGURED 503 API response + Async operation after_delay Platform data services are temporarily unavailable.

CONTROL_PLANE_UNAVAILABLE 503 API response + Async operation after_delay Platform data is temporarily unavailable. Please try again.

COPY_PROGRAM_BLOCKED 400 API response + Async operation after_user_action Copy program blocked.

CREATE_EVENT_TRIGGER_BLOCKED 400 API response + Async operation after_user_action Create event trigger blocked.

CREATE_FOREIGN_TABLE_BLOCKED 400 API response + Async operation after_user_action Create foreign table blocked.

CREATE_LANGUAGE_BLOCKED 400 API response + Async operation after_user_action Create language blocked.

CREATE_ROLE_SUPERUSER_BLOCKED 400 API response + Async operation after_user_action Create role superuser blocked.

CREATE_SERVER_BLOCKED 400 API response + Async operation after_user_action Create server blocked.

CREATE_USER_MAPPING_BLOCKED 400 API response + Async operation after_user_action Create user mapping blocked.

CURSOR_INVALID 400 API response + Async operation after_user_action Cursor is invalid.

CURSOR_INVALID/cursor_invalid_retrieval 400 API response + Async operation after_user_action Cursor is invalid for this retrieval request.

CURSOR_INVALID/cursor_belongs_inactive_compatibility_generation 400 API response + Async operation after_user_action Cursor belongs to an inactive compatibility generation.

CURSOR_INVALID/cursor_belongs_different_compatibility_generation 400 API response + Async operation after_user_action Cursor belongs to a different compatibility generation.

CURSOR_INVALID/cursor_compatibility_generation_invalid 400 API response + Async operation after_user_action Cursor compatibility generation is invalid.

CURSOR_INVALID/cursor_does_not_match_text_search_request 400 API response + Async operation after_user_action Cursor does not match this text search request.

CURSOR_KIND_MISMATCH 400 API response + Async operation after_user_action Cursor kind does not match route.

DASHBOARD_PUBLIC_BASE_URL_INVALID 503 API response + Async operation after_delay Dashboard public base URL must be an absolute URL.

DASHBOARD_PUBLIC_BASE_URL_REQUIRED 503 API response + Async operation after_delay Dashboard public base URL must be configured.

DATABASE_OPERATION_FAILED 503 API response + Async operation after_delay A database operation failed.

DIRECT_RUNTIME_ACCESS_DISABLED 503 API response + Async operation after_delay Direct Runtime access is disabled.

DIRECT_RUNTIME_GRAPH_MANAGE_DISABLED 503 API response + Async operation after_delay Direct Runtime graph management is disabled.

DROP_EVENT_TRIGGER_BLOCKED 400 API response + Async operation after_user_action Drop event trigger blocked.

DROP_FOREIGN_TABLE_BLOCKED 400 API response + Async operation after_user_action Drop foreign table blocked.

DROP_LANGUAGE_BLOCKED 400 API response + Async operation after_user_action Drop language blocked.

DROP_OWNED_BLOCKED 400 API response + Async operation after_user_action Drop owned blocked.

DROP_SERVER_BLOCKED 400 API response + Async operation after_user_action Drop server blocked.

DROP_USER_MAPPING_BLOCKED 400 API response + Async operation after_user_action Drop user mapping blocked.

EXPRESSION_INDEX_UNSUPPORTED 400 API response + Async operation after_user_action Expression index unsupported.

IDENTIFIER_INVALID 400 API response + Async operation after_user_action SQL identifier is invalid.

ID_INVALID 400 API response + Async operation after_user_action ID invalid.

INDEX_INVALID 400 API response + Async operation after_user_action Index invalid.

INDEX_NOT_READY 409 API response + Async operation after_user_action Index not ready.

INTERNAL_ERROR 500 API response + Async operation never The authentication request failed. Please wait a while and try again. If it continues, contact support.

INTERNAL_ERROR/unexpected_server_error_occurred 500 API response + Async operation never An unexpected server error occurred.

INTERNAL_ERROR/failed_revoke_invitation 503 API response + Async operation never Failed to revoke invitation.

INVALID_INVITATION_ROLE 422 API response user_retry The invitation role is invalid.

INVALID_TOKEN 401 API response user_retry The authentication token is invalid.

KEY_VAULT_NOT_CONFIGURED 503 API response + Async operation after_delay Native database password reveal requires the Key Vault adapter.

KUBECTL_FAILED 503 API response + Async operation after_delay Kubectl failed.

KUBECTL_NOT_FOUND 503 API response + Async operation after_delay kubectl is required for Kubernetes project provisioning.

KUBECTL_TIMEOUT 503 API response after_delay kubectl command timed out while provisioning the project runtime.

KUBERNETES_API_UNAVAILABLE 503 API response + Async operation after_delay Database setup is temporarily delayed because the runtime service is unavailable. Polygres will retry automatically.

KUBERNETES_CONFIGURATION_ERROR 400 API response + Async operation after_user_action We couldn’t finish setting up your database because the runtime configuration needs attention. Contact support with the project ID and error code.

KUBERNETES_INSPECTION_UNAVAILABLE 503 API response + Async operation after_delay Kubernetes inspection unavailable.

KUBERNETES_PORT_FORWARD_FAILED 503 API response + Async operation after_delay Kubernetes database port forwarding failed.

KUBERNETES_RBAC_NOT_CONFIGURED 503 API response + Async operation after_delay kubectl does not have the required project provisioning permissions.

KUBERNETES_RESPONSE_INVALID 503 API response + Async operation after_delay Kubernetes returned invalid JSON while inspecting runtime state.

KUBERNETES_RUNTIME_RESOURCE_MISSING 503 API response + Async operation after_delay Kubernetes runtime resource was not created before the provisioning timeout.

LEGAL_ACCEPTANCE_REQUIRED 422 API response user_retry Current legal terms must be accepted to continue.

LIMIT_OUT_OF_RANGE 400 API response after_user_action Limit must be within the allowed range.

LIMIT_OUT_OF_RANGE/default_limit_cannot_exceed_max_limit 400 API response after_user_action default_limit cannot exceed max_limit.

LIMIT_OUT_OF_RANGE/graph_depth_exceeds_runtime_limit 400 API response after_user_action max_depth exceeds this project’s runtime limit. Reduce max_depth and retry.

LOCAL_SESSION_CORRUPT 401 API response never The local session cannot be read and must be repaired.

LOCAL_SESSION_RESET_LIMIT_REACHED 409 API response user_retry Automatic session repair has already been attempted.

LO_EXPORT_BLOCKED 400 API response + Async operation after_user_action Lo export blocked.

LO_IMPORT_BLOCKED 400 API response + Async operation after_user_action Lo import blocked.

MAINTENANCE_FULL 503 API response after_delay Polygres is temporarily unavailable for scheduled maintenance. Try again after the maintenance window.

MAINTENANCE_READ_ONLY 503 API response after_delay Polygres is temporarily read-only for scheduled maintenance. Read requests are still available.

NOT_FOUND 404 API response + Async operation never Resource not found.

NOT_FOUND/route_not_found_check_method_path 404 API response + Async operation never Route not found. Check the request method and path against the API documentation.

ONBOARDING_NOT_FOUND 404 API response + Async operation after_user_action Onboarding request not found.

ONBOARDING_REQUEST_NOT_FOUND 404 API response + Async operation after_user_action Onboarding request not found.

OPERATOR_CLASS_UNSUPPORTED 400 API response + Async operation after_user_action Operator class unsupported.

PARTIAL_INDEX_PREDICATE_UNSUPPORTED 400 API response + Async operation after_user_action Partial index predicate unsupported.

PASSWORD_NOT_FOUND 404 API response + Async operation after_user_action Password not found.

PASSWORD_RESET_FAILED 500 API response + Async operation after_delay Generated database password was empty.

PASSWORD_RESET_RUNTIME_SYNC_FAILED 503 API response + Async operation after_delay Database password reset could not update the project runtime.

PASSWORD_RESET_UNSUPPORTED 503 API response + Async operation after_delay Database password reset is not supported for this secret store.

PASSWORD_RESET_UNSUPPORTED/database_password_reset_requires_managed_project 503 API response + Async operation after_delay Database password reset requires managed project secret references.

PERMISSION_DENIED 403 API response never Permission denied.

PG_LS_DIR_BLOCKED 400 API response + Async operation after_user_action Pg ls dir blocked.

PG_READ_BINARY_FILE_BLOCKED 400 API response + Async operation after_user_action Pg read binary file blocked.

PG_READ_FILE_BLOCKED 400 API response + Async operation after_user_action Pg read file blocked.

PG_STAT_FILE_BLOCKED 400 API response + Async operation after_user_action Pg stat file blocked.

POSTGRES_ANALYTICS_DELIVERY_FAILED 503 API response + Async operation after_delay PostgreSQL analytics ingestion could not reach PostHog.

POSTGRES_ANALYTICS_DISABLED 503 API response + Async operation after_delay PostgreSQL analytics ingestion is unavailable.

POSTGRES_ANALYTICS_UNAUTHORIZED 401 API response after_user_action PostgreSQL analytics credentials are invalid.

POSTGRES_ANALYTICS_UNAVAILABLE 503 API response + Async operation after_delay PostgreSQL analytics ingestion is unavailable.

PROFILE_NOT_FOUND 404 API response + Async operation after_user_action User profile was not found.

PROVISIONING_FAILED 500 API response + Async operation after_delay Local runtime provisioning failed.

PROVISIONING_FAILED/local_shared_runtime_pool_provisioning_failed 500 API response + Async operation after_delay Local shared runtime pool provisioning failed.

PROVISIONING_NOT_CONFIGURED 503 API response + Async operation after_delay Secret storage is not ready for Kubernetes project provisioning.

PROVISIONING_NOT_CONFIGURED/azure_key_vault_secret_storage_not 503 API response + Async operation after_delay Azure Key Vault secret storage is not configured for this runtime.

PROVISIONING_NOT_CONFIGURED/kubernetes_shared_runtime_pool_provisioning_not 503 API response + Async operation after_delay Kubernetes shared runtime pool provisioning is not ready.

PROVISIONING_NOT_CONFIGURED/azure_key_vault_dependencies_not_installed 503 API response + Async operation after_delay Azure Key Vault dependencies are not installed for this runtime.

PROVISIONING_NOT_CONFIGURED/azure_client_secret_must_not_be 503 API response + Async operation after_delay AZURE_CLIENT_SECRET must not be set in the production API container.

PROVISIONING_NOT_CONFIGURED/azure_managed_identity_client_id_required 503 API response + Async operation after_delay Azure managed identity client ID is required in production.

PROVISIONING_NOT_CONFIGURED/project_provisioning_not_configured_runtime 503 API response + Async operation after_delay Project provisioning is not configured for this runtime.

PROVISIONING_RETRY_UNAVAILABLE 409 API response + Async operation after_user_action Provisioning retry is not available for this project.

REASSIGN_OWNED_BLOCKED 400 API response + Async operation after_user_action Reassign owned blocked.

RECOVERY_GRANT_INVALID 403 API response user_retry The password-recovery session is no longer valid.

REGISTRATION_CURSOR_INVALID 422 API response + Async operation after_user_action registration_after must include a timezone.

REGISTRATION_CURSOR_INVALID/registration_after_required_when_registration_after 422 API response + Async operation after_user_action registration_after is required when registration_after_id is provided.

REGISTRATION_CURSOR_INVALID/monitored_user_profile_missing_its_creation 503 API response + Async operation after_user_action A monitored user profile is missing its creation timestamp.

ROADMAP_ALREADY_VOTED 409 API response after_user_action You already voted for this roadmap item.

ROADMAP_ITEM_NOT_CREATED 503 API response + Async operation after_delay Roadmap item was not created.

ROADMAP_ITEM_NOT_FOUND 404 API response + Async operation after_user_action Roadmap item not found.

ROADMAP_ITEM_NOT_VOTEABLE 409 API response after_user_action Roadmap item is not voteable.

ROADMAP_ITEM_UPDATE_EMPTY 400 API response after_user_action Roadmap item update is empty.

ROADMAP_SUGGESTION_NOT_CREATED 503 API response + Async operation after_delay Roadmap suggestion was not created.

ROADMAP_SUGGESTION_NOT_FOUND 404 API response + Async operation after_user_action Roadmap suggestion not found.

ROADMAP_SUGGESTION_UPDATE_EMPTY 400 API response after_user_action Roadmap suggestion update is empty.

ROADMAP_VOTE_NOT_CREATED 503 API response + Async operation after_delay Roadmap vote was not created.

ROADMAP_VOTE_NOT_FOUND 404 API response + Async operation after_user_action Active roadmap vote not found.

SDK_IDENTITY_CONFLICT 400 API response + Async operation after_user_action Polygres SDK identity headers disagree.

SDK_VERSION_UNSUPPORTED 426 API response + Async operation after_user_action This project requires Polygres SDK 0.2.0 or later.

SECRET_BACKEND_UNAVAILABLE 503 API response + Async operation after_delay Database setup is temporarily delayed because secure credential storage is unavailable. Polygres will retry automatically.

SECRET_NAME_INVALID 500 API response + Async operation after_delay Project secret name is invalid for Azure Key Vault.

SECRET_URI_INVALID 500 API response + Async operation after_delay Secret URI is invalid for the local secret store.

SECRET_URI_INVALID/secret_uri_invalid_azure_key_vault 500 API response + Async operation after_delay Secret URI is invalid for the Azure Key Vault secret store.

SECRET_URI_INVALID/azure_key_vault_secret_uri_must 500 API response + Async operation after_delay Azure Key Vault secret URI must include a secret name.

SECRET_URI_INVALID/secret_uri_invalid_kubernetes_secret_store 500 API response + Async operation after_delay Secret URI is invalid for the Kubernetes secret store.

SECRET_URI_INVALID/kubernetes_secret_uri_must_include_namespace 500 API response + Async operation after_delay Kubernetes secret URI must include namespace, secret name, and field.

SECRET_URI_INVALID/azure_key_vault_did_not_return 503 API response + Async operation after_delay Azure Key Vault did not return a usable secret URI.

SELF_INVITE_NOT_ALLOWED 400 API response user_retry You cannot invite your own email address.

SET_ROLE_BLOCKED 400 API response + Async operation after_user_action Set role blocked.

SET_SESSION_AUTHORIZATION_BLOCKED 400 API response + Async operation after_user_action Set session authorization blocked.

STORAGE_LIMIT_EXCEEDED 409 API response + Async operation after_user_action Project storage usage still exceeds the effective tier limit.

STORAGE_READ_ONLY_NOT_ACTIVE 409 API response after_user_action Project is not in storage read-only mode.

TABLE_NOT_FOUND 404 API response + Async operation after_user_action Table not found.

TOKEN_EXPIRED 401 API response bounded_retry The authentication token has expired.

UNSUPPORTED_API_VERSION 400 API response after_user_action The requested Runtime API version is not supported.

UNTRUSTED_LANGUAGE_BLOCKED 400 API response + Async operation after_user_action Untrusted language blocked.

USER_NOT_FOUND 404 API response + Async operation after_user_action User not found.

USE_CONTEXT_HYBRID_JOINT 400 API response after_user_action This request targets a pgContext-backed vector configuration. Use POST /v1/context/hybrid/joint with the bound collection instead of POST /v1/hybrid/joint.

VALIDATION_ERROR 422 API response + Async operation user_retry The request is invalid. Review the request fields and try again.

VALIDATION_ERROR/unsupported_multipart_field 422 API response + Async operation user_retry Unsupported multipart field.

VALIDATION_ERROR/csv_import_invalid 422 API response + Async operation user_retry CSV import request is invalid.

VALIDATION_ERROR/validation_failed_review_errors_correct_fields 422 API response + Async operation user_retry Request validation failed. Review the errors and correct the request fields.

VALIDATION_ERROR/multipart_csv_upload_required 422 API response + Async operation user_retry A multipart CSV upload is required.

VALIDATION_ERROR/multipart_field_name_required 422 API response + Async operation user_retry Multipart field name is required.

VALIDATION_ERROR/multipart_field_too_large 422 API response + Async operation user_retry Multipart field is too large.

VALIDATION_ERROR/only_one_csv_upload_file_allowed 422 API response + Async operation user_retry Only one CSV upload file is allowed.

VALIDATION_ERROR/csv_upload_did_not_contain_file 422 API response + Async operation user_retry CSV upload did not contain a file.

VALIDATION_ERROR/multipart_fields_must_use_utf_8 422 API response + Async operation user_retry Multipart fields must use UTF-8.

VALIDATION_ERROR/boolean_multipart_field_invalid 422 API response + Async operation user_retry Boolean multipart field is invalid.

VALIDATION_ERROR/sample_row_count_must_be_between 422 API response + Async operation user_retry sample_row_count must be between 1 and 200.

VALIDATION_ERROR/csv_import_mode_invalid 422 API response + Async operation user_retry CSV import mode is invalid.

VALIDATION_ERROR/csv_import_file_required_legacy_multipart 422 API response + Async operation user_retry CSV import file is required for legacy multipart confirmation.

VALIDATION_ERROR/csv_import_missing_required_multipart_fields 422 API response + Async operation user_retry CSV import request is missing required multipart fields.

VALIDATION_ERROR/target_table_required 422 API response + Async operation user_retry target_table is required.

VALIDATION_ERROR/csv_import_must_be_valid_json 422 API response + Async operation user_retry CSV import request must be valid JSON.

VALIDATION_ERROR/sample_row_count_must_be_integer 422 API response + Async operation user_retry sample_row_count must be an integer.

Data plane

Error identity HTTP Used by Retry Exact message

DATA_PLANE_CONNECTION_FAILED 503 API response + Async operation after_delay Project data-plane connection failed.

DATA_PLANE_CONNECTION_FAILED/context_operation_connection_lost 503 API response + Async operation after_delay Connection to the project database was lost during the Context operation. Retry the operation.

DATA_PLANE_CONNECTION_INVALID 500 API response + Async operation after_delay Invalid connection.

DATA_PLANE_CONNECTION_INVALID/table_browsing_must_use_pooled_project 500 API response + Async operation after_delay Table browsing must use a pooled project-owner connection.

DATA_PLANE_CONNECTION_INVALID/runtime_api_only_supports_project_owner 500 API response + Async operation after_delay Runtime API only supports project-owner connections.

DATA_PLANE_CONNECTION_INVALID/platform_admin_data_plane_connections_must 500 API response + Async operation after_delay Platform admin data-plane connections must be direct.

DATA_PLANE_CONNECTION_INVALID/sql_editor_execution_must_use_direct 500 API response + Async operation after_delay SQL editor execution must use a direct project-owner connection.

DATA_PLANE_CONNECTION_INVALID/sql_script_execution_must_use_direct 500 API response + Async operation after_delay SQL script execution must use a direct project-owner connection.

DATA_PLANE_CONNECTION_INVALID/csv_import_execution_must_use_direct 500 API response + Async operation after_delay CSV import execution must use a direct project-owner connection.

DATA_PLANE_CONNECTION_INVALID/plain_pg_dump_restore_must_use 500 API response + Async operation after_delay Plain pg_dump restore must use a direct project-owner connection.

DATA_PLANE_CONNECTION_INVALID/custom_pg_dump_restore_must_use 500 API response + Async operation after_delay Custom pg_dump restore must use a direct project-owner connection.

DATA_PLANE_CONNECTION_UNRESOLVED 503 API response after_delay Project data-plane host is not available.

DATA_PLANE_CONNECTION_UNRESOLVED/basic_upgrade_migration_requires_direct_connection 503 API response after_delay Basic project migration requires a direct data-plane connection.

DATA_PLANE_CONNECTION_UNRESOLVED/basic_upgrade_target_not_registered 503 API response after_delay Basic project data-plane registration is not ready.

DATA_PLANE_CONNECTION_UNRESOLVED/project_data_plane_credentials_not_configured 503 API response after_delay Project data-plane credentials are not configured.

DATA_PLANE_DRIVER_UNAVAILABLE 503 API response + Async operation after_delay SQL script execution driver is not available.

DATA_PLANE_NOT_CONFIGURED 503 API response + Async operation after_delay Project query execution is not configured for this runtime. Ask the project operator to configure the data plane.

DATA_PLANE_QUERY_FAILED 400 API response + Async operation after_user_action Data-plane query failed.

DATA_PLANE_RESPONSE_INVALID 502 API response + Async operation dependency_retry The data plane returned an invalid response.

DATA_PLANE_RESPONSE_INVALID/pggraph_invalid_path_response 502 API response + Async operation dependency_retry pgGraph returned an invalid path response.

DATA_PLANE_SECRET_UNAVAILABLE 503 API response + Async operation after_delay Project data-plane credentials are not available.

DATA_PLANE_SQL_FAILED 503 API response + Async operation after_delay The database could not complete this operation. Review the input and try again.

DATA_PLANE_SQL_FAILED/column_not_found 400 API response + Async operation after_delay A required column does not exist. Check the target table and column mapping, then try again.

DATA_PLANE_SQL_FAILED/disk_full 409 API response + Async operation after_delay The project does not have enough storage to complete this operation.

DATA_PLANE_SQL_FAILED/foreign_key_violation 400 API response + Async operation after_delay This operation references rows that do not exist. Import the referenced rows first or correct the references.

DATA_PLANE_SQL_FAILED/invalid_value 400 API response + Async operation after_delay A value does not match the target column type. Check the source values and column mapping.

DATA_PLANE_SQL_FAILED/not_null_violation 400 API response + Async operation after_delay A required column contains an empty value. Add the missing value and try again.

DATA_PLANE_SQL_FAILED/out_of_memory 503 API response + Async operation after_delay The database ran out of memory while processing this operation. Reduce the input size or split it into smaller batches.

DATA_PLANE_SQL_FAILED/permission_denied 403 API response + Async operation after_delay The database denied this operation. Remove actions that are not permitted for this project.

DATA_PLANE_SQL_FAILED/relation_not_found 400 API response + Async operation after_delay A required table or view does not exist. Create or import it before trying again.

DATA_PLANE_SQL_FAILED/syntax_error 400 API response + Async operation after_delay The SQL contains a syntax error. Correct the SQL and try again.

DATA_PLANE_SQL_FAILED/timeout 408 API response + Async operation after_delay The database operation exceeded its time limit and was cancelled. Try again with a smaller input.

DATA_PLANE_SQL_FAILED/unique_violation 409 API response + Async operation after_delay This operation conflicts with an existing unique value. Remove duplicate values and try again.

Email

Error identity HTTP Used by Retry Exact message

EMAIL_DELIVERY_FAILED 503 API response + Async operation dependency_retry The email couldn’t be delivered. Wait a moment and try the email action again.

EMAIL_DELIVERY_FAILED/email_couldn_t_be_sent_wait 503 API response + Async operation dependency_retry The email couldn’t be sent. Wait a moment and try the email action again; contact support with the request ID if it continues.

EMAIL_NOT_CONFIGURED 503 API response + Async operation after_delay Production email delivery is not configured for this runtime.

EMAIL_NOT_VERIFIED 403 API response user_retry Verify the account email before continuing.

EMAIL_NOT_VERIFIED/email_verification_required 403 API response user_retry Email verification is required.

EMAIL_TEMPLATE_NOT_FOUND 503 API response + Async operation after_delay Email template was not found.

EMAIL_VERIFICATION_EVIDENCE_MISMATCH 403 API response + Async operation after_user_action Email verification evidence did not match the authenticated identity.

EMAIL_VERIFICATION_LINK_FAILED 503 API response + Async operation after_delay Email verification link could not be generated.

EMAIL_VERIFICATION_PROFILE_MISMATCH 409 API response + Async operation after_user_action Email verification profile did not match the authenticated identity.

EMAIL_VERIFICATION_PROFILE_NOT_FOUND 404 API response + Async operation after_user_action Email verification profile was not found.

EMAIL_VERIFICATION_SYNC_FAILED 503 API response + Async operation after_delay Email verification could not be synchronized.

Graph

Error identity HTTP Used by Retry Exact message

GRAPH_ACTIVATION_FAILED 503 API response + Async operation after_delay Runtime now reflects the failed graph activation state.

GRAPH_ACTIVATION_STALE 409 API response + Async operation after_user_action A newer graph activation has already been synchronized.

GRAPH_ACTIVATION_STALE/newer_graph_activation_already_been_synchronized 409 API response + Async operation after_user_action A newer graph activation has already been synchronized.

GRAPH_ACTIVATION_VERIFICATION_FAILED 409 API response + Async operation after_user_action The applied graph does not match its configuration.

GRAPH_ACTIVATION_VERIFICATION_UNAVAILABLE 503 API response + Async operation after_delay Graph activation verification is unavailable.

GRAPH_ACTIVATION_VERSION_UNAVAILABLE 503 API response + Async operation after_delay A graph activation version could not be allocated.

GRAPH_BUILD_FAILED 400 API response + Async operation after_user_action Graph build failed. Review the failure recorded in graph status, correct it if possible, then retry the build. If no failure details are available, contact support.

GRAPH_BUILD_POPULATION_MISMATCH 409 API response + Async operation after_user_action The refreshed Runtime connection does not see the rebuilt graph.

GRAPH_COLUMN_NOT_FOUND 400 API response + Async operation after_user_action Configured column was not found.

GRAPH_COLUMN_NOT_SYNCABLE 400 API response after_user_action Configured column is not eligible for pgGraph sync.

GRAPH_CONCURRENT_BUILD_UNAVAILABLE 409 API response + Async operation after_user_action Basic projects build graphs synchronously. Retry with concurrent set to false.

GRAPH_CONFIGURATION_EMPTY 409 API response after_user_action Graph configuration is empty. Register at least one graph table, build the graph, and retry.

GRAPH_CONFIGURATION_INVALID 400 API response + Async operation after_user_action A graph table requires an id column.

GRAPH_CONFIGURATION_INVALID/use_either_id_column_id_columns 400 API response + Async operation after_user_action Use either id_column or id_columns, not both.

GRAPH_CONFIGURATION_NOT_FOUND 404 API response + Async operation after_user_action Graph configuration not found.

GRAPH_DISCOVERY_FORBIDDEN 500 API response + Async operation after_delay pgGraph auto-discovery is not allowed in registration or build plans.

GRAPH_FILTER_INVALID 400 API response + Async operation after_user_action Graph filter is invalid.

GRAPH_FILTER_NOT_REGISTERED 400 API response after_user_action Graph filter is not registered.

GRAPH_FILTER_SCOPE_INVALID 400 API response after_user_action The graph filters do not belong to one common target table.

GRAPH_FILTER_SCOPE_INVALID/filters_do_not_share_target_table 400 API response after_user_action The graph filters do not belong to one common target table.

GRAPH_FILTER_SCOPE_INVALID/filters_not_registered_requested_target 400 API response after_user_action The graph filters are not registered on the requested target table.

GRAPH_FILTER_SCOPE_INVALID/target_not_registered_graph_table 400 API response after_user_action The graph filter target is not a registered graph table.

GRAPH_FILTER_SCOPE_REQUIRED 400 API response after_user_action Choose the target table for these graph filters.

GRAPH_FILTER_SCOPE_UNSAFE 400 API response after_user_action The filter has conflicting types across graph tables.

GRAPH_FILTER_TYPE_UNSUPPORTED 400 API response + Async operation after_user_action Graph filter column type is unsupported.

GRAPH_ID_NOT_STABLE 400 API response after_user_action Graph table ID column is not a stable key.

GRAPH_MAINTENANCE_FAILED 400 API response + Async operation after_user_action Graph maintenance failed. Review graph status and retry maintenance. If the failure continues, contact support.

GRAPH_NODE_NOT_FOUND 400 API response + Async operation after_user_action The graph start node does not exist in its source table.

GRAPH_NOT_READY 409 API response + Async operation after_user_action Graph not ready.

GRAPH_REBUILD_REQUIRED 409 API response + Async operation after_user_action Rebuild the graph before running maintenance.

GRAPH_RELATIONSHIP_NOT_FOUND 400 API response + Async operation after_user_action Graph relationship was not found in the catalog.

GRAPH_RELATIONSHIP_TYPE_NOT_FOUND 400 API response + Async operation after_user_action One or more requested graph relationship types are not registered.

GRAPH_SCHEMA_NOT_ALLOWED 400 API response + Async operation after_user_action Graph configuration cannot reference system schema tables.

GRAPH_STATUS_UNAVAILABLE 503 API response + Async operation after_delay Graph status is unavailable.

GRAPH_TABLE_NOT_FOUND 400 API response + Async operation after_user_action Graph table not found.

GRAPH_TENANT_AMBIGUOUS 400 API response after_user_action Graph tenant filters must resolve to one tenant value.

GRAPH_TENANT_AMBIGUOUS/graph_start_table_multiple_possible_tenant 400 API response after_user_action The graph start table has multiple possible tenant columns.

GRAPH_TENANT_LOOKUP_UNSUPPORTED 400 API response + Async operation after_user_action Tenant-scoped graph expansion does not support a compound start identifier.

GRAPH_TENANT_MISMATCH 400 API response + Async operation after_user_action The graph tenant filter does not match the start node tenant.

GRAPH_TENANT_REQUIRED 400 API response + Async operation after_user_action The graph start node does not provide the tenant scope required by this graph.

Hybrid retrieval

Error identity HTTP Used by Retry Exact message

HYBRID_DIRECTION_INVALID 400 API response + Async operation after_user_action Hybrid direction must be out, in, any, or both.

HYBRID_MODE_UNSUPPORTED 400 API response + Async operation after_user_action Hybrid mode is not supported.

HYBRID_START_REQUIRED 400 API response + Async operation after_user_action Hybrid graph retrieval requires a start node.

HYBRID_WEIGHTS_INVALID 400 API response + Async operation after_user_action Hybrid weights contain unsupported keys.

HYBRID_WEIGHTS_INVALID/hybrid_weights_must_be_finite_non 400 API response + Async operation after_user_action Hybrid weights must be finite non-negative numbers.

HYBRID_WEIGHTS_INVALID/at_least_one_hybrid_weight_must 400 API response + Async operation after_user_action At least one hybrid weight must be greater than zero.

Imports

Error identity HTTP Used by Retry Exact message

CSV_DELIMITER_UNSUPPORTED 400 API response + Async operation after_user_action CSV delimiter is unsupported.

CSV_ENCODING_INVALID 400 API response + Async operation after_user_action CSV file could not be decoded with the requested encoding.

CSV_ENCODING_UNSUPPORTED 400 API response + Async operation after_user_action CSV encoding is unsupported.

CSV_HEADERS_DUPLICATE 400 API response after_user_action CSV headers must be unique.

CSV_MAPPING_INVALID 400 API response + Async operation after_user_action CSV mapping references unknown preview columns.

CSV_PREVIEW_LIMIT_EXCEEDED 400 API response + Async operation after_user_action CSV preview could not collect the requested sample within the preview limit.

CSV_VALIDATION_FAILED 400 API response + Async operation after_user_action CSV validation failed.

CSV_VALIDATION_FAILED/csv_row_different_column_count_than 400 API response + Async operation after_user_action CSV row has a different column count than the header.

IMPORT_CANCELLED 409 API response + Async operation after_user_action Import job was cancelled.

IMPORT_COLUMNS_REQUIRED 400 API response + Async operation after_user_action CSV import requires columns.

IMPORT_COLUMNS_REQUIRED/csv_create_table_import_requires_columns 400 API response + Async operation after_user_action CSV create-table import requires columns.

IMPORT_COLUMN_TYPE_INVALID 400 API response + Async operation after_user_action Import column type invalid.

IMPORT_CONCURRENCY_LIMIT 409 API response after_user_action Import concurrency limit reached for this project.

IMPORT_CSV_EMPTY 400 API response after_user_action CSV file is empty.

IMPORT_FILE_INVALID 400 API response + Async operation after_user_action Import filename is invalid.

IMPORT_FILE_INVALID/csv_multipart_upload_ended_unexpectedly 400 API response + Async operation after_user_action CSV multipart upload ended unexpectedly.

IMPORT_FILE_INVALID/import_job_not_csv_preview 400 API response + Async operation after_user_action Import job is not a CSV preview.

IMPORT_FILE_MISMATCH 409 API response + Async operation after_user_action CSV import file must match the preview upload.

IMPORT_FILE_MISMATCH/uploaded_csv_size_does_not_match 409 API response + Async operation after_user_action Uploaded CSV size does not match the local file.

IMPORT_FOREIGN_SCHEMA_BLOCKED 400 API response + Async operation after_user_action Import foreign schema blocked.

IMPORT_JOB_ID_CONFLICT 409 API response + Async operation after_user_action Import job ID is already associated with another upload.

IMPORT_JOB_NOT_FOUND 404 API response + Async operation after_user_action Import job not found.

IMPORT_LIMIT_EXCEEDED 413 API response + Async operation never File exceeds the tier upload limit.

IMPORT_LIMIT_EXCEEDED/file_exceeds_project_tier_storage_limit 413 API response + Async operation never File exceeds the project tier storage limit.

IMPORT_NOT_CANCELLABLE 409 API response + Async operation after_user_action Import job cannot be cancelled in its current state.

IMPORT_PREVIEW_MISMATCH 409 API response + Async operation after_user_action CSV import target must match the preview.

IMPORT_PREVIEW_MISMATCH/csv_import_parser_settings_must_match 409 API response + Async operation after_user_action CSV import parser settings must match the preview.

IMPORT_RLS_COPY_UNSUPPORTED 409 API response + Async operation after_user_action The target table enabled row-level security while the import was running. Retry the import.

IMPORT_RLS_REPLACE_UNSUPPORTED 409 API response + Async operation after_user_action Replacing an RLS-protected table is not supported. Use an append import or a tenant-scoped database migration.

IMPORT_RLS_WRITE_POLICY_REQUIRED 403 API response + Async operation after_user_action The target table’s row-level security policy does not permit this import.

IMPORT_RUNTIME_NOT_CONFIGURED 503 API response + Async operation after_delay Import runtime not configured.

IMPORT_STAGED_FILE_MISMATCH 409 API response + Async operation after_user_action The staged CSV no longer matches its preview metadata.

IMPORT_STAGED_FILE_MISSING 409 API response + Async operation after_user_action The staged CSV upload is no longer available.

IMPORT_STAGING_READ_FAILED 503 API response + Async operation after_delay The staged CSV could not be read.

IMPORT_STAGING_READ_FAILED/staged_csv_preview_could_not_be 503 API response + Async operation after_delay The staged CSV preview could not be extended.

IMPORT_STAGING_UNAVAILABLE 503 API response + Async operation after_delay CSV staging storage is unavailable.

IMPORT_STATE_INVALID 409 API response + Async operation after_user_action CSV import preview is not ready for execution.

IMPORT_STORAGE_LIMIT_EXCEEDED 413 API response + Async operation after_user_action Import exceeds the remaining project storage allowance.

IMPORT_TARGET_COLUMN_INVALID 400 API response + Async operation after_user_action CSV import mapping references target columns that do not exist.

IMPORT_TARGET_NOT_FOUND 404 API response + Async operation after_user_action CSV import target table does not exist.

IMPORT_TENANT_CONTEXT_REQUIRED 409 API response + Async operation after_user_action The project organization context required for this RLS import is unavailable.

IMPORT_UPLOAD_DISCONNECTED 400 API response after_user_action CSV upload was interrupted.

IMPORT_UPLOAD_SESSION_MISMATCH 409 API response + Async operation after_user_action CSV upload session does not match the requested job.

PG_DUMP_ARCHIVE_INVALID 400 API response + Async operation after_user_action Custom-format pg_dump archive is invalid.

PG_DUMP_ARCHIVE_INVALID/custom_format_pg_dump_archive_could 400 API response + Async operation after_user_action Custom-format pg_dump archive could not be decoded.

PG_DUMP_ARCHIVE_VERSION_UNSUPPORTED 400 API response + Async operation after_user_action This pg_dump archive was created by a newer PostgreSQL version than the restore service supports. Use a compatible pg_dump version and try again.

PG_DUMP_CUSTOM_BODY_REQUIRED 400 API response + Async operation after_user_action Pg dump custom body required.

PG_DUMP_CUSTOM_RESTORE_UNAVAILABLE 503 API response + Async operation after_delay Pg dump custom restore unavailable.

PG_DUMP_FORMAT_MISMATCH 400 API response + Async operation after_user_action The selected pg_dump format does not match this file.

PG_DUMP_FORMAT_MISMATCH/custom_archive_uploaded_as_plain 400 API response + Async operation after_user_action This file is a custom-format pg_dump archive. Select Custom format and try again.

PG_DUMP_FORMAT_MISMATCH/plain_sql_uploaded_as_custom 400 API response + Async operation after_user_action This file contains plain SQL. Select Plain SQL format and try again.

PG_DUMP_RESTORE_BODY_REQUIRED 400 API response + Async operation after_user_action Pg dump restore body required.

PG_DUMP_RESTORE_FAILED 503 API response + Async operation after_delay The pg_dump restore could not be completed. Review the archive and try again.

PG_DUMP_RESTORE_FAILED/disk_full 409 API response + Async operation after_delay The project does not have enough storage to restore this archive.

PG_DUMP_RESTORE_FAILED/out_of_memory 503 API response + Async operation after_delay The database ran out of memory while restoring this archive. Try a smaller archive or restore it in parts.

PG_DUMP_RESTORE_FAILED/permission_denied 403 API response + Async operation after_delay The database denied an operation in this archive. Remove unsupported operations and try again.

PG_DUMP_RESTORE_FAILED/syntax_error 400 API response + Async operation after_delay The pg_dump restore contains invalid SQL. Create a new dump and try again.

PG_DUMP_RESTORE_FAILED/timeout 408 API response + Async operation after_delay The pg_dump restore exceeded its time limit and was cancelled. Try a smaller archive or restore it in parts.

PG_DUMP_RESTORE_TOOL_FAILED 503 API response + Async operation after_delay psql could not be started for pg_dump restore.

PG_DUMP_RESTORE_TOOL_FAILED/pg_restore_could_not_inspect_custom 503 API response + Async operation after_delay pg_restore could not inspect the custom pg_dump archive.

PG_DUMP_RESTORE_TOOL_FAILED/pg_restore_could_not_be_started 503 API response + Async operation after_delay pg_restore could not be started for pg_dump restore.

PG_DUMP_RESTORE_TOOL_UNAVAILABLE 503 API response + Async operation after_delay psql is not available in this runtime.

PG_DUMP_RESTORE_TOOL_UNAVAILABLE/pg_restore_not_available_runtime 503 API response + Async operation after_delay pg_restore is not available in this runtime.

PG_DUMP_RESTORE_UNAVAILABLE 503 API response + Async operation after_delay Pg dump restore unavailable.

Maintenance

Error identity HTTP Used by Retry Exact message

DATABASE_MAINTENANCE_FENCE_FAILED 503 API response + Async operation after_delay Local database maintenance fence failed.

DATABASE_MAINTENANCE_KUBERNETES_NOT_READY 503 API response + Async operation after_delay Kubernetes is not ready for database maintenance.

DATABASE_MAINTENANCE_LEASE_LOST 409 API response + Async operation after_user_action Database maintenance reconciliation lease was lost.

DATABASE_MAINTENANCE_POOLER_SCALE_FAILED 503 API response + Async operation after_delay The database connection pooler did not reach its maintenance state.

DATABASE_MAINTENANCE_PREFLIGHT_FAILED 503 API response + Async operation after_delay Local database maintenance preflight failed.

DATABASE_MAINTENANCE_PROBE_FAILED 503 API response + Async operation after_delay Database maintenance connectivity probe returned an invalid result.

DATABASE_MAINTENANCE_RECONCILE_FAILED 503 API response + Async operation after_delay Database maintenance reconcile failed.

DATABASE_MAINTENANCE_RESTORE_FAILED 503 API response + Async operation after_delay Local database maintenance restoration failed.

DATABASE_MAINTENANCE_ROUTE_PROBE_FAILED 503 API response + Async operation after_delay A restored database maintenance route failed its connectivity probe.

DATABASE_MAINTENANCE_ROUTE_RESTORE_FAILED 503 API response + Async operation after_delay A database maintenance route was not restored.

DATABASE_MAINTENANCE_ROUTE_STILL_AVAILABLE 503 API response after_delay A database maintenance route is still available.

DATABASE_MAINTENANCE_ROUTE_STILL_AVAILABLE/public_database_route_still_accepts_postgresql 503 API response after_delay A public database route still accepts PostgreSQL connections.

DATABASE_MAINTENANCE_SECRET_INVALID 503 API response + Async operation after_delay A database maintenance secret is invalid.

DATABASE_MAINTENANCE_SECRET_NOT_FOUND 503 API response + Async operation after_delay Database maintenance credentials are unavailable.

DATABASE_MAINTENANCE_SESSIONS_NOT_QUIET 503 API response after_delay Database sessions did not reach a maintenance quiet interval.

DATABASE_MAINTENANCE_SESSION_REAPER_FAILED 503 API response + Async operation after_delay The database maintenance session reaper failed.

DATABASE_MAINTENANCE_SESSION_REAPER_FAILED/database_maintenance_session_reaper_could_not 503 API response + Async operation after_delay The database maintenance session reaper could not connect.

DATABASE_MAINTENANCE_STATE_INVALID 503 API response + Async operation after_delay Database maintenance target state is invalid.

DATABASE_MAINTENANCE_TARGET_FAILED 503 API response + Async operation after_delay Database maintenance target failed.

DATABASE_MAINTENANCE_TARGET_INVALID 503 API response + Async operation after_delay A shared database maintenance pool is unavailable.

DATABASE_MAINTENANCE_TARGET_INVALID/database_maintenance_target_missing_platform_credentials 503 API response + Async operation after_delay A database maintenance target is missing platform credentials.

DATABASE_MAINTENANCE_TARGET_INVALID/shared_database_maintenance_target_missing_its 503 API response + Async operation after_delay A shared database maintenance target is missing its pool.

DATABASE_MAINTENANCE_TARGET_NOT_READY 503 API response + Async operation after_delay A database maintenance target dependency is unavailable.

Metrics

Error identity HTTP Used by Retry Exact message

METRICS_AZURE_AUTH_FAILED 503 API response + Async operation after_delay Project metrics are unavailable because the monitoring service could not authenticate. Contact support.

METRICS_AZURE_QUERY_FAILED 503 API response + Async operation after_delay Project metrics could not be collected for this sampling interval. Newer values may become available after the next sample.

METRICS_AZURE_TIMEOUT 503 API response + Async operation after_delay Metrics source timed out.

METRICS_CPU_UNAVAILABLE 503 API response + Async operation after_delay CPU metrics are not available from the configured metrics source.

METRICS_DISK_IO_UNAVAILABLE 503 API response + Async operation after_delay Disk I/O metrics are not available from the configured metrics source.

METRICS_MEMORY_UNAVAILABLE 503 API response + Async operation after_delay Memory metrics are not available from the configured metrics source.

METRICS_NEGATIVE_VALUE 503 API response + Async operation after_delay Metrics source returned an invalid negative value.

METRICS_PROJECT_NAMESPACE_MISSING 404 API response + Async operation after_user_action Project runtime namespace is unavailable.

METRICS_PROVIDER_DISABLED 400 API response + Async operation after_user_action Metrics collection is disabled.

METRICS_PROVIDER_FAILED 503 API response + Async operation after_delay Runtime metrics could not be collected for this sampling interval. The displayed values may be stale.

METRICS_SAMPLE_NOT_FOUND 404 API response + Async operation after_user_action No metrics sample exists for this project.

METRICS_SHARED_ATTRIBUTION_UNAVAILABLE 503 API response + Async operation after_delay Shared project metrics are unavailable because safe attribution is not available.

METRICS_SHARED_SAMPLE_STALE 409 API response + Async operation after_user_action Shared project metrics are stale.

METRICS_SOURCE_UNAVAILABLE 503 API response + Async operation after_delay Metrics source is unavailable.

METRICS_TIER_LIMIT_INVALID 400 API response + Async operation after_user_action Project tier limits are invalid.

Migrations

Error identity HTTP Used by Retry Exact message

MIGRATION_APPLY_FAILED 500 API response + Async operation after_user_action The migration could not be applied. Review the migration SQL and try again.

MIGRATION_APPLY_FAILED/permission_denied 403 API response + Async operation after_user_action The database denied this migration. Remove actions that are not permitted for this project, then try again.

MIGRATION_APPLY_FAILED/syntax_error 400 API response + Async operation after_user_action The migration contains a SQL syntax error. Correct the SQL and try again.

MIGRATION_APPLY_FAILED/timeout 408 API response + Async operation after_user_action The migration exceeded its time limit and was cancelled. Split it into smaller migrations and try again.

MIGRATION_CUTOVER_BLOCKED 409 API response after_user_action A legacy migration is still marked as applying.

MIGRATION_CUTOVER_CHECKSUM_MISMATCH 409 API response after_user_action Legacy migration history failed checksum verification.

MIGRATION_CUTOVER_CONFLICT 409 API response after_user_action Tenant migration history exists before legacy cutover.

MIGRATION_CUTOVER_PAGINATION_INVALID 503 API response after_delay Legacy migration history pagination did not advance.

MIGRATION_CUTOVER_STATE_INVALID 409 API response after_user_action Legacy failed migration is missing its error state.

MIGRATION_LOCK_BUSY 409 API response + Async operation after_user_action Migration lock is busy.

MIGRATION_NAME_CONFLICT 409 API response + Async operation after_user_action Migration name already exists with different SQL.

MIGRATION_NOT_FOUND 404 API response + Async operation after_user_action Migration not found.

MIGRATION_RUNTIME_NOT_CONFIGURED 503 API response + Async operation after_delay Migration runtime not configured.

MIGRATION_SQL_BLOCKED 400 API response + Async operation after_user_action Migration SQL blocked.

MIGRATION_SQL_CHECKSUM_MISMATCH 409 API response + Async operation after_user_action Migration SQL checksum does not match the stored body.

Organizations

Error identity HTTP Used by Retry Exact message

ADMIN_INVITATION_BILLING_STATUS_INVALID 422 API response + Async operation after_user_action Billing status must be active or beta.

ADMIN_INVITATION_EXISTS 409 API response after_user_action A sent admin invitation already exists for this email.

ADMIN_INVITATION_NOT_CREATED 503 API response + Async operation after_delay Admin invitation was not created.

ADMIN_INVITATION_NOT_FOUND 404 API response + Async operation after_user_action Admin invitation not found.

ADMIN_INVITATION_NOT_RESENDABLE 400 API response after_user_action Only sent admin invitations can be resent.

ADMIN_INVITATION_RESEND_TOO_SOON 429 API response after_delay Admin invitation can only be resent one hour after it was last sent.

ADMIN_INVITATION_SENT_AT_MISSING 409 API response + Async operation after_user_action Admin invitation sent time is missing.

ADMIN_INVITATION_USER_MISMATCH 403 API response + Async operation after_user_action Admin invitation does not match this user.

ADMIN_INVITATION_USER_MISSING 409 API response + Async operation after_user_action Admin invitation is missing its auth user.

INVITATION_DELIVERY_FAILED 503 API response + Async operation dependency_retry The invitation email couldn’t be delivered. Check the recipient address, then resend the invitation or create a new one.

INVITATION_DELIVERY_FAILED/invitation_sent_but_delivery_confirmation_could 503 API response + Async operation dependency_retry The invitation was sent, but delivery confirmation could not be recorded.

INVITATION_DELIVERY_FAILED/invitation_delivery_failed_its_retry_state 503 API response + Async operation dependency_retry Invitation delivery failed and its retry state could not be recorded.

INVITATION_EMAIL_MISMATCH 403 API response user_retry Sign in with the email address that received this invitation.

INVITATION_EXISTS 409 API response user_retry A pending invitation already exists.

INVITATION_EXPIRED 410 API response user_retry This invitation has expired.

INVITATION_LINK_GENERATION_FAILED 503 API response + Async operation after_delay Invitation link generation failed.

INVITATION_LINK_INVALID 503 API response + Async operation after_delay The invitation link could not be generated. Please try again.

INVITATION_NOT_FOUND 404 API response + Async operation never Invitation not found.

INVITATION_NOT_FOUND/organization_invitation_not_found 404 API response + Async operation never Organization invitation not found.

INVITATION_NOT_PENDING 409 API response never This invitation is no longer pending.

INVITATION_NOT_RESENDABLE 409 API response never This invitation cannot be resent.

INVITATION_RESEND_TOO_SOON 429 API response bounded_retry This invitation was sent recently. Try again later.

INVITATION_RESEND_TOO_SOON/invitation_delivery_already_progress_try_again 409 API response bounded_retry Invitation delivery is already in progress. Try again shortly.

ORGANIZATION_NAME_GENERATION_EXHAUSTED 503 API response + Async operation after_delay Could not assign an organization name. Try again.

ORGANIZATION_NAME_REQUIRED 422 API response + Async operation after_user_action Organization name is required.

ORG_INVITATION_ACCEPT_FAILED 503 API response + Async operation after_delay Organization invitation acceptance did not return a result.

ORG_INVITATION_EMAIL_DELIVERY_FAILED 503 API response + Async operation after_delay Org invitation email delivery failed.

ORG_INVITATION_EMAIL_INVALID 422 API response + Async operation after_user_action Invitation email is invalid.

ORG_INVITATION_EMAIL_MISMATCH 403 API response + Async operation after_user_action Organization invitation does not match this user.

ORG_INVITATION_EXISTS 409 API response after_user_action A pending invitation already exists for this email.

ORG_INVITATION_EXPIRED 410 API response + Async operation never Organization invitation has expired.

ORG_INVITATION_NOT_CREATED 503 API response + Async operation after_delay Organization invitation was not created.

ORG_INVITATION_NOT_FOUND 404 API response + Async operation after_user_action Organization invitation not found.

ORG_INVITATION_NOT_PENDING 400 API response after_user_action Only pending invitations can be revoked.

ORG_INVITATION_NOT_UPDATED 503 API response + Async operation after_delay Organization invitation was not updated.

ORG_INVITATION_SELECTION_CANCEL_FAILED 503 API response + Async operation after_delay Organization invitation selection cancellation did not return a result.

ORG_INVITATION_SELECTION_FAILED 503 API response + Async operation after_delay Organization invitation selection did not return a result.

ORG_INVITEE_ALREADY_HAS_MEMBERSHIP 409 API response after_user_action This email already belongs to an active organization member.

ORG_MEMBERSHIP_LIMIT_EXCEEDED 409 API response + Async operation user_retry This account already belongs to an active organization.

ORG_MEMBERSHIP_LIMIT_EXCEEDED/user_can_belong_only_one_active 409 API response + Async operation user_retry A user can belong to only one active organization.

ORG_MEMBER_NOT_CREATED 503 API response + Async operation after_delay Organization member was not created.

ORG_MEMBER_NOT_FOUND 404 API response + Async operation after_user_action Member not found.

ORG_NAME_INVALID 422 API response + Async operation after_user_action Organization name must be between 1 and 120 characters.

ORG_NOT_CREATED 503 API response + Async operation after_delay Organization was not created.

ORG_NOT_CREATED/approval_succeeded_but_organization_could_not 503 API response + Async operation after_delay Approval succeeded but organization could not be created. Ops follow-up required.

ORG_NOT_FOUND 404 API response + Async operation after_user_action Organization not found.

ORG_NOT_UPDATED 503 API response + Async operation after_delay Organization was not updated.

ORG_OWNER_REQUIRED 409 API response + Async operation after_user_action Owner membership cannot be removed.

ORG_PERMISSION_DENIED 403 API response + Async operation after_user_action Permission denied.

ORG_REQUIRED 403 API response + Async operation after_user_action An organization is required.

ORG_ROLE_INVALID 422 API response + Async operation after_user_action Organization role must be one of owner, admin, developer, or viewer.

ORG_ROLE_INVALID/organization_invite_role_must_be_one 422 API response + Async operation after_user_action Organization invite role must be one of admin, developer, or viewer.

ORG_SELF_INVITE_NOT_ALLOWED 400 API response + Async operation after_user_action You cannot invite your own email.

ORG_SELF_REMOVE_NOT_ALLOWED 400 API response + Async operation after_user_action You cannot remove your own account from the organization.

Projects

Error identity HTTP Used by Retry Exact message

CNPG_READY_TIMEOUT 503 API response + Async operation after_delay Database setup is taking longer than expected. Polygres will retry automatically.

DATABASE_IMAGE_PULL_DELAY 503 API response + Async operation after_delay Database setup is waiting for the runtime image. Polygres will retry automatically.

DATABASE_SCHEDULING_DELAY 503 API response + Async operation after_delay Database setup is waiting for runtime capacity. Polygres will retry automatically.

KUBERNETES_DELETE_REISSUED 202 API response + Async operation after_delay Project deletion was reissued because the runtime namespace was still active.

KUBERNETES_NAMESPACE_CONTENT_REMAINING 202 API response + Async operation after_delay Project deletion is waiting for resources in the runtime namespace to be removed.

KUBERNETES_NAMESPACE_DELETION_STALLED 503 API response + Async operation after_delay Project deletion is taking longer than expected. Polygres will continue checking the runtime namespace.

KUBERNETES_NAMESPACE_FINALIZERS_REMAINING 202 API response + Async operation after_delay Project deletion is waiting for Kubernetes finalizers to finish.

KUBERNETES_NAMESPACE_STILL_PRESENT 202 API response + Async operation after_delay Project deletion is still in progress while the runtime namespace is removed.

KUBERNETES_NAMESPACE_TERMINATING 202 API response + Async operation after_delay Project deletion is in progress. The runtime namespace is terminating.

PROJECT_CURSOR_INVALID 422 API response + Async operation after_user_action project_after must include a timezone.

PROJECT_CURSOR_INVALID/project_after_required_when_project_after 422 API response + Async operation after_user_action project_after is required when project_after_id is provided.

PROJECT_CURSOR_INVALID/project_missing_its_creation_timestamp 503 API response + Async operation after_user_action A project is missing its creation timestamp.

PROJECT_DELETE_FAILED 500 API response + Async operation after_delay Local runtime deletion failed.

PROJECT_HEADER_REQUIRED 400 API response + Async operation user_retry X-Polygres-Project is required and must match the route project.

PROJECT_HEADER_REQUIRED/x_project_required 400 API response + Async operation user_retry X-Polygres-Project is required.

PROJECT_ID_INVALID 422 API response + Async operation after_user_action Project ID is invalid.

PROJECT_MEMORY_PRESSURE 409 API response after_user_action Heavy setup work is restricted after repeated memory restarts.

PROJECT_MEMORY_RESTRICTION_NOT_ACTIVE 409 API response after_user_action Project memory restriction is not active.

PROJECT_NOT_FOUND 404 API response + Async operation after_user_action Project not found.

PROJECT_NOT_FOUND/runtime_api_rollout_project_no_longer 404 API response + Async operation after_user_action A Runtime API rollout project no longer exists.

PROJECT_NOT_READY 409 API response + Async operation user_retry The project is not ready for this operation.

PROJECT_NOT_READY/project_not_ready 409 API response + Async operation user_retry Project is not ready.

PROJECT_NOT_READY/project_must_be_ready_read_only 409 API response + Async operation user_retry Project must be ready or read-only to clear memory restrictions.

PROJECT_PROVISIONING_FAILED 503 API response + Async operation after_delay We couldn’t finish setting up your database. Try again. If the problem continues, contact support with the project ID and error code.

PROJECT_RUNTIME_NOT_FOUND 409 API response + Async operation after_user_action Project runtime version not found.

PROJECT_SECRETS_NOT_FOUND 409 API response + Async operation after_user_action Project runtime secrets are not available.

PROJECT_SECRETS_NOT_FOUND/project_owner_credentials_not_available 503 API response + Async operation after_user_action Project owner credentials are not available.

PROJECT_TIER_LIMIT_INVALID 500 API response + Async operation after_delay Project tier storage limit is invalid.

PROJECT_TIER_UNAVAILABLE 409 API response + Async operation after_user_action Project tier is not active.

PROJECT_TIER_UNAVAILABLE/project_tier_not_configured 409 API response + Async operation after_user_action Project tier is not configured.

RUNTIME_DELETION_STILL_IN_PROGRESS 202 API response + Async operation after_delay Project deletion is still in progress. Polygres will continue checking the runtime.

TIER_LIMIT_INVALID 500 API response + Async operation after_delay Tier project_limit must be a non-negative integer.

TIER_NOT_FOUND 404 API response + Async operation after_user_action Tier not found.

TIER_PLACEMENT_CLASS_INVALID 500 API response + Async operation after_delay Tier placement_class must be isolated or shared.

TIER_PROJECT_LIMIT_EXCEEDED 409 API response + Async operation after_user_action Each organization can have one Free Nano project. To continue, create a Basic project, or delete or upgrade the existing Nano project.

TIER_REQUIRED 403 API response + Async operation after_user_action A tier is required.

TIER_REQUIRED/tier_required_synchronize_runtime_limits 409 API response + Async operation after_user_action A tier is required to synchronize Runtime limits.

TIER_STORAGE_LIMIT_INVALID 500 API response + Async operation after_delay The project tier storage limit is invalid.

TIER_TENANT_MEMORY_WEIGHT_INVALID 400 API response + Async operation after_user_action Tier tenant memory weight invalid.

Rate limits

Error identity HTTP Used by Retry Exact message

RATE_LIMITED 429 API response bounded_retry Too many requests. Try again later.

RATE_LIMITED/rate_limit_exceeded 429 API response bounded_retry Rate limit exceeded.

RATE_LIMIT_STORAGE_NOT_CONFIGURED 503 API response + Async operation after_delay RATE_LIMIT_BACKEND must be either memory or redis.

RATE_LIMIT_STORAGE_NOT_CONFIGURED/production_rate_limiting_requires_rate_limit 503 API response + Async operation after_delay Production rate limiting requires RATE_LIMIT_BACKEND=redis.

RATE_LIMIT_STORAGE_NOT_CONFIGURED/rate_limit_redis_url_required_when 503 API response + Async operation after_delay RATE_LIMIT_REDIS_URL is required when RATE_LIMIT_BACKEND=redis.

RATE_LIMIT_UNAVAILABLE 503 API response + Async operation dependency_retry Request-rate protection is temporarily unavailable.

RATE_LIMIT_UNAVAILABLE/rate_limit_storage_unavailable_retry_later 503 API response + Async operation dependency_retry Rate limit storage is unavailable. Retry the request later; if the problem persists, contact support with the request ID.

Rows

Error identity HTTP Used by Retry Exact message

ROW_COLUMN_NOT_WRITABLE 400 API response after_user_action The requested row column is not writable.

ROW_COLUMN_UNKNOWN 400 API response after_user_action The requested row column does not exist.

ROW_CONFLICT_CONSTRAINT_INVALID 400 API response after_user_action Conflict columns must match one non-deferrable primary or unique constraint.

ROW_CONSTRAINT_VIOLATION 400 API response after_user_action The row violates a table constraint.

ROW_CONSTRAINT_VIOLATION/check 400 API response after_user_action The row violates a check constraint.

ROW_CONSTRAINT_VIOLATION/exclusion 409 API response after_user_action The row violates an exclusion constraint.

ROW_CONSTRAINT_VIOLATION/foreign_key 400 API response after_user_action The row violates a foreign-key constraint.

ROW_CONSTRAINT_VIOLATION/not_null 400 API response after_user_action The row omits a required value.

ROW_CONSTRAINT_VIOLATION/trigger 400 API response after_user_action A table trigger rejected the row.

ROW_CONSTRAINT_VIOLATION/unique 409 API response after_user_action The row conflicts with an existing unique value.

ROW_CONTEXT_IDEMPOTENCY_CONFLICT 409 API response after_user_action The row idempotency key was already used for a different request.

ROW_CONTEXT_IDEMPOTENCY_EXPIRED 409 API response never The row idempotency record has expired.

ROW_CONTEXT_IDEMPOTENCY_REQUIRED 400 API response after_user_action Context-backed row writes require an Idempotency-Key.

ROW_CONTEXT_RECONCILIATION_FAILED 503 API response bounded_retry The row committed, but Context point reconciliation failed.

ROW_LOCK_TIMEOUT 503 API response after_delay The row write could not acquire a database lock in time.

ROW_OPTION_INVALID 400 API response after_user_action The row write options are incompatible.

ROW_REQUEST_INVALID 400 API response after_user_action The row write request is invalid.

ROW_STATEMENT_TIMEOUT 503 API response after_delay The row write exceeded its statement timeout.

ROW_TARGET_NOT_FOUND 404 API response after_user_action The row target table was not found.

ROW_TARGET_NOT_OWNED 403 API response after_user_action The row target is not owned by the project-owner role.

ROW_TARGET_RLS_UNSUPPORTED 400 API response after_user_action Forced row-level security is not supported for Runtime row writes.

ROW_TARGET_UNSUPPORTED 400 API response after_user_action The requested relation is not an eligible row-write target.

ROW_VALUE_TYPE_INVALID 400 API response after_user_action A row value is invalid for its target PostgreSQL type.

ROW_WRITE_FAILED 500 API response never The row write failed.

ROW_WRITE_OUTCOME_AMBIGUOUS 503 API response never The row write outcome is unknown because commit acknowledgement was lost.

ROW_WRITE_PERMISSION_DENIED 403 API response after_user_action The project-owner role cannot write the target table.

ROW_WRITE_REQUEST_TOO_LARGE 413 API response after_user_action The row write request exceeds the size limit.

ROW_WRITE_RESPONSE_TOO_LARGE 422 API response after_user_action The requested returning values exceed the response size limit.

STORAGE_READ_ONLY 503 API response after_delay Project storage is read-only and cannot accept row writes.

Runtime

Error identity HTTP Used by Retry Exact message

GATEWAY_RUNTIME_JWKS_UNAVAILABLE 503 API response dependency_retry Gateway Runtime signing keys are unavailable.

GATEWAY_RUNTIME_JWT_INVALID 401 API response + Async operation never The Gateway Runtime token is invalid.

GATEWAY_RUNTIME_JWT_INVALID/gateway_runtime_jwt_invalid 401 API response + Async operation never Gateway Runtime JWT is invalid.

GATEWAY_RUNTIME_JWT_KEY_INVALID 500 API response + Async operation after_delay Gateway Runtime JWT private key is invalid.

GATEWAY_RUNTIME_JWT_REQUIRED 401 API response + Async operation never A Gateway Runtime token is required.

GATEWAY_RUNTIME_PROJECT_MISMATCH 403 API response never The Gateway Runtime token is for a different project.

GATEWAY_RUNTIME_SCOPE_DENIED 403 API response never The Gateway Runtime token does not allow this operation.

GATEWAY_RUNTIME_SCOPE_INVALID 403 API response + Async operation never The Gateway Runtime token scope is invalid.

GATEWAY_RUNTIME_SCOPE_INVALID/gateway_runtime_jwt_scope_invalid 403 API response + Async operation never Gateway Runtime JWT scope is invalid.

RUNTIME_ACCESS_NOT_CONFIGURED 503 API response + Async operation after_delay Direct Runtime access is not configured.

RUNTIME_ACCESS_SCOPE_INVALID 422 API response + Async operation after_user_action Runtime access scope is invalid.

RUNTIME_ACCESS_SCOPE_INVALID/runtime_access_scope_invalid 403 API response + Async operation after_user_action Runtime access scope is invalid.

RUNTIME_API_CONFIG_MISSING 409 API response + Async operation after_user_action Runtime API ConfigMap is missing.

RUNTIME_API_CONTAINER_MISSING 409 API response + Async operation after_user_action Runtime API container is missing from the Deployment.

RUNTIME_API_DEPLOYMENT_MISSING 409 API response + Async operation after_user_action Runtime API Deployment is missing.

RUNTIME_API_IMAGE_NOT_APPLIED 503 API response after_delay Runtime API Deployment does not reference the target image.

RUNTIME_API_KEY_SNAPSHOT_UNAVAILABLE 503 API response + Async operation dependency_retry Runtime API-key state is temporarily unavailable.

RUNTIME_API_KEY_SNAPSHOT_UNAVAILABLE/runtime_api_key_snapshot_unavailable 503 API response + Async operation dependency_retry Runtime API key snapshot is unavailable.

RUNTIME_API_READINESS_FAILED 503 API response + Async operation after_delay Runtime API /v1/readyz verification failed.

RUNTIME_API_ROLLOUT_ALREADY_ACTIVE 409 API response after_user_action A Runtime API rollout is already active.

RUNTIME_API_ROLLOUT_JOB_EXISTS 409 API response after_user_action Runtime API rollout job already exists.

RUNTIME_API_ROLLOUT_NOT_CREATED 503 API response + Async operation after_delay Runtime API rollout job was not created.

RUNTIME_API_ROLLOUT_NOT_FOUND 404 API response + Async operation after_user_action Runtime API rollout job not found.

RUNTIME_API_ROLLOUT_TARGET_NOT_CONFIGURED 409 API response + Async operation after_user_action Runtime API rollout target must match the configured production image.

RUNTIME_API_ROLLOUT_VERIFICATION_FAILED 503 API response + Async operation after_delay Runtime API rollout verification did not pass.

RUNTIME_API_TARGET_POD_NOT_READY 503 API response + Async operation after_delay No restarted Runtime API pod became Ready.

RUNTIME_API_TARGET_POD_NOT_READY/no_target_image_runtime_api_pod 503 API response + Async operation after_delay No target-image Runtime API pod became Ready.

RUNTIME_AUTH_INVALID 400 API response + Async operation after_user_action Runtime auth invalid.

RUNTIME_AUTH_REQUIRED 401 API response + Async operation after_user_action Runtime authorization is required.

RUNTIME_CONTEXT_PROXY_FAILED 502 API response + Async operation after_delay Runtime Context proxy request failed.

RUNTIME_DATABASE_HOST_DOMAIN_MISMATCH 409 API response + Async operation after_user_action Runtime database hosts do not match the configured database domain.

RUNTIME_DEFAULT_NOT_FOUND 503 API response + Async operation after_delay Default runtime version is not configured.

RUNTIME_DELETE_REQUEST_FAILED 503 API response + Async operation after_delay Runtime delete request failed.

RUNTIME_GRAPH_CONFIGURATION_SYNC_FAILED 503 API response + Async operation after_delay Runtime graph configuration synchronization failed.

RUNTIME_GRAPH_CONFIGURATION_SYNC_STALE 409 API response + Async operation after_user_action A newer Runtime graph configuration has already been synchronized.

RUNTIME_GRAPH_CONFIGURATION_SYNC_UNAVAILABLE 503 API response + Async operation after_delay Runtime graph configuration synchronization is unavailable.

RUNTIME_HOST_INVALID 400 API response + Async operation user_retry The runtime host is invalid.

RUNTIME_HOST_INVALID/runtime_host_invalid 400 API response + Async operation user_retry Runtime host is invalid.

RUNTIME_INSPECTION_UNAVAILABLE 503 API response + Async operation after_delay Runtime inspection unavailable.

RUNTIME_JOINT_QUERY_BUSY 503 API response after_delay Hybrid retrieval is busy. Try again shortly.

RUNTIME_KEY_SYNC_FAILED 503 API response + Async operation after_delay Runtime key sync failed.

RUNTIME_LIMITS_SYNC_FAILED 503 API response + Async operation after_delay Runtime limits sync failed.

RUNTIME_LIMITS_UNAVAILABLE 503 API response + Async operation after_delay Runtime limits snapshot is unavailable.

RUNTIME_NOT_READY 409 API response + Async operation after_user_action Project Runtime API is not ready.

RUNTIME_PROJECT_NOT_FOUND 404 API response + Async operation never Runtime project not found.

RUNTIME_PROJECT_NOT_FOUND/runtime_project_not_found 404 API response + Async operation never Runtime project was not found.

RUNTIME_PROJECT_NOT_READY 409 API response + Async operation user_retry The runtime project is not ready.

RUNTIME_PROJECT_NOT_READY/runtime_project_not_ready 503 API response + Async operation user_retry Runtime project is not ready.

RUNTIME_PROXY_NOT_CONFIGURED 503 API response + Async operation after_delay Gateway Runtime JWT signing key is not configured.

RUNTIME_RECONCILE_UNAVAILABLE 409 API response + Async operation after_user_action Runtime reconciliation is available only for ready projects.

RUNTIME_ROUTING_HEADER_REJECTED 400 API response never A client-supplied runtime routing header is not allowed.

RUNTIME_ROUTING_HEADER_REJECTED/caller_controlled_project_routing_headers_not 400 API response never Caller-controlled project routing headers are not accepted.

RUNTIME_SETUP_PROXY_FAILED 502 API response + Async operation after_delay The project Runtime API is not responding. Check the project Runtime status and retry after it is ready; contact support with the request ID if it remains unavailable.

RUNTIME_SYNC_STATE_NOT_FOUND 503 API response + Async operation after_delay Runtime sync state was not persisted.

RUNTIME_TENANT_CAPACITY_EXCEEDED 503 API response + Async operation after_delay Shared Runtime tenant connection capacity is temporarily exhausted.

RUNTIME_UPGRADE_ALREADY_ACTIVE 409 API response after_user_action A runtime upgrade is already active for this project.

RUNTIME_UPGRADE_JOB_EXISTS 409 API response after_user_action Runtime upgrade job already exists.

RUNTIME_UPGRADE_JOB_NOT_CREATED 503 API response + Async operation after_delay Runtime upgrade job was not created.

RUNTIME_UPGRADE_JOB_NOT_FOUND 404 API response + Async operation after_user_action Runtime upgrade job not found.

RUNTIME_UPGRADE_PATH_EXISTS 409 API response after_user_action Runtime upgrade path already exists.

RUNTIME_UPGRADE_PATH_INVALID 400 API response + Async operation after_user_action Runtime upgrade path source and target must differ.

RUNTIME_UPGRADE_PATH_NOT_CREATED 503 API response + Async operation after_delay Runtime upgrade path was not created.

RUNTIME_UPGRADE_PATH_NOT_FOUND 404 API response + Async operation after_user_action Runtime upgrade path not found.

RUNTIME_UPGRADE_PATH_NOT_LATEST 409 API response after_user_action Runtime upgrade path is not the latest runtime bundle path.

RUNTIME_UPGRADE_PATH_NOT_LATEST/runtime_upgrade_path_does_not_target 409 API response after_user_action Runtime upgrade path does not target the latest runtime bundle.

RUNTIME_UPGRADE_PATH_NOT_STABLE 409 API response after_user_action Runtime upgrade path is not stable.

RUNTIME_UPGRADE_PATH_UPDATE_EMPTY 400 API response after_user_action Runtime upgrade path update is empty.

RUNTIME_UPGRADE_PROJECT_NOT_READY 409 API response + Async operation after_user_action Runtime upgrade is available only for ready projects.

RUNTIME_UPGRADE_SOURCE_MISMATCH 409 API response + Async operation after_user_action Runtime upgrade path does not match the current project runtime.

RUNTIME_UPGRADE_TARGET_NOT_FOUND 409 API response + Async operation after_user_action Runtime upgrade target version not found.

RUNTIME_VERSION_EXISTS 409 API response after_user_action Runtime version already exists.

RUNTIME_VERSION_IN_USE 409 API response after_user_action Runtime version is used by existing projects.

RUNTIME_VERSION_NOT_CREATED 503 API response + Async operation after_delay Runtime version was not created.

RUNTIME_VERSION_NOT_FOUND 404 API response + Async operation after_user_action Runtime version not found.

RUNTIME_VERSION_UPDATE_EMPTY 400 API response after_user_action Runtime version update is empty.

Shared runtime

Error identity HTTP Used by Retry Exact message

SHARED_DATABASE_BOOTSTRAP_CLEANUP_FAILED 500 API response + Async operation after_delay Shared database bootstrap failed and its partial resources could not be cleaned up.

SHARED_DATABASE_BOOTSTRAP_INVALID 500 API response + Async operation after_delay Shared database bootstrap passwords are required.

SHARED_DATABASE_BOOTSTRAP_INVALID/existing_database_owner_mismatch 500 API response + Async operation after_delay An existing shared database has an unexpected owner.

SHARED_DATABASE_BOOTSTRAP_INVALID/postgres_did_not_return_valid_quoted 500 API response + Async operation after_delay Postgres did not return a valid quoted password literal.

SHARED_DATABASE_BOOTSTRAP_INVALID/shared_database_bootstrap_passwords_must_be 500 API response + Async operation after_delay Shared database bootstrap passwords must be distinct.

SHARED_DATABASE_BOOTSTRAP_NOT_CONFIGURED 503 API response + Async operation after_delay Shared database schema reconciliation is not configured.

SHARED_DATABASE_PROVISIONING_NOT_CONFIGURED 503 API response + Async operation after_delay Shared database provisioning is not configured.

SHARED_DATABASE_PROVISIONING_NOT_CONFIGURED/shared_database_admin_credentials_required_provision 503 API response + Async operation after_delay Shared database admin credentials are required to provision a pool.

SHARED_GRAPH_STORAGE_CLEANUP_FAILED 500 API response + Async operation after_delay Shared graph artifacts remain after tenant cleanup.

SHARED_GRAPH_STORAGE_CONFLICT 500 API response + Async operation after_delay Another database already uses the shared tenant graph storage directory.

SHARED_GRAPH_STORAGE_DIRECTORY_EXISTS 500 API response after_delay The shared tenant graph storage directory already exists and requires operator reconciliation.

SHARED_GRAPH_STORAGE_EFFECTIVE_MISMATCH 500 API response + Async operation after_delay A fresh tenant connection did not inherit its isolated graph storage setting.

SHARED_GRAPH_STORAGE_OID_INVALID 500 API response + Async operation after_delay Shared tenant database OID must be a positive integer.

SHARED_GRAPH_STORAGE_OID_INVALID/postgres_did_not_return_one_positive 500 API response + Async operation after_delay Postgres did not return one positive OID for the shared tenant database.

SHARED_GRAPH_STORAGE_PERSISTENCE_MISMATCH 500 API response + Async operation after_delay Postgres did not persist the expected shared tenant graph storage setting.

SHARED_POOL_AUTOSCALING_DISABLED 400 API response + Async operation after_user_action Shared runtime pool autoscaling is disabled, so this operation will not continue.

SHARED_POOL_CAPACITY_PENDING 503 API response + Async operation after_delay Your project is waiting for shared runtime capacity.

SHARED_POOL_CONTROL_MIGRATION_CONFLICT 500 API response + Async operation after_delay The shared Context dispatch schema checksum does not match.

SHARED_POOL_CONTROL_MIGRATION_CONFLICT/shared_context_dispatch_v2_schema_checksum 500 API response + Async operation after_delay The shared Context dispatch V2 schema checksum does not match.

SHARED_POOL_CONTROL_MIGRATION_CONFLICT/shared_context_dispatch_v3_schema_checksum 500 API response + Async operation after_delay The shared Context dispatch V3 schema checksum does not match.

SHARED_POOL_CONTROL_MIGRATOR_NOT_CONFIGURED 503 API response + Async operation after_delay Shared pool-control schema migration is not configured.

SHARED_POOL_CONTROL_ROLE_NOT_READY 503 API response + Async operation after_delay The shared Context dispatch role has not been reconciled.

SHARED_POOL_GENERATION_LIMIT_REACHED 503 API response + Async operation after_delay The shared runtime pool generation limit has been reached.

SHARED_POOL_JOB_NOT_FOUND 404 API response + Async operation after_user_action Shared runtime pool provisioning job not found.

SHARED_POOL_JOB_NOT_FOUND/shared_runtime_pool_provisioning_job_not 500 API response + Async operation after_user_action Shared runtime pool provisioning job was not completed.

SHARED_POOL_JOB_NOT_FOUND/shared_runtime_pool_provisioning_job_failure 500 API response + Async operation after_user_action Shared runtime pool provisioning job failure was not recorded.

SHARED_POOL_LEASE_LOST 409 API response + Async operation after_user_action Shared runtime pool provisioning lease was lost.

SHARED_POOL_MAX_ATTEMPTS_EXHAUSTED 400 API response + Async operation after_user_action Shared runtime pool provisioning could not be completed after several attempts.

SHARED_POOL_NOT_ASSIGNED 500 API response after_delay Shared project is missing a pool assignment.

SHARED_POOL_NOT_ASSIGNED/shared_project_missing_pool_assignment 409 API response after_delay Shared project is missing a pool assignment.

SHARED_POOL_NOT_FOUND 404 API response + Async operation after_user_action Shared runtime pool not found.

SHARED_POOL_NOT_FOUND/shared_runtime_pool_not_found 500 API response + Async operation after_user_action Shared runtime pool was not found.

SHARED_POOL_NOT_FOUND/shared_runtime_pool_not_created 500 API response + Async operation after_user_action Shared runtime pool was not created.

SHARED_POOL_SELECTOR_INVALID 500 API response + Async operation after_delay Shared pool selector is invalid.

SHARED_POOL_TEMPLATE_NOT_FOUND 409 API response + Async operation after_user_action No shared runtime pool template exists for this pool family.

SHARED_RUNTIME_CONTROL_PLANE_NOT_CONFIGURED 503 API response + Async operation after_delay Supabase control-plane credentials are required to provision a pool.

SHARED_RUNTIME_DELETE_NOT_STARTED 202 API response + Async operation after_delay Project deletion is queued and has not started in the shared runtime yet.

SHARED_RUNTIME_DELETE_REISSUED 202 API response + Async operation after_delay Project deletion was reissued because shared-runtime cleanup had not started.

SHARED_RUNTIME_IDENTITY_NOT_CONFIGURED 503 API response + Async operation after_delay The shared runtime Azure tenant ID is required.

SHARED_RUNTIME_IDENTITY_NOT_CONFIGURED/shared_runtime_azure_managed_identity_client 503 API response + Async operation after_delay The shared runtime Azure managed identity client ID is required.

SHARED_RUNTIME_POOL_PROVISIONING_FAILED 503 API response + Async operation after_delay Shared runtime pool provisioning failed.

SHARED_TENANT_LIMIT_RECONCILIATION_FAILED 500 API response + Async operation after_delay Shared tenant database limits were not reconciled.

SQL

Error identity HTTP Used by Retry Exact message

SQL_IMPORT_BINARY_DUMP_UNSUPPORTED 400 API response + Async operation after_user_action This file is a custom-format pg_dump archive. Use pg_dump restore with Custom format (-Fc).

SQL_IMPORT_BLOCKED 400 API response + Async operation after_user_action SQL import blocked.

SQL_IMPORT_EMPTY 400 API response + Async operation after_user_action SQL import body is required.

SQL_PARSE_FAILED 503 API response + Async operation after_delay SQL parse failed.

SQL_QUERY_BLOCKED 400 API response + Async operation after_user_action SQL query blocked.

SQL_QUERY_FAILED 503 API response + Async operation after_delay SQL query failed.

SQL_QUERY_FAILED/column_not_found 400 API response + Async operation after_delay A referenced column does not exist. Check the query and try again.

SQL_QUERY_FAILED/permission_denied 403 API response + Async operation after_delay The database denied this query. Remove actions that are not permitted for this project.

SQL_QUERY_FAILED/relation_not_found 400 API response + Async operation after_delay A referenced table or view does not exist. Check the query and try again.

SQL_QUERY_FAILED/syntax_error 400 API response + Async operation after_delay The query contains a SQL syntax error. Correct the SQL and try again.

SQL_QUERY_FAILED/timeout 408 API response + Async operation after_delay The query exceeded its time limit and was cancelled. Simplify it and try again.

Sync

Error identity HTTP Used by Retry Exact message

SYNCED_PROJECT_SURFACE_UNAVAILABLE 403 API response never This operation is unavailable for a synchronized project.

SYNC_ACTION_INVALID_FOR_STAGE 409 API response + Async operation after_user_action This synchronization action is not available in the current lifecycle stage.

SYNC_ATTEMPT_EXPIRED 409 API response + Async operation after_user_action The synchronization preflight attempt has expired.

SYNC_ATTEMPT_GENERATION_CONFLICT 409 API response + Async operation after_user_action The synchronization preflight attempt changed before this request completed.

SYNC_ATTEMPT_NOT_FOUND 404 API response + Async operation after_user_action Synchronization preflight attempt not found.

SYNC_ATTEMPT_NOT_READY 409 API response + Async operation user_retry Synchronization preflight is not ready for this operation.

SYNC_CAPACITY_BLOCKED 409 API response + Async operation after_user_action Synchronization work is blocked until target storage capacity is available.

SYNC_CONFIGURATION_GENERATION_CONFLICT 409 API response + Async operation after_user_action The synchronization configuration changed before this request completed.

SYNC_CONFIRMATIONS_INCOMPLETE 422 API response + Async operation after_user_action All required synchronization confirmations must be accepted.

SYNC_IDEMPOTENCY_CONFLICT 409 API response + Async operation never This idempotency key was already used for a different synchronization request.

SYNC_IDEMPOTENCY_EXPIRED 409 API response + Async operation never This synchronization idempotency record has expired.

SYNC_PREFLIGHT_BACKEND_UNAVAILABLE 503 API response + Async operation after_delay Synchronization preflight is temporarily unavailable.

SYNC_PREFLIGHT_NOT_ADMITTED 409 API response + Async operation after_user_action Synchronization preflight has not been admitted for project creation.

SYNC_SELECTION_GENERATION_CONFLICT 409 API response + Async operation after_user_action The selected synchronization tables changed before this request completed.

SYNC_SELECTION_INVALID 422 API response + Async operation after_user_action The selected table is not eligible for synchronization.

SYNC_SELECTION_OVER_TIER_LIMIT 409 API response + Async operation after_user_action The selected tables exceed the organization’s storage limit.

SYNC_SOURCE_IDENTITY_IMMUTABLE 422 API response + Async operation never Source host, port, and database cannot be changed during credential rotation.

SYNC_SOURCE_URL_INVALID 422 API response + Async operation after_user_action The PostgreSQL source connection is invalid or unsupported.

Text retrieval

Error identity HTTP Used by Retry Exact message

TEXT_COLUMN_NOT_FOUND 400 API response + Async operation after_user_action Text row ID column not found.

TEXT_COLUMN_NOT_FOUND/text_search_column_not_found 400 API response + Async operation after_user_action Text search column was not found.

TEXT_COLUMN_NOT_FOUND/tsvector_source_column_not_found 400 API response + Async operation after_user_action A TSVector source column was not found.

TEXT_COLUMN_TYPE_UNSUPPORTED 400 API response + Async operation after_user_action Fuzzy search requires a text-like column.

TEXT_COLUMN_TYPE_UNSUPPORTED/tsvector_search_requires_tsvector_column 400 API response + Async operation after_user_action tsvector search requires a tsvector column.

TEXT_COLUMN_TYPE_UNSUPPORTED/generated_tsvector_source_must_be_text_like 400 API response + Async operation after_user_action Generated TSVector source columns must be text-like.

TEXT_CONFIGURATION_EXISTS 409 API response after_user_action Text configuration already exists.

TEXT_CONFIGURATION_INVALID 400 API response + Async operation after_user_action Default limit cannot exceed max limit.

TEXT_CONFIGURATION_INVALID/text_search_requires_at_least_one 400 API response + Async operation after_user_action Text search requires at least one row ID column.

TEXT_CONFIGURATION_INVALID/tsvector_configuration_missing_tsvector_column 400 API response + Async operation after_user_action tsvector configuration is missing tsvector_column.

TEXT_CONFIGURATION_INVALID/fuzzy_configuration_missing_text_column 400 API response + Async operation after_user_action Fuzzy configuration is missing text_column.

TEXT_CONFIGURATION_INVALID/tsvector_search_requires_tsvector_column_no 400 API response + Async operation after_user_action tsvector search requires tsvector_column and no text_column.

TEXT_CONFIGURATION_INVALID/fuzzy_search_requires_text_column_no 400 API response + Async operation after_user_action Fuzzy search requires text_column and no tsvector_column.

TEXT_CONFIGURATION_INVALID/text_search_kind_unsupported 400 API response + Async operation after_user_action Text search kind is unsupported.

TEXT_CONFIGURATION_INVALID/generated_tsvector_column_must_differ_from_sources 400 API response + Async operation after_user_action Generated TSVector column must differ from its source columns.

TEXT_CONFIGURATION_INVALID/language_conflicts_with_tsvector_setup 400 API response + Async operation after_user_action language conflicts with the TSVector setup.

TEXT_CONFIGURATION_INVALID/tsvector_column_conflicts_with_setup 400 API response + Async operation after_user_action tsvector_column conflicts with the TSVector setup.

TEXT_CONFIGURATION_INVALID/tsvector_setup_only_valid_for_tsvector_search 400 API response + Async operation after_user_action TSVector setup is only valid for tsvector search.

TEXT_CONFIGURATION_KIND_MISMATCH 400 API response + Async operation after_user_action Text configuration kind does not match endpoint.

TEXT_CONFIGURATION_NOT_FOUND 404 API response + Async operation after_user_action Text configuration not found.

TEXT_CONFIGURATION_NOT_READY 409 API response + Async operation after_user_action Text configuration is not ready.

TEXT_FILTER_INVALID 400 API response + Async operation after_user_action Text filter is invalid.

TEXT_FILTER_NOT_REGISTERED 400 API response after_user_action Text filter is not registered.

TEXT_FILTER_TYPE_UNSUPPORTED 400 API response + Async operation after_user_action Text filter column type is unsupported.

TEXT_GENERATED_COLUMN_EXISTS 409 API response after_user_action The requested generated TSVector column already exists. Use existing mode or choose another name.

TEXT_INDEX_DELETE_FAILED 409 API response after_user_action Text index deletion failed; the configuration was retained so deletion can retry.

TEXT_INDEX_FAILED 400 API response + Async operation after_user_action Text index creation failed. Review the failure recorded in text-index status, correct it if possible, then retry.

TEXT_INDEX_FAILED/tsvector_setup_cleanup_incomplete 500 API response + Async operation after_user_action TSVector setup failed and automatic cleanup was incomplete. Inspect the table and text configurations before retrying.

TEXT_INDEX_FAILED/text_index_rebuild_failed_review_failure 400 API response + Async operation after_user_action Text index rebuild failed. Review the failure recorded in text-index status, correct it if possible, then retry the rebuild.

TEXT_INDEX_VERIFICATION_FAILED 409 API response after_user_action The physical text index is missing or invalid.

TEXT_LANGUAGE_NOT_FOUND 400 API response after_user_action Text search language was not found.

TEXT_QUERY_EMPTY 400 API response after_user_action Text query is required.

TEXT_ROW_ID_NOT_STABLE 400 API response after_user_action Text row ID columns are not a primary or unique NOT NULL key.

Vector retrieval

Error identity HTTP Used by Retry Exact message

VECTOR_COLUMN_NOT_FOUND 400 API response + Async operation after_user_action Vector row ID column not found.

VECTOR_COLUMN_NOT_FOUND/vector_embedding_column_not_found_requested 400 API response + Async operation after_user_action Vector embedding column was not found with the requested dimensions.

VECTOR_COMPATIBILITY_ENGINE_INVALID 400 API response + Async operation after_user_action Vector compatibility engine must be pgvector or pgcontext.

VECTOR_COMPATIBILITY_OPERATION_ACTIVE 409 API response after_user_action The compatibility operation is still stopping; retry deletion.

VECTOR_COMPATIBILITY_REINDEX_ACTIVE 409 API response after_user_action The compatibility index is already being rebuilt.

VECTOR_COMPATIBILITY_RETRY_UNAVAILABLE 409 API response + Async operation after_user_action The vector compatibility binding is not eligible for a provisioning retry.

VECTOR_CONFIGURATION_AMBIGUOUS 409 API response after_user_action Multiple vector configurations match that name. Select one by ID.

VECTOR_CONFIGURATION_EXISTS 409 API response after_user_action Vector configuration already exists.

VECTOR_CONFIGURATION_INVALID 400 API response + Async operation after_user_action Default limit cannot exceed max limit.

VECTOR_CONFIGURATION_NOT_FOUND 404 API response + Async operation after_user_action Vector configuration not found.

VECTOR_CONFIGURATION_NOT_FOUND/vector_compatibility_binding_not_found 404 API response + Async operation after_user_action Vector compatibility binding was not found.

VECTOR_CONFIGURATION_REQUIRED 409 API response + Async operation after_user_action Multiple ready vector configurations are available. Select one by exact name or ID.

VECTOR_CREATION_RETIRED 410 API response + Async operation never New pgvector column registrations are no longer supported.

Update your CLI version with pipx upgrade polygres-cli , and create a collection using polygres context collections create .

Refer to the documentation for more information: https://docs.polygres.com/cli/context#collection-lifecycle

VECTOR_DIMENSION_MISMATCH 400 API response + Async operation after_user_action Embedding dimensions do not match configuration.

VECTOR_FILTER_INVALID 400 API response + Async operation after_user_action Vector filter is invalid.

VECTOR_FILTER_NOT_REGISTERED 400 API response after_user_action Vector filter is not registered.

VECTOR_FILTER_TYPE_UNSUPPORTED 400 API response + Async operation after_user_action Vector filter column type is unsupported.

VECTOR_INDEX_DELETE_FAILED 503 API response + Async operation after_delay Vector index deletion failed. The configuration was not deleted; retry after the database is available.

VECTOR_INDEX_FAILED 400 API response + Async operation after_user_action Vector index update failed. Review the failure recorded in vector status, correct it if possible, then save again.

VECTOR_INDEX_FAILED/vector_reindexing_failed_review_failure_recorded 400 API response + Async operation after_user_action Vector reindexing failed. Review the failure recorded in vector status, then retry. If no failure details are available, contact support.

VECTOR_INDEX_VERIFICATION_FAILED 409 API response + Async operation after_user_action The physical vector index does not match its configuration.

VECTOR_INDEX_VERIFICATION_UNAVAILABLE 503 API response + Async operation after_delay Vector index verification is unavailable.

VECTOR_INVALID 400 API response + Async operation after_user_action Embedding contains invalid values.

VECTOR_NOT_READY 409 API response + Async operation after_user_action Vector not ready.

VECTOR_REINDEX_FAILED 400 API response + Async operation after_user_action Vector reindexing failed. The legacy pgvector index remains available; retry to rebuild the compatibility index.

VECTOR_REINDEX_FAILED/vector_reindexing_failed_review_failure_recorded 400 API response + Async operation after_user_action Vector reindexing failed. Review the failure recorded in vector status, then retry. If no failure details are available, contact support.

VECTOR_ROW_ID_INVALID 400 API response + Async operation after_user_action row_id is invalid for the configured row ID column.

VECTOR_ROW_ID_NOT_STABLE 400 API response after_user_action Vector row ID column is not a primary or unique NOT NULL key.

VECTOR_ROW_ID_TYPE_UNAVAILABLE 409 API response + Async operation after_user_action The configured row ID column type is unavailable.

VECTOR_ROW_ID_TYPE_UNSUPPORTED 400 API response + Async operation after_user_action The configured row ID column type is not supported.

VECTOR_SEARCH_INVALID 400 API response + Async operation after_user_action Distance and similarity conflict.
