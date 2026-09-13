source: https://docs.evokoa.com/polygres/platform/automatic-embeddings
title: Automatic embeddings | Polygres
source_hash: 303ba018a0869d4152513e1afd2cbaa9fc387b369e8c9f93c1a85bae6ea4f1ce
discovered_from: https://docs.evokoa.com/polygres

# Automatic embeddings | Polygres

Automatic embeddings

Automatic embeddings make your text searchable by meaning. Choose a text column

and a model, and Polygres generates the embeddings and keeps them up to date as

your text changes.

Generated embeddings live alongside your data in the project database.

Your original columns stay as they are.

Set up a source

Open Embeddings in your project. Select the table, the text column to embed,

and a row identifier such as id . The identifier must be unique and have a value

in every row. You can select several columns that together identify a row.

A default model is selected for you. Select Change to choose another model,

or expand Additional settings to change dimensions, update mode, or chunking.

When the table has vector columns, select Use existing embeddings and confirm

the model, version, dimensions, and settings used to create them. Polygres copies

compatible embeddings during setup and generates the rest. After that, it keeps

its own embeddings in sync with the text column; changes to the original vector

column stay in that column.

For longer text, turn on chunking to split each document into smaller passages.

Choose a size in tokens and an overlap to keep context between passages. This

option generates new embeddings for each passage, including when you already

have embeddings for the whole document. Review and confirm this choice during

setup.

Choose how to process future text changes:

Automatic processes changes as they arrive.

Manual collects changes until you select Run now .

Both modes start by processing the existing text. Polygres manages the batch

sizes for you.

Select Review and start to see how many embeddings can be reused, how many

will be generated, and the estimated token, storage, and credit usage. Review

the model and dimensions, then select Create and start . Estimates use a

sample of your data; final usage reflects the tokens actually processed.

Model availability

Your configuration keeps the model version and dimensions you selected during

setup. To try another model or number of dimensions, create a new configuration.

The model list shows the options available for new configurations. Existing

configurations can continue using a retired model. If a model is temporarily

disabled, saved embeddings are retained, and generation can resume with a retry

after the model is reactivated.

Quota and credits

Your project includes separate allowances for generating embeddings from source

text and from search queries:

Project Generation allowance Retrieval allowance Renewal

Free and existing Starter projects $5 $5 First day of each month at 00:00 UTC

Other paid projects $10 $10 Each project billing period

A paid project’s first period starts at activation and receives the full

allowance through its next billing renewal. Upgrading between paid tiers keeps

your current allowance and usage. Each renewal replaces the previous period’s

remaining allowance with a fresh allowance.

Starter projects with an active paid allowance keep it through the current

period, then receive the Free allowance.

Costs use the model provider’s published input price, with zero markup. Open

Billing/Usage to see dollars used and available, your renewal date, and token

counts and prices for each model. Amounts marked reserved cover requests

that are still processing or awaiting confirmation of their usage.

An organization owner or administrator can enable additional usage and set a

project spending limit per billing cycle . You can then allow individual

embedding configurations or queries to use organization credits at one credit

per US cent. Polygres adds up fractional usage before rounding the total charge

up to a whole credit.

When an allowance or spending limit is reached, continue after it renews or ask

an owner or administrator to authorize more spending. Your saved embeddings

remain available.

Create AI Context and search

Once embeddings are available, select Configure search to create a Context

collection using them. Choose your text search options, filters, and result

columns, then wait for the collection to be ready. In synchronized projects, this

setup uses the generated embeddings in Polygres and preserves your source

database schema.

Use the Python SDK, CLI, or MCP to search the collection with a question or

phrase. Polygres embeds the query with your configured model and dimensions,

using the retrieval allowance. Results include matching passages and their

source row identifiers, with your collection filters and row access permissions

applied.

Search follows your latest text. When the text changes, its previous embedding is

set aside and the updated text becomes searchable once its new embedding is

ready. Deleting a row or clearing its text also removes its search results.

Changes to other source fields appear in results while reusing the existing

embeddings.

Python SDK

After configuring embeddings and creating the collection, use SDK 0.5.0 or newer

to query it from your application:

results = project.context.search(

"articles" ,

text = "How do I reset access?" ,

)

for result in results.results:

print (result.properties)

This uses the collection’s default vector and its saved embedding model.

Pass vector_name to choose another vector in the collection. Manage generation

through the dashboard, CLI, or MCP. See the

Python SDK guide for client setup, query

options, and credit usage.

CLI and MCP

Use CLI 0.5.0 or newer to set up embeddings from your terminal:

polygres --project PROJECT embeddings sources

polygres --project PROJECT embeddings models

polygres --project PROJECT embeddings preview --file configuration.json

polygres --project PROJECT embeddings create --file configuration.json --idempotency-key setup-articles-v1

polygres --project PROJECT embeddings list

polygres --project PROJECT embeddings context CONFIGURATION_ID

Run embeddings context to get the source details for

creating a Context collection , or select

Configure search in the dashboard. Once the collection is Ready , search

it by name:

polygres --project PROJECT context search articles --text "How do I reset access?"

See Context retrieval to choose a vector, apply

filters, read questions from a file, or set retry options.

For an articles table with id and body columns, configuration.json looks

like this:

{

"name" : "Articles" ,

"source_schema" : "public" ,

"source_table" : "articles" ,

"source_key_columns" : [ "id" ],

"source_text_column" : "body" ,

"model_id" : "CATALOG_MODEL_UUID" ,

"dimensions" : 1536 ,

"mode" : "automatic" ,

"use_credits" : false

}

Use embeddings models to choose the model ID and supported dimensions for your

configuration.

With a Polygres MCP connection , ask your AI client to choose a source,

preview generation, set up embeddings, or search your text. Enable the Context

feature group to access these tools, and review configuration changes before

confirming them. See MCP embedding tools

for the available commands. Searches use the query allowance, with organization

credits available when you enable them.

Pause, recover, or remove

Open a configuration to check embedding progress and search updates. Use

Pause and Resume to control generation, or Run now to process pending

changes.

If processing needs attention, follow the guidance in its status and select

Retry . Reconcile checks previous attempts and recovers saved results.

Some requests may need an administrator to confirm their model usage before

processing continues.

When removing a configuration, choose whether to keep or delete its generated

embeddings. To delete the embeddings, first remove any Context collections that

use them. Your original source columns are preserved with either choice.

Working with large documents

Each source record can contain up to 4 MiB of JSON, and each document can produce

up to 1,024 chunks. For larger content, split it into smaller records or reduce

the overlap between chunks. Preview uses a sample of up to 200 rows and 8 MiB of

source records to help you estimate usage before starting.
