source: https://docs.evokoa.com/polygres/cli/installation-and-authentication
title: CLI installation and authentication | Polygres
source_hash: d1f37d78247970dd3477b5fded1a9b7ca797a0abd333e4148231b5af6dc159e5
discovered_from: https://docs.evokoa.com/polygres

# CLI installation and authentication | Polygres

Installation and authentication

The public CLI package is polygres-cli and requires Python 3.10 or newer. Install it with pipx so it does not alter an application environment:

pipx install "polygres-cli==0.4.0"

polygres --version

For an application that uses the SDK, create a virtual environment and install polygres-sdk there. This is separate from the pipx CLI environment.

python -m venv .venv

. .venv/bin/activate

pip install "polygres-sdk==0.4.0"

Package split migration

The combined polygres 0.2.x package included both the SDK and CLI. The SDK

0.1.x releases remove the polygres command from the SDK package. Replace the old pipx

installation with the standalone CLI:

pipx uninstall polygres

pipx install "polygres-cli==0.4.0"

polygres --version

For an application virtual environment that needs both tools:

pip uninstall polygres

pip install "polygres-sdk==0.4.0"

pip install --force-reinstall "polygres-cli==0.4.0"

polygres --version

Confirm that the CLI reports version 0.4.0 before continuing. Existing login

credentials remain on disk. Sign in again when the CLI reports that the saved

session needs renewal.

Sign in

polygres login

polygres --json whoami

polygres login --timeout 120

polygres logout

Login opens, and also prints, a browser approval URL. Approve the request in the browser. Browser-open failure is non-fatal; login polls until approved, denied, expired, or its timeout. Approval state is signed, and the resulting credential can be collected only once, so restart polygres login if the browser flow expires or the poll has already completed. The CLI has no terminal username/password flow and does not print tokens. logout removes local credentials even if remote revocation cannot complete. Active organization is determined by the dashboard, so switch organizations there before using projects by name.
