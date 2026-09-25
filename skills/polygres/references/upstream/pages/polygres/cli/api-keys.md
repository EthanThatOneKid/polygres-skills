source: https://docs.evokoa.com/polygres/cli/api-keys
title: CLI API keys | Polygres
source_hash: c7600dbec39fe98e311d4deda1f74c83068b9743f44ecef825adb510491e6a44
discovered_from: https://docs.evokoa.com/polygres

# CLI API keys | Polygres

API keys

polygres keys create local-dev

polygres keys list

polygres keys revoke 123e4567-e89b-12d3-a456-426614174000 --yes

Run keys create without --quiet so the raw Runtime API key is displayed

once. Save it immediately in a secret manager or local environment, then

combine it with POLYGRES_RUNTIME_URL from polygres env .

export POLYGRES_API_KEY = "poly_live_..."

List output contains prefixes, not secrets. Revocation requires --yes in non-interactive use.
