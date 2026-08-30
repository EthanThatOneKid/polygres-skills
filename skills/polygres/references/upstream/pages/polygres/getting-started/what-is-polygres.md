source: https://docs.evokoa.com/polygres/getting-started/what-is-polygres
title: What is Polygres? | Polygres
source_hash: 721ede8087c0c20ac8ea4f2b04389cbb6d7c7bd4c59cb89048e9cd4e1aa49c2e
discovered_from: https://docs.evokoa.com/polygres

# What is Polygres? | Polygres

What is Polygres?

Polygres is a managed PostgreSQL service with graph, vector, text, hybrid, and

pgContext AI Search built around the same project data. Your application keeps

using PostgreSQL for normal reads and writes while your team adds richer ways

to find and connect records.

The result is one operational data foundation for your SaaS product: PostgreSQL stays the source of truth, and retrieval is configured over the tables you already manage in Polygres.

One database, complementary retrieval modes

Graph pgContext AI Search Text Legacy Vector Legacy Hybrid

Graph Records connected through relationships, such as a customer, their account, tickets, messages, and related incidents.

Mode What it helps you find

Graph Records connected through relationships, such as a customer, their account, tickets, messages, and related incidents.

Legacy Vector (deprecated) Compatibility retrieval for a persisted pgvector configuration.

Text Words and phrases through TSVector full-text search, or close text matches through Fuzzy pg_trgm search.

Legacy Hybrid (deprecated) Compatibility retrieval that combines a ready graph build with an effectively Ready persisted Legacy vector registration.

pgContext AI Search The normal path for new semantic and composed retrieval, with collection-based dense, grouped, text-hybrid, graph-composed, rank-fusion, and Joint methods through the CLI, API, or Python SDK.

Your data workflow creates embeddings and stores them in PostgreSQL. For new

vector and hybrid development, create a pgContext collection with a native

pgcontext.vector(n) column and use the Context API or project.context SDK

namespace. A compatible existing public.vector(n) column can be migrated

during collection creation; Polygres converts that column in place to

pgcontext.vector(n) . Deprecated Vector and Hybrid surfaces continue to

support existing integrations while teams adopt Context, provided the

persisted registration is effectively Ready. HNSW requires its exact physical

index to be Ready. An existing index_kind: none registration can be Ready for

exact-scan retrieval without HNSW. A physical pgvector index without a persisted

registration is never an implicit Legacy configuration, and the retired API

cannot register or re-enable it.

How Polygres fits your application stack

Polygres focuses on managed PostgreSQL and retrieval over operational data,

with clear integration points for the rest of your application stack:

Your embedding pipeline selects the model and writes vectors with the exact

dimensions expected by the chosen retrieval configuration or collection.

Your application selects the language model for RAG and uses Polygres results

as grounded context with source identity and provenance.

Dashboard sessions, PostgreSQL credentials, and project API keys each have a

focused role and can be managed independently.

Analytical warehouses can continue serving OLAP and columnar reporting while

Polygres serves transactional and retrieval workflows.

Four fixed organization roles provide consistent team permissions.

Graph discovery proposes eligible tables and relationships for your team to

review and shape around real product questions.

Who Polygres is for

Polygres is a fit for teams that need a production PostgreSQL database and also want retrieval features close to their application data:

SaaS product teams adding search, recommendations, investigation, or AI-assisted workflows.

Data and operations teams exploring connected records without moving data into a separate graph system.

Developers building retrieval-backed application features through Python or HTTP after product setup is complete.

The dashboard is the starting point for SaaS customers. It provides organization and member management, project creation, imports, table browsing, SQL, migrations, connection details, and retrieval setup. Developers use standard PostgreSQL clients for application data and a Polygres API key for retrieval from backend code.

A concrete example

Consider a customer-support product with accounts , customers , tickets , and messages tables:

accounts account_id

▼

▼

customers customer_id → account_id

▼

tickets ticket_id → customer_id

▼

messages message_id → ticket_id

▼

incidents related through tickets

PostgreSQL serves the product’s normal ticket and customer workflows.

Graph retrieval follows relationships from an account to its customers, tickets, and incidents.

pgContext dense retrieval finds semantically similar ticket descriptions from stored embeddings.

TSVector search finds exact terms such as error codes, while Fuzzy search supports misspelled titles and short labels.

pgContext graph-composed, rank-fusion, or Joint retrieval combines semantic results with relevant graph context.

pgContext AI Search supports a collection over ticket content with filters,

point synchronization, text hybrid, graph composition, and Joint retrieval.

The data stays in the same Polygres project. Your team chooses which tables, relationships, embedding columns, text-search columns, metadata, and filters are available to retrieval.

The same support product might also add:

ALTER TABLE tickets ADD COLUMN body_embedding vector( 1536 );

During text-search setup, Polygres can create the stored generated TSVector

column and its GIN index through the existing configuration endpoint. Teams

that already maintain a compatible TSVector column can register it instead.

With that schema in place, the application continues writing normal support data to PostgreSQL while Polygres reads from the same rows for semantic similarity, full-text search, and connected-record traversal.

How Polygres compares to separate systems

Teams often evaluate Polygres against a stack of separate products: PostgreSQL for transactions, a vector store for semantic search, a graph engine for traversal, and a text-search cluster for lexical search.

Polygres is the better fit when your team wants:

one operational data store instead of multiple systems to provision, monitor, and keep in sync,

retrieval that reads the same PostgreSQL rows your application just wrote,

standard PostgreSQL tooling for schema work, imports, migrations, and day-to-day application access,

a dashboard-first workflow where product and data teams configure retrieval before developers wire it into backend code.

Separate specialized systems can still be the better choice for some workloads. If you need warehouse-style analytics, extremely large multi-tenant vector estates, or graph-heavy patterns that justify a dedicated graph engine, evaluate those systems directly. Polygres is optimized for SaaS teams that would rather not operate four different data services to answer one product question.

How you use Polygres

Use the dashboard to create and operate the SaaS workspace and configure

retrieval. Start at the organization home ( /{organization} ), create a project

from New project ( /{organization}/new ), and open the project overview

( /{organization}/{projectId} ). Query retrieval features through the CLI,

API, or Python SDK.

Use PostgreSQL connection URLs for application reads and writes, database clients, schema tools, imports, and migrations. Open connection details ( /{organization}/{projectId}/connect ) for the project.

Use the Polygres API or Python SDK for graph, text, and pgContext retrieval

from trusted application code. Existing Vector and Hybrid integrations use

their deprecated compatibility surfaces during migration. Create a project API key in

the dashboard and store the one-time value, such as poly_live_<...> , in a

secret manager or environment variable.

What to do first

Follow the Quickstart to create or join an organization, create a project, connect data, configure retrieval, and run a query. For the full customer journey, read the Core workflow .

Next steps

Product Guides

Connect and credentials

Connection examples

Load and manage data

Configure and query retrieval

Retrieval integration patterns

Reference

Routes

Error codes

pgContext API
