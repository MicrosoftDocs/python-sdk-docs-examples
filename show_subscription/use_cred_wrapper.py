# Show Azure subscription information
 
# This code uses the CredentialWrapper around DefaultAzureCredential, which
# is helpful until the management libraries are updated.
from cred_wrapper import CredentialWrapper
from azure.mgmt.resource import SubscriptionClient

credential = CredentialWrapper()
subscription_client = SubscriptionClient(credential)
subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
