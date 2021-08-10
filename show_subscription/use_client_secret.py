# Show Azure subscription information

import os
from azure.mgmt.resource import SubscriptionClient
from azure.identity import ClientSecretCredential

# Retrieve the IDs and secret to use with ClientSecretCredential. NOTE: this code uses
# environment variables for convenience instead of retrieving the values from another source
# such as Azure Storage or Azure Key Vault. If you already have values in environment
# variables, just use EnvironmentCredential.

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]
client_id = os.environ["AZURE_CLIENT_ID"]
client_secret = os.environ["AZURE_CLIENT_SECRET"]

credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)