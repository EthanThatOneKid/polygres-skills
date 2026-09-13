source: https://docs.evokoa.com/polygres/cli/installation-and-authentication
title: CLI installation and authentication | Polygres
source_hash: 7d6fcf8afc3ee383ab9bf956aab764c129eba5eb8e078c3b86d043d45795c0f6
discovered_from: https://docs.evokoa.com/polygres

# CLI installation and authentication | Polygres

Installation and authentication

The Polygres CLI requires Python 3.10 or newer. Install polygres-cli with pipx

to give the CLI its own Python environment:

pipx install "polygres-cli==0.5.0"

polygres --version

For an application that uses the SDK, create a virtual environment and install polygres-sdk there. This is separate from the pipx CLI environment.

python -m venv .venv

. .venv/bin/activate

pip install "polygres-sdk==0.5.0"

Package split migration

If you installed the combined polygres 0.2.x package, move to the separate

polygres-cli and polygres-sdk packages. For a pipx installation:

pipx uninstall polygres

pipx install "polygres-cli==0.5.0"

polygres --version

For an application virtual environment that needs both tools:

pip uninstall polygres

pip install "polygres-sdk==0.5.0"

pip install --force-reinstall "polygres-cli==0.5.0"

polygres --version

Check that polygres --version reports 0.5.0 . Your saved sign-in is preserved;

the CLI will prompt you to sign in again when your session needs renewal.

Upgrade to 0.5.0

CLI 0.5.0 lets you set up automatic embeddings and search with text through

existing Context commands. Upgrade your installation with:

pipx install "polygres-cli==0.5.0" --force

polygres --version

polygres embeddings sources --help

polygres context search --help

In an application virtual environment, use

pip install --upgrade "polygres-cli==0.5.0" instead. Your existing commands and

saved sign-in continue to work after the upgrade. Earlier CLI versions keep

supporting their existing commands and vector inputs.

To get started, choose a text column and a model, then preview the work before

starting generation. Polygres then tracks changes to your text and processes

them in your chosen automatic or manual mode. Follow the

automatic embeddings guide for the full setup.

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
