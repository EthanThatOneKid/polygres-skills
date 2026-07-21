source: https://docs.evokoa.com/polygres/cli/graph
title: CLI graph retrieval | Polygres
source_hash: 53734623e95129cb7105450a34a7abc6538c10130e542c75f2b823f621ff5cf4
discovered_from: https://docs.evokoa.com/polygres

# CLI graph retrieval | Polygres

Graph retrieval

polygres graph discover

polygres --json graph config export

polygres graph config apply --file ./graph-config.json

polygres graph build

polygres graph status

Discovery proposes configuration but does not apply it. Export emits configuration: null on an unconfigured project. Apply accepts an exported wrapper or raw configuration and validates it before an API request. The CLI configures graph retrieval only. Query it with the Python SDK after the build is ready.
