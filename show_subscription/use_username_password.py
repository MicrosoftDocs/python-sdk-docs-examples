# Show Azure subscription information

import os
from azure.mgmt.resource import SubscriptionClient
from azure.identity import UsernamePasswordCredential

# Retrieve the information necessary for the credentials, which are assumed to
# be in environment variables for the purpose of this example.
client_id = os.environ["AZURE_CLIENT_ID"]
tenant_id = os.environ["AZURE_TENANT_ID"]
username = os.environ["AZURE_USERNAME"]
password = os.environ["AZURE_PASSWORD"]

credential = UsernamePasswordCredential(client_id=client_id, tenant_id = tenant_id,
    username = username, password = password)

subscription_client = SubscriptionClient(credential)

subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)