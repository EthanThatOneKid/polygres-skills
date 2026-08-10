source: https://docs.evokoa.com/polygres/cli/vector
title: CLI vector retrieval | Polygres
source_hash: 995b004ff7b27265d562ba7a6c5ee7a68a60c5801b8aef6068eb7e7a583e02f0
discovered_from: https://docs.evokoa.com/polygres

# CLI vector retrieval | Polygres

Vector retrieval

New pgvector configuration registration is retired. Use a

pgContext collection for new vector setup.

The legacy vector configs create command remains in the CLI only to return the

stable VECTOR_CREATION_RETIRED migration error.

Previously registered vector configurations continue to support listing,

default selection, reindexing, and deletion. Legacy retrieval uses only a

persisted enabled registration that is effectively Ready. HNSW requires its

exact physical index to be Ready; an existing index_kind: none registration

can be Ready for exact scan without HNSW. An unregistered physical index is not

synthesized into a configuration, and the retired API cannot register or

re-enable one.

polygres vector configs list

polygres vector configs set-default 123e4567-e89b-12d3-a456-426614174000

polygres vector reindex 123e4567-e89b-12d3-a456-426614174000

polygres vector configs delete 123e4567-e89b-12d3-a456-426614174000 --yes

To configure a new searchable vector source, create a collection with a native

pgcontext.vector(n) column. You can use an existing compatible

public.vector(n) column as the source; ordinary Context collection creation

converts it in place to pgcontext.vector(n) . Polygres does not generate

embeddings, so populate the vector column from your model or embedding pipeline

before searching it.

polygres context capabilities

polygres context sources discover

polygres context collections create support_docs \

--source new-table \

--table support_docs \

--dimensions 768

If a persisted legacy configuration still owns the selected column, remove

that registration before using ordinary Context collection creation. Neither

opening the dashboard collection form nor creating a collection automatically

deletes a legacy registration. The dashboard currently offers only native

pgContext columns in its Existing vector column source picker, so use the

CLI or API for an explicitly reviewed in-place pgvector conversion. Inspect

and delete the exact legacy configuration only after explicit approval, then

create the Context collection from the same table and column.

polygres context init is only a guided way to choose one eligible persisted

legacy registration and submit ordinary Context collection creation. It does

not activate an internal same-column bridge or preserve the old pgvector index;

the selected column follows the same native in-place conversion described

above.
