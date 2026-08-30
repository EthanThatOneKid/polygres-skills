source: https://docs.evokoa.com/polygres/platform/billing
title: Billing and credits | Polygres
source_hash: 98e4ca99b1e1e59a7d9cb7dc447e152ec53cd10431b4e900315c8dfffc51dc76
discovered_from: https://docs.evokoa.com/polygres

# Billing and credits | Polygres

Billing and credits

Billing belongs to the organization, not to an individual project or member.

Organization owners and admins can open Billing in the dashboard to view or

manage the subscription, credit balance, top-ups, invoices, and payment

methods. Developers and viewers can ask an owner or admin to make billing

changes for the organization.

Understand credits

One Polygres credit represents one US cent. The dashboard displays credit

amounts as USD, so 1,000 credits appear as $10.00.

Subscription credits and purchased credits do not expire. Unused credits roll

over between billing cycles. Promotional credits can expire, and the dashboard

shows their expiration date. When credits are used, credits with the earliest

expiration are applied before balances that expire later or never expire.

On each billing date, Polygres adds the plan’s monthly credits before charging

Paid projects. Those credits can therefore help pay the same billing date’s

project charges. Polygres uses available organization credits first, then

Stripe bills any remaining amount.

Choose an organization plan

The dashboard offers these organization subscription plans:

Plan Monthly price Credits after each paid renewal

Launch $16 $10

Scale $256 $260

The subscription plans differ in price and monthly credit grant. Paid-project

pricing and included project capacity do not change between Launch and Scale.

To subscribe:

Open Billing for the organization.

Review the available plans and select Subscribe for the plan you want.

Complete payment in Stripe Checkout.

Return to Billing and wait for the subscription and credit balance to

update.

After Checkout, Polygres updates the subscription and credit balance when

Stripe confirms payment. Keep the Billing page open or return to it later if

confirmation is still pending.

Use Payment methods and invoices on the Billing page to open the Stripe

billing portal.

Change plans

Upgrade from Launch to Scale

The dashboard shows the prorated amount due and the estimated additional credit

grant before you confirm an upgrade. Scale becomes active and the additional

credits appear after Stripe confirms payment.

Schedule a downgrade from Scale to Launch

A Scale-to-Launch downgrade takes effect on the organization’s next billing

date. Scale remains active through the current period, and existing credits

remain available. Launch pricing and credits begin with the first paid Launch

renewal.

The Billing page shows a pending plan change and its effective date after the

downgrade is scheduled.

Buy a credit top-up

Credit top-ups are one-time purchases made through Stripe Checkout. They are

available while the organization has an active, paid subscription:

Choose one of the displayed fixed offers, or enter a custom amount when a

custom offer is available.

Review the purchased-credit amount, any promotional bonus, and its

expiration terms.

Continue to Stripe Checkout and complete payment.

Return to Billing and wait for the credit balance and purchase history to

update.

Purchased credits never expire. Promotional bonus credits are recorded

separately and show their own expiration date. If a refund or payment dispute

affects a purchase, Polygres adjusts the related credits to match the final

payment outcome.

Top-up amounts and promotional bonuses can change. Review the current amount,

minimum, increment, bonus, and expiration in Billing before each purchase.

Purchased and promotional credits appear after Stripe confirms the top-up

payment.

Manage Paid-project capacity

Billing shows each Paid project’s current Storage, Context, and Graph capacity,

plus any capacity change already scheduled. Owners and admins can configure a

new capacity from the project’s Upgrade page. The project card in Billing

links to the same page.

When the selected monthly price is higher, the dashboard shows the new monthly

price and the prorated amount due now. Available credits pay part or all of that

amount, and Stripe bills the remainder. The additional capacity becomes active

after payment succeeds.

When the selected monthly price is lower, the change is scheduled for the next

organization billing date. The current capacity remains active until then.

Current usage and active work must fit within every lower limit when you

schedule the change and when it takes effect. If cleanup is required, the

dashboard shows how much usage to remove before you try again.

If a selection raises the total monthly price while lowering one capacity

value, Polygres treats it as an increase. The lower value must already fit the

project’s current usage and active work.

Review billing and credit history

The Billing page shows:

The available credit balance, current subscription, next billing date, and

billing status.

Credit history, including subscription grants, top-up grants, promotional

credit expiration, Paid-project charges, and payment adjustments.

Top-up purchase history, including purchased and promotional amounts,

payment status, bonus expiration, and any refund or dispute status.

Current and pending Storage, Context, and Graph capacity for each Paid

project.

If a purchase is marked for support review, monitor its status in Billing and

contact support if it remains unchanged.

Continue

Review organizations as the ownership boundary for

projects, members, billing, and credits.

Review roles and permissions before

granting organization access.

Compare Free and Paid projects ,

including Basic capacity and billing.

Learn how to create and manage projects .
