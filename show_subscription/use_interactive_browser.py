# Show Azure subscription information

import os
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource import SubscriptionClient

credential = InteractiveBrowserCredential()
subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
