source: https://docs.evokoa.com/polygres/cli/database-and-environment
title: CLI database and environment | Polygres
source_hash: 93ba038bb80c39fa34a42c56b0b77ccfdcef33e0879e5087636cf6ca0ece398b
discovered_from: https://docs.evokoa.com/polygres

# CLI database and environment | Polygres

Database and environment

polygres env

polygres db info

polygres db psql

env prints passwordless, POSIX-shell-quoted DATABASE_URL , DIRECT_URL , and POLYGRES_RUNTIME_URL . It never prints an API-key secret. db info shows safe connection metadata. db psql uses the direct host, requires psql on PATH , and prompts for the database password. If psql is unavailable, it exits 9 and prints the command to run after installation.

Open psql and paste SQL into the prompt. Do not describe this command as piping SQL unless you supply an actual pipe command. Use the direct URL for migrations and administrative tools, and use the pooled URL for normal application traffic.
