# Show Azure subscription information
 
import os
from azure.mgmt.resource import SubscriptionClient
from azure.identity import EnvironmentCredential

# EnvironmentCredential assumes that the following environment variables are set:
#     AZURE_TENANT_ID
#     AZURE_CLIENT_ID
#
# Plus one of the following (which are attempted in this order):
#     AZURE_CLIENT_SECRET
#  or:
#     AZURE_CLIENT_CERTIFICATE_PATH
#  or:
#     AZURE_USERNAME and AZURE_PASSWORD

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

credential = EnvironmentCredential()

subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
