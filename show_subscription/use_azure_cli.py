# Show Azure subscription information

from azure.identity import AzureCliCredential
from azure.mgmt.resource import SubscriptionClient

credential = AzureCliCredential()
subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
