-- Import this file via Polygres Dashboard > Import > SQL
-- or paste into the SQL Editor.
--
-- Creates a child table of docs_pages that holds paragraph-chunked
-- documentation content and per-chunk vector(384) embeddings.
-- Run enrich_docs.py after importing to populate embeddings.

CREATE TABLE IF NOT EXISTS doc_chunks (
  id            text PRIMARY KEY,
  doc_id        text NOT NULL REFERENCES docs_pages(id) ON DELETE CASCADE,
  content       text NOT NULL,
  chunk_index   integer NOT NULL,
  embedding     vector(384)
);
