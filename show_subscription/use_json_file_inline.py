# Show Azure subscription information
 
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import SubscriptionClient

subscription_client = get_client_from_auth_file(SubscriptionClient, auth_path="credentials.json")
subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
