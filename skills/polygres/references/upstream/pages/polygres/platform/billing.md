source: https://docs.evokoa.com/polygres/platform/billing
title: Billing and credits | Polygres
source_hash: 32dbf4756fd03fb447caa85a7613c019505ab8127939da3af1dfb49a20a4a2ec
discovered_from: https://docs.evokoa.com/polygres

# Billing and credits | Polygres

Billing and credits

Billing belongs to the organization. Organization owners and admins can open

Billing to manage payment methods, credits, top-ups, paid projects, and

invoices. Developers and viewers can ask an owner or admin to make a billing

change.

Understand the account category

Billing shows the organization as Free until its first Paid project becomes

active. An organization with at least one active Paid project is shown as

Launch .

Launch is a display-only account category derived from active Paid projects.

Project limits and charges come from each project’s selected Storage, Context,

and Graph limits.

Add a payment method

A payment method is needed when a project charge is greater than the available

credit balance.

Open Billing .

Select Add payment method or Update payment method .

Complete the secure Stripe Checkout flow.

Return to Polygres. Billing updates after Stripe confirms the saved payment

method.

You can also be sent to Stripe while creating a Paid project. After the payment

method is confirmed, Polygres returns to the project flow and continues with

the saved selection.

Use Invoice portal to manage the payment method and open Stripe invoice

documents.

Understand credits

One Polygres credit represents one US cent. The dashboard displays credits as

USD, so 1,000 credits appear as $10.00.

Purchased credits do not expire. Promotional credits can expire, and Billing

shows their expiration date. Existing credits continue to roll over between

billing periods. Polygres uses credits with the earliest expiration first.

For every Paid-project charge, available credits are applied before the

organization’s payment method. Billing and Stripe invoices show the project

charge, the credit applied, and the remaining amount paid through Stripe.

Buy a credit top-up

Credit top-ups are one-time purchases through Stripe Checkout. Owners and

admins can buy one before or after creating a Paid project.

Choose a fixed offer, or enter a custom amount when that option is shown.

Review the purchased credits, promotional bonus, and expiration terms.

Select the payment action and complete Stripe Checkout.

Return to Billing and wait for the balance and purchase history to update.

Purchased credits never expire. Promotional bonus credits appear separately

with their expiration date. If a refund or payment dispute changes a purchase,

Polygres updates the related credits to match the final payment result.

Offers can change. Review the amount, minimum, increment, bonus, and expiration

shown in Billing before each purchase.

Understand when projects are charged

The first Paid project establishes the organization’s monthly billing date and

is charged for one full month when it activates. A later Paid project is charged

from its activation time through the organization’s next billing date.

At each renewal, one organization invoice lists every active Paid project and

its selected Storage, Context, and Graph limits. Available credits reduce the

invoice before the remaining amount is charged to the payment method.

Billing starts after the project is ready and payment is confirmed. If

activation ends before payment succeeds, reserved credits are returned and the

project is not billed.

Deleting a Paid project does not create a prorated refund. The project is left

off invoices for later billing periods. When no active Paid projects remain,

the organization returns to the Free category, and the current billing period

closes on its scheduled date.

Increase or reduce a Paid project’s limits

Billing lists every Paid project’s current monthly amount and selected Storage,

Context, and Graph limits. Open the project’s Upgrade page to change them.

When any selected limit increases, the dashboard shows the monthly price and

the prorated difference due through the next billing date. Available credits

are applied first. The higher limits become active after payment succeeds.

When all changes are decreases, the lower limits and monthly price begin on the

next billing date. Current usage and active work must fit within each lower

limit. The dashboard explains how much cleanup is needed before you try again.

A selection with both increases and decreases is treated as an increase. Every

lower value must already fit the project’s current usage and active work.

Review billing history

Billing shows:

the available credit balance, account category, and next billing date;

payment-method setup and the Stripe invoice portal;

current and scheduled limits for each Paid project;

invoice history with amount, status, and document links;

top-up purchase history and promotional bonus details; and

credit history, including purchases, promotions, Paid-project charges,

expirations, refunds, and payment adjustments.

If a payment or purchase is marked for review, monitor its status in Billing

and contact support if it remains unchanged.

Continue

Compare Free and Paid projects .

Learn how to create and manage projects .

Review roles and permissions before

granting organization access.
