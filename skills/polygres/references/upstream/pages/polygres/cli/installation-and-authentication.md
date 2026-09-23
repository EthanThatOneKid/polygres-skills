source: https://docs.evokoa.com/polygres/cli/installation-and-authentication
title: CLI installation and authentication | Polygres
source_hash: cb83f57eccd7960c6ea864ca0e7454f418c151e07ecdd3e4b39aad6675715ac1
discovered_from: https://docs.evokoa.com/polygres

# CLI installation and authentication | Polygres

Installation and authentication

The Polygres CLI requires Python 3.10 or newer. Install polygres-cli with pipx

to give the CLI its own Python environment:

pipx install "polygres-cli==0.6.0"

polygres --version

For an application that uses the SDK, create a virtual environment and install polygres-sdk there. This is separate from the pipx CLI environment.

python -m venv .venv

. .venv/bin/activate

pip install "polygres-sdk==0.5.0"

Package split migration

If you installed the combined polygres 0.2.x package, move to the separate

polygres-cli and polygres-sdk packages. For a pipx installation:

pipx uninstall polygres

pipx install "polygres-cli==0.6.0"

polygres --version

For an application virtual environment that needs both tools:

pip uninstall polygres

pip install "polygres-sdk==0.5.0"

pip install --force-reinstall "polygres-cli==0.6.0"

polygres --version

Check that polygres --version reports 0.6.0 . Your saved sign-in is preserved;

the CLI will prompt you to sign in again when your session needs renewal.

Upgrade to 0.6.0

CLI 0.6.0 adds commands to retry rows whose text was too long and to watch

embedding progress. New configurations use automatic chunking by default.

For a pipx installation:

pipx install "polygres-cli==0.6.0" --force

polygres --version

For an application virtual environment:

pip install --upgrade "polygres-cli==0.6.0"

polygres --version

Your existing commands, JSON output, and saved sign-in keep working. Existing

embedding configurations keep their settings.

Next steps:

Set up embeddings .

Retry rows whose text was too long .

Check and watch progress .

Sign in

polygres login

polygres --json whoami

polygres login --timeout 120

polygres logout

polygres login opens your browser so you can approve the sign-in request. You

can also open the link printed in the terminal. Return to the terminal after

approval and run polygres --json whoami to confirm your account.

Use --timeout 120 to allow more time for approval. If the request expires,

run polygres login again to get a fresh link. Run polygres logout to clear

your saved sign-in.

The CLI uses your active organization in the dashboard. Switch organizations

there before selecting a project by name.
