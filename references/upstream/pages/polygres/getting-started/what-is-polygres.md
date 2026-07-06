source: https://docs.evokoa.com/polygres/getting-started/what-is-polygres
title: What is Polygres? | Polygres
source_hash: f371ab1aea038eef7776acc6dfb40ced0cd36cd0cb074432347bbf298a407da1
discovered_from: https://docs.evokoa.com/polygres

# What is Polygres? | Polygres

What is Polygres?

Polygres is a managed PostgreSQL service with graph, vector, text, and hybrid retrieval built around the same project data. Your application can keep using PostgreSQL for normal reads and writes while your team adds richer ways to find and connect records.

The result is one operational data foundation for your SaaS product: PostgreSQL stays the source of truth, and retrieval is configured over the tables you already manage in Polygres.

One database, four retrieval modes

Mode What it helps you find

Graph Records connected through relationships, such as a customer, their account, tickets, messages, and related incidents.

Vector Records with similar meaning, based on embeddings stored in an existing fixed-dimension vector(n) column.

Text Words and phrases through TSVector full-text search, or close text matches through Fuzzy pg_trgm search.

Hybrid Results that combine graph context with vector similarity. Hybrid does not replace text search; it specifically combines graph and vector signals.

Polygres does not generate embeddings. You bring or create embeddings in your own data workflow, store them in PostgreSQL, and point a vector configuration at that column.

What Polygres does not do

Polygres has deliberate boundaries. It integrates retrieval into an operational PostgreSQL system; it does not try to replace every adjacent part of a modern SaaS stack.

It does not generate embeddings. You supply the model and embedding pipeline, then store the output in a fixed-dimension vector(n) column.

It does not host an LLM. For retrieval-augmented generation, Polygres returns context; your application chooses the model that turns that context into an answer.

It does not make dashboard sessions or PostgreSQL passwords interchangeable with the retrieval API key. Each credential has a separate job and boundary.

It does not replace an analytical warehouse for OLAP or columnar analytics workloads.

It does not support custom roles or per-member permission overrides in the current beta.

It does not infer that every discovered table or relationship belongs in graph retrieval. Auto discovery is a starting point, not an instruction to register the whole schema.

These boundaries matter because they keep Polygres focused on one job: managed PostgreSQL plus integrated retrieval over the same operational data.

Who Polygres is for

Polygres is a fit for teams that need a production PostgreSQL database and also want retrieval features close to their application data:

SaaS product teams adding search, recommendations, investigation, or AI-assisted workflows.

Data and operations teams exploring connected records without moving data into a separate graph system.

Developers building retrieval-backed application features through Python or HTTP after product setup is complete.

The dashboard is the starting point for SaaS customers. It provides organization and member management, project creation, imports, table browsing, SQL, migrations, connection details, retrieval setup, and a query workbench. Developers use standard PostgreSQL clients for application data and a Polygres API key for retrieval from backend code.

A concrete example

Consider a customer-support product with accounts , customers , tickets , and messages tables:

PostgreSQL serves the product’s normal ticket and customer workflows.

Graph retrieval follows relationships from an account to its customers, tickets, and incidents.

Vector retrieval finds semantically similar ticket descriptions from stored embeddings.

TSVector search finds exact terms such as error codes, while Fuzzy search supports misspelled titles and short labels.

Hybrid retrieval finds semantically similar tickets within relevant graph context.

The data stays in the same Polygres project. Your team chooses which tables, relationships, embedding columns, text-search columns, metadata, and filters are available to retrieval.

The same support product might also add:

ALTER TABLE tickets ADD COLUMN body_embedding vector( 1536 );

ALTER TABLE tickets ADD COLUMN body_tsv tsvector

GENERATED ALWAYS AS (to_tsvector( 'english' , body)) STORED;

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

Use the dashboard to create and operate the SaaS workspace. Start at the organization home ( /{organization} ), create a project from New project ( /{organization}/new ), and open the project overview ( /{organization}/{projectId} ).

Use PostgreSQL connection URLs for application reads and writes, database clients, schema tools, imports, and migrations. Open connection details ( /{organization}/{projectId}/connect ) for the project.

Use the Polygres API or Python SDK for graph, vector, text, and hybrid retrieval from trusted application code. Create a project API key in the dashboard and store the one-time value, such as poly_live_<...> , in a secret manager or environment variable.

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
