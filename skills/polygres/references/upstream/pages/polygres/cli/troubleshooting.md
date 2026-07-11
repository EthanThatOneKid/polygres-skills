source: https://docs.evokoa.com/polygres/cli/troubleshooting
title: CLI troubleshooting | Polygres
source_hash: 578ca47234ba599d1b452feabb858c7c7c7b7aafc878cbd12e05a1c0bb69696b
discovered_from: https://docs.evokoa.com/polygres

# CLI troubleshooting | Polygres

CLI troubleshooting

Symptom Action

polygres --version is older than 0.1.0 Upgrade with pipx install "polygres-cli==0.1.0" --force , or pip install --force-reinstall "polygres-cli==0.1.0" in your app venv. See package split migration .

Exit 3 or “Run polygres login ” Run polygres login , then confirm with polygres --json whoami .

Project is not selected Run polygres projects use "Project Name" , or use --project before the command.

Name is ambiguous Use the project ID from polygres projects list .

Project is still provisioning Run polygres projects status ; use the dashboard if provisioning fails.

db psql exits 9 Install PostgreSQL client tools, then rerun polygres db psql .

Text or vector query is not ready Check text configs list , vector configs list , and polygres ready .

You need to delete a project Use the dashboard project lifecycle controls , not the CLI.

For a request failure, preserve the request ID from JSON or error output when contacting support. See reference troubleshooting for dashboard and runtime guidance.
