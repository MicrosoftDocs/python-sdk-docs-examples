# Show Azure subscription information
 
# This code uses the CredentialWrapper around DefaultAzureCredential, which
# is helpful until the management libraries are updated.
from cred_wrapper import CredentialWrapper
from azure.mgmt.resource import SubscriptionClient

import sys, logging

logger = logging.getLogger('azure.mgmt.resource')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

credential = CredentialWrapper()
subscription_client = SubscriptionClient(credential, logging_enabled=True)
subscription = next(subscription_client.subscriptions.list())
print(subscription.subscription_id)
