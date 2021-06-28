# Show Azure subscription information

from azure.identity import DeviceCodeCredential
from azure.mgmt.resource import SubscriptionClient

credential = DeviceCodeCredential()
subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
