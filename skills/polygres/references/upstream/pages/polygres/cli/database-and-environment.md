source: https://docs.evokoa.com/polygres/cli/database-and-environment
title: CLI database and environment | Polygres
source_hash: 1e58ebde5c11e203f3ef0a87e676a5616213139b88bd2a80bc7daec710bb55a7
discovered_from: https://docs.evokoa.com/polygres

# CLI database and environment | Polygres

Database and environment

The native database commands on this page apply only to managed database projects created with Host with Polygres . Synced projects do not issue PostgreSQL credentials or connection URLs, so polygres db psql and direct SQL access are unavailable for them. Run SQL against the source PostgreSQL database instead.

polygres env

polygres db info

polygres db psql

For a managed database project, env prints passwordless, POSIX-shell-quoted DATABASE_URL , DIRECT_URL , and

POLYGRES_RUNTIME_URL . It keeps API-key secrets separate. db info shows safe

connection metadata. db psql is an interactive command for standard human

output; it uses the direct host, requires psql on PATH , and prompts for the

database password. Use polygres --json db info or polygres --json env for

connection automation. When PostgreSQL client tools are ready, db psql opens

the session directly.

For a managed database project, open psql and paste SQL into the prompt. Do not describe this command as piping SQL unless you supply an actual pipe command. Use the direct URL for migrations and administrative tools, and use the pooled URL for normal application traffic.
