source: https://docs.evokoa.com/polygres/cli/projects
title: CLI projects | Polygres
source_hash: 1082fc72935462d0661d9cc5a3be9ef28a06c40abc6ed99c2f201b31f3f3e69d
discovered_from: https://docs.evokoa.com/polygres

# CLI projects | Polygres

Projects

polygres projects list

polygres projects create "Support Search"

polygres projects use "Support Search"

polygres projects status

Project names are exact and case-sensitive. If a name is ambiguous, use its project ID. projects create waits up to 600 seconds by default; use --no-wait or --timeout <seconds> as needed. Creating a project does not set the selected project. Run projects use explicitly.

polygres projects create "Support Search" --no-wait

polygres --project "Support Search" projects status

polygres config path

The selected project ID is stored locally. --project targets one command without changing it. Project deletion is deliberately dashboard-only. See dashboard projects and organizations .
