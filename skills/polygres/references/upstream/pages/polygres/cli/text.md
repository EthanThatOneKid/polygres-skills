source: https://docs.evokoa.com/polygres/cli/text
title: CLI text retrieval | Polygres
source_hash: 7db5f5f5e8efbe1dc853f0709923ce0bd4762697717f34a738ebc8272e347ad3
discovered_from: https://docs.evokoa.com/polygres

# CLI text retrieval | Polygres

Text retrieval

polygres text configs list

polygres text configs create-tsvector docs_body --table documents --tsvector-column body_tsv

polygres text configs create-tsvector docs_body --table documents --text-column body --generated-column body_tsv --yes

polygres text configs create-fuzzy docs_body_fuzzy --table documents --text-column body --similarity-threshold 0.3

polygres text configs delete 123e4567-e89b-12d3-a456-426614174000 --yes

Use exactly one of --tsvector-column , or --text-column with --generated-column . Generated-column mode applies a migration and needs --yes for non-interactive use. If its migration succeeds but registration fails, rerun using --tsvector-column body_tsv . There is no text reindex command; query readiness from text configs list when index_status is ready .
