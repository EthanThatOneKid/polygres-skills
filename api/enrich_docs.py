"""
Batch-generate Gemini embeddings for every row in docs_pages and store them.

Two modes:

  1. SQL mode (default) — prints UPDATE statements you can run in the
     Polygres SQL Editor.

       python api/enrich_docs.py

  2. Direct mode — connects to Polygres over PostgreSQL and writes
     embeddings directly. Requires POLYGRES_DIRECT_URL in the environment.

       python api/enrich_docs.py --direct
"""

import argparse
import os
import sys
import textwrap

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from api.embed import embed_many


def build_title_body(row: dict) -> str:
    title = row.get("title", "").replace("| Polygres", "").strip()
    return title


def vector_literal(values: list[float]) -> str:
    return "[" + ",".join(str(v) for v in values) + "]"


def sql_mode():
    import json

    manifest_path = os.path.join(
        _PROJECT_ROOT,
        "references",
        "upstream",
        "manifest.json",
    )
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    items = manifest["items"]
    texts = [build_title_body(item) for item in items]

    print("-- Generating embeddings with gemini-embedding-2 ...", flush=True)
    embeddings = embed_many(texts)

    print("-- Paste the following into your Polygres SQL Editor:\n")
    for item, emb in zip(items, embeddings):
        doc_id = os.path.splitext(os.path.basename(item["path"]))[0]
        lit = vector_literal(emb)
        print(
            textwrap.dedent(f"""\
            UPDATE docs_pages
               SET embedding = '{lit}'::vector
             WHERE id = '{doc_id}'
               AND embedding IS NULL;
            """)
        )


def direct_mode():
    import psycopg

    import json

    manifest_path = os.path.join(
        _PROJECT_ROOT,
        "references",
        "upstream",
        "manifest.json",
    )
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    items = manifest["items"]
    texts = [build_title_body(item) for item in items]

    print("-- Generating embeddings ...", flush=True)
    embeddings = embed_many(texts)

    direct_url = os.environ["POLYGRES_DIRECT_URL"]
    with psycopg.connect(direct_url) as conn:
        with conn.cursor() as cur:
            for item, emb in zip(items, embeddings):
                doc_id = os.path.splitext(os.path.basename(item["path"]))[0]
                lit = vector_literal(emb)
                cur.execute(
                    "UPDATE docs_pages SET embedding = %s::vector WHERE id = %s AND embedding IS NULL",
                    (lit, doc_id),
                )
        conn.commit()

    updated = sum(1 for _ in embeddings)
    print(f"Done. {updated} rows updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich docs_pages with Gemini embeddings.")
    parser.add_argument(
        "--direct",
        action="store_true",
        help="Write directly via PostgreSQL (requires POLYGRES_DIRECT_URL).",
    )
    args = parser.parse_args()

    if args.direct:
        direct_mode()
    else:
        sql_mode()
