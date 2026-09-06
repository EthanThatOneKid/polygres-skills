source: https://docs.evokoa.com/polygres/mcp/confirm-actions
title: Review and confirm MCP actions | Polygres
source_hash: 005dd88d82c35d0f7a632189926908989e220cefb5b89589eee708ffc373e139
discovered_from: https://docs.evokoa.com/polygres

# Review and confirm MCP actions | Polygres

Review and confirm MCP actions

Polygres gives important MCP changes a two-step review. Your AI client first

prepares the action, then shows you the exact project, tool, and arguments.

The confirmation flow

The client calls the change tool with the proposed arguments.

Polygres returns status: action_required with the proposed action and an

action_digest .

The client presents that action for your approval.

After you approve it, the client repeats the same call with the confirmation

object supplied by Polygres.

Polygres matches the digest to the exact action and runs it.

The confirmation object has this shape:

{

"confirmation" : {

"confirmed" : true ,

"action_digest" : "<digest returned by Polygres>"

}

}

The digest belongs to one exact tool call. A change to the project, target, or

arguments produces a fresh action review.

Action classes

Class Examples What the review highlights

Write Create a collection, configure graph, retry synchronization Target and configuration

Destructive Delete points, delete a collection, cancel an import, resnapshot sync Data or state affected

Resource intensive Backfill Context points, build graph, run graph maintenance Expected work and project impact

External financial Upgrade project capacity Quote, maximum charge, and capacity change

upsert_row is a bounded one-record write that runs directly under the write

permission granted to the connection. When the request also reconciles AI

Search, it supplies an idempotency key for safe replay.

Idempotency keys

Keep the same idempotency key when you repeat the same intended action after a

connection timeout or an uncertain response. Use a fresh key for a new action.

This lets Polygres return the earlier result when the first request already

completed.

Durable operations

Collection work, graph builds, imports, and synchronization can continue after

the first response. Keep the returned operation ID and use

wait_for_operation or the matching status tool. A timeout means the client

finished its current watch period; the latest operation state remains available

for the next status check.
