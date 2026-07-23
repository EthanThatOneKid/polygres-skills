source: https://docs.evokoa.com/polygres/reference/changelog
title: Changelog | Polygres
source_hash: f34cc8a5c54b457bdc6f8d408e30fa14c066806d28d213b4c794d4c875762af8
discovered_from: https://docs.evokoa.com/polygres

# Changelog | Polygres

Changelog

2026-07-20

Accounts and teams

Organization invitations now have a clearer review flow. After signing in, you can choose which organization to join, verify your email if needed, or decline the invitation and create your own organization.

Projects and data

Project API Keys are displayed immediately after creation. Copy the secret when it appears because it cannot be shown again.

Graph and vector readiness now reflects the actual database configuration more accurately, reducing false ready states after configuration or index changes.

Developer tools

Polygres CLI 0.1.2 increases the supported CSV upload size to the storage allowance of your project tier and improves upload reliability.

polygres-skills

Released an expanded polygres-skills package for Polygres operations and Python retrieval:

polygres-cli operates projects, imports, migrations, credentials, and retrieval setup;

polygres-sdk builds Python graph, vector, text, and hybrid retrieval.

Install the package with npx skills add Evokoa/polygres-skills , or through the Polygres plugin marketplace for Codex or Claude Code.

2026-07-09

Polygres CLI 0.1.0

Added browser-based sign-in and commands for managing projects, connection details, Runtime API Keys, CSV imports, and migrations.

Added graph, vector, and text-search configuration commands, plus retrieval-readiness checks.

Added JSON output, stable exit codes, and confirmation prompts for automation and destructive operations.

Runtime API Key secrets are shown once when created and are excluded from later list and environment output.
