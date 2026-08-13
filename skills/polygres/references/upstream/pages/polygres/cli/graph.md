source: https://docs.evokoa.com/polygres/cli/graph
title: CLI graph retrieval | Polygres
source_hash: b3b5bed6911d20df0a83cc5880ce574a933fd65aa2241aa25d15be69825135f8
discovered_from: https://docs.evokoa.com/polygres

# CLI graph retrieval | Polygres

Graph retrieval

polygres graph discover

polygres --json graph config export

polygres graph config apply --file ./graph-config.json

polygres graph build

polygres graph status

Discovery proposes configuration but does not apply it. Export emits configuration: null on an unconfigured project. Apply accepts an exported wrapper or raw configuration and validates it before an API request. The CLI configures graph retrieval only. Query it with the Python SDK after the build is ready.
