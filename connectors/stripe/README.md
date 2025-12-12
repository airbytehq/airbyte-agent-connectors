# Airbyte Stripe AI Connector

Stripe is a payment processing platform that enables businesses to accept payments,
manage subscriptions, and handle financial transactions. This connector provides
access to customers for payment analytics and customer management.


## Example Questions

- Show me my top 10 customers by total revenue this month
- List all customers who have spent over $5,000 in the last quarter
- Analyze payment trends for my Stripe customers
- Identify which customers have the most consistent subscription payments
- Give me insights into my customer retention rates
- Summarize the payment history for [customerX]
- Compare customer spending patterns from last month to this month
- Show me details about my highest-value Stripe customers
- What are the key financial insights from my customer base?
- Break down my customers by their average transaction value

## Unsupported Questions

- Create a new customer profile in Stripe
- Update the billing information for [customerX]
- Delete a customer record
- Send a payment reminder to [customerX]
- Schedule an automatic invoice for [Company]

## Installation

```bash
uv pip install airbyte-ai-stripe
```

## Usage

```python
from airbyte_ai_stripe import StripeConnector, StripeAuthConfig

connector = StripeConnector(
  auth_config=StripeAuthConfig(
    token="..."
  )
)
result = connector.customers.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Customers | [List](./REFERENCE.md#customers-list), [Get](./REFERENCE.md#customers-get) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Stripe API Reference](https://docs.stripe.com/api).

## Version Information

**Package Version:** 0.5.9

**Connector Version:** 0.1.1

**Generated with connector-sdk:** 4d366cb586482b57efd0c680b3523bbfe48f2180