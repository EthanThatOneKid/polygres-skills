source: https://docs.evokoa.com/polygres/cli/vector
title: CLI vector retrieval | Polygres
source_hash: 2852d451f7a706907b830c5fb4063f6a724e4990cedc76c08c492b9b29fc0d11
discovered_from: https://docs.evokoa.com/polygres

# CLI vector retrieval | Polygres

Vector retrieval

polygres vector configs list

polygres vector configs create docs_embedding --table documents --embedding-column embedding --dimensions 1536

polygres vector reindex 123e4567-e89b-12d3-a456-426614174000

polygres vector configs delete 123e4567-e89b-12d3-a456-426614174000 --yes

Creation supports --schema , --row-id-column , --metric cosine|inner_product|l2 , --index-kind hnsw|none , repeated --metadata-column , and repeated --filter-column . The embedding column must already contain vectors from your model or embedding pipeline.
