import os
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.identity import DefaultAzureCredential, AzureAuthorityHosts

authority = AzureAuthorityHosts.AZURE_CHINA
resource_manager = "https://management.chinacloudapi.cn"

# Set environment variable AZURE_SUBSCRIPTION_ID as well as environment variables
# for DefaultAzureCredential. For combinations of environment variables, see
# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#environment-variables
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# When using sovereign domains (that is, any cloud other than AZURE_PUBLIC_CLOUD),
# you must use an authority with DefaultAzureCredential.
credential = DefaultAzureCredential(authority=authority)

resource_client = ResourceManagementClient(
    credential, subscription_id,
    base_url=resource_manager,
    credential_scopes=[resource_manager + "/.default"])

subscription_client = SubscriptionClient(
    credential,
    base_url=resource_manager,
    credential_scopes=[resource_manager + "/.default"])
 