source: https://docs.evokoa.com/polygres/mcp/capabilities
title: MCP tools and capabilities | Polygres
source_hash: 2737d7d094cd824f7d4a4afd320529ff00a9506b2bbac48cac8434fa77b8a97e
discovered_from: https://docs.evokoa.com/polygres

# MCP tools and capabilities | Polygres

MCP tools and capabilities

Polygres MCP catalog 1.0 contains 91 tools. Your client shows the tools that

match the connection settings, your current Polygres role, the project type,

and the project state.

How the catalog adapts

Each connection combines these choices:

the selected feature groups

View only or View and make changes

one fixed project or all accessible projects

the installation scopes approved in the browser

your current organization and project permissions

the project type and current state

This gives each client a focused catalog for the work it can perform. A

fixed-project connection also fills in the project automatically.

Find the tools for your workflow

Connection choice Tools you receive How to expand the catalog

Fixed project Tools that work with the selected project Create an All accessible projects connection for organization-wide setup and project selection.

All accessible projects Organization and project tools, with project_id shown on project-scoped calls Pass the exact project ID requested by each tool.

View only Inspection, retrieval, status, and documentation tools Create a View and make changes connection when you want the client to prepare changes.

Selected feature groups Tools from those features Add another feature through a new connection.

Current Polygres role Tools allowed by your organization and project permissions Ask an organization owner or administrator for the role needed by the workflow.

Standard project Database rows, imports, and supported retrieval tools Use the project tools that match a standard project.

Synchronized project Synchronization and supported retrieval tools Make application data changes in the source PostgreSQL database.

Current project state Actions available for the project now Read project or operation status and continue with the lifecycle action offered for that state.

Organization-wide setup tools include list_projects , project creation,

synchronized-project preflight, source-table discovery, table selection, and

synchronized-project creation. A fixed-project connection keeps its catalog

focused on the project chosen during connection setup.

Projects

Project tools cover identity, project status, creation, capacity, and durable

operations.

View tools: whoami , list_projects , get_project ,

get_project_status , get_project_creation_options ,

preview_capacity_upgrade , list_operations , get_operation , and

wait_for_operation .

Change tools: create_standard_project , retry_project_provisioning ,

create_capacity_upgrade_quote , upgrade_project_capacity ,

cancel_operation , and retry_operation .

Project creation appears with an organization-wide connection. Capacity

upgrades use a current quote, a maximum charge guard, an idempotency key, and

your existing commercial authorization.

Database rows

Database tools work with standard projects.

View and validation tools: list_tables , read_table_rows , and

validate_row_write .

Change tool: upsert_row writes one bounded record with upsert behavior. It

works with standard projects. A request that also reconciles AI Search supplies

an idempotency key for safe replay. Use the CLI or Python SDK when an

application needs insert or ignore behavior. For a synchronized project, write

the record to the source PostgreSQL database.

Dashboard imports

Import tools follow CSV jobs started from the project’s Import page.

View tools: list_imports and get_import .

Change tool: cancel_import stops an eligible job after a destructive

action review.

The Dashboard handles file selection, upload, preview, configuration, and job

start. MCP continues with status, progress, and cancellation.

Synchronized projects

Sync tools guide source setup and manage the synchronization lifecycle.

Setup tools: get_synchronized_project_preflight ,

list_synchronized_source_tables , select_synchronized_tables , and

create_synchronized_project .

Lifecycle tools: get_synchronization_status , pause_synchronization ,

resume_synchronization , retry_synchronization , and

resnapshot_synchronization .

The Polygres Dashboard collects the source connection securely. MCP receives

the resulting preflight attempt ID and selected table information.

Polygres AI Search

Context tools cover collection setup, retrieval, diagnostics, filters, points,

and operations.

Collection views: get_context_capabilities , discover_context_sources ,

preflight_context_collection , list_context_collections ,

get_context_collection , get_context_collection_status ,

verify_context_collection , get_context_index_status ,

list_context_filters , get_context_point_status , and list_context_points .

Retrieval: context_search , search_full_text ,

context_text_hybrid_search , hybrid_search , context_graph_first_search ,

context_first_graph_search , context_rank_fusion_search ,

context_joint_search , group_context_results , count_context_points ,

get_context_facets , recommend_context_records ,

explore_context_records , explain_context_query , and

check_context_recall .

Configuration and point changes: create_context_collection ,

update_context_collection , reindex_context_collection ,

add_context_filter_column , add_context_filter_jsonb_path ,

upsert_context_points , reconcile_context_points ,

delete_context_collection , delete_context_points , and

backfill_context_points .

Your application or AI client creates source and query embeddings. Polygres

stores and retrieves the resulting evidence.

Graph retrieval

Graph tools cover discovery, configuration, builds, bounded traversal, and

maintenance.

View and retrieval tools: discover_graph_schema ,

get_graph_configuration , get_graph_status , get_graph_system ,

expand_graph , get_graph_neighborhood , find_related_records ,

find_graph_path , and find_graph_connection .

Configuration and maintenance tools: configure_graph ,

update_graph_system , build_graph , and run_graph_maintenance .

Graph and Context hybrid searches use both context and graph read scopes.

Diagnostics

Diagnostics provide concise project and retrieval evidence:

get_retrieval_readiness , get_context_diagnostics ,

get_context_index_diagnostics , get_context_index_advice ,

get_context_query_stats , get_project_capacity ,

get_project_storage_usage , get_project_metrics , and

get_project_metrics_history .

These tools return user-facing health, usage, and recommendations with request

IDs for follow-up.

Documentation

search_docs searches the public documentation included with the MCP release.

get_doc opens one result by document ID. Each result includes its public URL

and documentation version.

Other Polygres workflows

Polygres offers complementary interfaces for broader development work:

Use the CLI for migrations, Runtime key management, and interactive database work.

Use the Python SDK for long-running application integrations.

Use the Dashboard for project deletion, project pause and restore, import uploads, and source connection entry.

Use existing pgvector application code for registered legacy vector configurations.

This separation keeps MCP focused on predictable agent workflows while every

Polygres interface continues to serve its strongest use cases.

Request and result limits

MCP uses bounded JSON so requests stay predictable for interactive clients.

Input Limit

JSON request or result 1 MiB

Nested object and list depth 12 levels

Fields in one object 512

Items in one list 10,000

Characters in one string 100,000

Normal page size 1–100

wait_for_operation watch time 1–30 seconds

Operation polling interval 0.5–5 seconds

Use cursors for additional list pages and split larger inputs into bounded

batches. Ranked retrieval uses explicit result limits and returns provenance

for each result. A completed wait_for_operation watch returns the latest

observed state while the operation continues independently.

See MCP errors and recovery for request corrections,

retry decisions, and durable-operation follow-up.
