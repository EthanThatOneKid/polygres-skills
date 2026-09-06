source: https://docs.evokoa.com/polygres/platform/projects/free-and-paid-projects
title: Free and Paid projects | Polygres
source_hash: 0254379e771fffeb6619192a86832406677066e1b17fcfa76ed9f27ad65ebaf8
discovered_from: https://docs.evokoa.com/polygres

# Free and Paid projects | Polygres

Free and Paid projects

You choose a project’s Storage, Context, and Graph limits when you create it.

The selected values determine whether Polygres creates a Free Nano project or a

Paid Basic project. One set of controls covers both choices.

Project Monthly price Database placement

Free Nano $0 Shared PostgreSQL capacity

Paid Basic From $16 An isolated PostgreSQL database

Choose Free Nano

The exact Free selection is:

Limit Free value

Storage 500 MiB

Context 100,000 points

Graph 100,000 units

New-project controls start with these values. Select Use free capacity to

return all three controls to the Free selection.

Each organization has one Free Nano project slot across hosted and synchronized

projects:

A hosted Nano project uses the slot.

A Nano project synchronized from an external PostgreSQL source uses the same

slot.

Paid Basic projects leave the Free slot available.

Deleting a Nano project or upgrading it to Basic releases the slot.

Owners, admins, and developers can create an eligible Free project. Some

existing organizations may already have more than one Nano project. Those

projects can continue running, and the organization can create another Free

project after it no longer has a Nano project.

Choose Paid Basic

Increasing any limit above the Free values switches the whole selection to the

minimum Basic limits:

Limit Included with Basic Maximum Price above the included amount

Storage 2 GiB 128 GiB $2 per additional GiB each month

Context 200,000 points 4,000,000 points $3 per additional 100,000 points each month

Graph 200,000 units 4,000,000 units $1 per additional 100,000 units each month

The minimum Basic project costs $16 per month. Storage changes in 1 GiB steps.

Context and Graph change in 100,000-unit steps. Each active Graph node uses 1

unit, and every 10 active edges use 1 unit.

For example, 3 GiB of Storage, 300,000 Context points, and 300,000 Graph units

costs $22 per month: $16 for the project, $2 for Storage, $3 for Context, and $1

for Graph.

An organization owner or admin can create a Paid project directly. If the

charge is greater than the available credit balance, the organization needs a

payment method.

Review the cost before creating a project

The new-project page shows:

the selected Storage, Context, and Graph limits;

the full monthly price;

the amount due for the first billing period;

the amount covered by available credits; and

the remainder charged to the organization’s payment method.

If a payment method is needed, Polygres opens Stripe Checkout and returns to the

saved project flow after Stripe confirms it.

The first active Paid project starts the organization’s monthly billing period

and is charged for one full month. Paid projects added later are prorated to the

same next billing date.

Billing starts after the project is ready and payment is confirmed. If

activation ends before payment succeeds, the project is not billed and

reserved credits are returned.

Create a hosted project

Open New project ( /{organization}/new ).

Choose Host with Polygres .

Adjust Storage, Context, and Graph, or keep the Free values.

Review the monthly total and the amount due for the first billing period.

Select Create free project for Nano or Create Project for Basic.

The project page shows saved provisioning progress. You can leave and return

later.

Create a synchronized project

Open New project ( /{organization}/new ).

Choose Supabase , Neon , PlanetScale , or Postgres Database .

Complete the source checks and select the tables to synchronize.

Review the estimated Context points from selected embedding tables.

Adjust Storage, Context, and Graph, or select Use free capacity .

For Nano, select Create free project . For Basic, select Review

payment , review the breakdown, and then select Create Project .

A Paid synchronized project is provisioned directly on Basic. The external

PostgreSQL database remains the source of truth for synchronized rows and

schemas. Continue making application writes and schema changes in the source.

The synchronized project dashboard focuses on synchronization and retrieval

rather than destination database connection details.

Upgrade an existing Nano project

Owners and admins can open a Nano project’s Upgrade page, choose Basic

limits, and review the charge through the next billing date. Available credits

are applied first, and the payment method covers the remainder.

For a hosted project, Polygres pauses writes, copies and verifies the database,

then switches the project to Basic. For a synchronized project, Polygres

prepares a fresh Basic copy while Nano remains active, then performs the final

switch. Plan for up to 30 minutes of paused writes near the end. Reads may also

be briefly unavailable.

The charge is collected when Basic activates. If the upgrade ends before

activation, Nano remains active and the project is not billed for Basic. Follow

the saved progress on the Upgrade page before starting another upgrade.

For source preparation and synchronization details, see Create a synced

PostgreSQL project .
