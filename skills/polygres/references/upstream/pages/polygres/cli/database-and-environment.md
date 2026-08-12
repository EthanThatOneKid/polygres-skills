source: https://docs.evokoa.com/polygres/cli/database-and-environment
title: CLI database and environment | Polygres
source_hash: 200fb6c5dd5645ef9d67912425689c15e0d3ff03d5b5e4d8d1df34122969fc79
discovered_from: https://docs.evokoa.com/polygres

# CLI database and environment | Polygres

Database and environment

polygres env

polygres db info

polygres db psql

env prints passwordless, POSIX-shell-quoted DATABASE_URL , DIRECT_URL , and

POLYGRES_RUNTIME_URL . It keeps API-key secrets separate. db info shows safe

connection metadata. db psql is an interactive command for standard human

output; it uses the direct host, requires psql on PATH , and prompts for the

database password. Use polygres --json db info or polygres --json env for

connection automation. When PostgreSQL client tools are ready, db psql opens

the session directly.

Open psql and paste SQL into the prompt. Do not describe this command as piping SQL unless you supply an actual pipe command. Use the direct URL for migrations and administrative tools, and use the pooled URL for normal application traffic.
