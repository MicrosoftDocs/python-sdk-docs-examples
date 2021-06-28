# Show Azure subscription information
 
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import SubscriptionClient

credential = DefaultAzureCredential()
subscription_client = SubscriptionClient(credential)

sub_list = subscription_client.subscriptions.list()
print(list(sub_list))
