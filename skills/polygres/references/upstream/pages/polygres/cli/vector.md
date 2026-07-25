source: https://docs.evokoa.com/polygres/cli/vector
title: CLI vector retrieval | Polygres
source_hash: d450f623de141e57bdd0e24d67b004eb5501201363ded63491e01ba621ef2277
discovered_from: https://docs.evokoa.com/polygres

# CLI vector retrieval | Polygres

Vector retrieval

polygres vector configs list

polygres vector configs create docs_embedding --table documents --embedding-column embedding --dimensions 1536

polygres vector configs set-default 123e4567-e89b-12d3-a456-426614174000

polygres vector reindex 123e4567-e89b-12d3-a456-426614174000

polygres vector configs delete 123e4567-e89b-12d3-a456-426614174000 --yes

Creation supports --schema , --row-id-column , --metric cosine|inner_product|l2 , --index-kind hnsw|none , repeated --metadata-column , and repeated --filter-column . The embedding column must already contain vectors from your model or embedding pipeline.

Use vector configs set-default <config-id> to select the configuration used when a vector or hybrid query does not name one explicitly. The target configuration must be ready before retrieval can use it. Run vector configs list to find the configuration ID and inspect is_default , index_status , and index_error .

The set-default command is available in CLI 0.1.3 and later.
