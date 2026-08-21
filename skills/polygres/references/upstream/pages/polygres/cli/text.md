source: https://docs.evokoa.com/polygres/cli/text
title: CLI text retrieval | Polygres
source_hash: c52a6be4ae05955bfafc1b0e52a1e4469ff193ca754a3946161c86b59bf8121f
discovered_from: https://docs.evokoa.com/polygres

# CLI text retrieval | Polygres

Text retrieval

polygres text configs list

polygres text configs get docs_body

polygres text configs create-tsvector docs_body --table documents --tsvector-column body_tsv

polygres text configs create-tsvector docs_body --table documents --text-column body --generated-column body_tsv --yes

polygres text configs create-fuzzy docs_body_fuzzy --table documents --text-column body --similarity-threshold 0.3

polygres text configs update docs_body --metadata-column title --filter-column status

polygres text configs diagnostics docs_body

polygres text configs reindex docs_body

polygres text configs delete 123e4567-e89b-12d3-a456-426614174000 --yes

Use exactly one setup mode:

--tsvector-column registers an existing compatible TSVector column.

--text-column with --generated-column asks the existing configuration

endpoint to create the stored TSVector column, its GIN index, and the saved

configuration in one operation.

Generated-column mode changes the table, so interactive use asks for

confirmation. Pass --yes only after reviewing the table and column names. It

does not create or apply a migration. If setup fails, Polygres automatically

tries to remove the new generated column, index, and configuration.

Repeat --row-id-column for a compound row key. Repeat --metadata-column to

return additional properties and --filter-column to allow exact-match query

filters. Use diagnostics to compare saved and physical index state, then use

reindex after correcting a failed or stale target. Continue only when

index_status is ready .

The CLI calls POST /projects/{project_id}/text/configurations for both

existing-column and generated-column setup. Existing scripts that use

--tsvector-column keep the same behavior. See the Text Search API

reference for the request payloads and complete

endpoint list.
