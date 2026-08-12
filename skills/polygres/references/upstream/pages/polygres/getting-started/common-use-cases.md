source: https://docs.evokoa.com/polygres/getting-started/common-use-cases
title: Common use cases | Polygres
source_hash: b9d543d59195f6f614a6901654a51d8e1a8379c2e671701e2a4f1f718e2603ef
discovered_from: https://docs.evokoa.com/polygres

# Common use cases | Polygres

Common use cases

Polygres works best when application records and retrieval context belong

together. Your product keeps using PostgreSQL, while the dashboard, CLI, API,

and SDK add graph, vector, text, hybrid, and pgContext ways to retrieve from

those records.

Choose the retrieval mode by question

Question Start with

“What records are connected to this customer, account, device, or event?” Graph retrieval.

“What content means something similar to this text or record?” pgContext dense retrieval over stored embeddings.

“Which rows contain these words, phrases, or a close spelling?” Text search using TSVector full-text or Fuzzy matching.

“What is semantically similar within relevant connected context?” pgContext graph-composed, rank-fusion, or Joint retrieval .

“How do I build a collection with semantic, lexical, filter, graph, and Joint retrieval?” pgContext AI Search through the CLI, API, or Python SDK.

A product can combine these modes. Text search remains useful alongside

semantic search because exact terminology, names, error codes, and misspellings

benefit from lexical matching. Legacy Vector and Legacy Hybrid remain available

only for persisted registrations that are effectively Ready. HNSW requires its

matching physical index to be Ready; an existing exact-scan index_kind: none

registration does not. A physical-only pgvector index is never implicitly

usable.

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

Create the TSVector configuration from tickets.body in the dashboard, with

the CLI, or through POST /text/configurations . Polygres can create the stored

generated column and its GIN index in the same setup operation, so this feature

does not require a separate migration.

TSVector search finds exact error messages and policy terms; Fuzzy search catches misspelled ticket titles and labels.

pgContext dense retrieval finds tickets with similar meaning even when they use different wording.

Graph retrieval follows the customer, account, product, incident, and conversation relationships around a ticket.

pgContext graph-composed, rank-fusion, or Joint retrieval combines semantic results with relevant connected context.

Start in the dashboard with Text search setup ( /{organization}/{projectId}/workspace/text-search ), AI Context (Vector) setup ( /{organization}/{projectId}/workspace/vector ), and Graph setup ( /{organization}/{projectId}/workspace/graph ). Verify retrieval readiness there, then exercise the intended method through the public API or Python SDK, or use the CLI for pgContext.

This pattern is the core Polygres value proposition in one workflow:

complementary retrieval modes, one operational data store, and no second system

to synchronize before support agents can see current data.

Retrieval-augmented generation and knowledge features

Use Polygres as the operational store behind an assistant, answer system, or context-building feature.

PostgreSQL stores documents, chunks, sources, permissions metadata, and

application records. Text search handles exact phrases and product terminology.

pgContext dense retrieval finds semantically relevant passages. Graph retrieval

connects passages to products, customers, cases, or citations. pgContext

graph-composed, rank-fusion, or Joint retrieval combines semantic ranking with

those relationships.

Generate embeddings in your application pipeline and store them in the vector

type selected by the retrieval workflow. Authenticate and authorize the request

in your backend first, then derive tenant, user, or permission scope from that

trusted authorization context. Retrieval filters narrow the already authorized

search; they are not an authorization boundary and should not be copied from an

untrusted client request. pgContext collections use native

pgcontext.vector(n) columns and support dense, text-hybrid, graph-composed,

rank-fusion, and Joint retrieval.

Account and customer intelligence

A B2B SaaS product can connect organizations, users, subscriptions, events, support cases, and feature usage.

Text search finds named features, notes, and contract language. pgContext dense

retrieval groups similar feedback or requests. Graph retrieval exposes the

records surrounding an account or user. pgContext composed retrieval helps find

similar issues among customers with relevant relationships.

This pattern works well for success teams, internal search, product feedback analysis, and account-health investigations without exporting operational records to a separate graph system.

Fraud, risk, and entity investigation

Store users, devices, addresses, payments, orders, claims, and review notes in PostgreSQL.

Graph retrieval surfaces shared identifiers and multi-hop connections. Text

search finds names, notes, codes, and fuzzy variations. pgContext dense

retrieval can compare embedded descriptions or behavior summaries, while its

graph-composed methods combine similarity with connected entities to produce a

more focused candidate set.

Choose graph relationships deliberately. Broad hubs can connect too many records and reduce result quality. Use the Product Guide for Choosing graph relationships before building investigation paths.

Catalog, marketplace, and recommendation features

Store products, sellers, categories, inventory, reviews, and customer activity in the same project.

Text search supports product titles, SKUs, attributes, and misspellings.

pgContext dense retrieval finds semantically similar products or reviews. Graph

retrieval follows seller, category, order, and customer relationships. pgContext

composed retrieval combines product similarity with connected marketplace

context.

Use the pooled PostgreSQL connection for the transactional catalog. Use retrieval APIs for recommendation, discovery, and exploration features in backend services.

Data migration followed by richer retrieval

Polygres can also start as a database modernization project.

Create an organization-owned project.

Move an existing PostgreSQL database through a direct connection or import.

Point application traffic at the pooled connection.

Add graph and text retrieval incrementally over the migrated schema.

Add pgContext collections for new semantic and composed retrieval, including

collection lifecycle, filters, point synchronization, and combined modes.

This lets a team establish managed PostgreSQL first and add retrieval only where it improves a real product workflow.

Pick a practical first feature

A small, measurable first use case is better than configuring every table:

Choose text search for a known phrase or fuzzy lookup problem.

Choose pgContext dense retrieval for semantic similarity over an existing embedding column.

Choose graph retrieval for a connected-record workflow with clear relationships.

Choose a pgContext composed method when graph context and semantic similarity are both useful.

Choose pgContext when the feature benefits from a managed collection with

semantic, lexical, filter, graph, or Joint retrieval options.

Verify graph, text, and vector readiness in the dashboard, then exercise the

intended method through the CLI, API, or SDK. Review result quality with domain

users, then move the validated query into backend application code.

Next steps

Product Guides

Load and manage data

Configure and query retrieval

Choosing graph relationships

Retrieval integration patterns

Reference

Routes

Error codes
