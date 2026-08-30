source: https://docs.evokoa.com/polygres/platform/projects/free-and-paid-projects
title: Free and Paid projects | Polygres
source_hash: b1d02a142ebb55834c86348cfc1f7add1d0b2b19f8154b34ee7ea63ee1355b86
discovered_from: https://docs.evokoa.com/polygres

# Free and Paid projects | Polygres

Free and Paid projects

The project plan determines its price, capacity, and database placement:

Project plan Project tier Price Database placement

Free Nano $0 Shared PostgreSQL capacity

Paid Basic From $10 per month An isolated PostgreSQL database

Availability: Paid project creation is being enabled in stages. The

new-project screen shows the plans currently available to your organization.

Launch and Scale are organization subscriptions. Nano and Basic describe an

individual project’s capacity and database placement. Each Paid project has its

own Basic capacity configuration.

See Billing and credits for subscription plans, top-ups,

payment confirmation, and credit history.

Use the free Nano project

A Free project uses the Nano tier and shared capacity. It is suitable for

getting started, evaluation, and smaller workloads. You can create one without

a paid subscription.

Each organization has one free Nano project slot across both project types:

A Polygres-hosted Nano project consumes the slot.

A Nano project synchronized from an external PostgreSQL source consumes the

same slot.

Paid Basic projects leave the Free slot available.

Deleting a Nano project makes the slot available again.

Upgrading a Nano project to Basic also releases the slot.

Some existing organizations may already have more than one Nano project. Those

projects can continue running. The organization can create another Free project

after it no longer has a Nano project.

Configure a paid Basic project

A Paid project uses the Basic tier. It starts at $10 per month and provides an

isolated PostgreSQL database with configurable Storage, Context, and Graph

capacity.

For a hosted project, Basic provides complete pooled and direct PostgreSQL

connection details. For a synced project, the external database remains the

source of truth for synchronized tables, so continue making application writes

and schema changes there. After Synced Basic is ready, the project overview also

shows the stable pooled and direct hostnames for its isolated Polygres database;

the connection details shown there are limited to those hostnames.

An organization owner or admin with an eligible subscription can create a Paid

project. The dashboard explains any subscription or availability requirement

before setup begins.

Capacity and monthly pricing

Capacity Included Maximum in project creation Price above the included amount

Storage 1 GiB 64 GiB $2 per additional GiB

Context 100,000 points 5,000,000 points $3 per additional 100,000 points

Graph 200,000 weighted units 5,000,000 weighted units $1 per additional 100,000 weighted units

Storage changes in 1 GiB increments. Context and Graph capacity change in exact

100,000-unit increments. The dashboard calculates the monthly price

from the selected capacity. Graph capacity uses weighted units: each active

node counts as 1 unit and every 10 active edges count as 1 unit.

The $10 base charge includes the minimum capacity in the table. For example, a

project configured with 2 GiB of Storage, 200,000 Context points, and 300,000

weighted Graph units costs $16 per month: $10 base, $2 for

Storage, $3 for Context, and $1 for Graph.

Understand activation and billing

The first Basic charge is collected when the project becomes ready:

Project setup itself is not billed.

The first cycle is prorated from activation through the organization’s next

subscription billing date.

Available organization credits pay the prorated charge first. Stripe bills

any remaining amount.

If setup cannot be completed, Basic billing does not begin.

Before you confirm, the dashboard shows the estimated first-cycle total, the

part covered by credits, the part paid through Stripe, and the maximum amount

you could pay. The final first-cycle charge is recalculated when Basic becomes

ready and will not exceed that maximum when the selected capacity and pricing

remain unchanged.

For a Paid synced project, Polygres temporarily sets aside the available-credit

portion shown in the payment review while setup continues. Creation works with

any available credit balance, including zero; the payment method covers the

remainder. The hold is released when the project activates or when setup ends

before activation. Hosted Basic creation starts without a temporary credit

hold.

Capacity increases are prorated, paid, and activated immediately. Capacity

decreases are scheduled for the next billing date.

Create a hosted Paid project

When direct Paid creation is available for your organization:

Open New project ( /{organization}/new ).

Choose Paid .

Choose Host with Polygres .

Configure Storage, Context, and Graph capacity.

Review the monthly total and first-cycle billing notice.

Select Create Project and review the displayed maximum charge.

The project page shows saved provisioning progress. You can leave the page and

return later. Billing begins when the isolated Basic database is ready.

Create a Paid synchronized project

When direct Paid synchronized-project creation is available for your

organization:

Open New project ( /{organization}/new ) and choose Paid .

Choose Supabase , Neon , PlanetScale , or Postgres Database .

Complete the source checks and select the tables to synchronize.

Review the estimated Context points from selected embedding tables.

Configure Storage, Context, and Graph capacity.

Select Review payment , check the credit and payment-method amounts, then

select Create Project .

Polygres establishes synchronization and activates Basic automatically. Your

credit balance can cover any portion of the first charge, including none of it;

the payment method covers the remainder.

The project keeps its identity and synchronization settings. Near completion,

Polygres may pause writes for up to 30 minutes while it applies the latest

source changes. Reads may also pause briefly.

The external PostgreSQL source remains authoritative throughout setup. If the

dashboard reports that setup needs attention, follow its guidance or contact

support with the displayed error code before trying again.

Upgrade an existing Nano project

Owners and admins can open a Nano project’s Upgrade page, choose Basic

capacity, and review the estimated first-cycle charge. The dashboard shows how

much available credit will be used and how much will be paid through Stripe.

For a hosted project, Polygres pauses writes, copies and verifies the database,

then switches the project to Basic. For a synced project, Polygres prepares a

fresh synchronized copy while the current project remains active, then performs

the final switch. Plan for up to 30 minutes of paused writes near the end;

reads may also be briefly unavailable.

The charge is collected when Basic is activated. If the upgrade cannot reach

activation, the project remains on Nano and is not charged. Follow the saved

progress on the Upgrade page instead of starting another upgrade.

For source preparation and synchronization details, see Create a synced

PostgreSQL project .
