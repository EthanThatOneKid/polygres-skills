source: https://docs.evokoa.com/polygres/cli/installation-and-authentication
title: CLI installation and authentication | Polygres
source_hash: f336b492731e0f050ddaf30200bb408d97b7ede8aa8101cec63cec4a7fd4d1a7
discovered_from: https://docs.evokoa.com/polygres

# CLI installation and authentication | Polygres

Installation and authentication

The public CLI package is polygres-cli and requires Python 3.10 or newer. Install it with pipx so it does not alter an application environment:

pipx install "polygres-cli==0.1.2"

polygres --version

For an application that uses the SDK, create a virtual environment and install polygres-sdk there. This is separate from the pipx CLI environment.

python -m venv .venv

. .venv/bin/activate

pip install "polygres-sdk==0.1.0"

Package split migration

The combined polygres 0.2.x package included both the SDK and CLI. The SDK

0.1.x releases remove the polygres command from the SDK package. Replace the old pipx

installation with the standalone CLI:

pipx uninstall polygres

pipx install "polygres-cli==0.1.2"

polygres --version

For an application virtual environment that needs both tools:

pip uninstall polygres

pip install "polygres-sdk==0.1.0"

pip install --force-reinstall "polygres-cli==0.1.2"

polygres --version

Confirm the printed CLI version is 0.1.2 before continuing. Existing login credentials remain on disk; run polygres login again only if a command exits with authentication errors.

Sign in

polygres login

polygres --json whoami

polygres login --timeout 120

polygres logout

Login opens, and also prints, a browser approval URL. Approve the request in the browser. Browser-open failure is non-fatal; login polls until approved, denied, expired, or its timeout. Approval state is signed, and the resulting credential can be collected only once, so restart polygres login if the browser flow expires or the poll has already completed. The CLI has no terminal username/password flow and does not print tokens. logout removes local credentials even if remote revocation cannot complete. Active organization is determined by the dashboard, so switch organizations there before using projects by name.
