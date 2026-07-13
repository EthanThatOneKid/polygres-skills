source: https://docs.evokoa.com/polygres/getting-started/common-use-cases
title: Common use cases | Polygres
source_hash: 9a7ea20fc1ddfe34a0b319155338a7c88be17490a7560887d84a62ea00ba1903
discovered_from: https://docs.evokoa.com/polygres

# Common use cases | Polygres

Common use cases

Polygres works best when application records and retrieval context belong together. Your product keeps using PostgreSQL, while the dashboard and API add graph, vector, text, and hybrid ways to retrieve from those records.

Choose the retrieval mode by question

Question Start with

“What records are connected to this customer, account, device, or event?” Graph retrieval.

“What content means something similar to this text or record?” Vector retrieval over stored embeddings.

“Which rows contain these words, phrases, or a close spelling?” Text search using TSVector full-text or Fuzzy matching.

“What is semantically similar within relevant connected context?” Hybrid retrieval, which combines graph and vector.

A product can use all four. Text search remains useful even when vector search is available: exact terminology, names, error codes, and misspellings often need lexical matching rather than semantic similarity.

Customer support search and investigation

Store accounts, users, tickets, messages, incidents, and product areas in PostgreSQL.

A representative schema looks like this:

accounts (id, name , plan, created_at)

customers (id, account_id, name , email)

tickets (id, customer_id, subject , body, status , created_at)

messages (id, ticket_id, author, body, created_at)

incidents (id, ticket_id, severity, postmortem)

product_areas (id, name , slug)

ALTER TABLE tickets ADD COLUMN body_embedding vector( 1536 );

ALTER TABLE tickets ADD COLUMN body_tsv tsvector

GENERATED ALWAYS AS (to_tsvector( 'english' , body)) STORED;

TSVector search finds exact error messages and policy terms; Fuzzy search catches misspelled ticket titles and labels.

Vector retrieval finds tickets with similar meaning even when they use different wording.

Graph retrieval follows the customer, account, product, incident, and conversation relationships around a ticket.

Hybrid retrieval narrows semantic results to relevant connected context.

Start in the dashboard with Text search setup ( /{organization}/{projectId}/workspace/text-search ), Vector setup ( /{organization}/{projectId}/workspace/vector ), and Graph setup ( /{organization}/{projectId}/workspace/graph ), then validate the experience in the query workbench ( /{organization}/{projectId}/workspace/query ).

This pattern is the core Polygres value proposition in one workflow: four retrieval modes, one operational data store, and no second system to synchronize before support agents can see current data.

Retrieval-augmented generation and knowledge features

Use Polygres as the operational store behind an assistant, answer system, or context-building feature.

PostgreSQL stores documents, chunks, sources, permissions metadata, and application records. Text search handles exact phrases and product terminology. Vector retrieval finds semantically relevant passages. Graph retrieval connects passages to products, customers, cases, or citations. Hybrid retrieval combines semantic ranking with those relationships.

Polygres supplies retrieval, not an embedding model or language model. Generate embeddings in your own pipeline, store them in a fixed-dimension vector(n) column, and keep authorization decisions in your application.

Account and customer intelligence

A B2B SaaS product can connect organizations, users, subscriptions, events, support cases, and feature usage.

Text search finds named features, notes, and contract language. Vector retrieval groups similar feedback or requests. Graph retrieval exposes the records surrounding an account or user. Hybrid retrieval helps find similar issues among customers with relevant relationships.

This pattern works well for success teams, internal search, product feedback analysis, and account-health investigations without exporting operational records to a separate graph system.

Fraud, risk, and entity investigation

Store users, devices, addresses, payments, orders, claims, and review notes in PostgreSQL.

Graph retrieval surfaces shared identifiers and multi-hop connections. Text search finds names, notes, codes, and fuzzy variations. Vector retrieval can compare embedded descriptions or behavior summaries. Hybrid retrieval combines similarity with connected entities to produce a more focused candidate set.

Choose graph relationships deliberately. Broad hubs can connect too many records and reduce result quality. Use the Product Guide for Choosing graph relationships before building investigation paths.

Catalog, marketplace, and recommendation features

Store products, sellers, categories, inventory, reviews, and customer activity in the same project.

Text search supports product titles, SKUs, attributes, and misspellings. Vector retrieval finds semantically similar products or reviews. Graph retrieval follows seller, category, order, and customer relationships. Hybrid retrieval combines product similarity with connected marketplace context.

Use the pooled PostgreSQL connection for the transactional catalog. Use retrieval APIs for recommendation, discovery, and exploration features in backend services.

Data migration followed by richer retrieval

Polygres can also start as a database modernization project.

Create an organization-owned project.

Move an existing PostgreSQL database through a direct connection or import.

Point application traffic at the pooled connection.

Add graph, vector, text, and hybrid retrieval incrementally over the migrated schema.

This lets a team establish managed PostgreSQL first and add retrieval only where it improves a real product workflow.

Pick a practical first feature

A small, measurable first use case is better than configuring every table:

Choose text search for a known phrase or fuzzy lookup problem.

Choose vector retrieval for semantic similarity over an existing embedding column.

Choose graph retrieval for a connected-record workflow with clear relationships.

Choose hybrid retrieval when graph context and vector similarity are both already useful.

Test the feature in the dashboard, review result quality with domain users, then move the validated query into backend application code.

Next steps

Product Guides

Load and manage data

Configure and query retrieval

Choosing graph relationships

Retrieval integration patterns

Reference

Routes

Error codes
