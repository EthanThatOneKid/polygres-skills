source: https://docs.evokoa.com/polygres/platform/automatic-embeddings
title: Automatic embeddings | Polygres
source_hash: 138721f2018346b188b488fdb497e52be6b9a1bb8923527398d3dda9755ceba7
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

A configuration saves your selected source, model, and generation settings.

A default model is selected for you. Select Change to choose another model,

or expand Additional settings to change dimensions, update mode, or chunking.

Choose how to handle long text

Each embedding model accepts a maximum amount of text at a time, measured in

tokens . A token can be a word, part of a word, or punctuation. The dashboard

shows the selected model’s token limit under automatic chunking.

Chunking splits the text in a row into smaller parts and generates an

embedding for each part. Your original row and text stay unchanged. For example,

a long article in one row can have several embeddings, so search can find the

relevant passage within that article.

Choose one of these settings under Additional settings :

Setting When to use it What happens

Automatic (recommended) The default for new generation configurations Text within the model’s limit gets one embedding. Longer text is split into chunks that fit the model.

Custom chunk size You want to search smaller passages, even when the full text fits the model Choose Tokens per chunk and Overlap tokens . Overlap repeats some text between adjacent chunks to preserve context.

Off You want one embedding per row and know the text fits the model Text above the model’s limit fails generation for that row.

Automatic chunking applies both to existing rows during setup and to later text

changes, including synchronized updates. Polygres calculates the chunk sizes for

you. Existing configurations keep their saved chunking settings.

Choose when to process changes

For future text changes, choose:

Automatic processes changes as they arrive.

Manual collects changes until you select Run now .

Both modes process the existing text when you start the configuration. Manual

mode only changes when later updates are processed.

Reuse existing embeddings

If your table already has a vector column, select Use existing embeddings and

confirm the model, version, dimensions, and settings used to create those vectors.

Polygres copies compatible embeddings and generates any that are missing. Later

generation follows changes to your text column; editing the original vector

column does not update the copied embeddings.

Chunking is off when copying existing embeddings. If you enable chunking during

setup, confirm that Polygres should generate new embeddings for the chunks.

Review and start

Select Review and start to see how many embeddings can be reused, how many

will be generated, and the estimated token, storage, and credit usage. Review

the model and dimensions, then select Create and start . The estimate samples

up to 200 rows and 8 MiB of source data. Actual usage depends on the text processed

and the number of chunks generated.

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

Search text limits

The question or phrase you send to search must meet both limits:

Limit Maximum

Search request 131,072 characters in the text field

Embedding model The selected model’s max_input_tokens , including any required model instructions

Run polygres --project PROJECT embeddings models to check your model’s token

limit. Token counts depend on the language and wording, so text below the

character cap can still exceed the model’s limit.

Polygres converts your search text into one embedding. Automatic chunking applies

to the text in your table. If a search is rejected because its text is too long,

shorten the question or remove unnecessary pasted context and try again.

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

Set up embeddings with the CLI

Use CLI 0.6.0 or newer for this setup and the recovery and monitoring commands

below. Install or upgrade the CLI

and sign in first. Replace PROJECT with your project ID in these examples.

1. Choose a source and model

polygres --project PROJECT embeddings sources

polygres --project PROJECT embeddings models

2. Save the configuration

Create a file named configuration.json . This example uses an articles table

with id and body columns. Replace the source fields with your table’s details,

replace CATALOG_MODEL_UUID with the model ID from the previous command, and

choose a dimension count that the model supports.

{

"name" : "Articles" ,

"source_schema" : "public" ,

"source_table" : "articles" ,

"source_key_columns" : [ "id" ],

"source_text_column" : "body" ,

"model_id" : "CATALOG_MODEL_UUID" ,

"dimensions" : 1536 ,

"mode" : "automatic" ,

"chunking" : { "mode" : "automatic" },

"use_credits" : false

}

Here, mode controls when text changes are processed. chunking.mode controls

how long text is split. Both are set to automatic.

3. Preview, then start generation

polygres --project PROJECT embeddings preview --file configuration.json --summary

Review the estimate, then create the configuration:

polygres --project PROJECT embeddings create --file configuration.json --idempotency-key setup-articles-v1

Copy the returned configuration id and use it in place of CONFIGURATION_ID :

polygres --project PROJECT embeddings get CONFIGURATION_ID --summary

See Watch generation progress

to wait for processing to finish. If you retry the same creation request, reuse

its idempotency key. Use a new key for a different configuration.

4. Set up search

Run this command for the source details needed to

create a Context collection :

polygres --project PROJECT embeddings context CONFIGURATION_ID

You can also select Configure search in the dashboard. Creating embeddings

does not create the search collection. Once your collection is Ready , search

it by name:

polygres --project PROJECT context search articles --text "How do I reset access?"

Replace articles with your collection’s name. See

Context retrieval for filters, query files, and

other search options.

Use MCP

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

If processing needs attention, the configuration explains the problem. Follow

the displayed action, such as reviewing spending settings or viewing affected

rows, then select Resume when offered. Delayed requests are recovered

automatically. Requests flagged for investigation need further checks by Polygres.

Retry rows whose text is too long

If source text exceeds the model’s input limit, a user who can manage the

configuration can enable chunking and retry the affected rows:

Open the affected configuration and select Review automatic chunking .

In Enable automatic chunking? , review the model’s token limit, the failed

rows that can be retried, example chunk counts, and any rows that cannot be fixed

by chunking. Additional chunks use more tokens and storage.

Select Enable and retry failed rows . This enables automatic chunking for

future text changes and queues the failed rows that chunking can fix. Rows

with completed embeddings are not regenerated.

If the configuration is paused, select Resume when you are ready. Watch

generation progress and any pending Context updates. The recovered rows become

searchable after their embeddings and search updates finish.

If chunking cannot fix any of the failed rows, the confirmation button is disabled

and your settings stay unchanged. Use View affected rows to find the source

text to review, and check the row limits .

If Polygres cannot confirm whether a previous request completed, that row is

excluded from this retry while recovery or investigation continues. This action

requires a configuration that generates new embeddings from text.

Remove a configuration

When removing a configuration, choose whether to keep or delete its generated

embeddings. To delete the embeddings, first remove any Context collections that

use them. Your original source columns are preserved with either choice.

Limits for each row

For embedding generation, a source row must fit within 4 MiB when represented as

JSON. This includes every column in the row. Its selected text can produce up to

1,024 chunks.

If a row exceeds these limits, shorten its content or split it across multiple

rows. If you use custom chunking, reducing overlap can also reduce the number of

chunks. The preview helps estimate generation; it does not check every row.

Retry long text with the CLI

Use embeddings recover-oversized in CLI 0.6.0 to enable automatic chunking and

retry failed rows from your terminal. It follows the same rules as dashboard

recovery. See Retry rows whose text is too long

for the preview and confirmation commands.
