# Show Azure subscription information

from azure.identity import VisualStudioCodeCredential
from azure.mgmt.resource import SubscriptionClient

credential = VisualStudioCodeCredential()
subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
