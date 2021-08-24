# Show Azure subscription information
 
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import SubscriptionClient

# This form of get_client_from_auth_file relies on the AZURE_AUTH_LOCATION
# environment variable.
subscription_client = get_client_from_auth_file(SubscriptionClient)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
