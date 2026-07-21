source: https://docs.evokoa.com/polygres/cli/api-keys
title: CLI API keys | Polygres
source_hash: 8540679f1d1b249b2303ac3988f2467cd271ffd89bc4e6c97aaad3b6819cfab6
discovered_from: https://docs.evokoa.com/polygres

# CLI API keys | Polygres

API keys

polygres keys create local-dev

polygres keys list

polygres keys revoke 123e4567-e89b-12d3-a456-426614174000 --yes

keys create prints the raw Runtime API key exactly once. Save it immediately in a secret manager or local environment, then combine it with POLYGRES_RUNTIME_URL from polygres env .

export POLYGRES_API_KEY = "poly_live_..."

List output contains prefixes, not secrets. Revocation requires --yes in non-interactive use.
