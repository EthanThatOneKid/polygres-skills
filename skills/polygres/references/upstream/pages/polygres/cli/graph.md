source: https://docs.evokoa.com/polygres/cli/graph
title: CLI graph retrieval | Polygres
source_hash: 045b6c5c7af79bd63a1d18890ba5927453fc02265654333cadf4cddb64180b2d
discovered_from: https://docs.evokoa.com/polygres

# CLI graph retrieval | Polygres

Graph retrieval

polygres graph discover

polygres --json graph config export

polygres graph config apply --file ./graph-config.json

polygres graph build

polygres graph status

Discovery proposes configuration but does not apply it. Export emits configuration: null on an unconfigured project. Apply accepts an exported wrapper or raw configuration and validates it before an API request. The CLI configures graph retrieval only. Query it with the Python SDK after the build is ready.
