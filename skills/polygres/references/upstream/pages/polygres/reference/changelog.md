source: https://docs.evokoa.com/polygres/reference/changelog
title: Changelog | Polygres
source_hash: 5e00434297e1ffcb124065563f2d770d57a458cd990a4d292aab12053bfe1632
discovered_from: https://docs.evokoa.com/polygres

# Changelog | Polygres

Changelog

2026-07-09

Polygres CLI v0.1.0

Features & Capabilities

Session & Organization Management

Account Control: Sign in, sign out, and verify your active session using login , logout , and whoami .

Organization Context: The CLI automatically uses your active organization. To switch organizations, use the Polygres dashboard.

Authentication Note: Browser approval is the CLI authentication flow. See the CLI authentication documentation for current availability and setup instructions.

Project & Database Management

Project Lifecycle: List, select, create, and monitor projects directly from the terminal. Use the global --project flag for one-off project execution.

App Environment: Configure application environments using env .

Direct Database Access: Inspect connection details with db info or open a native Postgres session over SSL using db psql (requires a local psql installation).

Graph & Search Configurations

Knowledge Graphs: Discover graph relationships, export or apply graph configurations, trigger a graph build, and track build status.

Vector Search: Create, manage, and reindex vector configurations.

Text Search: Build and manage TSVector and fuzzy text search configurations.

Readiness Checks: Verify graph, vector, and hybrid retrieval readiness with ready , or check text search readiness using text configs list .

Data & Migrations

CSV Imports: Streamline data ingestion. Start imports, monitor status, or block execution until completion using --wait and --timeout .

Schema Migrations: Track and apply SQL migration files.

Runtime API Keys: Provision, list, and revoke Runtime API keys.

Security & Automation

Destructive Safeguards: All destructive commands require explicit confirmation unless bypassed with the --yes flag.

Credential Masking: Runtime API key secrets are never exposed in env or keys list output. Secrets are displayed exactly once upon creation.

Secure Local Storage: Credentials are saved to ~/.config/polygres/config.json with owner-only permissions on macOS and Linux. Verbose traces automatically redact sensitive secrets.

CI/CD Integration:

Pass the --json flag for stable, script-friendly top-level fields.

Supports the global flags --no-color , --quiet , and --verbose .

Distinct exit codes support streamlined handling of authentication, permission, not-found, conflict, rate-limit, service, and local dependency errors.

Troubleshooting: Locate the local configuration file using config path when debugging or contacting support.
