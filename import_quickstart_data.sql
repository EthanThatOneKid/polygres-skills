-- Quickstart sample dataset from the Polygres docs
-- Run this in the SQL Editor or import via Import > SQL.
-- Then configure Text/Vector/Graph retrieval in the dashboard.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS accounts (
  id   text PRIMARY KEY,
  name text
);

CREATE TABLE IF NOT EXISTS documents (
  id         text PRIMARY KEY,
  account_id text REFERENCES accounts(id),
  title      text,
  body       text,
  embedding  vector(8)
);

INSERT INTO accounts (id, name) VALUES
  ('acct_1', 'Acme Corp');

INSERT INTO documents (id, account_id, title, body, embedding) VALUES
  ('doc_1', 'acct_1', 'Refund Request', 'I need a refund for my recent purchase.', '[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]'),
  ('doc_2', 'acct_1', 'Login Issue',   'Password reset is not working.',       '[0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]');
