source: https://docs.evokoa.com/polygres/cli/graph
title: CLI graph retrieval | Polygres
source_hash: 08e6e7a014686b83eb46b4154d2e315547e5edcd6a4e4199b81e15412658530b
discovered_from: https://docs.evokoa.com/polygres

# CLI graph retrieval | Polygres

Graph retrieval

polygres graph discover

polygres --json graph config export

polygres graph config apply --file ./graph-config.json

polygres graph build

polygres graph status

Discovery proposes configuration but does not apply it. Export emits configuration: null on an unconfigured project. Apply accepts an exported wrapper or raw configuration and validates it before an API request. The CLI configures graph retrieval only. Query it with the Python SDK after the build is ready.
