---
name: polygres
description: Master Polygres workflow skill backed by the nightly mirrored docs in references/upstream.
compatibility: Created for any AI agent. No external services required.
metadata:
  author: EthanThatOneKid
  version: "0.1"
---

# Polygres

Use this skill as the entry point for Polygres work.

This repository keeps a nightly mirror of the public Polygres docs under `references/upstream/`. Treat that mirror as the source of truth for the eventual subcommand map and workflow routing.

## Subcommand map

- `polygres start` - what Polygres is, how the product fits, and the shortest path from account to query.
  - Source docs: `What is Polygres?`, `Quickstart`, `Key Concepts`, `Core Workflow`, `Common Use Cases`
- `polygres workspace` - organization, project, data loading, and dashboard operations.
  - Source docs: `Projects & Organizations`, `Load & Manage Data`, `Querying from Dashboard`, `Database Access & Connections`
- `polygres sdk` - application integration and client setup.
  - Source docs: `Python SDK`, `Connect Your App`, `Connection Examples`
- `polygres retrieve` - retrieval configuration and query patterns.
  - Source docs: `Configure Retrieval`, `Retrieval Integration Patterns`, `Routes`
- `polygres reference` - guardrails, permissions, limits, and troubleshooting.
  - Source docs: `Security Basics`, `Roles & Permissions`, `Limits`, `Error Codes`, `Troubleshooting`

## Upstream references

- `references/upstream/manifest.json`
- `references/upstream/pages/**`

## Routing rule

Route to the smallest command that matches the user’s intent.

- Use `start` for product orientation and onboarding.
- Use `workspace` for organization, project, data, and dashboard tasks.
- Use `sdk` for code integration and credentials.
- Use `retrieve` for search/query configuration and API route details.
- Use `reference` for security, limits, errors, and debugging.
