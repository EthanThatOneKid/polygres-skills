"""
Batch-generate Gemini embeddings for every doc chunk and store them.

Embeds the full body text of each documentation page (not just titles)
using paragraph-based chunking for scalable vector search.

Two modes:

  1. SQL mode (default) — prints INSERT statements for the SQL Editor.
  2. Direct mode — writes directly via PostgreSQL.

       python api/enrich_docs.py
       python api/enrich_docs.py --direct
"""

import argparse
import json
import os
import re
import sys
import textwrap

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from api.chunk_docs import chunk_text  # noqa: E402
from api.embed import embed_many  # noqa: E402


def strip_frontmatter(text: str) -> str:
    lines = text.split("\n")
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith(("source:", "title:", "source_hash:", "discovered_from:", "#")) or line.strip() == "":
            body_start = i + 1
        else:
            break
    return "\n".join(lines[body_start:])


def vector_literal(values: list[float]) -> str:
    return "[" + ",".join(str(v) for v in values) + "]"


def process_all_items(sql_output: bool = True):
    manifest_path = os.path.join(_PROJECT_ROOT, "references", "upstream", "manifest.json")
    pages_dir = os.path.join(_PROJECT_ROOT, "references", "upstream", "pages")

    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    all_chunks: list[dict] = []
    for item in manifest["items"]:
        doc_id = os.path.splitext(os.path.basename(item["path"]))[0]
        title = item["title"].replace(" | Polygres", "").strip()
        md_path = os.path.join(pages_dir, item["path"])

        if not os.path.exists(md_path):
            print(f"-- WARNING: {md_path} not found, skipping", file=sys.stderr)
            continue

        md_text = open(md_path, encoding="utf-8").read()
        body = strip_frontmatter(md_text)
        full_text = f"{title}\n\n{body}"

        chunks = chunk_text(full_text)
        for idx, chunk in enumerate(chunks):
            all_chunks.append({
                "chunk_id": f"chunk_{doc_id}_{idx}",
                "doc_id": doc_id,
                "content": chunk,
                "chunk_index": idx,
            })

    if not all_chunks:
        print("-- No chunks to embed.", file=sys.stderr)
        return

    print(f"-- {len(all_chunks)} chunks from {len(manifest['items'])} pages", flush=True)
    texts = [c["content"] for c in all_chunks]
    embeddings = embed_many(texts)

    if sql_output:
        conn = None
    else:
        import psycopg

        direct_url = os.environ["POLYGRES_DIRECT_URL"]
        conn = psycopg.connect(direct_url)

    for chunk, emb in zip(all_chunks, embeddings):
        lit = vector_literal(emb)

        if sql_output:
            escaped = chunk["content"].replace("'", "''")
            print(
                textwrap.dedent(f"""\
                INSERT INTO doc_chunks (id, doc_id, content, chunk_index, embedding) VALUES
                  ('{chunk['chunk_id']}', '{chunk['doc_id']}', '{escaped}', {chunk['chunk_index']}, '{lit}'::vector)
                ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding;
                """)
            )
        else:
            conn.cursor().execute(
                "INSERT INTO doc_chunks (id, doc_id, content, chunk_index, embedding) "
                "VALUES (%s, %s, %s, %s, %s::vector) "
                "ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding",
                (chunk["chunk_id"], chunk["doc_id"], chunk["content"], chunk["chunk_index"], lit),
            )

    if conn:
        conn.commit()
        conn.close()
        print(f"Done. {len(all_chunks)} rows written.")

    print(f"-- {len(all_chunks)} chunks processed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich doc sections with Gemini embeddings.")
    parser.add_argument(
        "--direct",
        action="store_true",
        help="Write directly via PostgreSQL (requires POLYGRES_DIRECT_URL).",
    )
    args = parser.parse_args()
    process_all_items(sql_output=not args.direct)
