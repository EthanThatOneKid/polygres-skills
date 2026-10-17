source: https://docs.evokoa.com/polygres/cli/graph
title: CLI graph retrieval | Polygres
source_hash: 0874385c94b6e74bbd970c041880c5f7e3a847c61c589054c09221536c5d1795
discovered_from: https://docs.evokoa.com/polygres

# CLI graph retrieval | Polygres

Graph retrieval

polygres graph discover

polygres --json graph config export

polygres graph config apply --file ./graph-config.json

polygres graph build

polygres graph status

Discovery proposes configuration but does not apply it. Export emits configuration: null on an unconfigured project. Apply accepts an exported wrapper or raw configuration and validates it before an API request. The CLI configures graph retrieval only. After the build is ready, query it with the Python SDK or follow the Graph Retrieval API reference for REST and Python examples.
